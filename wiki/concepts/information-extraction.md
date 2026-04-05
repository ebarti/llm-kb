---
title: "Information Extraction with LLMs"
type: concept
sources: ["[[sources/willison-llm-schemas-structured-extraction]]", "[[sources/gpt-ner-named-entity-recognition]]", "[[sources/kggen-knowledge-graph-extraction]]", "[[sources/instructor-library-structured-extraction]]", "[[sources/claimify-claim-extraction]]", "[[sources/ontogpt-ontology-extraction]]", "[[sources/llm-kg-construction-survey]]", "[[sources/wolfe-llm-summarization-evolution]]"]
related: ["[[concepts/named-entity-recognition]]", "[[concepts/relation-extraction]]", "[[concepts/structured-output-extraction]]", "[[concepts/claim-extraction]]", "[[concepts/entity-linking]]", "[[concepts/llm-summarization]]", "[[concepts/schema-guided-extraction]]", "[[concepts/zero-shot-information-extraction]]", "[[concepts/knowledge-graph]]", "[[concepts/wiki-compilation]]"]
last_compiled: 2026-04-05
summary: "The discipline of automatically extracting structured knowledge (entities, relations, claims, facts) from unstructured text using LLMs — the foundational capability enabling wiki compilation pipelines."
---

## Overview

Information extraction (IE) is the process of automatically identifying and structuring knowledge from unstructured text. With LLMs, IE has undergone a paradigm shift: tasks that previously required task-specific supervised models (trained on thousands of labeled examples) can now be performed zero-shot or few-shot by prompting general-purpose language models.

For the [[concepts/llm-knowledge-base]] system, information extraction is the foundational capability. The [[concepts/wiki-compilation]] pipeline depends on extracting entities, concepts, relationships, and claims from raw ingested sources to produce structured wiki articles. Every other capability — Q&A, linting, cross-referencing — builds on extraction quality.

## The IE Task Taxonomy

Information extraction encompasses several interconnected subtasks:

| Subtask | What it Extracts | Example |
|---------|-----------------|---------|
| [[concepts/named-entity-recognition]] | Named entities (people, orgs, locations) | "Karpathy" -> PERSON |
| [[concepts/relation-extraction]] | Relationships between entities | (Karpathy, created, LLM-KB-system) |
| [[concepts/entity-linking]] | Map mentions to canonical KB entries | "GPT-4o" -> OpenAI GPT-4o entity |
| [[concepts/claim-extraction]] | Atomic verifiable statements | "GPT-NER achieves SOTA on CoNLL2003" |
| [[concepts/llm-summarization]] | Condensed representations | Key points from a 5000-word article |
| [[concepts/structured-output-extraction]] | Schema-conformant JSON/objects | {name: "...", type: "...", relations: [...]} |

## How LLMs Changed IE

### Before LLMs
Traditional IE required separate supervised models for each subtask (NER model, RE model, coreference model), each trained on thousands of labeled examples in a specific domain. Pipeline architectures suffered from error propagation — mistakes in NER cascaded into relation extraction.

### With LLMs
LLMs enable:
- **Zero-shot extraction**: No labeled data needed ([[concepts/zero-shot-information-extraction]])
- **Unified models**: One model handles NER, RE, summarization, and structured output
- **Schema flexibility**: Change what you extract by changing the prompt, not retraining
- **Cross-domain transfer**: A prompt written for biomedical text can be adapted to legal text in minutes

The [[sources/llm-kg-construction-survey]] documents that few-shot GPT-4/Claude achieves accuracy equivalent to fully supervised traditional models without requiring thousands of labeled training examples.

### The Structured Output Revolution

As of early 2026, all major providers (OpenAI, Anthropic, Gemini, Mistral, Cohere, xAI) support native [[concepts/structured-output-extraction]]. The JSON Schema is compiled into a finite state machine (FSM) providing mathematical guarantees of schema-conformant output. This eliminates the "parse and pray" approach and makes extraction pipelines production-reliable.

## Approaches to LLM-Based IE

### 1. Schema-Guided Extraction
Define an ontology or schema upfront; constrain the LLM to extract only matching entities and relations. Examples: [[entities/ontogpt]] (SPIRES method), KARMA, ODKE+. See [[concepts/schema-guided-extraction]].

**Strengths**: High precision, consistent output, ontology-aligned
**Weaknesses**: Rigid, domain-specific, misses novel entities

### 2. Schema-Free / Open Extraction
Let the LLM discover entities and relations without predefined schemas. Examples: OpenIE, EDC framework, ChatIE.

**Strengths**: Flexible, discovers novel patterns, cross-domain
**Weaknesses**: Inconsistent naming, redundant entities, requires post-processing

### 3. Hybrid / Dynamic Schema
Start schema-free, then converge toward a schema through clustering and canonicalization. Examples: [[entities/kggen]] (generate-aggregate-cluster), AutoSchemaKG.

**Strengths**: Best of both worlds — discovery with consistency
**Weaknesses**: Complex pipelines, LLM cost for clustering/validation

## Relevance to Wiki Compilation

The [[concepts/wiki-compilation]] pipeline performs information extraction at every stage:

1. **Ingest**: Extract title, author, date, tags from raw sources ([[concepts/structured-output-extraction]])
2. **Entity identification**: Find people, tools, papers, organizations mentioned ([[concepts/named-entity-recognition]])
3. **Concept extraction**: Identify key ideas and themes ([[concepts/claim-extraction]], [[concepts/llm-summarization]])
4. **Relationship mapping**: Connect entities to concepts and to each other ([[concepts/relation-extraction]])
5. **Deduplication**: Resolve different mentions of the same entity ([[concepts/entity-linking]])

The quality of these extraction steps directly determines [[concepts/data-quality-bottleneck]] — errors here cascade through the entire knowledge base, compounding via [[concepts/hallucination-contamination]].

## Key Tools and Systems

| Tool | Approach | Key Feature |
|------|----------|-------------|
| [[entities/instructor]] | Pydantic-based structured extraction | Validation + retry loop |
| [[entities/ontogpt]] | Ontology-grounded SPIRES | Zero-shot with ontology constraints |
| [[entities/kggen]] | Generate-aggregate-cluster pipeline | Entity resolution via LLM clustering |
| [[entities/claimify]] | 4-stage claim decomposition | Disambiguation-aware extraction |
| Simon Willison's LLM | Schema-based CLI extraction | FSM-guaranteed output |

## Three Emerging Trends (from the KGC Survey)

1. **Schema Dynamism**: Progression from static predefined schemas toward continuously evolving structures
2. **Pipeline Integration**: Movement from modular, fragmented stages to unified generative frameworks
3. **Semantic Adaptability**: Shift from rigid symbolic constraints toward flexible, language-grounded reasoning

## Sources

- [[sources/willison-llm-schemas-structured-extraction]] — structured extraction as "the most commercially valuable LLM application"
- [[sources/gpt-ner-named-entity-recognition]] — bridging the NER-generation gap
- [[sources/kggen-knowledge-graph-extraction]] — three-stage KG extraction pipeline
- [[sources/instructor-library-structured-extraction]] — Pydantic-based extraction library
- [[sources/claimify-claim-extraction]] — atomic claim decomposition
- [[sources/ontogpt-ontology-extraction]] — ontology-grounded zero-shot extraction
- [[sources/llm-kg-construction-survey]] — comprehensive taxonomy of LLM-based KG construction
- [[sources/wolfe-llm-summarization-evolution]] — summarization as extraction

## Related Concepts

- [[concepts/wiki-compilation]] — IE is the engine behind wiki compilation
- [[concepts/knowledge-graph]] — IE populates knowledge graphs
- [[concepts/data-quality-bottleneck]] — extraction quality determines KB quality
- [[concepts/hallucination-contamination]] — extraction errors propagate through the KB
- [[concepts/multi-agent-systems]] — KARMA uses 9 agents for IE
