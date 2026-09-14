---
id: solid-ocp
title: Open/Closed Principle (OCP)
category: solid-principles
priority: critical
triggers: [switch-on-type, growing-if-else-chain, editing-core-class-for-new-feature, type-code-conditional]
tags: [SOLID, OCP, open-closed, polymorphism, strategy-pattern]
---

# Open/Closed Principle (OCP)

**Trigger Anchor:** Open for extension, closed for modification. Add new behaviors by adding new classes or handlers, not by editing existing `switch`/`if` statements.

---

### Bad
```typescript
// ❌ Core processor must be edited every time a new payment or report type is added
class PaymentProcessor {
  process(payment: Payment) {
    if (payment.type === 'credit_card') {
      return this.processCard(payment);
    } else if (payment.type === 'paypal') {
      return this.processPayPal(payment);
    } else if (payment.type === 'apple_pay') {
      return this.processApplePay(payment);
    } // Every new payment method requires modifying this method
  }
}
```

### Good
```typescript
// ✅ Polymorphic handlers registered into a stable runner
interface PaymentHandler {
  supports(type: string): boolean;
  process(payment: Payment): Promise<PaymentResult>;
}

class PaymentProcessor {
  constructor(private handlers: PaymentHandler[]) {}

  async process(payment: Payment): Promise<PaymentResult> {
    const handler = this.handlers.find(h => h.supports(payment.type));
    if (!handler) throw new UnsupportedPaymentError(payment.type);
    return handler.process(payment);
  }
}

// Adding ApplePay requires zero edits to PaymentProcessor
class ApplePayHandler implements PaymentHandler {
  supports(type: string) { return type === 'apple_pay'; }
  async process(p: Payment) { return chargeApplePay(p); }
}
```
