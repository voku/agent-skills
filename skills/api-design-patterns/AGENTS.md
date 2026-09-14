# API Design Patterns - Agent Documentation

**Version:** 2.0.0  
**Focus:** RESTful APIs, Resource Design, Error Handling, Security, Pagination, Versioning  
**Rules:** 10 rules across 7 categories  
**License:** MIT  

---

This skill provides guidelines and patterns for designing consistent, secure, and developer-friendly REST APIs using standard HTTP semantics, RFC 7807 problem details, and OpenAPI contracts.

## Operational Contract

When applying this skill, agents must:
- Treat this skill as repo-owned guidance and defer to repository-specific API routing or framework conventions when they conflict.
- Limit changes to the smallest relevant route, controller, or schema definition.
- Never expose internal database stack traces or SQL errors in API responses.
- Respect idempotency: never use GET requests for state mutations.
- Prefer machine-readable evidence first (e.g. HTTP status codes, curl outputs, contract linting), then summarize changes.

## Validation & Evidence

- Run the repository's existing API contract validation or test suite (e.g. `npm test`, `spectral lint openapi.yaml`, `phpunit`).
- If no validation command exists, say so explicitly.

## When to Use This Skill

Activate this skill when:
- Designing or refactoring REST endpoints
- Implementing or standardizing error response structures
- Setting up query parameters for pagination, sorting, or filtering
- Implementing authentication, authorization, or rate limiting
- Planning non-breaking API evolution or deprecation headers
- Authoring or reviewing OpenAPI specifications

## Trigger Phrases

- "design API"
- "REST best practices"
- "API patterns"
- "review endpoints"
- "error response format"
- "pagination design"
- "API versioning"
- "rate limiting"

## Skill Structure

```
api-design-patterns/
├── SKILL.md              # Main skill definition & quick reference
├── AGENTS.md             # This file - agent guidance
├── README.md             # User-facing overview
├── metadata.json         # Structured metadata
└── rules/
    ├── _sections.md      # Category definitions
    ├── _template.md      # Rule template
    ├── rest-*.md         # Resource Design (2 rules: endpoints, idempotency)
    ├── error-*.md        # Error Handling (1 rule: problem-details)
    ├── sec-*.md          # Security (2 rules: auth-protection, data-exposure)
    ├── query-*.md        # Pagination & Querying (2 rules: pagination, filters-sorting)
    ├── ver-*.md          # Versioning (1 rule: lifecycle)
    ├── resp-*.md         # Response Format (1 rule: conventions)
    └── doc-*.md          # Documentation (1 rule: openapi)
```

## Rule Categories

### 1. Resource Design (`rest-`, CRITICAL)
- `rest-endpoints`: Plural nouns, shallow hierarchy (max 2 levels), standard HTTP method semantics (GET, POST, PUT, PATCH, DELETE), and canonical status codes (201 Created with Location header, 204 No Content).
- `rest-idempotency`: Safe methods, PUT full replacement vs PATCH delta updates, and `Idempotency-Key` headers on mutating POST endpoints.

### 2. Error Handling (`error-`, CRITICAL)
- `error-problem-details`: RFC 7807 Problem Details (`application/problem+json`) with machine-readable `code`, correlation `trace_id`, field validation errors in `invalid_params`, and zero leaked internal traces.

### 3. Security (`sec-`, CRITICAL)
- `sec-auth-protection`: Standard `Authorization: Bearer` headers, scoped RBAC permission checks, strict request validation, standard rate limiting (`429` with `Retry-After`), and explicit CORS allowlists.
- `sec-data-exposure`: HTTPS enforcement with HSTS (`Strict-Transport-Security`), zero credentials in query parameters or access logs, and filtering passwords, secret keys, and PII from responses.

### 4. Pagination & Querying (`query-`, HIGH)
- `query-pagination`: Cursor-based pagination for high-throughput or real-time collections, offset pagination for simple lists, and structured pagination metadata envelopes.
- `query-filters-sorting`: Standardized attribute filter parameters, multi-field sorting (`?sort=-created_at,priority`), and sparse fieldsets (`?fields=id,name`).

### 5. Versioning (`ver-`, HIGH)
- `ver-lifecycle`: Explicit `/v1/` URL version prefixes, additive backward-compatible evolution, and deprecation communication via `Sunset` and `Deprecation` HTTP headers.

### 6. Response Format (`resp-`, MEDIUM)
- `resp-conventions`: Consistent top-level JSON objects, uniform key casing (snake_case or camelCase), ISO 8601 UTC dates, and HTTP payload compression (gzip, brotli).

### 7. Documentation (`doc-`, MEDIUM)
- `doc-openapi`: Contract-first OpenAPI 3.1 specifications with complete request/response examples across all status codes, and semantic changelogs.

## Practical Application Examples

### Example 1: Endpoint Design Review

**User:** "Review this endpoint: `POST /api/getUserDetails?userId=123`"

**Agent Approach:**
1. Reference `rest-endpoints`.
2. Flag verb in URL (`getUserDetails`).
3. Flag POST method used for a safe read-only operation.
4. Flag ID passed in query parameter rather than URL path.
5. Propose canonical REST form: `GET /v1/users/123`.

### Example 2: Standardizing Error Responses

**User:** "Our API returns `{ error: 'failed' }` on bad requests."

**Agent Approach:**
1. Reference `error-problem-details`.
2. Convert to RFC 7807 structure with `type`, `title`, `status`, `detail`, `code`, `trace_id`, and `invalid_params`.
3. Ensure status is `400 Bad Request` or `422 Unprocessable Entity` with `Content-Type: application/problem+json`.
