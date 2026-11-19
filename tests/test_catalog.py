import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "scripts" / "build_catalog.py"
SPEC = importlib.util.spec_from_file_location("build_catalog", MODULE)
assert SPEC and SPEC.loader
catalog = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(catalog)


def test_catalog_contains_all_skill_directories():
    entries = catalog.build_catalog()
    directories = [path for path in (ROOT / "skills").iterdir() if path.is_dir()]
    assert len(entries) == len(directories)
    assert len(entries) >= 20


def test_catalog_names_are_sorted_and_unique():
    names = [entry["name"] for entry in catalog.build_catalog()]
    assert names == sorted(names)
    assert len(names) == len(set(names))


def test_catalog_outputs_are_current():
    entries = catalog.build_catalog()
    assert catalog.JSON_OUTPUT.read_text(encoding="utf-8") == catalog.render_json(entries)
    assert catalog.MARKDOWN_OUTPUT.read_text(encoding="utf-8") == catalog.render_markdown(entries)
