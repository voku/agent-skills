# Code Review Architecture — Agent Routing

This file routes agents to the canonical [SKILL.md](SKILL.md) for scope, evidence discipline, handoffs, and the terminal status contract. Specialized checks are maintained in [rules/](rules/), not duplicated here.

Apply this lens when architecture or ownership boundary is the dominant review concern. Load only relevant rules and ground findings in real source, caller, and transaction-boundary evidence. Report missing evidence as blocked rather than guessing.
