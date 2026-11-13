# Code Review Type Safety — Agent Routing

This is a supporting agent projection. [SKILL.md](SKILL.md) defines the review lens, evidence requirements, handoffs, and terminal status contract. Detailed type-safety checks belong to the relevant files in [rules/](rules/).

Use this lens when a concrete change raises a type-contract concern. Load only the relevant canonical rules and report findings against inspected producer/consumer evidence. Do not invent missing evidence or duplicate the rule index here.
