---
title: "Cheap Ontology"
type: concept
sources: ["[[sources/pebblous-cheap-ontology]]"]
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/knowledge-graph]]", "[[concepts/markdown-as-universal-interface]]"]
last_compiled: 2026-04-05
summary: "Pebblous framing: LLM wikis replace $10M–$20M enterprise knowledge graphs using only markdown files, LLM APIs, and natural-language schema instructions — democratizing what was once exclusive ontology engineering expertise."
reading_time: "2 min"
---

## Overview

"Cheap Ontology" is the Pebblous framing for what Karpathy's LLM wiki approach represents historically: a 1000x cost reduction in building structured knowledge systems, achieved by replacing formal ontology engineering with LLM-maintained markdown files.

## Key Ideas

**The cost disruption:**
- Traditional enterprise knowledge graphs: $10M–$20M upfront investment, ontology engineers at $107K–$207K/year, only 27% reaching production
- Karpathy's approach: API costs only, setup in days, no specialized expertise required

**What gets replaced:**
- RDF/OWL/SPARQL formal ontologies → natural-language markdown with wikilinks
- Schema axioms → CLAUDE.md or AGENTS.md instructions in plain English
- Ontology engineers → developers who can write a system prompt
- Formal reasoners → LLM health checks (linting)

**Context window as enabler:** GPT-3 had 2K tokens; Gemini 2.0 Pro has 2M tokens — a 1,000-fold expansion in five years. This expansion is what made loading entire wikis into context feasible, eliminating the need for vector retrieval at personal scale.

**Historical phases:**
1. 1970s–2000: Expert-built formal ontologies (Description Logic, Closed World Assumption)
2. 2001–2007: Semantic Web (RDF, RDFS, OWL, SPARQL) — technically sound, expensive to deploy
3. 2007–2020: Knowledge graph maturation (DBpedia, Google's 570M-entity graph, Wikidata)
4. 2024–present: LLM wikis — Cheap Ontology era

## Limitations

Cheap Ontology trades rigor for accessibility:
- No formal query language (SPARQL) — just LLM natural-language navigation
- No closed-world reasoning — LLMs can confabulate
- Scale ceiling: ~100–400 articles; beyond this, LlamaIndex or GraphRAG needed
- No schema enforcement — the LLM must be prompted to maintain consistency

## Sources
- [[sources/pebblous-cheap-ontology]] — coined the "Cheap Ontology" framing; provides full historical context

## Related Concepts
- [[concepts/llm-knowledge-base]] — the implementation of Cheap Ontology
- [[concepts/knowledge-graph]] — the expensive alternative
- [[concepts/markdown-as-universal-interface]] — the substrate
- [[concepts/rag-vs-index-based-retrieval]] — retrieval implications

## Related Entities

- [[entities/vannevar-bush]] — historical starting point (Memex, 1945)
- [[entities/memex]] — the original vision of personal associative knowledge
- [[entities/andrej-karpathy]] — modern implementer of cheap ontology

## Related Comparisons

- [[comparisons/knowledge-graph-vs-wiki]] — formal (expensive) vs. markdown (cheap) ontology
