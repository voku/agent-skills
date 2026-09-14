---
id: arch-events-queues
title: "Domain Events, Async Queues, and Centralized Routing"
category: arch
priority: HIGH
triggers: [synchronous-side-effect, missing-job-queue, blocking-http-request, unrouted-queue-jobs]
tags: [laravel, events, listeners, queues, async, background-jobs]
---

# Domain Events, Async Queues, and Centralized Routing

**Trigger Anchor:** Decouple domain side effects (emails, webhooks, search indexing) using domain events and queued listeners, configure explicit queue routing, and ensure all queue jobs are idempotent.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Blocking HTTP request executing 4 slow external side effects synchronously
class OrderCheckoutController extends Controller
{
    public function complete(Order $order): JsonResponse
    {
        $order->update(['status' => 'completed']);

        // ❌ Synchronous: HTTP request blocks 4-10 seconds
        Mail::to($order->user)->send(new OrderReceiptMail($order));
        PdfInvoiceService::generateAndStore($order);
        SalesforceSync::pushOrder($order);
        SlackNotifier::alert("#sales", "New order #{$order->id}");

        return response()->json(['status' => 'success']);
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

namespace App\Domain\Orders\Events;

use App\Domain\Orders\Models\Order;
use Illuminate\Foundation\Events\Dispatchable;

final readonly class OrderPlaced
{
    use Dispatchable;

    public function __construct(
        public Order $order,
    ) {}
}
```

```php
<?php

declare(strict_types=1);

namespace App\Domain\Orders\Listeners;

use App\Domain\Orders\Events\OrderPlaced;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Support\Facades\Mail;

// ✅ Queued listener runs asynchronously in background worker
final class SendOrderConfirmationEmail implements ShouldQueue
{
    use InteractsWithQueue;

    public string $queue = 'notifications';

    public function handle(OrderPlaced $event): void
    {
        Mail::to($event->order->user)->send(new OrderReceiptMail($event->order));
    }
}
```
