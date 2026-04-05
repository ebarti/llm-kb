---
title: "Source: Rerankers and Two-Stage Retrieval"
type: source-summary
source: "[[raw/pinecone-rerankers-two-stage]]"
related: ["[[concepts/reranking]]", "[[concepts/bi-encoder-vs-cross-encoder]]", "[[concepts/two-stage-retrieval]]"]
last_compiled: 2026-04-05
summary: "Pinecone's guide to cross-encoder reranking: why bi-encoders lose information, how two-stage retrieval (retrieve top-25, rerank to top-3) improves RAG, and practical impact of moving relevant chunks from position 23 to position 1."
reading_time: "2 min"
---

## Key Points

- Bi-encoders compress all document meaning into one vector — information is lost
- Cross-encoders process query+document pairs together, analyzing relevance specific to each query
- Core problem: increasing top_k hurts LLM performance ("LLM recall degrades with more context tokens")
- Solution: retrieve many (top_k=25), rerank to few (top_n=3)
- Scale challenge: BERT reranker on 40M records with V100 takes >50 hours per query; vector search does it in <100ms
- Practical impact: reranking moved the most relevant chunk from position 23 to position 1
- Models: bge-reranker-v2-m3 (reranker), multilingual-e5-large (embeddings, 1024 dims)

## Detailed Summary

The article makes the strongest case for [[concepts/reranking]] as essential infrastructure in RAG pipelines. The fundamental insight is that bi-encoders must create document representations without knowing the future query, forcing lossy compression. Cross-encoders see both query and document simultaneously but cannot scale to full collections. [[concepts/two-stage-retrieval]] resolves this tension: use fast bi-encoder retrieval to narrow candidates, then apply expensive cross-encoder reranking on just the top results. The demonstrated improvement — lifting a relevant passage from rank 23 to rank 1 — illustrates why this architecture is becoming standard.

## Related Concepts

- [[concepts/reranking]] — the technique
- [[concepts/bi-encoder-vs-cross-encoder]] — the architectural tradeoff driving two-stage design
- [[concepts/two-stage-retrieval]] — the overall architecture
