---
id: err-outcome-batch-discipline
title: "Outcome Messaging and Batch Aggregation Discipline"
category: messaging
priority: HIGH
triggers: [premature-success-message, silent-else-trap, batch-partial-failure, duplicate-outcome-notification, misleading-error-branch]
tags: [error-handling, messaging, batch-processing, outcome, user-feedback, silent-else]
---

# Outcome Messaging and Batch Aggregation Discipline

**Trigger Anchor:** Surface exactly one honest outcome per reachable branch, track accumulated status (`$allSuccess`) before reporting batch success, and avoid silent early returns or missing else branches on guarded self-reporting callees.

---

### Bad
```php
// ❌ Reporting unconditional success despite loop failures
$failedCount = 0;
foreach ($items as $item) {
    if (!$processor->process($item)) {
        $failedCount++;
    }
}
// Misleading: user is told all items succeeded even when failures occurred
$notifier->notifySuccess('All items processed successfully.');

// ❌ Silent else trap: skipping self-reporting callee leaves UI blank (white page)
if ($targetUser !== null) {
    // Callee renders its own view / outcome message
    renderUserDetails($view, $targetUser);
}
// If $targetUser is null, code falls through with NO message or template rendered!

// ❌ Misleading combined error message for distinct conditions
if ($account === null || $account->isLocked()) {
    throw new UserException('Account not found'); // Misleading when account exists but is locked!
}
```

### Good
```php
// ✅ Track batch outcome and provide honest aggregate reporting
$allSuccess = true;
$failedItems = [];
foreach ($items as $item) {
    if (!$processor->process($item)) {
        $allSuccess = false;
        $failedItems[] = $item->id;
    }
}
if ($allSuccess) {
    $notifier->notifySuccess(sprintf('All %d items processed successfully.', count($items)));
} else {
    $notifier->notifyWarning(sprintf('%d items succeeded, %d failed: %s', count($items) - count($failedItems), count($failedItems), implode(', ', $failedItems)));
}

// ✅ Explicit else branch when callee is guarded
if ($targetUser !== null) {
    renderUserDetails($view, $targetUser);
} else {
    $view->renderError('User not found or access denied.');
}

// ✅ Distinct honest messaging per branch
if ($account === null) {
    throw new UserNotFoundException('Account does not exist.');
}
if ($account->isLocked()) {
    throw new AccountLockedException('Account is locked due to too many failed attempts.');
}
```
