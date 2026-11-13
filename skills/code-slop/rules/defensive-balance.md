---
id: defensive-balance
title: Real Defenses vs Defensive Overdose
category: defensive
priority: HIGH
triggers: [generic-catch-swallowing, impossible-null-check, missing-timeout, missing-rate-limit]
tags: [defensive-programming, error-handling, resilience, observability]
---

# Real Defenses vs Defensive Overdose

**Trigger Anchor:** Stop swallowing errors in generic catch blocks or asserting impossible nulls on typed values; catch only specific recoverable exceptions, allow programming bugs to fail loudly, and enforce real boundary defenses (timeouts, rate limits).

---

### Bad

Avoid these observable failure patterns:

- **PHP:** checking a non-nullable typed `User` argument against `null` as a substitute for input-boundary validation; catching every exception from external I/O and returning `false` without communicating that a sync failed
- **PHP:** making outbound requests without an explicit timeout or bounded retry policy
- **TypeScript:** fetching orders without an abort timeout, then catching every network or JSON error and returning an empty order list that falsely looks like successful business data

These failures should be testable at the actual I/O boundary. The following examples show focused positive alternatives.

### Good
```php
<?php

declare(strict_types=1);

final readonly class UserSyncService
{
    public function sync(User $user): void
    {
        try {
            // ✅ Explicit network timeout, retry, and exception propagation
            Http::timeout(5)
                ->retry(2, 100)
                ->get("https://api.external.com/sync/{$user->id}")
                ->throw();

            $user->update(['synced_at' => now()]);
        } catch (ConnectionException $e) {
            Log::warning('External sync service temporarily unreachable', [
                'user_id' => $user->id,
                'exception' => $e->getMessage(),
            ]);
            throw new SyncGatewayException("Failed syncing user {$user->id}", previous: $e);
        }
    }
}
```

```typescript
// ✅ Explicit timeout via AbortSignal and transparent error propagation for caller/boundary
async function fetchOrders(userId: string): Promise<Order[]> {
  const res = await fetch(`/api/users/${encodeURIComponent(userId)}/orders`, {
    signal: AbortSignal.timeout(5000),
  });

  if (!res.ok) {
    throw new HttpError(`Failed to fetch orders: ${res.status} ${res.statusText}`);
  }

  return res.json();
}
```
