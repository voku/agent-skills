---
id: perf-efficiency
title: Performance and Memory Efficiency (Generators, Native Functions, No Globals)
category: perf
priority: MEDIUM
triggers: [memory-exhaustion, large-dataset-array, global-state-perf, unbuffered-load]
tags: [performance, generators, memory, native-functions]
---

# Performance and Memory Efficiency

**Trigger Anchor:** Use generators (`yield`) to stream large files or database query results without loading them into memory. Avoid `$GLOBALS` and superglobals in domain logic.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Reads entire 500MB CSV file into memory, causing out-of-memory fatal error
function parseBigCsv(string $path): array
{
    $rows = [];
    $handle = fopen($path, 'r');
    while (($data = fgetcsv($handle)) !== false) {
        $rows[] = $data; // unbounded memory allocation
    }
    fclose($handle);
    return $rows;
}
```

### Good
```php
<?php

declare(strict_types=1);

use Generator;

// ✅ Streams rows one by one with constant memory footprint (~few KB)
function parseBigCsv(string $path): Generator
{
    $handle = fopen($path, 'r');
    if ($handle === false) {
        throw new RuntimeException("Cannot open {$path}");
    }

    try {
        while (($data = fgetcsv($handle)) !== false) {
            yield $data;
        }
    } finally {
        fclose($handle);
    }
}

// Consumer iterates without loading full dataset
foreach (parseBigCsv('/path/to/export.csv') as $row) {
    processRow($row);
}
```
