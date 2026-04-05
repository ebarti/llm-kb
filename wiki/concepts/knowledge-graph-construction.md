---
title: "Knowledge Graph Construction"
type: concept
sources: ["[[sources/llm-kg-construction-survey]]", "[[sources/kggen-knowledge-graph-extraction]]", "[[sources/graphrag-microsoft-research]]", "[[sources/karma-multi-agent-knowledge-graph]]"]
related: ["[[concepts/knowledge-graph]]", "[[concepts/knowledge-extraction]]", "[[concepts/knowledge-fusion]]", "[[concepts/ontology-engineering]]", "[[concepts/multi-agent-systems]]"]
last_compiled: 2026-04-05
summary: "The end-to-end process of building knowledge graphs from unstructured data, now transformed by LLMs from rule-based pipelines to generative frameworks achieving near-human-expert quality."
---

## Overview

Knowledge graph construction is the process of converting unstructured or semi-structured data into structured knowledge graphs consisting of entities, relations, and facts. With the advent of LLMs, this field has undergone a paradigm shift — from rule-based and statistical NLP pipelines requiring thousands of labeled examples to language-driven generative frameworks that work with few-shot prompting or zero-shot extraction.

## The Three Pipeline Stages

### 1. Ontology Engineering

Defines the schema (types of entities, types of relations, constraints) that the knowledge graph will follow. See [[concepts/ontology-engineering]] for details.

- **Top-down**: Expert-defined or LLM-assisted ontology creation from requirements (competency questions → OWL)
- **Bottom-up**: Data-driven schema induction from extracted instances (AutoSchemaKG, EDC framework)
- **Schema-free**: No predefined schema; entities and relations emerge from text (open information extraction)

### 2. Knowledge Extraction

Extracts entities, relations, and facts from source text. See [[concepts/knowledge-extraction]] for details.

- **Named Entity Recognition (NER)**: Identifying entities (people, places, concepts)
- **Relation Extraction**: Identifying relationships between entities
- **Event Extraction**: Identifying complex event structures with participants and temporal context

### 3. Knowledge Fusion

Merges, deduplicates, and reconciles extracted knowledge. See [[concepts/knowledge-fusion]] for details.

- **Entity alignment**: Recognizing that different mentions refer to the same entity
- **Schema reconciliation**: Aligning different ontological frameworks
- **Conflict resolution**: Handling contradictory information from different sources

## LLM-Driven Approaches

### Schema-Based Methods

Use predefined or LLM-generated ontologies to guide extraction:
- **KARMA** ([[entities/karma-framework]]): 9-agent multi-agent architecture for schema-guided extraction from PubMed papers
- **ODKE+**: Ontology snippets (dynamically selected subsets) for context-aware prompt construction
- **AdaKGC**: Schema-Enriched Prefix Instruction + Schema-Constrained Dynamic Decoding for runtime schema adaptation

### Schema-Free Methods

Extract knowledge without predefined schemas:
- **[[entities/kggen]]**: Three-stage pipeline (extract → aggregate → cluster) achieving 66% on MINE benchmark
- **Chain-of-Thought prompting**: Stepwise reasoning without external schemas
- **ChatIE**: Multi-turn dialogue extraction for iterative refinement
- **EDC (Extract-Define-Canonicalize)**: Few-shot prompting → raw triples → definition → normalization

### Hybrid Methods

- **AutoSchemaKG**: Bridges schema-based and schema-free via unsupervised clustering for enterprise-scale deployment
- **[[entities/microsoft-graphrag]]**: Builds entity-relationship graphs from text then applies community detection

## Performance

Few-shot prompting with GPT-4 or Claude achieves accuracy roughly equivalent to — and sometimes superior to — fully supervised traditional models. LLMs approach junior human modeler quality in autonomous ontology generation, independently identifying classes, properties, and generating logically consistent axioms.

Key benchmark: [[entities/kggen]] achieves 66.07% on MINE vs. GraphRAG's 47.80% and OpenIE's 29.84%.

## Current Limitations

1. **Semantic heterogeneity**: Merging knowledge from diverse sources remains challenging
2. **Scale**: Processing millions of documents requires efficient batching and deduplication
3. **Dynamic updating**: Most pipelines are batch-oriented; real-time graph evolution is an open problem
4. **Validation**: Automated quality assessment of extracted knowledge is immature

## Future Directions

The [[sources/llm-kg-construction-survey]] identifies key trends:
- KGs as dynamic knowledge memory for LLM agents
- Multimodal KG construction (vision + language)
- KGs as cognitive middle layers beyond simple retrieval
- Evolution from static schemas toward dynamic induction

## Sources

- [[sources/llm-kg-construction-survey]] — comprehensive 2025 survey of the field
- [[sources/kggen-knowledge-graph-extraction]] — state-of-the-art extraction pipeline
- [[sources/graphrag-microsoft-research]] — Microsoft's graph construction for RAG
- [[sources/karma-multi-agent-knowledge-graph]] — multi-agent approach

## Related Concepts

- [[concepts/knowledge-graph]] — the output artifact
- [[concepts/knowledge-extraction]] — entity and relation extraction stage
- [[concepts/knowledge-fusion]] — deduplication and merging stage
- [[concepts/ontology-engineering]] — schema design stage
