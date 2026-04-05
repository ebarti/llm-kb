---
title: "Ontology and Taxonomy"
type: concept
sources: ["[[sources/earley-ontology-ia-role-in-ai]]", "[[sources/ek-taxonomy-ia-semantic-layer]]", "[[sources/ek-km-trends-2026]]"]
related: ["[[concepts/semantic-layer]]", "[[concepts/information-architecture]]", "[[concepts/knowledge-graph]]", "[[concepts/enterprise-knowledge-management]]", "[[concepts/cheap-ontology]]"]
last_compiled: 2026-04-05
summary: "Formal knowledge organization systems for enterprise AI. Taxonomy = hierarchical parent-child relationships (single-parent trees). Ontology = relationships across multiple taxonomies (multi-parent inheritance). Together they form the structural scaffolding of semantic layers. Ontology functions as 'master data management for AI' -- changes propagate automatically through associative relationships."
---

## Overview

Ontologies and taxonomies are formal knowledge organization systems that provide the structural scaffolding for enterprise knowledge management, AI systems, and [[concepts/semantic-layer]] implementations. While often conflated, they serve distinct purposes at different levels of representational power.

## The Knowledge Model Hierarchy

Per [[sources/earley-ontology-ia-role-in-ai]], knowledge structures progress along a continuum of increasing representational power:

| Level | What It Does | Example |
|-------|-------------|---------|
| **Controlled Vocabulary** | Standardizes terminology | Always use "client" not "customer" |
| **Thesaurus** | Identifies related terms | "client" = "customer" = "account holder" |
| **Taxonomy** | Establishes hierarchy | Products > Software > Enterprise > CRM |
| **Ontology** | Cross-taxonomy relationships | CRM-product *serves* Sales-department *using* Cloud-infrastructure |
| **Knowledge Graph** | Specific relationship instances | "Salesforce CRM serves Acme Corp Sales via AWS us-east-1" |

Each level adds representational power. Organizations typically start at the top and work down as their needs mature.

## Taxonomy

A taxonomy is a controlled vocabulary structured into hierarchies of broader-narrower (parent-child) relationships. Key characteristics:
- **Single-parent tree structure**: each concept has exactly one parent
- **Primary use**: tagging content for improved discoverability and retrieval
- **Operational roles** (per [[sources/ek-taxonomy-ia-semantic-layer]]):
  - Consistent naming across systems
  - Semantic context for AI disambiguation
  - Front/back-end alignment (not all concepts need to be visible to users)

## Ontology

An ontology represents "a set of concepts and categories in a subject area or domain that shows their properties and the relations between them." Key distinctions from taxonomy:
- **Multi-parent inheritance**: objects can relate to multiple parent categories simultaneously (a smartphone is both a communication device and a computing device)
- **Three relationship types**: equivalence (same concept, different terms), hierarchical (parent-child), associative (cross-taxonomy connections)
- **Functions as "master data management for AI"** (per [[sources/earley-ontology-ia-role-in-ai]]): structural frameworks encompassing workflows and business processes

### Scalability Advantage

When changes occur in an ontology, modifications propagate automatically through associative relationships, eliminating redundant recoding across multiple applications. This is a critical enterprise advantage: updating a product category once automatically updates every system that references it.

## Enterprise Applications

### AI Disambiguation
Taxonomy provides the context AI needs to distinguish between ambiguous terms. Without taxonomy, an AI system cannot tell whether "Mercury" refers to a planet, a chemical element, a car brand, or an internal product line. This is critical preparation for [[concepts/retrieval-augmented-generation]] and [[concepts/enterprise-search]] systems.

### Semantic Layer Foundation
Per [[sources/ek-taxonomy-ia-semantic-layer]], taxonomies and ontologies are core components of the [[concepts/semantic-layer]], working alongside business glossaries, controlled metadata, and data catalogs to provide a unified abstraction over organizational data.

### AI-Ready Knowledge Assets
Per [[sources/ek-km-trends-2026]], AI can now automate the standardization and enrichment of legacy content using taxonomies, accomplishing metadata enrichment and quality improvement in minutes rather than thousands of manual hours. Structured data professionals are increasingly adopting KM concepts (ontologies, controlled vocabularies) as the data and KM fields converge.

## Case Study: Cleveland Museum of Art

Per [[sources/earley-ontology-ia-role-in-ai]], the Cleveland Museum of Art developed an ontology connecting geo-spatial data with behavioral analytics. By correlating visitor interactions with collection characteristics, themes, and locations, the institution improved experience personalization -- demonstrating ontology's applicability beyond traditional enterprise IT.

## Governance

Per [[sources/ek-taxonomy-ia-semantic-layer]], taxonomies must be governed outside individual system implementations (CMS, DAM, CRM) that may contain their own taxonomy features. Best practice: build on open W3C standards, specifically **SKOS** (Simple Knowledge Organization System), ensuring interoperability and avoiding vendor lock-in.

## Relationship to Cheap Ontology

[[concepts/cheap-ontology]] describes how LLM wikis can replace formal ontology efforts costing $10M-$20M. The distinction matters at scale: personal-scale systems can rely on LLM understanding as an implicit ontology; enterprise systems typically need explicit, governed ontologies to ensure consistency across thousands of users and dozens of applications. However, LLMs are increasingly used to accelerate formal ontology construction, reducing the cost/time barrier.

## Sources

- [[sources/earley-ontology-ia-role-in-ai]] -- knowledge model hierarchy and ontology as master data management for AI
- [[sources/ek-taxonomy-ia-semantic-layer]] -- taxonomy and IA as components of semantic layers
- [[sources/ek-km-trends-2026]] -- data adopting KM principles, AI-ready knowledge assets

## Related Concepts

- [[concepts/semantic-layer]] -- ontology and taxonomy are core components
- [[concepts/information-architecture]] -- the design discipline that applies ontologies
- [[concepts/knowledge-graph]] -- the most specific level of the hierarchy
- [[concepts/enterprise-knowledge-management]] -- the organizational context
- [[concepts/cheap-ontology]] -- the personal-scale LLM-powered alternative
