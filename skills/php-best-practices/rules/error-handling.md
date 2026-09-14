---
id: error-handling
title: Resilient Error Handling and Domain Exceptions
category: error
priority: HIGH
triggers: [suppressed-error, broad-catch, generic-exception, missing-finally]
tags: [exceptions, error-handling, try-catch, finally]
---

# Resilient Error Handling and Domain Exceptions

**Trigger Anchor:** Throw typed domain exceptions instead of returning `false` or null. Catch only specific exceptions at recovery boundaries. Use `finally` for resource cleanup. Never suppress errors with `@`.

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Silencing errors with @, returning false on error, and catching generic Exception
function readFileContents(string $path)
{
    $file = @fopen($path, 'r'); // hides underlying permission/missing error
    if (!$file) {
        return false;
    }

    try {
        $content = fread($file, 1024);
        fclose($file);
        return $content;
    } catch (\Exception $e) { // blanket catch catches unrelated bugs
        return null;
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

final class FileReadException extends RuntimeException
{
    public static function unableToOpen(string $path): self
    {
        return new self("Cannot open file at {$path}");
    }
}

function readFileContents(string $path): string
{
    $file = fopen($path, 'r');
    if ($file === false) {
        throw FileReadException::unableToOpen($path);
    }

    try {
        $content = stream_get_contents($file);
        if ($content === false) {
            throw new FileReadException("Error reading {$path}");
        }
        return $content;
    } finally {
        // ✅ Guaranteed resource cleanup even if exceptions throw
        fclose($file);
    }
}
```
