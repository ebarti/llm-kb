---
title: "Knowledge Graph"
type: concept
sources: ["[[sources/karma-multi-agent-knowledge-graph]]", "[[sources/gallagher-second-brain-knowledge-graphs]]", "[[sources/graphiti-temporal-knowledge-graphs]]", "[[sources/pebblous-cheap-ontology]]"]
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/cheap-ontology]]", "[[concepts/temporal-knowledge]]", "[[concepts/multi-agent-systems]]"]
last_compiled: 2026-04-05
summary: "Formal representation of knowledge as nodes (entities) and edges (relationships), with three distinct modern approaches: KARMA (automated multi-agent enrichment), Graphiti (temporal context graphs), and Gallagher's Knowledge Graph Kit (personal SQLite graph)."
---

## Overview

A knowledge graph represents information as a network of entities (nodes) and relationships (edges), enabling structured querying and reasoning that flat text doesn't support. LLMs have dramatically changed how knowledge graphs are built and maintained — shifting from expensive manual ontology engineering to automated extraction and enrichment.

## Three Modern LLM-Powered Approaches

### KARMA (Research-Grade Automated Enrichment)
- **Architecture**: 9 collaborative LLM agents (entity discovery, relation extraction, schema alignment, conflict resolution)
- **Input**: Unstructured scientific text (PubMed articles)
- **Output**: Formal graph triplets with schema validation
- **Performance**: 83.1% accuracy, 38,230 new entities from 1,200 papers, 18.6% conflict reduction
- **Best for**: Large-scale scientific literature domains
- **NeurIPS 2025 Spotlight**

### Graphiti (Temporal Context Graphs)
- **Architecture**: Open-source framework; episodes (raw) → entities/relationships (with time windows)
- **Key feature**: Facts have validity windows — when they became true and when superseded
- **Retrieval**: Hybrid (semantic + BM25 + graph traversal)
- **Best for**: AI agents operating in dynamic, changing environments
- **Open source** via Zep AI

### Knowledge Graph Kit (Personal Graph)
- **Architecture**: SQLite (nodes/edges) + ChromaDB (semantic search)
- **Node types**: Task, Note, Person, Project
- **Edge labels**: part_of, mentions, related_to
- **Best for**: Personal task/project/relationship management

## Knowledge Graphs vs. Markdown Wikis

| Dimension | Knowledge Graph | Markdown Wiki (Karpathy) |
|-----------|-----------------|--------------------------|
| Structure | Formal (triplets) | Implicit (wikilinks) |
| Queryability | Structured + semantic | LLM-mediated natural language |
| Temporality | Explicit (Graphiti) | Manual (file dates) |
| Auditability | Provenance to episodes | Provenance to raw/ files |
| Setup complexity | Higher | Lower |
| Scale | Enterprise to production | Personal |

## The Convergence

Both approaches share core principles: raw input preserved as source of truth, LLM-derived structured knowledge separate from raw, incremental enrichment from new sources, conflict detection. The difference is representation: formal graph triplets vs. human-readable markdown.

## Sources
- [[sources/karma-multi-agent-knowledge-graph]] — automated KG enrichment at research scale
- [[sources/graphiti-temporal-knowledge-graphs]] — temporal context graphs for AI agents
- [[sources/gallagher-second-brain-knowledge-graphs]] — personal SQLite graph approach
- [[sources/pebblous-cheap-ontology]] — historical context; KGs as expensive alternative to markdown wikis

## Related Concepts
- [[concepts/cheap-ontology]] — LLM wikis as low-cost alternative to KGs
- [[concepts/temporal-knowledge]] — Graphiti's temporal features
- [[concepts/multi-agent-systems]] — KARMA's multi-agent architecture
- [[concepts/llm-knowledge-base]] — the markdown-based alternative
