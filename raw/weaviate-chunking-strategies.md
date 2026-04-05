---
title: "Chunking Strategies to Improve LLM RAG Pipeline Performance"
source: "https://weaviate.io/blog/chunking-strategies-for-rag"
author: "Weaviate"
date_published: 2024-05-10
date_ingested: 2026-04-05
tags: [chunking, RAG, text-splitting, embeddings, retrieval]
type: article
status: raw
discovered_via: search
---

# Chunking Strategies for RAG — Weaviate

## Fixed-Size Chunking

Splits text into predetermined chunk sizes (tokens or characters). Common baseline: 512 tokens per chunk, 10-20% overlap (50-100 tokens). Simple, no semantic awareness. Good for prototyping.

Trade-off: large chunks mix multiple ideas; small chunks lose context at boundaries. Overlap addresses boundary issues.

## Recursive Chunking

Hierarchical splitting using prioritized separators (double newlines, single newlines, periods, spaces). Attempts highest-priority separator first, recursively applies next for oversized chunks. Preserves document structure.

Best for: unstructured text (articles, blog posts, research papers).

## Document-Based Chunking

Leverages intrinsic document structure: Markdown by headings, HTML by semantic tags, code by functions/classes, PDF requires preprocessing. Aligns chunks with logical organization.

## Semantic Chunking

1. Sentence segmentation
2. Embedding generation per sentence
3. Similarity analysis to detect topic boundaries
4. Chunk formation at semantic breakpoints

Creates highly coherent chunks, each containing a self-contained idea. Medium-high complexity.

## Advanced Strategies

- Late Chunking (Jina AI, 2024): Embeds entire documents first, then derives chunk embeddings from token-level representations
- Hierarchical Chunking: Multiple layers (sections → paragraphs → sentences)
- LLM-Based Chunking: Language models identify propositions and summarize sections
- Agentic Chunking: AI agent dynamically selects optimal strategy per document
- Adaptive Chunking: ML models analyze semantic density, creating smaller chunks for complex sections

## Recommendations

Start with fixed-size (512 tokens, 50-100 token overlap). Measure: hit rate, precision, recall. Include human review. Key principle: "if a chunk makes sense to you when read alone, it will make sense to the LLM too." Balance precision against "lost in the middle" effect.
