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

# --- (Optional) callback typedefs if you ever need them ---
# DGClientInitialiseProc = C.WINFUNCTYPE(None, W.INT, C.c_void_p)
# DGClientUpdateProc     = C.WINFUNCTYPE(None, W.INT, C.c_void_p, C.c_void_p)
# DGClientCloseProc      = C.WINFUNCTYPE(None, W.INT, C.c_void_p)

# --- Function prototypes (callbacks as void* so we can pass None) ---
# int __stdcall DGD188_Initialise(int* Reference, int* Error, DGClientInitialiseProc cb, void* param);
lib.DGD188_Initialise.argtypes = [C.POINTER(W.INT), C.POINTER(W.INT), C.c_void_p, C.c_void_p]
lib.DGD188_Initialise.restype  = W.INT

# int __stdcall DGD188_Update(int Reference, int* Error,
#                             void* NewState, int cbNewState,
#                             void* CurrentState, int* cbCurrentState,
#                             DGClientUpdateProc cb, void* param);
lib.DGD188_Update.argtypes = [W.INT, C.POINTER(W.INT),
                              C.c_void_p, W.INT,
                              C.c_void_p, C.POINTER(W.INT),
                              C.c_void_p, C.c_void_p]
lib.DGD188_Update.restype  = W.INT

# int __stdcall DGD188_Close(int* Reference, int* Error, DGClientCloseProc cb, void* param);
lib.DGD188_Close.argtypes = [C.POINTER(W.INT), C.POINTER(W.INT), C.c_void_p, C.c_void_p]
lib.DGD188_Close.restype  = W.INT

# ----- Struct mirrors (from D188API.h) -----
class DEVHDR(C.Structure):
    _fields_ = [("DeviceCount", W.INT)]

class D188STATE_T(C.Structure):
    _fields_ = [
        ("D188_Mode",      C.c_uint8),   # 0=OFF, 1=USB/API, 2=TTL(1..8), 3=TTL(4..8)
        ("D188_Select",    C.c_uint8),   # CH1=1, CH2=2, ..., CH8=128 (first set bit honored)
        ("D188_Indicator", C.c_uint8),   # 0=off, nonzero=on
        ("D188_Delay",     C.c_uint16),  # n * 100 µs
    ]
    _pack_ = 1  # helps with byte/short packing on Windows

class D188DEVICESTATE_T(C.Structure):
    _fields_ = [
        ("D188_DeviceID",  W.INT),
        ("D188_VersionID", W.INT),
        ("D188_Error",     W.INT),
        ("D188_State",     D188STATE_T),
    ]
    # _pack_ = 1  # uncomment if fields look misaligned on your machine

def read_device_count(buf):
    return DEVHDR.from_buffer_copy(buf).DeviceCount

def device_at_mutable(buf, index):
    base = C.addressof(buf)
    offset = C.sizeof(DEVHDR) + index * C.sizeof(D188DEVICESTATE_T)
    return C.cast(base + offset, C.POINTER(D188DEVICESTATE_T))

def D188_Controller(channel=1,
                   light = 1):
    """
    Channel = channel # on D188,
    Light = 1 (on), 0 (off)
    
    """

    channel = channel-1
    
    ref = W.INT(0)
    err = W.INT(0)

    # 1) Open session
    r = lib.DGD188_Initialise(C.byref(ref), C.byref(err), None, None)
    if r != 0 or err.value != 0:
        print(f"Initialise failed: ret={r} apiErr={err.value}")
        return

    try:
        # 2) Size probe
        cb = W.INT(0)
        r = lib.DGD188_Update(ref, C.byref(err),
                              None, 0,
                              None, C.byref(cb),
                              None, None)
        if r != 0 or cb.value <= 0:
            print(f"Size probe failed: ret={r} apiErr={err.value} cb={cb.value}")
            return

        # 3) Allocate buffer and read current state
        buf = C.create_string_buffer(cb.value)
        r = lib.DGD188_Update(ref, C.byref(err),
                              None, 0,
                              C.addressof(buf), C.byref(cb),
                              None, None)
        if r != 0 or err.value != 0:
            print(f"Read state failed: ret={r} apiErr={err.value}")
            return

        devs = read_device_count(buf)
        print(f"Found {devs} device(s).")
        if devs == 0:
            return

        # 4) Modify device 0 in-place
        dev0_ptr = device_at_mutable(buf, 0)
        dev0 = dev0_ptr.contents
        print(f"Before: Mode={dev0.D188_State.D188_Mode} Select={dev0.D188_State.D188_Select}")

        dev0.D188_State.D188_Mode      = 1       # USB/API
        dev0.D188_State.D188_Indicator = light       # LED on
        dev0.D188_State.D188_Select    = 1 << channel  # CH1

        # 5) Write back (send same buffer as NewState) and fetch post-state into same buffer
        r = lib.DGD188_Update(ref, C.byref(err),
                              C.addressof(buf), cb,                 # NewState
                              C.addressof(buf), C.byref(cb),        # CurrentState
                              None, None)
        if r == 0 and err.value == 0:
            print("Channel set to 1 on device 0.")
        else:
            print(f"Write failed: ret={r} apiErr={err.value}")

    finally:
        lib.DGD188_Close(C.byref(ref), C.byref(err), None, None)

def current_calc(desired_current, # in mA
                input_volts,
                output_current # in mA (ON DS5)
                ):
    vs = (desired_current * input_volts) / output_current
    return vs


def burst_mode(
    interpulse_delay=0,   # ms
    interstim_delay=1,    # seconds
    num_stims=10,
    jitter=False,
    jitter_rate=0,        # seconds
    burst_cycles = 1,
    ch1_ttl=True,
    ch1_shape="sine",
    DS5=True,
    DS5_input_volt=5,
    DS5_output_current=50,
    DS5_desired_current=1,
    *,
    fg: dict | None = None,  # kwargs forwarded to func_gen_control when ch1_ttl=False
):
    """
    Configure and trigger paired-pulse “burst mode” output on a Keysight 33512B.

    Conceptually, each stimulation event is a *pair* of pulses:
      - Channel 1: first pulse in the pair (either TTL trigger OR a custom waveform)
      - Channel 2: second pulse in the pair (ALWAYS TTL trigger)

    Both channels are configured for burst operation and are software-triggered over the
    instrument bus. Timing between the two pulses in each pair is controlled by
    `interpulse_delay` via per-channel trigger delays.

    Timing: interpulse_delay sign convention
    ---------------------------------------
    `interpulse_delay` is interpreted in **milliseconds** and sets the relative timing
    between Channel 1 and Channel 2 *within each pulse pair*:

      - interpulse_delay > 0:
          Channel 1 occurs first.
          Channel 2 is delayed by `interpulse_delay` ms.
          (ch1.trigger.delay = 0, ch2.trigger.delay = +interpulse_delay)

      - interpulse_delay < 0:
          Channel 2 occurs first.
          Channel 1 is delayed by abs(`interpulse_delay`) ms.
          (ch2.trigger.delay = 0, ch1.trigger.delay = abs(interpulse_delay))

      - interpulse_delay == 0:
          Both channels occur simultaneously (zero trigger delay on both).

    Practical note: because only one software trigger is issued when `jitter=False`,
    the function triggers the channel whose delay is zero:
      - interpulse_delay >= 0  -> software trigger Channel 1
      - interpulse_delay < 0   -> software trigger Channel 2

    Burst scheduling: interstim_delay and num_stims
    -----------------------------------------------
    `interstim_delay` sets the repetition period between pulse pairs (seconds). Internally,
    both channels are set to frequency = 1 / interstim_delay. When `jitter=False`, the
    Keysight burst engine outputs `num_stims` pulse pairs per single software trigger
    (i.e., number_of_cycles = num_stims). When `jitter=True`, the function instead triggers
    one pair at a time from software and sleeps between triggers with optional randomness.

    Channel roles and waveform types
    --------------------------------
    Channel 2 is always configured as a TTL pulse:
      - 0–5 V, pulse width = 1 ms, burst-enabled, BUS trigger source

    Channel 1 depends on `ch1_ttl`:
      - ch1_ttl=True:
          Channel 1 is also configured as a TTL pulse (0–5 V, 1 ms width).
      - ch1_ttl=False:
          Channel 1 is configured using `func_gen_control(...)` to generate a custom
          waveform (e.g., sine or user-defined). In this mode, only Channel 1 can be
          “custom”; Channel 2 remains TTL.

    DS5 current scaling behavior
    ----------------------------
    If `DS5=True` and `ch1_ttl=False`, Channel 1’s output voltage bounds are overridden to
    achieve a target DS5 output current using a linear scaling model:

        v_max = (DS5_desired_current[mA] * DS5_input_volt[V]) / DS5_output_current[mA]
        v_min = 0

    IMPORTANT: DS5_input_volt and DS5_output_current MUST match the *physical DS5 front-panel*
    settings you are actually using:
      - DS5_input_volt: the DS5 input sensitivity setting (e.g., “5 V” input full-scale)
      - DS5_output_current: the DS5 output current range setting (e.g., “50 mA” range)

    If these do not match the DS5 hardware settings, the delivered current will not match
    `DS5_desired_current`.

    Forwarded func_gen_control parameters
    -------------------------------------
    When `ch1_ttl=False`, the `fg` dict is forwarded to `func_gen_control` as kwargs.
    This keeps the burst/timing API clean and makes it explicit which settings only apply
    to the Channel 1 custom waveform path.

    Returns
    -------
    None
    """
    # --- basic validation ---
    assert interstim_delay > 0, "interstim_delay must be > 0 seconds"
    assert num_stims >= 1, "num_stims must be >= 1"
    assert jitter_rate >= 0, "jitter_rate must be >= 0 seconds"
    assert jitter_rate <= interstim_delay, (
        f"jitter_rate ({jitter_rate}s) must be <= interstim_delay ({interstim_delay}s) "
        "to avoid negative or invalid sleep intervals when jitter=True."
    )

    # --- open instrument ---
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

        shape_def = ks.FunctionShape.PULSE

        # --- Channel 1 setup ---
        if ch1_ttl:
            # CH1 TTL pulse
            ch1.output_function.function = shape_def
            ch1.output.voltage.high = 5
            ch1.output.voltage.low = 0
            ch1.output_function.pulse.width = 1e-3
        else:
            # CH1 custom waveform via func_gen_control
            fg = {} if fg is None else dict(fg)  # copy to avoid mutating caller

            # Optional: enforce allowed forwarded keys (helps catch typos)
            allowed_fg = {
                "v_min", "v_max", "vpp",
                "custom", "ramp",
                "auto_k", "k",
                "pph", "ppw", "pw",
                "channel", "state",
                "charge_balance", "reverse",
            }
            unknown = set(fg) - allowed_fg
            assert not unknown, f"Unknown func_gen_control kwargs in fg: {sorted(unknown)}"

            # DS5 override of voltage bounds (only relevant for custom CH1)
            if DS5:
                v_max = current_calc(DS5_desired_current, DS5_input_volt, DS5_output_current)
                v_min = 0
                fg["v_min"] = v_min
                fg["v_max"] = v_max

            # Ensure Channel 1 + ON state if caller didn't specify
            fg.setdefault("channel", 1)
            fg.setdefault("state", 1)

            func_gen_control(
                shape=ch1_shape,
                freq=1 / interstim_delay,
                **fg,
            )

        # --- Channel 2 setup (ALWAYS TTL trigger) ---
        ch2.output_function.function = shape_def
        ch2.output.voltage.high = 5
        ch2.output.voltage.low = 0
        ch2.output_function.pulse.width = 1e-3

        # --- burst + trigger config ---
        ch1.burst.enabled = True
        ch2.burst.enabled = True

        ch1.trigger.source = ks.TriggerSource.BUS
        ch2.trigger.source = ks.TriggerSource.BUS

        ch1.output.frequency = 1 / interstim_delay
        ch2.output.frequency = 1 / interstim_delay

        if not jitter:
            ch1.burst.number_of_cycles = num_stims
            ch2.burst.number_of_cycles = num_stims
        else:
            ch1.burst.number_of_cycles = burst_cycles
            ch2.burst.number_of_cycles = burst_cycles

        ch1.output.set_load_infinity()
        ch2.output.set_load_infinity()

        # --- set trigger delays based on interpulse_delay sign ---
        if interpulse_delay > 0:
            ch1.trigger.delay = datetime.timedelta(0, 0, 0, 0)
            ch2.trigger.delay = datetime.timedelta(0, 0, 0, interpulse_delay)
        elif interpulse_delay < 0:
            ch2.trigger.delay = datetime.timedelta(0, 0, 0, 0)
            ch1.trigger.delay = datetime.timedelta(0, 0, 0, abs(interpulse_delay))
        else:
            ch1.trigger.delay = datetime.timedelta(0, 0, 0, 0)
            ch2.trigger.delay = datetime.timedelta(0, 0, 0, 0)

        # --- enable outputs ---
        ch1.output.enabled = 1
        ch2.output.enabled = 1

        pw = fg.get("pw", 1)
        # --- trigger ---
        if jitter:
            # One pair per trigger, randomized delay between triggers
            if burst_cycles != 1:
                ch1.output.frequency = 1 / ((interpulse_delay + pw)*1e-3)
                ch2.output.frequency = 1 / ((interpulse_delay + pw)*1e-3)
                

            count = 0
            while count <= num_stims:
                if interpulse_delay >= 0:
                    ch1.trigger.software_trigger()
                else:
                    ch2.trigger.software_trigger()

                rand = random.uniform(interstim_delay - jitter_rate, interstim_delay + jitter_rate)
                time.sleep(rand)
                count += 1
        else:
            # One trigger starts an instrument burst of num_stims cycles
            if interpulse_delay >= 0:
                ch1.trigger.software_trigger()
            else:
                ch2.trigger.software_trigger()

    finally:
        driver.close()


# def burst_mode(interpulse_delay = 0, #ms
#                 interstim_delay = 1, #seconds
#                 num_stims = 10,
#                 jitter = False,
#                 jitter_rate = 0, #seconds
#                 ch1_ttl = True,
#                 ch1_shape = 'sine',
#                 DS5 = True,
#                 DS5_input_volt = 5,
#                 DS5_output_current = 50,
#                 DS5_desired_current = 1,
#                 v_min = -1,
#                 v_max = 1,
#                 vpp = 2,
#                 custom = 'no',
#                 ramp = 'yes',
#                 auto_k = True,
#                 k = 0.1,
#                 pph=0, # between 0-1
#                 ppw=0, # in ms
#                 pw = 1, # in ms
#                 channel = 1,
#                 state = 1,
#                 charge_balance = False,
#                 reverse = False   
#               ):

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
#     If `DS5=True` and `ch1_ttl=False`, Channel 1’s output voltage is automatically set to
#     achieve a target DS5 output current using a linear scaling model:

#         v_max = (DS5_desired_current[mA] * DS5_input_volt[V]) / DS5_output_current[mA]
#         v_min = 0

#     This assumes you are driving the DS5 input with the function generator (Channel 1),
#     and the DS5 is set to a known input sensitivity and output current range.

#     IMPORTANT: DS5_input_volt and DS5_output_current MUST match the *physical DS5 front-panel*
#     settings you are actually using:
#       - DS5_input_volt: the DS5 input sensitivity setting (e.g., “5 V” input full-scale)
#       - DS5_output_current: the DS5 output current range setting (e.g., “50 mA” range)

#     If these do not match the DS5 hardware settings, the computed voltage scaling will be
#     wrong and the delivered current will not equal `DS5_desired_current`.

#     Clarifying func_gen_control-only parameters
#     ------------------------------------------
#     This function forwards a block of parameters directly to `func_gen_control(...)` when
#     `ch1_ttl=False`. To make it obvious which arguments are *only* relevant for that
#     sub-configuration, consider one of these patterns:

#       1) Group them under a single dict/namespace:
#            funcgen_kwargs: dict | None = None
#          and call:
#            func_gen_control(..., **funcgen_kwargs)

#       2) Prefix forwarded parameters consistently (e.g., fg_shape, fg_ramp, fg_pw, ...)

#       3) Split into a small dataclass (FuncGenConfig) and accept one object:
#            funcgen: FuncGenConfig | None

#     Any of these avoids a long mixed signature where DS5 / burst timing arguments are
#     interleaved with waveform-shaping arguments.

#     Returns
#     -------
#     None
#         Configures both channels, triggers output (instrument burst or software loop),
#         then closes the instrument connection.

#     Notes / assumptions
#     -------------------
#     - Both channels are set to high impedance load ("infinite") via set_load_infinity().
#     - Channel 2 is always TTL; Channel 1 is TTL only when ch1_ttl=True.
#     - If `jitter=True`, the function triggers repeatedly in software; otherwise it relies
#       on Keysight burst cycles per trigger.
#     """

#     assert jitter_rate <= interstim_delay, (
#     f"jitter_rate ({jitter_rate}s) must be <= interstim_delay ({interstim_delay}s) "
#     "to avoid negative or invalid sleep intervals when jitter=True."
# )



#     resource_name = "33512B"
#     id_query = True
#     reset = False
#     options = ""
#     driver = ks.Kt33000(resource_name, id_query, reset, options)
#     print('  identifier: ', driver.identity.identifier)
#     print('  revision:   ', driver.identity.revision)
#     print('  vendor:     ', driver.identity.vendor)
#     print('  description:', driver.identity.description)
#     print('  model:      ', driver.identity.instrument_model)
#     print('  resource:   ', driver.driver_operation.io_resource_descriptor)
#     print('  options:    ', driver.driver_operation.driver_setup)


#     ch1 = driver.output_channels[0]
#     ch2 = driver.output_channels[1]

#     ch1.output.enabled = 0
#     ch2.output.enabled = 0
#     shape_def = ks.FunctionShape.PULSE

#     if ch1_ttl:

#         ch1.output_function.function = shape_def
#         ch1.output.voltage.high = 5
#         ch1.output.voltage.low = 0
#         ch1.output_function.pulse.width = 1e-3
        
#     else:

#         if DS5:
#             v_max = current_calc(DS5_desired_current,DS5_input_volt,DS5_output_current)    
#             v_min = 0
            
#         func_gen_control(
#             shape = ch1_shape,
#             freq =  1/interstim_delay,
#             v_min = v_min,
#             v_max = v_max,
#             vpp = vpp,
#             custom = custom,
#             ramp = ramp,
#             auto_k = auto_k,
#             k = k,
#             pph=pph, # between 0-1
#             ppw=ppw, # in ms
#             pw = pw, # in ms
#             channel = 1,
#             state = 1,
#             charge_balance = charge_balance,
#             reverse = reverse
#             )

#     # CH2 is always a TTL Trigger
#     ch2.output_function.function = shape_def
#     ch2.output.voltage.high = 5
#     ch2.output.voltage.low = 0
#     ch2.output_function.pulse.width = 1e-3

#     ch1.burst.enabled = True
#     ch2.burst.enabled = True
    
#     ch1.trigger.source = ks.TriggerSource.BUS
#     ch2.trigger.source = ks.TriggerSource.BUS
    
#     # ch1.output_function.pulse.width = 1e-3
#     # ch2.output_function.pulse.width = 1e-3
    
#     ch1.output.frequency = 1/interstim_delay
#     ch2.output.frequency = 1/interstim_delay

#     if not jitter:

#         ch1.burst.number_of_cycles = num_stims
#         ch2.burst.number_of_cycles = num_stims

#     else:
#         ch1.burst.number_of_cycles = 1
#         ch2.burst.number_of_cycles = 1

#     ch1.output.set_load_infinity()
#     ch2.output.set_load_infinity()

#     # ch1.phase_lock.synchronize_channels()
    
#     if interpulse_delay > 0:
    
#         ch1.trigger.delay = datetime.timedelta(0,0,0,0)
#         ch2.trigger.delay = datetime.timedelta(0,0,0,interpulse_delay)
#         # ch1.trigger.software_trigger

#     elif interpulse_delay < 0:
        
#         ch2.trigger.delay = datetime.timedelta(0,0,0,0)
#         ch1.trigger.delay = datetime.timedelta(0,0,0,abs(interpulse_delay))
#         # ch2.trigger.software_trigger
        
#     else:
#         ch1.trigger.delay = datetime.timedelta(0,0,0,0)
#         ch2.trigger.delay = datetime.timedelta(0,0,0,0)
#         # ch1.trigger.software_trigger
    

#     ch1.output.enabled = 1
#     ch2.output.enabled = 1

#     if jitter:
#         if interpulse_delay >= 0:
#             count = 0
#             while (count<=num_stims):
#                 ch1.trigger.software_trigger()
#                 rand = random.uniform(interstim_delay-jitter_rate, interstim_delay+jitter_rate) 
#                 time.sleep(rand)
#                 count +=1
#         else:
#             count = 0
#             while (count<=num_stims):
#                 ch2.trigger.software_trigger()
#                 rand = random.uniform(interstim_delay-jitter_rate, interstim_delay+jitter_rate) 
#                 time.sleep(rand)
#                 count +=1
                        
#     else:
#         if interpulse_delay >= 0:
#             ch1.trigger.software_trigger()
#         else:
#             ch2.trigger.software_trigger()
    
#     driver.close()

