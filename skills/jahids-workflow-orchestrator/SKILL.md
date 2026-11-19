---
name: jahids-workflow-orchestrator
description: Build reliable JAHIDS.AI workflows with explicit states, dependencies, retries, checkpoints, idempotency, and approval gates.
---

# JAHIDS Workflow Orchestrator

## Use when
Turning multi-step work into a durable workflow or mission runtime.

## Inputs
- Workflow goal and completion criteria
- Task dependencies and external systems
- Retry, budget, timeout, and approval requirements

## Procedure
1. Model the workflow as explicit states and transitions.
2. Define task inputs, outputs, owners, and dependency edges.
3. Make side-effecting steps idempotent or add deduplication keys.
4. Persist checkpoints and use leases or fencing for concurrent workers.
5. Set bounded retries, backoff, deadlines, and dead-letter handling.
6. Pause at approval states and bind approval to the exact operation.
7. Handle cancellation, compensation, partial completion, and recovery.
8. Emit evidence and audit events for each state transition.

## Output
A workflow definition, state diagram, retry policy, checkpoint plan, and acceptance tests.

## Verification
Test duplicate delivery, worker crash, timeout, cancellation, stale lease, and recovery from the last checkpoint.

## Authority boundary
The orchestrator schedules approved work; it cannot bypass Governor decisions or reuse expired approvals.
