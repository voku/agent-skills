---
id: ver-lifecycle
title: API Versioning and Deprecation Lifecycle
category: ver
priority: HIGH
triggers: [breaking-api-change, unversioned-breaking-update, silent-endpoint-removal, missing-sunset-header]
tags: [versioning, backward-compatibility, deprecation, rfc-9745, rfc-8594, sunset-header, migration]
---

# API Versioning & Deprecation Lifecycle

**Trigger Anchor:** Evolve an existing API compatibly where practical, isolate intentional breaking contracts behind an explicit version boundary when the repository's API strategy requires one, and communicate lifecycle changes using the standardized `Deprecation` and `Sunset` response headers when they fit the resource lifecycle.

- RFC 9745 defines `Deprecation`, which communicates when a resource will be or has been deprecated.
- RFC 8594 defines `Sunset`, which communicates when a resource is expected to become unresponsive.
- When both are present, the `Sunset` timestamp must not be earlier than the `Deprecation` timestamp.

Do not treat URL prefixes such as `/v1/` as the only valid API versioning model; preserve the target API's established and documented versioning contract unless the task is explicitly redesigning it.

---

## Additive Compatibility vs Breaking Changes

### Bad
```text
# Existing v1 contract changed in-place:
# Previous: "price": 19.99
# New:      "price_cents": 1999
```

### Better
```json
{
  "price": 19.99,
  "price_cents": 1999
}
```

Keep compatible fields during the supported migration window. For a genuinely incompatible redesign, use the API's established version boundary rather than silently changing the existing contract.

---

## Deprecation & Sunset Headers

### Bad
```text
# Endpoint disappears with no machine-readable lifecycle signal.
HTTP/1.1 404 Not Found
```

### Good
```text
HTTP/1.1 200 OK
Deprecation: @1735689599
Sunset: Wed, 31 Dec 2026 23:59:59 GMT
Link: <https://api.example.com/v2/reports>; rel="successor-version"
```

`Deprecation` and `Sunset` communicate different lifecycle facts. A deprecated resource may remain operational for a substantial period; use `Sunset` only when an expected unavailability time is actually known and appropriate to publish.
