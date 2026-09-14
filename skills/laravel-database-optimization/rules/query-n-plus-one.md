---
id: query-n-plus-one
title: "Query Performance: Eager Loading and Column Selection"
category: query
priority: CRITICAL
triggers: [n-plus-one-query, lazy-loading-violation, select-star-bloat, nested-relation-loop]
tags: [laravel, eloquent, eager-loading, n-plus-one, performance]
---

# Query Performance: Eager Loading and Column Selection

**Trigger Anchor:** Eliminate N+1 queries with eager loading (`with()`), disable lazy loading in local/CI (`Model::preventLazyLoading(!app()->isProduction())`), and select only required columns (`select(['id', 'email'])`).

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Triggers 101 queries for 100 users and pulls unnecessary text/blob columns
$users = User::all(); // SELECT * FROM users

foreach ($users as $user) {
    // ❌ Lazy loading triggered in loop: N extra queries
    echo $user->profile->bio;
    echo $user->company->name;
}
```

### Good
```php
<?php

declare(strict_types=1);

namespace App\Providers;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\ServiceProvider;

final class AppServiceProvider extends ServiceProvider
{
    public function boot(): void
    {
        // ✅ Fails fast in local/testing when an accidental lazy load occurs
        Model::preventLazyLoading(! $this->app->isProduction());
    }
}
```

```php
<?php

declare(strict_types=1);

// ✅ Eager load relations with column projection (always include foreign keys!)
$users = User::query()
    ->select(['id', 'name', 'company_id'])
    ->with([
        'profile:id,user_id,bio',
        'company:id,name',
    ])
    ->get();
```
