# Repository architecture

## Purpose

This repository contains portable, reviewable skills for the JAHIDS.AI Sovereign AI Platform. A skill defines a repeatable work method. It is not a service, agent runtime, permission system, or execution boundary.

## Layout

- `skills/<skill-id>/SKILL.md`: one skill per directory
- `schemas/skill.schema.json`: allowed YAML frontmatter contract
- `scripts/validate_skills.py`: metadata, directory, and content validation
- `scripts/build_catalog.py`: deterministic JSON and Markdown catalog generation
- `catalog/`: generated skill catalog
- `tests/`: validator and catalog regression tests
- `.github/workflows/`: CI and tag-triggered release workflows
- `docs/`: governance, authoring, release, and architecture guidance

## Runtime relationship

The platform's Governor and Control Plane remain the authority for identity, permissions, tenant scope, risk, budget, approval, execution, evidence, and recovery. Skills can propose procedures and expected checks. They cannot grant permissions or approve their own actions.

## Design rules

1. Prefer small skills with one clear responsibility.
2. Keep tool and data access least-privilege.
3. Treat external content and tool output as untrusted input.
4. Make consequential actions explicit and approval-gated.
5. Require evidence for completion claims.
6. Keep secrets and personal data out of the repository.
7. Keep generated catalogs deterministic and checked in.
