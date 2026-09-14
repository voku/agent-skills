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
```php
<?php

declare(strict_types=1);

// ❌ Swallows all exceptions, masks failures with false, and misses external timeouts
class UserSyncService
{
    public function sync(User $user): bool
    {
        // ❌ Impossible null check on non-nullable typed parameter
        if ($user === null || $user->id === null) {
            return false;
        }

        try {
            // ❌ No timeout or retry policy configured
            $response = Http::get('https://api.external.com/sync/' . $user->id);
            $user->update(['synced_at' => now()]);
            return true;
        } catch (\Exception $e) { // ❌ Catches TypeError, OutOfMemory, DatabaseException indiscriminately
            Log::error('Sync error: ' . $e->getMessage());
            return false; // Caller falsely assumes silent no-op
        }
    }
}
```

```typescript
// ❌ Defensive overdose: triple null checks and generic catch returning empty array
async function fetchOrders(userId: string): Promise<Order[]> {
  try {
    if (!userId || typeof userId !== 'string' || userId === null) {
      return [];
    }
    const res = await fetch(`/api/users/${userId}/orders`); // No AbortController timeout
    return await res.json();
  } catch (err) {
    console.error('Error fetching orders:', err);
    return []; // UI shows empty state instead of error boundary
  }
}
```

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
