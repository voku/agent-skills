---
id: prd-requirements-criteria
title: "Requirements Engineering: User Stories, Functional Specs, and Testable Criteria"
category: requirements
priority: HIGH
triggers: [user-story-acceptance-criteria, functional-requirements-spec, gherkin-criteria-given-when-then, non-functional-requirements]
tags: [prd, requirements, user-stories, acceptance-criteria, gherkin, testability]
---

# Requirements Engineering: User Stories, Functional Specs, and Testable Criteria

**Trigger Anchor:** Write user stories following "As a / I want / So that", assign unique IDs to functional requirements (`FR-1`), specify numeric non-functional targets, and formulate testable acceptance criteria using Gherkin (`Given / When / Then`).

---

### Bad
```markdown
<!-- ❌ Vague, untestable, non-verifiable requirements without clear persona or boundary -->
- The system should be fast and easy to use.
- Users should be able to download stuff.
- Error messages should be helpful.
```

### Good
```markdown
<!-- ✅ Precise, testable user stories and requirements -->
## User Stories & Acceptance Criteria

### US-1: Date-Filtered CSV Generation
**As a** Finance Manager  
**I want to** select a custom date range and download all paid invoices as a CSV  
**So that** I can import monthly receivables into our general ledger.

#### Acceptance Criteria (Gherkin)
- **Scenario:** Export under 250 invoices completes synchronously
  - **Given** I am an authenticated Organization Administrator
  - **And** there are 142 paid invoices in the selected date range
  - **When** I click "Export CSV"
  - **Then** the browser begins downloading the file within 2.5 seconds
  - **And** the file includes columns: `invoice_id`, `issue_date`, `due_date`, `total_amount`, `currency`, `tax_id`

- **Scenario:** Export over 250 invoices dispatches background queue
  - **Given** there are 1,200 paid invoices in the selected date range
  - **When** I click "Export CSV"
  - **Then** an in-app toast announces "Generating export in background, you will receive an email shortly"
  - **And** an encrypted temporary download link is sent to my verified email within 3 minutes

## Functional Requirements
- **FR-1:** Provide date range pickers restricted to maximum 12-month export windows.
- **FR-2:** Escape CSV injection characters (`=`, `+`, `-`, `@`) with prepended single quote `'`.

## Non-Functional Requirements
- **NFR-1 (Performance):** Synchronous exports (<250 records) must stream with TTFB < 800ms.
- **NFR-2 (Security):** Export links must expire after 4 hours and require valid tenant session cookies.
```
