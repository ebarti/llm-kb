---
title: "KARMA: Leveraging Multi-Agent LLMs for Automated Knowledge Graph Enrichment"
source: "https://arxiv.org/abs/2502.06472"
author: "Research team (NeurIPS 2025 Spotlight)"
date_published: 2025-02-10
date_ingested: 2026-04-05
tags: [knowledge-graph, multi-agent, llm, entity-extraction, relation-extraction]
type: paper
status: raw
discovered_via: search
---

# KARMA: Leveraging Multi-Agent LLMs for Automated Knowledge Graph Enrichment

## Abstract

KARMA automates knowledge graph (KG) enrichment by analyzing unstructured text using multiple collaborative LLM agents. The system addresses the challenge of maintaining current, comprehensive KGs as scientific literature grows rapidly.

## Key Contributions

- **Multi-agent architecture**: Nine specialized agents working together for different tasks
- **Comprehensive pipeline**: Covers entity discovery, relation extraction, schema alignment, and conflict resolution
- **Iterative refinement**: Agents parse documents, verify extracted knowledge, and integrate findings into existing graph structures while maintaining domain-specific consistency

## Methodology

The framework employs nine collaborative agents that:
- Parse unstructured documents in a structured manner
- Verify extracted knowledge against existing data
- Integrate new information into graph structures
- Resolve conflicts through multi-layer assessments
- Maintain adherence to domain-specific schemas

## Findings

Testing on 1,200 PubMed articles across three domains demonstrated:
- **Entity identification**: Up to 38,230 new entities discovered
- **Accuracy**: 83.1% LLM-verified correctness
- **Conflict reduction**: 18.6% decrease in conflict edges through multi-layer assessments

## Recognition

Selected as a **Spotlight paper at NeurIPS 2025**.

## Significance for LLM Knowledge Bases

KARMA represents the research-grade counterpart to Karpathy's markdown-based approach. While Karpathy's system uses markdown files as the knowledge representation, KARMA builds formal graph structures. Both share:
- Multi-step pipeline from raw documents to structured knowledge
- LLM-driven extraction and linking
- Conflict detection and resolution mechanisms
- Incremental enrichment from new sources

The difference lies in representation: KARMA uses formal graph triplets (entity, relation, entity) with schema constraints, while Karpathy's approach uses natural-language markdown with wikilinks. KARMA is better suited for large-scale scientific domains; Karpathy's approach is better for personal, auditable, human-readable knowledge bases.
