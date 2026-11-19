---
name: jahids-incident-responder
description: Coordinate JAHIDS.AI incident triage, containment, evidence preservation, communication, and recovery under approved authority.
---

# JAHIDS Incident Responder

## Use when
A service, agent, integration, account, or data boundary shows a security or reliability incident.

## Inputs
- Alert or incident report
- Affected service, tenant, and time window
- Available runbooks and authorized response roles

## Procedure
1. Record the report, time, affected scope, and confidence.
2. Classify severity and notify the designated incident owner.
3. Preserve relevant logs and evidence with access controls.
4. Stop unsafe automation or isolate affected components only within granted authority.
5. Avoid destructive cleanup before evidence capture.
6. Determine impact, affected identities, data, and external dependencies.
7. Coordinate containment and recovery with the authorized owner.
8. Verify service restoration and monitor for recurrence.
9. Produce a timeline, root-cause analysis, and tracked corrective actions.

## Output
An incident timeline, severity assessment, evidence record, containment actions, recovery status, and follow-up list.

## Verification
Confirm containment and recovery through observable system evidence; distinguish confirmed impact from unknown scope.

## Authority boundary
Emergency access must follow the organization's incident policy. Do not independently access unrelated accounts, destroy evidence, or notify external parties without authorization.
