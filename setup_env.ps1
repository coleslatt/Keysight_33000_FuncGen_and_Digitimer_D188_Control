# setup_env.ps1
# One-shot script to create and activate a virtualenv, then install dependencies.

$ErrorActionPreference = "Stop"

Write-Host "=== Setting up Python virtual environment ==="

# Always work from the directory where this script lives (repo root)
Set-Location -Path $PSScriptRoot

# 1. Create venv if it doesn't exist
if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment in '.venv'..."
    py -3.10 -m venv .venv
}
else {
    Write-Host "Virtual environment '.venv' already exists, skipping creation."
}

# 2. Activate the venv in this PowerShell session
Write-Host "Activating virtual environment..."
. ".\.venv\Scripts\Activate.ps1"   # dot-source so activation affects this session

# Path to the venv's python explicitly
$venvPython = ".\.venv\Scripts\python.exe"

# 3. Upgrade pip *inside the venv*
Write-Host "Upgrading pip in the virtual environment..."
& $venvPython -m pip install --upgrade pip

# 4. Install project requirements
Write-Host "Installing dependencies from requirements.txt into the virtual environment..."
& $venvPython -m pip install -r "requirements.txt"


Write-Host "=== Checking for Digitimer D188 driver installer ==="

# Relative path to the installer from the repo root
$D188Installer = Join-Path $PSScriptRoot "drivers\D188-Install-5.exe"

if (Test-Path $D188Installer) {
    Write-Host "Found D188 installer at:"
    Write-Host "  $D188Installer"
    Write-Host "Launching installer (you may be prompted for admin rights)..."

    # Launch the installer elevated and wait for it to finish
    Start-Process -FilePath $D188Installer -Verb RunAs -Wait
}
else {
    Write-Host "WARNING: D188 installer not found at expected path:"
    Write-Host "  $D188Installer"
    Write-Host "Skipping D188 driver installation."
}

Write-Host ""
Write-Host "✅ Done!"
Write-Host "The virtual environment is now ACTIVE in this PowerShell session."
Write-Host "When you open a new PowerShell later, re-activate it with:"
Write-Host "  .\.venv\Scripts\Activate.ps1"
