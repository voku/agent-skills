---
id: arch-separation-domain-presentation
title: "Separation of Concerns: Domain Logic vs View and Controller Boundaries"
category: boundaries
priority: CRITICAL
triggers: [fat-controller-business-logic, sql-in-template-view, request-input-in-domain, smarty-php-logic-coupling]
tags: [architecture, separation-of-concerns, domain-layer, controllers, views]
---

# Separation of Concerns: Domain Logic vs View and Controller Boundaries

**Trigger Anchor:** Keep business calculation, state mutation, and database queries in dedicated domain services/repositories; keep HTTP controllers thin (request parsing and response formatting only) and templates pure (display branching only).

---

### Bad
```php
// ❌ Business logic and raw SQL embedded directly in controller
class InvoiceController extends Controller
{
    public function store(Request $request): Response
    {
        // Controller directly validates business rules, computes taxes, executes queries
        $items = $request->input('items');
        $subtotal = 0;
        foreach ($items as $item) {
            $subtotal += $item['qty'] * $item['price'];
        }
        $tax = $subtotal * 0.19; // Domain logic leaked into controller!
        
        DB::insert('INSERT INTO invoices ...', [$subtotal, $tax]);
        
        return view('invoice.created');
    }
}

// ❌ SQL queries or heavy data aggregation embedded in template files
// In template: {foreach from=InvoiceModel::fetchAllUnpaid() item=inv}
```

### Good
```php
// ✅ Thin controller orchestrating validated input, domain service, and presentation
class InvoiceController extends Controller
{
    public function __construct(
        private readonly CreateInvoiceService $invoiceService,
    ) {}

    public function store(StoreInvoiceRequest $request): JsonResponse
    {
        $dto = InvoiceCreationDTO::fromRequest($request);
        $invoice = $this->invoiceService->createInvoice($dto);

        return response()->json(new InvoiceResource($invoice), 201);
    }
}

// ✅ Encapsulated domain service owning pricing, tax, and persistence
class CreateInvoiceService
{
    public function createInvoice(InvoiceCreationDTO $dto): Invoice
    {
        $tax = $this->taxCalculator->calculate($dto->subtotal, $dto->countryCode);
        return $this->invoiceRepository->save($dto, $tax);
    }
}
```
