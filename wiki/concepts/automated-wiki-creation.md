---
title: "Automated Wiki Creation"
type: concept
sources: ["[[sources/storm-automated-wiki-creation]]", "[[sources/reeves-automated-wikipedia-content-review]]"]
related: ["[[concepts/wiki-compilation]]", "[[concepts/llm-knowledge-base]]", "[[concepts/multi-agent-systems]]", "[[concepts/wikipedia-knowledge-model]]", "[[concepts/ai-generated-content-risks]]", "[[concepts/collaborative-knowledge-building]]"]
last_compiled: 2026-04-05
summary: "STORM's approach: single-shot, multi-perspective Wikipedia-style article generation from web search using simulated expert conversations and outline-first synthesis — contrasting with Karpathy's incremental, accumulating KB model."
reading_time: "2 min"
---

## Overview

Automated wiki creation refers to systems that generate full structured articles from scratch, typically from web search or document corpora, without requiring human authoring. STORM is the primary research system; Karpathy's LLM-KB is the alternative persistent-KB model.

## STORM's Approach

**Core innovation**: Rather than retrieving and summarizing, STORM simulates the pre-writing research phase:
1. **Perspective discovery**: Analyze related Wikipedia ToCs to identify N distinct viewpoints on the topic
2. **Simulated expert conversations**: LLMs role-playing each perspective ask multi-turn questions, breaking down queries into searchable sub-questions
3. **Outline synthesis**: Refine a structured outline from the conversations before writing full content

**FreshWiki evaluation**: Dataset of recent Wikipedia articles created after LLM training cutoffs — ensures test articles couldn't have been memorized during training.

**Metrics**: Heading soft recall, entity recall (outline quality); ROUGE, entity recall (article quality); Wikipedia editor expert rubrics (interest, coherence, relevance, coverage, verifiability).

## STORM vs. Karpathy LLM-KB

| Dimension | STORM | Karpathy LLM-KB |
|-----------|-------|-----------------|
| Mode | Single-shot article generation | Persistent, accumulating KB |
| Input | Web search per topic | Curated raw/ sources |
| Output | One standalone article | Full wiki with cross-links |
| Compounding | None | Yes (filing loop) |
| Auditability | Source citations | raw/ provenance |
| Best for | Standalone reference articles | Research knowledge synthesis |

## Sources
- [[sources/storm-automated-wiki-creation]] — full STORM description and evaluation

## Related Concepts
- [[concepts/wiki-compilation]] — the persistent-KB counterpart
- [[concepts/llm-knowledge-base]] — the accumulating approach
- [[concepts/multi-agent-systems]] — multi-perspective agent architecture

## Related Entities

- [[entities/storm]] — the primary automated wiki creation system
- [[entities/freshwiki]] — evaluation dataset for STORM

## Related Comparisons

- [[comparisons/storm-vs-karpathy-workflow]] — single-shot vs. accumulating KB
- [[comparisons/single-agent-vs-multi-agent]] — agent architecture comparison
