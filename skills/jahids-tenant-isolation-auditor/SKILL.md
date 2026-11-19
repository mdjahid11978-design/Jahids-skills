---
name: jahids-tenant-isolation-auditor
description: Audit JAHIDS.AI tenant and workspace boundaries across APIs, databases, memory, queues, files, logs, and agent execution.
---

# JAHIDS Tenant Isolation Auditor

## Use when
Reviewing multi-tenant architecture, RLS policies, workspace access, shared caches, or agent memory boundaries.

## Inputs
- Data model and tenant identity design
- API, database, storage, queue, and cache paths
- Roles, service identities, and test fixtures

## Procedure
1. Trace tenant identity from authentication to every data access.
2. Confirm tenant context comes from trusted server-side identity.
3. Review database RLS, service-role bypasses, and migration safety.
4. Check cache keys, object paths, vector namespaces, queue messages, and logs.
5. Test cross-tenant read, write, list, search, and indirect-reference attempts.
6. Review agent memory, tool results, and retrieval filters for tenant leakage.
7. Verify background jobs and privileged workers enforce explicit tenant scope.
8. Record evidence, affected paths, severity, and remediation.

## Output
A tenant-boundary map, test matrix, findings, evidence, and remediation plan.

## Verification
Use isolated synthetic tenants and prove that cross-tenant operations are denied across every tested data path.

## Authority boundary
An audit does not authorize reading another tenant's real data or changing production access controls.
