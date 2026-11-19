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
4. Define tenant, workspace, and role-based access boundaries.
5. Set retention, deletion, export, and correction handling.
6. Review logs, prompts, traces, embeddings, and backups for unintended data leakage.
7. Check encryption, secret handling, processor access, and audit trails.
8. Document unresolved legal or policy questions for qualified review.
9. Verify controls with synthetic data and non-production tests.

## Output
A data-flow inventory, minimization plan, access matrix, retention rules, privacy risks, and verification evidence.

## Verification
Trace representative records end to end and confirm each storage and access control against the documented policy.

## Authority boundary
Do not infer legal compliance from a checklist. Escalate jurisdiction-specific legal questions to qualified reviewers.
