---
id: simp-intention-revealing-naming
title: "Intention-Revealing Naming and Eliminating Comment Noise"
category: readability
priority: MEDIUM
triggers: [vague-variable-name, noisy-comment-restatement, outdated-docblock-comment, boolean-negation-naming]
tags: [simplicity, naming, readability, self-documenting, clean-code]
---

# Intention-Revealing Naming and Eliminating Comment Noise

**Trigger Anchor:** Replace cryptic single-letter names, manager/processor dumping grounds, and noisy comments restating the code with precise domain verbs and nouns; avoid double-negative boolean names.

---

### Bad
```php
// ❌ Vague names and redundant noise comments
// Process the data array
function handle($d, $m) {
    // Check if not disabled
    if (!$d->isNotDisabled) {
        return false;
    }
    // Update manager
    return $m->proc($d);
}

// ❌ Comment that merely translates code into English
// Increment count by 1
$count++;
```

### Good
```php
// ✅ Self-documenting domain names and affirmative booleans
function processSubscriptionRenewal(Subscription $subscription, BillingGateway $billingGateway): PaymentReceipt
{
    if (!$subscription->isActive()) {
        throw new InactiveSubscriptionException($subscription->id);
    }

    return $billingGateway->chargeRenewal($subscription);
}
```
