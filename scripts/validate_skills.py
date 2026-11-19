#!/usr/bin/env python3
"""Validate JAHIDS skill directories and required frontmatter."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
REQUIRED = ("name", "description")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return [f"{path.relative_to(ROOT)}: missing YAML frontmatter"]
    end = text.find("\n---\n", 4)
    if end < 0:
        return [f"{path.relative_to(ROOT)}: unterminated YAML frontmatter"]
    header = text[4:end]
    fields: dict[str, str] = {}
    for line in header.splitlines():
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"\'')
    for key in REQUIRED:
        if not fields.get(key):
            errors.append(f"{path.relative_to(ROOT)}: missing {key}")
    name = fields.get("name", "")
    if name and not NAME_RE.fullmatch(name):
        errors.append(f"{path.relative_to(ROOT)}: invalid skill name {name!r}")
    if path.parent.name != name:
        errors.append(f"{path.relative_to(ROOT)}: directory must match name {name!r}")
    if not text[end + 5:].strip():
        errors.append(f"{path.relative_to(ROOT)}: skill body is empty")
    return errors


def main() -> int:
    paths = sorted(SKILLS.glob("*/SKILL.md"))
    if not paths:
        print("FAIL: no skills found")
        return 1
    errors = [error for path in paths for error in validate_file(path)]
    if errors:
        print("\n".join(errors))
        return 1
    print(f"PASS: validated {len(paths)} skills")
    return 0


if __name__ == "__main__":
    sys.exit(main())
