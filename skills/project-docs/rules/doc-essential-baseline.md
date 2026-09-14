---
id: doc-essential-baseline
title: "Essential Repository Documents: README, CHANGELOG, LICENSE, and SECURITY"
category: essential
priority: CRITICAL
triggers: [readme-scaffolding, changelog-keep-a-changelog, license-file-setup, security-md-policy, contributing-guide]
tags: [docs, readme, changelog, license, security, contributing]
---

# Essential Repository Documents: README, CHANGELOG, LICENSE, and SECURITY

**Trigger Anchor:** Provide a complete `README.md` with installation, testing, and architecture overview, follow the Keep-a-Changelog standard for `CHANGELOG.md`, specify an SPDX `LICENSE`, and publish `SECURITY.md` with explicit vulnerability disclosure instructions.

---

### Bad
```markdown
<!-- ❌ README with missing prerequisites, un-copyable pseudo commands, and no license info -->
# My App
A cool web app.

## How to run
Install stuff and run npm start.
Contact me on Slack if anything breaks.
```

### Good
```markdown
<!-- ✅ README.md: Clear project overview, prerequisites, quickstart, and test commands -->
# Acme Portal

Secure client portal for managing enterprise cloud resources and billing.

## Requirements
- PHP 8.3+ with `pdo_pgsql`, `redis` extensions
- Node.js 20+ (LTS)
- PostgreSQL 16+ with `pgvector`

## Quickstart

```bash
# 1. Clone and install dependencies
git clone git@github.com:acme/portal.git && cd portal
composer install
npm install

# 2. Environment setup and database migration
cp .env.example .env
php artisan key:generate
php artisan migrate --seed

# 3. Start local development
npm run dev
php artisan serve
```

## Testing & Quality

```bash
composer test      # Pest test suite
composer phpstan   # Static analysis (level 8)
npm run lint       # ESLint & Prettier
```

## License
Licensed under the [MIT License](LICENSE).
```

```markdown
<!-- ✅ CHANGELOG.md: Keep a Changelog standard format -->
# Changelog

All notable changes to this project will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Real-time invoice extraction with Anthropic Claude Haiku.

### Fixed
- Prevented double-submission on billing checkout forms.

## [1.2.0] - 2026-02-15
### Added
- Full-text and vector search powered by PostgreSQL `pgvector`.
```
