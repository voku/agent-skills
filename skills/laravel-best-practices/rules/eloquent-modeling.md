---
id: eloquent-modeling
title: "Eloquent Modeling: Modern Casts, Accessors, and Lifecycles"
category: eloquent
priority: HIGH
triggers: [legacy-casts-property, legacy-get-attr-mutator, missing-prunable-cleanup, soft-delete-confusion]
tags: [laravel, eloquent, casts, accessors, prunable, soft-deletes]
---

# Eloquent Modeling: Modern Casts, Accessors, and Lifecycles

**Trigger Anchor:** Define model attribute casts via the modern `casts()` method returning typed cast arrays/enums, use `Attribute::make()` closures for accessors/mutators, and automate record lifecycles using the `Prunable` trait.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Legacy casts property, legacy string mutator methods, and unmanaged stale records
class User extends Authenticatable
{
    // ❌ Deprecated style: property-based casts
    protected $casts = [
        'is_admin' => 'boolean',
        'metadata' => 'array',
    ];

    // ❌ Legacy split accessor/mutator methods
    public function getFullNameAttribute(): string
    {
        return "{$this->first_name} {$this->last_name}";
    }

    public function setEmailAttribute(string $value): void
    {
        $this->attributes['email'] = strtolower(trim($value));
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

namespace App\Models;

use App\Enums\UserRole;
use Illuminate\Database\Eloquent\Builder;
use Illuminate\Database\Eloquent\Casts\Attribute;
use Illuminate\Database\Eloquent\Prunable;
use Illuminate\Foundation\Auth\User as Authenticatable;

final class User extends Authenticatable
{
    use Prunable;

    /**
     * ✅ Modern method-based casts with typed Enums and native datetime
     *
     * @return array<string, string|class-string>
     */
    protected function casts(): array
    {
        return [
            'role' => UserRole::class,
            'is_active' => 'boolean',
            'metadata' => 'encrypted:array',
            'last_login_at' => 'immutable_datetime',
        ];
    }

    /**
     * ✅ Modern unified Attribute object with get and set closures
     */
    protected function email(): Attribute
    {
        return Attribute::make(
            get: static fn (?string $val): ?string => $val,
            set: static fn (string $val): string => strtolower(trim($val)),
        );
    }

    /**
     * ✅ Automatic cleanup of unverified abandoned accounts
     */
    public function prunable(): Builder
    {
        return static::whereNull('email_verified_at')
            ->where('created_at', '<=', now()->subDays(30));
    }
}
```
