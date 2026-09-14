# Code Review Security

Targeted security review lens for vulnerabilities, input validation, data protection, authentication/authorization, and secure defaults.

## Canonical source

`SKILL.md` and `rules/` are the canonical contract for this skill. This README is a summary projection and must not introduce an independent rule inventory.

## Consolidated rules

| Rule | Priority | Primary focus |
|------|----------|---------------|
| `sec-injection-defense` | CRITICAL | SQL/process/path injection defense |
| `sec-auth-fail-closed` | CRITICAL | Identity, authorization, tenant isolation |
| `sec-sink-appropriate-escaping` | HIGH | Context-aware escaping at output sinks |
| `sec-input-revalidation` | HIGH | Server-side re-validation and assignment boundaries |
| `sec-secrets-configuration` | HIGH | Secret injection, password hashing, secure configuration |

## Usage

Use this lens when a trust boundary, vulnerability, validation, authorization, secret, or output-sink concern dominates the review. Hand off when resilience, type safety, architecture, or performance becomes primary.

## References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Pi Ensemble security lens](https://raw.githubusercontent.com/randomm/pi-ensemble/main/skill/code-review-security/SKILL.md)
