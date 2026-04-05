---
title: "Source: Context Compression and Summarization Techniques"
type: source-summary
source: "[[raw/context-compression-techniques]]"
related: ["[[concepts/context-compression]]", "[[concepts/context-engineering]]", "[[concepts/context-windows]]"]
last_compiled: 2026-04-05
summary: "Comprehensive survey of compression techniques: hard prompts (LLMLingua, 20x), soft prompts (480x), hierarchical summarization, adaptive compression (83% reduction at 100 messages), and structured pruning (Provence, 95%)."
---

## Key Points

- Combined techniques achieve **50-80% token reduction** while preserving information quality
- **LLMLingua**: Up to 20x prompt compression using small models for token ranking
- **Soft prompt methods**: Up to 480x compression ratio (but model-specific, requires training)
- **Provence**: Up to 95% compression with structured priority-based pruning
- Adaptive compression: 83% reduction at 100 messages in long-running interactions
- Six practical techniques: truncation, model routing, memory buffering, hierarchical summarization, KG-based compression, RAG

## Detailed Summary

Context compression is the bridge between the information you need and the context window you have. This compilation covers the full spectrum from simple truncation to sophisticated learned compression.

**Hard prompt methods** work at the token level: SelectiveContext filters low-information tokens, LLMLingua uses small language models to rank token importance, and LongLLMLingua extends this to document-level compression. These are practical and model-agnostic but limited to ~20x compression.

**Soft prompt methods** achieve much higher ratios (up to 480x) by encoding prompts into continuous embeddings, but they require training and are tied to specific models.

**Structured approaches** like Provence treat context as objects with priority levels (always-keep, prune-old, prune-low-relevance, prune-superseded), achieving up to 95% compression. This maps directly to how [[concepts/llm-knowledge-base]] systems should manage their context: system instructions are always-keep, article summaries are medium-priority, and full article text is loaded on demand.

## Related Concepts

- [[concepts/context-compression]] — the core technique surveyed
- [[concepts/context-engineering]] — compression is a key tool in context engineering
- [[concepts/context-windows]] — compression extends effective context capacity
- [[concepts/hierarchical-memory]] — hierarchical summarization relates to memory hierarchy design
