# Keysight_33000_FuncGen_and_Digitimer_D188_Control
A simple package for controlling a Keysight 33000 Series Function Generator and a Digitimer D188, for lab use in stimulation studies.

      * Opens a Keysight 33512B driver session (using resource name "33512B").
      * Selects output channel 1 or 2.
      * Configures waveform type, frequency, amplitude, and pulse width.
      * Optionally selects a built-in arbitrary waveform or a custom ARB mode.
      * Optionally configures channel 2 as a 0–5 V trigger output.
      * Optionally sends a command to an external D188 controller.
      * Prints a human-readable summary of the configuration and then closes
        the driver session.

## Installation

** Make sure you've installed the Keysight Library Suite here: https://www.keysight.com/find/iosuite

Notes:

On some systems and UBC computers, there may be security features that prevent you from running scripts. If there are problems running the setup file or activating the python virtual environment in Powershell, run:
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```


1. Using Windows Powershell, clone the repo with:
```
git clone https://github.com/coleslatt/Keysight_33000_FuncGen_and_Digitimer_D188_Control.git
```

2. In Powershell, navigate to your repo directory with (replace with your own path):
```
cd "C:\your\path\to\Keysight_33000_FuncGen_and_Digitimer_D188_Control"
```

3. Run setup script with:
```
.\setup_env.ps1
```
## Usage

Notes (REMINDER!):

On some systems and UBC computers, there may be security features that prevent you from running scripts. If there are problems running the setup file or activating the python virtual environment in Powershell, run:
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

1. In Powershell, navigate to your repo directory with (replace with your own path):
```
cd "C:\your\path\to\Keysight_33000_FuncGen_and_Digitimer_D188_Control"
```
2. Activate your Python virtual environment with:
```
.\.venv\Scripts\Activate.ps1
```

3. Ensure you are using the correct Python version by running:
```
$Python = ".\.venv\Scripts\python.exe"
```

4. On Windows, ensure you are not referencing another Python installation by running:
```
Remove-Item Alias:python -ErrorAction SilentlyContinue
$ExecutionContext.InvokeCommand.CommandNotFoundAction = $null
```
## User Interface Initiation

1. Start user interface with:
```
& $Python .\Application_Files\Controller.py
```

### Burst Mode Function

1. Follow the above steps to set up your environment.

2. Navigate to Application_Files folder with:

```
cd Application_Files
```

3. Run this to start burst mode function:
```
python
from burst_mode_function import burst_mode
```

4. Use this as the function caller, changing parameters as needed:

```
burst_mode(num_stims = 50, 
           interpulse_delay= 10,
           interstim_delay = 0.1,
           jitter = 0,
           jitter_rate = 0.001,
           ch1_ttl = 1,
           ch1_shape = 'pulse',
            DS5 = True,
            DS5_input_volt = 5,
            DS5_output_current = 50,
            DS5_desired_current = 50,
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
            charge_balance = True,
            reverse = False
          )
```


### Hardware Setup

1. 









### List of Parameters

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

### Behavior

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



