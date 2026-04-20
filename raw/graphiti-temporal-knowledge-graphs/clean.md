---
title: "Graphiti: Temporal Context Graphs for AI Agents"
source: "https://github.com/getzep/graphiti"
author: "Zep AI"
date_published: 2024-10-01
date_ingested: 2026-04-05
tags: [knowledge-graph, temporal, ai-agents, rag, hybrid-retrieval, open-source]
type: repo
status: raw
discovered_via: search
---

# Graphiti: Temporal Context Graphs for AI Agents

## What is Graphiti?

Graphiti is an open-source framework for building and querying temporal context graphs designed specifically for AI agents. Unlike traditional knowledge graphs, it tracks how facts change over time while maintaining full provenance to source data.

## Core Concept: Context Graphs

A context graph represents entities, relationships, and facts with temporal validity windows. As stated in the README: "A context graph is a temporal graph of entities, relationships, and facts" that captures when information became true and when it was superseded. This differs fundamentally from static knowledge graphs by preserving historical context.

## Key Components

The framework consists of four essential elements:

- **Entities (nodes)**: Represent people, products, concepts with evolving summaries
- **Facts/Relationships (edges)**: Triplets with temporal validity windows
- **Episodes**: Raw ingested data serving as ground truth; every derived fact traces back here
- **Custom Types (ontology)**: Developer-defined entity and edge types via Pydantic models

## Why Graphiti Matters

Traditional RAG approaches struggle with frequently changing data. Graphiti addresses this through:

- **Temporal management**: Facts have validity windows; old facts are invalidated, not deleted
- **Incremental updates**: New data integrates without batch recomputation
- **Hybrid retrieval**: Combines semantic, keyword (BM25), and graph-based search
- **Provenance tracking**: Full lineage from derived facts to source data

## Graphiti vs. Zep

Graphiti is the **open-source temporal context graph engine**, while Zep provides enterprise-grade managed infrastructure. Choose Graphiti for flexibility and self-hosting; choose Zep for turnkey, production-ready deployment.

## Comparison with Karpathy's Markdown Approach

| Dimension | Graphiti | Karpathy/Markdown Wiki |
|-----------|----------|------------------------|
| Representation | Graph triplets (entity, relation, entity) | Markdown files + wikilinks |
| Temporality | Built-in time windows | Manual, via file dates |
| Retrieval | Hybrid (semantic + BM25 + graph) | LLM reads index files |
| Auditability | Episodes as provenance | raw/ files as provenance |
| Scale | Production/enterprise | Personal (~100 articles) |
| Infrastructure | Neo4j / graph database | File system + LLM API |
| Learning curve | Higher (graph concepts) | Lower (markdown) |

Graphiti occupies the middle ground between simple markdown wikis and full enterprise knowledge graphs: more structured than Karpathy's approach but more accessible than KARMA's formal ontology system.
