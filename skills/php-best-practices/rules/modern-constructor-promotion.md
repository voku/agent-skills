# Constructor Property Promotion

## Why it matters
Manually declaring properties, then re-listing them as constructor parameters, then assigning them is mechanical repetition. That boilerplate drifts — someone adds a parameter but forgets the property declaration, or renames one place but not another. Promotion eliminates the surface area for these mistakes by collapsing all three steps into one canonical location.

## Rule
Use constructor property promotion for dependency injection and DTOs. Skip it only when the constructor body contains significant logic that would become harder to read alongside the promoted declarations.

## Bad
```php
<?php

declare(strict_types=1);

class UserService
{
    private UserRepository $repository;
    private EventDispatcher $dispatcher;
    private LoggerInterface $logger;

    public function __construct(
        UserRepository $repository,
        EventDispatcher $dispatcher,
        LoggerInterface $logger,
    ) {
        $this->repository = $repository;
        $this->dispatcher = $dispatcher;
        $this->logger = $logger;
    }
}
```

## Better
```php
<?php

declare(strict_types=1);

class UserService
{
    public function __construct(
        private UserRepository $repository,
        private EventDispatcher $dispatcher,
        private LoggerInterface $logger,
    ) {}
}
```

## Best
```php
<?php

declare(strict_types=1);

final class CreateUserCommand
{
    public function __construct(
        public readonly string $email,
        public readonly string $name,
        public readonly string $role = 'user',
    ) {}
}
```

## Exceptions / trade-offs
- When the constructor body has non-trivial logic (validation, transformation, conditional branching), keep traditional declarations so the assignments are not buried among the promoted parameter list.
- Non-promoted properties (e.g., lazily initialised, computed in the body) can coexist, but more than one or two breaks the clarity benefit.

## Static-analysis notes
PHPStan and Psalm infer the property type directly from the promoted parameter type, including nullability. No separate `@var` annotation is required or useful.

## Version notes
`PHP 8.0+`

## Related topics
- [modern-readonly-properties.md](modern-readonly-properties.md) — add `readonly` to promoted properties for immutability
- [modern-readonly-classes.md](modern-readonly-classes.md) — make every property readonly at the class level
