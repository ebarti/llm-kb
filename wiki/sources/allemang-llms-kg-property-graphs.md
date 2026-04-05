---
title: "Source: LLMs, Knowledge Graphs and Property Graphs"
type: source-summary
source: "[[raw/allemang-llms-kg-property-graphs]]"
related: ["[[concepts/ontology-engineering]]", "[[concepts/property-graphs]]", "[[concepts/rdf-knowledge-representation]]", "[[entities/dean-allemang]]"]
last_compiled: 2026-04-05
summary: "Dean Allemang argues LLMs have created a renaissance for ontologies, demonstrating that OWL ontologies and property graphs are complementary (not competing), and LLMs natively understand formal ontological languages."
---

## Key Points

- The property graph vs. ontology question is a "false dichotomy" — ontologies provide conceptual frameworks instantiated in property graphs
- LLMs (GPT-3.5, GPT-4) successfully generate accurate Cypher queries from OWL ontology summaries without seeing data
- Practical workflow: OWL ontology → R2RML mapping → property graph → LLM query generation
- Knowledge-directed RAG utilizing OWL structure outperforms vector-only approaches for large ontologies
- Ontologies enable governance at three levels: intra-enterprise, inter-institutional, human-to-LLM

## Detailed Summary

Allemang's analysis resolves a persistent debate in the knowledge graph community. Using Jesus Barrasa's Neo4j demonstration as evidence, he shows that an OWL ontology structures business concepts that then organize actual graph data — the ontology exists whether explicitly defined or organically emergent.

The most striking finding is that LLMs understand formal ontological languages remarkably well. When provided only an OWL ontology summary (no data examples), GPT-3.5 and GPT-4 generated accurate Cypher queries for Neo4j property graphs. This suggests ontologies serve as excellent interface specifications between human domain knowledge and LLM capabilities.

For large ontologies exceeding context windows, Allemang advocates for knowledge-directed RAG that utilizes OWL structure, which proves more effective than pure vector-database approaches.

## Related Concepts

- [[concepts/ontology-engineering]] — core topic: LLMs revitalizing formal ontologies
- [[concepts/property-graphs]] — demonstrated as complementary to ontologies
- [[concepts/rdf-knowledge-representation]] — OWL as the ontology language
