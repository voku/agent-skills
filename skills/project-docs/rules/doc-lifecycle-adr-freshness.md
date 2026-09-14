---
id: doc-lifecycle-adr-freshness
title: "Architecture Decision Records (ADR), Verification Dates, and Changelog Discipline"
category: lifecycle
priority: MEDIUM
triggers: [adr-creation-lifecycle, doc-freshness-verification, changelog-pr-discipline, adr-template]
tags: [docs, adr, lifecycle, freshness, changelog, architecture]
---

# Architecture Decision Records (ADR), Verification Dates, and Changelog Discipline

**Trigger Anchor:** Record irreversible technical decisions using MADR formatted records (`Proposed` -> `Accepted` -> `Superseded`), maintain explicit `Last Verified: YYYY-MM-DD` timestamps on architecture docs, and update `CHANGELOG.md` in the exact PR introducing the change.

---

### Bad
```markdown
<!-- ❌ Informal unversioned decision lost in Slack; stale docs with unknown accuracy -->
# Architecture Notes
We decided to switch from MySQL to PostgreSQL yesterday because of JSON support.
```

### Good
```markdown
<!-- ✅ docs/adr/0002-adopt-postgresql-and-pgvector.md: MADR Architecture Decision Record -->
# 0002. Adopt PostgreSQL and pgvector for Search and Storage

Date: 2026-02-10

## Status
Accepted (Supersedes [0001-initial-mysql-schema.md](0001-initial-mysql-schema.md))

## Context
We need high-performance vector similarity search for semantic documentation querying and RAG, alongside ACID transactional guarantees for tenant billing.

## Decision
We will migrate our primary datastore from MySQL 8 to PostgreSQL 16 with the `pgvector` extension enabled.

## Consequences
### Positive
- Unified transactional and vector search data model (no separate Pinecone/Qdrant cluster).
- Native support for cosine distance (`<=>`) operators in Laravel Eloquent queries.

### Negative
- Requires team onboarding for PostgreSQL query profiling and connection poolers (PgBouncer).
```

```markdown
<!-- ✅ docs/architecture/overview.md: Explicit verification header -->
# System Architecture Overview

> **Status:** Active  
> **Last Verified:** 2026-03-01 against Laravel 13 & PostgreSQL 16  
> **Owner:** Core Infrastructure Team
```
