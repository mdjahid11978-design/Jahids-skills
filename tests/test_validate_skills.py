import importlib.util
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "scripts" / "validate_skills.py"
SPEC = importlib.util.spec_from_file_location("validate_skills", MODULE)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


def write_skill(folder: Path, metadata: str, body: str = "# Skill\n\n## Use when\nx\n\n## Procedure\nx\n\n## Output\nx\n\n## Authority boundary\nx\n") -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / "SKILL.md"
    path.write_text(f"---\n{metadata}---\n{body}", encoding="utf-8")
    return path


def test_repository_skills_are_valid():
    errors, checked = validator.validate_tree()
    expected = {
        'jahids-agent-builder', 'jahids-agent-group-coordinator', 'jahids-api-architect',
        'jahids-data-privacy-steward', 'jahids-documentation-curator', 'jahids-evidence-auditor',
        'jahids-governor-policy', 'jahids-incident-responder', 'jahids-integration-engineer',
        'jahids-mcp-integration', 'jahids-memory-manager', 'jahids-mission-planner',
        'jahids-model-operations', 'jahids-observability-engineer', 'jahids-recovery-manager',
        'jahids-release-manager', 'jahids-repository-maintainer', 'jahids-security-review',
        'jahids-tenant-isolation-auditor', 'jahids-test-engineer', 'jahids-workflow-orchestrator',
    }
    directories = {path.name for path in validator.SKILLS.iterdir() if path.is_dir()}
    assert directories == expected
    assert checked == len(expected)
    assert errors == []


def test_yaml_comments_are_parsed_correctly(tmp_path):
    path = write_skill(tmp_path / "example", "name: example # stable id\ndescription: A valid description\n")
    assert validator.validate_file(path, root=tmp_path) == []


def test_malformed_yaml_is_rejected(tmp_path):
    path = write_skill(tmp_path / "example", 'name: example\ndescription: "unterminated\n')
    errors = validator.validate_file(path, root=tmp_path)
    assert any("invalid YAML" in error for error in errors)


def test_duplicate_yaml_keys_are_rejected(tmp_path):
    path = write_skill(tmp_path / "example", "name: example\ndescription: first\ndescription: second\n")
    errors = validator.validate_file(path, root=tmp_path)
    assert any("duplicate key" in error for error in errors)


def test_non_string_metadata_is_rejected(tmp_path):
    path = write_skill(tmp_path / "example", "name: example\ndescription: [not, a, string]\n")
    errors = validator.validate_file(path, root=tmp_path)
    assert any("metadata schema error" in error for error in errors)


def test_unknown_metadata_is_rejected(tmp_path):
    path = write_skill(tmp_path / "example", "name: example\ndescription: valid\nowner: someone\n")
    errors = validator.validate_file(path, root=tmp_path)
    assert any("Additional properties" in error for error in errors)


def test_description_length_is_enforced(tmp_path):
    description = "x" * 1025
    path = write_skill(tmp_path / "example", f"name: example\ndescription: {description}\n")
    errors = validator.validate_file(path, root=tmp_path)
    assert any("metadata schema error" in error for error in errors)


def test_invalid_name_is_rejected(tmp_path):
    path = write_skill(tmp_path / "Bad_Name", "name: Bad_Name\ndescription: Invalid test\n")
    errors = validator.validate_file(path, root=tmp_path)
    assert any("metadata schema error" in error or "directory must match" in error for error in errors)


def test_missing_entrypoint_is_rejected(tmp_path):
    (tmp_path / "good").mkdir()
    write_skill(tmp_path / "valid", "name: valid\ndescription: A valid skill\n")
    errors, checked = validator.validate_tree(tmp_path)
    assert checked == 1
    assert any("missing required SKILL.md" in error for error in errors)


def test_empty_tree_is_rejected(tmp_path):
    errors, checked = validator.validate_tree(tmp_path)
    assert checked == 0
    assert errors


def test_missing_required_section_is_rejected(tmp_path):
    path = write_skill(tmp_path / "example", "name: example\ndescription: valid\n", body="# Example\n")
    errors = validator.validate_file(path, root=tmp_path)
    assert any("missing required section" in error for error in errors)


def test_block_scalar_description_at_schema_limit_is_valid(tmp_path):
    description = "x" * 1023
    metadata = "name: example\ndescription: |\n  " + description + "\n"
    path = write_skill(tmp_path / "example", metadata)
    assert validator.validate_file(path, root=tmp_path) == []


def test_block_scalar_description_over_schema_limit_is_rejected(tmp_path):
    description = "x" * 1024
    metadata = "name: example\ndescription: |\n  " + description + "\n"
    path = write_skill(tmp_path / "example", metadata)
    errors = validator.validate_file(path, root=tmp_path)
    assert any("metadata schema error" in error for error in errors)


def test_empty_frontmatter_is_reported_as_non_mapping(tmp_path):
    folder = tmp_path / "example"
    folder.mkdir()
    path = folder / "SKILL.md"
    path.write_text("---\n---\n# Example\n", encoding="utf-8")
    errors = validator.validate_file(path, root=tmp_path)
    assert any("frontmatter must be a YAML mapping" in error for error in errors)


def test_invalid_implicit_date_is_reported_and_does_not_abort(tmp_path):
    path = write_skill(tmp_path / "invalid-date", "name: invalid-date\ndescription: 2026-02-30\n")
    errors = validator.validate_file(path, root=tmp_path)
    assert any("invalid YAML frontmatter" in error for error in errors)


def test_quoted_date_description_is_valid(tmp_path):
    path = write_skill(tmp_path / "quoted-date", 'name: quoted-date\ndescription: "2026-02-30"\n')
    assert validator.validate_file(path, root=tmp_path) == []


def test_invalid_explicit_timestamp_is_reported(tmp_path):
    path = write_skill(tmp_path / "bad-timestamp", "name: bad-timestamp\ndescription: !!timestamp today\n")
    errors = validator.validate_file(path, root=tmp_path)
    assert any("invalid YAML frontmatter" in error for error in errors)


def test_invalid_timestamp_does_not_abort_tree_validation(tmp_path):
    write_skill(tmp_path / "invalid-date", "name: invalid-date\ndescription: 2026-02-30\n")
    write_skill(tmp_path / "valid", "name: valid\ndescription: A valid skill\n")
    errors, checked = validator.validate_tree(tmp_path)
    assert checked == 2
    assert any("invalid YAML frontmatter" in error for error in errors)
