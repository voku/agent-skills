---
id: index-strategies
title: "Indexing Strategies: Foreign Keys, Composite, and Covering Indexes"
category: index
priority: CRITICAL
triggers: [missing-foreign-key-index, slow-multi-column-where, full-table-scan, filesort-query]
tags: [mysql, postgres, indexes, composite-index, covering-index, foreign-keys]
---

# Indexing Strategies: Foreign Keys, Composite, and Covering Indexes

**Trigger Anchor:** Index all foreign keys, create composite indexes matching multi-column WHERE/ORDER BY query shapes following the leftmost prefix rule, and utilize covering indexes for read-hot projections.

---

### Bad
```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

// ❌ Missing indexes on foreign keys and compound query predicates
return new class extends Migration {
    public function up(): void
    {
        Schema::create('orders', function (Blueprint $table) {
            $table->id();
            $table->unsignedBigInteger('user_id'); // ❌ Unindexed FK -> full table scan on joins
            $table->string('status');
            $table->timestamp('ordered_at');
            // Query: WHERE user_id = ? AND status = ? ORDER BY ordered_at DESC (performs table scan + filesort)
        });
    }
};
```

### Good
```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration {
    public function up(): void
    {
        Schema::create('orders', function (Blueprint $table) {
            $table->id();
            $table->foreignId('user_id')->constrained()->cascadeOnDelete();
            $table->string('status');
            $table->timestamp('ordered_at');

            // ✅ Composite index: Equality columns first (user_id, status), then Sort column (ordered_at)
            $table->index(['user_id', 'status', 'ordered_at'], 'idx_orders_user_status_ordered');

            // ✅ Fulltext index for search queries
            $table->fullText(['notes']);
        });
    }
};
```
