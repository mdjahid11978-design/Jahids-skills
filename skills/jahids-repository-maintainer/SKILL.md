---
name: jahids-repository-maintainer
description: Maintain JAHIDS.AI repositories through safe inspection, scoped branches, quality checks, documentation, and reviewable pull requests.
---

# JAHIDS Repository Maintainer

## Use when
Maintaining a repository, resolving issues, updating dependencies, improving documentation, or preparing a pull request.

## Inputs
- Repository and target branch
- Requested outcome and acceptance criteria
- Available permissions and local or hosted execution environment

## Procedure
1. Confirm repository identity, visibility, default branch, permissions, and working-tree state.
2. Inspect relevant files, recent commits, open pull requests, and existing automation.
3. Preserve user work; never overwrite unrelated changes.
4. Create a narrowly scoped feature branch from the intended base.
5. Make the smallest coherent change and update documentation or tests.
6. Run available validation and capture exact results.
7. Review the diff for secrets, generated noise, licensing, and scope creep.
8. Open a pull request with summary, tests, risks, and rollback notes.
9. Leave merge, repository deletion, visibility changes, and deployment to explicit authorization.

## Output
An inspection record, scoped change set, validation evidence, and review-ready pull request.

## Verification
Confirm branch, commit, changed files, CI state, and PR URL from repository evidence.

## Authority boundary
Repository access is not blanket permission to alter every repository or change repository administration settings.
