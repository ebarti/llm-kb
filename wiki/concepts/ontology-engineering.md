---
title: "Ontology Engineering"
type: concept
sources: ["[[sources/llm-kg-construction-survey]]", "[[sources/allemang-llms-kg-property-graphs]]", "[[sources/rdf-vs-property-graph-comparison]]", "[[sources/pebblous-cheap-ontology]]"]
related: ["[[concepts/knowledge-graph-construction]]", "[[concepts/rdf-knowledge-representation]]", "[[concepts/knowledge-graph]]", "[[concepts/cheap-ontology]]"]
last_compiled: 2026-04-05
summary: "The design of formal schemas (ontologies) that define entity types, relation types, and constraints for knowledge graphs — now increasingly automated by LLMs that achieve near-junior-expert quality."
---

## Overview

Ontology engineering is the process of designing the formal schema — the types of entities, types of relations, hierarchies, and constraints — that structures a [[concepts/knowledge-graph]]. Traditionally requiring specialized ontologists and months of manual work costing $10M-$20M for enterprise deployments (per [[concepts/cheap-ontology]]), LLMs are now automating much of this process.

## Top-Down Construction (LLMs as Assistants)

Human experts or LLMs define the ontology from requirements before data is processed:

### Competency Question Methods

1. Domain experts (or LLMs) formulate competency questions (CQs) — questions the ontology should be able to answer
2. CQs are translated into formal OWL classes, properties, and axioms
3. Notable systems:
   - **Ontogenia**: Metacognitive prompting + design patterns for ontology generation
   - **CQbyCQ**: Iterative CQ-driven ontology construction
   - **NeOn-GPT**: End-to-end LLM workflow for complex domains
   - **LLMs4Life**: Domain-specific ontology generation for life sciences

### Natural Language Extraction

Extract semantic structures directly from unstructured text, inferring class hierarchies and property definitions from language patterns.

## Bottom-Up Construction (Data-Driven Schema Induction)

Schemas emerge from the data rather than being imposed:

- **AutoSchemaKG**: Induces schemas from large corpora via unsupervised clustering, bridging schema-based and schema-free paradigms for enterprise-scale deployment
- **EDC (Extract-Define-Canonicalize)**: Extracts raw open triples, generates semantic definitions, then normalizes via vector similarity
- **AdaKGC**: Dynamic schema evolution without model retraining, using Schema-Enriched Prefix Instruction for runtime adaptation

## LLM Capabilities in Ontology Engineering

The [[sources/llm-kg-construction-survey]] documents that LLMs achieve performance approaching junior human modelers in autonomous ontology generation. They can independently:

- Identify classes and subclass hierarchies
- Define object and data properties
- Generate logically consistent axioms
- Produce OWL-formatted ontologies

[[sources/allemang-llms-kg-property-graphs]] demonstrates that LLMs "already speak OWL well enough" to generate accurate Cypher queries from ontology descriptions alone, without seeing actual data examples.

## The OWL + Property Graph Workflow

Dean Allemang's practical workflow bridges formal ontologies and graph databases:

1. Express domain concepts as OWL ontologies
2. Map ontological concepts to property graph structures via R2RML
3. Provision property graph databases aligned to the ontology
4. Provide ontology summaries to LLMs for query generation

This resolves the "false dichotomy" between [[concepts/property-graphs]] and formal ontologies — they are complementary, with ontologies providing conceptual frameworks that property graphs instantiate.

## Sources

- [[sources/llm-kg-construction-survey]] — comprehensive taxonomy of LLM-driven ontology engineering
- [[sources/allemang-llms-kg-property-graphs]] — practical OWL + property graph workflow
- [[sources/rdf-vs-property-graph-comparison]] — reasoning capabilities of ontological approaches
- [[sources/pebblous-cheap-ontology]] — historical context of ontology costs

## Related Concepts

- [[concepts/knowledge-graph-construction]] — ontology engineering as the first pipeline stage
- [[concepts/rdf-knowledge-representation]] — the formalism (OWL/RDFS) ontologies use
- [[concepts/cheap-ontology]] — LLMs democratizing ontology creation
- [[concepts/knowledge-graph]] — the artifact ontologies structure
