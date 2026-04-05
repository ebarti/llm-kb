---
marp: true
theme: default
paginate: true
---

# The RAG Landscape
## Retrieval-Augmented Generation in 2026
### From Naive Pipelines to Agentic Context Engines

---

## Agenda

1. What is RAG?
2. Why RAG Matters: The Knowledge Problem
3. Core RAG Architecture
4. RAG vs Fine-Tuning vs Long-Context
5. The Evolution: Naive to Agentic
6. Advanced RAG Techniques
7. GraphRAG
8. RAPTOR: Hierarchical Retrieval
9. Agentic RAG
10. Self-RAG and Corrective RAG
11. Evaluation: RAGAS Metrics
12. Vector Search vs BM25 vs Hybrid
13. Chunking Strategies
14. RAG Hallucinations
15. Real-World Deployment

---

## What is RAG?

**Retrieval-Augmented Generation** (Lewis et al., 2020, Facebook AI Research):

1. **Retrieve** relevant documents from an external corpus
2. **Inject** them into the LLM's context window as grounding material
3. **Generate** a response conditioned on both query and evidence

As of 2026: **~85% of production LLM applications** incorporate RAG (up from ~30% in early 2024).

---

## Why RAG? The Knowledge Problem

LLMs have **static knowledge** frozen at training time. RAG solves:

| Problem | RAG Solution |
|---------|-------------|
| Knowledge cutoff | Retrieve current documents |
| Hallucination | Ground in evidence |
| Domain specificity | Index domain corpus |
| Traceability | Cite retrieved sources |
| Cost | Cheaper than fine-tuning |

---

## Core RAG Architecture

```
     Offline (Indexing)              Online (Query)

  Documents                     User Query
      |                             |
      v                             v
  Chunking                     Query Encoding
      |                             |
      v                             v
  Embedding                    Vector Search
      |                             |
      v                             v
  Vector Store  <----------->  Top-K Retrieval
                                    |
                                    v
                               LLM Generation
                                    |
                                    v
                               Cited Answer
```

---

## RAG vs Fine-Tuning vs Long-Context

| Dimension | RAG | Fine-Tuning | Long-Context |
|-----------|-----|-------------|--------------|
| Knowledge update | Minutes | Hours-days | Real-time |
| Cost per query | Moderate | Low | High |
| Latency | ~1s retrieval | Fastest | 30-60s |
| Traceability | Citations | None | Position-based |
| Infrastructure | Vector DB | GPU training | Large context model |
| Best for | Dynamic facts | Persistent behavior | Full-doc reasoning |

**Key finding**: RAG + fine-tuning are complementary (+11pp cumulative accuracy in agriculture study).

---

## RAFT: The Best of Both Worlds

**Retrieval-Augmented Fine-Tuning** (2024):
- Train the model to reason over retrieved documents
- Include both relevant and distractor documents during training
- Model learns to identify and cite relevant passages
- **Up to 76% improvement** on domain benchmarks
- Combines RAG's dynamic retrieval with fine-tuning's persistent behavior

---

## Cache-Augmented Generation (CAG)

An alternative for **small, stable knowledge bases**:
- Preload all documents into context (no retrieval step)
- Skip the entire retrieval pipeline
- **10x faster** than RAG on small KBs
- Works when total KB fits in context window
- Mirrors Karpathy's index-based approach at small scale

**Use CAG when**: KB < context window, low latency needed, documents rarely change

---

## The Evolution: Three Phases of RAG

**Naive RAG (2020-2023)**
- Simple retrieve-then-generate
- Fixed chunking, single-pass retrieval, no quality control
- Fails on complex reasoning, holistic queries, multi-hop questions

**Advanced RAG (2023-2025)**
- Query rewriting, expansion, HyDE
- Reranking, filtering, semantic chunking
- RAPTOR hierarchical summaries, hybrid search

**Agentic RAG (2025-present)**
- Autonomous agents manage retrieval and refinement
- Self-reflection loops, dynamic source selection
- Self-RAG, Corrective RAG, multi-agent collaboration

---

## GraphRAG: Knowledge Graph + RAG

**Microsoft Research (2024)**: addresses two RAG failures:
1. Inability to connect disparate information sharing common attributes
2. Poor performance on holistic summarization queries

**How it works**:
- LLMs extract entities and relationships from text
- Graph ML creates hierarchical community structures (Leiden algorithm)
- Pre-generated summaries at multiple abstraction levels
- Two query modes: local (entity-focused) and global (theme-level)

---

## GraphRAG: Why It Matters

**Evaluation on Ukraine-Russia conflict data**:

| Query: "Top themes?" | Baseline RAG | GraphRAG |
|---------------------|-------------|----------|
| Result 1 | Urban development | Armed conflict |
| Result 2 | Economic growth | Political entities |
| Result 3 | Infrastructure | Humanitarian issues |

Baseline RAG retrieved **irrelevant chunks** via similarity search.
GraphRAG correctly identified **structural themes** via community summaries.

---

## RAPTOR: Recursive Tree Retrieval

**ICLR 2024** -- Recursive Abstractive Processing for Tree-Organized Retrieval:

```
         [Global Summary]          Level 3
           /          \
    [Cluster A]    [Cluster B]     Level 2
     /    \          /    \
  [C1]  [C2]     [C3]   [C4]      Level 1 (chunks)
```

- Cluster chunks via GMM (soft clustering -- chunks can belong to multiple clusters)
- Summarize each cluster, then cluster and summarize again
- **Collapsed tree retrieval**: search across ALL levels simultaneously
- **+20% absolute improvement** on QuALITY benchmark (82.6% vs 62.3%)
- **18.5-57%** of useful nodes come from summary (non-leaf) layers

---

## Agentic RAG

**Key patterns** (arXiv survey):

| Pattern | Description |
|---------|-------------|
| Reflection | Agent evaluates retrieval quality before generating |
| Planning | Agent decomposes complex queries into sub-queries |
| Tool use | Agent selects retrieval tools dynamically |
| Multi-agent | Specialized agents for retrieval, synthesis, verification |

**Taxonomy**: agent cardinality x control structure x autonomy level x knowledge representation

---

## Self-RAG: Reflection Tokens

Self-Reflective RAG adds quality control via reflection tokens:

1. **Retrieve**: decide whether retrieval is needed for this query
2. **ISREL**: is the retrieved passage relevant?
3. **ISSUP**: is the response supported by the passage?
4. **ISUSE**: is the response useful to the user?

The model learns to critique its own retrieval and generation, creating a self-correcting loop.

---

## Corrective RAG (CRAG)

When retrieval quality is poor, CRAG adds fallback:

```
Query -> Retrieve -> Evaluate Relevance
                          |
              +-----------+-----------+
              |           |           |
          Correct     Ambiguous    Incorrect
              |           |           |
          Use docs   Refine query  Web search
              |           |           |
              +-----------+-----------+
                          |
                      Generate
```

Combines retrieval correction with web search fallback.

---

## RAG Evaluation: Three Dimensions

| Dimension | Metrics | What It Measures |
|-----------|---------|-----------------|
| Retrieval Quality | Precision@k, Recall@k, MRR, nDCG | Did we find the right documents? |
| Generation Quality | Faithfulness, Answer Relevance, Citation Coverage | Did we produce a faithful answer? |
| Operational Quality | Latency, Cost, Safety, Compliance | Is it production-ready? |

---

## RAGAS: The Evaluation Framework

**RAGAS** (Retrieval Augmented Generation Assessment) -- dominant open-source framework:

- **Faithfulness**: Is the answer grounded in retrieved context?
- **Answer Relevance**: Does the answer address the question?
- **Context Precision**: Are retrieved documents relevant?
- **Context Recall**: Did we retrieve all needed information?

**Key benchmarks**:
- RAGBench: 100,000 examples for general testing
- CRAG: comprehensive RAG evaluation
- LegalBench-RAG: domain-specific compliance
- T2-RAGBench: temporal reasoning

---

## Vector Search vs BM25 vs Hybrid

| Method | Strength | Weakness |
|--------|----------|----------|
| **BM25** (sparse) | Exact keyword match, rare terms, proper nouns | Misses synonyms, no semantic understanding |
| **Vector search** (dense) | Semantic similarity, synonyms, concepts | Misses exact terms, rare words, acronyms |
| **Hybrid** | Both semantic + keyword | Higher complexity and latency |

**Key insight**: failure modes are **complementary** -- use both.

---

## Hybrid Search Architecture

```
Query
  |
  +---> BM25 (keyword) ---> Ranked list A
  |
  +---> Vector (dense) ---> Ranked list B
  |
  +---> [Optional: SPLADE (learned sparse)] ---> Ranked list C
  |
  v
Reciprocal Rank Fusion (RRF) or alpha-weighted merge
  |
  v
Cross-encoder reranking (e.g., ColBERT, Cohere Rerank)
  |
  v
Top-K to LLM
```

Weaviate uses an **alpha parameter** (0 = pure BM25, 1 = pure vector) for tuning.

---

## Chunking Strategies

| Strategy | Description | Best For |
|----------|-------------|----------|
| Fixed-size (512 tokens) | Split at token count, 10-20% overlap | Baseline, predictable |
| Recursive | Hierarchical separators (paragraphs, sentences) | Structured text |
| Semantic | Embed sentences, detect topic boundaries | Topic-coherent chunks |
| Document-based | Use headings, HTML tags, functions | Structured documents |
| Late chunking (Jina) | Embed full doc first, extract chunk embeddings | Context preservation |
| Agentic | AI selects optimal strategy per document | Heterogeneous corpora |

> "If a chunk makes sense to you when read alone, it will make sense to the LLM too."

---

## Chunking Benchmarks

| Strategy | Recall | Coherence | Best Metric |
|----------|--------|-----------|-------------|
| Fixed-size | **92%** | 85% | Recall |
| Semantic boundary | 89% | **95%** | Coherence |
| Hybrid | **94%** accuracy | 91% | Balance |
| Sliding window | 90% | 88% | Overlap handling |

**Recommendation**: Start with 512-token fixed-size baseline. Measure retrieval metrics. Only add complexity when needed.

---

## RAG Hallucinations

**Stanford research**: 17-33% hallucination rates in specialized legal RAG tools.

**Causes**:
- Model ignores retrieved evidence
- Fuses information from multiple documents incorrectly
- Generates with unwarranted confidence
- Retrieval returns irrelevant but plausible passages

**Mitigation**:
- Self-RAG reflection tokens
- Citation enforcement in prompts
- Cross-encoder reranking to improve retrieval quality
- Faithfulness evaluation in production

---

## The Long-Context Debate

> "Will 1M+ token context windows kill RAG?"

**No.** Research shows:
- Feeding massive document batches causes **attention scatter** and "information flooding"
- LLMs exhibit a **U-shaped performance curve**: best at beginning/end, >30% degradation in the middle
- Optimal approach: **retrieval-first, long-context containment**
  - Use RAG to select relevant material
  - Use long context to hold more complete chunks

RAG and long context are **complementary, not competing**.

---

## RAG as Context Engine (2026)

RAG is evolving from a retrieval pattern into a **context engineering** discipline:

| Context Type | Traditional | Context Engine |
|-------------|-------------|----------------|
| Domain knowledge | RAG retrieval | Unified retrieval |
| Tool selection | Hardcoded | Retrieved from hundreds |
| Conversation state | Chat history | Managed memory |
| User preferences | System prompt | Retrieved profile |

RAGFlow 2025: "RAG is becoming the foundation for a unified Context Engine."

---

## Real-World Deployment Checklist

1. **Start simple**: fixed chunking, single vector store, basic prompt
2. **Measure first**: RAGAS metrics before optimizing
3. **Hybrid search**: BM25 + vector from the start
4. **Reranking**: cross-encoder as second stage (cheap quality boost)
5. **Evaluation pipeline**: golden dataset + synthetic + human review
6. **Monitor in production**: A/B tests, faithfulness tracking
7. **Scale gradually**: add GraphRAG, RAPTOR, agentic patterns as needed

---

## References

- Lewis, P. et al. (2020). "Retrieval-Augmented Generation." Facebook AI Research.
- Microsoft Research (2024). "GraphRAG." 
- Sarthi, P. et al. (2024). "RAPTOR." ICLR.
- RAGFlow (2025). "Year-End Review: RAG to Context Engine."
- Asai, A. et al. (2024). "Self-RAG." 
- Es, S. et al. (2024). "RAGAS: Automated Evaluation of RAG."
- Mindee (2025). "RAG Hallucinations Explained."
- Weaviate (2025). "Chunking Strategies for RAG."
