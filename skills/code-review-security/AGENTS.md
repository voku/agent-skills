# Code Review Security — Agent Projection

**Version:** 2.0.0  
**Rules:** 5 consolidated rules  
**License:** MIT

This file is a compact projection for agents. The canonical contract is `SKILL.md` plus the files under `rules/`. Do not add independent security-review semantics here.

## Fast Path

1. Use this lens only when security is the dominant concern.
2. Read `SKILL.md` first.
3. Load only rule files relevant to the observed trust boundary, sink, or control.
4. Trace untrusted input through validation, authorization, persistence, and output handling when those boundaries changed.
5. Hand off to at most one focused review lens when another concern becomes dominant.

## Rule Index

| Rule | Priority | Focus |
|------|----------|-------|
| [`sec-injection-defense`](rules/sec-injection-defense.md) | CRITICAL | SQL/process/path injection defense |
| [`sec-auth-fail-closed`](rules/sec-auth-fail-closed.md) | CRITICAL | Identity, authorization, tenant isolation |
| [`sec-sink-appropriate-escaping`](rules/sec-sink-appropriate-escaping.md) | HIGH | Context-aware escaping at output sinks |
| [`sec-input-revalidation`](rules/sec-input-revalidation.md) | HIGH | Server-side re-validation and assignment boundaries |
| [`sec-secrets-configuration`](rules/sec-secrets-configuration.md) | HIGH | Secret injection, password hashing, secure configuration |

## Evidence Boundary

- Identify the concrete trust boundary and sink/control before claiming a vulnerability.
- Keep sanitization, storage representation, and output escaping context-specific.
- If required trust-boundary evidence cannot be inspected, report `blocked` rather than guessing.

## Terminal Contract

Follow the exact `STATUS: findings|clean|blocked` contract in `SKILL.md`. The caller owns merge, dedupe, approval, persistence, and workflow progression.
