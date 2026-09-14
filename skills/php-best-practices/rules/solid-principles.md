---
id: solid-principles
title: SOLID Principles in Modern PHP
category: solid
priority: HIGH
triggers: [god-class, tight-coupling, violated-lsp, fat-interface, hardcoded-dependency]
tags: [SOLID, srp, ocp, lsp, isp, dip, architecture]
---

# SOLID Principles in Modern PHP

**Trigger Anchor:** Design classes with a single responsibility (SRP), open for extension via polymorphism (OCP), substitutable subtypes (LSP), client-focused interfaces (ISP), and dependency on abstractions injected via constructors (DIP).

---

### Bad
```php
<?php

declare(strict_types=1);

// ❌ Violates SRP (validation + DB + notification) and DIP (hardcoded dependency)
class UserManager
{
    public function registerUser(array $data): void
    {
        if (!isset($data['email'])) throw new Exception('Missing email');

        // Hardcoded dependency (violates DIP)
        $pdo = new PDO('mysql:host=localhost;dbname=test', 'root', '');
        $stmt = $pdo->prepare('INSERT INTO users (email) VALUES (?)');
        $stmt->execute([$data['email']]);

        // Direct email sending in manager
        mail($data['email'], 'Welcome', 'Welcome to our platform!');
    }
}
```

### Good
```php
<?php

declare(strict_types=1);

// ✅ Focused interfaces (ISP) and injected abstractions (DIP)
interface UserRepositoryInterface
{
    public function save(User $user): void;
}

interface NotificationServiceInterface
{
    public function sendWelcome(EmailAddress $email): void;
}

// ✅ Single responsibility orchestrator (SRP)
final readonly class RegisterUserUseCase
{
    public function __construct(
        private UserRepositoryInterface $repository,
        private NotificationServiceInterface $notifications,
    ) {}

    public function execute(RegisterUserCommand $command): User
    {
        $user = User::create($command->email, $command->hashedPassword);
        $this->repository->save($user);
        $this->notifications->sendWelcome($user->email);
        return $user;
    }
}
```
