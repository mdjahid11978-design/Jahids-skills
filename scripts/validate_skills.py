#!/usr/bin/env python3
"""Validate every JAHIDS skill directory, YAML frontmatter, and metadata schema."""
from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Any

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
SCHEMA_PATH = ROOT / "schemas" / "skill.schema.json"
SCHEMA: dict[str, Any] = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _label(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def validate_file(path: Path, root: Path = ROOT) -> list[str]:
    label = _label(path, root)
    try:
        content = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"{label}: cannot read UTF-8 file: {exc}"]

    if not content.startswith("---\n"):
        return [f"{label}: missing YAML frontmatter opening delimiter"]
    closing = content.find("\n---\n", 4)
    if closing < 0:
        return [f"{label}: missing YAML frontmatter closing delimiter"]
    after = closing + 5

    try:
        metadata = yaml.safe_load(content[4:closing])
    except yaml.YAMLError as exc:
        return [f"{label}: invalid YAML frontmatter: {exc}"]
    if not isinstance(metadata, dict):
        return [f"{label}: frontmatter must be a YAML mapping"]

    errors: list[str] = []
    try:
        jsonschema.validate(instance=metadata, schema=SCHEMA)
    except jsonschema.ValidationError as exc:
        location = ".".join(str(part) for part in exc.absolute_path)
        suffix = f" at {location}" if location else ""
        errors.append(f"{label}: metadata schema error{suffix}: {exc.message}")

    name = metadata.get("name")
    if isinstance(name, str) and path.parent.name != name:
        errors.append(f"{label}: directory must match metadata name {name!r}")
    if not content[after:].strip():
        errors.append(f"{label}: skill body is empty")
    return errors


def validate_tree(skills_dir: Path = SKILLS) -> tuple[list[str], int]:
    if not skills_dir.is_dir():
        return [f"{skills_dir}: skills directory does not exist"], 0
    directories = sorted(path for path in skills_dir.iterdir() if path.is_dir())
    if not directories:
        return [f"{skills_dir}: no skill directories found"], 0

    errors: list[str] = []
    checked = 0
    for directory in directories:
        entrypoint = directory / "SKILL.md"
        if not entrypoint.is_file():
            alternatives = [p.name for p in directory.iterdir() if p.is_file()]
            hint = f"; found files: {', '.join(alternatives)}" if alternatives else ""
            errors.append(f"{directory}: missing required SKILL.md{hint}")
            continue
        checked += 1
        errors.extend(validate_file(entrypoint, root=skills_dir.parent))
    return errors, checked


def main() -> int:
    errors, checked = validate_tree()
    if errors:
        print("\n".join(errors))
        print(f"FAIL: {len(errors)} issue(s); {checked} skill file(s) checked")
        return 1
    print(f"PASS: validated {checked} skills against the YAML and JSON schemas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
