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
    state = 0,
    arb_name: Literal["CARDIAC", "D_LORENTZ", "GAUSSIAN", "HAVERSINE", "LORENTZ", "NEG_RAMP", "SINC", "EXP_FALL", "EXP_RISE"] = "EXP_FALL",
    trigger = False,
    trigger_pw = 1e-3,
    d188 = False,
    d188_channel = 1,
    d188_led = True
    ):

    """
    Configure and optionally enable a Keysight 33512B output channel.

    This helper:
      * Opens a Keysight 33512B driver session (using resource name "33512B").
      * Selects output channel 1 or 2.
      * Configures waveform type, frequency, amplitude, and pulse width.
      * Optionally selects a built-in arbitrary waveform or a custom ARB mode.
      * Optionally configures channel 2 as a 0–5 V trigger output.
      * Optionally sends a command to an external D188 controller.
      * Prints a human-readable summary of the configuration and then closes
        the driver session.

    Parameters
    ----------
    freq : float, default 60
        Output frequency in hertz (Hz) for the main channel. Used for:
          * Standard waveforms (sine, square, ramp, triangle, pulse).
          * Arbitrary waveforms (ARB).
          * Channel 2 trigger output if ``trigger=True``.

    shape : {'sine', 'square', 'ramp', 'pulse', 'arb', 'arbitrary', 'triangle'}, \
            default 'sine'
        Waveform shape for the main output channel.
          * ``'sine'``: Sinusoidal waveform.
          * ``'square'``: Square wave.
          * ``'ramp'``: Sawtooth/ramp waveform.
          * ``'pulse'``: Pulse waveform (uses ``pw`` as pulse width).
          * ``'triangle'``: Triangle wave.
          * ``'arb'`` or ``'arbitrary'``: Arbitrary waveform mode. If
            ``custom == 'no'`` a built-in ARB waveform named by ``arb_name``
            is selected. If ``custom == 'yes'``, the channel is left in
            ARB mode for a user-defined arbitrary waveform (custom
            generator currently commented out).

    v_min : float, default -1
        Low (minimum) output level in volts for the main channel.
        Together with ``v_max`` this defines the DC levels for non-ARB
        waveforms. If both ``v_min == -1`` and ``v_max == 1`` (their
        defaults) and ``vpp`` is changed away from 2, then
        ``v_min`` and ``v_max`` are recomputed as ``± vpp / 2`` and
        those values are applied instead.

    v_max : float, default 1
        High (maximum) output level in volts for the main channel.
        See ``v_min`` and ``vpp`` for how the three interact.

    vpp : float, default 2
        Peak-to-peak amplitude in volts. If ``vpp != 2`` while
        ``v_min == -1`` and ``v_max == 1``, the function derives
        symmetric levels:
        ``v_min = -vpp/2``, ``v_max = +vpp/2``.
        If you explicitly override ``v_min`` and/or ``v_max``, those
        explicit levels are used and ``vpp`` is treated as informational.

    custom : str, {'yes', 'no'}, default 'no'
        Custom arbitrary waveform mode flag.
          * ``'no'``: Use standard shapes or built-in ARB waveforms.
          * ``'yes'``: Put the main channel into ARB mode for a user-defined
            waveform and set ARB rate units to frequency. (The actual
            custom waveform creation / download is currently commented out
            and must be implemented separately.)
        The string is compared case-insensitively; values like "no", "NO",
        "false", "0" are treated as disabled in the verbose summary.

    pph : float, default 0
        Pre-pulse height parameter for custom ARB waveforms (dimensionless).
        Intended to represent either:
          * A fraction of the main pulse amplitude if ``0 <= pph <= 1``
            (interpreted as a percentage in the summary), or
          * A relative/absolute amplitude parameter if outside [0, 1].
        Currently used only in the verbose summary and for potential future
        custom ARB generation.

    ppw : float, default 0
        Pre-pulse width parameter for custom ARB waveforms. Interpreted as:
          * A fraction of the main pulse width when ``0 <= ppw <= 1``, or
          * A duration in seconds when outside [0, 1] (formatted as ms/µs
            in the summary).
        As with ``pph``, currently used only in the verbose summary and for
        potential custom ARB generation.

    pw : float, default 1e-3
        Pulse width for the main channel, in seconds.
          * For ``shape == 'pulse'``, this is applied to
            ``ch.output_function.pulse.width``.
          * For custom ARB modes, it is intended to describe the total
            duration of the complex pulse (used by the custom waveform
            helpers when enabled).

    channel : int, {1, 2}, default 1
        Main output channel to configure (1-based index).
          * ``1`` → channel index 0 in the underlying driver.
          * ``2`` → channel index 1 in the underlying driver.
        Any other value raises ``ValueError``.

    state : int, {0, 1}, default 0
        Output enable state for the main channel.
          * ``1`` → turn the main channel output ON (and, if
            ``trigger=True``, also enable the trigger channel and
            phase-lock / synchronize channels).
          * ``0`` → turn the main channel output OFF (and, if
            ``trigger=True``, also disable the trigger channel).
        Any other value raises ``ValueError``.

    arb_name : Literal["CARDIAC", "D_LORENTZ", "GAUSSIAN", "HAVERSINE",
                       "LORENTZ", "NEG_RAMP", "SINC", "EXP_FALL", "EXP_RISE"], \
                default "EXP_FALL"
        Name of a built-in arbitrary waveform stored in instrument memory.
        Used only when:
          * ``shape in {'arb', 'arbitrary'}``, and
          * ``custom == 'no'``.
        In that case the existing arbitrary waveform is cleared and the
        specified built-in ARB file
        ``INT:\\BUILTIN\\{arb_name}.arb`` is opened and selected, and its
        frequency is set to ``freq``.

    trigger : bool, default False
        If ``True``, configure channel 2 as a 0–5 V pulse train that can be
        used as a trigger:
          * Channel 2 is set to pulse shape with frequency ``freq``.
          * Channel 2 levels are 0 V (low) and 5 V (high).
          * Channel 2 pulse width is fixed at 1 ms.
          * Channel 2 load is set to high impedance.
          * When ``state == 1``, both channels are enabled and the generator
            attempts to synchronize channel phase.
        If ``False``, channel 2 is explicitly disabled.

    d188 : bool, default False
        If ``True``, send a command to an attached Digitimer D188 (or
        compatible) device via ``D188_Controller(d188_channel, d188_led)``.
        The precise behavior depends on your implementation of
        ``D188_Controller`` (not defined in this function).

    d188_channel : int, default 1
        D188 output channel to select when ``d188=True``. Must be an
        integer in the range 1–8 inclusive. Any value outside this range
        raises ``ValueError``.

    d188_led : bool, default True
        Desired state of the D188 front-panel LED when ``d188=True``.
        Interpreted and applied by ``D188_Controller``. Also reported as
        ``ON``/``OFF`` in the verbose summary.

    Behavior
    --------
    - Creates a new Keysight driver instance with:
        ``resource_name='33512B', id_query=True, reset=False``.
    - Selects the specified output channel and sets its load to infinity
      (high impedance).
    - Maps ``shape`` to the corresponding Keysight ``FunctionShape`` and
      configures the main channel waveform accordingly.
    - If ``custom == 'yes'``, puts the main channel in ARB mode and sets
      ARB rate units to frequency, leaving room for user-defined waveform
      download (currently commented out).
    - If ``shape in {'arb', 'arbitrary'}`` and ``custom == 'no'``, clears the
      current arbitrary waveform and selects the built-in waveform named
      by ``arb_name``.
    - Applies ``freq``, voltage levels (via ``v_min``, ``v_max``, ``vpp``),
      and pulse width (for pulse shape).
    - If ``trigger == True``, configures channel 2 as a 0–5 V, 1 ms-wide
      pulse train at frequency ``freq`` and synchronizes channels when
      enabling output.
    - If ``d188 == True``, calls ``D188_Controller(d188_channel, d188_led)``.
    - Prints a detailed, human-readable configuration summary (including
      units and descriptive labels) to stdout.
    - Closes the driver session before returning.

    Returns
    -------
    None
        The function configures the instrument via side effects and prints
        a summary; it does not return a value.

    Raises
    ------
    ValueError
        If ``shape`` is not one of the supported values.
        If ``channel`` is not 1 or 2.
        If ``state`` is not 0 or 1.
        If ``d188_channel`` is not an integer in the range 1–8 when
        ``d188 == True``.

    Notes
    -----
    - This function opens and closes a new driver session on every call.
      If you need high-throughput or repeated reconfiguration, you may want
      to refactor it to accept an existing ``ks.Kt33000`` driver instance
      instead of creating a new one internally.
    - The custom ARB waveform generation is currently stubbed out; enabling
      it requires implementing and calling a helper such as
      ``custom_waveform_pp2``.
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
        ch2.output_function.pulse.width = trigger_pw
        
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

    ])

    if trigger:
        summary_lines.append(f"  Trigger Pulse Width:  {_format_pw(trigger_pw)}")
    
    summary_lines.extend([
        f"  D188 Control:         {_yes_no(d188)}",
    ])
    
    if d188:
        summary_lines.extend([
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

    