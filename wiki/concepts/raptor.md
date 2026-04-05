---
title: "RAPTOR (Recursive Abstractive Processing for Tree-Organized Retrieval)"
type: concept
sources: ["[[sources/raptor-tree-retrieval]]"]
related: ["[[concepts/retrieval-augmented-generation]]", "[[concepts/hierarchical-retrieval]]", "[[concepts/graphrag]]"]
last_compiled: 2026-04-05
summary: "ICLR 2024 technique that recursively clusters and summarizes text chunks into a tree structure, enabling retrieval at multiple abstraction levels — achieving 20% absolute improvement on QuALITY benchmark."
---

## Overview

RAPTOR (Recursive Abstractive Processing for Tree-Organized Retrieval) is a retrieval technique presented at ICLR 2024 that addresses a fundamental limitation of standard [[concepts/retrieval-augmented-generation]]: most retrieval systems only fetch short contiguous text chunks, preventing holistic understanding of long documents or document collections.

RAPTOR solves this by constructing a hierarchical tree of summaries. Leaf nodes are original text chunks; intermediate and root nodes are progressively more abstract summaries produced by recursively clustering and summarizing groups of related chunks. At query time, the system can retrieve from any level of the tree, matching the abstraction level needed by the question.

## Tree Construction Process

1. **Chunking**: Segment source documents into 100-token chunks
2. **Embedding**: Encode chunks using SBERT to create leaf node embeddings
3. **Clustering**: Group semantically similar chunks using **Gaussian Mixture Models** (soft clustering — a chunk can belong to multiple clusters). Uses UMAP for dimensionality reduction and Bayesian Information Criterion (BIC) for determining optimal cluster count.
4. **Summarization**: Generate abstractive summaries of each cluster using an LLM (gpt-3.5-turbo in the original work). Analysis found ~4% of summaries contain minor hallucinations, but these do not propagate to parent nodes.
5. **Recursion**: Repeat steps 2-4 on the summary nodes, building upward until the tree converges to a root.

The use of soft clustering is particularly important: it allows a text chunk about "climate policy and economic growth" to appear in both a climate cluster and an economics cluster, preserving multi-topic information.

## Retrieval Strategies

RAPTOR supports two querying approaches:

**Tree Traversal**: Start at the root, select top-k most relevant nodes by cosine similarity, descend to their children, select again, and repeat layer by layer until reaching leaves. This provides a guided, top-down search.

**Collapsed Tree**: Flatten the entire tree hierarchy and retrieve nodes across all levels simultaneously until reaching a token budget. Testing showed this approach **consistently outperforms tree traversal** because it provides greater flexibility in matching the query's required abstraction level.

## Key Results

| Benchmark | RAPTOR + GPT-4 | Previous Best | Improvement |
|---|---|---|---|
| QuALITY | 82.6% | 62.3% | +20% absolute |
| QASPER | 55.7% F-1 | 53.9% (CoLT5 XL) | +1.8% |
| NarrativeQA | New METEOR benchmark | — | — |

Layer analysis revealed that **18.5-57% of useful retrieved nodes come from non-leaf summary layers**, depending on the dataset. This directly validates the value of multi-level abstraction: many questions cannot be answered from raw chunks alone.

## Computational Profile

RAPTOR scales **linearly** in both token expenditure and build time, making it practical for large document collections. The one-time cost is the tree construction (embedding + clustering + summarization passes), after which retrieval is standard vector similarity search over a larger set of nodes.

## Sources

- [[sources/raptor-tree-retrieval]] — original ICLR 2024 paper details

## Related Concepts

- [[concepts/retrieval-augmented-generation]] — the pipeline RAPTOR enhances
- [[concepts/hierarchical-retrieval]] — the broader paradigm of multi-level retrieval
- [[concepts/graphrag]] — alternative structured retrieval using graphs instead of trees
