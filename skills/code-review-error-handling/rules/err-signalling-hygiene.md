---
id: err-signalling-hygiene
title: "Exception Hygiene and Explicit Failure Signalling"
category: signalling
priority: CRITICAL
triggers: [swallowed-exception, empty-catch-block, missing-cause-chaining, silent-null-on-error, return-false-on-failure]
tags: [error-handling, exceptions, cause-chaining, failure-signalling, exception-hygiene]
---

# Exception Hygiene and Explicit Failure Signalling

**Trigger Anchor:** Throw specific typed exceptions with contextual detail instead of suppressing errors with empty catch blocks or returning ambiguous null/false; always preserve the original exception cause (`$previous`) when wrapping.

---

### Bad
```php
// ❌ Catching broad Throwable and swallowing without logging or re-throwing
try {
    $response = $httpClient->post('/api/v1/charge', $payload);
    return json_decode($response->getBody(), true);
} catch (\Throwable $e) {
    // Silent failure: caller cannot distinguish failure from empty result
    return null;
}

// ❌ Wrapping an exception but dropping the original stack trace and cause
try {
    $db->executeStatement($sql, $params);
} catch (\PDOException $e) {
    throw new DatabaseQueryException('Query execution failed'); // Lost $e!
}
```

### Good
```php
// ✅ Catch specific exception, log or wrap while preserving $previous cause
try {
    $response = $httpClient->post('/api/v1/charge', $payload);
    return json_decode($response->getBody()->getContents(), true, 512, JSON_THROW_ON_ERROR);
} catch (ClientExceptionInterface $e) {
    throw new PaymentGatewayException(
        message: sprintf('Payment gateway request failed for order %s: %s', $payload['order_id'], $e->getMessage()),
        previous: $e
    );
}

// ✅ Preserve original cause in custom domain exception
try {
    $db->executeStatement($sql, $params);
} catch (\PDOException $e) {
    throw new DatabaseQueryException(
        message: sprintf('Failed to execute query for tenant %s: %s', $tenantId, $e->getMessage()),
        previous: $e
    );
}
```
