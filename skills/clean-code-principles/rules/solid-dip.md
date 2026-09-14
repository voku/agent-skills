---
id: solid-dip
title: Dependency Inversion Principle (DIP)
category: solid-principles
priority: critical
triggers: [hardcoded-new-instantiation, direct-infrastructure-coupling, untestable-database-dependency, constructor-side-effects]
tags: [SOLID, DIP, dependency-inversion, dependency-injection, decoupling]
---

# Dependency Inversion Principle (DIP)

**Trigger Anchor:** High-level modules must not depend on low-level details. Both must depend on abstractions. Inject dependencies from outside instead of creating them with `new Concrete()`.

---

### Bad
```typescript
// ❌ High-level business service instantiates concrete infrastructure inside constructor
class OrderService {
  private db: MySQLDatabase;
  private mailer: SmtpSender;
  private stripe: StripeGateway;

  constructor() {
    this.db = new MySQLDatabase(process.env.DB_HOST);
    this.mailer = new SmtpSender(process.env.SMTP_USER);
    this.stripe = new StripeGateway(process.env.STRIPE_KEY);
  }

  async placeOrder(order: Order) {
    await this.stripe.charge(order.total);
    await this.db.save(order);
    await this.mailer.send(order.customerEmail, 'Order placed');
  }
}
```

### Good
```typescript
// ✅ High-level service depends only on injected abstractions
interface OrderRepository { save(order: Order): Promise<void>; }
interface PaymentGateway { charge(amount: number): Promise<void>; }
interface Notifier { notify(email: string, msg: string): Promise<void>; }

class OrderService {
  constructor(
    private repo: OrderRepository,
    private payment: PaymentGateway,
    private notifier: Notifier
  ) {}

  async placeOrder(order: Order) {
    await this.payment.charge(order.total);
    await this.repo.save(order);
    await this.notifier.notify(order.customerEmail, 'Order placed');
  }
}

// Low-level adapters implement the interfaces; swap DB or mail provider without touching OrderService
```
