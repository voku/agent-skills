# Rule Sections

## Priority Levels

| Level | Description | When to Apply |
|-------|-------------|---------------|
| CRITICAL | Discovery grounding and document structure | Beginning of feature planning |
| HIGH | Requirements, testable criteria, and scope boundaries | Spec drafting |
| MEDIUM | Technical contracts and sign-off review | Pre-engineering lock |

## Section Overview

### 1. Discovery (`discovery`)
- **Impact:** CRITICAL
- **Rules:** `prd-discovery-problem`
- **Description:** Grounding the feature in real user problems, exploring existing codebase architecture before drafting, and asking targeted clarifying questions.

### 2. Document Structure (`structure`)
- **Impact:** CRITICAL
- **Rules:** `prd-structure-template`
- **Description:** Single source of truth stored at `docs/prd/{feature-name}.md` with frontmatter, executive summary, and complete 12-section layout.

### 3. Requirements & Criteria (`requirements`)
- **Impact:** HIGH
- **Rules:** `prd-requirements-criteria`
- **Description:** Persona-driven user stories, numbered functional requirements (`FR-1`), performance NFRs, and Gherkin (`Given/When/Then`) acceptance criteria.

### 4. Scope & Metrics (`scope`)
- **Impact:** HIGH
- **Rules:** `prd-scope-metrics`
- **Description:** Guarding delivery timelines with explicit "Out of Scope" and "Non-Goals", risk mitigation registers, and quantifiable KPIs replacing vague buzzwords.

### 5. Technical Specifications & Review (`technical`)
- **Impact:** MEDIUM
- **Rules:** `prd-technical-review`
- **Description:** High-level entity data models, authorization scopes, API endpoint contracts, and stakeholder sign-off review workflows.
