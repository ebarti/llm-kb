---
title: "Source: Chunking Strategies for RAG"
type: source-summary
source: "[[raw/weaviate-chunking-strategies]]"
related: ["[[concepts/chunking-strategies]]", "[[concepts/text-embeddings]]", "[[concepts/vector-search]]"]
last_compiled: 2026-04-05
summary: "Weaviate's comprehensive guide to text chunking for RAG: fixed-size, recursive, semantic, document-based, and advanced strategies (late chunking, hierarchical, agentic), with the baseline recommendation of 512 tokens and 50-100 token overlap."
reading_time: "2 min"
---

## Key Points

- Fixed-size: 512 tokens, 10-20% overlap (50-100 tokens) as baseline
- Recursive: hierarchical separators (double newlines → newlines → periods → spaces)
- Semantic: embed sentences, detect topic boundaries by similarity drop
- Document-based: use structure (headings, HTML tags, code functions)
- Late chunking (Jina AI, 2024): embed full document first, then extract chunk embeddings from token-level representations
- Hierarchical: multiple layers (sections → paragraphs → sentences)
- LLM-based and agentic chunking: AI selects optimal strategy per document
- Key principle: "if a chunk makes sense to you when read alone, it will make sense to the LLM too"
- Large chunks mix topics; small chunks lose context; overlap mitigates boundaries

## Detailed Summary

The article provides the most systematic treatment of [[concepts/chunking-strategies]] for embedding-based retrieval. The progression from simple (fixed-size) to complex (agentic) reflects a real tradeoff: simpler strategies are faster and more predictable but may produce suboptimal chunk boundaries, while semantic and agentic approaches create more coherent chunks at higher computational cost. The practical recommendation is to start with the 512-token fixed-size baseline, measure retrieval metrics (hit rate, precision, recall), and only move to more complex strategies when the baseline proves insufficient for the specific use case.

## Related Concepts

- [[concepts/chunking-strategies]] — the techniques described
- [[concepts/text-embeddings]] — what operates on the chunks
- [[concepts/vector-search]] — what retrieves the chunks
