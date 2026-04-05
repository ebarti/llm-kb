---
title: "Hierarchical Retrieval"
type: concept
sources: ["[[sources/raptor-tree-retrieval]]", "[[sources/microsoft-graphrag]]", "[[sources/ragflow-rag-review-2025]]"]
related: ["[[concepts/raptor]]", "[[concepts/graphrag]]", "[[concepts/retrieval-augmented-generation]]"]
last_compiled: 2026-04-05
summary: "Retrieval across multiple levels of abstraction — from raw chunks to summaries to themes — addressing the limitation that standard RAG only fetches short contiguous text fragments."
---

## Overview

Hierarchical retrieval is a paradigm for organizing and searching information at multiple levels of abstraction, addressing the fundamental limitation that standard [[concepts/retrieval-augmented-generation]] only retrieves short contiguous text chunks. Different questions require different abstraction levels: a factual question might need a specific paragraph, while a thematic question might need a high-level summary spanning hundreds of pages.

## Key Approaches

### RAPTOR (Tree-Based)
[[concepts/raptor]] builds a tree by recursively clustering and summarizing text chunks. Leaf nodes are raw text; higher nodes are increasingly abstract summaries. At query time, the "collapsed tree" method retrieves across all levels simultaneously. Analysis shows 18.5-57% of useful retrieved nodes come from non-leaf summary layers.

### GraphRAG (Graph-Based)
[[concepts/graphrag]] constructs a knowledge graph with hierarchical community summaries. Entity-level nodes are grouped into communities via Leiden clustering, with pre-generated summaries at each level. This enables answering holistic queries about themes and relationships.

### TreeRAG (Document-Structure-Based)
RAGFlow's TreeRAG decouples search and retrieval into different granularities. Offline: construct hierarchical directory summaries (Chapter → Section → Subsection). Online: search fine-grained fragments, then assemble larger coherent context using the directory structure.

## Why Hierarchical Retrieval Matters

Standard chunk-based retrieval forces a tradeoff: small chunks preserve precision but fragment context; large chunks preserve context but introduce noise. Hierarchical retrieval sidesteps this by offering retrieval at whatever granularity the query demands.

## Sources

- [[sources/raptor-tree-retrieval]] — tree-based hierarchical retrieval
- [[sources/microsoft-graphrag]] — graph-based hierarchical retrieval
- [[sources/ragflow-rag-review-2025]] — TreeRAG document-structure approach

## Related Concepts

- [[concepts/raptor]] — tree-based implementation
- [[concepts/graphrag]] — graph-based implementation
- [[concepts/retrieval-augmented-generation]] — the pipeline hierarchical retrieval enhances
