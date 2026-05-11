# setup_env.ps1
# One-shot script to create and activate a virtualenv, then install dependencies.

$ErrorActionPreference = "Stop"

$RequiredPythonVersion = "3.10"
$RequiredPythonVersionTuple = [version]$RequiredPythonVersion
$PythonInstallerVersion = "3.10.11"

function Test-PythonCommand {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Executable,

        [string[]]$Arguments = @()
    )

    try {
        $versionText = & $Executable @Arguments -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>$null
        if ($LASTEXITCODE -ne 0) {
            return $false
        }

        return ([version]($versionText | Select-Object -First 1)) -eq $RequiredPythonVersionTuple
    }
    catch {
        return $false
    }
}

function Get-RequiredPythonCommand {
    $candidates = @(
        @{ Executable = "py"; Arguments = @("-$RequiredPythonVersion") },
        @{ Executable = "$env:LocalAppData\Programs\Python\Python310\python.exe"; Arguments = @() },
        @{ Executable = "$env:ProgramFiles\Python310\python.exe"; Arguments = @() },
        @{ Executable = "${env:ProgramFiles(x86)}\Python310-32\python.exe"; Arguments = @() },
        @{ Executable = "python$RequiredPythonVersion"; Arguments = @() },
        @{ Executable = "python"; Arguments = @() },
        @{ Executable = "python3"; Arguments = @() }
    )

    foreach ($candidate in $candidates) {
        if (Test-PythonCommand -Executable $candidate.Executable -Arguments $candidate.Arguments) {
            return $candidate
        }
    }

    return $null
}

function Update-ProcessPathFromRegistry {
    $machinePath = [Environment]::GetEnvironmentVariable("Path", "Machine")
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    $Env:Path = @($machinePath, $userPath) -join ";"
}

function Install-RequiredPython {
    Write-Host "Python $RequiredPythonVersion was not found. Attempting to install it..."

    if (Get-Command winget -ErrorAction SilentlyContinue) {
        Write-Host "Installing Python $RequiredPythonVersion with winget..."
        & winget install --id "Python.Python.$RequiredPythonVersion" --exact --source winget --scope user --silent --accept-package-agreements --accept-source-agreements

        if ($LASTEXITCODE -eq 0) {
            Update-ProcessPathFromRegistry
            return
        }

        Write-Warning "winget could not install Python $RequiredPythonVersion. Falling back to the official python.org installer."
    }
    else {
        Write-Host "winget is not available. Falling back to the official python.org installer."
    }

    $arch = if ([Environment]::Is64BitOperatingSystem) {
        "amd64"
    }
    else {
        "win32"
    }

    $installerFile = if ($arch -eq "win32") {
        "python-$PythonInstallerVersion.exe"
    }
    else {
        "python-$PythonInstallerVersion-$arch.exe"
    }

    $installerUrl = "https://www.python.org/ftp/python/$PythonInstallerVersion/$installerFile"
    $installerPath = Join-Path $env:TEMP $installerFile

    Write-Host "Downloading Python installer from:"
    Write-Host "  $installerUrl"
    Invoke-WebRequest -Uri $installerUrl -OutFile $installerPath -UseBasicParsing

    Write-Host "Installing Python $RequiredPythonVersion for the current user..."
    $installArgs = @(
        "/quiet",
        "InstallAllUsers=0",
        "PrependPath=1",
        "Include_launcher=1",
        "Include_pip=1",
        "SimpleInstall=1"
    )
    Start-Process -FilePath $installerPath -ArgumentList $installArgs -Wait
    Update-ProcessPathFromRegistry
}

function Invoke-RequiredPython {
    param(
        [Parameter(Mandatory = $true)]
        [hashtable]$PythonCommand,

        [Parameter(ValueFromRemainingArguments = $true)]
        [string[]]$Arguments
    )

    & $PythonCommand.Executable @($PythonCommand.Arguments) @Arguments
}

function Test-VisaInstalled {
    # Heuristic check for common VISA runtimes:
    #   - NI-VISA:  C:\Program Files\IVI Foundation\VISA\...
    #   - Keysight: C:\Program Files\Keysight\IO Libraries Suite\...

    $candidateDlls = @(
        "$Env:ProgramFiles\IVI Foundation\VISA\Win64\Bin\visa64.dll",
        "$Env:ProgramFiles(x86)\IVI Foundation\VISA\WinNT\Bin\visa32.dll",
        "$Env:ProgramFiles\Keysight\IO Libraries Suite\bin\visa64.dll",
        "$Env:ProgramFiles(x86)\Keysight\IO Libraries Suite\bin\visa32.dll"
    )

    foreach ($path in $candidateDlls) {
        if (Test-Path $path) {
            return $true
        }
    }

    return $false
}

Write-Host "=== Setting up Python virtual environment ==="


# Always work from the directory where this script lives (repo root)
Set-Location -Path $PSScriptRoot

$pythonCommand = Get-RequiredPythonCommand
if (-not $pythonCommand) {
    Install-RequiredPython
    $pythonCommand = Get-RequiredPythonCommand
}

if (-not $pythonCommand) {
    throw "Python $RequiredPythonVersion could not be found or installed. Please install Python $RequiredPythonVersion from https://www.python.org/downloads/release/python-$($PythonInstallerVersion.Replace('.', ''))/ and re-run this script."
}

Write-Host "Using Python $RequiredPythonVersion via: $($pythonCommand.Executable) $($pythonCommand.Arguments -join ' ')"

# 1. Create venv if it doesn't exist
if (-not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment in '.venv'..."
    Invoke-RequiredPython -PythonCommand $pythonCommand -Arguments @("-m", "venv", ".venv")
}
else {
    Write-Host "Virtual environment '.venv' already exists, skipping creation."
}

if (-not (Test-PythonCommand -Executable ".\.venv\Scripts\python.exe")) {
    throw "The existing '.venv' is not using Python $RequiredPythonVersion. Remove the '.venv' directory and re-run this script to recreate it with the required Python version."
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

Write-Host "=== Checking for VISA runtime (Keysight IO Libraries / NI-VISA) ==="

if (-not (Test-VisaInstalled)) {
    Write-Warning @"
VISA runtime does not appear to be installed on this system.

The Keysight 33512B driver (keysight_kt33000) will fail with errors like
'VISA is not installed, please install VISA first' until a VISA runtime
is installed.

Please install *Keysight IO Libraries Suite* before using this repository:

  Download page (always current version):
    https://www.keysight.com/find/iosuite

After installation, you may need to reboot, then re-run this setup script.
"@
}
else {
    Write-Host "VISA runtime detected."
}



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
