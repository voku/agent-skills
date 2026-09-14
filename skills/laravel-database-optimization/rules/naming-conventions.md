---
id: naming-conventions
title: "Database Naming Conventions: Tables, Columns, and Relationships"
category: naming
priority: HIGH
triggers: [non-standard-table-name, mismatched-foreign-key, relationship-naming-defect, non-conventional-migration]
tags: [laravel, eloquent, database-naming, conventions, relationships]
---

# Database Naming Conventions: Tables, Columns, and Relationships

**Trigger Anchor:** Follow standard Eloquent naming conventions (snake_case plural tables, singular snake_case FKs `user_id`, camelCase relationships) to prevent silent query failure or custom key overrides.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Violates standard conventions; forces custom keys on every relationship and query
class OrderModel extends Model
{
    protected $table = 'tblOrder'; // ❌ Non-standard table prefix & casing
    protected $primaryKey = 'orderId'; // ❌ Non-standard primary key

    // ❌ Plural relationship named singular, missing convention
    public function order_item(): HasMany
    {
        return $this->hasMany(OrderItem::class, 'orderFK', 'orderId');
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\HasMany;

// ✅ Conventional names allow zero-configuration Eloquent resolution
final class Order extends Model
{
    // Auto-resolves to table: 'orders' with PK: 'id'

    /**
     * ✅ Singular camelCase for BelongsTo / HasOne
     */
    public function customer(): BelongsTo
    {
        return $this->belongsTo(Customer::class); // Foreign key: 'customer_id'
    }

    /**
     * ✅ Plural camelCase for HasMany / BelongsToMany
     */
    public function items(): HasMany
    {
        return $this->hasMany(OrderItem::class); // Foreign key: 'order_id'
    }
}
```

### Convention Matrix
| Concept | Format | Example |
|---------|--------|---------|
| Table | Plural `snake_case` | `users`, `order_items` |
| Pivot Table | Singular alphabetical `snake_case` | `role_user`, `course_student` |
| Foreign Key | Singular model + `_id` | `user_id`, `author_id` |
| HasMany Relation | Plural `camelCase` | `items()`, `comments()` |
| BelongsTo Relation | Singular `camelCase` | `user()`, `category()` |
