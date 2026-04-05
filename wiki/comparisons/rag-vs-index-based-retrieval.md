---
title: "RAG vs. Index-Based Retrieval"
type: comparison
subjects: ["[[concepts/rag-vs-index-based-retrieval]]", "[[concepts/vector-databases]]"]
sources: ["[[sources/karpathy-llm-knowledge-bases]]", "[[sources/hn-vector-database-debate]]", "[[sources/pebblous-cheap-ontology]]", "[[sources/decodingai-second-brain-rag]]"]
last_compiled: 2026-04-06
summary: "Comparing vector-database RAG pipelines with Karpathy's index-based LLM navigation for knowledge base Q&A -- when each approach is appropriate and why."
---

## Overview

This is the foundational retrieval architecture decision in LLM knowledge base design. Retrieval-Augmented Generation (RAG) uses vector embeddings and approximate nearest-neighbor search to find relevant document chunks, while index-based retrieval uses LLM-maintained summary files to navigate directly to full articles. The choice between these approaches depends primarily on the scale of the knowledge base, the infrastructure budget, and the importance of retrieval accuracy vs. operational simplicity.

Karpathy's key insight -- that at ~100 articles and ~400K words, an LLM with a 1M-token context window can simply load and read the entire index -- challenged the prevailing assumption that every LLM Q&A system needs a vector database. The HN vector database debate corroborated this, with practitioners reporting that specialized vector DBs are overkill for most personal and team-scale use cases.

## Comparison Table

| Dimension | RAG (Vector Search) | Index-Based (LLM Navigation) |
|-----------|-------------------|---------------------------|
| Core approach | Embed documents into vectors, retrieve top-k by semantic similarity | LLM reads summary index, selects relevant articles, reads them in full |
| Scale ceiling | Billions of vectors (with dedicated DB) | ~100-400 articles / ~400K-1M words (context window limit) |
| Infrastructure | Vector DB + embedding pipeline + chunking logic | Markdown files + LLM API only |
| Retrieval accuracy | Approximate (ANN algorithms miss nearest neighbors) | Exact (LLM reads all summaries and makes a selection) |
| Freshness | Re-embed on update | Immediate (recompile summary file) |
| Auditability | Low (opaque vector similarity) | High (LLM explains why it chose specific articles) |
| Cost | Vector DB hosting + embedding API calls | LLM API calls only |
| Compounding | None (static index) | Yes (filing loop enriches the KB) |
| Setup complexity | High (chunking strategy, embedding model, DB tuning) | Low (LLM writes and maintains index files) |
| Best for | Large corpora (1000s+ docs), production reliability | Personal/team research (under ~400 articles) |

## Detailed Analysis

**Why RAG dominates the industry narrative**: The prevailing AI engineering playbook assumes RAG as the default retrieval strategy for any LLM application. This is driven by production-scale needs (enterprise document collections, customer support knowledge bases) and by vendor marketing from vector database companies. For these use cases -- hundreds of thousands of documents, real-time serving, multi-tenant access -- RAG is genuinely necessary.

**Why Karpathy's index approach works at personal scale**: At ~100 articles with one-line summaries, the entire index fits comfortably within a modern LLM's context window. The LLM reads all summaries, selects the relevant articles, and reads those in full. This is not approximate -- it is exact reasoning over the complete index, with zero accuracy loss from ANN approximation. The HN debate confirmed this: [[entities/pgvector]] with default settings achieves only ~50% recall, meaning RAG can actually be less accurate than index-based navigation at small scale.

**The scale threshold**: The crossover point occurs when the wiki's total content exceeds the LLM's context window. At ~400K words (~1M tokens), loading the full index becomes infeasible. At this point, options include (a) switching to RAG with [[entities/pgvector]] or [[entities/faiss]], (b) hierarchical indexing (index of indexes), or (c) fine-tuning the LLM on the corpus.

**The accuracy paradox**: RAG's approximate nearest-neighbor search introduces a fundamental accuracy tradeoff that is often overlooked. As the HN discussion noted, the real question is "do you actually need approximate nearest-neighbor search?" For knowledge base Q&A where missing a relevant document can lead to incorrect answers, the ~50-95% recall of ANN search (depending on algorithm and tuning) may be worse than the 100% recall of reading all summaries.

## When to Use Each

**Use index-based retrieval when:**
- Your knowledge base is under ~400 articles / ~1M words total
- You value human auditability and transparency
- You want the compounding filing loop (query results enriching the KB)
- You prefer minimal infrastructure (just files + LLM API)
- Retrieval accuracy matters more than query speed

**Use RAG when:**
- Your corpus exceeds 1M words
- You need sub-second retrieval latency at scale
- Multiple users/agents query the same knowledge base concurrently
- You have existing vector database infrastructure
- You need multi-modal retrieval (text + images + audio)

## Sources

- [[sources/karpathy-llm-knowledge-bases]] -- original observation that RAG was unnecessary at personal scale
- [[sources/hn-vector-database-debate]] -- practitioner consensus on vector DB necessity
- [[sources/pebblous-cheap-ontology]] -- quantitative comparison (RAG 87.5% accuracy vs. fine-tuning 50.4%)
- [[sources/decodingai-second-brain-rag]] -- production RAG implementation as counterpoint
