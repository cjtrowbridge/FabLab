#!/usr/bin/env python3
"""Lightweight component validation placeholder."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--component", type=Path)
    args = parser.parse_args()
    if args.component:
        data = json.loads(args.component.read_text())
        missing = {"schema_version", "id", "component_type", "status"}.difference(data)
        if missing:
            print(f"ERROR: missing fields {sorted(missing)}", file=sys.stderr)
            return 1
    print("component validation placeholder passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
