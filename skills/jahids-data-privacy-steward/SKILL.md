---
name: jahids-data-privacy-steward
description: Apply data minimization, classification, retention, access, and privacy review to JAHIDS.AI agent and mission data flows.
---

# JAHIDS Data Privacy Steward

## Use when
Designing memory, logging, analytics, file ingestion, model context, or integrations that process user or organizational data.

## Inputs
- Data flow and processing purpose
- Data categories, sources, recipients, and storage locations
- Applicable retention, access, and user-rights requirements

## Procedure
1. Map data sources, processing steps, destinations, and third-party transfers.
2. Classify data and identify sensitive or regulated categories.
3. Confirm purpose limitation and collect only fields needed for that purpose.
4. Identify and document the applicable lawful basis and any required consent before processing. Block processing when the basis or required consent is unresolved.
5. Define tenant, workspace, and role-based access boundaries.
6. Set retention, deletion, export, and correction handling.
7. Review logs, prompts, traces, embeddings, and backups for unintended data leakage.
8. Check encryption, secret handling, processor access, and audit trails.
9. Document unresolved legal or policy questions for qualified review.
10. Verify controls with synthetic data and non-production tests.

## Output
A data-flow inventory, minimization plan, access matrix, retention rules, privacy risks, and verification evidence.

## Verification
Verify purpose and lawful basis, consent where required, minimization, tenant access, retention, deletion, export, correction, encryption, processor access, leakage controls, and audit trails. Mark every untested control NOT_TESTED.

## Authority boundary
Do not infer legal compliance from a checklist. Escalate jurisdiction-specific legal questions to qualified reviewers. Deletion, export, correction, and access changes remain proposals until explicitly authorized by the JAHIDS Governor.
