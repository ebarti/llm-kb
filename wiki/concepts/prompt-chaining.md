---
title: "Prompt Chaining"
type: concept
sources: ["[[sources/promptingguide-prompt-chaining]]", "[[sources/anthropic-claude-prompting-best-practices]]"]
related: ["[[concepts/prompt-engineering]]", "[[concepts/multi-agent-systems]]", "[[concepts/meta-prompting]]", "[[concepts/chain-of-thought-prompting]]"]
last_compiled: 2026-04-05
summary: "Decomposing complex tasks into sequential LLM calls where each output feeds the next — the foundational pattern for production LLM workflows, enabling transparency, controllability, and debugging."
---

## Overview

Prompt chaining is the engineering practice of splitting a complex task into a sequence of simpler LLM calls, where each call's output feeds into the next call's input. Rather than overloading a single prompt with all requirements, each step has a focused objective and well-defined input/output contract.

This is the foundational design pattern for production LLM applications. It underpins [[concepts/multi-agent-systems]], agentic workflows, and the compile/query/lint operations of this [[concepts/llm-knowledge-base]] system.

## Core Patterns

**Extraction → Synthesis**: The most common two-step chain:
1. Extract relevant information from a document (quotes, facts, entities)
2. Synthesize the extracted information into a final answer

**Self-Correction** (the most widely used pattern):
1. Generate a draft
2. Review the draft against criteria
3. Refine based on the review

**Progressive Refinement**:
1. Create an outline
2. Expand each section
3. Polish and integrate

## Key Benefits

| Benefit | Why It Matters |
|---------|---------------|
| **Transparency** | Each step's input/output is inspectable |
| **Controllability** | Can steer behavior at each stage |
| **Debuggability** | Pinpoint exactly where errors occur |
| **Reliability** | Simpler prompts have lower failure rates |
| **Flexibility** | Can swap, add, or remove steps independently |

## Implementation

Prompt chaining can be implemented at multiple levels of complexity:
- **Simple scripting**: Loop of API calls with string interpolation
- **Frameworks**: LangChain, LlamaIndex, or custom pipelines
- **Native model capabilities**: Claude 4.6 with adaptive thinking handles much multi-step reasoning internally
- **Agent frameworks**: Auto-delegation to subagents for parallel chains

Anthropic notes that with modern models, explicit chaining is mainly needed when you need to "inspect intermediate outputs or enforce a specific pipeline structure."

## Application to This KB

The KB system implicitly uses prompt chaining in its RESEARCH operation:
1. Search the web (multiple queries)
2. Fetch and clean each source
3. Save to raw/
4. Compile source summaries
5. Synthesize concept articles across sources
6. Update metadata and index

Each step could benefit from explicit chain design with quality checks between stages.

## Sources
- [[sources/promptingguide-prompt-chaining]] — Foundational overview
- [[sources/anthropic-claude-prompting-best-practices]] — Self-correction as the most common pattern

## Related Concepts
- [[concepts/prompt-engineering]] — parent domain
- [[concepts/multi-agent-systems]] — prompt chaining at scale
- [[concepts/meta-prompting]] — self-improving chains
- [[concepts/chain-of-thought-prompting]] — reasoning within a single prompt (internal chaining)
