---
id: error-problem-details
title: RFC 9457 Problem Details and Error Consistency
category: error
priority: CRITICAL
triggers: [custom-inconsistent-error-format, leaked-stack-trace, sql-error-in-response, missing-trace-id, string-only-error]
tags: [error-handling, rfc-9457, problem-details, status-codes, trace-id, validation-errors]
---

# RFC 9457 Problem Details & Error Consistency

**Trigger Anchor:** When an HTTP API needs a structured error representation, use RFC 9457 Problem Details (`application/problem+json`) instead of inventing an incompatible envelope. Keep the standard members semantically correct, use problem-type-specific extension members only when useful, and never expose internal stack traces or sensitive implementation details.

RFC 9457 obsoletes RFC 7807. Existing APIs using the older format remain recognizable, but new guidance and references should target RFC 9457.

---

### Bad
```text
HTTP/1.1 200 OK
Content-Type: application/json

{
  "success": false,
  "error": "QueryFailedError: syntax error at or near SELECT at /app/db.ts:42"
}
```

Problems:
- transport status contradicts the failure;
- the shape is application-specific without a stable problem type;
- internal database/runtime details are leaked.

### Good
```text
HTTP/1.1 422 Unprocessable Content
Content-Type: application/problem+json

{
  "type": "https://api.example.com/problems/validation-failed",
  "title": "Validation failed",
  "status": 422,
  "detail": "The request payload contains invalid values.",
  "instance": "/orders/checkout",
  "code": "VALIDATION_FAILED",
  "trace_id": "req_01HPX7K9Y1V5",
  "invalid_params": [
    { "name": "email", "reason": "Must be a valid email address" },
    { "name": "items[0].quantity", "reason": "Must be greater than 0" }
  ]
}
```

`code`, `trace_id`, and `invalid_params` in this example are application/problem-type extensions, not universal RFC 9457 members. Define and document extension semantics consistently for the API instead of implying that every Problem Details consumer understands them.
