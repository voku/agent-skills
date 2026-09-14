---
id: perf-caching-invalidation
title: "Caching Strategy, TTLs, and Stampede Protection"
category: caching
priority: HIGH
triggers: [cache-stampede, dogpiling-thundering-herd, missing-cache-ttl, stale-unversioned-cache-key]
tags: [performance, caching, redis, ttl, cache-stampede, invalidation]
---

# Caching Strategy, TTLs, and Stampede Protection

**Trigger Anchor:** Specify explicit time-to-live (TTL) on all cached entries; incorporate entity versions or modification timestamps into cache keys; use atomic locks or stampede protection on high-concurrency recomputation.

---

### Bad
```php
// ❌ Caching indefinitely without TTL; stale cache upon entity updates
$userStats = Cache::rememberForever('user_stats_' . $userId, function () use ($userId) {
    return calculateHeavyStats($userId);
});

// ❌ Thundering herd / cache stampede: when cache key expires under high load,
// 100 concurrent requests all execute the heavy query simultaneously!
$popularFeed = Cache::get('homepage_feed');
if ($popularFeed === null) {
    $popularFeed = renderHeavyFeed();
    Cache::put('homepage_feed', $popularFeed, 300);
}
```

### Good
```php
// ✅ Versioned cache key incorporating updated_at timestamp and explicit TTL
$cacheKey = sprintf('user_stats_%d_v%d', $user->id, $user->updated_at->getTimestamp());
$userStats = Cache::remember($cacheKey, 3600, function () use ($user) {
    return calculateHeavyStats($user->id);
});

// ✅ Atomic lock / stampede-protected cache calculation
$popularFeed = Cache::remember('homepage_feed', 300, function () {
    return Cache::lock('computing_homepage_feed', 10)->get(function () {
        return renderHeavyFeed();
    });
});
```
