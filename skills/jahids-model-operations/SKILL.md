---
name: jahids-model-operations
description: Manage JAHIDS.AI model lifecycle, evaluation, deployment readiness, versioning, rollback, and inference budgets.
---

# JAHIDS Model Operations

## Use when
Evaluating, packaging, serving, upgrading, or rolling back an AI model or inference provider.

## Inputs
- Model identifier, version, license, and provenance
- Evaluation dataset and acceptance thresholds
- Runtime hardware, latency, privacy, and cost constraints

## Procedure
1. Verify model source, license, checksum, format, and provenance.
2. Separate training, evaluation, staging, and production artifacts.
3. Define representative quality, safety, latency, throughput, and cost tests.
4. Evaluate prompt injection, tool misuse, data leakage, and refusal behavior.
5. Record hardware requirements, quantization, context limits, and runtime settings.
6. Set inference budgets, concurrency limits, timeouts, and fallback policy.
7. Require approval before changing a production model route or serving version.
8. Preserve the previous known-good version and document rollback steps.

## Output
A model card, evaluation report, serving configuration, budget profile, and rollback plan.

## Verification
Reproduce evaluation results from versioned datasets and verify the selected model/runtime pair in staging.

## Authority boundary
A model score is evidence, not authority. Model output cannot approve its own deployment or expand tool permissions.
