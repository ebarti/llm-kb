---
title: "Microsoft Research"
type: entity
entity_type: org
sources: ["[[sources/microsoft-graphrag]]"]
related: ["[[concepts/graphrag]]", "[[concepts/retrieval-augmented-generation]]", "[[concepts/knowledge-graph]]"]
last_compiled: 2026-04-05
summary: "Developed GraphRAG — a knowledge-graph-based approach to RAG that constructs community hierarchies for holistic query answering, now available as open-source on GitHub and integrated into Azure."
---

## Overview

Microsoft Research is a major AI research organization that developed [[concepts/graphrag]], one of the most significant advances in [[concepts/retrieval-augmented-generation]] architecture. GraphRAG addresses the fundamental limitation that baseline RAG cannot answer holistic or aggregate queries over large document collections.

## Key Contributions to RAG

### GraphRAG
The flagship contribution: a system that extracts knowledge graphs from text using LLMs, applies graph machine learning for hierarchical community detection, and generates pre-computed summaries at each level. Released as open-source on GitHub (`microsoft/graphrag`).

### LazyGraphRAG
A lighter-weight variant that defers some graph processing to query time, reducing the massive upfront token costs of full GraphRAG indexing.

### Microsoft Discovery
An agentic platform for scientific research built on Azure that integrates GraphRAG and LazyGraphRAG technology.

## Mentioned In

- [[sources/microsoft-graphrag]] — original research blog post with evaluation results
