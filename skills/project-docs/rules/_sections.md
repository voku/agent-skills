# Rule Sections

## Priority Levels

| Level | Description | When to Apply |
|-------|-------------|---------------|
| CRITICAL | Structural conventions and baseline documentation | Always |
| HIGH | Content quality, anti-slop, and hygiene | Writing and auditing |
| MEDIUM | Long-term decision tracking & freshness | Ongoing maintenance |

## Section Overview

### 1. Structure & Naming (`structure`)
- **Impact:** CRITICAL
- **Rules:** `doc-structure-naming`
- **Description:** Root file conventions (`README.md`, `CHANGELOG.md`), kebab-case `docs/` hierarchy (`architecture/`, `adr/`, `guides/`), and sequential ADR file numbering.

### 2. Essential Repository Files (`essential`)
- **Impact:** CRITICAL
- **Rules:** `doc-essential-baseline`
- **Description:** Core baseline documents: comprehensive `README.md`, Keep-a-Changelog standard `CHANGELOG.md`, `LICENSE`, `CONTRIBUTING.md`, and `SECURITY.md`.

### 3. Markdown Quality & Anti-Slop (`quality`)
- **Impact:** HIGH
- **Rules:** `doc-markdown-quality-anti-slop`
- **Description:** Removing AI filler and sign-offs, sequential heading levels (`h1`->`h2`), explicit syntax highlighting on code blocks, and descriptive internal markdown links.

### 4. Hygiene & Cleanup (`cleanup`)
- **Impact:** HIGH
- **Rules:** `doc-hygiene-cleanup`
- **Description:** Eliminating transient AI plan files (`PLAN.md`, `TODO.md`), removing duplicate documentation, purging placeholder stubs, and archiving to `docs/archive/<year>/`.

### 5. Lifecycle & Freshness (`lifecycle`)
- **Impact:** MEDIUM
- **Rules:** `doc-lifecycle-adr-freshness`
- **Description:** Architecture Decision Record (MADR) status lifecycles, "Last Verified" accuracy timestamps on system designs, and PR-synchronized changelog discipline.
