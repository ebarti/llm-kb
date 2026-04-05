---
title: "Source: RAPTOR — Recursive Abstractive Processing for Tree-Organized Retrieval"
type: source-summary
source: "[[raw/raptor-tree-retrieval]]"
related: ["[[concepts/raptor]]", "[[concepts/retrieval-augmented-generation]]", "[[concepts/hierarchical-retrieval]]"]
last_compiled: 2026-04-05
summary: "ICLR 2024 paper introducing RAPTOR: builds a tree of recursive summaries via GMM clustering, achieving 20% absolute improvement on QuALITY benchmark by enabling multi-level abstraction retrieval."
reading_time: "1 min"
---

## Key Points

- Constructs hierarchical tree: chunk → cluster → summarize → repeat upward
- Uses soft clustering via Gaussian Mixture Models (segments can belong to multiple clusters)
- UMAP for dimensionality reduction, BIC for optimal cluster count
- Collapsed tree retrieval outperforms tree traversal
- 20% absolute improvement on QuALITY benchmark (82.6% vs 62.3% previous best)
- 18.5-57% of retrieved nodes come from non-leaf (summary) layers
- Scales linearly in token expenditure and build time

## Detailed Summary

[[concepts/raptor]] addresses a fundamental limitation of standard retrieval: most systems only retrieve short contiguous chunks, preventing holistic document understanding. RAPTOR solves this by recursively clustering semantically similar chunks using GMMs, generating abstractive summaries of each cluster, and repeating the process to build a tree with multiple levels of abstraction.

At query time, the "collapsed tree" method — which flattens all levels and retrieves across the entire hierarchy simultaneously — consistently outperforms layer-by-layer traversal. The experimental results are compelling: 18.5-57% of useful retrieved nodes come from non-leaf summary layers, proving that different questions require different abstraction levels.

## Related Concepts

- [[concepts/raptor]] — the retrieval technique
- [[concepts/hierarchical-retrieval]] — the broader paradigm
- [[concepts/retrieval-augmented-generation]] — the pipeline RAPTOR enhances
