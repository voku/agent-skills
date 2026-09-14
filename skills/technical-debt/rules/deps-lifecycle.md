---
id: deps-lifecycle
title: "Dependency Debt: CVEs, Outdated Versions, and Abandoned Packages"
category: deps
priority: HIGH
triggers: [vulnerable-dependency, outdated-dependency, abandoned-package, unused-dependency]
tags: [dependencies, composer, npm, cve, security-advisories]
---

# Dependency Debt: CVEs, Outdated Versions, and Abandoned Packages

**Trigger Anchor:** Audit dependencies for known CVEs (`composer audit`, `npm audit`), replace abandoned packages (>24 months without updates), prune unused dependencies (`knip`, `composer-unused`), and keep packages within 2 major versions of current stable.

---

### Bad
```json
// ❌ Pinned ancient versions with known critical vulnerabilities, abandoned libraries, and unused bloat
{
  "require": {
    "php": "^7.4",
    "abandoned/old-pdf-generator": "dev-master",
    "guzzlehttp/guzzle": "6.2.0",
    "unused/large-analytics-sdk": "^1.0"
  }
}
```

```bash
# ❌ Ignoring critical vulnerability reports in CI
$ composer audit
Found 4 vulnerabilities in 2 packages:
- CVE-2022-31160 (Critical): Guzzle improper header parsing
- CVE-2021-32708 (High): Arbitrary file overwrite
CI step continued with --ignore-platform-reqs / audit skipped
```

### Good
```json
// ✅ Modern supported versions, active maintenance, and exact constraints
{
  "require": {
    "php": "^8.3",
    "guzzlehttp/guzzle": "^7.8"
  },
  "config": {
    "audit": {
      "abandoned": "fail"
    }
  }
}
```

```bash
# ✅ Continuous automated audit in CI fail-closed pipeline
$ composer audit --locked
No security vulnerability advisories found.

$ npm audit --audit-level=high
found 0 vulnerabilities
```
