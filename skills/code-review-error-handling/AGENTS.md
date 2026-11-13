# Code Review Error Handling — Agent Routing

This file routes agents to the canonical [SKILL.md](SKILL.md) for scope, evidence discipline, handoffs, and the terminal status contract. Specialized checks are maintained in [rules/](rules/), not duplicated here.

Apply this lens when failure handling or resilience is the dominant review concern. Load only relevant rules and ground findings in observed failure paths, retries, persistence, and cleanup. Report missing evidence as blocked rather than guessing.
