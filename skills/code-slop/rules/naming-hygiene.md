---
id: naming-hygiene
title: Natural Domain Naming vs Generic Slop
category: naming
priority: CRITICAL
triggers: [generic-placeholder-name, over-descriptive-name, suffix-abuse, type-in-name]
tags: [naming, domain-modeling, readability, slop-reduction]
---

# Natural Domain Naming vs Generic Slop

**Trigger Anchor:** Use concise, intention-revealing nouns and verbs without redundant type suffixes (`userArray`, `orderObj`), vague grab-bag suffixes (`*Helper`, `*Manager`, `*Processor`), or overly narrative sentences (`theActiveAdminUser`); name by domain meaning.

---

### Bad

Examples of redundant, placeholder-heavy names:

| Language | Bad name | Why it obscures the domain |
|---|---|---|
| TypeScript | `UserDataHelperManager` | Generic helper/manager nesting without a clear role |
| TypeScript | `processUserDataArray` | Repeats types instead of describing the operation |
| TypeScript | `theUserEntityBeingProcessed` | Narrates control flow rather than naming a user |
| PHP | `OrderUtils` | Unbounded catch-all name |
| PHP | `$orderArrayData`, `$itemObj` | Type suffixes that hide domain meaning |

The problem is comprehension and ownership, not the author who produced the names.

### Good
```typescript
// ✅ Focused domain concept, natural naming without noise words
class UserFormatter {
  formatAll(users: User[]): FormattedUser[] {
    return users.map(user => this.format(user));
  }

  format(user: User): FormattedUser {
    return {
      id: user.id,
      name: `${user.firstName} ${user.lastName}`,
    };
  }
}
```

```php
<?php

declare(strict_types=1);

// ✅ Precise domain models and clean array mapping
final readonly class OrderPricer
{
    /**
     * @param list<OrderItem> $items
     * @return list<Money>
     */
    public function lineTotals(array $items): array
    {
        return array_map(
            static fn (OrderItem $item): Money => $item->unitPrice->multiply($item->quantity),
            $items,
        );
    }
}
```
