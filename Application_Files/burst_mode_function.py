import keysight_kt33000 as ks
import numpy as np
from typing import Literal
import datetime
import csv
import random
import time
from pathlib import Path
from FuncGen_Selector_Function_2 import func_gen_control


# The Keysight documentation notes that changing OUTPut operates a physical
# relay and that the signal can take about 1 ms to stabilize.  Keep later
# abort/burst commands well outside that transition so they cannot leak through
# a relay that is still opening or closing.
OUTPUT_RELAY_SETTLE_S = 0.010

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
        # print(f"\rRemaining time: {remaining:6.2f} s", end="", flush=True)
        time.sleep(min(chunk_s, max(0.0, remaining)))
    print ("[_sleep_with_stop] Ended")
    print("\n")
    return _stop_requested(stop_event)


def _wait_until_with_stop(
    deadline_s: float,
    stop_event=None,
    *,
    sleep_chunk_s: float = 0.005,
    spin_window_s: float = 0.001,
) -> bool:
    """Wait for an absolute ``perf_counter`` deadline with low scheduler jitter.

    Most of the wait is cooperative so a Stop request remains responsive.  The
    final short window is a busy wait, avoiding the relatively large and
    variable overshoot of ``time.sleep`` on Windows.

    Returns True if stopped while waiting, otherwise False.
    """
    while True:
        if _stop_requested(stop_event):
            return True

        remaining_s = deadline_s - time.perf_counter()
        if remaining_s <= 0:
            return False

        if remaining_s > spin_window_s:
            sleep_s = min(sleep_chunk_s, remaining_s - spin_window_s)
            stop_wait = getattr(stop_event, "wait", None)
            if callable(stop_wait):
                if stop_wait(sleep_s):
                    return True
            else:
                time.sleep(sleep_s)
        # For the final spin window, loop on perf_counter without yielding the
        # thread. This costs a small amount of CPU but improves trigger timing.

def _estimated_run_time(num_stims, freq):
    # A triggered burst contains ``num_stims`` complete waveform cycles.  Waiting
    # for all of them keeps the worker (and therefore the Stop button) alive
    # until the instrument has actually finished its burst.
    return num_stims / freq


def _settle_output_relay(
    driver,
    settle_s=OUTPUT_RELAY_SETTLE_S,
    *,
    wait_for_operation=True,
):
    """Wait for an output-relay command and its electrical settling time."""
    operation_error = None
    try:
        if driver is not None and wait_for_operation:
            driver.system.wait_for_operation_complete(
                datetime.timedelta(seconds=1)
            )
    except Exception as exc:
        operation_error = exc
    finally:
        # *OPC completion does not by itself guarantee that the connector has
        # passed the documented approximately 1 ms output-settling interval.
        time.sleep(max(0.0, float(settle_s)))

    if operation_error is not None:
        raise operation_error


def _shutdown_burst_channels(
    ch1,
    ch2,
    *,
    driver=None,
    abort_active=True,
    disconnect_before_abort=False,
):
    """
    Best-effort shutdown for both function-generator channels.

    This is deliberately called from the burst worker thread.  Keeping all
    driver access on one thread prevents Stop from racing an in-progress
    configuration or trigger command.
    """
    cleanup_errors = []

    def _abort_trigger_system():
        """One abort applies to both channels on a two-channel 33512B."""
        abort_channel = ch1 if ch1 is not None else ch2
        try:
            if abort_channel is not None:
                abort_channel.trigger.abort()
        except Exception as exc:
            cleanup_errors.append(f"trigger abort: {exc}")

    def _disconnect_outputs():
        for channel_name, channel in (("CH1", ch1), ("CH2", ch2)):
            if channel is None:
                continue
            try:
                channel.output.enabled = 0
            except Exception as exc:
                cleanup_errors.append(f"{channel_name} output disable: {exc}")

        # Do not change burst mode while the output relay may still be moving.
        # Otherwise disabling burst can briefly expose continuously playing ARB
        # data through a relay that has not physically opened yet.
        try:
            _settle_output_relay(
                driver,
                # Waiting for global operation completion during an active
                # finite burst can wait for the burst itself. OUTPUT OFF plus
                # the relay guard keeps interrupted Stop responsive.
                wait_for_operation=not (
                    abort_active and disconnect_before_abort
                ),
            )
        except Exception as exc:
            cleanup_errors.append(f"output relay settle: {exc}")

    # During an interrupted CSV burst, disconnect the electrical outputs before
    # resetting the ARB phase with ABORt.  This prevents that abrupt phase jump
    # from being delivered to the downstream stimulator.  Other modes retain
    # abort-first behavior so an active non-CSV burst is halted immediately.
    if abort_active and not disconnect_before_abort:
        _abort_trigger_system()

    _disconnect_outputs()

    if abort_active and disconnect_before_abort:
        _abort_trigger_system()

    # Leave burst mode disabled so a later trigger cannot resume the old run.
    for channel_name, channel in (("CH1", ch1), ("CH2", ch2)):
        if channel is None:
            continue
        try:
            channel.burst.enabled = False
        except Exception as exc:
            cleanup_errors.append(f"{channel_name} burst disable: {exc}")

    # With output and burst disabled, return the trigger system to its normal
    # idle source.  This avoids leaving a stale BUS-triggered run armed.
    for channel_name, channel in (("CH1", ch1), ("CH2", ch2)):
        if channel is None:
            continue
        try:
            channel.trigger.source = ks.TriggerSource.IMMEDIATE
        except Exception as exc:
            cleanup_errors.append(f"{channel_name} trigger source reset: {exc}")

    for cleanup_error in cleanup_errors:
        print(f"Cleanup warning: {cleanup_error}")

    return not cleanup_errors


def _export_burst_delay_log(delay_rows):
    log_dir = Path(__file__).resolve().parent.parent / "Burst_Logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")
    log_path = log_dir / f"{timestamp}_burst_delay_log.csv"

    with log_path.open("w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Stim_Number", "Delay (Seconds)"])
        writer.writerows(delay_rows)

    print(f"Burst delay log created: {log_path}")
    return log_path


def load_pulse_delay_waveform(
    *,
    ch,
    driver,
    pulse_delay_values_ms,
    pulse_width_ms,
    freq,
    v_min=0,
    v_max=5,
    waveform_name="PULSECSV",
    sample_count=1000000,
    sample_rate_hz=100000.0,
    trailing_settling_ms=5.0,
):
    """
    Build and download one arbitrary waveform from pulse delays.

    Each CSV delay value is the low-time after a pulse ends before the next
    pulse starts. A list of N delays therefore creates N + 1 pulses.
    ``sample_rate_hz`` defines the sample interval independently of ``freq``.
    One downloaded waveform represents one complete stimulation period: it
    starts with five low samples, contains the requested pulses and delays, and
    is padded low through the end of the period. Repeating that waveform in a
    hardware-timed N-cycle burst therefore preserves both the intra-stim pulse
    timing and the requested start-to-start stimulation period. ``sample_count``
    is the maximum number of points that may be downloaded.
    """
    pulse_delay_values_ms = [float(delay_ms) for delay_ms in pulse_delay_values_ms]
    pulse_width_ms = float(pulse_width_ms)
    freq = float(freq)
    sample_count = int(sample_count)
    sample_rate_hz = float(sample_rate_hz)
    trailing_settling_ms = float(trailing_settling_ms)

    if freq <= 0:
        raise ValueError("freq must be > 0.")
    if pulse_width_ms <= 0:
        raise ValueError("pulse_width_ms must be > 0.")
    if sample_count < 8:
        raise ValueError("sample_count must be at least 8 points.")
    if sample_rate_hz <= 0:
        raise ValueError("sample_rate_hz must be > 0.")
    if trailing_settling_ms <= 0:
        raise ValueError("trailing_settling_ms must be > 0.")
    if any(delay_ms < 0 for delay_ms in pulse_delay_values_ms):
        raise ValueError("pulse_delay_values_ms values must be >= 0.")

    period = 1.0 / freq
    time_per_point = 1.0 / sample_rate_hz

    pulse_starts_ms = [0.0]
    current_start_ms = 0.0
    for delay_ms in pulse_delay_values_ms:
        current_start_ms += pulse_width_ms + delay_ms
        pulse_starts_ms.append(current_start_ms)

    waveform_duration_ms = pulse_starts_ms[-1] + pulse_width_ms
    if waveform_duration_ms <= 0:
        raise ValueError("Generated waveform duration must be > 0.")

    leading_low_points = 5
    pulse_ranges = []
    for start_ms in pulse_starts_ms:
        start_idx = leading_low_points + int(
            round(start_ms * 1e-3 / time_per_point)
        )
        end_idx = leading_low_points + int(
            round((start_ms + pulse_width_ms) * 1e-3 / time_per_point)
        )
        end_idx = max(start_idx + 1, end_idx)
        pulse_ranges.append((start_idx, end_idx))

    last_end_idx = pulse_ranges[-1][1]
    trailing_low_points = max(
        1,
        int(round(trailing_settling_ms * 1e-3 / time_per_point)),
    )
    minimum_waveform_points = last_end_idx + trailing_low_points
    period_sample_count = int(round(period * sample_rate_hz))
    if period_sample_count < 8:
        raise ValueError(
            "The selected stimulation period is shorter than the minimum "
            "8-point arbitrary waveform."
        )
    if minimum_waveform_points > period_sample_count:
        raise ValueError(
            "Pulse delay waveform, including its leading and trailing low "
            "samples, exceeds one period at the selected frequency."
        )
    if period_sample_count > sample_count:
        raise ValueError(
            "One complete stimulation period requires "
            f"{period_sample_count} points, exceeding the configured maximum "
            f"of {sample_count} points at {sample_rate_hz:g} Sa/s."
        )

    # Include the entire interstim period in one waveform cycle. The portion
    # after the final pulse remains low, so hardware cycle repetition defines
    # the next stimulation onset without any per-stim software trigger latency.
    trimmed_sample_count = period_sample_count
    downloaded_duration_s = trimmed_sample_count * time_per_point

    waveform = np.full(trimmed_sample_count, -1.0, dtype=">f4")
    for start_idx, end_idx in pulse_ranges:
        waveform[start_idx:end_idx] = 1.0

    waveform_bytes = waveform.view(np.uint8)
    waveform_freq = sample_rate_hz / trimmed_sample_count
    total_trailing_low_ms = (
        (trimmed_sample_count - last_end_idx) * time_per_point * 1e3
    )

    ch.output_function.function = ks.FunctionShape.ARBITRARY
    driver.display.arb_rate_unit = ks.DisplayARBRateUnits.FREQUENCY
    ch.output_function.arbitrary_waveform.clear()
    ch.output_function.arbitrary_waveform.load_arb_waveform(
        name=waveform_name,
        data=waveform_bytes,
    )
    ch.output_function.arbitrary_waveform.select_arb_waveform(waveform_name)
    # Pulse edges must not be reconstructed with the ARB interpolation filter.
    # Even the driver's default STEP filter can introduce pre-/overshoot around
    # a discontinuity, which appears as a negative pulse before the train and
    # small extra pulses after an edge on a sensitive downstream trigger.
    ch.output_function.arbitrary_waveform.interpolation_enabled = (
        ks.ArbWaveformInterpolation.OFF
    )
    ch.output_function.arbitrary_waveform.frequency = waveform_freq
    ch.output.frequency = waveform_freq
    ch.output.voltage.high = v_max
    ch.output.voltage.low = v_min

    print(
        f"Loaded {waveform_name}: {len(pulse_starts_ms)} pulses, "
        f"pulse_width={pulse_width_ms} ms, duration={waveform_duration_ms} ms, "
        f"trailing_low={total_trailing_low_ms} ms, "
        f"sample_rate={sample_rate_hz} Sa/s, frequency={waveform_freq} Hz, "
        f"downloaded_points="
        f"{trimmed_sample_count}/{sample_count}"
    )

    return {
        "pulse_count": len(pulse_starts_ms),
        "duration_ms": waveform_duration_ms,
        "frequency_hz": waveform_freq,
        "requested_frequency_hz": freq,
        "sample_rate_hz": sample_rate_hz,
        "downloaded_duration_ms": downloaded_duration_s * 1e3,
        "occupied_points": last_end_idx,
        "downloaded_points": trimmed_sample_count,
        "leading_low_points": leading_low_points,
        "trailing_low_points": trimmed_sample_count - last_end_idx,
        "trailing_settling_ms": total_trailing_low_ms,
        "minimum_trailing_settling_ms": trailing_low_points * time_per_point * 1e3,
    }



def burst_mode(
    interpulse_delay=0,   # ms
    interstim_delay=1,    # seconds
    num_stims=10,
    jitter=False,
    jitter_rate=0,        # seconds
    jitter_quantize=0.0001,
    pulse_delay_values_ms=None,
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
    hardware_enabled=True,
):
    """
    Configure and trigger paired-pulse burst-mode output on a Keysight 33512B.

    stop_event:
        Optional threading.Event-like object. If set, the function exits early
        and performs cleanup before returning.
    """
    if pulse_delay_values_ms is not None:
        pulse_delay_values_ms = [float(delay_ms) for delay_ms in pulse_delay_values_ms]

    assert interstim_delay > 0, "interstim_delay must be > 0 seconds"
    assert num_stims >= 1, "num_stims must be >= 1"
    assert jitter_rate >= 0, "jitter_rate must be >= 0 seconds"
    assert jitter_quantize > 0, "jitter_quantize must be > 0 seconds"
    if pulse_delay_values_ms is not None:
        assert all(delay_ms >= 0 for delay_ms in pulse_delay_values_ms), (
            "pulse_delay_values_ms values must be >= 0 ms."
        )
        if jitter:
            raise ValueError(
                "Jitter cannot be combined with a Pulse Delay CSV because "
                "CSV timing is generated as one hardware-timed N-cycle burst."
            )
        if rand_freq:
            raise ValueError(
                "Random stimulation frequency cannot be combined with a "
                "Pulse Delay CSV. Select one fixed interstim period or frequency."
            )
    assert jitter_rate <= interstim_delay, (
        f"jitter_rate ({jitter_rate}s) must be <= interstim_delay ({interstim_delay}s) "
        "to avoid negative or invalid sleep intervals when jitter=True."
    )

    def _prepare_fg_args(fg_args, channel_num):
        fg_args = {} if fg_args is None else dict(fg_args)
        allowed_fg = {
            "v_min", "v_max", "vpp", "shape",
            "custom", "ramp",
            "auto_k", "k",
            "pph", "ppw", "pw",
            "channel", "state",
            "charge_balance", "reverse",
        }
        unknown = set(fg_args) - allowed_fg
        assert not unknown, (
            f"Unknown func_gen_control kwargs in fg_ch{channel_num}: {sorted(unknown)}"
        )
        fg_args.setdefault("channel", channel_num)
        fg_args.setdefault("state", 1)
        return fg_args

    if not ch1_ttl:
        fg_ch1 = _prepare_fg_args(fg_ch1, 1)

    if not ch2_ttl:
        fg_ch2 = _prepare_fg_args(fg_ch2, 2)

    jitter_delay_rows = []

    if not hardware_enabled:
        if jitter:
            for stim_number in range(1, num_stims + 1):
                delay = random.uniform(
                    interstim_delay - jitter_rate,
                    interstim_delay + jitter_rate
                )
                delay = round(delay / jitter_quantize) * jitter_quantize
                jitter_delay_rows.append([stim_number, delay])
            _export_burst_delay_log(jitter_delay_rows)

        print("[burst_mode] Hardware disabled; skipping Keysight burst commands.")
        print(
            "[burst_mode] Simulated request: "
            f"num_stims={num_stims}, interstim_delay={interstim_delay}, "
            f"interpulse_delay={interpulse_delay}, jitter={jitter}, "
            f"jitter_rate={jitter_rate}, burst_cycles={burst_cycles}, "
            f"ch2_state={ch2_state}, ch1_ttl={ch1_ttl}, ch2_ttl={ch2_ttl}, "
            f"rand_freq={rand_freq}, pulse_delay_values_ms={pulse_delay_values_ms}"
        )
        return

    resource_name = "33512B"
    id_query = True
    reset = False
    options = ""
    driver = ks.Kt33000(resource_name, id_query, reset, options)
    ch1 = None
    ch2 = None
    pulse_delay_waveform_info = None
    csv_burst_completed_normally = False

    print("  identifier: ", driver.identity.identifier)
    print("  revision:   ", driver.identity.revision)
    print("  vendor:     ", driver.identity.vendor)
    print("  description:", driver.identity.description)
    print("  model:      ", driver.identity.instrument_model)
    print(
        "  firmware:   ",
        getattr(driver.identity, "instrument_firmware_revision", "unknown"),
    )
    print("  resource:   ", driver.driver_operation.io_resource_descriptor)
    print("  options:    ", driver.driver_operation.driver_setup)

    try:
        ch1 = driver.output_channels[0]
        ch2 = driver.output_channels[1]

        ch1.output.enabled = 0
        ch2.output.enabled = 0

        # Ensure both physical output relays are open before aborting or
        # changing the previous burst configuration.  This is especially
        # important when a new run follows an interrupted CSV run immediately.
        _settle_output_relay(driver)

        # Use explicit finite arming for every mode. This prevents a previous
        # run's continuous-initiation state from either re-arming stale output
        # during setup or leaving a later regular (non-CSV) trigger ignored.
        ch1.trigger.initiate_continuous_enabled = False
        ch2.trigger.initiate_continuous_enabled = False

        # One abort applies to both channels on the 33512B.
        ch1.trigger.abort()

        ch1.burst.enabled = False
        ch2.burst.enabled = False

        ch1.trigger.source = ks.TriggerSource.BUS
        ch2.trigger.source = ks.TriggerSource.BUS

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
                driver = driver,
                hardware_enabled = hardware_enabled
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
                    driver = driver,
                    hardware_enabled = hardware_enabled
                )


        if _stop_requested(stop_event):
            print("Stop requested after CH2 setup.")
            return

        if pulse_delay_values_ms is not None:
            ch1_args = {} if fg_ch1 is None else dict(fg_ch1)
            ch2_args = {} if fg_ch2 is None else dict(fg_ch2)

            ch1_pw_ms = ch1_args.get("pw", 1)
            ch2_pw_ms = ch2_args.get("pw", ch1_pw_ms)
            stim_frequency_hz = 1 / interstim_delay

            pulse_delay_waveform_info = load_pulse_delay_waveform(
                ch=ch1,
                driver=driver,
                pulse_delay_values_ms=pulse_delay_values_ms,
                pulse_width_ms=ch1_pw_ms,
                freq=stim_frequency_hz,
                v_min=0 if ch1_ttl else ch1_args.get("v_min", 0),
                v_max=5 if ch1_ttl else ch1_args.get("v_max", 5),
                waveform_name="PULSECSV1",
            )

            if ch2_state:
                load_pulse_delay_waveform(
                    ch=ch2,
                    driver=driver,
                    pulse_delay_values_ms=pulse_delay_values_ms,
                    pulse_width_ms=ch2_pw_ms,
                    freq=stim_frequency_hz,
                    v_min=0 if ch2_ttl else ch2_args.get("v_min", 0),
                    v_max=5 if ch2_ttl else ch2_args.get("v_max", 5),
                    waveform_name="PULSECSV2",
                )

        # --- burst + trigger config ---
        if pulse_delay_values_ms is not None:
            def _set_burst_phase_zero(channel, channel_name):
                burst_attributes = set(dir(channel.burst))
                for phase_attribute in ("phase", "start_phase", "burst_phase"):
                    if phase_attribute in burst_attributes:
                        setattr(channel.burst, phase_attribute, 0.0)
                        print(
                            f"{channel_name} burst start phase set to 0 degrees "
                            f"using {phase_attribute}."
                        )
                        return

                raise AttributeError(
                    f"The Keysight driver does not expose a recognized burst "
                    f"phase property for {channel_name}. Available burst "
                    f"attributes: {sorted(burst_attributes)}"
                )

            _set_burst_phase_zero(ch1, "CH1")
            if ch2_state:
                _set_burst_phase_zero(ch2, "CH2")

        if rand_freq and pulse_delay_values_ms is None:
                random_frequency = random.uniform(
                    rand_freq_lower,
                    rand_freq_upper
                )
                ch1.output.frequency = random_frequency
                ch2.output.frequency = random_frequency

        elif pulse_delay_values_ms is None:

            ch1.output.frequency = 1 / interstim_delay
            ch2.output.frequency = 1 / interstim_delay

        if pulse_delay_values_ms is not None:
            ch1.burst.number_of_cycles = num_stims
            ch2.burst.number_of_cycles = num_stims
            print(
                "Pulse Delay CSV hardware burst: "
                f"{num_stims} cycles x "
                f"{pulse_delay_waveform_info['pulse_count']} pulses = "
                f"{num_stims * pulse_delay_waveform_info['pulse_count']} "
                "total pulses."
            )
        elif (not jitter) and (burst_cycles == 1):
            print(f"burst cycles = {burst_cycles}")
            print("burst = num_stims")
            ch1.burst.number_of_cycles = num_stims
            ch2.burst.number_of_cycles = num_stims
            jitter_rate = 0
        else:
            print(f"burst cycles = {burst_cycles}")
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

        # Arm burst only after frequency, cycle count, load, and trigger
        # delay have all been configured.
        ch1.burst.enabled = True
        ch2.burst.enabled = bool(ch2_state)

        if pulse_delay_values_ms is not None:
            print("Enabling configured 0-5 V CSV output at its low starting point.")
        ch1.output.enabled = 1
        ch2.output.enabled = 1 if ch2_state else 0

        # Configuration is already at the waveform's low first point.  Let the
        # output relay close and stabilize before the channel is armed, so the
        # relay transition cannot overlap the requested pulse train.
        _settle_output_relay(driver)

        if _stop_requested(stop_event):
            print("Stop requested before trigger phase.")
            return

        # --- trigger ---
        def arm_and_trigger_once():
            # Abort above returns both channels to idle. A BUS trigger is
            # ignored in that state, so every finite burst must first move the
            # shared two-channel trigger system to wait-for-trigger.
            ch1.trigger.initiate()
            if interpulse_delay >= 0:
                # print("triggered")
                # print(ch1.trigger.source)
                ch1.trigger.software_trigger()
            else:
                ch2.trigger.software_trigger()

        if pulse_delay_values_ms is not None:
            # The channel is armed and resting at the first low waveform point.
            # Wait one exact period before starting the finite hardware burst.
            initial_delay_s = pulse_delay_waveform_info["downloaded_duration_ms"] / 1e3
            print(
                f"Waiting {initial_delay_s:g} s before the first burst trigger."
            )
            if _wait_until_with_stop(
                time.perf_counter() + initial_delay_s,
                stop_event=stop_event,
            ):
                print("Stop requested during initial interstim wait.")
                return

            if _stop_requested(stop_event):
                print("Stop requested before CSV hardware burst trigger.")
                return

            # Explicitly move from idle to wait-for-trigger only after the
            # waveform, voltage, output relay, phase, and burst count are final.
            print("Arming CSV burst and sending the only software trigger.")
            arm_and_trigger_once()
            print(
                "Triggered Pulse Delay CSV hardware burst: "
                f"{num_stims} stimulation cycles."
            )

            # Wait for every hardware-timed cycle to finish before normal
            # cleanup. Starting after software_trigger returns is deliberately
            # conservative and prevents aborting the final cycle early.
            hardware_burst_duration_s = initial_delay_s * num_stims
            if _wait_until_with_stop(
                time.perf_counter() + hardware_burst_duration_s,
                stop_event=stop_event,
            ):
                print(
                    "Stop requested during CSV hardware burst; "
                    "disconnecting outputs before abort."
                )
                return

            print(
                "Pulse Delay CSV hardware burst completed: "
                f"{num_stims * pulse_delay_waveform_info['pulse_count']} "
                "pulses requested."
            )

            csv_burst_completed_normally = True

        elif jitter or (burst_cycles > 1):
            
            if (
                burst_cycles != 1
                and not rand_freq
                and pulse_delay_values_ms is None
            ):
                if interpulse_delay <= 0:
                    raise ValueError(
                        "interpulse_delay must be > 0 ms when burst_cycles > 1 and rand_freq is False."
                    )
                pulse_freq = 1000.0 / interpulse_delay
                ch1.output.frequency = pulse_freq
                ch2.output.frequency = pulse_freq

            # Give the armed output one complete interstim period to settle at
            # the waveform's low starting point before the first trigger. This
            # also makes startup timing consistent with all later stims.
            print(
                f"Waiting {interstim_delay:g} s before the first burst trigger."
            )
            initial_wait_complete = _wait_until_with_stop(
                time.perf_counter() + interstim_delay,
                stop_event=stop_event,
            )
            if initial_wait_complete:
                print("Stop requested during initial interstim wait.")
                return

            if jitter:
                # The initial wait is deliberately one exact period; jitter is
                # applied only to intervals between subsequent stimulations.
                jitter_delay_rows.append([1, interstim_delay])

            count = 1
            while count <= num_stims:
                if _stop_requested(stop_event):
                    print("Stop requested during burst loop.")
                    return
                
                if rand_freq and pulse_delay_values_ms is None:
                    random_frequency = random.uniform(
                        rand_freq_lower,
                        rand_freq_upper
                    )
                    ch1.output.frequency = random_frequency
                    ch2.output.frequency = random_frequency

                arm_and_trigger_once()
                print(f"Triggered burst {count}/{num_stims}.")

                # There is no reason to remain armed for another full period
                # after the final requested stimulation.
                if count >= num_stims:
                    break

                # Start the deadline after the trigger command returns. This
                # compensates the Python work below without ever shortening a
                # requested wait to catch up after a slow VISA transaction.
                trigger_complete_s = time.perf_counter()
                # print(f"Trigger: {count}")

                rand = random.uniform(
                    interstim_delay - jitter_rate,
                    interstim_delay + jitter_rate
                )
                rand = round(rand / jitter_quantize) * jitter_quantize
                if jitter:
                    jitter_delay_rows.append([count + 1, rand])

                stopped = _wait_until_with_stop(
                    trigger_complete_s + rand,
                    stop_event=stop_event,
                )
                if stopped:
                    print("Stop requested during interstim wait.")
                    return

                count += 1
        else:
            arm_and_trigger_once()

            # Optional: if you want Stop to remain meaningful even in the
            # single-trigger/burst-engine case, wait cooperatively for the
            # expected run duration so the worker stays alive and can be stopped.

            freq = 1 / interstim_delay

            estimated_run_time = _estimated_run_time(num_stims, freq)

            print(f"Estimated run time: {estimated_run_time:.3f} s")

            if _sleep_with_stop(
                estimated_run_time,
                stop_event=stop_event,
                chunk_s=0.01,
            ):
                print("Stop requested during hardware burst.")

    finally:
        print("Disabling hardware")
        if _shutdown_burst_channels(
            ch1,
            ch2,
            driver=driver,
            abort_active=not csv_burst_completed_normally,
            disconnect_before_abort=(
                pulse_delay_values_ms is not None
                and _stop_requested(stop_event)
            ),
        ):
            print("Hardware disabled")

        try:
            if jitter:
                _export_burst_delay_log(jitter_delay_rows)
        finally:
            print("Closing Driver")
            driver.close()
            print("Driver Closed")



    
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
