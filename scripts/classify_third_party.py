#!/usr/bin/env python3
"""Check FabLab third-party submodule classification metadata."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


ALLOWED_CLASSIFICATIONS = {
    "temporary_assimilation_source",
    "permanent_provider",
    "permanent_reference",
    "permanent_provider_dependency",
    "manual_operator_reference",
    "inspection_only_provider",
    "component_source",
    "viewer_reference",
    "rejected_with_rationale",
    "deprecated",
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def top_level_submodules(root: Path) -> list[str]:
    output = subprocess.check_output(
        ["git", "config", "--file", ".gitmodules", "--get-regexp", r"^submodule\..*\.path$"],
        cwd=root,
        text=True,
    )
    paths: list[str] = []
    for line in output.splitlines():
        _, path = line.split(maxsplit=1)
        if path.startswith("third_party/") and path.count("/") == 1:
            paths.append(path)
    return sorted(paths)


def load_versions(root: Path) -> dict[str, dict[str, object]]:
    data = json.loads((root / "provider_versions.json").read_text())
    return {entry["path"]: entry for entry in data.get("submodules", [])}


def load_adapters(root: Path) -> dict[str, dict[str, object]]:
    adapters: dict[str, dict[str, object]] = {}
    for path in sorted((root / "tool_adapters").glob("*.json")):
        data = json.loads(path.read_text())
        adapters[data["submodule_path"]] = data
    return adapters


def check(root: Path) -> list[str]:
    errors: list[str] = []
    third_party_paths = top_level_submodules(root)
    versions = load_versions(root)
    adapters = load_adapters(root)

    for path in third_party_paths:
        entry = versions.get(path)
        if entry is None:
            errors.append(f"{path}: missing from provider_versions.json")
            continue
        classification = entry.get("classification")
        if classification not in ALLOWED_CLASSIFICATIONS:
            errors.append(f"{path}: invalid classification {classification!r}")
        if classification != "temporary_assimilation_source" and path not in adapters:
            errors.append(f"{path}: permanent/reference submodule missing adapter manifest")

    for path in versions:
        if path.startswith("third_party/") and path.count("/") == 1 and path not in third_party_paths:
            errors.append(f"{path}: listed in provider_versions.json but not .gitmodules")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["list", "check", "audit"])
    args = parser.parse_args()
    root = repo_root()

    if args.command == "list":
        versions = load_versions(root)
        for path in top_level_submodules(root):
            entry = versions.get(path, {})
            print(f"{path}\t{entry.get('classification', 'missing')}")
        return 0

    errors = check(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("third-party classification check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
