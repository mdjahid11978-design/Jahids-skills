import importlib.util
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "scripts" / "validate_skills.py"
SPEC = importlib.util.spec_from_file_location("validate_skills", MODULE)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


def test_repository_skills_are_valid():
    paths = sorted(validator.SKILLS.glob("*/SKILL.md"))
    assert paths
    assert [error for path in paths for error in validator.validate_file(path)] == []


def test_invalid_name_is_rejected(tmp_path):
    skill = tmp_path / "Bad_Name"
    skill.mkdir()
    file = skill / "SKILL.md"
    file.write_text("---\nname: Bad_Name\ndescription: Invalid test\n---\nBody\n", encoding="utf-8")
    errors = validator.validate_file(file)
    assert any("invalid skill name" in error for error in errors)
