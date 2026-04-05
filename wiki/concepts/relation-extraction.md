---
title: "Relation Extraction with LLMs"
type: concept
sources: ["[[sources/kggen-knowledge-graph-extraction]]", "[[sources/llm-kg-construction-survey]]", "[[sources/ontogpt-ontology-extraction]]"]
related: ["[[concepts/information-extraction]]", "[[concepts/named-entity-recognition]]", "[[concepts/knowledge-graph]]", "[[concepts/entity-linking]]", "[[concepts/schema-guided-extraction]]"]
last_compiled: 2026-04-05
summary: "Extracting subject-predicate-object relationships between entities from text — LLMs enable zero-shot relation extraction that matches supervised models, feeding knowledge graph construction."
---

## Overview

Relation extraction (RE) identifies semantic relationships between entities in text, typically producing subject-predicate-object triples. Given "Karpathy works at OpenAI," RE produces (Karpathy, works_at, OpenAI). It is the second core step in [[concepts/information-extraction]] pipelines, following [[concepts/named-entity-recognition]].

## How LLMs Perform Relation Extraction

### Zero-Shot RE

LLMs can extract relations from text without any training data by leveraging natural language prompts. From [[sources/llm-kg-construction-survey]], this "provides the possibility of extracting relations from text without any data and parameter tuning." The prompt specifies desired relation types or leaves extraction open-ended.

### Two-Step Extraction (KGGen Pattern)

[[sources/kggen-knowledge-graph-extraction]] demonstrates the dominant pipeline:
1. First LLM call identifies key entities
2. Second call extracts subject-predicate-object triples using the identified entities

This two-step approach ensures consistency between entity recognition and relation extraction, avoiding the error propagation problem of traditional pipeline architectures.

### Dialogue-Based Refinement (ChatIE)

ChatIE reformulates extraction as multi-turn dialogue, iteratively refining extracted relations through conversation. This approach handles complex sentences where relations are implicit or require inference.

### Schema-Guided RE

When the target relation types are known (e.g., "works_at", "authored", "cites"), [[concepts/schema-guided-extraction]] constrains the LLM to only extract matching relations. ODKE+ from Apple Research uses dynamically selected ontology subsets for context-aware relation prompting.

## Key Challenges

### Implicit Relations
Complex sentences contain relations that are implied but not stated: "After graduating from Stanford, Karpathy joined OpenAI" implies (Karpathy, educated_at, Stanford) AND (Karpathy, works_at, OpenAI). LLMs handle these better than rule-based systems but still miss subtle implications.

### Relation Canonicalization
Different texts express the same relation differently: "works at," "employed by," "is a researcher at." [[entities/kggen]]'s clustering phase addresses this by merging synonymous relation predicates.

### Hallucinated Relations
LLMs may infer relations not supported by the source text. This connects to [[concepts/hallucination-contamination]] — extracted relations need verification against source material.

## Performance

From [[sources/llm-kg-construction-survey]]:
- Few-shot GPT-4 achieves accuracy comparable to supervised RE models
- KGGen achieves 66.07% on the MINE benchmark (vs. GraphRAG 47.80%, OpenIE 29.84%)
- AutoRE's RHF (Relation-Head-Facts) pipeline via instruction fine-tuning shows strong results

## Relevance to Wiki Compilation

In the [[concepts/wiki-compilation]] pipeline, relation extraction:
- Populates the `related:` frontmatter field in wiki articles
- Generates the `[[wikilinks]]` connecting concepts to entities
- Builds the backlink graph in `wiki/_meta/links.md`
- Identifies comparison opportunities (when two entities share competing relations)

## Sources

- [[sources/kggen-knowledge-graph-extraction]] — two-step entity-then-relation extraction
- [[sources/llm-kg-construction-survey]] — comprehensive taxonomy of RE approaches
- [[sources/ontogpt-ontology-extraction]] — ontology-constrained relation extraction

## Related Concepts

- [[concepts/information-extraction]] — RE is a core IE subtask
- [[concepts/named-entity-recognition]] — entities must be identified before relations
- [[concepts/knowledge-graph]] — triples populate knowledge graphs
- [[concepts/entity-linking]] — canonicalizes entities in extracted triples
- [[concepts/schema-guided-extraction]] — constrains allowed relation types
