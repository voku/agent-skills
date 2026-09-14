---
id: ops-testing-monitoring
title: "Queue Operations: Testing, Scheduling, and Horizon Monitoring"
category: ops
priority: MEDIUM
triggers: [un-tested-queue-dispatch, overlapping-scheduled-job, horizon-monitoring-gap]
tags: [laravel, queue, testing, horizon, schedule, withoutOverlapping]
---

# Queue Operations: Testing, Scheduling, and Horizon Monitoring

**Trigger Anchor:** Fake queues in tests (`Queue::fake()`, `Bus::fake()`), prevent overlapping scheduled jobs with `withoutOverlapping()`, and monitor throughput and queue wait times with Laravel Horizon.

---

### Bad
```php
<?php

// ❌ Running live jobs during tests or letting scheduled tasks overlap and exhaust workers
// routes/console.php
Schedule::job(new HeavyHourlyAggregationJob)->hourly(); // Can stack if run > 60 minutes!
```

### Good
```php
<?php

declare(strict_types=1);

// ✅ Scheduled job with overlap prevention and background dispatch
use App\Jobs\HeavyHourlyAggregationJob;
use Illuminate\Support\Facades\Schedule;

Schedule::job(new HeavyHourlyAggregationJob)
    ->hourly()
    ->withoutOverlapping(expiresAt: 120) // Prevents job pileups
    ->onOneServer(); // Ensures single execution across multi-server clusters
```

```php
<?php

declare(strict_types=1);

use App\Jobs\SendWelcomeEmail;
use Illuminate\Support\Facades\Queue;

// ✅ Testing job dispatch without executing worker side-effects
test('dispatches welcome email on registration', function () {
    Queue::fake([SendWelcomeEmail::class]);

    $this->postJson('/api/register', [
        'email' => 'alice@example.com',
        'password' => 'Password123!',
    ])->assertCreated();

    Queue::assertPushed(SendWelcomeEmail::class, function ($job) {
        return $job->email === 'alice@example.com';
    });
});
```
