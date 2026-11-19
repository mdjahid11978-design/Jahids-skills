---
name: jahids-api-architect
description: Design versioned JAHIDS.AI APIs with stable contracts, authentication, tenant isolation, rate limits, and compatibility rules.
---

# JAHIDS API Architect

## Use when
Designing or reviewing REST, WebSocket, event, or SDK-facing API contracts.

## Inputs
- Product use cases and consumers
- Data model and authorization requirements
- Reliability, latency, and compatibility targets

## Procedure
1. Define resources, operations, events, and consumer workflows.
2. Specify request and response schemas, validation, pagination, errors, and idempotency.
3. Define authentication and server-side authorization for every operation.
4. Resolve tenant and workspace context from trusted identity, never caller-controlled tenant headers alone.
5. Set rate, payload, timeout, and concurrency limits.
6. Define versioning, deprecation, compatibility, and migration policy.
7. Document audit events and privacy-safe observability.
8. Add contract tests for success, invalid input, denied access, and backward compatibility.

## Output
An API specification, auth matrix, version policy, error model, and contract test plan.

## Verification
Validate schemas and run consumer contract tests against the documented API version.

## Authority boundary
API design does not authorize exposing data, granting scopes, or deploying endpoints.
