---
id: code-smells
title: "Code Debt: Complexity, Duplication, and Bloat"
category: code
priority: CRITICAL
triggers: [cyclomatic-complexity, long-function, god-class, duplicate-code, dead-code, magic-numbers, long-parameter-list]
tags: [refactoring, complexity, clean-code, maintainability]
---

# Code Debt: Complexity, Duplication, and Bloat

**Trigger Anchor:** Break down god classes (>300 lines or >15 public methods), split high-cyclomatic functions (>10), eliminate duplicate blocks (>30 lines), remove dead code, group wide parameter lists into DTOs/value objects, and replace magic literals with typed constants.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ God class: high cyclomatic complexity, magic numbers, 7 parameters, duplicate DB logic
class OrderProcessor
{
    public function process(
        int $userId,
        float $subtotal,
        float $tax,
        float $shipping,
        string $coupon,
        bool $isVip,
        string $paymentMethod
    ): array {
        // Deeply nested cyclomatic complexity with magic literals
        if ($subtotal > 1000) {
            if ($isVip) {
                $discount = $subtotal * 0.15; // ❌ Magic number
            } else {
                if ($coupon === 'SUMMER20') {
                    $discount = $subtotal * 0.20; // ❌ Magic number
                } else {
                    $discount = 0.0;
                }
            }
        } else {
            $discount = 0.0;
        }

        // Duplicate calculation pattern repeated across controllers
        $total = ($subtotal - $discount) + $tax + $shipping;

        // Unused dead code left behind
        // $debugLog = "Processed for " . $userId;

        return ['total' => $total, 'status' => 1]; // ❌ Magic status code
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

// ✅ Focused Value Objects and typed Command DTOs eliminate wide parameter lists
final readonly class CheckoutContext
{
    public function __construct(
        public UserId $userId,
        public Money $subtotal,
        public TaxRate $taxRate,
        public ShippingCost $shipping,
        public ?Coupon $coupon = null,
        public bool $isVip = false,
    ) {}
}

final readonly class OrderPricer
{
    private const float VIP_DISCOUNT_RATE = 0.15;

    public function calculateTotal(CheckoutContext $ctx): Money
    {
        $discount = $this->determineDiscount($ctx);
        $tax = $ctx->subtotal->multiply($ctx->taxRate->percentage);

        return $ctx->subtotal
            ->subtract($discount)
            ->add($tax)
            ->add($ctx->shipping->amount);
    }

    private function determineDiscount(CheckoutContext $ctx): Money
    {
        if ($ctx->isVip && $ctx->subtotal->isGreaterThan(Money::usd(1000_00))) {
            return $ctx->subtotal->multiply(self::VIP_DISCOUNT_RATE);
        }

        return $ctx->coupon?->calculateDiscount($ctx->subtotal) ?? Money::zero();
    }
}
```
