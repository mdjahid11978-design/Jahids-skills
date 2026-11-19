---
name: jahids-release-manager
description: Prepare controlled JAHIDS.AI releases with versioning, change review, CI evidence, release notes, and rollback planning.
---

# JAHIDS Release Manager

## Use when
Preparing a versioned release of a skill library, agent package, SDK, or platform component.

## Inputs
- Approved change set and target version
- CI and security review results
- Release notes, compatibility requirements, and rollback method

## Procedure
1. Confirm the release scope and compare it with the previous release.
2. Check that required reviews and CI jobs passed on the exact release commit.
3. Verify version consistency, dependency metadata, license, and documentation.
4. Classify breaking changes and document migration steps.
5. Draft release notes from verified changes only.
6. Confirm artifact contents and checksums where available.
7. Require explicit authorization before creating or pushing a release tag.
8. Publish through the approved workflow and verify the resulting release page and artifacts.
9. Record rollback or forward-fix steps.

## Output
A release checklist, notes, version, artifact inventory, evidence, and recovery plan.

## Verification
A release is complete only after the platform confirms the tag, workflow success, and published artifacts.

## Authority boundary
Do not merge, tag, publish, or deploy without the required approval.
