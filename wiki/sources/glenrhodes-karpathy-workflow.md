---
title: "Source: Andrej Karpathy's LLM-Powered Knowledge Base Workflow"
type: source-summary
source: "[[raw/glenrhodes-karpathy-workflow]]"
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/wiki-compilation]]", "[[concepts/llm-qa-over-documents]]", "[[concepts/hallucination-contamination]]"]
last_compiled: 2026-04-05
summary: "Technical walkthrough of Karpathy's workflow emphasizing the 'filing loop' where query results compound the knowledge base, and the product gap for non-technical users."
---

## Key Points
- The **filing loop**: query results get written back into the wiki — "his explorations accumulate, the knowledge base grows from use"
- At ~100 articles / 400K words, LLMs can maintain indexes and read comprehensively within context windows
- Current implementation is "a hacky collection of scripts" — significant product opportunity for polished tooling
- LLM health checks actively scan for inconsistencies and fill gaps via web search
- Synthetic data generation / fine-tuning is the future direction

## Detailed Summary

Glen Rhodes' walkthrough emphasizes the compounding nature of the system as its defining feature. Unlike traditional knowledge management tools where notes sit inert, Karpathy's system creates a feedback loop: every question asked enriches the knowledge base with a new filed answer. This transforms the wiki from a static repository into a living, growing resource.

The article identifies a key product gap: the current workflow requires significant technical expertise (CLI tooling, LLM API configuration, Obsidian customization). Karpathy himself acknowledges this as a "hacky collection of scripts," signaling opportunity for productized tooling.

The system architecture is straightforward: raw sources → LLM compilation → markdown wiki → Obsidian viewer → LLM Q&A → filed answers back to wiki.

## Notable Quotes
> "His explorations accumulate. The knowledge base grows from use."

## Related Concepts
- [[concepts/llm-knowledge-base]] — the system
- [[concepts/wiki-compilation]] — compilation process
- [[concepts/llm-qa-over-documents]] — query/answer loop
- [[concepts/hallucination-contamination]] — key risk
- [[concepts/knowledge-base-product-gap]] — the product opportunity
