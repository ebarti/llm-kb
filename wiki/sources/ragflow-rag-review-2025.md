---
title: "Source: From RAG to Context — A 2025 Year-End Review"
type: source-summary
source: "[[raw/ragflow-rag-review-2025]]"
related: ["[[concepts/retrieval-augmented-generation]]", "[[concepts/context-engineering]]", "[[concepts/hybrid-search]]", "[[concepts/multimodal-rag]]", "[[entities/ragflow]]"]
last_compiled: 2026-04-05
summary: "RAGFlow's year-end review arguing RAG is evolving from a retrieval pattern into a Context Engine — combining domain knowledge, tool retrieval, and memory into unified context platforms."
reading_time: "2 min"
---

## Key Points

- RAG solidified as "a cornerstone of data infrastructure" in enterprise AI during 2025, contrary to predictions of obsolescence
- Long context windows do not replace RAG — they complement it via "retrieval-first, long-context containment"
- TreeRAG decouples search and retrieval into different text granularities, addressing the "Lost in the Middle" problem
- [[concepts/graphrag]] showed promise but revealed challenges: massive token consumption, quality gaps in extraction
- RAG is evolving into a **Context Engine** serving three data categories: domain knowledge, tool data, and conversation state
- [[concepts/multimodal-rag]] stalled due to storage costs (512KB per page image with ColPali)
- 85% of production LLM applications now incorporate RAG (up from 30% in early 2024)

## Detailed Summary

The RAGFlow team's comprehensive 2025 review charts RAG's transformation from a simple retriever-generator pipeline into a sophisticated enterprise intelligence architecture. The article identifies four approaches to knowledge provision with roughly 100x cost differences between them, from full RAG to simple grep-based search.

A central thesis is that RAG's core capability — intelligent retrieval — is becoming the foundation for a broader discipline called [[concepts/context-engineering]]. Rather than being replaced by [[concepts/multi-agent-systems]], RAG provides the "fuel" that agents need to make good decisions. The article introduces a three-layered context model: domain knowledge (traditional RAG), tool retrieval (selecting which APIs/tools to use from hundreds of options), and conversation state (memory management).

The review also covers practical challenges with [[concepts/graphrag]], noting that while the approach is promising for relational discovery, real-world implementations consume several to dozens of times the original text in tokens, and extraction quality often falls short of expectations.

## Notable Quotes

> "No matter how intelligent an Agent is, the quality of its decisions and actions fundamentally depends on the quality and relevance of the Context it receives."

> RAG is "undergoing its own profound metamorphosis, evolving from the specific pattern of 'Retrieval-Augmented Generation' into a 'Context Engine' with 'intelligent retrieval' as its core capability."

## Related Concepts

- [[concepts/retrieval-augmented-generation]] — the core topic
- [[concepts/context-engineering]] — RAG's evolutionary destination
- [[concepts/hybrid-search]] — combining retrieval strategies
- [[concepts/multimodal-rag]] — extending beyond text
- [[concepts/graphrag]] — graph-based RAG variant discussed
