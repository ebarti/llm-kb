---
title: "RDF Knowledge Representation"
type: concept
sources: ["[[sources/rdf-vs-property-graph-comparison]]", "[[sources/allemang-llms-kg-property-graphs]]", "[[sources/llm-kg-construction-survey]]"]
related: ["[[concepts/property-graphs]]", "[[concepts/knowledge-graph]]", "[[concepts/ontology-engineering]]"]
last_compiled: 2026-04-05
summary: "The W3C-standardized Resource Description Framework for representing knowledge as subject-predicate-object triples with URIs, SPARQL queries, and OWL reasoning — the semantic web foundation for formal knowledge graphs."
---

## Overview

RDF (Resource Description Framework) is the W3C-standardized data model for knowledge representation. It structures knowledge as triples — (subject, predicate, object) — where each element is identified by a URI/IRI, enabling global interoperability across datasets and organizations. Combined with RDFS (RDF Schema) and OWL (Web Ontology Language), RDF provides the most formal and reasoning-capable foundation for [[concepts/knowledge-graph]] systems.

## Data Model

### The Triple

The atomic unit of RDF is the triple: (subject, predicate, object).

- **Subject**: A URI identifying the entity being described
- **Predicate**: A URI identifying the property or relationship
- **Object**: A URI (another entity) or a literal value (string, number, date)

Example: `(dbpedia:Barack_Obama, dbo:birthPlace, dbpedia:Honolulu)`

### Edge-Centric Design

RDF is fundamentally edge-centric — relationships are first-class citizens. This contrasts with [[concepts/property-graphs]], which are node-centric. Every piece of information is decomposed into atomic triples, maximizing semantic granularity.

## Semantic Technologies Stack

### RDFS (RDF Schema)

Defines class hierarchies (rdfs:subClassOf), property domains and ranges, and basic type constraints. Provides the foundation for simple ontologies.

### OWL (Web Ontology Language)

Builds on RDFS with richer expressiveness:
- **Class restrictions**: "A FoodLover is any Person who likes some Food"
- **Property characteristics**: Symmetric, transitive, functional, inverse
- **Logical axioms**: Disjointness, equivalence, cardinality constraints
- **Automated reasoning**: Deriving implicit knowledge from explicit axioms

### SHACL (Shapes Constraint Language)

Validates RDF data against shape constraints — structural schema validation for the graph.

### SPARQL

The W3C standard query language for RDF:
- Pattern-matching over triples
- Federated queries across multiple endpoints
- Aggregation, filtering, and optional matching
- Construct queries for graph transformation

## Reasoning and Inference

The core differentiator of RDF/OWL systems is automated reasoning:

- **Subsumption**: If A is a subclass of B, instances of A are automatically instances of B
- **Transitivity**: If A is part of B and B is part of C, then A is part of C
- **Inverse relations**: If A employs B, then B is employed by A
- **Logical consistency validation**: Detecting contradictions in the knowledge base

This ability to derive implicit knowledge and validate consistency is what makes RDF systems suitable for domains requiring formal correctness (healthcare, finance, legal).

## RDF and LLMs

LLMs interact with RDF in several important ways:

- **LLMs understand OWL**: As [[sources/allemang-llms-kg-property-graphs]] demonstrates, GPT-3.5/GPT-4 generate accurate queries from OWL ontology summaries without data examples
- **GraphRAG uses triple structure**: Most KAG and [[concepts/graphrag]] research uses RDF-style triple graphs because "LLM itself is semantically based and requires semantics"
- **Knowledge-directed RAG**: OWL structure enables more effective RAG than vector-only approaches for large ontologies
- **LLM-driven ontology construction**: LLMs can generate OWL ontologies from natural language requirements (see [[concepts/ontology-engineering]])

## Serialization Formats

- **Turtle**: Human-readable, compact
- **JSON-LD**: JSON-compatible, web-friendly
- **RDF/XML**: Original XML serialization
- **N-Triples**: One triple per line, simple parsing

## Limitations

- **Performance at scale**: High atomicity of triples makes analytics workloads slower than [[concepts/property-graphs]]
- **Complexity**: Steeper learning curve; requires understanding of semantic web stack
- **Verbosity**: Simple facts may require multiple triples to represent
- **Tooling**: Fewer developer-friendly tools compared to property graph databases

## Sources

- [[sources/rdf-vs-property-graph-comparison]] — detailed RDF vs property graph comparison
- [[sources/allemang-llms-kg-property-graphs]] — LLMs understanding OWL
- [[sources/llm-kg-construction-survey]] — RDF in LLM-driven KG construction

## Related Concepts

- [[concepts/property-graphs]] — the alternative graph data model
- [[concepts/knowledge-graph]] — RDF as one implementation approach
- [[concepts/ontology-engineering]] — OWL as the ontology formalism
