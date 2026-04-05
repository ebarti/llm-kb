---
title: "LLMs, Knowledge Graphs and Property Graphs"
source: "https://medium.com/@dallemang/llms-knowledge-graphs-and-property-graphs-5b6fc2cf9f55"
author: "Dean Allemang"
date_published: 2024-06-15
date_ingested: 2026-04-05
tags: [llm, knowledge-graph, property-graph, ontology, owl, cypher]
type: article
status: raw
discovered_via: search
---

# LLMs, Knowledge Graphs and Property Graphs

## Core Thesis

Allemang argues that LLMs have created a renaissance for ontologies. Rather than positioning property graphs and ontologies as competing approaches, he demonstrates they are complementary: ontologies provide the conceptual framework that gets instantiated within property graphs.

## False Dichotomy Resolution

The "question itself makes a false dichotomy" between property graphs and ontologies. In Jesus Barrasa's Neo4j demonstration, an OWL ontology structures the business concepts that then organize the actual graph data. The ontology exists whether explicitly defined or organically emergent.

## LLM Compatibility with Ontologies

LLMs understand formal ontological languages remarkably well. When provided with an OWL ontology summary, models like GPT-3.5 and GPT-4 successfully generated accurate Cypher queries without seeing actual data examples. This suggests "the LLM already speaks OWL well enough."

## Practical Workflow

1. Express business concepts as formal ontologies (OWL)
2. Map ontological concepts to physical data structures (R2RML)
3. Provision property graph databases aligned to the ontology
4. Provide ontology summaries (not data samples) to LLMs for query generation

## RAG and Scalability

For large ontologies exceeding context windows, Retrieval Augmented Generation becomes essential. "Knowledge-directed ways to do RAG that utilize the structure of OWL" prove more effective than vector-database approaches alone.

## Enterprise and Industry Benefits

Ontologies enable three governance levels:
1. Intra-enterprise communication between divisions
2. Inter-institutional industry coordination (exemplified by banking's EDMC)
3. Improved human-to-LLM communication
