# API Design Patterns - Agent Projection

This file is a compact routing projection. The canonical contract is `SKILL.md` plus the non-underscore rule files under `rules/`. Do not maintain a second rule inventory, standards catalog, or compiled example set here.

## Fast Path

1. Inspect the target API's existing routes, public contract, compatibility/versioning policy, auth model, error format, query conventions, and OpenAPI/tests.
2. Read `SKILL.md` first and load only the relevant canonical rules.
3. Preserve existing public behavior unless the task explicitly requires a migration.
4. Prefer standard HTTP semantics and current RFCs where they fit the owned API contract.
5. Validate with repository-owned contract tests, HTTP integration tests, linters, and runtime evidence.

## Ownership Boundary

- `SKILL.md` owns activation, rule routing, standards boundaries, and decision discipline.
- `rules/` owns detailed API guidance.
- the target repository owns route shape, compatibility/version strategy, auth policy, public response contracts, query conventions, and validation commands.
- upstream HTTP/RFC/OpenAPI specifications own protocol semantics.
- this projection owns no independent API-design semantics.

## Safety and Compatibility Boundary

- Never use safe HTTP methods for state-changing operations.
- Never expose stack traces, SQL/runtime internals, credentials, secrets, or sensitive data in responses or logs.
- Do not silently break an existing public contract merely to match a generic REST preference.
- Treat RFC 9457 Problem Details and RFC 9745/RFC 8594 lifecycle headers according to their actual semantics, not as decorative response fields.
- Do not force `/v1/`, cursor pagination, a particular JSON envelope, or any other generic convention when the target API already owns a different documented contract.

## Projection Boundary

If this file disagrees with `SKILL.md`, `rules/`, or stronger repository/task instructions, follow the authoritative source and repair this projection. Do not copy current rule IDs, counts, or long examples back into this file.
