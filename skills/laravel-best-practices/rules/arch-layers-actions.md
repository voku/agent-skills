---
id: arch-layers-actions
title: "Actions, Services, DTOs, and Value Objects"
category: arch
priority: CRITICAL
triggers: [fat-controller-logic, untyped-array-payload, primitive-obsession, bloated-service-class]
tags: [laravel, actions, services, dto, value-objects, architecture]
---

# Actions, Services, DTOs, and Value Objects

**Trigger Anchor:** Extract complex business logic from controllers into invokable single-purpose Action classes or Services, transport structured request data via typed readonly DTOs, and encapsulate domain rules inside immutable Value Objects.

---

### Bad
```php
<?php

declare(strict_types=1);

namespace App\Http\Controllers;

use App\Models\Order;
use App\Models\User;
use Illuminate\Http\Request;
use Stripe\Charge;

// ❌ Fat controller with primitive obsession, inline third-party API calls, and untyped arrays
class OrderController extends Controller
{
    public function store(Request $request)
    {
        $userId = (int) $request->input('user_id');
        $rawAmount = (float) $request->input('amount'); // ❌ Primitive obsession for currency

        $charge = Charge::create([
            'amount' => $rawAmount * 100,
            'currency' => 'usd',
            'source' => $request->input('stripe_token'),
        ]);

        $order = Order::create([
            'user_id' => $userId,
            'amount' => $rawAmount,
            'stripe_charge_id' => $charge->id,
            'status' => 'paid',
        ]);

        return response()->json($order);
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

namespace App\Domain\Orders\Data;

use App\Domain\Shared\ValueObjects\Money;

// ✅ Immutable typed DTO
final readonly class CreateOrderData
{
    public function __construct(
        public int $userId,
        public Money $amount,
        public string $paymentToken,
    ) {}
}
```

```php
<?php

declare(strict_types=1);

namespace App\Domain\Orders\Actions;

use App\Domain\Orders\Data\CreateOrderData;
use App\Domain\Orders\Models\Order;
use App\Domain\Payments\Contracts\PaymentGateway;
use Illuminate\Support\Facades\DB;

// ✅ Invokable single-purpose action
final readonly class CreateOrderAction
{
    public function __construct(
        private PaymentGateway $gateway,
    ) {}

    public function __invoke(CreateOrderData $data): Order
    {
        return DB::transaction(function () use ($data): Order {
            $charge = $this->gateway->charge($data->amount, $data->paymentToken);

            return Order::create([
                'user_id' => $data->userId,
                'amount_cents' => $data->amount->cents,
                'payment_id' => $charge->id,
                'status' => OrderStatus::Paid,
            ]);
        });
    }
}
```
