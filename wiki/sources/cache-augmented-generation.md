---
title: "Source: Don't Do RAG — When Cache-Augmented Generation is All You Need"
type: source-summary
source: "[[raw/cache-augmented-generation]]"
related: ["[[concepts/cache-augmented-generation]]", "[[concepts/retrieval-augmented-generation]]", "[[comparisons/rag-vs-cag]]"]
last_compiled: 2026-04-05
summary: "ArXiv paper proposing CAG as a RAG alternative that preloads all documents into KV cache — achieving 10x faster inference (0.85s vs 9.24s) with higher BERTScores, but limited to manageable knowledge base sizes."
reading_time: "1 min"
---

## Key Points

- CAG preloads all documents and caches KV parameters, eliminating retrieval entirely
- Three-phase framework: Preloading → Inference → Cache Reset
- 10x faster than RAG on HotPotQA-Small (0.85s vs 9.24s)
- Higher BERTScores across most test configurations on SQuAD and HotPotQA
- Limited to knowledge bases that fit within extended context windows (~128k tokens)
- Eliminates retrieval ranking errors — deterministic behavior

## Detailed Summary

This paper challenges the default assumption that RAG is always necessary for knowledge-intensive tasks. [[concepts/cache-augmented-generation]] works by computing a KV cache from all documents once, then loading this cache alongside each query. The model processes all documents holistically, enabling multi-hop reasoning without the variability introduced by document ranking.

The approach excels when knowledge is bounded and relatively stable. As long-context LLMs continue expanding their context windows, CAG becomes viable for increasingly large knowledge bases. However, it remains impractical for dynamic or very large corpora where continuous updates are needed.

## Related Concepts

- [[concepts/cache-augmented-generation]] — the core concept
- [[concepts/retrieval-augmented-generation]] — the baseline being compared against
- [[comparisons/rag-vs-cag]] — when to use each
