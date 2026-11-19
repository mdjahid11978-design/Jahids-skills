---
name: jahids-documentation-curator
description: Maintain accurate JAHIDS.AI technical documentation, skill references, API guides, examples, and change history.
---

# JAHIDS Documentation Curator

## Use when
Creating or updating platform docs, skill guides, architecture records, examples, or release notes.

## Inputs
- Source implementation or approved design
- Target audience and documentation location
- Verified behavior and version scope

## Procedure
1. Identify the source of truth and intended reader.
2. Separate implemented behavior from planned or proposed behavior.
3. Check links, commands, versions, configuration names, and code examples.
4. Include prerequisites, expected output, failure cases, and recovery steps.
5. Remove secrets, personal data, and unsupported claims from examples.
6. Keep terminology and architecture names consistent across docs.
7. Link changes to relevant issues, commits, and releases where available.
8. Review docs against the current implementation before publication.

## Output
A documentation change set with tested examples, version notes, and source references.

## Verification
Run documented commands in a clean environment where possible and mark untested instructions clearly.

## Authority boundary
Documentation cannot grant permissions or describe a planned feature as already deployed.
