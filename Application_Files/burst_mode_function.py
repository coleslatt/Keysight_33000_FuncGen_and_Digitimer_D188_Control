import keysight_kt33000 as ks
import numpy as np
from typing import Literal
import datetime
import random
import time
from FuncGen_Selector_Function import func_gen_control

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

    end_time = time.monotonic() + duration_s
    while time.monotonic() < end_time:
        if _stop_requested(stop_event):
            return True
        remaining = end_time - time.monotonic()
        time.sleep(min(chunk_s, max(0.0, remaining)))
    return _stop_requested(stop_event)


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

            func_gen_control(
                freq=1 / interstim_delay,
                **fg_ch2,
            )

        if _stop_requested(stop_event):
            print("Stop requested after CH2 setup.")
            return

        # --- burst + trigger config ---
        ch1.burst.enabled = True
        ch2.burst.enabled = True

        ch1.trigger.source = ks.TriggerSource.BUS
        ch2.trigger.source = ks.TriggerSource.BUS

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
            if burst_cycles != 1:
                ch1.output.frequency = 1e3 / interpulse_delay
                ch2.output.frequency = 1e3 / interpulse_delay

            count = 1
            while count <= num_stims:
                if _stop_requested(stop_event):
                    print("Stop requested during burst loop.")
                    return

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
            estimated_run_time = num_stims * interstim_delay
            _sleep_with_stop(estimated_run_time, stop_event=stop_event, chunk_s=0.01)

    finally:
        try:
            # Put hardware in a safe state on normal exit or Stop.
            ch1.output.enabled = 0
            ch2.output.enabled = 0

            ch1.burst.enabled = False
            ch2.burst.enabled = False

            # PLACEHOLDER:
            # Insert the actual Keysight/function-generator command here that
            # aborts or stops burst execution immediately, once you know it.
            #
            # Example placeholder only:
            # ch1.some_abort_or_stop_command()
            # ch2.some_abort_or_stop_command()

        except Exception as cleanup_error:
            print(f"Cleanup warning: {cleanup_error}")

        driver.close()



## Old Burst Mode Function (pre stop button implementation) -- kept for reference and potential reuse of timing logic in future versions

# import keysight_kt33000 as ks
# import numpy as np
# from typing import Literal
# import datetime
# import random
# import time
# from FuncGen_Selector_Function import func_gen_control

# # d188.py — minimal ctypes bridge for DGD188API.DLL (Windows) — fixed prototypes to allow None
# import ctypes as C
# from ctypes import wintypes as W

# # --- Load the DLL (stdcall) ---
# lib = C.WinDLL("DGD188API.DLL")  # WinDLL = stdcall

# # --- Function prototypes (callbacks as void* so we can pass None) ---

# lib.DGD188_Initialise.argtypes = [C.POINTER(W.INT), C.POINTER(W.INT), C.c_void_p, C.c_void_p]
# lib.DGD188_Initialise.restype  = W.INT

# lib.DGD188_Update.argtypes = [W.INT, C.POINTER(W.INT),
#                               C.c_void_p, W.INT,
#                               C.c_void_p, C.POINTER(W.INT),
#                               C.c_void_p, C.c_void_p]
# lib.DGD188_Update.restype  = W.INT

# # int __stdcall DGD188_Close(int* Reference, int* Error, DGClientCloseProc cb, void* param);
# lib.DGD188_Close.argtypes = [C.POINTER(W.INT), C.POINTER(W.INT), C.c_void_p, C.c_void_p]
# lib.DGD188_Close.restype  = W.INT

# # ----- Struct mirrors (from D188API.h) -----
# class DEVHDR(C.Structure):
#     _fields_ = [("DeviceCount", W.INT)]

# class D188STATE_T(C.Structure):
#     _fields_ = [
#         ("D188_Mode",      C.c_uint8),   # 0=OFF, 1=USB/API, 2=TTL(1..8), 3=TTL(4..8)
#         ("D188_Select",    C.c_uint8),   # CH1=1, CH2=2, ..., CH8=128 (first set bit honored)
#         ("D188_Indicator", C.c_uint8),   # 0=off, nonzero=on
#         ("D188_Delay",     C.c_uint16),  # n * 100 µs
#     ]
#     _pack_ = 1  # helps with byte/short packing on Windows

# class D188DEVICESTATE_T(C.Structure):
#     _fields_ = [
#         ("D188_DeviceID",  W.INT),
#         ("D188_VersionID", W.INT),
#         ("D188_Error",     W.INT),
#         ("D188_State",     D188STATE_T),
#     ]
#     # _pack_ = 1  # uncomment if fields look misaligned on your machine

# def read_device_count(buf):
#     return DEVHDR.from_buffer_copy(buf).DeviceCount

# def device_at_mutable(buf, index):
#     base = C.addressof(buf)
#     offset = C.sizeof(DEVHDR) + index * C.sizeof(D188DEVICESTATE_T)
#     return C.cast(base + offset, C.POINTER(D188DEVICESTATE_T))

# def D188_Controller(channel=1,
#                    light = 1):
#     """
#     Channel = channel # on D188,
#     Light = 1 (on), 0 (off)
    
#     """

#     channel = channel-1
    
#     ref = W.INT(0)
#     err = W.INT(0)

#     # 1) Open session
#     r = lib.DGD188_Initialise(C.byref(ref), C.byref(err), None, None)
#     if r != 0 or err.value != 0:
#         print(f"Initialise failed: ret={r} apiErr={err.value}")
#         return

#     try:
#         # 2) Size probe
#         cb = W.INT(0)
#         r = lib.DGD188_Update(ref, C.byref(err),
#                               None, 0,
#                               None, C.byref(cb),
#                               None, None)
#         if r != 0 or cb.value <= 0:
#             print(f"Size probe failed: ret={r} apiErr={err.value} cb={cb.value}")
#             return

#         # 3) Allocate buffer and read current state
#         buf = C.create_string_buffer(cb.value)
#         r = lib.DGD188_Update(ref, C.byref(err),
#                               None, 0,
#                               C.addressof(buf), C.byref(cb),
#                               None, None)
#         if r != 0 or err.value != 0:
#             print(f"Read state failed: ret={r} apiErr={err.value}")
#             return

#         devs = read_device_count(buf)
#         print(f"Found {devs} device(s).")
#         if devs == 0:
#             return

#         # 4) Modify device 0 in-place
#         dev0_ptr = device_at_mutable(buf, 0)
#         dev0 = dev0_ptr.contents
#         print(f"Before: Mode={dev0.D188_State.D188_Mode} Select={dev0.D188_State.D188_Select}")

#         dev0.D188_State.D188_Mode      = 1       # USB/API
#         dev0.D188_State.D188_Indicator = light       # LED on
#         dev0.D188_State.D188_Select    = 1 << channel  # CH1

#         # 5) Write back (send same buffer as NewState) and fetch post-state into same buffer
#         r = lib.DGD188_Update(ref, C.byref(err),
#                               C.addressof(buf), cb,                 # NewState
#                               C.addressof(buf), C.byref(cb),        # CurrentState
#                               None, None)
#         if r == 0 and err.value == 0:
#             print("Channel set to 1 on device 0.")
#         else:
#             print(f"Write failed: ret={r} apiErr={err.value}")

#     finally:
#         lib.DGD188_Close(C.byref(ref), C.byref(err), None, None)

# def current_calc(desired_current, # in mA
#                 input_volts,
#                 output_current # in mA (ON DS5)
#                 ):
#     vs = (desired_current * input_volts) / output_current
#     return vs


# def burst_mode(
#     interpulse_delay=0,   # ms
#     interstim_delay=1,    # seconds
#     num_stims=10,
#     jitter=False,
#     jitter_rate=0,        # seconds
#     burst_cycles = 1,
#     ch2_state = 0,
#     ch2_delay=0,
#     ch1_ttl=True,
#     ch2_ttl=False,
#     *,
#     fg_ch1: dict | None = None,  # kwargs forwarded to func_gen_control when ch1_ttl=False
#     fg_ch2: dict | None = None,  # kwargs forwarded to func_gen_control when ch2_ttl=False
# ):
#     """
#     Configure and trigger paired-pulse “burst mode” output on a Keysight 33512B.

#     Conceptually, each stimulation event is a *pair* of pulses:
#       - Channel 1: first pulse in the pair (either TTL trigger OR a custom waveform)
#       - Channel 2: second pulse in the pair (ALWAYS TTL trigger)

#     Both channels are configured for burst operation and are software-triggered over the
#     instrument bus. Timing between the two pulses in each pair is controlled by
#     `interpulse_delay` via per-channel trigger delays.

#     Timing: interpulse_delay sign convention
#     ---------------------------------------
#     `interpulse_delay` is interpreted in **milliseconds** and sets the relative timing
#     between Channel 1 and Channel 2 *within each pulse pair*:

#       - interpulse_delay > 0:
#           Channel 1 occurs first.
#           Channel 2 is delayed by `interpulse_delay` ms.
#           (ch1.trigger.delay = 0, ch2.trigger.delay = +interpulse_delay)

#       - interpulse_delay < 0:
#           Channel 2 occurs first.
#           Channel 1 is delayed by abs(`interpulse_delay`) ms.
#           (ch2.trigger.delay = 0, ch1.trigger.delay = abs(interpulse_delay))

#       - interpulse_delay == 0:
#           Both channels occur simultaneously (zero trigger delay on both).

#     Practical note: because only one software trigger is issued when `jitter=False`,
#     the function triggers the channel whose delay is zero:
#       - interpulse_delay >= 0  -> software trigger Channel 1
#       - interpulse_delay < 0   -> software trigger Channel 2

#     Burst scheduling: interstim_delay and num_stims
#     -----------------------------------------------
#     `interstim_delay` sets the repetition period between pulse pairs (seconds). Internally,
#     both channels are set to frequency = 1 / interstim_delay. When `jitter=False`, the
#     Keysight burst engine outputs `num_stims` pulse pairs per single software trigger
#     (i.e., number_of_cycles = num_stims). When `jitter=True`, the function instead triggers
#     one pair at a time from software and sleeps between triggers with optional randomness.

#     Channel roles and waveform types
#     --------------------------------
#     Channel 2 is always configured as a TTL pulse:
#       - 0–5 V, pulse width = 1 ms, burst-enabled, BUS trigger source

#     Channel 1 depends on `ch1_ttl`:
#       - ch1_ttl=True:
#           Channel 1 is also configured as a TTL pulse (0–5 V, 1 ms width).
#       - ch1_ttl=False:
#           Channel 1 is configured using `func_gen_control(...)` to generate a custom
#           waveform (e.g., sine or user-defined). In this mode, only Channel 1 can be
#           “custom”; Channel 2 remains TTL.

#     DS5 current scaling behavior
#     ----------------------------
#     If `DS5=True` and `ch1_ttl=False`, Channel 1’s output voltage bounds are overridden to
#     achieve a target DS5 output current using a linear scaling model:

#         v_max = (DS5_desired_current[mA] * DS5_input_volt[V]) / DS5_output_current[mA]
#         v_min = 0

#     IMPORTANT: DS5_input_volt and DS5_output_current MUST match the *physical DS5 front-panel*
#     settings you are actually using:
#       - DS5_input_volt: the DS5 input sensitivity setting (e.g., “5 V” input full-scale)
#       - DS5_output_current: the DS5 output current range setting (e.g., “50 mA” range)

#     If these do not match the DS5 hardware settings, the delivered current will not match
#     `DS5_desired_current`.

#     Forwarded func_gen_control parameters
#     -------------------------------------
#     When `ch1_ttl=False`, the `fg` dict is forwarded to `func_gen_control` as kwargs.
#     This keeps the burst/timing API clean and makes it explicit which settings only apply
#     to the Channel 1 custom waveform path.

#     Returns
#     -------
#     None
#     """
#     # --- basic validation ---
#     assert interstim_delay > 0, "interstim_delay must be > 0 seconds"
#     assert num_stims >= 1, "num_stims must be >= 1"
#     assert jitter_rate >= 0, "jitter_rate must be >= 0 seconds"
#     assert jitter_rate <= interstim_delay, (
#         f"jitter_rate ({jitter_rate}s) must be <= interstim_delay ({interstim_delay}s) "
#         "to avoid negative or invalid sleep intervals when jitter=True."
#     )

#     # --- open instrument ---
#     resource_name = "33512B"
#     id_query = True
#     reset = False
#     options = ""
#     driver = ks.Kt33000(resource_name, id_query, reset, options)

#     print("  identifier: ", driver.identity.identifier)
#     print("  revision:   ", driver.identity.revision)
#     print("  vendor:     ", driver.identity.vendor)
#     print("  description:", driver.identity.description)
#     print("  model:      ", driver.identity.instrument_model)
#     print("  resource:   ", driver.driver_operation.io_resource_descriptor)
#     print("  options:    ", driver.driver_operation.driver_setup)

#     try:
#         ch1 = driver.output_channels[0]
#         ch2 = driver.output_channels[1]

#         ch1.output.enabled = 0
#         ch2.output.enabled = 0

#         # --- Channel 1 setup ---
#         if ch1_ttl:
#             # CH1 TTL pulse
#             ch1.output_function.function = ks.FunctionShape.PULSE
#             ch1.output.voltage.high = 5
#             ch1.output.voltage.low = 0
#             ch1.output_function.pulse.width = 1e-3

#         else:
#             # CH1 custom waveform via func_gen_control
#             fg_ch1 = {} if fg_ch1 is None else dict(fg_ch1)  # copy to avoid mutating caller

#             # Optional: enforce allowed forwarded keys (helps catch typos)
#             allowed_fg = {
#                 "v_min", "v_max", "vpp", "shape",
#                 "custom", "ramp",
#                 "auto_k", "k",
#                 "pph", "ppw", "pw",
#                 "channel", "state",
#                 "charge_balance", "reverse",
#             }
#             unknown = set(fg_ch1) - allowed_fg
#             assert not unknown, f"Unknown func_gen_control kwargs in fg: {sorted(unknown)}"

#             # Ensure Channel 1 + ON state if caller didn't specify
#             fg_ch1.setdefault("channel", 1)
#             fg_ch1.setdefault("state", 1)

#             func_gen_control(
#                 freq=1 / interstim_delay,
#                 **fg_ch1,
#             )

#         # --- Channel 2 setup ---
#         if ch2_ttl:
#             # CH1 TTL pulse
#             ch2.output_function.function = ks.FunctionShape.PULSE
#             ch2.output.voltage.high = 5
#             ch2.output.voltage.low = 0
#             ch2.output_function.pulse.width = 1e-3
#         else:
#             # CH1 custom waveform via func_gen_control
#             fg_ch2 = {} if fg_ch2 is None else dict(fg_ch2)  # copy to avoid mutating caller

#             # Optional: enforce allowed forwarded keys (helps catch typos)
#             allowed_fg = {
#                 "v_min", "v_max", "vpp", "shape",
#                 "custom", "ramp",
#                 "auto_k", "k",
#                 "pph", "ppw", "pw",
#                 "channel", "state",
#                 "charge_balance", "reverse",
#             }
#             unknown = set(fg_ch2) - allowed_fg
#             assert not unknown, f"Unknown func_gen_control kwargs in fg: {sorted(unknown)}"

#             # Ensure Channel 1 + ON state if caller didn't specify
#             fg_ch2.setdefault("channel", 2)
#             fg_ch2.setdefault("state", 1)

#             pw = fg_ch2.get("pw", 1)
#             channel = fg_ch2.get("channel", 1)
            
#             print(f'channel {channel} pw: {pw}')

#             func_gen_control(
#                 freq=1 / interstim_delay,
#                 **fg_ch2,
#             )


#         # --- burst + trigger config ---
#         ch1.burst.enabled = True
#         ch2.burst.enabled = True

#         ch1.trigger.source = ks.TriggerSource.BUS
#         ch2.trigger.source = ks.TriggerSource.BUS

#         ch1.output.frequency = 1 / interstim_delay
#         ch2.output.frequency = 1 / interstim_delay

#         print(f"burst cycles = {burst_cycles}")

#         if (not jitter) and (burst_cycles==1):

#             print("burst = num_stims")
#             ch1.burst.number_of_cycles = num_stims
#             ch2.burst.number_of_cycles = num_stims
#             jitter_rate = 0  # ensure no jitter if burst engine is handling repetition
            
#         else:
#             ch1.burst.number_of_cycles = burst_cycles
#             ch2.burst.number_of_cycles = burst_cycles

#         ch1.output.set_load_infinity()
#         ch2.output.set_load_infinity()

#         # --- set trigger delays based on interpulse_delay sign ---
#         if interpulse_delay > 0:
#             ch1.trigger.delay = datetime.timedelta(0, 0, 0, 0)
#             ch2.trigger.delay = datetime.timedelta(0, 0, 0, ch2_delay)
#         elif interpulse_delay < 0:
#             ch2.trigger.delay = datetime.timedelta(0, 0, 0, 0)
#             ch1.trigger.delay = datetime.timedelta(0, 0, 0, abs(ch2_delay))
#         else:
#             ch1.trigger.delay = datetime.timedelta(0, 0, 0, 0)
#             ch2.trigger.delay = datetime.timedelta(0, 0, 0, 0)

#         # --- enable outputs ---
#         ch1.output.enabled = 1
#         ch2.output.enabled = 1 if ch2_state else 0

#         pw = fg_ch1.get("pw", 1)

#         # --- trigger ---
#         if jitter or (burst_cycles > 1):
#             # One pair per trigger, randomized delay between triggers
#             if burst_cycles != 1:
#                 ch1.output.frequency = 1e3 / ((interpulse_delay))
#                 ch2.output.frequency = 1e3 / ((interpulse_delay))
                
#             count = 1
#             while count <= num_stims:
#                 if interpulse_delay >= 0:
#                     print('trigged')
#                     print(ch1.trigger.source)
#                     ch1.trigger.software_trigger()

#                 print(f"Trigger: {count}")

#                 rand = random.uniform(interstim_delay - jitter_rate, interstim_delay + jitter_rate)
#                 time.sleep(rand)
#                 count += 1
#         else:
#             # One trigger starts an instrument burst of num_stims cycles
#             if interpulse_delay >= 0:
#                 ch1.trigger.software_trigger()
#             else:
#                 ch2.trigger.software_trigger()

#     finally:
#         driver.close()
