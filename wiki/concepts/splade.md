---
title: "SPLADE (Sparse Lexical and Expansion Model)"
type: concept
sources: ["[[sources/hybrid-search-bm25-splade-vector]]"]
related: ["[[concepts/bm25]]", "[[concepts/hybrid-search]]", "[[concepts/retrieval-augmented-generation]]"]
last_compiled: 2026-04-05
summary: "A learned sparse retrieval model using transformer encoding to generate sparse vectors with vocabulary expansion — outperforms BM25 on BEIR benchmarks while maintaining inverted index compatibility."
---

## Overview

SPLADE (Sparse Lexical and Expansion model) is a learned sparse retrieval method that uses transformer encoding to generate sparse vectors with **vocabulary expansion**. Unlike [[concepts/bm25]], which can only match exact terms, SPLADE enriches both query and document representations with semantically related terms during indexing — so a query about "car" can match documents containing "automobile," "vehicle," or "driving."

## How It Works

SPLADE uses a BERT-based transformer to generate a sparse vector for each text passage. The key innovation is that the model's output vocabulary is the full BERT vocabulary (~30K tokens), and the model learns to assign non-zero weights to terms that are semantically relevant to the passage — even if those terms don't appear in the original text.

This produces sparse vectors that:
- Maintain compatibility with standard inverted indexes (fast at query time)
- Include vocabulary expansion terms (semantic matching)
- Can be stored and searched like traditional keyword indexes

## Performance

SPLADE outperforms BM25 on most BEIR benchmarks while maintaining the computational advantages of sparse retrieval at query time. The trade-off is requiring **GPU-accelerated transformer inference during indexing** — a one-time cost for static corpora but significant for frequently updated collections.

## When to Use SPLADE vs. BM25

| Factor | BM25 | SPLADE |
|---|---|---|
| Vocabulary mismatch | Poor (no expansion) | Good (learned expansion) |
| Exact match | Excellent | Good |
| Indexing cost | CPU only | GPU required |
| Training required | None | Yes (or use pretrained) |
| Best for | Legal IDs, codes, exact terms | Enterprise KBs with diverse query styles |

## Sources

- [[sources/hybrid-search-bm25-splade-vector]] — BM25 vs. SPLADE comparison with benchmarks

## Related Concepts

- [[concepts/bm25]] — the traditional alternative
- [[concepts/hybrid-search]] — SPLADE as the sparse component
- [[concepts/colbert]] — another learned retrieval approach (dense, late interaction)
