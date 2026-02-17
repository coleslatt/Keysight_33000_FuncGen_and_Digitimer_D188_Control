#!/usr/bin/env python3
from __future__ import annotations

import platform
import shutil
import subprocess
import sys
from pathlib import Path

# -----------------------------------------------------------------------------
# Paths (assumes this file lives at repo_root/scripts/run.py)
# -----------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parents[1]
APP_DIR = REPO_ROOT / "Application_Files"
UI_ENTRY = APP_DIR / "Controller.py"

# Windows venv activation + interpreter (repo-local)
WIN_ACTIVATE_PS1 = REPO_ROOT / ".venv" / "Scripts" / "Activate.ps1"
WIN_VENV_PY = REPO_ROOT / ".venv" / "Scripts" / "python.exe"

# POSIX venv interpreter candidates (repo-local)
POSIX_VENV_PY_CANDIDATES = [
    REPO_ROOT / ".venv" / "bin" / "python",
    REPO_ROOT / "venv" / "bin" / "python",
]


# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------
def is_windows() -> bool:
    return platform.system().lower().startswith("win")


def which_powershell() -> str | None:
    """Prefer PowerShell 7 (pwsh) if present, else Windows PowerShell."""
    return shutil.which("pwsh") or shutil.which("powershell.exe") or shutil.which("powershell")


def run(cmd: list[str], cwd: Path | None = None) -> int:
    print("+", " ".join(cmd))
    return subprocess.call(cmd, cwd=str(cwd) if cwd else None)


def posix_python() -> str:
    """Pick repo-local venv python if it exists; otherwise fall back to python3."""
    for p in POSIX_VENV_PY_CANDIDATES:
        if p.exists():
            return str(p)
    return shutil.which("python3") or "python3"


def windows_powershell_block(extra_lines: list[str]) -> str:
    """
    Build a PowerShell script block that:
      1) Activates .venv via Activate.ps1 (your documented step)
      2) Defines $Python as ABSOLUTE path to .venv python (so it works after cd)
      3) Removes python alias + disables CommandNotFoundAction
      4) Prints python executable + version
      5) Runs extra_lines
    """
    if not WIN_ACTIVATE_PS1.exists():
        raise FileNotFoundError(f"Missing venv activation script: {WIN_ACTIVATE_PS1}")

    lines = [
        r".\.venv\Scripts\Activate.ps1",

        # CRITICAL FIX:
        # Make $Python absolute so it remains valid even after changing directories.
        r'$Python = (Resolve-Path ".\.venv\Scripts\python.exe").Path',

        r"Remove-Item Alias:python -ErrorAction SilentlyContinue",
        r"$ExecutionContext.InvokeCommand.CommandNotFoundAction = $null",
        r'Write-Host "Using Python:" $Python',
        r'& $Python -c "import sys; print(sys.executable); print(sys.version)"',
        *extra_lines,
    ]
    return "\n".join(lines)


def run_windows_via_activation(extra_lines: list[str]) -> int:
    """Run commands in a child PowerShell session from repo root, after venv activation."""
    ps = which_powershell()
    if not ps:
        print("ERROR: Could not find PowerShell (pwsh/powershell.exe) on PATH.", file=sys.stderr)
        return 2

    try:
        block = windows_powershell_block(extra_lines)
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    return run(
        [ps, "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", block],
        cwd=REPO_ROOT,
    )


# -----------------------------------------------------------------------------
# Commands
# -----------------------------------------------------------------------------
def cmd_info() -> int:
    """Show python executable + version."""
    if is_windows():
        if WIN_ACTIVATE_PS1.exists() and WIN_VENV_PY.exists():
            return run_windows_via_activation(extra_lines=[])
        py = shutil.which("python.exe") or "python.exe"
        return run([py, "-c", "import sys; print(sys.executable); print(sys.version)"], cwd=REPO_ROOT)

    py = posix_python()
    return run([py, "-c", "import sys; print(sys.executable); print(sys.version)"], cwd=REPO_ROOT)


def cmd_ui() -> int:
    """Launch the UI (Controller.py)."""
    if not UI_ENTRY.exists():
        print(f"ERROR: UI entry not found: {UI_ENTRY}", file=sys.stderr)
        return 2

    if is_windows():
        return run_windows_via_activation(extra_lines=[r"& $Python .\Application_Files\Controller.py"])

    py = posix_python()
    return run([py, str(UI_ENTRY)], cwd=REPO_ROOT)


def cmd_burst() -> int:
    """Open an interactive python in Application_Files and (optionally) pre-import burst_mode."""
    if is_windows():
        # Option A (recommended): auto-import and stay interactive
        # -i keeps the interpreter open after executing -c
        return run_windows_via_activation(
            extra_lines=[
                r"cd .\Application_Files",
                r'& $Python -i -c "from burst_mode_function import burst_mode"',
            ]
        )

        # Option B (manual import) would be:
        # return run_windows_via_activation(
        #     extra_lines=[
        #         r"cd .\Application_Files",
        #         r'Write-Host "Then run in Python:" "from burst_mode_function import burst_mode"',
        #         r"& $Python",
        #     ]
        # )

    py = posix_python()
    print(f"Launching interactive Python in {APP_DIR}")
    print("Then run: from burst_mode_function import burst_mode")
    return run([py], cwd=APP_DIR)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main(argv: list[str]) -> int:
    if "--info" in argv:
        return cmd_info()
    if "--ui" in argv:
        return cmd_ui()
    if "--burst" in argv:
        return cmd_burst()

    print("Usage:")
    print("  python scripts/run.py --info   # show python executable + version")
    print("  python scripts/run.py --ui     # launch UI (Controller.py)")
    print("  python scripts/run.py --burst  # interactive python in Application_Files (burst_mode imported)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
