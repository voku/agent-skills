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
```typescript
// ❌ Vague placeholders, type suffixes, and run-on sentence naming
class UserDataHelperManager {
  processUserDataArray(userObjectDataList: User[]): ProcessedUserResultData[] {
    const tempResultArray: ProcessedUserResultData[] = [];

    for (const theUserEntityBeingProcessed of userObjectDataList) {
      const dataInfo = this.formatData(theUserEntityBeingProcessed);
      tempResultArray.push(dataInfo);
    }

    return tempResultArray;
  }

  private formatData(theUserItem: User): ProcessedUserResultData {
    return {
      userIdString: theUserItem.id,
      userFullNameString: `${theUserItem.firstName} ${theUserItem.lastName}`,
    };
  }
}
```

```php
<?php

declare(strict_types=1);

// ❌ Vague manager with redundant type parameters and placeholder variables
class OrderUtils
{
    public function handleOrderData(array $orderArrayData): array
    {
        $res = [];
        foreach ($orderArrayData as $itemObj) {
            $temp = $itemObj->price * $itemObj->qty;
            $res[] = ['val' => $temp];
        }
        return $res;
    }
}
```

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
