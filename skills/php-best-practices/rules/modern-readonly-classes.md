# Readonly Classes

## Why it matters
When you mark individual properties `readonly`, it is easy to forget one — especially when a new property is added weeks later. A `readonly` class modifier applies the constraint to every promoted or declared property automatically, making immutability structural rather than a per-property discipline.

## Rule
Use `readonly class` for pure value objects where every property is set at construction and must never change. This is the default choice for DTOs, events, and commands.

## Bad
```php
<?php

declare(strict_types=1);

// Easy to forget readonly on a new property — Color is silently mutable
class Colour
{
    public function __construct(
        public readonly int $red,
        public readonly int $green,
        public int $blue,   // forgot readonly — silent bug
    ) {}
}
```

## Better
```php
<?php

declare(strict_types=1);

readonly class Colour
{
    public function __construct(
        public int $red,
        public int $green,
        public int $blue,
    ) {}
}
```

## Best
```php
<?php

declare(strict_types=1);

final readonly class Colour
{
    public function __construct(
        public int $red,
        public int $green,
        public int $blue,
    ) {}

    public function withBlue(int $blue): self
    {
        return new self($this->red, $this->green, $blue);
    }
}
```

## Exceptions / trade-offs
- Classes with properties that need post-construction mutation (e.g., entities with status transitions) cannot be `readonly`.
- Classes designed to be extended may be `readonly` but not `final`; be aware that child classes must also be `readonly`.
- ORM entities managed by Doctrine or Eloquent typically require mutable, non-readonly properties.

## Static-analysis notes
PHPStan and Psalm treat every property in a `readonly class` as write-once. Any write attempt after construction is flagged as an error. Tools also recognise that `readonly class` implies all properties are `readonly`, and will warn about redundant per-property annotations.

## Version notes
`PHP 8.2+`

## Related topics
- [modern-readonly-properties.md](modern-readonly-properties.md) — per-property readonly for when you need selective immutability
- [modern-constructor-promotion.md](modern-constructor-promotion.md) — pair with promotion for compact value objects
