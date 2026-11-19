---
name: jahids-test-engineer
description: Design and run layered tests for JAHIDS.AI skills, agents, APIs, integrations, and mission workflows.
---

# JAHIDS Test Engineer

## Use when
Defining acceptance tests, investigating regressions, validating a release, or testing agent and tool behavior.

## Inputs
- Acceptance criteria and expected behavior
- Relevant code, schemas, interfaces, and supported environments
- Safe test data and available test tools

## Procedure
1. Convert every acceptance criterion into an observable test and map it to one or more required checks.
2. Cover normal, boundary, malformed, unauthorized, timeout, retry, and recovery cases.
3. Separate unit, contract, integration, end-to-end, and security tests.
4. Use deterministic fixtures and isolated test resources.
5. Never use production credentials or destructive production data.
6. Record exact commands, environment, versions, and test output.
7. Re-run focused tests after fixes, then the full relevant suite.
8. Treat skipped, filtered, or unexecuted required tests as BLOCKED or NOT_TESTED, never PASS.
9. Report flaky tests and missing coverage instead of hiding them.

## Output
A test plan, test cases, execution evidence, defects, coverage gaps, and PASS/FAIL/BLOCKED/NOT_TESTED status.

## Verification
A PASS requires complete acceptance-criterion coverage, successful execution of every required test, no unexplained skips, and captured output from the exact commit.

## Authority boundary
The JAHIDS Governor controls test scope and permissions. Test execution or a passing result does not grant authority for production writes, external notifications, or deployment.
