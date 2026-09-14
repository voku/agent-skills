---
id: arch-coupling-cohesion
title: "High Cohesion and Loose Coupling: Dependency Inversion and Leaky Abstractions"
category: coupling
priority: HIGH
triggers: [circular-dependency, tight-coupling-concrete, leaky-abstraction-internals, shotgun-surgery]
tags: [architecture, coupling, cohesion, dependency-inversion, boundaries]
---

# High Cohesion and Loose Coupling: Dependency Inversion and Leaky Abstractions

**Trigger Anchor:** Depend on stable abstractions rather than volatile concrete implementations; prevent leaky abstractions that expose internal database cursors, raw queries, or low-level connection handles to caller layers.

---

### Bad
```php
// ❌ High coupling: high-level business service directly instantiates and depends on MySQL PDO
class MonthlyBillingService
{
    public function generateBills(): void
    {
        // Concrete dependency and SQL queries leaked into billing domain service
        $pdo = new \PDO('mysql:host=localhost;dbname=prod', 'root', 'secret');
        $stmt = $pdo->query('SELECT * FROM subscriptions WHERE status = 1');
        while ($row = $stmt->fetch(\PDO::FETCH_ASSOC)) {
            // Leaks DB column names directly into billing algorithm
        }
    }
}

// ❌ Leaky abstraction exposing PDOStatement cursor across layer boundaries
interface SubscriptionRepositoryInterface
{
    public function getActiveSubscriptionsCursor(): \PDOStatement; // Leaks driver-specific cursor!
}
```

### Good
```php
// ✅ Dependency inversion: domain service depends on high-level repository interface
class MonthlyBillingService
{
    public function __construct(
        private readonly SubscriptionRepositoryInterface $subscriptions,
        private readonly InvoiceGeneratorInterface $invoiceGenerator,
    ) {}

    public function generateBills(): void
    {
        // Clean domain models returned, abstracting database driver details
        $activeSubscriptions = $this->subscriptions->findActive();
        foreach ($activeSubscriptions as $subscription) {
            $this->invoiceGenerator->generateForSubscription($subscription);
        }
    }
}
```
