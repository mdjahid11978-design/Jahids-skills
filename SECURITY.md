# Security policy

## Reporting

Do not publish secrets, exploit details, or private user data in a public issue. Report suspected vulnerabilities privately through the repository owner's GitHub security reporting channel when enabled. If private reporting is unavailable, contact the repository owner through a trusted private channel.

## Scope

Report issues involving:
- unsafe instructions that bypass Governor approval
- credential or private-data exposure
- tenant or workspace isolation failures
- unsafe CI permissions or dependency handling
- misleading claims about validation or execution authority

## Handling

Preserve evidence, avoid accessing unrelated data, and do not test destructive behavior against production systems. Security reports should include affected files or versions, impact, reproduction steps using synthetic data, and suggested mitigation.
