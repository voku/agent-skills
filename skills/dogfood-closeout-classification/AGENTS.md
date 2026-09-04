# Dogfood Closeout Classification - Agent Guide

Refer to this skill at session closeout or when upstreaming fixes.

## Trigger Phrases
- "dogfood closeout"
- "closeout classification"
- "inference classification"
- "leak check public diffs"
- "session closeout"

## Core Workflow

1. **Scan for Inferences**: Locate any documented LLM inferences or workflow gaps.
2. **Classify**: Map every inference to its category (`docs_fix`, `skill_proposal`, etc.).
3. **Leak Check**: Execute private leak checks on the public repository checkouts.
4. **Environment Check**: Ensure all host-specific commands remain private.
