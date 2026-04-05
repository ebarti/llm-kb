---
title: "Neo4j"
type: entity
entity_type: tool
sources: ["[[sources/graphiti-temporal-knowledge-graphs]]"]
related: ["[[entities/graphiti]]", "[[concepts/knowledge-graph]]", "[[concepts/temporal-knowledge]]"]
last_compiled: 2026-04-06
summary: "A native graph database used as the backend for Graphiti's temporal context graphs, providing mature graph query and visualization capabilities."
reading_time: "2 min"
---

## Overview

Neo4j is the most widely adopted native graph database, storing data as nodes and relationships (edges) rather than tables or documents. It uses the Cypher query language for graph traversal, pattern matching, and pathfinding operations that are prohibitively expensive in relational databases. Neo4j is the backend for [[entities/graphiti]]'s temporal context graphs, providing the storage and query engine for entities, facts, and their temporal validity windows.

## Key Features

- **Native graph storage**: Data is stored as nodes and relationships on disk, enabling constant-time relationship traversal regardless of graph size. This contrasts with relational databases where joins become expensive as tables grow.

- **Cypher query language**: A declarative, pattern-based query language for expressing graph traversals (e.g., "find all entities connected to X through relationships of type Y that were valid before date Z").

- **Visualization tools**: Neo4j Browser and Neo4j Bloom provide interactive graph visualizations for exploring node-and-edge structures.

- **Enterprise features**: Clustering, role-based access control, and certified drivers for major programming languages support production deployments.

## Role in LLM Knowledge Bases

Neo4j provides the infrastructure that makes [[entities/graphiti]]'s temporal knowledge graph possible. While Karpathy's markdown wiki uses the file system as its database and wikilinks as its edges, Graphiti requires a proper graph database to support operations like temporal filtering (find facts valid at time T), graph traversal (find all entities N hops from entity X), and hybrid retrieval combining graph structure with semantic similarity. Neo4j supplies these capabilities, though at the cost of operational complexity that Karpathy's file-based approach avoids entirely.

## Mentioned In

- [[sources/graphiti-temporal-knowledge-graphs]] -- identified as the graph database backend for Graphiti's temporal context graphs
