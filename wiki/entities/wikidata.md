---
title: "Wikidata"
type: entity
entity_type: tool
sources: ["[[sources/ai-in-wikimedia-projects]]", "[[sources/federated-wiki-cunningham]]"]
related: ["[[concepts/knowledge-graph]]", "[[concepts/federated-knowledge]]", "[[concepts/knowledge-commons]]", "[[entities/wikipedia]]"]
last_compiled: 2026-04-05
summary: "Wikimedia's collaboratively edited structured knowledge base — 100M+ items in semantic triple format, linked to 7,500+ external databases, forming the backbone of federated knowledge graph infrastructure."
---

## Overview

Wikidata is a free, collaborative, multilingual knowledge base operated by the Wikimedia Foundation as a sister project to [[entities/wikipedia]]. It stores structured data in semantic triple format (subject-property-value) and serves as a central hub for linked data across the Wikimedia ecosystem and beyond.

## Key Facts

- Founded: 2012
- Items: 100+ million
- Properties: 10,000+
- License: CC0 (public domain)
- External links: 7,500+ websites, catalogs, and databases (OpenStreetMap, MusicBrainz, Amazon, Apple, Google, OpenAI)
- Access: Live SPARQL endpoint, RDF dumps, linked data APIs

## Technical Architecture

Wikidata uses **semantic triples** (item + property + value) as its fundamental data model. Items represent subjects, properties represent predicates, and values represent objects. This structure enables:
- **SPARQL queries**: Complex questions across the entire knowledge base
- **Federated queries**: Spanning multiple Wikibase instances
- **Linked data**: Integration with the broader Semantic Web

## Significance for AI

Wikidata serves as both training resource and evaluation benchmark for AI systems. Computer scientists have used it "as a source of factual knowledge to train language models." It represents a [[concepts/knowledge-commons]] of structured data with community governance — a model for how shared knowledge infrastructure might be governed in the AI era.

## Mentioned In

- [[sources/ai-in-wikimedia-projects]] — as part of the Wikimedia AI ecosystem
- [[sources/federated-wiki-cunningham]] — Wikibase federation architecture
