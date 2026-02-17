# Run from repo root: .\scripts\run.ps1 --ui
$RepoRoot = Split-Path -Parent $PSScriptRoot
$Py = Join-Path $RepoRoot ".venv\Scripts\python.exe"

if (-not (Test-Path $Py)) {
  $Py = "python.exe"
}

& $Py (Join-Path $RepoRoot "scripts\run.py") @Args
