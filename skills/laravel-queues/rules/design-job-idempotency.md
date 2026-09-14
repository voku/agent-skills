---
id: design-job-idempotency
title: "Job Design: ShouldQueue, Pure Constructors, and Idempotency"
category: design
priority: CRITICAL
triggers: [missing-should-queue, duplicate-side-effect, heavy-model-in-job-constructor, non-idempotent-job]
tags: [laravel, jobs, shouldqueue, idempotency, shouldbeunique, serialization]
---

# Job Design: ShouldQueue, Pure Constructors, and Idempotency

**Trigger Anchor:** Always implement `ShouldQueue`, keep constructors pure (pass IDs rather than stale models), and guarantee idempotency using atomic state checks or `ShouldBeUnique`.

---

### Bad
```php
<?php

// ❌ Missing ShouldQueue makes job execute synchronously; side effects repeat on retry
class ProcessPaymentJob
{
    // ❌ Heavy model passed; if status changes before worker runs, job has stale state
    public function __construct(public Order $order)
    {
        // ❌ Side effects in constructor run synchronously during dispatch!
        Log::info('Constructed payment job');
    }

    public function handle(): void
    {
        // ❌ Non-idempotent: If worker dies mid-way or retries, card is charged twice!
        PaymentGateway::charge($this->order->total);
        $this->order->update(['status' => 'paid']);
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

namespace App\Jobs;

use App\Models\Order;
use App\Services\PaymentGateway;
use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldBeUnique;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Bus\Dispatchable;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Queue\SerializesModels;

// ✅ Explicit ShouldQueue and ShouldBeUnique to prevent duplicate in-flight executions
final class ProcessPaymentJob implements ShouldQueue, ShouldBeUnique
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    // Pass IDs or scalar identifiers, not bloated state
    public function __construct(
        public int $orderId,
        public string $idempotencyKey,
    ) {}

    public function uniqueId(): string
    {
        return "payment:order:{$this->orderId}";
    }

    public function handle(PaymentGateway $gateway): void
    {
        $order = Order::findOrFail($this->orderId);

        // ✅ Atomic idempotency guard: skip if already settled
        if ($order->isPaid()) {
            return;
        }

        $charge = $gateway->chargeWithIdempotency(
            amount: $order->total_cents,
            idempotencyKey: $this->idempotencyKey,
        );

        $order->markAsPaid($charge->id);
    }
}
```
