---
id: query-pagination
title: Cursor and Offset Collection Pagination
category: query
priority: HIGH
triggers: [unbounded-collection-query, offset-drift-duplicates, inconsistent-page-params, missing-pagination-meta]
tags: [pagination, cursor-pagination, offset-pagination, collections, query-parameters]
---

# Cursor & Offset Collection Pagination

**Trigger Anchor:** Use cursor-based pagination for high-volume or real-time collections; provide standard parameter names (`limit`, `cursor`/`page`) and structured pagination envelopes.

---

## Cursor vs Offset

### Bad
```text
# ❌ Unbounded query or high-offset performance degradation
GET /api/transactions                 # Returns 500,000 rows, crashes server
GET /api/transactions?offset=1000000  # Full table scan in SQL, shifts on concurrent inserts
```

### Good
```text
# ✅ Opaque cursor pagination with safe limit constraints
GET /api/transactions?limit=25&cursor=eyJpZCI6ImtxXzEyMyJ9
```

---

## Consistent Pagination Envelope

### Bad
```json
// ❌ Bare array with no continuation token or pagination metadata
[ { "id": "tx_1" }, { "id": "tx_2" } ]
```

### Good
```json
// ✅ Standard collection wrapper with cursor and navigation flags
{
  "data": [
    { "id": "tx_1", "amount": 100 },
    { "id": "tx_2", "amount": 250 }
  ],
  "pagination": {
    "limit": 25,
    "has_more": true,
    "next_cursor": "eyJpZCI6InR4XzIifQ==",
    "total_count": 1420
  }
}
```
