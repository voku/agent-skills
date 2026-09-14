---
id: migrate-zero-downtime
title: Zero-Downtime Migrations and Concurrent Indexing
category: migrate
priority: HIGH
triggers: [table-lock-migration, column-addition-downtime, index-creation-lock, production-migration-hang]
tags: [migrations, zero-downtime, mysql, ddl, online-schema-change]
---

# Zero-Downtime Migrations and Concurrent Indexing

**Trigger Anchor:** Execute schema changes without downtime by adding nullable/defaulted columns, creating large indexes concurrently/algorithmically (`ALGORITHM=INPLACE`), and separating schema additions from data backfills.

---

### Bad
```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

// ❌ Adding non-nullable column without default locks multi-million row table
return new class extends Migration {
    public function up(): void
    {
        Schema::table('orders', function (Blueprint $table) {
            // ❌ MySQL locks table for write rebuild on 50M rows -> outage
            $table->string('status_code');
            $table->index('status_code');
        });
    }
};
```

### Good
```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Schema;

return new class extends Migration {
    public function up(): void
    {
        // Phase 1: Add column as nullable so table rewrite is instantaneous
        Schema::table('orders', function (Blueprint $table) {
            $table->string('status_code')->nullable()->after('status');
        });

        // Phase 2: Add index with INPLACE algorithm to permit concurrent reads and writes
        DB::statement('ALTER TABLE orders ADD INDEX idx_orders_status_code (status_code), ALGORITHM=INPLACE, LOCK=NONE');
    }
};
```

### 3-Phase Zero Downtime Rollout
1. **Expand:** Deploy migration adding nullable column/table.
2. **Dual-Write:** Deploy application code writing to both old and new schema. Backfill historical records asynchronously via background worker.
3. **Contract:** Switch reads to new column, drop legacy column in a subsequent release.
