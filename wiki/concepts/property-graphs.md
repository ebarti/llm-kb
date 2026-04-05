---
title: "Property Graphs"
type: concept
sources: ["[[sources/rdf-vs-property-graph-comparison]]", "[[sources/allemang-llms-kg-property-graphs]]", "[[sources/gallagher-second-brain-knowledge-graphs]]"]
related: ["[[concepts/rdf-knowledge-representation]]", "[[concepts/knowledge-graph]]", "[[concepts/ontology-engineering]]"]
last_compiled: 2026-04-05
summary: "Node-centric graph data model where nodes and edges carry rich attribute data, optimized for traversal performance and developer experience — the dominant model for production knowledge graph applications."
---

## Overview

Property graphs are a graph data model where entities are represented as nodes with labels and key-value properties, connected by typed, directed edges that also carry properties. Unlike [[concepts/rdf-knowledge-representation]], which decomposes everything into atomic triples, property graphs treat nodes and edges as rich, self-contained objects.

This model is the foundation of popular graph databases including Neo4j, Amazon Neptune, TigerGraph, and Memgraph, and is the dominant approach for production [[concepts/knowledge-graph]] applications in 2025.

## Data Model

### Nodes

- Identified by database-assigned internal IDs
- Classified by human-readable labels (e.g., :Person, :Company, :Document)
- Carry arbitrary key-value properties (name: "Alice", age: 30)

### Edges (Relationships)

- Typed and directed (e.g., WORKS_FOR, AUTHORED, RELATED_TO)
- Carry their own properties (since: "2020-01-01", weight: 0.85)
- Connect exactly two nodes (source → target)

### vs. RDF

| Dimension | Property Graph | RDF |
|-----------|---------------|-----|
| Orientation | Node-centric | Edge-centric |
| Identity | Internal DB IDs | Global URIs |
| Properties | On nodes and edges | Separate triples |
| Schema | Optional | OWL/RDFS formalized |
| Reasoning | Custom logic | Automated inference |
| Query Language | Cypher, Gremlin, GQL | SPARQL |

## Query Languages

### Cypher (Neo4j)

Declarative pattern-matching with ASCII-art syntax:
```cypher
MATCH (p:Person)-[:WORKS_FOR]->(c:Company {name: "Acme"})
RETURN p.name, p.role
```

### Gremlin (Apache TinkerPop)

Imperative traversal-oriented:
```gremlin
g.V().hasLabel('Person').out('WORKS_FOR').has('name', 'Acme')
```

### GQL (ISO Standard)

Emerging ISO standard aiming to unify property graph query languages, closing the standardization gap with SPARQL.

## Strengths

- **Performance**: Optimized for high-velocity traversal and real-time analytics
- **Developer experience**: Schema-optional; start building without upfront ontology design
- **Rich context**: Properties directly on nodes and edges without triple decomposition
- **Scalability**: Handles big data with optimized index-free adjacency

## LLM Integration

Property graphs align with several key LLM workflows:

- **Text2Cypher**: LLMs generate Cypher queries from natural language, made more accurate when guided by OWL ontology summaries (per [[sources/allemang-llms-kg-property-graphs]])
- **Embedding-centric AI**: Property graphs store entity embeddings as node properties, supporting vector search alongside graph traversal
- **Neo4j LLM Knowledge Graph Builder**: Extracts entities and relationships from text into a property graph, combining lexical graph (documents/chunks with embeddings) and entity graph (nodes and relationships)
- **GraphRAG**: While conceptually using triple-like structures, practical implementations often land in property graph databases

## The Ontology Bridge

Dean Allemang resolves the "false dichotomy" between property graphs and ontologies: OWL ontologies define the conceptual framework, property graphs instantiate the data. The practical workflow is:

1. Define domain concepts in OWL
2. Map to property graph structures via R2RML
3. Provision graph database aligned to ontology
4. Provide ontology summary to LLMs for query generation

## Practical Implementations

- **Neo4j**: Market leader; LLM Knowledge Graph Builder, GraphRAG integration
- **TigerGraph**: High-performance analytics workloads
- **Amazon Neptune**: Managed service supporting both property graph and RDF
- **Gallagher's Knowledge Graph Kit** ([[sources/gallagher-second-brain-knowledge-graphs]]): SQLite-based personal property graph with ChromaDB semantic search

## Sources

- [[sources/rdf-vs-property-graph-comparison]] — detailed comparison with RDF
- [[sources/allemang-llms-kg-property-graphs]] — ontology + property graph workflow
- [[sources/gallagher-second-brain-knowledge-graphs]] — personal-scale implementation

## Related Concepts

- [[concepts/rdf-knowledge-representation]] — the alternative formal model
- [[concepts/knowledge-graph]] — the broader concept both implement
- [[concepts/ontology-engineering]] — designing schemas for property graphs
