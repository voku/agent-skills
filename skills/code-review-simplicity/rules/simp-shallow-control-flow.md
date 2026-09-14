---
id: simp-shallow-control-flow
title: "Shallow Control Flow and Guard Clauses Over Arrow Anti-Patterns"
category: cognitive-load
priority: HIGH
triggers: [deep-nesting-arrow, nested-if-else, boolean-flag-parameter, cognitive-load-cyclomatic]
tags: [simplicity, guard-clauses, cyclomatic-complexity, cognitive-load, early-return]
---

# Shallow Control Flow and Guard Clauses Over Arrow Anti-Patterns

**Trigger Anchor:** Flatten nested `if`/`else` pyramids using early return guard clauses, decompose multi-condition boolean expressions into descriptive variables or methods, and avoid boolean flag arguments that control two different functions in one.

---

### Bad
```php
// ❌ Deeply nested arrow anti-pattern with high cognitive load
function processOrder(?Order $order, ?User $user): bool
{
    if ($user !== null) {
        if ($user->isActive()) {
            if ($order !== null) {
                if ($order->hasItems()) {
                    if ($order->getTotal() > 0) {
                        return $this->submitPayment($order);
                    } else {
                        return false;
                    }
                } else {
                    return false;
                }
            } else {
                return false;
            }
        } else {
            return false;
        }
    } else {
        return false;
    }
}

// ❌ Boolean flag argument controlling two divergent functions
function savePost(Post $post, bool $isDraft): void
{
    if ($isDraft) {
        $post->status = 'draft';
        $post->published_at = null;
        $this->repo->saveDraft($post);
    } else {
        $post->status = 'published';
        $post->published_at = now();
        $this->repo->saveAndNotifySubscribers($post);
    }
}
```

### Good
```php
// ✅ Shallow control flow with early-exit guard clauses
function processOrder(?Order $order, ?User $user): bool
{
    if ($user === null || !$user->isActive()) {
        return false;
    }

    if ($order === null || !$order->hasItems() || $order->getTotal() <= 0) {
        return false;
    }

    return $this->submitPayment($order);
}

// ✅ Separate, intention-revealing methods instead of boolean flag parameters
function saveDraft(Post $post): void
{
    $post->status = 'draft';
    $post->published_at = null;
    $this->repo->saveDraft($post);
}

function publishPost(Post $post): void
{
    $post->status = 'published';
    $post->published_at = now();
    $this->repo->saveAndNotifySubscribers($post);
}
```
