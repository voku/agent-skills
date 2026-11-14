---
name: code-review-security
description: Security-focused review lens for identifying injection risks, auth flaws, secret exposure, unsafe configuration, and missing validation during code review.
license: MIT
metadata:
  author: Agent Skills Team
  version: "2.0.0"
---

# Code Review Security

Targeted security review lens for vulnerabilities, input validation, data protection, authentication/authorization, and secure defaults.

## Quick Reference

| Category | Priority | Rule File | Primary Focus |
|----------|----------|-----------|---------------|
| **Injection Defense** | CRITICAL | [`sec-injection-defense`](rules/sec-injection-defense.md) | Parameterized SQL queries, process execution without shell strings, path traversal checks |
| **Auth & Authorization** | CRITICAL | [`sec-auth-fail-closed`](rules/sec-auth-fail-closed.md) | Fail-closed user identity, tenant query scoping (IDOR prevention), policy gate enforcement |
| **Context Escaping** | HIGH | [`sec-sink-appropriate-escaping`](rules/sec-sink-appropriate-escaping.md) | Clean raw storage in DB/LDAP, context-aware escaping strictly at template output sinks |
| **Input Re-validation** | HIGH | [`sec-input-revalidation`](rules/sec-input-revalidation.md) | Server-side FK/status re-validation for dropdown choices, mass-assignment protection |
| **Secrets & Config** | HIGH | [`sec-secrets-configuration`](rules/sec-secrets-configuration.md) | Environment secret injection, Argon2id password hashing, secure cookie flags |

---

## Scope

Run this lens when security is the dominant concern or a workflow explicitly dispatches it. Do not broaden into a generic review bundle.

Out of scope as primary concerns: type coverage, retry hygiene without security impact, performance/architecture trade-offs, readability-only feedback.

## Handoff

When another concern becomes dominant, emit **at most one** focused handoff with the observed `path:line` and why that concern is dominant:

- `code-review-error-handling` for cleanup/retry/failure behavior weakening controls;
- `code-review-type-safety` for untrusted shape or validation proof;
- `code-review-architecture` for broken authz/trust boundaries;
- `code-review-performance` for user-triggerable cost amplification.

## Evidence Discipline

- Identify the trust boundary and concrete sink/control before claiming a vulnerability.
- When the diff changes untrusted input, authorization, persistence, or output encoding, construct one relevant adversarial input and trace validation, authorization, persistence, and output handling.
- Keep sanitization, persistence formatting, and output escaping context-specific; do not treat one as a substitute for another.
- If required trust-boundary evidence cannot be inspected, return `blocked` instead of guessing.
- Prefer secure defaults and smaller attack surface over configurable complexity.

## Terminal Contract

```text
STATUS: findings
<path>:<line>: <CRITICAL|HIGH|MEDIUM|LOW> <problem>. <concrete fix>.
HANDOFF: <code-review-* lens> <path>:<line> <why this concern is dominant>   # optional, at most one
```

```text
STATUS: clean
```

```text
STATUS: blocked
UNKNOWN: <exact missing evidence>.
```

`STATUS` is this lens' judgment only. The caller owns merge, dedupe, precedence, approval, persistence, and workflow progression.

## Severity

- **CRITICAL**: direct exploitable RCE, SQL injection, authentication bypass, IDOR, or credential leak.
- **HIGH**: missing authorization gate, unescaped XSS sink, missing server-side input re-validation, or insecure cookies.
- **MEDIUM**: defense-in-depth gaps, verbose error disclosure, or weak cryptographic parameters.
- **LOW**: minor configuration hygiene or suboptimal header flags.

## References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Pi Ensemble security lens](https://raw.githubusercontent.com/randomm/pi-ensemble/main/skill/code-review-security/SKILL.md)
