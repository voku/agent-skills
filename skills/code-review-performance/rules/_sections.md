# Rule Sections

## Priority Levels

| Level | Description | When to Apply |
|-------|-------------|---------------|
| CRITICAL | Database query shape and algorithmic complexity | Queries, loops, and collection processing |
| HIGH | Memory streaming, caching invalidation, and network batching | Large exports, cached services, and remote API calls |

## Section Overview

### 1. Database Performance (`database`)
- **Impact:** CRITICAL
- **Rules:** `perf-database-nplusone`
- **Description:** Eliminating N+1 queries with eager loading and bulk `IN (...)` queries; index alignment; precise count queries.

### 2. Algorithmic Complexity (`algorithms`)
- **Impact:** CRITICAL
- **Rules:** `perf-algorithmic-collections`
- **Description:** Replacing O(N^2) nested scans with O(1) hash maps and key-indexed lookup sets; avoiding linear in-array scans.

### 3. Memory Management (`memory`)
- **Impact:** HIGH
- **Rules:** `perf-memory-streaming`
- **Description:** Streaming large datasets with generators (`yield`); chunked processing to keep memory constant.

### 4. Caching & Stampede (`caching`)
- **Impact:** HIGH
- **Rules:** `perf-caching-invalidation`
- **Description:** Explicit TTLs, versioned cache keys with entity timestamps, and atomic lock stampede protection.

### 5. Network I/O & Batching (`network-io`)
- **Impact:** HIGH
- **Rules:** `perf-network-batching`
- **Description:** Batching chatty remote calls; targeted column selection over `SELECT *` payload bloat.
