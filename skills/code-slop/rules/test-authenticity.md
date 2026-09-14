---
id: test-authenticity
title: Genuine Behavioral Testing vs Test Slop
category: test
priority: HIGH
triggers: [mock-everything, doesnt-throw-smoke-test, mirror-implementation-test, snapshot-abuse]
tags: [testing, assertions, mocks, quality-assurance]
---

# Genuine Behavioral Testing vs Test Slop

**Trigger Anchor:** Test observable behavior, boundary conditions, and state changes instead of mocking every collaborator; eliminate "does-not-throw" smoke tests, mirror implementations, and uninspected blob snapshots.

---

### Bad
```typescript
// ❌ 100% mocked tautology: tests the mock wiring, not the business behavior
it('calculates discount correctly', () => {
  const mockTierRepo = { getTier: jest.fn().mockReturnValue('gold') };
  const mockLogger = { info: jest.fn() };
  const service = new PricingService(mockTierRepo, mockLogger);

  const total = service.calculateDiscount(100);

  // ❌ Re-encodes implementation formula and asserts mock calls rather than outcome rules
  expect(mockTierRepo.getTier).toHaveBeenCalledTimes(1);
  expect(mockLogger.info).toHaveBeenCalledWith('Applied 20%');
  expect(total).toBe(100 - (100 * 0.2));
});

// ❌ "Doesn't throw" smoke test that verifies nothing about correctness
it('handles user event', async () => {
  const handler = new OrderEventHandler();
  await expect(handler.handle({ type: 'order.placed' })).resolves.not.toThrow();
});
```

```php
<?php

declare(strict_types=1);

// ❌ Mocking PHP stdlib / internal functions or mirroring simple math
it('applies coupon', function () {
    $repo = Mockery::mock(CouponRepository::class);
    $repo->shouldReceive('find')->andReturn(new Coupon(discountPercent: 15));

    $service = new CheckoutService($repo);
    $finalPrice = $service->apply('SAVE15', 200.0);

    // Mirrors code exactly: 200 * (1 - 0.15)
    expect($finalPrice)->toBe(200.0 - (200.0 * 0.15));
});
```

### Good
```typescript
// ✅ Asserts concrete domain contracts, invariants, and edge cases
describe('PricingService', () => {
  it('applies 20% discount for gold customers', () => {
    const service = new PricingService();
    const result = service.applyDiscount(Money.usd(100), CustomerTier.Gold);

    expect(result.amount).toBe(80);
  });

  it('rejects negative base prices with domain exception', () => {
    const service = new PricingService();

    expect(() => service.applyDiscount(Money.usd(-50), CustomerTier.Gold))
      .toThrow(InvalidPriceException);
  });
});
```

```php
<?php

declare(strict_types=1);

// ✅ Real state verification and boundary assertion
it('reduces total by valid coupon percentage', function () {
    $service = new CheckoutService();
    $order = new Order(subtotal: Money::usd(200_00));
    $coupon = new Coupon(code: 'SAVE15', discountPercentage: 15);

    $total = $service->applyCoupon($order, $coupon);

    expect($total->cents)->toBe(170_00);
});
```
