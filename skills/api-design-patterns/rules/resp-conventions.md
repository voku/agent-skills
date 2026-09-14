---
id: resp-conventions
title: Response Envelopes, JSON Conventions, and Compression
category: resp
priority: MEDIUM
triggers: [top-level-json-array, mixed-casing-conventions, non-standard-date-format, missing-http-compression]
tags: [response-format, json, casing, date-format, compression, envelopes]
---

# Response Envelopes, JSON Conventions & Compression

**Trigger Anchor:** Always return top-level JSON objects with consistent key casing and ISO 8601 UTC dates; enable gzip/brotli compression for payloads exceeding 1KB.

---

## Top-Level Envelopes & Date Conventions

### Bad
```json
// ❌ Top-level JSON array, mixed casing, and ambiguous local timestamp format
[
  {
    "user_id": 123,
    "userFirstName": "Alice",
    "updatedAt": "09/14/2026 09:30 AM"
  }
]
```

### Good
```json
// ✅ Top-level object, consistent snake_case (or camelCase), and ISO 8601 UTC timestamp
{
  "data": {
    "user_id": "usr_123",
    "first_name": "Alice",
    "updated_at": "2026-09-14T09:30:00Z"
  }
}
```

---

## Response Compression

### Bad
```text
# ❌ Serving uncompressed 5MB JSON payloads over high-latency mobile networks
HTTP/1.1 200 OK
Content-Length: 5242880
```

### Good
```text
# ✅ Brotli / Gzip compression negotiated via Accept-Encoding
HTTP/1.1 200 OK
Content-Encoding: br
Content-Type: application/json; charset=utf-8
```
