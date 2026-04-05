---
title: "Microsoft GraphRAG"
type: entity
entity_type: tool
sources: ["[[sources/graphrag-microsoft-research]]", "[[sources/llm-kg-construction-survey]]"]
related: ["[[concepts/graphrag]]", "[[concepts/knowledge-graph]]", "[[concepts/knowledge-graph-construction]]"]
last_compiled: 2026-04-05
summary: "Open-source modular graph-based RAG system from Microsoft Research that builds knowledge graphs from text using LLM extraction, Leiden community detection, and hierarchical summarization."
---

## Overview

Microsoft GraphRAG is an open-source system that implements the [[concepts/graphrag]] paradigm — building knowledge graphs from text corpora and using them for retrieval-augmented generation. Released on GitHub (microsoft/graphrag), it provides a modular pipeline for indexing (text → knowledge graph → communities → summaries) and multiple query modes (Global, Local, DRIFT, Basic search).

## Key Features

- **LLM-based entity/relation extraction** from source text
- **Leiden algorithm** for hierarchical community detection
- **Bottom-up community summarization** at multiple abstraction levels
- **Multiple query modes**: Global (corpus-wide), Local (entity-specific), DRIFT (hybrid), Basic (vector fallback)
- **Prompt Tuning Guide** for domain-specific optimization

## Technical Stack

- Python library with modular architecture
- Supports multiple LLM providers for extraction and summarization
- Available through Microsoft Discovery (Azure platform) for scientific research

## Performance

Consistently outperforms baseline RAG on comprehensiveness, diversity, and source provenance. Maintains equivalent faithfulness per SelfCheckGPT evaluation. However, [[entities/kggen]] outperforms GraphRAG's extraction quality on the MINE benchmark (66% vs 48%).

## Variants

- **LazyGraphRAG**: Lighter-weight variant deferring some processing to query time
- **GraphRAG + Discovery**: Integration with Microsoft's agentic scientific research platform

## Mentioned In

- [[sources/graphrag-microsoft-research]] — core documentation and evaluation
- [[sources/llm-kg-construction-survey]] — placed within broader KG construction taxonomy
- [[sources/kggen-knowledge-graph-extraction]] — benchmarked against for extraction quality
