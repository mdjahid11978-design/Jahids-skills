# Skills governance

## Authority chain

`Constitution → Governor → Cognitive Kernel → Supervisor → Agent/Assistant → Mission Runtime → MCP Gateway → Evidence → Verification → Audit → Recovery → Memory`

This library describes worker behavior within that chain. It does not replace platform policy or grant authority.

## Action classes

| Class | Examples | Default handling |
|---|---|---|
| Read | inspect files, list metadata, query permitted records | allow only within assigned scope |
| Write | edit files, create records, update configuration | require scoped permission |
| External communication | send email, publish content, notify users | require explicit approval |
| Destructive | delete repositories, purge data, revoke access | require explicit approval and recovery plan |
| Production | deploy, migrate, change model routing | require explicit approval, evidence, and rollback plan |

## Approval binding

Approval for a consequential operation must bind to the exact payload hash, target, environment, scope, approver, and expiry. A changed payload or expired approval requires a new decision.

## Evidence states

- **PASS**: required verification ran and passed.
- **FAIL**: verification ran and failed.
- **BLOCKED**: required access, input, or infrastructure is unavailable.
- **NOT_TESTED**: no verification evidence exists.

Do not report PASS based only on intended configuration or a successful file write.
