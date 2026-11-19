# Release process

JAHIDS.AI Skills uses reviewed, version-tagged releases. The workflow does not create tags, merge pull requests, deploy services, or change production systems.

## Before release

1. Open a pull request and obtain the required review.
2. Confirm CI passes on the exact commit.
3. Review skill content, metadata, license, and dependency changes.
4. Update the project version in `pyproject.toml`.
5. Merge the approved pull request.

## Publish

From the reviewed release commit, create and push a semantic version tag:

```powershell
git checkout main
git pull --ff-only
git tag v0.2.0
git push origin v0.2.0
```

The `Build and publish release` workflow validates the skills, runs tests, builds source and wheel distributions, and creates a GitHub Release with generated notes.

## Recovery

If the workflow fails, inspect the failed job and fix the cause in a new pull request. Do not overwrite a published tag. For a corrected release, increment the version and publish a new tag.
