import keysight_kt33000 as ks
import numpy as np
from typing import Literal
import datetime
import random
import time
from FuncGen_Selector_Function_2 import func_gen_control

# d188.py — minimal ctypes bridge for DGD188API.DLL (Windows) — fixed prototypes to allow None
import ctypes as C
from ctypes import wintypes as W

# --- Load the DLL (stdcall) ---
lib = C.WinDLL("DGD188API.DLL")  # WinDLL = stdcall

# --- Function prototypes (callbacks as void* so we can pass None) ---

lib.DGD188_Initialise.argtypes = [C.POINTER(W.INT), C.POINTER(W.INT), C.c_void_p, C.c_void_p]
lib.DGD188_Initialise.restype = W.INT

lib.DGD188_Update.argtypes = [
    W.INT, C.POINTER(W.INT),
    C.c_void_p, W.INT,
    C.c_void_p, C.POINTER(W.INT),
    C.c_void_p, C.c_void_p
]
lib.DGD188_Update.restype = W.INT

lib.DGD188_Close.argtypes = [C.POINTER(W.INT), C.POINTER(W.INT), C.c_void_p, C.c_void_p]
lib.DGD188_Close.restype = W.INT


class DEVHDR(C.Structure):
    _fields_ = [("DeviceCount", W.INT)]


class D188STATE_T(C.Structure):
    _fields_ = [
        ("D188_Mode", C.c_uint8),
        ("D188_Select", C.c_uint8),
        ("D188_Indicator", C.c_uint8),
        ("D188_Delay", C.c_uint16),
    ]
    _pack_ = 1


class D188DEVICESTATE_T(C.Structure):
    _fields_ = [
        ("D188_DeviceID", W.INT),
        ("D188_VersionID", W.INT),
        ("D188_Error", W.INT),
        ("D188_State", D188STATE_T),
    ]


def read_device_count(buf):
    return DEVHDR.from_buffer_copy(buf).DeviceCount


def device_at_mutable(buf, index):
    base = C.addressof(buf)
    offset = C.sizeof(DEVHDR) + index * C.sizeof(D188DEVICESTATE_T)
    return C.cast(base + offset, C.POINTER(D188DEVICESTATE_T))


def D188_Controller(channel=1, light=1):
    """
    Channel = channel # on D188,
    Light = 1 (on), 0 (off)
    """

    channel = channel - 1

    ref = W.INT(0)
    err = W.INT(0)

    r = lib.DGD188_Initialise(C.byref(ref), C.byref(err), None, None)
    if r != 0 or err.value != 0:
        print(f"Initialise failed: ret={r} apiErr={err.value}")
        return

    try:
        cb = W.INT(0)
        r = lib.DGD188_Update(
            ref, C.byref(err),
            None, 0,
            None, C.byref(cb),
            None, None
        )
        if r != 0 or cb.value <= 0:
            print(f"Size probe failed: ret={r} apiErr={err.value} cb={cb.value}")
            return

        buf = C.create_string_buffer(cb.value)
        r = lib.DGD188_Update(
            ref, C.byref(err),
            None, 0,
            C.addressof(buf), C.byref(cb),
            None, None
        )
        if r != 0 or err.value != 0:
            print(f"Read state failed: ret={r} apiErr={err.value}")
            return

        devs = read_device_count(buf)
        print(f"Found {devs} device(s).")
        if devs == 0:
            return

        dev0_ptr = device_at_mutable(buf, 0)
        dev0 = dev0_ptr.contents
        print(f"Before: Mode={dev0.D188_State.D188_Mode} Select={dev0.D188_State.D188_Select}")

        dev0.D188_State.D188_Mode = 1
        dev0.D188_State.D188_Indicator = light
        dev0.D188_State.D188_Select = 1 << channel

        r = lib.DGD188_Update(
            ref, C.byref(err),
            C.addressof(buf), cb,
            C.addressof(buf), C.byref(cb),
            None, None
        )
        if r == 0 and err.value == 0:
            print("Channel set to 1 on device 0.")
        else:
            print(f"Write failed: ret={r} apiErr={err.value}")

    finally:
        lib.DGD188_Close(C.byref(ref), C.byref(err), None, None)


def current_calc(desired_current, input_volts, output_current):
    vs = (desired_current * input_volts) / output_current
    return vs


def _stop_requested(stop_event) -> bool:
    return stop_event is not None and stop_event.is_set()


def _sleep_with_stop(duration_s: float, stop_event=None, chunk_s: float = 0.01) -> bool:
    """
    Sleep cooperatively so Stop requests can be handled quickly.
    Returns True if stopped during the wait, else False.
    """
    if duration_s <= 0:
        return _stop_requested(stop_event)
    
    print ("[_sleep_with_stop] started")

    end_time = time.monotonic() + duration_s
    while time.monotonic() < end_time:
        if _stop_requested(stop_event):
            return True
        remaining = end_time - time.monotonic()
        print(f"\rRemaining time: {remaining:6.2f} s", end="", flush=True)
        time.sleep(min(chunk_s, max(0.0, remaining)))
    print ("[_sleep_with_stop] Ended")
    print("\n")
    return _stop_requested(stop_event)

def _estimated_run_time(num_stims, freq):

    run_time = (num_stims - 1) / freq

    return run_time



def burst_mode(
    interpulse_delay=0,   # ms
    interstim_delay=1,    # seconds
    num_stims=10,
    jitter=False,
    jitter_rate=0,        # seconds
    burst_cycles=1,
    ch2_state=0,
    ch2_delay=0,
    ch1_ttl=True,
    ch2_ttl=False,
    rand_freq = False,
    rand_freq_upper = 0,
    rand_freq_lower = 0,
    *,
    fg_ch1: dict | None = None,
    fg_ch2: dict | None = None,
    stop_event=None,
):
    """
    Configure and trigger paired-pulse burst-mode output on a Keysight 33512B.

    stop_event:
        Optional threading.Event-like object. If set, the function exits early
        and performs cleanup before returning.
    """
    assert interstim_delay > 0, "interstim_delay must be > 0 seconds"
    assert num_stims >= 1, "num_stims must be >= 1"
    assert jitter_rate >= 0, "jitter_rate must be >= 0 seconds"
    assert jitter_rate <= interstim_delay, (
        f"jitter_rate ({jitter_rate}s) must be <= interstim_delay ({interstim_delay}s) "
        "to avoid negative or invalid sleep intervals when jitter=True."
    )

    resource_name = "33512B"
    id_query = True
    reset = False
    options = ""
    driver = ks.Kt33000(resource_name, id_query, reset, options)

    print("  identifier: ", driver.identity.identifier)
    print("  revision:   ", driver.identity.revision)
    print("  vendor:     ", driver.identity.vendor)
    print("  description:", driver.identity.description)
    print("  model:      ", driver.identity.instrument_model)
    print("  resource:   ", driver.driver_operation.io_resource_descriptor)
    print("  options:    ", driver.driver_operation.driver_setup)

    try:
        ch1 = driver.output_channels[0]
        ch2 = driver.output_channels[1]

        ch1.output.enabled = 0
        ch2.output.enabled = 0

        if _stop_requested(stop_event):
            print("Stop requested before configuration.")
            return

        # --- Channel 1 setup ---
        if ch1_ttl:
            ch1.output_function.function = ks.FunctionShape.PULSE
            ch1.output.voltage.high = 5
            ch1.output.voltage.low = 0
            ch1.output_function.pulse.width = 1e-3
        else:
            fg_ch1 = {} if fg_ch1 is None else dict(fg_ch1)

            allowed_fg = {
                "v_min", "v_max", "vpp", "shape",
                "custom", "ramp",
                "auto_k", "k",
                "pph", "ppw", "pw",
                "channel", "state",
                "charge_balance", "reverse",
            }
            unknown = set(fg_ch1) - allowed_fg
            assert not unknown, f"Unknown func_gen_control kwargs in fg_ch1: {sorted(unknown)}"

            fg_ch1.setdefault("channel", 1)
            fg_ch1.setdefault("state", 1)

            func_gen_control(
                freq=1 / interstim_delay,
                **fg_ch1,
                burst_mode = True,
                driver = driver
            )

        if _stop_requested(stop_event):
            print("Stop requested after CH1 setup.")
            return

        # --- Channel 2 setup ---
        if ch2_ttl:
            ch2.output_function.function = ks.FunctionShape.PULSE
            ch2.output.voltage.high = 5
            ch2.output.voltage.low = 0
            ch2.output_function.pulse.width = 1e-3
        else:
            fg_ch2 = {} if fg_ch2 is None else dict(fg_ch2)

            allowed_fg = {
                "v_min", "v_max", "vpp", "shape",
                "custom", "ramp",
                "auto_k", "k",
                "pph", "ppw", "pw",
                "channel", "state",
                "charge_balance", "reverse",
            }
            unknown = set(fg_ch2) - allowed_fg
            assert not unknown, f"Unknown func_gen_control kwargs in fg_ch2: {sorted(unknown)}"

            fg_ch2.setdefault("channel", 2)
            fg_ch2.setdefault("state", 1)

            pw = fg_ch2.get("pw", 1)
            channel = fg_ch2.get("channel", 2)

            print(f"channel {channel} pw: {pw}")

            if not ch2_state:

                print("CH2 disabled; skipping CH2 configuration.")

            else:

                func_gen_control(
                    freq=1 / interstim_delay,
                    **fg_ch2,
                    burst_mode = True,
                    driver = driver
                )


        if _stop_requested(stop_event):
            print("Stop requested after CH2 setup.")
            return

        # --- burst + trigger config ---
        ch1.burst.enabled = True
        ch2.burst.enabled = True

        ch1.trigger.source = ks.TriggerSource.BUS
        ch2.trigger.source = ks.TriggerSource.BUS

        if rand_freq:
                random_frequency = random.uniform(
                    rand_freq_lower,
                    rand_freq_upper
                )
                ch1.output.frequency = random_frequency
                ch2.output.frequency = random_frequency

        else:

            ch1.output.frequency = 1 / interstim_delay
            ch2.output.frequency = 1 / interstim_delay

        print(f"burst cycles = {burst_cycles}")

        if (not jitter) and (burst_cycles == 1):
            print("burst = num_stims")
            ch1.burst.number_of_cycles = num_stims
            ch2.burst.number_of_cycles = num_stims
            jitter_rate = 0
        else:
            ch1.burst.number_of_cycles = burst_cycles
            ch2.burst.number_of_cycles = burst_cycles

        ch1.output.set_load_infinity()
        ch2.output.set_load_infinity()

        # --- set trigger delays ---
        if interpulse_delay > 0:
            ch1.trigger.delay = datetime.timedelta(0, 0, 0, 0)
            ch2.trigger.delay = datetime.timedelta(0, 0, 0, ch2_delay)
        elif interpulse_delay < 0:
            ch2.trigger.delay = datetime.timedelta(0, 0, 0, 0)
            ch1.trigger.delay = datetime.timedelta(0, 0, 0, abs(ch2_delay))
        else:
            ch1.trigger.delay = datetime.timedelta(0, 0, 0, 0)
            ch2.trigger.delay = datetime.timedelta(0, 0, 0, 0)

        ch1.output.enabled = 1
        ch2.output.enabled = 1 if ch2_state else 0

        if _stop_requested(stop_event):
            print("Stop requested before trigger phase.")
            return

        # --- trigger ---
        if jitter or (burst_cycles > 1):
            
            if burst_cycles != 1 and not rand_freq:
                if interpulse_delay <= 0:
                    raise ValueError(
                        "interpulse_delay must be > 0 ms when burst_cycles > 1 and rand_freq is False."
                    )
                pulse_freq = 1000.0 / interpulse_delay
                ch1.output.frequency = pulse_freq
                ch2.output.frequency = pulse_freq

            count = 1
            while count <= num_stims:
                if _stop_requested(stop_event):
                    print("Stop requested during burst loop.")
                    return
                
                if rand_freq:
                    random_frequency = random.uniform(
                        rand_freq_lower,
                        rand_freq_upper
                    )
                    ch1.output.frequency = random_frequency
                    ch2.output.frequency = random_frequency

                if interpulse_delay >= 0:
                    print("triggered")
                    print(ch1.trigger.source)
                    ch1.trigger.software_trigger()
                else:
                    ch2.trigger.software_trigger()

                print(f"Trigger: {count}")

                rand = random.uniform(
                    interstim_delay - jitter_rate,
                    interstim_delay + jitter_rate
                )

                stopped = _sleep_with_stop(rand, stop_event=stop_event, chunk_s=0.01)
                if stopped:
                    print("Stop requested during interstim wait.")
                    return

                count += 1
        else:
            if interpulse_delay >= 0:
                ch1.trigger.software_trigger()
            else:
                ch2.trigger.software_trigger()

            # Optional: if you want Stop to remain meaningful even in the
            # single-trigger/burst-engine case, wait cooperatively for the
            # expected run duration so the worker stays alive and can be stopped.

            freq = 1 / interstim_delay

            estimated_run_time = int(_estimated_run_time(num_stims, freq))

            print(f'Estimated run time: {estimated_run_time}')

            # _sleep_with_stop(estimated_run_time, stop_event=stop_event, chunk_s=0.01)

    finally:

        try:
            # Put hardware in a safe state on normal exit or Stop.

            print("Disabling Hardware")

            # ch1.output.enabled = 0
            # ch2.output.enabled = 0

            # ch1.burst.enabled = False
            # ch2.burst.enabled = False

            # ch1.trigger.abort()
            # ch2.trigger.abort()

            # # 2) Put channels back into inert trigger mode
            # ch1.trigger.source = ks.TriggerSource.IMMEDIATE
            # ch2.trigger.source = ks.TriggerSource.IMMEDIATE

            # print("Hardware Disabled")

            # PLACEHOLDER:
            # Insert the actual Keysight/function-generator command here that
            # aborts or stops burst execution immediately, once you know it.
            #
            # Example placeholder only:
            # ch1.some_abort_or_stop_command()
            # ch2.some_abort_or_stop_command()
        
            # driver.utility.reset()

        except Exception as cleanup_error:
            print(f"Cleanup warning: {cleanup_error}")

        print("Closing Driver")
        driver.close()
        print ("Driver Closed")



    
'''
Usage examples:

from burst_mode_function import burst_mode

burst_mode(
    interpulse_delay=0,   # ms
    interstim_delay=0.5,    # seconds
    num_stims=6,
    jitter=False,
    jitter_rate=0,        # seconds
    burst_cycles=1,
    ch2_state=0,
    ch2_delay=0,
    ch1_ttl=True,
    ch2_ttl=False,
    rand_freq = False,
    rand_freq_upper = 1,
    rand_freq_lower = 5,
)

import sys
sys.modules.pop("burst_mode_function", None)



'''