# Contributing

## Before editing

1. Confirm the repository and base branch.
2. Read the architecture, governance, and skill authoring docs.
3. Open an issue or record the intended scope when the change is substantial.
4. Create a feature branch and preserve unrelated work.

## Required checks

```powershell
python -m pip install -e ".[dev]"
python scripts/validate_skills.py
python scripts/build_catalog.py
python scripts/build_catalog.py --check
python -m pytest
python -m build --sdist
```

## Pull requests

Include:
- User problem and scope
- Skills or schemas changed
- Validation and test results
- Security, privacy, licensing, and compatibility notes
- Any blocked or untested items

Do not merge, publish a release, or deploy a platform service without the required approval.
