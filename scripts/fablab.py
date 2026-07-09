#!/usr/bin/env python3
"""FabLab command skeleton."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


COMMANDS = [
    "new",
    "brief",
    "decompose",
    "recommend",
    "plan",
    "build",
    "audit",
    "output-readme",
    "components",
]


def create_project(name: str) -> None:
    project_id = name.replace(" ", "_").lower()
    project_dir = Path("projects") / project_id
    project_dir.mkdir(parents=True, exist_ok=True)
    data = {
        "schema_version": 1,
        "id": project_id,
        "name": name,
        "status": "proposed",
        "parts": [],
        "components": [],
    }
    (project_dir / "project.json").write_text(json.dumps(data, indent=2) + "\n")
    print(f"created project skeleton: {project_dir}")


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    for command in COMMANDS:
        command_parser = sub.add_parser(command)
        command_parser.add_argument("--project")
        if command == "new":
            command_parser.add_argument("--name")
    args = parser.parse_args()

    if args.command == "new":
        create_project(args.name or args.project or "untitled_project")
        return 0

    print(
        f"fablab {args.command} is parsed but not implemented yet; "
        "no fabrication artifacts were generated and no readiness claim is made."
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
