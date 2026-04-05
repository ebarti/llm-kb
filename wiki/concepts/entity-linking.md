---
title: "Entity Linking and Resolution"
type: concept
sources: ["[[sources/kggen-knowledge-graph-extraction]]", "[[sources/llm-kg-construction-survey]]", "[[sources/ontogpt-ontology-extraction]]"]
related: ["[[concepts/named-entity-recognition]]", "[[concepts/information-extraction]]", "[[concepts/knowledge-graph]]", "[[concepts/schema-guided-extraction]]"]
last_compiled: 2026-04-05
summary: "Mapping textual entity mentions to canonical KB entries — resolving ambiguity ('Apple' the company vs. fruit) and merging synonyms ('GPT-4o' / 'gpt4o') via LLM-based clustering and ontology grounding."
---

## Overview

Entity linking (EL) maps textual entity mentions to canonical entries in a knowledge base. It resolves two problems:

1. **Ambiguity**: "Apple" could be the company, the fruit, or Apple Records
2. **Synonymy**: "GPT-4o", "gpt-4o", and "OpenAI's GPT-4o" all refer to the same entity

Entity linking follows [[concepts/named-entity-recognition]] in the extraction pipeline and is a prerequisite for building accurate [[concepts/knowledge-graph]] structures.

## LLM-Based Approaches

### 1. LLM-Based Clustering (KGGen)

[[sources/kggen-knowledge-graph-extraction]] performs entity resolution through iterative LLM-based clustering:
- LLM examines entity lists to find synonymous groups
- LLM-as-a-judge validates each cluster
- Handles tense, plurality, stemming, and capitalization variations
- Example: "vulnerabilities," "vulnerable," "weaknesses" merge into one entity

### 2. Ontology Grounding (OntoGPT)

[[entities/ontogpt]] constrains extraction to established ontology terms. Rather than free-form entity names, extracted entities must map to canonical identifiers in ontologies like Gene Ontology, Disease Ontology, etc. This eliminates ambiguity at extraction time.

### 3. Two-Phase Refinement (EntGPT)

EntGPT generates candidates first, then applies targeted reasoning to select the correct KB entry. This handles long-tail entities where training data is sparse.

### 4. Cascading Models (COMEM)

Smaller models handle easy cases (high-confidence matches); larger models handle ambiguous cases. This balances cost and accuracy.

### 5. Context Augmentation (LLMAEL)

Uses LLMs as context augmenters — generating entity descriptions that help specialized EL models make better linking decisions.

## Challenges

From [[sources/llm-kg-construction-survey]]:
- Specialized EL models struggle with long-tail entities due to limited training data
- LLMs possess broader knowledge of uncommon entities but frequently fail to generate accurate KB entity names
- Best results come from combining LLM knowledge with specialized retrieval

## Relevance to Wiki Compilation

Entity linking is critical for the [[concepts/wiki-compilation]] pipeline:

1. **Deduplication**: When multiple sources mention "Karpathy" / "Andrej Karpathy" / "@karpathy," these must map to a single `wiki/entities/andrej-karpathy.md`
2. **Wikilink generation**: Entity mentions in text become `[[entities/andrej-karpathy]]` wikilinks
3. **Cross-source synthesis**: Concept articles aggregate information about entities across sources — this requires knowing which mentions refer to the same entity
4. **Manifest checking**: Before creating a new entity page, check if the entity already exists under a different name

The `wiki/_meta/manifest.md` and `wiki/_meta/summaries.md` files serve as a lightweight entity registry for the wiki compiler.

## Sources

- [[sources/kggen-knowledge-graph-extraction]] — LLM-based clustering for entity resolution
- [[sources/llm-kg-construction-survey]] — entity alignment taxonomy (LLM-Align, EntGPT, COMEM)
- [[sources/ontogpt-ontology-extraction]] — ontology grounding as entity linking

## Related Concepts

- [[concepts/named-entity-recognition]] — identifies entities before linking
- [[concepts/information-extraction]] — entity linking is an IE subtask
- [[concepts/knowledge-graph]] — entity linking ensures graph consistency
- [[concepts/schema-guided-extraction]] — ontology grounding constrains entity linking
