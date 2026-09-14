---
id: type-strict-native-declarations
title: "Strict Native Declarations, Honest Return Types, and Strict Comparisons"
category: type-correctness
priority: CRITICAL
triggers: [missing-property-type, loose-equality-drift, false-folded-return-type, unsafe-strict-comparison]
tags: [type-safety, strict-types, native-types, strict-comparison, active-row]
---

# Strict Native Declarations, Honest Return Types, and Strict Comparisons

**Trigger Anchor:** Declare native types on all class properties, parameters, and return types; never downgrade `===` to loose `==` merely because a property is untyped—add the native type instead; avoid falsy folding in return types.

---

### Bad
```php
// ❌ Untyped property leads to unsafe strict comparison or loose equality bug
class UserActiveRow
{
    public $status_id; // Untyped property!
}

$row = new UserActiveRow();
// Loose equality triggers subtle type coercion bugs (e.g. 0 == "active" in legacy PHP)
if ($row->status_id == 1) { ... }

// Downgrading strict comparison to loose comparison to bypass type errors:
if ($row->status_id == '1') { ... } // Hides type drift!

// ❌ Folding falsy or zero return values into ambiguous sentinel numbers
function getActiveCount(PDO $pdo): int
{
    // Returns -1 if 0 records match, conflating error with legitimate zero!
    return $pdo->querySingleItem('SELECT COUNT(*) FROM users WHERE active = 1');
}
```

### Good
```php
declare(strict_types=1);

// ✅ Explicit native property typing and strict comparison
class UserActiveRow
{
    public int $status_id;
    public ?string $email = null;
}

$row = new UserActiveRow();
if ($row->status_id === 1) {
    // Exact type and value guaranteed
}

// ✅ Honest typed return contracts with exceptions on error
function getActiveCount(PDO $pdo): int
{
    // Returns actual 0 or throws on query failure
    return $pdo->querySingleItemAsIntOrThrowException('SELECT COUNT(*) FROM users WHERE active = 1');
}
```
