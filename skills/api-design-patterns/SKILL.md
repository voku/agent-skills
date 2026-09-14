---
name: api-design-patterns
description: RESTful API design, error handling, versioning, and best practices. Use when designing APIs, reviewing endpoints, implementing error responses, or setting up API structure. Triggers on "design API", "review API", "REST best practices", or "API patterns".
license: MIT
metadata:
  author: agent-skills
  version: "2.0.0"
---

# API Design Patterns

RESTful API design principles for building consistent, developer-friendly APIs. Contains 10 rules across 7 categories covering resource design, error handling, security, pagination, versioning, response format, and documentation.

## Metadata

- **Version:** 2.0.0
- **Rule Count:** 10 rules across 7 categories
- **License:** MIT

## When to Apply

Reference these guidelines when:
- Designing new API endpoints and resources
- Reviewing existing API structure and method semantics
- Implementing error handling with RFC 7807 Problem Details
- Setting up pagination, filtering, and sorting query parameters
- Planning API versioning and deprecation schedules
- Configuring API security (Bearer auth, CORS, rate limiting, data masking)
- Writing OpenAPI/Swagger contracts and changelogs

## Rule Categories by Priority

| Priority | Category | Impact | Prefix | Rules |
|----------|----------|--------|--------|-------|
| 1 | Resource Design | CRITICAL | `rest-` | 2 |
| 2 | Error Handling | CRITICAL | `error-` | 1 |
| 3 | Security | CRITICAL | `sec-` | 2 |
| 4 | Pagination & Querying | HIGH | `query-` | 2 |
| 5 | Versioning | HIGH | `ver-` | 1 |
| 6 | Response Format | MEDIUM | `resp-` | 1 |
| 7 | Documentation | MEDIUM | `doc-` | 1 |

## Quick Reference

### 1. Resource Design (`rest-`, CRITICAL)
- `rest-endpoints` - Plural noun modeling, shallow hierarchy (max 2 levels), canonical HTTP methods, and status codes
- `rest-idempotency` - Safe methods, PUT vs PATCH semantics, and `Idempotency-Key` headers on mutating operations

### 2. Error Handling (`error-`, CRITICAL)
- `error-problem-details` - RFC 7807 Problem Details (`application/problem+json`) with machine-readable codes, trace IDs, and zero leaked stack traces

### 3. Security (`sec-`, CRITICAL)
- `sec-auth-protection` - Bearer tokens, scoped RBAC authorization, rate limiting (`429` with `Retry-After`), and strict CORS allowlists
- `sec-data-exposure` - HTTPS enforcement with HSTS, and scrubbing sensitive credentials (passwords, payment cards, PII) from payloads and logs

### 4. Pagination & Querying (`query-`, HIGH)
- `query-pagination` - Cursor-based vs offset pagination with structured pagination metadata envelopes
- `query-filters-sorting` - Standardized attribute filtering, multi-field sorting (`-field`), and sparse fieldsets (`fields=`)

### 5. Versioning (`ver-`, HIGH)
- `ver-lifecycle` - Explicit `/v1/` URL versioning, additive backward compatibility, and RFC 8594 `Sunset` and `Deprecation` headers

### 6. Response Format (`resp-`, MEDIUM)
- `resp-conventions` - Consistent top-level JSON objects, uniform key casing, ISO 8601 UTC dates, and brotli/gzip compression

### 7. Documentation (`doc-`, MEDIUM)
- `doc-openapi` - Contract-first OpenAPI 3.1 specifications with complete request/response examples across all status codes, and semantic changelogs

## Essential Guidelines

### Resource Naming & Methods

```
# ✅ Nouns with HTTP methods
GET    /users          # List users
POST   /users          # Create user
GET    /users/123      # Get user
PUT    /users/123      # Replace user (full)
PATCH  /users/123      # Update user (partial delta)
DELETE /users/123      # Delete user
```

### RFC 7807 Error Response Format

```json
{
  "type": "https://api.example.com/errors/validation-failed",
  "title": "Validation Failed",
  "status": 422,
  "detail": "The email provided is invalid.",
  "code": "VALIDATION_FAILED",
  "trace_id": "req_abc123",
  "invalid_params": [
    { "name": "email", "reason": "Must be a valid email address" }
  ]
}
```

### Pagination Envelope

```json
{
  "data": [...],
  "pagination": {
    "limit": 25,
    "has_more": true,
    "next_cursor": "eyJpZCI6MTAwfQ==",
    "total_count": 195
  }
}
```

## References

- [RESTful API Guidelines](https://restfulapi.net)
- [Zalando RESTful API Guidelines](https://zalando.github.io/restful-api-guidelines)
- [Microsoft API Guidelines](https://github.com/microsoft/api-guidelines)
- [Google API Design Guide](https://cloud.google.com/apis/design)
- [OpenAPI Specification](https://swagger.io/specification)
- [RFC 7807: Problem Details](https://datatracker.ietf.org/doc/html/rfc7807)

## Full Compiled Document

For the complete guide with all rules expanded: `AGENTS.md`
