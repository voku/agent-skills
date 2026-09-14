---
id: db-assertions
title: "Database State, Record Absence, and Soft Delete Assertions"
category: db
priority: HIGH
triggers: [manual-db-query-assertion, missing-soft-delete-check, untracked-db-side-effects]
tags: [laravel, testing, database-assertions, assertDatabaseHas, soft-deletes]
---

# Database State, Record Absence, and Soft Delete Assertions

**Trigger Anchor:** Verify database persistence using built-in assertions (`assertDatabaseHas`, `assertDatabaseMissing`, `assertModelExists`, `assertSoftDeleted`) instead of manual query counts.

---

### Bad
```php
<?php

// ❌ Manual queries and count assertions instead of built-in helpers
test('deletes product', function () {
    $product = Product::factory()->create();

    $this->delete("/api/products/{$product->id}");

    // ❌ Cumbersome manual query that misses soft-delete verification
    $remaining = Product::where('id', $product->id)->count();
    expect($remaining)->toBe(0);
});
```

### Good
```php
<?php

declare(strict_types=1);

use App\Models\Product;
use Illuminate\Foundation\Testing\RefreshDatabase;

uses(RefreshDatabase::class);

test('soft-deletes product and archives audit record', function () {
    $product = Product::factory()->create(['name' => 'Vintage Chair']);

    $response = $this->deleteJson("/api/products/{$product->id}");

    $response->assertNoContent();

    // ✅ Explicit soft-delete assertion verifies deleted_at column is filled
    $this->assertSoftDeleted($product);

    // ✅ AssertDatabaseHas for specific column state
    $this->assertDatabaseHas('audit_logs', [
        'auditable_type' => Product::class,
        'auditable_id' => $product->id,
        'action' => 'deleted',
    ]);

    // ✅ Assert database missing for purge
    $this->assertDatabaseMissing('product_sync_queue', [
        'product_id' => $product->id,
    ]);
});
```
