---
title: "Naive RAG vs Advanced RAG vs Agentic RAG"
type: comparison
subjects: ["[[concepts/retrieval-augmented-generation]]", "[[concepts/agentic-rag]]"]
sources: ["[[sources/ragflow-rag-review-2025]]", "[[sources/agentic-rag-survey]]", "[[sources/self-reflective-rag-langgraph]]"]
last_compiled: 2026-04-05
summary: "Three evolutionary phases of RAG: naive (fixed pipeline, 2020-2023), advanced (optimized retrieval + reranking, 2023-2025), and agentic (self-correcting agent loops, 2025+) with increasing complexity and quality."
---

## Overview

[[concepts/retrieval-augmented-generation]] has evolved through three distinct phases, each adding sophistication and quality at the cost of increased complexity. Understanding these phases helps practitioners choose the right level of investment for their use case.

## Comparison Table

| Dimension | Naive RAG | Advanced RAG | Agentic RAG |
|---|---|---|---|
| **Era** | 2020-2023 | 2023-2025 | 2025-present |
| **Pipeline** | Fixed: retrieve → generate | Optimized: preprocess → retrieve → rerank → generate | Dynamic: agent decides pipeline per query |
| **Retrieval** | Single-pass vector similarity | [[concepts/hybrid-search]], [[concepts/raptor]], [[concepts/graphrag]] | Dynamic strategy selection |
| **Quality control** | None | [[concepts/reranking]], metadata filtering | [[concepts/self-rag]], [[concepts/corrective-rag]], hallucination checking |
| **Chunking** | Fixed-size (512 tokens) | Semantic/adaptive chunking | Context-aware chunking |
| **Self-correction** | None | Limited (reranking) | Full loops: re-retrieve, re-generate, web fallback |
| **Query handling** | Pass-through | Query rewriting/expansion | Query decomposition, planning |
| **Complexity** | Low | Medium | High |
| **Latency** | Low | Medium | Higher (multiple agent steps) |
| **Best for** | Simple factual QA | Production knowledge bases | Complex multi-hop reasoning, high-stakes domains |

## Evolution of Key Capabilities

### Retrieval Strategy
- **Naive**: Embed query → ANN search → top-k chunks
- **Advanced**: [[concepts/hybrid-search]] (BM25 + vector), [[concepts/raptor]] (hierarchical), metadata filters
- **Agentic**: Router selects strategy per query; may use vectorstore, web search, SQL, or skip retrieval entirely

### Quality Assurance
- **Naive**: Trust the retriever; trust the generator
- **Advanced**: Cross-encoder [[concepts/reranking]] improves retrieval precision
- **Agentic**: Retrieval grader evaluates documents; hallucination checker verifies generation; retry loops on failure

### Error Recovery
- **Naive**: No error recovery — if retrieval fails, the answer fails
- **Advanced**: Better initial retrieval reduces failure rate
- **Agentic**: [[concepts/corrective-rag]] supplements with web search; [[concepts/self-rag]] decides to re-retrieve with modified queries

## When to Use Each

**Naive RAG**: Prototyping, simple QA over small document sets, resource-constrained environments

**Advanced RAG**: Production knowledge bases, enterprise search, customer support — where quality matters but queries are relatively straightforward

**Agentic RAG**: High-stakes domains (medical, legal, financial), complex multi-hop questions, scenarios where wrong answers have significant consequences

## Sources

- [[sources/ragflow-rag-review-2025]] — RAG evolution timeline and techniques
- [[sources/agentic-rag-survey]] — agentic RAG taxonomy and capabilities
- [[sources/self-reflective-rag-langgraph]] — Self-RAG and CRAG implementations
