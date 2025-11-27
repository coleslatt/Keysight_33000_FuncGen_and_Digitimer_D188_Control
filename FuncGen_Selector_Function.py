import keysight_kt33000 as ks
import numpy as np
from typing import Literal

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
        



def custom_waveform_pp(ch,
                       freq=60,
                       pw = 1e-3,
                       pph = 0, # value between 0-1
                       ppw = 0 # in seconds
                      ):
    pw=pw
    freq = freq
    period = 1.0/freq
    num_points=100000
    time_per_point = period/num_points
    func_name = 'custom'
    ch.output_function.arbitrary_waveform.clear()
    pulse_points = int(pw/time_per_point)
    square_samples = np.empty(num_points, dtype=">f4")

    prepulse_points = int(ppw/time_per_point)

    square_samples[:prepulse_points] = pph
    square_samples[prepulse_points:pulse_points+prepulse_points] = 1
    square_samples[pulse_points+prepulse_points:] = 0
    
    # 2. View the same buffer as bytes (uint8)
    square_bytes = square_samples.view(np.uint8)
    
    # 3. Download to channel 1 arb memory
    # ch1 is your Kt33000OutputChannel instance, as you had earlier
    ch.output_function.arbitrary_waveform.load_arb_waveform(
        name=func_name,      # up to 12 chars, no extension needed
        data=square_bytes
    )
    
    ch.output_function.arbitrary_waveform.select_arb_waveform(func_name)
    ch.output_function.arbitrary_waveform.frequency = freq

    
def func_gen_control(
    freq = 60,
    shape = 'sine',
    v_min = -1,
    v_max = 1,
    vpp = 2,
    custom = 'no',
    pph=0,
    ppw=0,
    pw = 1e-3,
    channel = 1,
    state = 1,
    arb_name: Literal["CARDIAC", "D_LORENTZ", "GAUSSIAN", "HAVERSINE", "LORENTZ", "NEG_RAMP", "SINC", "EXP_FALL", "EXP_RISE"] = "EXP_FALL",
    trigger = False,
    d188 = False,
    d188_channel = 1,
    d188_led = True
    ):

    """
    Configure and enable/disable a Keysight 33512B output channel.

    This helper wraps common settings for the function generator, including
    waveform shape, frequency, voltage levels, channel selection, and optional
    arbitrary waveform loading. It assumes a global `driver` object
    (ks.Kt33000 instance), a global `ks` module (keysight_kt33000), and NumPy
    imported as `np`.

    Parameters
    ----------
    freq : float, default 60
        Output frequency in Hz. Used both for standard waveforms and
        arbitrary waveforms.
    shape : {'sine', 'square', 'ramp', 'pulse', 'arb', 'arbitrary', 'triangle'}, default 'sine'
        Waveform shape to generate. 'arb' / 'arbitrary' selects arbitrary
        waveform mode on the instrument.
    v_min : float, default -1
        Low output voltage level in volts. Ignored if left at the default
        together with `v_max` and `vpp` is changed; in that case v_min/v_max
        are recomputed from `vpp`.
    v_max : float, default 1
        High output voltage level in volts. See `v_min` and `vpp`.
    vpp : float, default 2
        Peak-to-peak voltage. If `vpp` is not 2 while `v_min == -1` and
        `v_max == 1`, then v_min/v_max are set to +/- vpp/2. Otherwise the
        explicitly provided `v_min` and `v_max` are used.
    custom : {'yes', 'no'}, default 'no'
        Whether to load a custom arbitrary waveform generated in Python.
        If 'yes' and `shape` is arbitrary, an internal pulse-like waveform
        is generated and loaded into volatile memory.
    pw : float, default 1e-3
        Pulse width in seconds. Used for pulse waveforms and for the internal
        arbitrary waveform generator.
    channel : int, {1, 2}, default 1
        Output channel to configure (1-based index).
    state : {0, 1}, default 1
        Whether to turn the selected channel output on or off.
    arb_name : Literal["CARDIAC", "D_LORENTZ", "GAUSSIAN", "HAVERSINE", "LORENTZ",
                       "NEG_RAMP", "SINC", "EXP_FALL", "EXP_RISE"], default "EXP_FALL"
        Name of a built-in arbitrary waveform to load from instrument
        memory when `shape == 'arb'` and `custom == 'no'`.

    Behavior
    --------
    - Maps `shape` to the corresponding Keysight `FunctionShape`.
    - Selects channel 1 or 2 from the global `driver`.
    - Sets the output load to infinity (high impedance).
    - If `custom == 'yes'`, generates an internal pulse-like arbitrary
      waveform, loads it into memory, and selects it.
    - If `shape == 'arb'` and `custom == 'no'`, clears the existing arbitrary
      waveform and selects the specified built-in arbitrary waveform `arb_name`.
    - Sets frequency, waveform shape, pulse width (for pulse shape), and
      high/low voltage levels.
    - Enables or disables the channel output according to `state`.
    - Sets the display ARB rate units to frequency.

    Raises
    ------
    ValueError
        If `shape` is not one of the supported strings.
        If `channel` is not 1 or 2.
        If `state` is not 'on' or 'off'.

    Notes
    -----
    This function configures the instrument via side effects on the global
    `driver` and does not return a value.
    """
    
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
    
    # ch1 = driver.output_channels[0]  

    if shape == 'sine':
        shape_def = ks.FunctionShape.SINUSOID
    elif shape == 'square':
        shape_def = ks.FunctionShape.SQUARE
    elif shape == 'ramp':
        shape_def = ks.FunctionShape.RAMP
    elif shape == 'pulse':
        shape_def = ks.FunctionShape.PULSE
    elif shape in ('arb', 'arbitrary'):
        shape_def = ks.FunctionShape.ARBITRARY
    elif shape == 'triangle':
        shape_def = ks.FunctionShape.TRIANGLE
    else:
        raise ValueError(
            f"Unknown shape '{shape}'. Must be one of "
            f"'sine', 'square', 'ramp', 'pulse', 'arb', 'arbitrary', 'triangle'."
        )
    
    if (channel==1):
        ch = driver.output_channels[0]
    elif (channel==2):
        ch = driver.output_channels[1]
    else:
        raise ValueError('Channel selection is invalid, must be 1 or 2')  

    ch.output.enabled = 0

    if not trigger:
        ch2 = driver.output_channels[1]
        ch2.output.enabled = 0
        
        
    ch.output.set_load_infinity()

    # if (custom == 'yes'):
    #     ch.output_function.function = ks.FunctionShape.ARBITRARY
    #     driver.display.arb_rate_unit = ks.DisplayARBRateUnits.FREQUENCY
    #     custom_waveform_pp(ch=ch,
    #                       freq=freq,
    #                       pw=pw,
    #                       pph=pph,
    #                       ppw=ppw)

    if (custom == 'yes'):
        ch.output_function.function = ks.FunctionShape.ARBITRARY
        driver.display.arb_rate_unit = ks.DisplayARBRateUnits.FREQUENCY
        # custom_waveform_pp2(ch=ch,
        #                     freq = freq,
        #                     pw   = pw,  # total duration of the complex pulse
        #                     h1   = pph,
        #                     w    = ppw,
        #                     ch_level = 1.0)
        
    else:
        ch.output_function.function = shape_def
        ch.output.frequency = freq
        ch.output_function.arbitrary_waveform.frequency = freq

        if (shape == 'pulse'):
            ch.output_function.pulse.width = pw

        if shape in ('arb', 'arbitrary'):
            driver.display.arb_rate_unit = ks.DisplayARBRateUnits.FREQUENCY

    if (shape == 'arb') & (custom == 'no'):
        ch.output_function.arbitrary_waveform.clear()
        if (arb_name != 'ARB_RISE'):
            ch.output_function.arbitrary_waveform.open_arb_waveform(rf'INT:\BUILTIN\{arb_name}.arb')
        ch.output_function.arbitrary_waveform.select_arb_waveform(rf'INT:\BUILTIN\{arb_name}.arb')
        ch.output_function.arbitrary_waveform.frequency = freq

    if (vpp != 2) & (v_min == -1) & (v_max == 1):
        v_min = -(vpp/2)
        v_max = (vpp/2)

    ch.output.voltage.high = v_max
    ch.output.voltage.low = v_min

    if trigger:
        ch2 = driver.output_channels[1]
        ch2.output.enabled = 0
        ch2.output.set_load_infinity()
        ch2.output_function.function = ks.FunctionShape.PULSE
        ch2.output.frequency = freq
        ch2.output.voltage.high = 5
        ch2.output.voltage.low = 0
        ch2.output_function.pulse.width = 1e-3
        
    if (state == 1):
        ch.output.enabled = 1
        if trigger:
            ch2.output.enabled = 1
            ch.phase_lock.synchronize_channels()
        
    elif (state == 0):
        ch.output.enabled = 0
        if trigger:
            ch2.output.enabled = 0
        
    else:
        raise ValueError('State selection is invalid, must be on or off')

    if d188:
        if (isinstance(d188_channel, int) and 1 <= d188_channel <= 8):
            D188_Controller(d188_channel,d188_led)
        else:
            raise ValueError('D188 Channel Selection is invalid, must be between 1-8')
        

 
        # --- Verbose human-readable summary of the configuration in effect ---

    def _yes_no(value, yes="Enabled", no="Disabled"):
        return yes if value else no

    def _on_off(value):
        return "ON" if value else "OFF"

    def _format_pw(seconds: float) -> str:
        """Format a pulse width in seconds as ms or µs."""
        if seconds is None:
            return "N/A"
        ms = seconds * 1e3
        if ms >= 1:
            return f"{ms:g} ms"
        else:
            us = seconds * 1e6
            return f"{us:g} µs"

    # Pre-pulse height: treat 0–1 as a fraction of main amplitude
    if 0 <= pph <= 1:
        pph_desc = f"{pph * 100:.1f} % of main amplitude"
    else:
        pph_desc = f"{pph:g} (relative units)"

    # Pre-pulse width: treat 0–1 as fraction of main width
    if 0 <= ppw <= 1:
        ppw_desc = f"{ppw * 100:.1f} % of main pulse width"
    else:
        ppw_desc = _format_pw(ppw)

    # Custom waveform mode: simple heuristic
    custom_str = str(custom).lower()
    if custom_str in ("no", "none", "false", "0"):
        custom_desc = "Disabled"
    else:
        custom_desc = f"Enabled (mode='{custom}')"

    custom_enabled = custom_str not in ("no", "none", "false", "0")


    summary_lines = [
    "",
    "=== Function Generator Configuration ===",
    f"  Frequency:            {freq:g} Hz",
    f"  Waveform Shape:       {shape!r}",
    f"  High Level:           {v_max:.3g} Volts",
    f"  Low  Level:           {v_min:.3g} Volts",
    f"  Amplitude (Vpp):      {vpp:.3g} Volts peak-to-peak",
    f"  Pulse Width:          {_format_pw(pw)}",
    f"  Custom Waveform:      {custom_desc}",
]

    # Only show pre-pulse parameters when custom waveform is enabled
    if custom_enabled:
        summary_lines.extend([
            f"  Pre-pulse Height:     {pph_desc}",
            f"  Pre-pulse Width:      {ppw_desc}",
        ])

    summary_lines.extend([
        f"  Output Channel:       CH{channel}",
        f"  Output State:         {_on_off(state)}",
        f"  Arb Waveform Name:    {arb_name!r}",
        f"  External Trigger:     {_yes_no(trigger)}",
        f"  D188 Control:         {_yes_no(d188)}",
        f"  D188 Channel:         {d188_channel}",
        f"  D188 Front-panel LED: {_on_off(d188_led)}",
        "========================================",
        "",
    ])


    summary = "\n".join(summary_lines)
    print(summary)
    # If you ever want to use this string programmatically, you could also:
    # return summary


    driver.close()
    return

from dataclasses import dataclass, asdict, replace

@dataclass
class FuncGenDefaults:
    freq: float = 60
    shape: str = "sine"
    v_min: float = -1
    v_max: float = 1
    vpp: float = 2
    custom: str = "no"
    pph: float = 0.0
    ppw: float = 0.0
    pw: float = 1e-3
    channel: int = 1
    state: int = 1
    arb_name: Literal[
        "CARDIAC",
        "D_LORENTZ",
        "GAUSSIAN",
        "HAVERSINE",
        "LORENTZ",
        "NEG_RAMP",
        "SINC",
        "EXP_FALL",
        "EXP_RISE",
    ] = "EXP_FALL"
    trigger: bool = False
    d188: bool = False
    d188_channel: int = 1
    d188_led: bool = True


# baseline and current “sticky” defaults
_BASE_DEFAULTS = FuncGenDefaults()
_current_defaults = FuncGenDefaults()


def func_gen_control_stateful(
    reset: bool = False,
    **overrides,
):
    """
    Stateful wrapper around func_gen_control.

    - On the first call, uses the baseline defaults in FuncGenDefaults.
    - On each call, only the parameters you pass in `overrides` are changed.
      All other parameters keep their last-used values.
    - If `reset=True`, the stored defaults are reset back to the baseline.

    Parameters are the same as func_gen_control; pass them as keyword args.
    Example:
        func_gen_control_stateful(freq=100, shape="pulse")
        func_gen_control_stateful(freq=200)      # shape stays "pulse"
        func_gen_control_stateful(reset=True)    # back to clean defaults
    """
    global _current_defaults

    # Basic guard: only allow known fields
    valid_keys = set(FuncGenDefaults.__annotations__.keys())
    unknown = set(overrides) - valid_keys
    if unknown:
        raise TypeError(f"Unknown parameter(s): {', '.join(sorted(unknown))}")

    if reset:
        _current_defaults = FuncGenDefaults()

    # Update stored defaults with what the user passed
    _current_defaults = replace(_current_defaults, **overrides)

    # Call the real function with the full parameter set
    return func_gen_control(**asdict(_current_defaults))

    