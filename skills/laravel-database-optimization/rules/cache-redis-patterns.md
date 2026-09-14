---
id: cache-redis-patterns
title: "Redis Caching, Invalidation, Tags, and TTLs"
category: cache
priority: HIGH
triggers: [un-cached-repeated-query, stale-cache-bug, cache-stampede, missing-cache-tags]
tags: [redis, caching, cache-remember, cache-tags, invalidation, ttl]
---

# Redis Caching, Invalidation, Tags, and TTLs

**Trigger Anchor:** Cache expensive database queries with `Cache::remember()` using strict TTLs, and invalidate selectively via cache tags (`Cache::tags(['users'])`) or model event observers.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Indefinite cache without TTL or invalidation creates permanent stale data
$categories = Cache::rememberForever('all_categories', function () {
    return Category::with('subcategories')->get();
    // When a category is updated in DB, this cache never refreshes!
});
```

### Good
```php
<?php

declare(strict_types=1);

namespace App\Services;

use App\Models\Category;
use Illuminate\Support\Collection;
use Illuminate\Support\Facades\Cache;

final class CategoryCache
{
    private const int TTL_SECONDS = 3600; // 1 hour

    /**
     * @return Collection<int, Category>
     */
    public function getActive(): Collection
    {
        // ✅ Cache tagged for atomic group invalidation
        return Cache::tags(['categories'])->remember(
            'categories:active',
            self::TTL_SECONDS,
            static fn () => Category::with('subcategories')->where('is_active', true)->get(),
        );
    }

    public function flush(): void
    {
        // ✅ Flushes all keys tagged with 'categories' at once
        Cache::tags(['categories'])->flush();
    }
}
```

```php
<?php

declare(strict_types=1);

namespace App\Observers;

use App\Models\Category;
use App\Services\CategoryCache;

final readonly class CategoryObserver
{
    public function __construct(private CategoryCache $cache) {}

    public function saved(Category $category): void
    {
        $this->cache->flush();
    }

    public function deleted(Category $category): void
    {
        $this->cache->flush();
    }
}
```
