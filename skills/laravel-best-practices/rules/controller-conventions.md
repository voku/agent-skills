---
id: controller-conventions
title: "Thin Controllers, Resource Conventions, and Method Injection"
category: controller
priority: HIGH
triggers: [fat-controller, non-restful-controller-actions, missing-route-model-binding, controller-logic-bloat]
tags: [laravel, controllers, routing, rest, dependency-injection]
---

# Thin Controllers, Resource Conventions, and Method Injection

**Trigger Anchor:** Keep controllers thin and declarative by adhering to standard RESTful resource methods (`index`, `store`, `show`, `update`, `destroy`) or single-action invokables (`__invoke`), leveraging route model binding, and delegating all business logic to dedicated actions.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Bloated controller with arbitrary non-RESTful method names and manual model fetching
class OrderManagerController extends Controller
{
    public function doApproveOrder(Request $request)
    {
        $id = $request->input('order_id');
        $order = Order::find($id); // ❌ Missing route model binding / 404 handling
        if (!$order) abort(404);

        // ❌ Direct business logic inside controller
        $order->status = 'approved';
        $order->approved_at = now();
        $order->save();

        Mail::to($order->user)->send(new OrderApprovedMail($order));

        return redirect()->back();
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

namespace App\Http\Controllers\Orders;

use App\Domain\Orders\Actions\ApproveOrderAction;
use App\Domain\Orders\Models\Order;
use App\Http\Controllers\Controller;
use App\Http\Requests\Orders\ApproveOrderRequest;
use Illuminate\Http\RedirectResponse;

// ✅ Invokable single-action controller with route model binding and action delegation
final class ApproveOrderController extends Controller
{
    public function __invoke(
        ApproveOrderRequest $request,
        Order $order,
        ApproveOrderAction $approveOrder,
    ): RedirectResponse {
        $approveOrder($order, $request->user());

        return redirect()
            ->route('orders.show', $order)
            ->with('status', 'Order approved successfully.');
    }
}
```
