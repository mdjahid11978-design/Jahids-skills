#!/usr/bin/env python3
"""Verify that a release tag matches the project version."""
from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def project_version() -> str:
    data = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    return str(data["project"]["version"])


def validate_tag(tag: str) -> tuple[bool, str]:
    if not re.fullmatch(r"v[0-9]+\.[0-9]+\.[0-9]+", tag):
        return False, "tag must use semantic version format vMAJOR.MINOR.PATCH"
    expected = f"v{project_version()}"
    if tag != expected:
        return False, f"tag {tag} does not match pyproject.toml version {expected}"
    return True, f"release tag {tag} matches project version"


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/check_release_version.py vX.Y.Z")
        return 2
    valid, message = validate_tag(sys.argv[1])
    print(message)
    return 0 if valid else 1


if __name__ == "__main__":
    sys.exit(main())
