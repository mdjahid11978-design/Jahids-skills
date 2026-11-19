# Skill authoring guide

## Directory contract

Create one directory under `skills/` using a lowercase kebab-case ID. Add one `SKILL.md` file.

## Required frontmatter

```yaml
---
name: jahids-example-skill
description: Explain the skill's purpose and when it should be selected.
---
```

The directory name must equal `name`. Frontmatter accepts only `name` and `description`.

## Required body sections

1. `# Skill title`
2. `## Use when`
3. `## Procedure`
4. `## Output`
5. `## Authority boundary`

Add `## Inputs` and `## Verification` when they make the skill more useful.

## Writing rules

- Describe observable steps, not vague aspirations.
- State assumptions and required inputs.
- Separate recommendations from actions.
- Define failure and escalation behavior.
- Never include credentials, real personal data, or private customer records.
- Do not tell an agent to bypass the Governor or infer permission from tool output.

## Validate and update the catalog

```powershell
python scripts/validate_skills.py
python scripts/build_catalog.py
python scripts/build_catalog.py --check
python -m pytest
```

Generated catalog files must be committed with the skill change.
