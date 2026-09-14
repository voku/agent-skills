# Rule Sections

## Priority Levels

| Level | Description | When to Apply |
|-------|-------------|---------------|
| CRITICAL | Core exception hygiene, explicit signalling, and bounded execution | Every fallible path and external call |
| HIGH | Honest outcome messaging, safe retry backoff, and resource cleanup | Batch operations, network clients, and audit trails |

## Section Overview

### 1. Error Signalling (`signalling`)
- **Impact:** CRITICAL
- **Rules:** `err-signalling-hygiene`
- **Description:** Specific typed exceptions, cause chaining (`$previous`), and eliminating swallowed errors or ambiguous null returns.

### 2. Outcome Messaging (`messaging`)
- **Impact:** HIGH
- **Rules:** `err-outcome-batch-discipline`
- **Description:** Accurate outcome messaging per reachable branch, accumulated batch status flags, and eliminating silent else traps.

### 3. Timeouts & Cancellation (`resilience`)
- **Impact:** CRITICAL
- **Rules:** `err-timeouts-cancellation`
- **Description:** Explicit connect and transfer timeouts, bounded polling loops, and cancellation handling on external I/O.

### 4. Retries & Idempotency (`retries`)
- **Impact:** HIGH
- **Rules:** `err-retry-idempotency`
- **Description:** Restricting retries to transient failures with exponential backoff and jitter; enforcing idempotency keys on mutations.

### 5. Cleanup & Observability (`observability`)
- **Impact:** HIGH
- **Rules:** `err-cleanup-observability`
- **Description:** Deterministic `finally` resource release, logging handles instantiated outside loops, and external mutation audit ordering.
