---
id: type-symmetric-rigor
title: "Symmetric Rigor Across Sibling Branches and Consumers"
category: asymmetric-rigor
priority: HIGH
triggers: [asymmetric-type-handling, half-migrated-types, inconsistent-nullability, mixed-return-branches]
tags: [type-safety, symmetry, nullability, consistency]
---

# Symmetric Rigor Across Sibling Branches and Consumers

**Trigger Anchor:** Enforce identical type rigor across all sibling branches; if one branch normalizes an empty string to `null`, all sibling branches must do the same; avoid methods where one branch returns a typed object and another returns an associative array or raw ID.

---

### Bad
```php
class CustomerResolver
{
    // ❌ Asymmetric return types across branches (mixed return types)
    public function resolve(string $identifier, string $type): mixed
    {
        if ($type === 'email') {
            return $this->userRepo->findByEmail($identifier); // Returns User object
        }

        if ($type === 'id') {
            return (int)$identifier; // Returns integer ID!
        }

        return ['raw' => $identifier]; // Returns array!
    }

    // ❌ Inconsistent null/empty string handling across sibling fields
    public function normalizeInput(array $data): array
    {
        $data['first_name'] = $data['first_name'] === '' ? null : trim($data['first_name']);
        // Asymmetric: last_name leaves empty string intact instead of normalizing to null
        $data['last_name'] = trim($data['last_name'] ?? '');
        return $data;
    }
}
```

### Good
```php
class CustomerResolver
{
    // ✅ Consistent typed return contract across all branches
    public function resolve(string $identifier, IdentifierType $type): ?User
    {
        return match ($type) {
            IdentifierType::Email => $this->userRepo->findByEmail($identifier),
            IdentifierType::Id    => $this->userRepo->findById((int)$identifier),
        };
    }

    // ✅ Symmetric normalization across all string attributes
    public function normalizeInput(array $data): array
    {
        foreach (['first_name', 'last_name', 'company'] as $field) {
            $value = isset($data[$field]) ? trim((string)$data[$field]) : '';
            $data[$field] = $value === '' ? null : $value;
        }
        return $data;
    }
}
```
