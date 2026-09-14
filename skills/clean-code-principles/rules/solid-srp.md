---
id: solid-srp
title: Single Responsibility Principle (SRP)
category: solid-principles
priority: critical
triggers: [god-class, multi-concern-module, mixed-persistence-validation-notification, monolithic-function]
tags: [SOLID, SRP, single-responsibility, cohesion]
---

# Single Responsibility Principle (SRP)

**Trigger Anchor:** One reason to change. Separate domain policy, persistence, validation, and presentation into cohesive units.

---

## Class-Level (Mixed Concerns vs Cohesive Units)

### Bad
```typescript
// ❌ Handles validation, database persistence, email notifications, and logging
class UserManager {
  async createUser(data: UserData): Promise<User> {
    if (!data.email.includes('@')) throw new Error('Invalid email');
    const user = await db.users.create(data);
    await mailer.send(user.email, 'Welcome!');
    fs.appendFileSync('audit.log', `User ${user.id} created`);
    return user;
  }
}
```

### Good
```typescript
// ✅ Composed orchestrator delegating to single-responsibility collaborators
class CreateUserUseCase {
  constructor(
    private validator: UserValidator,
    private repository: UserRepository,
    private notifications: UserNotificationService,
    private logger: AuditLogger
  ) {}

  async execute(data: UserData): Promise<User> {
    this.validator.validate(data);
    const user = await this.repository.create(data);
    await this.notifications.sendWelcome(user.email);
    await this.logger.log(`User ${user.id} created`);
    return user;
  }
}
```

---

## Function-Level (Monolith vs Step Pipeline)

### Bad
```typescript
// ❌ One monolithic function doing fetching, pricing, tax, payment, and email
async function processOrder(orderId: string): Promise<void> {
  const order = await db.query('SELECT * FROM orders WHERE id = ?', [orderId]);
  const tax = order.total * 0.1;
  const grandTotal = order.total + tax;
  await stripe.charges.create({ amount: grandTotal, customer: order.customerId });
  await db.query('UPDATE orders SET status = "completed" WHERE id = ?', [orderId]);
  await mailer.send(order.email, 'Confirmed');
}
```

### Good
```typescript
// ✅ Focused pipeline of cohesive, single-purpose functions
async function processOrder(orderId: string): Promise<ProcessedOrder> {
  const order = await fetchOrder(orderId);
  const pricing = calculatePricing(order);
  const payment = await chargePayment(order.customerId, pricing.grandTotal);
  return finalizeOrder(order.id, payment.id);
}
```
