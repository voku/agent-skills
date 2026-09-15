# Sections

This file groups the canonical API design rules by concern. The individual non-underscore files in this directory own the detailed rule semantics.

## Resource Contracts (`rest`)

**Impact:** CRITICAL

Resource modeling, HTTP method/status semantics, and retry-safe/idempotent mutation behavior.

## Error Handling (`error`)

**Impact:** CRITICAL

RFC 9457 Problem Details, consistent machine-readable failure semantics, useful correlation data, and prevention of internal-detail leakage.

## Security (`sec`)

**Impact:** CRITICAL

Authentication, authorization, rate limiting, CORS/request boundaries, transport protection, and sensitive-data exposure prevention.

## Pagination and Querying (`query`)

**Impact:** HIGH

Cursor/offset tradeoffs, pagination metadata, filtering, sorting, and sparse-field conventions grounded in the target API's contract.

## Lifecycle Evolution (`ver`)

**Impact:** HIGH

Backward-compatible evolution, explicit breaking-version boundaries, RFC 9745 `Deprecation`, and RFC 8594 `Sunset` lifecycle signaling.

## Response Conventions (`resp`)

**Impact:** MEDIUM

Consistent JSON representation, naming, timestamps, and transport behavior.

## Documentation (`doc`)

**Impact:** MEDIUM

OpenAPI contracts, request/response coverage, and change documentation.
