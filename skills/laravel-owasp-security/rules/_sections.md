# Rule Sections

## Priority Levels

| Level | Description | When to Apply |
|-------|-------------|---------------|
| CRITICAL | Inertia prop exposure, broken access control, and injection prevention | Controller responses, route definitions, and persistence |
| HIGH | Authentication rate limiting, session fixation, and production cryptography | Auth routes, middleware pipelines, and environment config |

## Section Overview

### 1. Inertia Prop Data Exposure (`inertia-security`)
- **Impact:** CRITICAL
- **Rules:** `sec-inertia-data-exposure`
- **Description:** Preventing raw Eloquent models and secret keys from leaking into the public HTML data-page attribute.

### 2. Access Control & IDOR (`access-control`)
- **Impact:** CRITICAL
- **Rules:** `sec-access-control-idor`
- **Description:** Server-side Policy/Gate authorization and tenant-scoped queries instead of client-only UI hiding.

### 3. Injection & Mass Assignment (`injection`)
- **Impact:** CRITICAL
- **Rules:** `sec-injection-mass-assignment`
- **Description:** Parameterized bindings in raw SQL, Form Request validation for mass-assignment, and process isolation.

### 4. Authentication & Rate Limiting (`authentication`)
- **Impact:** HIGH
- **Rules:** `sec-authentication-rate-limiting`
- **Description:** Throttle middleware on auth endpoints, session regeneration on login, and strong password validation.

### 5. Cryptography & Configuration (`configuration`)
- **Impact:** HIGH
- **Rules:** `sec-cryptography-headers-config`
- **Description:** Hashed casts, scoped CSRF exemptions, DOMPurify for dangerous HTML, and production security settings.
