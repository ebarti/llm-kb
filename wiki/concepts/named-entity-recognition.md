---
title: "Named Entity Recognition (NER) with LLMs"
type: concept
sources: ["[[sources/gpt-ner-named-entity-recognition]]", "[[sources/llm-kg-construction-survey]]"]
related: ["[[concepts/information-extraction]]", "[[concepts/relation-extraction]]", "[[concepts/entity-linking]]", "[[concepts/zero-shot-information-extraction]]"]
last_compiled: 2026-04-05
summary: "Identifying and classifying named entities (people, organizations, locations, etc.) in text — LLMs bridge the sequence-labeling-to-generation gap via task reformulation and self-verification."
---

## Overview

Named Entity Recognition (NER) identifies predefined categories of objects in text: people, organizations, locations, dates, monetary values, medical codes, and more. It is the first step in most [[concepts/information-extraction]] pipelines — you must know what entities exist before you can extract relationships between them.

## The LLM-NER Gap

Traditional NER is a sequence labeling task: given a sequence of tokens, assign a label (B-PER, I-PER, O, etc.) to each token. LLMs are text-generation models. This fundamental mismatch initially caused LLMs to significantly underperform supervised NER baselines.

## Approaches to LLM-Based NER

### 1. Generation-Based (GPT-NER)

[[sources/gpt-ner-named-entity-recognition]] transforms NER into generation by using special marker tokens. Given "Columbus is a city," the model generates "@@Columbus## is a city" where @@/## delimit entities. This approach:

- Achieves performance comparable to fully supervised baselines (first time for LLM-NER)
- Excels in few-shot and low-resource scenarios
- Uses self-verification to combat entity hallucination

### 2. Prompt-Based Classification

Reformulate NER as a question: "What persons are mentioned in this text?" This leverages LLMs' instruction-following ability but may miss entities or hallucinate.

### 3. Structured Output NER

Use [[concepts/structured-output-extraction]] to have the LLM return a JSON array of entities with types:

```json
[
  {"text": "Columbus", "type": "LOCATION", "start": 0, "end": 8},
  {"text": "Ohio", "type": "LOCATION", "start": 25, "end": 29}
]
```

This approach benefits from FSM-guaranteed output schemas (see [[sources/willison-llm-schemas-structured-extraction]]).

### 4. Nested NER

Entities within entities ("the University of California, Berkeley" contains both ORG and LOCATION). EMNLP 2024 research applies specific reasoning techniques to improve LLM performance on nested NER.

## Performance Benchmarks

From [[sources/llm-kg-construction-survey]]:
- LTNER reaches 91.91% on CoNLL2003 (standard NER benchmark)
- Few-shot GPT-4/Claude achieves accuracy roughly equivalent to fully supervised models
- LLMs excel when labeled training data is scarce (few-shot superiority)

## Self-Verification Against Hallucination

A critical challenge: LLMs over-confidently label tokens as entities even when no entities are present. GPT-NER's self-verification strategy prompts the model to confirm whether each extracted entity genuinely belongs to the target category. This is a form of [[concepts/hallucination-contamination]] mitigation specific to extraction.

## Relevance to Wiki Compilation

In the [[concepts/wiki-compilation]] pipeline, NER identifies:
- **People**: Authors, researchers, practitioners mentioned in sources
- **Tools/Products**: Software, frameworks, libraries discussed
- **Organizations**: Companies, research labs, universities
- **Papers/Datasets**: Academic works referenced

These become candidates for [[concepts/entity-linking]] (mapping to canonical KB entries) and for creating entity pages in `wiki/entities/`.

## Sources

- [[sources/gpt-ner-named-entity-recognition]] — task reformulation and self-verification
- [[sources/llm-kg-construction-survey]] — LTNER benchmark results and NER in KG pipelines

## Related Concepts

- [[concepts/information-extraction]] — NER is a core IE subtask
- [[concepts/relation-extraction]] — extracts relationships between NER-identified entities
- [[concepts/entity-linking]] — maps NER output to canonical KB entries
- [[concepts/zero-shot-information-extraction]] — LLM NER often works zero-shot
- [[concepts/hallucination-contamination]] — self-verification combats NER hallucinations
