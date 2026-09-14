---
id: err-retry-idempotency
title: "Safe Retries, Exponential Backoff, and Idempotency"
category: retries
priority: HIGH
triggers: [unsafe-retry-loop, non-idempotent-mutation-retry, missing-backoff-jitter, retry-on-4xx-error, storm-thundering-herd]
tags: [error-handling, retries, idempotency, backoff, jitter, resilience]
---

# Safe Retries, Exponential Backoff, and Idempotency

**Trigger Anchor:** Restrict automatic retries to transient, idempotent failures (e.g. 503 Service Unavailable, network connection reset, lock timeout) with exponential backoff and random jitter; never blindly retry non-idempotent state mutations without idempotency keys.

---

### Bad
```php
// ❌ Retrying non-idempotent mutations creates duplicate charges/orders
for ($attempt = 1; $attempt <= 3; $attempt++) {
    try {
        $paymentGateway->chargeCustomer($customerId, $amount); // Can double-charge if network dropped response!
        break;
    } catch (\Throwable $e) {
        // Tight retry without backoff hammers failing service
    }
}

// ❌ Retrying client-side 4xx errors that cannot succeed on retry
try {
    $api->createResource($payload);
} catch (ClientException $e) {
    if ($e->getResponse()->getStatusCode() === 422) {
        $api->createResource($payload); // Retrying validation failure is futile
    }
}
```

### Good
```php
// ✅ Safe retry: idempotent operation, filtered error types, backoff with jitter
$idempotencyKey = Uuid::uuid4()->toString();
$maxAttempts = 3;

for ($attempt = 1; $attempt <= $maxAttempts; $attempt++) {
    try {
        return $paymentGateway->chargeCustomerWithKey(
            customerId: $customerId,
            amount: $amount,
            idempotencyKey: $idempotencyKey
        );
    } catch (TransientNetworkException|ServerException $e) {
        // Only retry transient failures (5xx, timeouts), never 4xx client errors
        if ($attempt === $maxAttempts) {
            throw $e;
        }
        // Exponential backoff: 200ms, 400ms, 800ms + random jitter up to 100ms
        $baseDelayMs = 100 * (2 ** $attempt);
        $jitterMs = random_int(0, 100);
        usleep(($baseDelayMs + $jitterMs) * 1000);
    }
}
```
