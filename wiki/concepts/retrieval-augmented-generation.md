---
title: "Retrieval-Augmented Generation (RAG)"
type: concept
sources: ["[[sources/ragflow-rag-review-2025]]", "[[sources/rag-vs-finetuning-agriculture]]", "[[sources/rag-hallucinations-explained]]", "[[sources/hybrid-search-rag-optimization]]", "[[sources/rag-evaluation-metrics-benchmarks]]", "[[sources/agentic-rag-survey]]"]
related: ["[[concepts/hybrid-search]]", "[[concepts/graphrag]]", "[[concepts/agentic-rag]]", "[[concepts/cache-augmented-generation]]", "[[concepts/fine-tuning]]", "[[concepts/rag-evaluation]]", "[[concepts/rag-hallucinations]]", "[[concepts/context-engineering]]"]
last_compiled: 2026-04-05
summary: "The dominant paradigm for grounding LLM outputs in external knowledge: retrieve relevant documents at query time, inject them as context, and generate answers — now evolving into modular, agentic context engines."
reading_time: "4 min"
---

## Overview

Retrieval-Augmented Generation (RAG) is the dominant paradigm for augmenting Large Language Models with external knowledge. First introduced by Lewis et al. (2020) at Facebook AI Research, RAG combines an information retrieval system with a generative language model: given a query, the system retrieves relevant documents from an external corpus, injects them into the LLM's context window as grounding material, and generates a response conditioned on both the query and the retrieved evidence.

As of early 2026, approximately 85% of production LLM applications incorporate RAG (up from ~30% in early 2024), making it the most widely deployed technique for knowledge-grounded generation. What began as a simple retriever-generator pipeline has matured into a sophisticated enterprise intelligence architecture with multimodal capabilities, [[concepts/hybrid-search]] engines, and advanced filtering layers.

## Core Architecture

The canonical RAG pipeline has three stages:

1. **Indexing (offline)**: Documents are chunked, embedded into vector representations, and stored in a [[concepts/vector-databases|vector database]] or search index. This stage may also include metadata extraction, keyword indexing for [[concepts/bm25]], and knowledge graph construction for [[concepts/graphrag]].

2. **Retrieval (online)**: Given a user query, the system encodes it and searches the index for the most relevant document chunks. Modern systems use [[concepts/hybrid-search]] combining dense vector similarity with sparse keyword matching, often followed by [[concepts/reranking]] with cross-encoders.

3. **Generation (online)**: Retrieved chunks are injected into the LLM's prompt as context. The model generates a response grounded in this evidence, ideally with citations.

## Evolution: From Naive to Agentic

RAG has evolved through distinct phases:

**Naive RAG** (2020-2023): Simple retrieve-then-generate pipeline. Fixed chunking, single-pass retrieval, no quality control on retrieved documents. Works for simple factual queries but fails on complex reasoning, holistic summarization, or multi-hop questions.

**Advanced RAG** (2023-2025): Introduced pre-retrieval optimization (query rewriting, expansion), post-retrieval refinement ([[concepts/reranking]], filtering), and improved chunking strategies (semantic chunking, adaptive chunking). Techniques like [[concepts/raptor]] add hierarchical summarization, while [[concepts/hybrid-search]] combines multiple retrieval strategies.

**Modular/Agentic RAG** (2025-present): The current frontier decomposes RAG into specialized, interchangeable modules — query planners, retrievers, re-rankers, generators — orchestrated by an [[concepts/agentic-rag|agentic controller]]. Systems like [[concepts/self-rag]] and [[concepts/corrective-rag]] add self-reflection loops that dynamically assess retrieval quality and retry or fall back to alternative sources.

## The Long Context Debate

A persistent question is whether expanding LLM context windows (now reaching 1M+ tokens) will make RAG obsolete. Research in 2025 demonstrated that this is not the case: simply feeding massive document batches into models causes attention scatter and "information flooding," degrading answer quality. The optimal approach is "retrieval-first, long-context containment" — use RAG to select relevant material, then leverage long context to hold more complete, coherent chunks. RAG and long context are complementary, not competing.

## RAG's Transformation into Context Engineering

According to the RAGFlow 2025 review, RAG is evolving from a specific retrieval-generation pattern into a broader discipline of [[concepts/context-engineering]]. Modern AI agents require three types of context: domain knowledge (traditional RAG), tool data (selecting which APIs to use from hundreds of options), and conversation state (memory management). RAG's retrieval infrastructure serves all three needs, positioning it as the foundation for a unified "Context Engine."

## Limitations

RAG is not a silver bullet. Key limitations include:

- **[[concepts/rag-hallucinations]]**: Even with retrieved context, models can ignore evidence, fuse documents incorrectly, or generate with unwarranted confidence. Stanford research found 17-33% hallucination rates in specialized legal RAG tools.
- **Retrieval failures**: Similarity-based retrieval misses holistic/aggregate queries ([[concepts/graphrag]] addresses this), exact keyword matches ([[concepts/hybrid-search]] addresses this), and multi-hop reasoning ([[concepts/raptor]] addresses this).
- **Computational cost**: Storing retrieved documents in memory, processing extended context, and running retrieval at query time all add latency and infrastructure costs.
- **Chunk boundary effects**: Fixed-size chunking fragments context. Semantic and adaptive chunking mitigate this but add complexity.

## Key Variants

| Variant | Innovation | See Also |
|---------|-----------|----------|
| [[concepts/graphrag]] | Knowledge graph + community summaries | [[sources/microsoft-graphrag]] |
| [[concepts/raptor]] | Hierarchical tree of recursive summaries | [[sources/raptor-tree-retrieval]] |
| [[concepts/agentic-rag]] | Agent-orchestrated retrieval with reflection | [[sources/agentic-rag-survey]] |
| [[concepts/self-rag]] | Reflection tokens for quality control | [[sources/self-reflective-rag-langgraph]] |
| [[concepts/corrective-rag]] | Web fallback on poor retrieval | [[sources/self-reflective-rag-langgraph]] |
| [[concepts/cache-augmented-generation]] | Preload all docs, skip retrieval | [[sources/cache-augmented-generation]] |
| [[concepts/multimodal-rag]] | Extend beyond text to images/tables | [[sources/ragflow-rag-review-2025]] |

## Sources

- [[sources/ragflow-rag-review-2025]] — comprehensive 2025 state-of-the-art review
- [[sources/rag-vs-finetuning-agriculture]] — empirical comparison with fine-tuning
- [[sources/rag-hallucinations-explained]] — failure modes and mitigation
- [[sources/hybrid-search-rag-optimization]] — retrieval optimization techniques
- [[sources/rag-evaluation-metrics-benchmarks]] — evaluation framework
- [[sources/agentic-rag-survey]] — taxonomy of agentic systems

## Related Concepts

- [[concepts/fine-tuning]] — complementary approach (behavior vs. facts)
- [[concepts/hybrid-search]] — modern retrieval combining sparse + dense
- [[concepts/rag-evaluation]] — how to measure RAG quality
- [[concepts/context-engineering]] — RAG's evolutionary destination
- [[concepts/rag-vs-index-based-retrieval]] — when simpler approaches suffice
- [[concepts/llm-knowledge-base]] — alternative paradigm bypassing traditional RAG
