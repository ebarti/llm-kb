---
title: "Knowledge Extraction"
type: concept
sources: ["[[sources/llm-kg-construction-survey]]", "[[sources/kggen-knowledge-graph-extraction]]", "[[sources/graphrag-microsoft-research]]"]
related: ["[[concepts/knowledge-graph-construction]]", "[[concepts/knowledge-fusion]]", "[[concepts/knowledge-graph]]"]
last_compiled: 2026-04-05
summary: "LLM-driven extraction of entities, relations, and facts from unstructured text — the core pipeline stage of knowledge graph construction, now achieving near-expert accuracy via few-shot prompting."
---

## Overview

Knowledge extraction is the process of identifying entities, relationships, and structured facts from unstructured text. It is the central pipeline stage of [[concepts/knowledge-graph-construction]], converting raw documents into the subject-predicate-object triples that populate [[concepts/knowledge-graph]] structures.

With LLMs, extraction has shifted from requiring specialized NER/RE models trained on thousands of labeled examples to few-shot and zero-shot approaches that achieve comparable or superior accuracy.

## Core Tasks

### Named Entity Recognition (NER)

Identifies entities — people, organizations, locations, concepts — in text. LLM-based NER achieves state-of-the-art results: LTNER reaches 91.91% on CoNLL2003 via few-shot prompting, matching fully supervised baselines without labeled training data.

### Relation Extraction

Identifies semantic relationships between entities. LLMs can extract relations as structured triples (subject, predicate, object) through:
- Direct prompting ("Extract all relationships from this text")
- Two-step extraction (entities first, then relations using identified entities — as in [[entities/kggen]])
- Multi-turn dialogue (ChatIE reformulates extraction as conversational refinement)

### Event Extraction

Identifies complex event structures with participants, temporal context, and causal relationships. This extends beyond simple triples to capture richer semantics.

## LLM Extraction Approaches

### Structured Generative Extraction

The dominant approach: prompt an LLM to output structured (usually JSON) representations of entities and relations. Key methods:

- **Direct extraction**: Single prompt to extract all triples
- **Two-step extraction** ([[entities/kggen]]): First identify entities, then extract relations using those entities
- **Chain-of-Thought**: Stepwise reasoning improving extraction quality
- **Retrieval-augmented prompting**: Enriching context with relevant exemplars

### Schema-Guided Extraction

Uses a predefined ontology to constrain what the LLM extracts:
- **KARMA**: Multi-agent architecture with schema-guided task execution
- **ODKE+**: Ontology snippets as dynamic context for prompts
- **AdaKGC**: Schema-Enriched Prefix Instruction with runtime schema adaptation

### Open Information Extraction

No predefined schema — the LLM discovers entity types and relation types freely:
- **EDC framework**: Few-shot prompting → raw triples → definition → canonicalization
- **AutoRE**: RHF (Relation-Head-Facts) pipeline via instruction fine-tuning

## Entity Resolution and Post-Processing

Raw extraction produces duplicates and inconsistencies. Post-processing includes:
- **Entity standardization**: Unifying "AI" and "artificial intelligence"
- **Iterative clustering** (KGGen): LLM-as-a-Judge validates entity clusters
- **Schema alignment**: Mapping extracted types to canonical ontology

See [[concepts/knowledge-fusion]] for the full fusion pipeline.

## Sources

- [[sources/llm-kg-construction-survey]] — comprehensive taxonomy of extraction methods
- [[sources/kggen-knowledge-graph-extraction]] — state-of-the-art two-step extraction
- [[sources/graphrag-microsoft-research]] — extraction as part of the GraphRAG pipeline

## Related Concepts

- [[concepts/knowledge-graph-construction]] — the end-to-end process
- [[concepts/knowledge-fusion]] — what happens after extraction
- [[concepts/ontology-engineering]] — schema that guides extraction
