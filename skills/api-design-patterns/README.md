# API Design Patterns

Portable HTTP API design guidance for resource contracts, error handling, security, querying, lifecycle evolution, response conventions, and OpenAPI documentation.

## Canonical Source

`SKILL.md` defines activation, standards boundaries, decision discipline, and rule routing. The non-underscore files under `rules/` contain the canonical detailed guidance. This README is a routing projection only; it must not own a second rule inventory, count, standards matrix, or compiled example set.

## When to Use

Use this skill when designing or reviewing HTTP APIs, error responses, authentication/authorization boundaries, pagination/query semantics, compatibility/deprecation behavior, response conventions, or OpenAPI contracts.

## Routing

1. Inspect the target repository's existing API contract and compatibility policy.
2. Read `SKILL.md` first.
3. Load only the canonical rule files relevant to the task.
4. Preserve established public behavior unless the task explicitly changes it.
5. Verify using repository-owned contract tests, HTTP integration tests, linters, and runtime evidence.

## Standards Notes

- Problem Details: RFC 9457.
- `Deprecation` header: RFC 9745.
- `Sunset` header: RFC 8594.

## Projection Boundary

If this file disagrees with `SKILL.md` or `rules/`, follow the canonical source and repair this projection. Do not copy current rule IDs, counts, protocol recipes, or long examples back into this file.
