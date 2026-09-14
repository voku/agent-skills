---
id: pest-organization
title: "Pest Organization: Describe Blocks, Hooks, and Datasets"
category: pest
priority: MEDIUM
triggers: [unorganized-test-file, duplicate-test-scenarios, missing-before-each-setup, pest-dataset-opportunity]
tags: [pest, testing, describe, beforeEach, with, datasets]
---

# Pest Organization: Describe Blocks, Hooks, and Datasets

**Trigger Anchor:** Group related tests inside `describe` blocks, isolate shared test setup in `beforeEach()`, and eliminate repetitive test cases with parameterised `->with([...])` datasets.

---

### Bad
```php
<?php

// ❌ 4 copy-pasted tests verifying the same validation logic with slightly different invalid emails
test('rejects invalid email 1', function () {
    $this->postJson('/api/register', ['email' => 'plainaddress'])->assertUnprocessable();
});

test('rejects invalid email 2', function () {
    $this->postJson('/api/register', ['email' => '@missingusername.com'])->assertUnprocessable();
});

test('rejects invalid email 3', function () {
    $this->postJson('/api/register', ['email' => 'missingdomain@.com'])->assertUnprocessable();
});
```

### Good
```php
<?php

declare(strict_types=1);

use App\Models\User;

describe('User Registration Endpoint', function () {
    beforeEach(function () {
        $this->endpoint = '/api/register';
    });

    test('successfully registers with valid data', function () {
        $this->postJson($this->endpoint, [
            'name' => 'Alice',
            'email' => 'alice@example.com',
            'password' => 'Password123!',
        ])->assertCreated();
    });

    // ✅ Parameterised dataset runs one test across all variations
    test('rejects malformed email formats', function (string $invalidEmail) {
        $this->postJson($this->endpoint, [
            'name' => 'Alice',
            'email' => $invalidEmail,
            'password' => 'Password123!',
        ])->assertJsonValidationErrors(['email']);
    })->with([
        'missing @' => 'plainaddress',
        'missing username' => '@missingusername.com',
        'missing domain' => 'missingdomain@.com',
        'two @@' => 'a@@b.com',
    ]);
});
```
