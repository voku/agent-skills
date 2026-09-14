# Sections

This file defines all sections, their ordering, impact levels, and descriptions.
The section ID (in parentheses) is the filename prefix used to group rules.

---

## 1. Resource Design (rest)

**Impact:** CRITICAL  
**Description:** Foundational REST principles: resource modeling with plural nouns, shallow hierarchy, standard HTTP method and status semantics, and idempotent mutations with Idempotency-Key protection.

## 2. Error Handling (error)

**Impact:** CRITICAL  
**Description:** Standardized error responses using RFC 7807 Problem Details (`application/problem+json`) with machine-readable error codes, correlation trace IDs, field validation pointers, and zero exposed stack traces.

## 3. Security (sec)

**Impact:** CRITICAL  
**Description:** Core API security controls: Bearer token authentication, scoped authorization (RBAC), standard rate limiting (`429` with `Retry-After`), explicit CORS allowlists, HTTPS enforcement with HSTS, and sensitive data masking.

## 4. Pagination & Querying (query)

**Impact:** HIGH  
**Description:** Efficient collection retrieval: cursor-based and offset pagination with structured metadata, standard filtering, multi-field sorting (`-field`), and sparse fieldsets.

## 5. Versioning (ver)

**Impact:** HIGH  
**Description:** Additive, backward-compatible API evolution with explicit URL version prefixes (`/v1/`) and deprecation lifecycle signaling via `Sunset` and `Deprecation` headers.

## 6. Response Format (resp)

**Impact:** MEDIUM  
**Description:** Consistent top-level JSON objects, uniform key casing, ISO 8601 UTC dates, and HTTP payload compression (gzip, brotli).

## 7. Documentation (doc)

**Impact:** MEDIUM  
**Description:** Contract-first OpenAPI 3.1 specifications with complete request/response examples across all status codes, and semantic changelogs.
