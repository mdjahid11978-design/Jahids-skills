#!/usr/bin/env python3
"""Validate JAHIDS.AI skill directories, YAML metadata, and required sections."""
from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Any

import jsonschema
import yaml
from yaml.constructor import ConstructorError

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
SCHEMA_PATH = ROOT / "schemas" / "skill.schema.json"
SCHEMA: dict[str, Any] = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
jsonschema.Draft202012Validator.check_schema(SCHEMA)
VALIDATOR = jsonschema.Draft202012Validator(SCHEMA)
REQUIRED_SECTIONS = (
    "## Use when",
    "## Procedure",
    "## Output",
    "## Authority boundary",
)


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects duplicate mapping keys."""


def _construct_unique_mapping(loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False):
    loader.flatten_mapping(node)
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in mapping
        except TypeError as exc:
            raise ConstructorError(
                "while constructing a mapping", node.start_mark,
                "found an unhashable mapping key", key_node.start_mark,
            ) from exc
        if duplicate:
            raise ConstructorError(
                "while constructing a mapping", node.start_mark,
                f"found duplicate key {key!r}", key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping
)


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
    body = content[closing + 5 :]

    try:
        metadata = yaml.load(content[4:closing], Loader=UniqueKeyLoader)
    except yaml.YAMLError as exc:
        return [f"{label}: invalid YAML frontmatter: {exc}"]
    if not isinstance(metadata, dict):
        return [f"{label}: frontmatter must be a YAML mapping"]

    errors: list[str] = []
    for issue in sorted(VALIDATOR.iter_errors(metadata), key=lambda e: list(map(str, e.absolute_path))):
        location = ".".join(str(part) for part in issue.absolute_path)
        suffix = f" at {location}" if location else ""
        errors.append(f"{label}: metadata schema error{suffix}: {issue.message}")

    name = metadata.get("name")
    if isinstance(name, str) and path.parent.name != name:
        errors.append(f"{label}: directory must match metadata name {name!r}")
    if not body.strip():
        errors.append(f"{label}: skill body is empty")
    else:
        for heading in REQUIRED_SECTIONS:
            if heading not in body.splitlines():
                errors.append(f"{label}: missing required section {heading!r}")
        if not body.lstrip().startswith("# "):
            errors.append(f"{label}: skill body must start with a level-one Markdown title")
    return errors


def validate_tree(skills_dir: Path = SKILLS) -> tuple[list[str], int]:
    if not skills_dir.is_dir():
        return [f"{skills_dir}: skills directory does not exist"], 0

    directories = sorted(path for path in skills_dir.iterdir() if path.is_dir())
    if not directories:
        return [f"{skills_dir}: no skill directories found"], 0

    errors: list[str] = []
    checked = 0
    seen_names: dict[str, str] = {}
    for directory in directories:
        if directory.is_symlink():
            errors.append(f"{directory}: skill directories cannot be symbolic links")
            continue
        entrypoint = directory / "SKILL.md"
        if not entrypoint.is_file():
            alternatives = [p.name for p in directory.iterdir() if p.is_file()]
            hint = f"; found files: {', '.join(alternatives)}" if alternatives else ""
            errors.append(f"{directory}: missing required SKILL.md{hint}")
            continue
        checked += 1
        file_errors = validate_file(entrypoint, root=skills_dir.parent)
        errors.extend(file_errors)
        try:
            text = entrypoint.read_text(encoding="utf-8")
            closing = text.find("\n---\n", 4)
            if text.startswith("---\n") and closing >= 0:
                metadata = yaml.load(text[4:closing], Loader=UniqueKeyLoader)
                if isinstance(metadata, dict) and isinstance(metadata.get("name"), str):
                    key = metadata["name"].casefold()
                    if key in seen_names:
                        errors.append(
                            f"{entrypoint}: duplicate skill name {metadata['name']!r}; "
                            f"also used by {seen_names[key]}"
                        )
                    else:
                        seen_names[key] = str(entrypoint)
        except (OSError, UnicodeError, yaml.YAMLError):
            pass
    return errors, checked


def main() -> int:
    errors, checked = validate_tree()
    if errors:
        print("\n".join(errors))
        print(f"FAIL: {len(errors)} issue(s); {checked} skill file(s) checked")
        return 1
    print(f"PASS: validated {checked} skills against YAML, JSON Schema, and content rules")
    return 0


if __name__ == "__main__":
    sys.exit(main())
