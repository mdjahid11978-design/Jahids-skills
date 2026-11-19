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
4. If the worktree contains unrelated edits, isolate them in a separate worktree or safely preserve them before branching.
5. Create a narrowly scoped feature branch from the intended base.
6. Make the smallest coherent change and update documentation or tests.
7. Run available validation and capture exact results.
8. Review the diff for secrets, generated noise, licensing, and scope creep.
9. Obtain explicit Governor authorization before opening a pull request, which can trigger CI and external notifications; then include summary, tests, risks, and rollback notes.
10. Leave merge, repository deletion, visibility changes, and deployment to explicit JAHIDS Governor authorization.

## Output
An inspection record, scoped change set, validation evidence, and review-ready pull request.

## Verification
Confirm branch, commit, changed files, CI state, and PR URL from repository evidence. Report each check as PASS, FAIL, BLOCKED, or NOT_TESTED.

## Authority boundary
Repository access is not blanket permission to alter every repository or change repository administration settings. The JAHIDS Governor authorizes consequential actions.
