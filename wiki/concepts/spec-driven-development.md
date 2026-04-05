---
title: "Spec-Driven Development"
type: concept
sources: ["[[sources/osmani-llm-coding-workflow-2026]]", "[[sources/redmonk-agentic-ides-2025]]"]
related: ["[[concepts/ai-pair-programming]]", "[[concepts/agentic-coding]]", "[[concepts/ai-coding-assistants]]", "[[concepts/developer-experience-ai]]"]
last_compiled: 2026-04-05
summary: "The practice of writing detailed specification documents (spec.md, requirements.md) before AI code generation — described as 'waterfall in 15 minutes' — eliminating 80% of AI confusion and serving as contracts between humans and agents."
---

## Overview

Spec-driven development is an emerging practice in AI-assisted workflows where developers create detailed specification documents before engaging AI tools for code generation. Rather than prompting AI ad hoc, developers invest upfront time in structured planning documents that serve as contracts between human intent and AI execution.

This practice has emerged independently across multiple practitioner reports as the single most effective technique for improving AI coding outcomes.

## The "Waterfall in 15 Minutes"

[[sources/osmani-llm-coding-workflow-2026]] describes the approach as achieving "waterfall in 15 minutes" — the structure and clarity of traditional waterfall planning, but generated rapidly with AI assistance. The spec typically includes:

- **Requirements:** What the feature should do, including edge cases
- **Architecture decisions:** How it fits into the existing system
- **Data models:** Schema changes, API contracts
- **Testing strategy:** What tests to write, what coverage to target
- **Constraints:** Performance requirements, backward compatibility, security considerations

Osmani estimates this single step eliminates **80% of "the AI got confused halfway through" moments.**

## Spec Files as Agent Contracts

[[sources/redmonk-agentic-ides-2025]] identifies spec-driven development as one of the 10 requirements developers demand from agentic IDEs. The files serve as:

1. **Input for agents:** requirements.md and design.md guide AI execution toward the correct solution
2. **Verification checkpoints:** As implementation evolves, the spec provides criteria for checking correctness
3. **Communication artifact:** The spec is the shared understanding between developer and AI, replacing the implicit understanding that human pairs develop naturally
4. **Audit trail:** The spec documents intent, making it possible to evaluate whether AI output matches the goal

## Implementation Patterns

### Pattern 1: AI-Assisted Spec Generation
1. Developer describes the feature in natural language
2. AI generates a structured spec with requirements, architecture, and edge cases
3. Developer reviews, refines, and approves
4. Approved spec is fed to the coding agent as the implementation guide

### Pattern 2: Prompt Plans
Osmani describes generating a structured "prompt plan" — a sequence of prompts for each sub-task — that tools like Cursor can execute sequentially. This breaks the spec into atomic implementation steps.

### Pattern 3: CLAUDE.md / GEMINI.md Convention
Project-level files (CLAUDE.md, GEMINI.md, .cursorrules) encode persistent specifications: coding conventions, architectural patterns, testing requirements, and workflow rules. These provide ongoing context that survives across sessions.

## Why It Works

Spec-driven development addresses the fundamental challenge of AI coding: **context transfer.** LLMs have no memory of your project's history, constraints, or conventions unless you explicitly provide it. A spec file concentrates all this context into a single artifact the AI can consume.

Without a spec, developers communicate intent through iterative prompting — a lossy, time-consuming process where misunderstandings compound across interactions. With a spec, the AI starts with a complete picture of what's needed.

## Connection to Testing

[[sources/osmani-llm-coding-workflow-2026]] notes that specs should include testing strategy. This creates a virtuous cycle: the spec defines acceptance criteria, the AI generates tests from those criteria, and the tests validate the implementation. "Those who get the most out of coding agents tend to be those with strong testing practices."

## Sources

- [[sources/osmani-llm-coding-workflow-2026]] — The "waterfall in 15 minutes" framework
- [[sources/redmonk-agentic-ides-2025]] — Spec-driven development as agentic IDE requirement #6

## Related Concepts

- [[concepts/ai-pair-programming]] — Spec-driven development is the communication layer for pair programming
- [[concepts/agentic-coding]] — Specs serve as contracts for autonomous agent execution
- [[concepts/ai-coding-assistants]] — The tools that consume specs
- [[concepts/developer-experience-ai]] — How specs improve the developer's experience with AI
