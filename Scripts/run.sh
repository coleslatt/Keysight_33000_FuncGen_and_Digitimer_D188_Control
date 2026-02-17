#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PY="$REPO_ROOT/.venv/bin/python"
if [[ ! -x "$PY" ]]; then
  PY="$REPO_ROOT/venv/bin/python"
fi
if [[ ! -x "$PY" ]]; then
  PY="python3"
fi

exec "$PY" "$REPO_ROOT/scripts/run.py" "$@"
