---
title: "Schema-Guided vs. Schema-Free Extraction"
type: comparison
subjects: ["[[concepts/schema-guided-extraction]]", "[[concepts/information-extraction]]"]
sources: ["[[sources/llm-kg-construction-survey]]", "[[sources/ontogpt-ontology-extraction]]", "[[sources/kggen-knowledge-graph-extraction]]"]
last_compiled: 2026-04-05
summary: "Schema-guided extraction (OntoGPT, KARMA) trades flexibility for precision; schema-free extraction (KGGen, OpenIE) discovers novel patterns but requires post-processing — hybrid approaches are converging."
---

## Overview

The fundamental design choice in LLM-based [[concepts/information-extraction]] is whether to constrain extraction with a predefined schema or let the LLM extract freely. This comparison examines the tradeoffs.

## Comparison Table

| Dimension | Schema-Guided | Schema-Free |
|-----------|--------------|-------------|
| **Precision** | High — only expected entities/relations | Lower — may produce noise |
| **Recall / Discovery** | Low — misses novel entities | High — discovers unexpected patterns |
| **Consistency** | High — canonical names enforced | Low — synonym variations abound |
| **Domain expertise needed** | Yes — schema must be designed | No — LLM discovers structure |
| **Setup cost** | High — ontology development | Low — prompt and extract |
| **Post-processing** | Minimal | Extensive (clustering, canonicalization) |
| **Scalability** | Limited cross-domain | Flexible across domains |
| **Example systems** | [[entities/ontogpt]], KARMA, ODKE+ | [[entities/kggen]], OpenIE, ChatIE |

## When to Use Each

### Schema-Guided
- Domain is well-defined (biomedical, legal, financial)
- Established ontologies exist (Gene Ontology, SNOMED CT)
- Precision matters more than recall
- Output feeds into structured databases or compliance systems
- Multiple users need consistent entity naming

### Schema-Free
- Exploratory research across diverse topics
- Building a [[concepts/llm-knowledge-base]] from heterogeneous sources
- No domain expert available to build a schema
- Discovery of unexpected entities and relationships is valuable
- Output feeds into flexible representations (markdown wiki, graph visualization)

### Hybrid (Best of Both)
The [[sources/llm-kg-construction-survey]] identifies a convergence trend: dynamic schemas that start open and converge toward consistency:

1. **Extract freely** (schema-free generation)
2. **Cluster and canonicalize** (emergent schema via entity resolution)
3. **Formalize** (induce schema from extracted patterns)

This is KGGen's approach and the direction the field is moving.

## Relevance to Wiki Compilation

The [[concepts/wiki-compilation]] pipeline currently uses a lightweight static schema (entity types: person, tool, org, paper, dataset). This comparison suggests it could benefit from:

1. **Schema-free extraction** during initial ingest (discover all entities)
2. **Schema-guided classification** during compilation (categorize into known types)
3. **Dynamic schema expansion** when novel entity types emerge

## Sources

- [[sources/llm-kg-construction-survey]] — full taxonomy of schema approaches and evolution trends
- [[sources/ontogpt-ontology-extraction]] — canonical schema-guided approach
- [[sources/kggen-knowledge-graph-extraction]] — canonical schema-free-with-clustering approach
