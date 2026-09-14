---
id: data-integrity
title: "Data Debt: Schema Drift, Missing Indexes, and Orphaned Records"
category: data
priority: HIGH
triggers: [missing-index, orphaned-records, schema-drift, missing-foreign-key]
tags: [database, mysql, postgresql, migrations, indexing, referential-integrity]
---

# Data Debt: Schema Drift, Missing Indexes, and Orphaned Records

**Trigger Anchor:** Maintain strict migration-only schema provenance, index foreign keys and query predicate columns, and enforce foreign-key constraints to prevent orphaned records.

---

### Bad
```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

// ❌ Missing foreign key constraint and missing indexes on query predicates
return new class extends Migration {
    public function up(): void
    {
        Schema::create('order_items', function (Blueprint $table) {
            $table->id();
            // ❌ Unconstrained foreign key: deleting order leaves orphaned records
            $table->unsignedBigInteger('order_id');
            // ❌ Frequently filtered/joined column without index -> full table scan
            $table->string('sku');
            $table->integer('quantity');
            $table->timestamps();
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

// ✅ Explicit foreign key constraint with cascade/restrict policy and targeted indexes
return new class extends Migration {
    public function up(): void
    {
        Schema::create('order_items', function (Blueprint $table) {
            $table->id();
            $table->foreignId('order_id')
                ->constrained('orders')
                ->cascadeOnDelete(); // Enforces referential integrity

            $table->string('sku');
            $table->integer('quantity');
            $table->timestamps();

            // ✅ Composite index matching common lookup pattern
            $table->index(['order_id', 'sku']);
        });
    }
};
```
