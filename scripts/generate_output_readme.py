#!/usr/bin/env python3
"""Generate a conservative output README placeholder."""

from __future__ import annotations

import argparse
from pathlib import Path


TEMPLATE = """# Output: {project}

This output README is a Phase 4 skeleton placeholder.

No fabrication artifacts are declared fabrication-ready by this generator.
Validation, purchased-part measurements, material setup, machine setup, and
human safety review must be completed before fabrication.
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project", required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    output = args.output or Path("output") / args.project / "README.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(TEMPLATE.format(project=args.project))
    print(f"wrote conservative output README placeholder: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
