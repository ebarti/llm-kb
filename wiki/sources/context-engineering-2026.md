---
title: "Source: Context Engineering — The Emerging Discipline (2025-2026)"
type: source-summary
source: "[[raw/context-engineering-2026]]"
related: ["[[concepts/context-engineering]]", "[[concepts/context-compression]]", "[[concepts/context-windows]]", "[[concepts/llm-knowledge-base]]"]
last_compiled: 2026-04-05
summary: "Context engineering as the successor to prompt engineering: managing everything the model sees during inference — structured context objects, ACE framework, three dimensions (collection, management, usage)."
---

## Key Points

- Term credited to Andrej Karpathy (2024-2025); Gartner declared "prompt engineering is out, context engineering is in"
- Context engineering manages everything during inference: prompts, documents, memory, tools, state, caching
- **ACE (Agentic Context Engineering)**: Structured itemized bullets, evolving playbooks, modular generation/reflection/curation
- Three dimensions: collection & storage, management, usage
- 2026 stack: LlamaIndex for data structuring + LangGraph for agent orchestration

## Detailed Summary

Context engineering represents a maturation of the field beyond "prompt engineering." Where prompt engineering focused on crafting individual prompts, context engineering is a systems discipline that manages the entire information environment surrounding an LLM during inference.

The key shift is treating context as a structured object rather than a growing text buffer. Each element gets tagged with its function (goal, decision, action, error), priority, source, and confidence. This enables automated management — pruning low-priority elements, refreshing stale data, and maintaining a coherent information environment.

The ACE (Agentic Context Engineering) framework treats contexts as evolving playbooks that agents maintain through generation, reflection, and curation cycles. This maps remarkably well to the [[concepts/llm-knowledge-base]] workflow: raw ingestion (generation), wiki compilation (reflection), and linting/health checks (curation).

For wiki systems specifically, context engineering explains why the summaries-based navigation approach works: it is a structured context management system where the LLM loads only what it needs (selective retrieval), maintains hierarchical organization (summaries → articles → raw sources), and keeps the context focused on the current query.

## Related Concepts

- [[concepts/context-engineering]] — the core discipline described
- [[concepts/llm-knowledge-base]] — the wiki approach is a context engineering system
- [[concepts/context-compression]] — a key tool within context engineering
- [[concepts/context-windows]] — the constraint that motivates context engineering
- [[concepts/post-code-ai-workflow]] — Karpathy originated both the KB workflow and the context engineering term
