---
id: simp-dead-code-elimination
title: "Dead Code, Unused Parameters, and Symmetric Consistency"
category: maintainability
priority: HIGH
triggers: [unreferenced-private-method, unused-parameter, commented-out-code, asymmetric-handling]
tags: [simplicity, dead-code, unused-variables, symmetry, clean-up]
---

# Dead Code, Unused Parameters, and Symmetric Consistency

**Trigger Anchor:** Delete unreferenced private methods, unused function parameters, commented-out code blocks, and obsolete feature flags instead of hoarding them; maintain symmetric handling across sibling branches.

---

### Bad
```php
class ReportGenerator
{
    // ❌ Unused parameter left behind after refactoring
    public function generateReport(int $tenantId, bool $legacyExport = false): Report
    {
        // ❌ Commented-out dead code retained "just in case"
        // if ($legacyExport) {
        //     return $this->buildOldReport($tenantId);
        // }

        return $this->buildModernReport($tenantId);
    }

    // ❌ Dead private method with zero callers anywhere in the codebase
    private function buildOldReport(int $tenantId): Report
    {
        // 45 lines of unmaintained legacy code
    }

    // ❌ Asymmetric handling of sibling branches
    public function formatUser(User $user, string $channel): string
    {
        if ($channel === 'slack') {
            return sprintf('*%s* (<%s>)', $user->getName(), $user->getEmail());
        }
        // Asymmetric: returns array encoded string in one branch, plain string in another
        return json_encode(['name' => $user->getName(), 'mail' => $user->getEmail()]);
    }
}
```

### Good
```php
class ReportGenerator
{
    // ✅ Clean signature without obsolete parameters or dead code blocks
    public function generateReport(int $tenantId): Report
    {
        return $this->buildModernReport($tenantId);
    }

    private function buildModernReport(int $tenantId): Report
    {
        return new Report($this->fetchReportData($tenantId));
    }

    // ✅ Consistent, symmetric format across sibling branches
    public function formatUser(User $user, string $channel): string
    {
        return match ($channel) {
            'slack' => sprintf('*%s* (<%s>)', $user->getName(), $user->getEmail()),
            'email' => sprintf('%s <%s>', $user->getName(), $user->getEmail()),
            default => sprintf('%s (%s)', $user->getName(), $user->getEmail()),
        };
    }
}
```
