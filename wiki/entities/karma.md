---
title: "KARMA"
type: entity
entity_type: paper
sources: ["[[sources/karma-multi-agent-knowledge-graph]]"]
related: ["[[concepts/knowledge-graph]]", "[[concepts/multi-agent-systems]]", "[[concepts/llm-knowledge-base]]", "[[entities/andrej-karpathy]]"]
last_compiled: 2026-04-06
summary: "A NeurIPS 2025 Spotlight paper presenting a nine-agent LLM framework for automated knowledge graph enrichment from unstructured scientific text."
reading_time: "2 min"
---

## Overview

KARMA (Knowledge graph enrichment through Automated Retrieval and Multi-Agent systems) is a research framework published as a Spotlight paper at NeurIPS 2025. It automates the enrichment of knowledge graphs from unstructured text using nine collaborative LLM agents, each specialized for a distinct phase of the extraction pipeline. The system was evaluated on 1,200 PubMed articles across three scientific domains, discovering up to 38,230 new entities with 83.1% LLM-verified correctness and achieving an 18.6% reduction in conflict edges through multi-layer assessments.

KARMA represents the research-grade counterpart to Karpathy's markdown-based wiki approach. While both systems share the core architecture of converting raw documents into structured knowledge through LLM pipelines, KARMA produces formal graph triplets (entity, relation, entity) with schema constraints, whereas Karpathy produces human-readable markdown files with wikilinks.

## Key Features

- **Nine specialized agents**: Document parser, entity discoverer, relation extractor, schema aligner, conflict detector, conflict resolver, knowledge integrator, verifier, and schema validator. Each agent focuses on a single task, passing results to downstream agents and challenging each other's outputs.

- **Formal graph representation**: Knowledge is stored as triplets with domain-specific schema constraints, enabling structured querying and formal reasoning that markdown-based approaches cannot support.

- **Conflict resolution**: A multi-layer assessment mechanism where distinct agents independently evaluate the same facts, achieving 18.6% reduction in conflicting edges. This is a significant advantage over single-LLM approaches where contradictions may go undetected.

- **Schema adherence**: Domain-specific schemas constrain what types of entities and relationships are valid, preventing the LLM from generating structurally invalid knowledge.

- **Scalability**: Tested on thousands of scientific papers, well beyond the ~100-article sweet spot of Karpathy's personal wiki approach.

## Role in LLM Knowledge Bases

KARMA establishes the upper bound of automated knowledge extraction quality for formal knowledge graphs. It demonstrates that multi-agent LLM pipelines can achieve research-grade accuracy in entity and relation extraction, validating the core thesis of [[concepts/multi-agent-systems]] for knowledge management. However, its formal graph output trades the human readability and auditability of Karpathy's markdown approach for structural precision and scalability. The comparison between these approaches illustrates a fundamental design axis: formal graphs for machine-queryable precision vs. markdown for human-auditable transparency.

## Mentioned In

- [[sources/karma-multi-agent-knowledge-graph]] -- full paper description, methodology, results, and contrast with Karpathy's markdown approach
