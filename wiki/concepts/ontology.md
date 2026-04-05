---
title: "Ontology (Knowledge Engineering)"
type: concept
sources: ["[[sources/wikipedia-knowledge-representation-reasoning]]", "[[sources/wikipedia-semantic-web]]", "[[sources/wikipedia-cyc]]", "[[sources/pebblous-cheap-ontology]]"]
related: ["[[concepts/knowledge-representation]]", "[[concepts/semantic-web]]", "[[concepts/knowledge-graph]]", "[[concepts/cheap-ontology]]", "[[entities/cyc-project]]"]
last_compiled: 2026-04-05
summary: "Formal specification of concepts, relationships, and rules within a knowledge domain — from WordNet and Cyc through OWL/RDF to modern knowledge graphs, with LLM-era 'cheap ontology' as the latest evolution."
---

## Overview

In knowledge engineering, an ontology is a formal, explicit specification of a shared conceptualization. It defines the concepts, relationships, properties, and constraints within a domain, enabling machines to reason about that domain's knowledge.

Tom Gruber's insight captures the social dimension: "Every ontology is a treaty — a social agreement among people with common motive in sharing."

## Types and Scale

| Type | Scope | Example |
|------|-------|---------|
| Upper/foundational | Universal concepts (time, space, objects) | DOLCE, SUMO, [[entities/cyc-project]] |
| Domain | Specific field | SNOMED CT (370,000 medical terms), Gene Ontology |
| Application | Single system | A company's product taxonomy |
| Lightweight/folksonomy | Informal tags | Wikipedia categories, hashtags |

## Technical Standards

The [[concepts/semantic-web]] provides the formal standards for web ontologies:
- **RDF**: Subject-predicate-object triples (1999)
- **RDFS**: Vocabulary for classes and properties
- **OWL**: Full description logic with inference (2004, OWL 2 in 2009)
- **SPARQL**: Query language

## Historical Evolution

1. **Informal taxonomies** (pre-computer): Library classification systems (Dewey, Library of Congress)
2. **Semantic networks** (1960s): Graph representations of concept relationships
3. **Frames** (1970s, Minsky): Structured slots with inheritance
4. **KL-ONE and description logics** (1980s): Rigorous frame semantics with classification
5. **Cyc** (1984-present): Most ambitious ontology ever attempted (1.5M terms, 24.5M assertions)
6. **Web ontologies** (2000s): RDF/OWL make ontologies shareable on the web
7. **Knowledge graphs** (2012+): Google, Wikidata — lighter-weight, data-driven
8. **LLM-era "cheap ontology"** (2024+): Natural language schemas maintained by LLMs at a fraction of the cost

## The Cost Problem

Traditional ontology engineering is expensive. [[entities/cyc-project]] consumed $60M+ and 2,000 person-years. Enterprise knowledge graphs cost $10M-$20M. Marshall and Shipman (2003) noted the cognitive overhead of formalization exceeds traditional authoring.

[[concepts/cheap-ontology]] addresses this: LLMs can maintain natural-language schemas in markdown at API cost rather than enterprise cost, achieving perhaps 80% of the value at 1% of the investment.

## Sources
- [[sources/wikipedia-knowledge-representation-reasoning]] — ontology engineering theory
- [[sources/wikipedia-semantic-web]] — web ontology standards
- [[sources/wikipedia-cyc]] — the largest ontology project
- [[sources/pebblous-cheap-ontology]] — LLM-era ontology democratization

## Related Concepts
- [[concepts/knowledge-representation]] — the discipline ontologies serve
- [[concepts/semantic-web]] — the web platform for ontologies
- [[concepts/knowledge-graph]] — modern graph-based alternative/complement
- [[concepts/cheap-ontology]] — LLM-era cost reduction
- [[entities/cyc-project]] — the most ambitious ontology project
