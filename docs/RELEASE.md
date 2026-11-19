# Release process

JAHIDS.AI Skills publishes reviewed source archives. It does not publish a Python runtime wheel or deploy platform services.

## Before release

1. Update the version in `pyproject.toml` and prepare the release notes in the same pull request.
2. Regenerate and verify the skill catalog.
3. Require CI and review to pass on the exact proposed release commit.
4. Merge the approved pull request into `main` and record the resulting merge commit SHA.
5. Obtain explicit JAHIDS Governor approval for that exact merged commit and version.

## Publish the reviewed commit

Use the recorded merge commit SHA. Do not tag whatever happens to be the latest `main` commit.

```powershell
git fetch origin main --no-tags
git merge-base --is-ancestor <reviewed-merge-sha> origin/main
git tag -a v0.2.0 <reviewed-merge-sha> -m "JAHIDS.AI Skills v0.2.0"
git push origin v0.2.0
```

The release workflow independently checks that the tagged commit is an ancestor of `origin/main`, checks that the tag matches `pyproject.toml`, reruns validation and tests, audits dependencies, and builds the source distribution. The publishing job has write permission only after the read-only build job succeeds and downloads the verified artifact.

## GitHub settings required

Configure these repository controls before enabling public releases:

1. **Environment:** create a GitHub environment named `release`, add required reviewers, and prevent self-review where available. The publish job waits for this environment gate.
2. **Tag ruleset:** target `refs/tags/v*`, restrict tag creation to release maintainers, and block tag updates and deletion.
3. **Main branch:** require pull requests, at least one approval, and the `Python 3.11` and `Python 3.12` validation checks. Block force pushes and branch deletion.

The workflow checks that a release commit is on `main`; repository rulesets and environment reviewers provide the administrative approval gate.

## Recovery

If CI or publishing fails, inspect the failed job and fix the cause in a new pull request. Do not overwrite a published tag. For a corrected release, increment the version and publish a new tag.
