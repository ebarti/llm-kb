---
title: "Source: KGGen — Extracting Knowledge Graphs from Plain Text with Language Models"
type: source-summary
source: "[[raw/kggen-knowledge-graph-extraction]]"
related: ["[[concepts/knowledge-extraction]]", "[[concepts/knowledge-fusion]]", "[[entities/kggen]]", "[[entities/microsoft-graphrag]]"]
last_compiled: 2026-04-05
summary: "KGGen introduces a three-stage LLM pipeline (extract, aggregate, cluster) for knowledge graph construction from text, outperforming GraphRAG by 18% on the novel MINE benchmark for information capture."
reading_time: "2 min"
---

## Key Points

- Three-stage pipeline: (1) two-step LLM extraction of entities then triples, (2) aggregation across documents, (3) iterative LLM-based entity clustering for deduplication
- Entity resolution via crowd-sourcing-inspired iterative clustering with LLM-as-a-Judge validation
- Introduces MINE benchmark — first benchmark measuring KG extractor ability to capture text information
- Achieves 66.07% on MINE vs. GraphRAG's 47.80% and OpenIE's 29.84%
- Produces denser, more coherent graphs with fewer redundant entities

## Detailed Summary

KGGen (February 2025) presents a modular Python library for LLM-driven knowledge graph extraction using GPT-4o and the DSPy framework. Its key innovation is the three-stage architecture.

The **Generate** stage uses two LLM calls per text chunk: first identifying key entities, then extracting subject-predicate-object triples using those entities. This two-step approach ensures consistency between entity mentions and extracted relations.

The **Aggregate** stage collects all extracted entities and edges across documents, normalizes to lowercase, and consolidates — requiring no LLM involvement.

The **Cluster** stage performs iterative LLM-based entity resolution. The LLM examines the entity list to find clusters of equivalent entities, validates each cluster via LLM-as-a-Judge, and iterates until convergence. This handles variations in tense, plurality, stemming, and synonyms (e.g., merging "vulnerabilities" and "weaknesses").

The MINE benchmark evaluates whether extracted KGs preserve the information content of source texts, using 100 Wikipedia-length articles with 15 manually-verified facts each. KGGen's 18% improvement over GraphRAG comes from producing denser, more interconnected graphs.

## Related Concepts

- [[concepts/knowledge-extraction]] — KGGen's core contribution
- [[concepts/knowledge-fusion]] — the entity clustering/resolution stage
- [[entities/kggen]] — the tool itself
