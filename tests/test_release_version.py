import importlib.util
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "scripts" / "check_release_version.py"
SPEC = importlib.util.spec_from_file_location("check_release_version", MODULE)
assert SPEC and SPEC.loader
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


def test_current_project_tag_matches():
    assert checker.validate_tag(f"v{checker.project_version()}")[0]


def test_wrong_version_is_rejected():
    valid, message = checker.validate_tag("v99.0.0")
    assert not valid
    assert "does not match" in message


def test_non_semver_tag_is_rejected():
    valid, message = checker.validate_tag("latest")
    assert not valid
    assert "semantic version" in message
