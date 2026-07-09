#!/usr/bin/env bash
set -euo pipefail

cmd="${1:-doctor}"
if [[ "$cmd" == "run" ]]; then
  shift
  exec "$@"
fi

if [[ "$cmd" == "doctor" ]]; then
  python3 --version >/dev/null
  git --version >/dev/null
  python3 scripts/classify_third_party.py check >/dev/null
  python3 scripts/provider_tool.py validate >/dev/null
  echo "FabLab bootstrap doctor passed"
  exit 0
fi

if [[ "$cmd" == "--allow-downloads" ]]; then
  echo "downloads are not implemented in the Phase 4 skeleton" >&2
  exit 2
fi

echo "unknown bootstrap command: $cmd" >&2
exit 2
