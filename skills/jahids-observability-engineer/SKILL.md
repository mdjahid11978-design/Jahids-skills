---
name: jahids-observability-engineer
description: Define JAHIDS.AI logs, metrics, traces, alerts, and service-level indicators with privacy and tenant boundaries.
---

# JAHIDS Observability Engineer

## Use when
Adding monitoring to services, agents, workflows, mission execution, or tool integrations.

## Inputs
- Service and dependency map
- User-facing reliability goals
- Data classification and retention policy

## Procedure
1. Map service boundaries, critical paths, and dependency failure modes.
2. Define service-level indicators for availability, latency, correctness, and queue health.
3. Add structured logs with correlation IDs and explicit tenant-safe access controls.
4. Add metrics for task outcomes, retries, queue age, token/cost budgets, and tool failures.
5. Trace mission and agent handoffs without recording secrets or unnecessary personal data.
6. Define actionable alerts with owner, severity, and runbook.
7. Set sampling, retention, access, and cardinality limits.
8. Test telemetry during normal operation and controlled failures.

## Output
An observability plan, dashboards, alert rules, retention settings, and runbooks.

## Verification
Trigger a safe test event and trace it across the expected components without exposing restricted data.

## Authority boundary
Observability access is read-only by default and does not authorize changing production systems.
