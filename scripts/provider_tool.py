#!/usr/bin/env python3
"""Provider manifest utility for FabLab."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_FIELDS = {
    "schema_version",
    "id",
    "name",
    "classification",
    "upstream_url",
    "submodule_path",
    "invocation_mode",
    "license_boundary",
    "output_authority",
    "expected_outputs",
    "validation_required",
    "setup_command",
    "check_command",
    "notes",
}


def root() -> Path:
    return Path(__file__).resolve().parents[1]


def adapter_paths() -> list[Path]:
    return sorted((root() / "tool_adapters").glob("*.json"))


def load_adapters() -> list[dict[str, object]]:
    return [json.loads(path.read_text()) for path in adapter_paths()]


def validate() -> list[str]:
    errors: list[str] = []
    for path in adapter_paths():
        data = json.loads(path.read_text())
        missing = REQUIRED_FIELDS.difference(data)
        if missing:
            errors.append(f"{path}: missing fields {sorted(missing)}")
        submodule_path = root() / str(data.get("submodule_path", ""))
        if not submodule_path.exists():
            errors.append(f"{path}: submodule path does not exist: {submodule_path}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["list", "validate", "check", "setup", "run"])
    parser.add_argument("provider", nargs="?")
    args, rest = parser.parse_known_args()

    if args.command == "list":
        for adapter in load_adapters():
            print(f"{adapter['id']}\t{adapter['classification']}\t{adapter['submodule_path']}")
        return 0

    if args.command in {"validate", "check"}:
        errors = validate()
        if errors:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
            return 1
        print("provider manifest validation passed")
        return 0

    print(
        f"provider {args.command} is not implemented for {args.provider or 'unspecified'}; "
        "FabLab will not execute provider helpers until manifests declare safe commands.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
