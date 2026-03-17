# First-Class Callable Syntax

## Why it matters
Array callables like `[$obj, 'method']` are opaque strings at the type level — renaming the method in an IDE does not update them, static analysis cannot resolve their signature, and a typo produces a runtime error. First-class callables are real closures with fully-resolved types available at the call site.

## Rule
Use the `...` first-class callable syntax instead of array callables or `Closure::fromCallable()`. The result is a typed `Closure` that IDEs and static analysers can inspect.

## Bad
```php
<?php

declare(strict_types=1);

final class Formatter
{
    public function format(string $value): string
    {
        return strtoupper(trim($value));
    }
}

$formatter = new Formatter();

// String-based — not refactorable, no type info, runtime error on typo
$callable = [$formatter, 'format'];

$results = array_map($callable, $names);
```

## Better
```php
<?php

declare(strict_types=1);

final class Formatter
{
    public function format(string $value): string
    {
        return strtoupper(trim($value));
    }
}

$formatter = new Formatter();

// Explicit, but verbose
$callable = Closure::fromCallable([$formatter, 'format']);

$results = array_map($callable, $names);
```

## Best
```php
<?php

declare(strict_types=1);

final class Formatter
{
    public function format(string $value): string
    {
        return strtoupper(trim($value));
    }
}

$formatter = new Formatter();

// Concise, refactorable, fully typed Closure
$results = array_map($formatter->format(...), $names);

// Works for static methods and plain functions too
$trimmed = array_map(trim(...), $names);
```

## Exceptions / trade-offs
- When the method name is determined at runtime (dynamic dispatch), the array callable `[$obj, $methodName]` remains necessary. Document why and validate the name.

## Static-analysis notes
PHPStan and Psalm resolve the exact `Closure` type (including parameter and return types) from first-class callables. This enables accurate type inference for `array_map`, `array_filter`, and similar higher-order functions.

## Version notes
`PHP 8.1+`

## Related topics
- [modern-arrow-functions.md](modern-arrow-functions.md) — lightweight closures for simple transforms
- [modern-pipe-operator.md](modern-pipe-operator.md) — composing callables in a pipeline
