---
id: ver-lifecycle
title: API Versioning and Deprecation Lifecycle
category: ver
priority: HIGH
triggers: [breaking-api-change, unversioned-breaking-update, silent-endpoint-removal, missing-sunset-header]
tags: [versioning, backward-compatibility, deprecation, sunset-header, migration]
---

# API Versioning & Deprecation Lifecycle

**Trigger Anchor:** Use explicit URL version prefixes (`/v1/`), maintain additive backward compatibility, and signal sunset schedules using standard `Deprecation` and `Sunset` HTTP headers.

---

## Additive Compatibility vs Breaking Changes

### Bad
```json
// ❌ Renaming fields or changing data types in an existing version breaks client apps
// v1 changed without version bump:
// Previous: "price": 19.99 (number)
// New:      "price_cents": 1999 (integer)
```

### Good
```json
// ✅ Keep fields backward-compatible; add new fields alongside existing ones
{
  "price": 19.99,
  "price_cents": 1999
}
// For incompatible breaking redesigns, increment version prefix: /v2/orders
```

---

## Deprecation & Sunset Headers

### Bad
```text
# ❌ Deleting an endpoint without warning or communicating deprecation in blog posts only
HTTP/1.1 404 Not Found
```

### Good
```text
# ✅ RFC 8594 Sunset and Deprecation headers warn automated clients ahead of removal
HTTP/1.1 200 OK
Deprecation: @1735689600
Sunset: Wed, 31 Dec 2026 23:59:59 GMT
Link: <https://api.example.com/v2/reports>; rel="successor-version"
```
