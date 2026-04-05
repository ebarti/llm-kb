---
title: "Source: Choosing an Embedding Model"
type: source-summary
source: "[[raw/pinecone-embedding-models-rundown]]"
related: ["[[concepts/text-embeddings]]", "[[concepts/bi-encoder-vs-cross-encoder]]", "[[entities/openai-embeddings]]", "[[entities/mteb]]"]
last_compiled: 2026-04-05
summary: "Pinecone's practical guide comparing OpenAI, Cohere, and E5 embedding models on speed, dimensions, asymmetric search, and MTEB benchmark interpretation."
reading_time: "2 min"
---

## Key Points

- Embedding models compress text into vector representations that capture semantic meaning
- OpenAI ada-002 (1536 dims) took 9:07 to embed ~42K chunks; E5-base-v2 (768 dims, GPU) took 3:53 — nearly 2.5x faster
- Cohere embed-english-v3.0 (1024 dims) sits in between at 5:32
- Asymmetric search requires different treatment for queries vs documents: Cohere uses `input_type` parameter; E5 uses text prefixes ("passage:" / "query:")
- Mean pooling converts token-level embeddings into single vectors by averaging (with padding mask)
- MTEB results are self-reported and some models may be benchmark-optimized

## Detailed Summary

The article walks through the practical mechanics of choosing and using embedding models for RAG. It demonstrates that open-source models like E5 can match or exceed proprietary options in speed when run on GPU, while proprietary models offer easier API integration. The key insight is that dimensionality directly impacts storage cost and speed — higher dimensions do not always mean better retrieval quality. The article warns that [[entities/mteb]] leaderboard scores should be interpreted cautiously because results are self-reported and some models appear fine-tuned specifically for benchmark tasks.

## Notable Quotes

> "Storage costs scale with dimensionality — higher dimensions increase infrastructure expenses."

## Related Concepts

- [[concepts/text-embeddings]] — the core technology being compared
- [[concepts/bi-encoder-vs-cross-encoder]] — the architectural distinction underlying all embedding models
- [[entities/mteb]] — the benchmark used for evaluation
