---
id: query-filters-sorting
title: Filtering, Multi-Field Sorting, and Sparse Fieldsets
category: query
priority: HIGH
triggers: [unfiltered-search-scan, custom-sort-syntax, overfetching-payloads, inconsistent-filter-params]
tags: [filtering, sorting, sparse-fieldsets, query-parameters, optimization]
---

# Filtering, Multi-Field Sorting & Sparse Fieldsets

**Trigger Anchor:** Standardize filtering parameters, multi-field sorting via `-field` syntax, and sparse fieldsets (`fields=`) to avoid overfetching.

---

## Filter & Sorting Syntax

### Bad
```text
# ❌ Inconsistent query syntax requiring custom parser code
GET /products?sortBy=date&order=desc&filterByPrice=100to500&categoryFilter=electronics
```

### Good
```text
# ✅ Standard minus-prefix sorting and declarative attribute filters
GET /products?category=electronics&price_gte=100&price_lte=500&sort=-created_at,price
```

---

## Sparse Fieldsets (Avoid Overfetching)

### Bad
```json
// ❌ Client requested user name for a dropdown, received 5KB of nested profile data
GET /users?limit=50
// Returns full addresses, permissions, audit history, and bio for each user
```

### Good
```text
# ✅ Allow clients to request only the specific fields needed
GET /users?fields=id,name,avatar_url&limit=50
```

```json
{
  "data": [
    { "id": "u_1", "name": "Alice", "avatar_url": "https://cdn.example.com/u1.png" }
  ]
}
```
