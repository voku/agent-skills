---
id: prd-discovery-problem
title: "Product Discovery: Problem-First Framing, Clarifying Questions, and Codebase Grounding"
category: discovery
priority: CRITICAL
triggers: [prd-discovery-phase, clarifying-questions-product, problem-vs-solution-bias, codebase-exploration-spec]
tags: [prd, discovery, problem-statement, questions, exploration, alignment]
---

# Product Discovery: Problem-First Framing, Clarifying Questions, and Codebase Grounding

**Trigger Anchor:** Investigate the core customer problem before proposing solutions, explore existing codebase models and routes to establish baseline facts, and ask 3-5 targeted questions with lettered options to resolve unknowns.

---

### Bad
```markdown
<!-- ❌ Jumping straight to UI solution without understanding problem or checking codebase -->
# PRD: Add Export Button to Invoices

We need a blue "Export CSV" button in the top right corner of the invoice page that triggers a download.
```

### Good
```markdown
<!-- ✅ Grounded problem framing and targeted clarifying discovery -->
# Discovery: Bulk Invoice Accounting Reconciliation

## 1. Problem Framing
Finance managers currently spend 4.5 hours weekly manually copying invoice line items from our dashboard into NetSuite because individual invoice PDFs cannot be batch processed. This creates a 3-day reporting lag at month-end.

## 2. Existing Codebase Evidence
- **Model:** `App\Models\Invoice` has `hasMany(InvoiceItem::class)` with decimal currency values.
- **Route:** `GET /invoices` is paginated via Inertia React; no batch processing queue currently exists.
- **Auth:** `InvoicePolicy` already defines `export(User $user, Organization $org)` permissions.

## 3. Targeted Clarifying Questions
Before drafting the specification, please confirm:
1. **Target Format:**
   - [A] Standard generic CSV (comma-separated UTF-8)
   - [B] NetSuite-specific formatted CSV with GL account mapping
   - [C] QuickBooks Online IIF format
2. **Delivery Mechanism:**
   - [A] Instant streaming download in browser (<500 invoices)
   - [B] Asynchronous background job with email notification (>500 invoices)
```
