# Rule Sections

## Priority Levels

| Level | Description | When to Apply |
|-------|-------------|---------------|
| CRITICAL | Injection prevention and fail-closed authentication/authorization | Every untrusted input, persistence call, and identity lookup |
| HIGH | Contextual escaping, server-side selection re-validation, and secrets configuration | Rendering templates, dropdown forms, and infrastructure wiring |

## Section Overview

### 1. Injection Defense (`injection`)
- **Impact:** CRITICAL
- **Rules:** `sec-injection-defense`
- **Description:** Parameterized queries, process execution without shell interpolation, and path traversal boundary checks.

### 2. Authorization & Identity (`authorization`)
- **Impact:** CRITICAL
- **Rules:** `sec-auth-fail-closed`
- **Description:** Fail-closed authenticated user retrieval, tenant/organization query scoping, and server-side policy gate enforcement.

### 3. Escaping & Encoding (`data-protection`)
- **Impact:** HIGH
- **Rules:** `sec-sink-appropriate-escaping`
- **Description:** Storing clean raw strings in storage sinks; context-aware HTML escaping strictly at template output sinks.

### 4. Input Re-validation (`validation`)
- **Impact:** HIGH
- **Rules:** `sec-input-revalidation`
- **Description:** Server-side FK and status re-validation on dropdown submissions; mass-assignment guardrails.

### 5. Secrets & Configuration (`configuration`)
- **Impact:** HIGH
- **Rules:** `sec-secrets-configuration`
- **Description:** Environment-injected credentials, modern password hashing (Argon2id), and secure cookie flags (HttpOnly, Secure, SameSite).
