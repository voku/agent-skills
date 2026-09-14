# Rule Sections

## Priority Levels

| Level | Description | When to Apply |
|-------|-------------|---------------|
| CRITICAL | Role-based locators, strict-mode disambiguation, and web-first assertions | Every spec, locator, and assertion |
| HIGH | Global authentication state and controlled form/input interactions | Auth setup, forms, checkboxes, and date pickers |

## Section Overview

### 1. Accessible Locators (`locators`)
- **Impact:** CRITICAL
- **Rules:** `pw-locators-strict-mode`
- **Description:** Role and label locators matching user perception; resolving strict-mode multi-match errors.

### 2. Web-First Assertions (`assertions`)
- **Impact:** CRITICAL
- **Rules:** `pw-web-first-assertions`
- **Description:** Auto-retrying assertions (`await expect(locator).toBeVisible()`); zero arbitrary `waitForTimeout` sleeps.

### 3. Authenticated Sessions (`authentication`)
- **Impact:** HIGH
- **Rules:** `pw-auth-storage-state`
- **Description:** Single authentication setup saving storageState JSON; instant authenticated contexts across test workers.

### 4. Controlled Forms & Inputs (`forms`)
- **Impact:** HIGH
- **Rules:** `pw-form-interactions-custom-inputs`
- **Description:** Controlled React inputs, custom hidden checkboxes, and reliable date picker entry.
