---
id: arch-transaction-side-effects
title: "Transaction Boundaries and Rollback Safety with External Side Effects"
category: transactions
priority: CRITICAL
triggers: [external-api-in-db-transaction, unrollbackable-side-effect, email-sent-before-commit, long-running-transaction]
tags: [architecture, transactions, rollback-safety, side-effects, outbox-pattern]
---

# Transaction Boundaries and Rollback Safety with External Side Effects

**Trigger Anchor:** Never perform irreversible external network calls (emails, payment gateways, webhook dispatches, directory modifications) inside local database transactions; dispatch side effects after successful commit or queue them via an outbox pattern.

---

### Bad
```php
// ❌ Irreversible external network calls executed inside a database transaction
$db->beginTransaction();
try {
    $order = $orderRepo->createOrder($cart);
    
    // External call cannot be rolled back if DB commit fails!
    $paymentClient->chargeCard($order->id, $cart->total);
    
    // If mail server hangs or fails, DB lock is held open and transaction aborts,
    // leaving customer charged with NO order persisted in the database!
    $mailer->sendReceiptEmail($order);
    
    $db->commit();
} catch (\Throwable $e) {
    $db->rollBack();
    throw $e;
}
```

### Good
```php
// ✅ Clean transaction boundary: only durable database writes inside transaction
$order = $db->transaction(function () use ($orderRepo, $cart) {
    $order = $orderRepo->createOrder($cart);
    // Queue outbox event inside same transaction for guaranteed delivery
    $orderRepo->recordOutboxEvent('order.created', ['order_id' => $order->id]);
    return $order;
});

// ✅ External side effects executed strictly after transaction commits successfully
try {
    $paymentClient->chargeCard($order->id, $cart->total);
    $eventDispatcher->dispatch(new OrderPaidEvent($order));
} catch (PaymentFailedException $e) {
    $orderService->markPaymentFailed($order->id, $e->getMessage());
    throw $e;
}
```
