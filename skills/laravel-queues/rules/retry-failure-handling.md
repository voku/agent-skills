---
id: retry-failure-handling
title: "Retries, Exponential Backoff, and Failure Lifecycle"
category: retry
priority: HIGH
triggers: [infinite-job-loop, unhandled-failed-job, hung-job-timeout, immediate-retry-burn]
tags: [laravel, jobs, retry, backoff, fail-on-timeout, failed-method]
---

# Retries, Exponential Backoff, and Failure Lifecycle

**Trigger Anchor:** Configure explicit `$tries` and exponential `$backoff`, use `#[FailOnTimeout]` to prevent hung jobs from exhausting attempts, implement `failed(Throwable $e)` for terminal recovery, and distinguish transient network retries from permanent data errors.

---

### Bad
```php
<?php

// ❌ Burns all 3 tries in 0.5 seconds on network glitch, lacks timeout and cleanup
class PushWebhookJob implements ShouldQueue
{
    // Default $tries = 1 or no backoff: immediately exhausts attempts during network hiccup
    public function handle(): void
    {
        // ❌ Unbounded HTTP call hangs indefinitely until worker timeout kills it
        Http::post('https://partner.api/webhook');
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

namespace App\Jobs;

use App\Exceptions\PermanentValidationException;
use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Bus\Dispatchable;
use Illuminate\Http\Client\ConnectionException;
use Illuminate\Queue\Attributes\FailOnTimeout;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Support\Facades\Http;
use Throwable;

#[FailOnTimeout] // Marks job failed immediately if timeout expires
final class PushWebhookJob implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable;

    public int $tries = 5;
    public int $timeout = 30;

    /**
     * ✅ Exponential backoff in seconds (1s, 5s, 30s, 120s)
     *
     * @return list<int>
     */
    public function backoff(): array
    {
        return [1, 5, 30, 120];
    }

    public function handle(): void
    {
        try {
            Http::timeout(10)->post('https://partner.api/webhook', ['status' => 'synced'])->throw();
        } catch (ConnectionException $e) {
            // Transient network error: release back to queue according to backoff
            $this->release();
        } catch (PermanentValidationException $e) {
            // Permanent data defect: do not waste retry budget, fail immediately
            $this->fail($e);
        }
    }

    /**
     * ✅ Clean up terminal failure state when all retries are exhausted
     */
    public function failed(?Throwable $exception): void
    {
        NotificationService::alertOpsTeam('Webhook permanently failed', [
            'error' => $exception?->getMessage(),
        ]);
    }
}
```
