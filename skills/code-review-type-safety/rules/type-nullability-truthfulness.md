---
id: type-nullability-truthfulness
title: "Honest Nullability and Avoiding False Non-Null Assertions"
category: nullability
priority: HIGH
triggers: [false-non-null-assertion, hidden-null-pointer, unhandled-null-case, defensive-null-check-on-non-null]
tags: [type-safety, nullability, null-safety, defensive-checks]
---

# Honest Nullability and Avoiding False Non-Null Assertions

**Trigger Anchor:** Explicitly mark types nullable (`?Type`) when null is reachable; handle null branches explicitly; avoid suppressing static analysis with false non-null assertions without runtime checks.

---

### Bad
```php
class UserRepository
{
    // ❌ Dishonest return contract claiming non-null User when not found
    public function getById(int $id): User
    {
        $row = $this->db->find($id);
        if ($row === null) {
            // Returns null despite signature claiming User! Causes Fatal TypeError at caller
            return null; // @phpstan-ignore-line (false assertion hiding bug)
        }
        return new User($row);
    }
}

// ❌ Caller blindly calls method on nullable return without check
$user = $userRepository->findNullable($id);
echo $user->getName(); // Fatal Error: Call to a member function getName() on null
```

### Good
```php
class UserRepository
{
    // ✅ Honest nullable contract
    public function findById(int $id): ?User
    {
        $row = $this->db->find($id);
        return $row !== null ? new User($row) : null;
    }

    // ✅ Explicit OrThrow variant for callers requiring non-null
    public function getByIdOrThrow(int $id): User
    {
        $user = $this->findById($id);
        if ($user === null) {
            throw new UserNotFoundException(sprintf('User %d does not exist.', $id));
        }
        return $user;
    }
}

// ✅ Safe consumption with nullsafe operator or explicit guard
$user = $userRepository->findById($id);
$name = $user?->getName() ?? 'Guest';
```
