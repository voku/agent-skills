---
id: bus-batching-chaining
title: "Bus Batches, Sequential Chains, and Chunked Sub-Batches"
category: bus
priority: HIGH
triggers: [un-batched-mass-dispatch, broken-job-chain, unhandled-batch-failure, memory-bloat-mass-dispatch]
tags: [laravel, bus, batch, chain, BusBatch, chunking]
---

# Bus Batches, Sequential Chains, and Chunked Sub-Batches

**Trigger Anchor:** Choose parallel `Bus::batch()` for independent progress-tracked jobs, `Bus::chain()` for strict sequential steps where failure aborts subsequent tasks, and dispatch large sets in chunked sub-batches.

---

### Bad
```php
<?php

// ❌ Dispatching 100k individual jobs in an unbatched loop exhausts Redis memory
User::all()->each(function ($user) {
    SendEmailJob::dispatch($user->id); // 100k individual redis pushes without progress tracking
});
```

### Good
```php
<?php

declare(strict_types=1);

use App\Jobs\CreateInvoicePdf;
use App\Jobs\SendReceiptEmail;
use App\Jobs\UpdateInventory;
use Illuminate\Bus\Batch;
use Illuminate\Support\Facades\Bus;
use Throwable;

// ✅ Bus::chain for sequential workflows where Step 2 requires Step 1
Bus::chain([
    new CreateInvoicePdf($orderId),
    new SendReceiptEmail($orderId),
    new UpdateInventory($orderId),
])->catch(function (Throwable $e) {
    Log::error('Order completion chain halted', ['error' => $e->getMessage()]);
})->dispatch();

// ✅ Bus::batch for parallel processing with progress callbacks and failure tolerance
$batch = Bus::batch([])
    ->then(function (Batch $batch) {
        // Executed once all jobs complete successfully
        Log::info('Batch completed successfully');
    })
    ->catch(function (Batch $batch, Throwable $e) {
        // Executed on first job failure
    })
    ->finally(function (Batch $batch) {
        // Clean up temporary files
    })
    ->allowFailures()
    ->dispatch();

// Add jobs in chunked streams without exhausting memory
User::query()->chunkById(1000, function ($users) use ($batch) {
    $batch->add(
        $users->map(fn ($u) => new ProcessUserExport($u->id))->all()
    );
});
```
