---
title: "Chunking Strategies"
type: concept
sources: ["[[sources/weaviate-chunking-strategies]]"]
related: ["[[concepts/text-embeddings]]", "[[concepts/vector-search]]", "[[concepts/two-stage-retrieval]]", "[[concepts/colbert-late-interaction]]"]
last_compiled: 2026-04-05
summary: "How text is split into segments for embedding and retrieval in RAG: from simple fixed-size splitting (512 tokens, 10-20% overlap) to semantic, hierarchical, and agentic approaches that align chunk boundaries with meaning."
---

## Overview

Chunking is the process of splitting documents into smaller segments for embedding and retrieval in RAG pipelines. The choice of chunking strategy directly impacts retrieval accuracy, answer quality, and computational cost. A poorly chunked document produces embeddings that mix unrelated topics or fragment coherent ideas, degrading [[concepts/vector-search]] quality.

The fundamental principle: **"If a chunk makes sense to you when read alone, it will make sense to the LLM too."**

## Strategy Spectrum

### Fixed-Size Chunking (Simplest)

Split text into predetermined sizes with optional overlap.

- **Baseline recommendation**: 512 tokens per chunk, 50-100 tokens overlap (10-20%)
- **Tradeoff**: Large chunks mix multiple topics; small chunks lose context at boundaries
- **Overlap**: Repeats content at chunk boundaries to reduce information loss
- **Best for**: Quick prototyping, unstructured data with inconsistent formatting

### Recursive Chunking

Apply hierarchical separators in priority order:
1. Double newlines (paragraph breaks)
2. Single newlines
3. Periods (sentence boundaries)
4. Spaces (word boundaries)

Attempt the highest-priority separator first; recursively apply the next for oversized chunks. Preserves document structure better than fixed-size.

**Best for**: Articles, blog posts, research papers.

### Document-Based Chunking

Leverage intrinsic document structure:
- **Markdown**: Split by heading levels (#, ##, ###)
- **HTML**: Split by semantic tags (`<section>`, `<article>`, `<p>`)
- **Code**: Split by functions, classes, or modules
- **PDF**: Requires preprocessing to Markdown first

**Best for**: Structured documents where formatting correlates with semantic boundaries.

### Semantic Chunking

1. Segment text into sentences
2. Embed each sentence
3. Compute pairwise similarity between adjacent sentences
4. Split where similarity drops below threshold (topic boundary)

Creates highly coherent chunks, each containing a self-contained idea. More computationally expensive.

**Best for**: Long-form content with natural topic transitions.

### Late Chunking (Jina AI, 2024)

Inverts the traditional "chunk then embed" pipeline:
1. Embed the entire document through the transformer (token-level)
2. Extract chunk-level representations from full-document embeddings

This preserves full document context within each chunk's embedding — references to earlier content are not lost. Requires a model that supports long input sequences.

### Advanced Strategies

- **Hierarchical**: Multiple chunk layers (sections, paragraphs, sentences) for different query granularities
- **LLM-Based**: Use a language model to identify propositions, summarize sections, or highlight key points (most expensive)
- **Agentic**: An AI agent dynamically selects the optimal strategy per document, potentially combining multiple approaches
- **Adaptive**: ML models analyze semantic density, creating smaller chunks for complex sections and larger for simpler content

## Chunk Size Selection Guide

| Use Case | Recommended Size | Rationale |
|----------|-----------------|-----------|
| Fine-grained QA (customer support) | 128-256 tokens | Precise, focused answers |
| General RAG | 512 tokens | Good balance of context and precision |
| Document summarization | 1024+ tokens | Broader context needed |
| Code retrieval | Function/class-level | Natural semantic units |

## The "Lost in the Middle" Problem

Chunk size interacts with LLM context window behavior: LLMs tend to ignore information in the middle of long contexts. Excessive context from oversized chunks or too many retrieved chunks can degrade answer quality and increase hallucination risk. This is another reason [[concepts/reranking]] is important — it reduces the number of chunks passed to the LLM.

## Sources

- [[sources/weaviate-chunking-strategies]] — comprehensive survey of all strategies with recommendations

## Related Concepts

- [[concepts/text-embeddings]] — the embeddings computed on chunks
- [[concepts/vector-search]] — retrieval quality depends on chunk quality
- [[concepts/two-stage-retrieval]] — chunk size affects both retrieval and reranking stages
- [[concepts/colbert-late-interaction]] — operates on token-level within chunks
