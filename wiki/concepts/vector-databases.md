---
title: "Vector Databases"
type: concept
sources: ["[[sources/hn-vector-database-debate]]", "[[sources/decodingai-second-brain-rag]]", "[[sources/pebblous-cheap-ontology]]"]
related: ["[[concepts/rag-vs-index-based-retrieval]]", "[[concepts/llm-knowledge-base]]", "[[concepts/knowledge-graph]]"]
last_compiled: 2026-04-05
summary: "Specialized databases for approximate nearest-neighbor (ANN) search over embedding vectors, necessary at billion-vector scale but often overkill for personal or team-scale LLM knowledge bases where pgvector, FAISS, or index-based LLM navigation suffice."
---

## Overview

Vector databases store high-dimensional embedding vectors and support approximate nearest-neighbor (ANN) search — finding the most semantically similar documents to a query vector. They became popular as the retrieval backbone for RAG (Retrieval-Augmented Generation) systems.

## When You Actually Need One

**Specialized vector DB justified at:**
- Billion-vector scale (Wikipedia, social media, enterprise at scale)
- Sub-millisecond latency requirements for semantic search
- Multi-modal retrieval across text, images, audio

**Alternatives that suffice for smaller scale:**
- **pgvector** (PostgreSQL extension): handles most team/personal use cases; caveat: IVF algorithm with nprobes=3 default gives ~50% recall; HNSW support addresses this
- **Elasticsearch**: already deployed in most orgs, handles vector operations without new infrastructure
- **FAISS**: open-source, handles billions of vectors with disk-based indexing
- **Vespa.ai**: underrated hybrid engine (vector + metadata + multi-vector indexing)

## The Real Question

Rather than "do you need a vector database?", the better question is: "do you need approximate nearest-neighbor search?" This surfaces the accuracy-speed tradeoff: ANN is *approximate* — it may miss the true nearest neighbors. For knowledge base Q&A where recall matters, this can be a real problem.

## Relevance to LLM Knowledge Bases

Karpathy's key insight: at ~100 articles / ~400K words, an LLM with a 1M-token context window can load the entire index and navigate to relevant articles by reading one-line summaries — **no vector search needed at all**. This is not approximate; it's exact LLM reasoning over a compact index.

This "index-based navigation" approach:
- Eliminates ANN accuracy loss
- Eliminates vector DB infrastructure cost
- Requires only that the wiki fit within the LLM's context window
- Scales until the index + summaries exceed context limits (~400K words total, ~1M tokens)

## Sources
- [[sources/hn-vector-database-debate]] — practitioner consensus on when vector DBs are actually needed
- [[sources/decodingai-second-brain-rag]] — production RAG that does use MongoDB vector search (justified at scale)
- [[sources/pebblous-cheap-ontology]] — context window expansion making vector DBs unnecessary at personal scale

## Related Concepts
- [[concepts/rag-vs-index-based-retrieval]] — the comparison with index-based navigation
- [[concepts/llm-knowledge-base]] — the system that avoids vector DBs
- [[concepts/knowledge-graph]] — alternative structured retrieval approach
