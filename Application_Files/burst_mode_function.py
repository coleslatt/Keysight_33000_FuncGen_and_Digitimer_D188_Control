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


def burst_mode(interpulse_delay = 0, #ms
                interstim_delay = 1, #seconds
                num_stims = 10,
                jitter = False,
                jitter_rate = 0, #seconds
                ch1_ttl = True,
                ch1_shape = 'sine',
                DS5 = True,
                DS5_input_volt = 5,
                DS5_output_current = 50,
                DS5_desired_current = 1,
                v_min = -1,
                v_max = 1,
                vpp = 2,
                custom = 'no',
                ramp = 'yes',
                auto_k = True,
                k = 0.1,
                pph=0, # between 0-1
                ppw=0, # in ms
                pw = 1, # in ms
                channel = 1,
                state = 1,
                charge_balance = False,
                reverse = False   
              ):
    '''
    Configure and triggers burst mode on the Keysight 33512B for paired stimulation pulses.

    Channel 1 produces the first pulse in each pair. Channel 2 produces the second pulse,
    delayed by `interpulse_delay`.

    Parameters
    ----------
    interpulse_delay : float, default 0 (ms)
        Channel 2 trigger delay within each pair. Channel 2 will always come after channel 1,
        therefore this value must be positive.

    interstim_delay : float, default 1 (seconds)
        Controls the delay between each pair of pulses. Internally this is used to set the
        output frequency to 1 / interstim_delay.

    num_stims : int, default 10
        Total number of pulse pairs to generate.

    jitter : bool, default False
        If False, uses instrument burst mode to output `num_stims` cycles per trigger.
        If True, outputs one pulse pair per trigger and software-triggers repeatedly with
        a randomized delay between triggers.

    jitter_rate : float, default 0 (seconds)
        Jitter range applied when `jitter=True`. The sleep time between triggers is sampled
        uniformly from [interstim_delay - jitter_rate, interstim_delay + jitter_rate].

    ch1_ttl : bool, default True
        If True, configures Channel 1 as a 0–5 V TTL pulse with 1 ms width.

    ch2_ttl : bool, default True
        If True, configures Channel 2 as a 0–5 V TTL pulse with 1 ms width.

    Returns
    -------
    None
        This function configures the instrument, triggers output, and then closes the connection.
    '''




    # assert isinstance(trig_order, list), "trig_order must be a list"
    # assert len(trig_order) == num_steps, (
    #     f"trig_order must have length {num_steps}, got {len(trig_order)}"
    # )

    # assert all(isinstance(x, int) and x in (1, 2) for x in trig_order), "All values in trig_order must be integers equal to 1 or 2"

    # assert isinstance(delay_per_step, list), "delay_per_step must be a list"
    # assert len(delay_per_step) == num_steps, (
    #     f"delay_per_step must have length {num_steps}, got {len(delay_per_step)}"
    # )

    # assert isinstance(channel_per_step, list), "channel_per_step must be a list"
    # assert len(channel_per_step) == num_steps, (
    #     f"channel_per_step must have length {num_steps}, got {len(channel_per_step)}"
    # )

    # assert isinstance(trigs_per_step, list), "trigs_per_step must be a list"
    # assert len(trigs_per_step) == num_steps, (
    #     f"trigs_per_step must have length {num_steps}, got {len(trigs_per_step)}"
    # )

    resource_name = "33512B"
    id_query = True
    reset = False
    options = ""
    driver = ks.Kt33000(resource_name, id_query, reset, options)
    print('  identifier: ', driver.identity.identifier)
    print('  revision:   ', driver.identity.revision)
    print('  vendor:     ', driver.identity.vendor)
    print('  description:', driver.identity.description)
    print('  model:      ', driver.identity.instrument_model)
    print('  resource:   ', driver.driver_operation.io_resource_descriptor)
    print('  options:    ', driver.driver_operation.driver_setup)


    ch1 = driver.output_channels[0]
    ch2 = driver.output_channels[1]

    ch1.output.enabled = 0
    ch2.output.enabled = 0
    shape_def = ks.FunctionShape.PULSE

    if ch1_ttl:

        ch1.output_function.function = shape_def
        ch1.output.voltage.high = 5
        ch1.output.voltage.low = 0
        ch1.output_function.pulse.width = 1e-3
        
    else:

        if DS5:
            v_max = current_calc(DS5_desired_current,DS5_input_volt,DS5_output_current)    
            v_min = 0
            
        func_gen_control(
            shape = ch1_shape,
            freq =  1/interstim_delay,
            v_min = v_min,
            v_max = v_max,
            vpp = vpp,
            custom = custom,
            ramp = ramp,
            auto_k = auto_k,
            k = k,
            pph=pph, # between 0-1
            ppw=ppw, # in ms
            pw = pw, # in ms
            channel = 1,
            state = 1,
            charge_balance = charge_balance,
            reverse = reverse
            )

    # CH2 is always a TTL Trigger
    ch2.output_function.function = shape_def
    ch2.output.voltage.high = 5
    ch2.output.voltage.low = 0
    ch2.output_function.pulse.width = 1e-3

    ch1.burst.enabled = True
    ch2.burst.enabled = True
    
    ch1.trigger.source = ks.TriggerSource.BUS
    ch2.trigger.source = ks.TriggerSource.BUS
    
    # ch1.output_function.pulse.width = 1e-3
    # ch2.output_function.pulse.width = 1e-3
    
    ch1.output.frequency = 1/interstim_delay
    ch2.output.frequency = 1/interstim_delay

    if not jitter:

        ch1.burst.number_of_cycles = num_stims
        ch2.burst.number_of_cycles = num_stims

    else:
        ch1.burst.number_of_cycles = 1
        ch2.burst.number_of_cycles = 1

    ch1.output.set_load_infinity()
    ch2.output.set_load_infinity()

    # ch1.phase_lock.synchronize_channels()
    
    if interpulse_delay > 0:
    
        ch1.trigger.delay = datetime.timedelta(0,0,0,0)
        ch2.trigger.delay = datetime.timedelta(0,0,0,interpulse_delay)
        # ch1.trigger.software_trigger

    elif interpulse_delay < 0:
        
        ch2.trigger.delay = datetime.timedelta(0,0,0,0)
        ch1.trigger.delay = datetime.timedelta(0,0,0,abs(interpulse_delay))
        # ch2.trigger.software_trigger
        
    else:
        ch1.trigger.delay = datetime.timedelta(0,0,0,0)
        ch2.trigger.delay = datetime.timedelta(0,0,0,0)
        # ch1.trigger.software_trigger
    

    ch1.output.enabled = 1
    ch2.output.enabled = 1

    if jitter:
        count = 0
        while (count<=num_stims):
            ch1.trigger.software_trigger()
            rand = random.uniform(interstim_delay-jitter_rate, interstim_delay+jitter_rate) 
            time.sleep(rand)
            count +=1
                     
    else:
        if interpulse_delay >= 0:
            ch1.trigger.software_trigger()
        else:
            ch2.trigger.software_trigger()
    
    driver.close()

