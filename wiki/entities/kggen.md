---
title: "KGGen"
type: entity
entity_type: tool
sources: ["[[sources/kggen-knowledge-graph-extraction]]"]
related: ["[[concepts/knowledge-extraction]]", "[[concepts/knowledge-fusion]]", "[[concepts/knowledge-graph]]", "[[concepts/knowledge-graph-construction]]"]
last_compiled: 2026-04-05
summary: "Open-source Python library for extracting knowledge graphs from text via a 3-stage pipeline (generate, aggregate, cluster), achieving 66% on the MINE benchmark — 18% above GraphRAG."
---

## Overview

KGGen is an open-source Python library that extracts structured knowledge graphs from plain text using language models. It uses GPT-4o through the DSPy framework.

## Three-Stage Pipeline

1. **Generate**: Two-step LLM extraction — first entities, then subject-predicate-object triples
2. **Aggregate**: Normalize and consolidate triples across documents (no LLM needed)
3. **Cluster**: Iterative LLM-based entity resolution merging synonyms via LLM-as-a-judge

## MINE Benchmark

KGGen introduced MINE (Measure of Information in Nodes and Edges), the first standardized benchmark for text-to-KG extraction:
- 100 Wikipedia-length articles, 15 ground-truth facts each
- KGGen: 66.07% | GraphRAG: 47.80% | OpenIE: 29.84%

## Key Innovation

The clustering phase produces dense, well-connected graphs (suitable for TransE embeddings) by merging synonymous entities and relations, avoiding the sparsity problem of alternatives.

## Mentioned In

- [[sources/kggen-knowledge-graph-extraction]] — full pipeline, MINE benchmark, results
