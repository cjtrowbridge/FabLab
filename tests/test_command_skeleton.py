#!/usr/bin/env python3
"""Smoke tests for Phase 4 command skeletons."""

from __future__ import annotations

import subprocess


def test_provider_validate() -> None:
    subprocess.check_call(["python3", "scripts/provider_tool.py", "validate"])


def test_classification_check() -> None:
    subprocess.check_call(["python3", "scripts/classify_third_party.py", "check"])


def test_schema_examples() -> None:
    subprocess.check_call(["python3", "scripts/validate_project.py", "--examples"])


if __name__ == "__main__":
    test_provider_validate()
    test_classification_check()
    test_schema_examples()
    print("command skeleton smoke tests passed")
