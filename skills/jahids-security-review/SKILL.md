---
name: jahids-security-review
description: Review JAHIDS.AI code, agent designs, integrations, and workflows for security risks, trust-boundary failures, and unsafe permissions.
---

# JAHIDS Security Review

## Use when
Reviewing code, infrastructure, agent manifests, MCP tools, CI workflows, or proposed changes that affect identity, data, permissions, or execution.

## Inputs
- Change set, repository, or system design
- Intended users, data classes, and deployment environment
- Threat model and applicable policy requirements

## Procedure
1. Identify assets, trust boundaries, principals, tenants, and entry points.
2. Trace authentication, authorization, secret handling, and tenant isolation.
3. Check input validation, output handling, injection risks, dependency exposure, and logging.
4. Review tool permissions and classify read, write, destructive, and external actions.
5. Check approval binding, replay protection, rate limits, budgets, and kill-switch behavior.
6. Test failure paths and adversarial inputs in an authorized non-production environment with synthetic data; any production testing requires separate explicit Governor approval and a documented safety plan.
7. Rank findings by impact and likelihood; include exact evidence and remediation.
8. Re-test fixes and record any residual risk.

## Output
A finding list with severity, affected component, evidence, reproduction steps, remediation, and verification status.

## Verification
Every finding must link to a concrete code location, configuration, test, or observed behavior. Mark untested claims NOT_TESTED.

## Authority boundary
A security review does not grant permission to exploit systems, access unrelated data, or change production controls.
