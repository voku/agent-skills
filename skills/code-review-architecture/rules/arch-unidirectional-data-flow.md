---
id: arch-unidirectional-data-flow
title: "Unidirectional Data Flow and Explicit State Ownership"
category: data-flow
priority: HIGH
triggers: [global-mutable-state, action-at-a-distance, ambient-context-dependency, hidden-state-mutation]
tags: [architecture, data-flow, immutability, state-ownership, single-source-of-truth]
---

# Unidirectional Data Flow and Explicit State Ownership

**Trigger Anchor:** Pass state explicitly as immutable data transfer objects (DTOs) or method parameters; eliminate ambient global state modifications and action-at-a-distance.

---

### Bad
```php
// ❌ Relying on ambient global state or mutable singleton registries
class PricingCalculator
{
    public function calculateTotal(Cart $cart): float
    {
        // Ambient global state modified by previous middleware or request
        $currency = $GLOBALS['current_currency'];
        $discountCode = SessionRegistry::get('active_discount');

        // Mutates cart object by reference during calculation
        $cart->taxRate = 0.20;
        return $cart->subtotal * 1.20;
    }
}
```

### Good
```php
// ✅ Explicit, immutable parameter inputs and deterministic return values
class PricingCalculator
{
    public function calculateTotal(CartDTO $cart, PricingContext $context): PriceBreakdown
    {
        $tax = $this->taxService->calculate($cart->subtotal, $context->taxRate);
        $discount = $context->discount?->calculateDiscount($cart->subtotal) ?? 0.0;

        return new PriceBreakdown(
            subtotal: $cart->subtotal,
            tax: $tax,
            discount: $discount,
            total: max(0.0, ($cart->subtotal - $discount) + $tax),
            currency: $context->currency,
        );
    }
}
```
