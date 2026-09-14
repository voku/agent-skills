---
id: error-problem-details
title: RFC 7807 Problem Details and Error Consistency
category: error
priority: CRITICAL
triggers: [custom-inconsistent-error-format, leaked-stack-trace, sql-error-in-response, missing-trace-id, string-only-error]
tags: [error-handling, rfc-7807, problem-details, status-codes, trace-id, validation-errors]
---

# RFC 7807 Problem Details & Error Consistency

**Trigger Anchor:** Use RFC 7807 (`application/problem+json`) for all error responses; include machine-readable error codes, correlation trace IDs, field-level validation pointers, and never expose internal stack traces.

---

### Bad
```json
// ❌ Inconsistent, unparsed string with leaked database stack trace
HTTP/1.1 200 OK
{
  "success": false,
  "error": "QueryFailedError: syntax error at or near 'SELECT' at PostgresDriver.query (/app/db.ts:42)\n    at processTicksAndRejections"
}
```

### Good
```json
// ✅ Standard RFC 7807 Problem Details with trace ID and field pointers
HTTP/1.1 422 Unprocessable Entity
Content-Type: application/problem+json

{
  "type": "https://api.example.com/errors/validation-failed",
  "title": "Validation Failed",
  "status": 422,
  "detail": "The request payload failed 2 validation rules.",
  "instance": "/orders/checkout",
  "code": "VALIDATION_FAILED",
  "trace_id": "req_01HPX7K9Y1V5",
  "invalid_params": [
    { "name": "email", "reason": "Must be a valid RFC 5322 email address" },
    { "name": "items[0].quantity", "reason": "Must be an integer greater than 0" }
  ]
}
```
