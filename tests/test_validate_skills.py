import importlib.util
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "scripts" / "validate_skills.py"
SPEC = importlib.util.spec_from_file_location("validate_skills", MODULE)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


def write_skill(folder: Path, metadata: str, body: str = "# Skill\\n") -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / "SKILL.md"
    path.write_text(f"---\\n{metadata}---\\n{body}", encoding="utf-8")
    return path


def test_repository_skills_are_valid():
    errors, checked = validator.validate_tree()
    assert checked >= 7
    assert errors == []


def test_yaml_comments_are_parsed_correctly(tmp_path):
    path = write_skill(tmp_path / "example", "name: example # stable id\\ndescription: A valid description\\n")
    assert validator.validate_file(path, root=tmp_path) == []


def test_malformed_yaml_is_rejected(tmp_path):
    path = write_skill(tmp_path / "example", 'name: example\\ndescription: "unterminated\\n')
    errors = validator.validate_file(path, root=tmp_path)
    assert any("invalid YAML" in error for error in errors)


def test_non_string_metadata_is_rejected(tmp_path):
    path = write_skill(tmp_path / "example", "name: example\\ndescription: [not, a, string]\\n")
    errors = validator.validate_file(path, root=tmp_path)
    assert any("schema error" in error for error in errors)


def test_unknown_metadata_is_rejected(tmp_path):
    path = write_skill(tmp_path / "example", "name: example\\ndescription: valid\\nowner: someone\\n")
    errors = validator.validate_file(path, root=tmp_path)
    assert any("Additional properties" in error for error in errors)


def test_description_length_is_enforced(tmp_path):
    description = "x" * 1025
    path = write_skill(tmp_path / "example", f"name: example\\ndescription: {description}\\n")
    errors = validator.validate_file(path, root=tmp_path)
    assert any("schema error" in error for error in errors)


def test_invalid_name_is_rejected(tmp_path):
    path = write_skill(tmp_path / "Bad_Name", "name: Bad_Name\\ndescription: Invalid test\\n")
    errors = validator.validate_file(path, root=tmp_path)
    assert any("schema error" in error or "directory must match" in error for error in errors)


def test_missing_entrypoint_is_rejected(tmp_path):
    (tmp_path / "good").mkdir()
    write_skill(tmp_path / "valid", "name: valid\\ndescription: A valid skill\\n")
    errors, checked = validator.validate_tree(tmp_path)
    assert checked == 1
    assert any("missing required SKILL.md" in error for error in errors)


def test_empty_tree_is_rejected(tmp_path):
    errors, checked = validator.validate_tree(tmp_path)
    assert checked == 0
    assert errors
