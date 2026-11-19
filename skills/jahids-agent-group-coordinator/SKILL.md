---
name: jahids-agent-group-coordinator
description: Coordinate bounded JAHIDS.AI agent groups with explicit roles, task dependencies, shared context, budgets, handoffs, and supervision.
---

# JAHIDS Agent Group Coordinator

## Use when
A mission needs multiple agents or assistants working on distinct but coordinated tasks.

## Inputs
- Mission goal and acceptance criteria
- Agent registry, capabilities, and policy constraints
- Shared budget, deadlines, and autonomy level

## Procedure
1. Break the mission into tasks with clear ownership and dependency edges.
2. Select agents by verified capability and least-privilege tool scope.
3. Assign one accountable owner per task and define handoff contracts.
4. Set shared and per-agent token, time, cost, concurrency, and retry budgets.
5. Define shared context with provenance; avoid uncontrolled shared writable memory.
6. Track task state, blockers, evidence, and dependency completion.
7. Detect duplicate work, conflicting outputs, deadlocks, and budget exhaustion.
8. Escalate scope changes and consequential actions to the Governor.
9. Reconcile outputs against mission acceptance criteria before completion.

## Output
An agent-group plan, task graph, role map, budget allocation, handoff records, and consolidated evidence.

## Verification
Every task has an owner, status, output, and evidence. The group cannot report mission completion while required tasks remain unresolved.

## Authority boundary
Coordination does not grant agents shared authority or allow one agent to approve another agent's restricted actions.
