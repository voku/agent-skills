---
id: perf-memory-streaming
title: "Memory Management: Streaming Large Payloads and Generators"
category: memory
priority: HIGH
triggers: [out-of-memory-exhaustion, loading-large-file-string, unbuffered-query-cursor, chunk-processing]
tags: [performance, memory, generators, streaming, chunking, large-datasets]
---

# Memory Management: Streaming Large Payloads and Generators

**Trigger Anchor:** Stream large datasets, CSV exports, and file operations using generators (`yield`) or chunking (`chunkById`); avoid loading full multi-megabyte payloads into memory as giant arrays or strings.

---

### Bad
```php
// ❌ Loading an entire multi-gigabyte file into memory as a string
$logContent = file_get_contents('/var/log/app/large-audit.log');
$lines = explode("\n", $logContent);

// ❌ Loading 500,000 database rows into an in-memory array
$allRows = $pdo->query('SELECT * FROM large_transactions')->fetchAll();
foreach ($allRows as $row) {
    $report->add($row);
}
```

### Good
```php
// ✅ Line-by-line streaming generator with O(1) memory footprint
function readLines(string $filePath): \Generator
{
    $handle = fopen($filePath, 'r');
    if ($handle === false) {
        throw new \RuntimeException('Failed to open file: ' . $filePath);
    }

    try {
        while (($line = fgets($handle)) !== false) {
            yield $line;
        }
    } finally {
        fclose($handle);
    }
}

foreach (readLines('/var/log/app/large-audit.log') as $line) {
    $parser->parseLine($line);
}

// ✅ Unbuffered query iteration or chunked processing
$stmt = $pdo->prepare('SELECT * FROM large_transactions');
$stmt->execute();
while ($row = $stmt->fetch(\PDO::FETCH_ASSOC)) {
    $report->add($row); // Memory remains constant regardless of table size
}
```
