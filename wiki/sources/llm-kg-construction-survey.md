---
title: "Source: LLM-Empowered Knowledge Graph Construction — A Survey"
type: source-summary
source: "[[raw/llm-kg-construction-survey]]"
related: ["[[concepts/knowledge-graph-construction]]", "[[concepts/ontology-engineering]]", "[[concepts/knowledge-extraction]]", "[[concepts/knowledge-fusion]]", "[[concepts/knowledge-graph]]"]
last_compiled: 2026-04-05
summary: "Comprehensive survey cataloguing the paradigm shift from rule-based to LLM-driven knowledge graph construction across ontology engineering, knowledge extraction, and knowledge fusion — with schema-based and schema-free taxonomies."
reading_time: "2 min"
---

## Key Points

- LLMs have shifted KG construction from rule-based/statistical pipelines to language-driven generative frameworks
- Dual paradigm: schema-based methods (ontology-guided consistency) vs. schema-free methods (open discovery flexibility)
- Few-shot prompting with GPT-4/Claude matches or exceeds fully supervised traditional models without labeled training data
- Key frameworks: KARMA (multi-agent), AutoSchemaKG (dynamic schema induction), KGGEN (iterative entity clustering), EDC (extract-define-canonicalize)
- Future directions: KG-based reasoning for LLMs, dynamic knowledge memory for agents, multimodal KG construction, KGs as cognitive middle layers

## Detailed Summary

This arXiv survey (October 2025) systematically maps how LLMs are transforming the three traditional stages of KG construction: ontology engineering, knowledge extraction, and knowledge fusion.

**Ontology Engineering** now supports both top-down (LLMs as assistants converting competency questions into OWL ontologies) and bottom-up (data-driven schema induction from instance graphs). Notable systems include Ontogenia (metacognitive prompting), NeOn-GPT, and AutoSchemaKG which bridges schema-based and schema-free paradigms.

**Knowledge Extraction** spans static schema-driven approaches (KARMA's multi-agent architecture, ODKE+ with ontology snippets), dynamic schema approaches (AdaKGC with runtime adaptation), and schema-free methods including Chain-of-Thought prompting, ChatIE (multi-turn dialogue extraction), and KGGEN (sequential entity-then-relation extraction).

**Knowledge Fusion** addresses the critical challenge of merging extracted knowledge: entity alignment (KGGEN's iterative clustering, EntGPT's two-phase refinement, COMEM's cascading LLM pipeline), schema-level unification, and comprehensive frameworks like Graphusion.

The survey concludes that KGs are becoming "living, cognitive infrastructures that blend language understanding with structured reasoning."

## Notable Quotes

> "Traditional fusion pipelines continue to struggle with semantic heterogeneity, large-scale integration, and dynamic knowledge updating."

## Related Concepts

- [[concepts/knowledge-graph-construction]] — the central topic of this survey
- [[concepts/ontology-engineering]] — automated ontology creation with LLMs
- [[concepts/knowledge-extraction]] — entity and relation extraction from text
- [[concepts/knowledge-fusion]] — merging and deduplicating extracted knowledge
- [[concepts/knowledge-graph]] — the output artifact
