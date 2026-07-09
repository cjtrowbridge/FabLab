#!/usr/bin/env python3
"""Lightweight FabLab schema/example validator.

This intentionally avoids third-party JSON Schema dependencies in the first pass.
It checks JSON parseability and the required top-level fields used by Phase 3
fixtures.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED = {
    "project.example.json": {"schema_version", "id", "name", "status"},
    "part_graph.example.json": {"schema_version", "project_id", "parts"},
    "process_recommendation.example.json": {"schema_version", "part_id", "recommended_processes"},
    "provider.example.json": {"schema_version", "id", "classification", "submodule_path", "output_authority"},
    "component.example.json": {"schema_version", "id", "component_type", "status"},
    "validation_report.example.json": {"schema_version", "project_id", "results"},
    "artifact_manifest.example.json": {"schema_version", "project_id", "artifacts"},
}


def validate_examples(root: Path) -> list[str]:
    errors: list[str] = []
    examples = root / "schemas" / "examples"
    for name, required in REQUIRED.items():
        path = examples / name
        if not path.exists():
            errors.append(f"missing example: {path}")
            continue
        data = json.loads(path.read_text())
        missing = required.difference(data)
        if missing:
            errors.append(f"{path}: missing required fields {sorted(missing)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--examples", action="store_true", help="validate schema example fixtures")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    errors = validate_examples(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("schema example validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
