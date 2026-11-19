---
name: jahids-integration-engineer
description: Build and maintain safe JAHIDS.AI integrations with external services using scoped credentials, contracts, retries, and audit evidence.
---

# JAHIDS Integration Engineer

## Use when
Connecting email, storage, issue trackers, databases, cloud services, or third-party APIs.

## Inputs
- Provider documentation and account scope
- Required data flows and operations
- Credential, privacy, and availability constraints

## Procedure
1. Verify provider identity, official API endpoint, and supported authentication.
2. Define minimum scopes and store credentials in an approved secret manager.
3. Map inbound and outbound data, including retention and deletion behavior.
4. Validate requests and responses against explicit schemas.
5. Add timeouts, rate-limit handling, bounded retries, and idempotency.
6. Classify every operation as read, write, external communication, or destructive.
7. Route consequential operations through Governor approval.
8. Add contract tests with synthetic data and record integration evidence.

## Output
An integration design, scope list, data-flow map, error policy, tests, and operations guide.

## Verification
Run contract tests in a non-production account and confirm denied operations fail closed.

## Authority boundary
Possession of an API credential is not permission to use every provider capability.
