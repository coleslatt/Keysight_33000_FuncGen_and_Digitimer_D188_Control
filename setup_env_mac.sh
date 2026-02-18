You said:
setup_env.ps1
File
requirements.txt
Document
Can you adapt the following setup script such that it can run on a mac and set up everything included?


ChatGPT said:

Below is a macOS-friendly equivalent of your PowerShell setup that does the same core job:

    cd to repo root

    create .venv (Python 3.10 if available)

    activate it

    upgrade pip

    install requirements

    handles the Windows-only wheel in your requirements.txt (the ...win_amd64.whl line) by filtering it out on macOS

    checks (heuristically) for a VISA runtime and warns if it doesn’t look installed

    skips Digitimer D188 installer (your script points to a Windows .exe, so it can’t run on macOS)

1) Create setup_env_mac.sh in your repo root

#!/usr/bin/env bash
# setup_env_mac.sh
# macOS one-shot script to create + activate a venv, then install dependencies.
set -euo pipefail

echo "=== Setting up Python virtual environment (macOS) ==="

# Always work from the directory where this script lives (repo root)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# ---- helpers ----
have_cmd() { command -v "$1" >/dev/null 2>&1; }

pick_python() {
  # Prefer python3.10 if present, else python3.
  if have_cmd python3.10; then
    echo "python3.10"
  elif have_cmd python3; then
    echo "python3"
  else
    echo ""
  fi
}

check_visa_runtime() {
  # Heuristic checks (varies by vendor/version):
  # - NI-VISA often installs a VISA.framework
  # - Keysight IO Libraries may install VISA components as well
  if [ -d "/Library/Frameworks/VISA.framework" ]; then
    return 0
  fi
  # Broader heuristic: any framework with "visa" in name
  if ls /Library/Frameworks 2>/dev/null | grep -qi visa; then
    return 0
  fi
  return 1
}

# ---- pick python ----
PY="$(pick_python)"
if [ -z "$PY" ]; then
  echo "ERROR: Could not find python3 or python3.10 on PATH."
  echo "Install Python 3 (ideally 3.10) then re-run."
  exit 1
fi

echo "Using interpreter: $PY"
$PY -V

# 1) Create venv if it doesn't exist
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment in '.venv'..."
  "$PY" -m venv .venv
else
  echo "Virtual environment '.venv' already exists, skipping creation."
fi

# 2) Activate the venv
echo "Activating virtual environment..."
# shellcheck disable=SC1091
source ".venv/bin/activate"

VENV_PY=".venv/bin/python"

# 3) Upgrade pip inside the venv
echo "Upgrading pip in the virtual environment..."
"$VENV_PY" -m pip install --upgrade pip

# 4) Install project requirements
# Your requirements.txt contains a Windows-only wheel path:
#   ./drivers/.../keysight_kt33000-...-win_amd64.whl
# That will fail on macOS, so we filter out *.whl lines on macOS.
echo "Installing dependencies from requirements.txt into the virtual environment..."
if [ ! -f "requirements.txt" ]; then
  echo "ERROR: requirements.txt not found in repo root."
  exit 1
fi

TMP_REQ="$(mktemp)"
# Remove local wheel references (and other OS-specific wheel pins if you add more later)
grep -vE '^[[:space:]]*\./.*\.whl[[:space:]]*$' "requirements.txt" > "$TMP_REQ"

"$VENV_PY" -m pip install -r "$TMP_REQ"

rm -f "$TMP_REQ"

# 5) Keysight 33512B driver note (keysight_kt33000)
# On macOS you generally install from a source archive (tar.gz) from Keysight,
# unless you have a macOS-compatible wheel.
echo ""
echo "=== Keysight 33500/33512 driver (keysight_kt33000) ==="
echo "Your requirements.txt references a Windows wheel; on macOS you likely need a source archive."
echo "If you have a keysight_kt33000-*.tar.gz, install it like:"
echo "  python -m pip install ./drivers/keysight_kt33000-1.2.0.tar.gz"
echo "Otherwise download it from Keysight and pip install the tar.gz."

# 6) VISA runtime check
echo ""
echo "=== Checking for VISA runtime (NI-VISA / Keysight IO Libraries) ==="
if check_visa_runtime; then
  echo "VISA runtime appears to be present (heuristic check)."
else
  echo "WARNING: VISA runtime does not appear to be installed (heuristic check)."
  echo "PyVISA + VISA is required for instrument control."
  echo "Install Keysight IO Libraries Suite (recommended by Keysight) or NI-VISA."
fi

# 7) Digitimer D188 driver
echo ""
echo "=== Digitimer D188 driver ==="
echo "Your Windows script launches drivers/D188-Install-5.exe."
echo "That installer is Windows-only, so it is skipped on macOS."
echo "If you need D188 control from macOS, you'll likely need:"
echo "  - a Windows VM / separate Windows machine, OR"
echo "  - a macOS-compatible vendor SDK (if available)."

echo ""
echo "✅ Done!"
echo "The virtual environment is now ACTIVE in this shell."
echo "Later, re-activate with:"
echo "  source .venv/bin/activate"

Make it executable and run it:

chmod +x setup_env_mac.sh
./setup_env_mac.sh

2) Keysight driver and VISA: what to do on macOS
VISA runtime

Keysight’s Python driver stack uses VISA; Keysight explicitly recommends Keysight IO Libraries Suite (which includes VISA) for their Python instrument drivers.
keysight_kt33000 on macOS

Your requirements.txt hard-codes a Windows wheel path (...win_amd64.whl).
For macOS, you typically install the source archive (.tar.gz) that Keysight provides (their docs show pip install keys:contentReference[oaicite:3]{index=3}r.gz).

Practical options:

    Best (recommended): download Keysight’s keysight_kt33000-1.2.0.tar.gz and install it inside the venv:

    source .venv/bin/activate
    python -m pip install /path/to/keysight_kt33000-1.2.0.tar.gz

    (Keysight provides a “Version 1.2.0” download page.)

    If you later add a macOS wheel or an internal wheel, you can update the script to install it conditionally.

3) What I changed vs your Windows setup_env.ps1

    Replaced py -3.10 -m venv .venv with python3.10 -m venv .venv (fallback to python3).

    Replaced PowerShell activation with source .venv/bin/activate.

    Replaced the Windows VISA DLL existence check with a macOS framework heuristic.

    Filtered out *.whl local references from requirements.txt because your file includes a Windows-only wheel line.

    Skipped running drivers/D188-Install-5.exe because it’s Windows-only.

If you want, I can also generate a single cross-platform script (macOS/Linux bash + Windows PowerShell) that shares the same logic and keeps OS-specific bits minimal.


