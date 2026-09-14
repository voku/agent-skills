---
id: type-shape-validation-boundaries
title: "Shape Validation at Boundaries: Typed DTOs Over Untyped Arrays"
category: type-safety
priority: CRITICAL
triggers: [untyped-array-shape, mixed-type-leak, unchecked-array-key, missing-shape-phpdoc]
tags: [type-safety, array-shapes, phpstan, dto, trust-boundary]
---

# Shape Validation at Boundaries: Typed DTOs Over Untyped Arrays

**Trigger Anchor:** Validate and narrow external untrusted inputs (JSON, HTTP, external API responses) into typed DTOs or validated array shapes before passing them into internal layers; avoid unconstrained `array` or `mixed`.

---

### Bad
```php
// ❌ Unconstrained array passed across layer boundaries without shape contracts
class WebhookHandler
{
    /**
     * @param array $payload
     */
    public function handle(array $payload): void
    {
        // Unsafe key accesses trigger undefined array key notices and type errors at runtime
        $orderId = $payload['data']['order']['id'];
        $amount = (float)$payload['data']['amount'];
        $this->process($orderId, $amount);
    }
}
```

### Good
```php
// ✅ Typed readonly DTO validating external payload at boundary
readonly class WebhookOrderPayload
{
    public function __construct(
        public int $orderId,
        public float $amount,
        public string $currency,
    ) {}

    /**
     * @param array<string, mixed> $raw
     */
    public static function fromArray(array $raw): self
    {
        if (!isset($raw['data']['order']['id'], $raw['data']['amount'], $raw['data']['currency'])) {
            throw new \InvalidArgumentException('Malformed webhook payload structure.');
        }

        return new self(
            orderId: (int)$raw['data']['order']['id'],
            amount: (float)$raw['data']['amount'],
            currency: (string)$raw['data']['currency'],
        );
    }
}
```
