---
title: "Schema-Guided and Ontology-Driven Extraction"
type: concept
sources: ["[[sources/ontogpt-ontology-extraction]]", "[[sources/llm-kg-construction-survey]]", "[[sources/willison-llm-schemas-structured-extraction]]"]
related: ["[[concepts/information-extraction]]", "[[concepts/structured-output-extraction]]", "[[concepts/knowledge-graph]]", "[[concepts/entity-linking]]", "[[concepts/cheap-ontology]]", "[[entities/ontogpt]]"]
last_compiled: 2026-04-05
summary: "Constraining LLM extraction with predefined schemas or ontologies — from static templates to dynamic, co-evolving schemas — trading flexibility for precision and consistency."
---

## Overview

Schema-guided extraction constrains what an LLM extracts by providing a predefined ontology, schema, or set of entity/relation types. Rather than open-ended extraction ("extract everything"), the LLM is told exactly what to look for ("extract Drug, Disease, and Treatment entities and their dosage_for relationships").

This approach represents a fundamental design choice in [[concepts/information-extraction]] pipelines: **precision vs. discovery**.

## The Schema Spectrum

### 1. Static Schema (Rigid)

Fully predefined ontologies ensure high consistency but limited adaptability. The LLM can only extract entities and relations defined in the schema.

**Example**: [[entities/ontogpt]] uses SPIRES with established biomedical ontologies — extracted entities must map to Gene Ontology terms, Disease Ontology terms, etc.

**Strengths**: High precision, ontology-aligned, no novel junk entities
**Weaknesses**: Misses novel entities, requires domain expertise to build schema, domain-specific

### 2. Dynamic/Adaptive Schema

The schema evolves during extraction. ODKE+ (Apple Research) dynamically selects ontology subsets relevant to each entity type, constructing context-aware prompts. AdaKGC handles schema evolution without model retraining via Schema-Enriched Prefix Instruction.

**Strengths**: Adapts to new entity types, balances precision and recall
**Weaknesses**: Complex implementation, schema quality depends on LLM

### 3. Schema-Free with Post-Hoc Clustering

No predefined schema — the LLM extracts freely, then clustering/canonicalization creates an emergent schema. [[entities/kggen]]'s approach: extract all entities and relations, then cluster synonyms into canonical forms.

**Strengths**: Maximum discovery, no domain expertise needed upfront
**Weaknesses**: Noisy initial extraction, requires expensive clustering step

## Schema Co-Evolution

From [[sources/llm-kg-construction-survey]], a key trend: "the progression from fixed schema control to selective, context-aware schema prompting marks the field's gradual shift toward more adaptive, data-responsive frameworks. Recent approaches reconceptualize the schema as a dynamic, evolving component rather than a fixed template."

This mirrors the [[concepts/cheap-ontology]] thesis: LLM wikis replace expensive enterprise ontologies with natural-language schemas that evolve alongside the knowledge base.

## Key Systems

| System | Schema Approach | Innovation |
|--------|----------------|------------|
| [[entities/ontogpt]] / SPIRES | Static (biomedical ontologies) | Zero-shot with ontology grounding |
| KARMA | Static (multi-agent) | 9 agents with schema-guided task execution |
| ODKE+ (Apple) | Dynamic (ontology snippets) | Context-aware prompt construction |
| AutoSchemaKG | Bottom-up induction | Unsupervised schema clustering from corpora |
| AdaKGC | Adaptive | Schema evolution without retraining |
| [[entities/kggen]] | Schema-free + clustering | Entity resolution as emergent schema |

## Relevance to Wiki Compilation

The [[concepts/wiki-compilation]] pipeline uses an implicit schema:
- **Entity types**: person, tool, org, paper, dataset (defined in CLAUDE.md)
- **Article types**: source-summary, concept, entity, comparison
- **Frontmatter fields**: title, type, sources, related, summary

This is a lightweight static schema. The wiki compiler could benefit from dynamic schema approaches — as new entity types emerge (e.g., "benchmark," "technique," "conference"), the schema should expand rather than force everything into existing categories.

## Sources

- [[sources/ontogpt-ontology-extraction]] — canonical static schema-guided extraction
- [[sources/llm-kg-construction-survey]] — full taxonomy from static to dynamic to schema-free
- [[sources/willison-llm-schemas-structured-extraction]] — JSON Schema as extraction constraint

## Related Concepts

- [[concepts/information-extraction]] — schema-guided is one approach to IE
- [[concepts/structured-output-extraction]] — the output mechanism for schema-guided extraction
- [[concepts/knowledge-graph]] — schemas define KG structure
- [[concepts/entity-linking]] — ontology grounding is a form of entity linking
- [[concepts/cheap-ontology]] — LLM-driven schema as affordable ontology replacement
