---
id: simp-premature-abstraction
title: "Guarding Against Premature Abstraction and Speculative Generality"
category: abstraction
priority: HIGH
triggers: [single-implementation-interface, speculative-factory, wrapper-purely-for-mocking, unnecessary-indirection]
tags: [simplicity, premature-abstraction, yagni, clean-code, indirection]
---

# Guarding Against Premature Abstraction and Speculative Generality

**Trigger Anchor:** Inline single-use helpers, interfaces, or factories with only one real implementation; never introduce bespoke wrappers or helper classes purely to mock a single call in a test when surrounding code calls it directly.

---

### Bad
```php
// ❌ Creating an interface, factory, and service layer for a single trivial operation
interface CsvExportFormatStrategyInterface
{
    public function formatRow(array $data): string;
}

class StandardCsvExportFormatStrategy implements CsvExportFormatStrategyInterface
{
    public function formatRow(array $data): string { return implode(',', $data); }
}

class CsvExportStrategyFactory
{
    public function create(): CsvExportFormatStrategyInterface {
        return new StandardCsvExportFormatStrategy(); // Only ever one strategy!
    }
}

// ❌ Bespoke wrapper class introduced solely to mock a global in a unit test
class CurrentTimeProviderWrapper
{
    public function getMicrotime(): float { return microtime(true); }
}
```

### Good
```php
// ✅ Direct, straightforward implementation without premature indirection
class CsvExporter
{
    public function export(array $rows): string
    {
        $fp = fopen('php://temp', 'r+');
        foreach ($rows as $row) {
            fputcsv($fp, $row);
        }
        rewind($fp);
        return stream_get_contents($fp);
    }
}

// ✅ Use standard library / framework primitives directly; inject clock interface only when multi-timezone / test time travel is genuinely needed
class JobMetrics
{
    public function recordExecutionTime(float $startMicrotime): float
    {
        return microtime(true) - $startMicrotime;
    }
}
```
