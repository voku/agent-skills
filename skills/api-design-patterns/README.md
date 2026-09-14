# API Design Patterns v2.0.0

RESTful API design principles for building consistent, developer-friendly APIs.

## Overview

- **Resource design:** Plural nouns, canonical HTTP methods, status codes, idempotent mutations
- **Error handling:** RFC 7807 Problem Details (`application/problem+json`) with trace IDs
- **Security:** Bearer token authentication, scoped RBAC, rate limiting (`429`), HTTPS with HSTS, data masking
- **Pagination & querying:** Cursor and offset pagination, structured metadata, multi-field sorting (`-field`), sparse fieldsets
- **Versioning:** Explicit `/v1/` URL versioning, additive backward compatibility, `Sunset` and `Deprecation` headers
- **Response format:** Consistent top-level JSON objects, uniform casing, ISO 8601 UTC dates, brotli/gzip compression
- **Documentation:** Contract-first OpenAPI 3.1 specifications with complete request/response examples, changelog
- **Total Rules:** 10 rules across 7 categories

## Categories

### 1. Resource Design (Critical)
Plural noun modeling, shallow hierarchy (max 2 levels), standard HTTP method semantics, status codes, and idempotency keys.

### 2. Error Handling (Critical)
RFC 7807 Problem Details with machine-readable error codes, correlation trace IDs, field validation details, and zero leaked stack traces.

### 3. Security (Critical)
Bearer token authentication, RBAC authorization, rate limiting (`429` with `Retry-After`), explicit CORS allowlists, HTTPS with HSTS, and sensitive data masking.

### 4. Pagination & Querying (High)
Cursor and offset pagination, standardized attribute filtering, multi-field sorting, and sparse fieldsets.

### 5. Versioning (High)
Additive non-breaking evolution, explicit URL version prefixes, and deprecation communication with `Sunset` and `Deprecation` headers.

### 6. Response Format (Medium)
Consistent top-level JSON objects, uniform key casing, ISO 8601 UTC dates, and HTTP payload compression.

### 7. Documentation (Medium)
Contract-first OpenAPI 3.1 specifications with complete examples across all status codes, and semantic changelogs.

## Usage

```
Review my API design
Check REST best practices for these endpoints
Design error responses for my API
Set up pagination for this endpoint
```

## References

- [RESTful API Guidelines](https://restfulapi.net)
- [Zalando RESTful API Guidelines](https://zalando.github.io/restful-api-guidelines)
- [Microsoft API Guidelines](https://github.com/microsoft/api-guidelines)
- [OpenAPI Specification](https://swagger.io/specification)
- [RFC 7807: Problem Details](https://datatracker.ietf.org/doc/html/rfc7807)
