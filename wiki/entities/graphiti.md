---
title: "Graphiti"
type: entity
entity_type: tool
sources: ["[[sources/graphiti-temporal-knowledge-graphs]]"]
related: ["[[concepts/knowledge-graph]]", "[[concepts/temporal-knowledge]]", "[[entities/zep]]", "[[concepts/rag-vs-index-based-retrieval]]", "[[comparisons/knowledge-graph-vs-wiki]]"]
last_compiled: 2026-04-06
summary: "An open-source framework by Zep for building temporal context graphs where facts have validity windows, designed for AI agents operating in dynamic environments."
reading_time: "3 min"
---

## Overview

Graphiti is an open-source framework developed by [[entities/zep]] for building and querying temporal context graphs designed specifically for AI agents. Unlike traditional knowledge graphs that treat facts as eternally true or false, Graphiti represents facts with temporal validity windows -- tracking when information became true and when it was superseded. This temporal awareness makes it uniquely suited for AI agents that need to reason over changing information in dynamic environments such as product management, competitive intelligence, and organizational knowledge.

Graphiti occupies the architectural middle ground between Karpathy's simple markdown wiki approach and heavyweight enterprise knowledge graph systems like KARMA. It provides more formal structure than markdown files (entities, relationships, and facts as first-class objects) while remaining more accessible than a full multi-agent ontology enrichment pipeline.

## Key Features

- **Temporal validity windows**: Every fact (relationship edge) has a `valid_from` and `valid_until` timestamp. Old facts are invalidated rather than deleted, preserving complete historical context. This enables queries like "what was true about X before date Y?" alongside "what is currently true about X?"

- **Four core components**: Entities (nodes with evolving summaries), Facts/Relationships (edges with time windows), Episodes (raw ingested data serving as ground truth), and Custom Types (developer-defined entity and edge types via Pydantic models).

- **Hybrid retrieval**: Combines three search methods -- semantic similarity, BM25 keyword matching, and graph traversal -- to provide more robust retrieval than any single approach. This hybrid strategy outperforms pure vector search or pure keyword search for knowledge graph queries.

- **Incremental updates**: New data integrates without batch recomputation of the entire graph. This incremental approach mirrors Karpathy's incremental wiki compilation but at the graph level.

- **Full provenance**: Every derived fact traces back to its source Episode, paralleling how Karpathy's wiki traces all claims back to `raw/` files. This enables auditability and error correction.

- **Neo4j backend**: Uses Neo4j as the graph database, providing mature graph query capabilities and visualization tools.

## Role in LLM Knowledge Bases

Graphiti addresses a key limitation of Karpathy's markdown wiki: temporal reasoning. Markdown files handle temporality only through file modification dates and manual notes, which is adequate for static research knowledge (papers do not change) but insufficient for operational knowledge that evolves over time (org charts, product roadmaps, competitive landscapes). Graphiti's explicit temporal model fills this gap.

The Episodes concept in Graphiti directly mirrors the `raw/` directory in Karpathy's system -- both serve as the immutable source of truth from which all derived knowledge is compiled. The key difference is that Graphiti stores derived knowledge as formal graph structures rather than markdown files, enabling structured queries and temporal reasoning at the cost of reduced human readability.

## Mentioned In

- [[sources/graphiti-temporal-knowledge-graphs]] -- full description of the framework, architecture, and comparison with markdown wiki and KARMA approaches
