---
title: "Knowledge Graph"
type: concept
sources: ["[[sources/karma-multi-agent-knowledge-graph]]", "[[sources/gallagher-second-brain-knowledge-graphs]]", "[[sources/graphiti-temporal-knowledge-graphs]]", "[[sources/pebblous-cheap-ontology]]", "[[sources/graphrag-microsoft-research]]", "[[sources/llm-kg-construction-survey]]", "[[sources/kg-vs-vector-db-glean]]", "[[sources/rdf-vs-property-graph-comparison]]", "[[sources/knowledge-graph-embeddings-overview]]", "[[sources/branzan-production-knowledge-graphs-2025]]", "[[sources/cio-knowledge-graphs-enterprise-ai]]"]
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/cheap-ontology]]", "[[concepts/temporal-knowledge]]", "[[concepts/multi-agent-systems]]", "[[concepts/graphrag]]", "[[concepts/knowledge-graph-construction]]", "[[concepts/knowledge-graph-embeddings]]", "[[concepts/rdf-knowledge-representation]]", "[[concepts/property-graphs]]", "[[concepts/hybrid-retrieval]]", "[[concepts/enterprise-knowledge-management]]", "[[concepts/knowledge-system-scaling]]", "[[concepts/semantic-layer]]", "[[concepts/ontology-and-taxonomy]]"]
last_compiled: 2026-04-05
summary: "Formal representation of knowledge as nodes (entities) and edges (relationships), with three distinct modern approaches: KARMA (automated multi-agent enrichment), Graphiti (temporal context graphs), and Gallagher's Knowledge Graph Kit (personal SQLite graph)."
reading_time: "2 min"
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

## Graph Data Models

Knowledge graphs can be implemented using two fundamentally different data models (see [[comparisons/rdf-vs-property-graph]]):

- **[[concepts/rdf-knowledge-representation]]**: Edge-centric triples (subject-predicate-object) with URIs, W3C standards, SPARQL queries, and OWL reasoning. Best for formal reasoning and global interoperability.
- **[[concepts/property-graphs]]**: Node-centric with rich properties on both nodes and edges. Cypher/Gremlin queries. Best for traversal performance and developer experience.

## Knowledge Graph Embeddings

[[concepts/knowledge-graph-embeddings]] map entities and relations to continuous vector spaces, enabling link prediction, entity classification, and knowledge graph completion. Key model families include TransE (translation-based), ComplEx (tensor decomposition), and RotatE (rotation-based). These are increasingly complemented by LLM approaches that outperform them on multi-hop reasoning tasks (see [[sources/kg-llm-link-prediction]]).

## GraphRAG

[[concepts/graphrag]] represents a major application of knowledge graphs for LLM retrieval, where graphs are constructed from text via LLM extraction, organized via community detection, and queried through hierarchical summarization — dramatically outperforming baseline vector RAG on holistic and cross-document queries.

## Enterprise Production Deployments (2025)

Per [[sources/branzan-production-knowledge-graphs-2025]] and [[sources/cio-knowledge-graphs-enterprise-ai]], knowledge graph construction reached production maturity in 2024-2025, delivering 300-320% ROI across finance, healthcare, and manufacturing.

### Production-Ready Tools
- **[[entities/falkordb]]**: Sub-50ms latency, 90% hallucination reduction, multi-model support
- **[[entities/cognee]]**: Cognitive memory for agentic AI, hybrid graph+vector, incremental learning
- **Microsoft GraphRAG**: Community detection, 70-80% win rate over naive RAG, 97% fewer tokens
- **LightRAG**: 10x token reduction, 65-80% cost savings at scale, incremental updates

### Real-World Deployments
- **[[entities/novartis]]**: Drug discovery KG linking genes, diseases, and compounds
- **Intuit**: Security knowledge platform on [[entities/neo4j]], 75 million hourly updates
- **LinkedIn**: RAG + KG improved customer service accuracy 78%, reduced resolution time 29%
- **Financial services**: Fine-tuned Mistral-7B achieves 91.3% entity F1 at $1,200 (vs. $8,500 zero-shot)

### Decision Boundaries
- <1,500 documents: prompt-based extraction (70-80% accuracy)
- >1,500 documents: fine-tuned models (210% improvement over zero-shot)
- Schema design: 3-7 node types, 5-15 relationship types (80/20 rule)

Despite these advances, production deployments remain relatively rare. Per CIO: "If you haven't yet built a knowledge graph, then you've got this whole big project to go through first." Gartner places GraphRAG 2-5 years from mainstream maturity.

## Sources
- [[sources/karma-multi-agent-knowledge-graph]] — automated KG enrichment at research scale
- [[sources/graphiti-temporal-knowledge-graphs]] — temporal context graphs for AI agents
- [[sources/gallagher-second-brain-knowledge-graphs]] — personal SQLite graph approach
- [[sources/pebblous-cheap-ontology]] — historical context; KGs as expensive alternative to markdown wikis
- [[sources/graphrag-microsoft-research]] — GraphRAG: graph-based retrieval augmented generation
- [[sources/llm-kg-construction-survey]] — comprehensive survey of LLM-driven KG construction
- [[sources/kg-vs-vector-db-glean]] — knowledge graphs vs vector databases
- [[sources/rdf-vs-property-graph-comparison]] — RDF vs property graph data models
- [[sources/knowledge-graph-embeddings-overview]] — embedding methods for KGs
- [[sources/branzan-production-knowledge-graphs-2025]] — production-ready KG tools and benchmarks
- [[sources/cio-knowledge-graphs-enterprise-ai]] — enterprise KG deployment status and real-world examples

## Related Concepts
- [[concepts/cheap-ontology]] — LLM wikis as low-cost alternative to KGs
- [[concepts/temporal-knowledge]] — Graphiti's temporal features
- [[concepts/multi-agent-systems]] — KARMA's multi-agent architecture
- [[concepts/llm-knowledge-base]] — the markdown-based alternative
- [[concepts/graphrag]] — graph-based retrieval augmented generation
- [[concepts/knowledge-graph-construction]] — building KGs from unstructured data
- [[concepts/knowledge-graph-embeddings]] — vector representations of KG structure
- [[concepts/rdf-knowledge-representation]] — RDF/OWL data model
- [[concepts/property-graphs]] — property graph data model
- [[concepts/hybrid-retrieval]] — combining graph and vector search

## Related Entities

- [[entities/karma]] — nine-agent KG enrichment (NeurIPS 2025)
- [[entities/graphiti]] — temporal context graphs by [[entities/zep]]
- [[entities/sam-gallagher]] — Knowledge Graph Kit (SQLite + ChromaDB)
- [[entities/neo4j]] — graph database backend for Graphiti
- [[entities/sqlite]], [[entities/chromadb]] — storage for Knowledge Graph Kit

## Related Comparisons

- [[comparisons/knowledge-graph-vs-wiki]] — formal graphs vs. markdown wikis
- [[comparisons/obsidian-vs-graph-database]] — file-based vs. database storage
