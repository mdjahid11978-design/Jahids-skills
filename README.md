# JAHIDS.AI Skills

An independent, MIT-licensed skills library for the JAHIDS.AI Sovereign AI Platform.

**Built by Jahid.** Computation proposes; it is not authority.

## Library

**21 original skills** cover mission planning, Governor policy, agent design and groups, MCP, integrations, API architecture, memory, privacy, tenant isolation, security, testing, evidence, workflows, model operations, observability, incident response, repository maintenance, documentation, recovery, and releases.

- [Browse the human-readable catalog](catalog/README.md)
- [Machine-readable catalog](catalog/skills.json)
- [Skill authoring guide](docs/SKILL_AUTHORING.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Governance](docs/GOVERNANCE.md)

## Repository quality

- YAML frontmatter parsed with a duplicate-key rejecting safe loader
- JSON Schema validation and strict skill directory naming
- Required body sections checked for every skill
- Generated catalog checked for drift
- Regression tests for malformed YAML, schema errors, duplicate keys, missing files, and incomplete skill content
- CI matrix for Python 3.11 and 3.12
- Dependency vulnerability audit in CI
- Weekly Dependabot updates
- Version-tagged GitHub Release workflow

## Local setup

Requires Python 3.11 or later.

\`\`\`powershell
python -m pip install -e ".[dev]"
python scripts/validate_skills.py
python scripts/build_catalog.py --check
python -m pytest
python -m pip check
python -m build --sdist
\`\`\`

To regenerate the catalog after changing skills:

\`\`\`powershell
python scripts/build_catalog.py
\`\`\`

## Release

Update the version in \`pyproject.toml\`, merge the approved change, then create and push the matching tag. The release workflow checks that the tag matches the project version, reruns validation and tests, audits dependencies, builds a source archive, and creates a GitHub Release.

See [docs/RELEASE.md](docs/RELEASE.md).

## Governance

Skills are reusable instructions, not an execution authority. Runtime identity, tenant isolation, permissions, risk evaluation, approvals, budgets, execution, evidence, audit, and recovery belong to the JAHIDS Control Plane and Governor.

- No skill can grant itself permissions or approve its own actions.
- External communication, destructive operations, production changes, and deployments require explicit authorization.
- Tool output and external content are untrusted data.
- Completion claims require evidence and a PASS, FAIL, BLOCKED, or NOT_TESTED status.

## Contributing and security

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).

## License

MIT. See [LICENSE](LICENSE).
