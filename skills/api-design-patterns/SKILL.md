---
name: api-design-patterns
description: Portable HTTP API design guidance for resource contracts, error handling, security, querying, lifecycle evolution, response conventions, and OpenAPI documentation. Use when designing or reviewing HTTP APIs; preserve the target repository's established API contract unless the task explicitly changes it.
license: MIT
metadata:
  author: agent-skills
  version: "2.1.0"
---

# API Design Patterns

Portable guidance for designing and evolving consistent, secure HTTP APIs without replacing target-repository contracts with generic REST folklore.

## Grounding and Scope

Before applying a rule, inspect the target API's existing routes, HTTP semantics, compatibility policy, authentication and authorization model, error format, pagination/query conventions, OpenAPI contract, and validation tooling.

Preserve an established public contract unless the task explicitly requires a migration. Prefer standards where they improve interoperability, but do not force a generic URL shape, envelope, pagination style, or versioning strategy onto a repository that already owns those decisions.

## Canonical Rule Boundaries

### Resource Contracts
- [rest-endpoints.md](rules/rest-endpoints.md) - resource naming, hierarchy, HTTP methods, and status semantics.
- [rest-idempotency.md](rules/rest-idempotency.md) - safe/idempotent operations and retry-safe mutation design.

### Error Handling
- [error-problem-details.md](rules/error-problem-details.md) - RFC 9457 Problem Details, consistent machine-readable errors, and no internal-detail leakage.

### Security
- [sec-auth-protection.md](rules/sec-auth-protection.md) - authentication, authorization, rate limiting, request validation, and CORS boundaries.
- [sec-data-exposure.md](rules/sec-data-exposure.md) - transport protection and prevention of credential, secret, and sensitive-data exposure.

### Querying and Collections
- [query-pagination.md](rules/query-pagination.md) - cursor/offset tradeoffs and pagination metadata.
- [query-filters-sorting.md](rules/query-filters-sorting.md) - filtering, sorting, and sparse-field conventions.

### Lifecycle Evolution
- [ver-lifecycle.md](rules/ver-lifecycle.md) - backward-compatible evolution, explicit breaking-version boundaries, RFC 9745 `Deprecation`, and RFC 8594 `Sunset`.

### Response Conventions
- [resp-conventions.md](rules/resp-conventions.md) - consistent JSON shape, naming, timestamps, and transport conventions.

### Documentation
- [doc-openapi.md](rules/doc-openapi.md) - OpenAPI contracts, request/response coverage, and change documentation.

## Standards Boundary

- RFC 9457 is the current Problem Details specification and obsoletes RFC 7807.
- RFC 9745 defines the `Deprecation` response header.
- RFC 8594 defines the `Sunset` response header.
- Standard fields and headers do not remove the need to document application-specific extension members and lifecycle semantics.

## Decision Discipline

- Treat these rules as defaults and interoperability guidance, not automatic redesign mandates.
- Never use a safe HTTP method for a state-changing operation.
- Do not leak stack traces, SQL errors, credentials, secrets, or sensitive internal identifiers into responses or logs.
- Preserve compatibility unless a breaking change is explicit and has an owned migration/version boundary.
- Match pagination, filtering, response, and versioning choices to the target API's actual scale and client contract.
- Prefer the repository's existing OpenAPI/contract tests, HTTP integration tests, linters, and runtime evidence over invented validation commands.

## Projection Boundary

`README.md`, `AGENTS.md`, and `metadata.json` are supporting projections. If they disagree with this file or `rules/`, follow the canonical source and repair the projection. Do not copy a second current rule inventory or compiled examples into supporting projections.
