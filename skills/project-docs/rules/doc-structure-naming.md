---
id: doc-structure-naming
title: "Documentation Structure and Naming: Root Files, docs/ Hierarchy, and ADRs"
category: structure
priority: CRITICAL
triggers: [doc-structure-setup, markdown-naming-conventions, adr-file-naming, docs-subfolder-organization]
tags: [docs, structure, naming, adr, root-files, markdown]
---

# Documentation Structure and Naming: Root Files, docs/ Hierarchy, and ADRs

**Trigger Anchor:** Restrict root files to standard uppercase documents (`README.md`, `CHANGELOG.md`, `LICENSE`, `CONTRIBUTING.md`), organize long-term documentation under `docs/` using kebab-case subfolders, and prefix Architecture Decision Records with sequential numbers (`docs/adr/0001-decision.md`).

---

### Bad
```
# ❌ Cluttered root, inconsistent casing, dates in filenames, and version suffixes
.
├── Readme.md                       # Inconsistent casing
├── MyArchitectureNotes.md          # Personal thoughts in repo root
├── PLAN-2026-03.md                 # Ephemeral transient state committed to root
├── docs/
│   ├── Architecture/Overview.md    # PascalCase in docs subfolder
│   ├── deployment-guide-v2-final.md # "v2-final" anti-pattern
│   └── adr-database.md             # Unnumbered ADR without sequential prefix
```

### Good
```
# ✅ Standardized repository documentation layout
.
├── README.md                       # Canonical entry point
├── CHANGELOG.md                    # Release history
├── LICENSE                         # Legal license text
├── CONTRIBUTING.md                 # Contributor guidelines
├── SECURITY.md                     # Vulnerability reporting process
└── docs/
    ├── architecture/
    │   ├── overview.md             # High-level system design
    │   └── data-model.md           # Database relationships & boundaries
    ├── adr/
    │   ├── 0001-record-architecture-decisions.md
    │   ├── 0002-adopt-postgresql-and-pgvector.md
    │   └── 0003-use-inertia-react-frontend.md
    ├── guides/
    │   ├── local-development.md    # Environment bootstrap & seeding
    │   └── deployment.md           # Production deployment steps
    ├── runbooks/
    │   └── incident-response.md    # On-call triage procedures
    └── archive/
        └── 2025/
            └── legacy-v1-migration.md
```
