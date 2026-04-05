---
title: "Zero-Shot Information Extraction"
type: concept
sources: ["[[sources/gpt-ner-named-entity-recognition]]", "[[sources/ontogpt-ontology-extraction]]", "[[sources/llm-kg-construction-survey]]"]
related: ["[[concepts/information-extraction]]", "[[concepts/named-entity-recognition]]", "[[concepts/relation-extraction]]", "[[concepts/schema-guided-extraction]]"]
last_compiled: 2026-04-05
summary: "Extracting entities, relations, and structured data from text without any task-specific training examples — enabled by LLMs' general language understanding and instruction-following abilities."
---

## Overview

Zero-shot information extraction uses LLMs to extract structured information from text without any labeled training examples for the specific task. The model relies entirely on its pre-trained knowledge and instruction-following ability.

This is the most significant paradigm shift LLMs brought to [[concepts/information-extraction]]: traditional IE required thousands of labeled examples per task per domain. Zero-shot IE requires only a well-crafted prompt.

## How It Works

1. **Prompt Design**: Describe the extraction task in natural language ("Extract all person names and organizations from this text")
2. **Schema Specification**: Optionally provide a [[concepts/structured-output-extraction]] schema defining expected output format
3. **LLM Generation**: The model generates extracted entities/relations based on its pre-trained understanding
4. **Validation**: Optionally validate output against schema constraints

## Evidence of Effectiveness

From [[sources/llm-kg-construction-survey]]:
- Few-shot GPT-4/Claude achieves accuracy roughly equivalent to — and sometimes superior to — fully supervised models
- LTNER reaches 91.91% on CoNLL2003 (standard NER benchmark) with few-shot prompting
- Open-source LLMs demonstrate zero-shot performance comparable to neural networks trained on thousands of examples

From [[sources/gpt-ner-named-entity-recognition]]:
- GPT-NER achieves supervised-comparable NER performance
- Significant advantage when labeled data is extremely scarce

From [[sources/ontogpt-ontology-extraction]]:
- SPIRES performs zero-shot knowledge base population without any task-specific training data
- Ontology constraints guide extraction without labeled examples

## Prompt Engineering for Zero-Shot IE

Clinical NLP research identifies six prompt types for zero-shot extraction, in order of sophistication:

1. **Simple Prefix**: "Extract entities from: {text}"
2. **Simple Cloze**: "The entities in '{text}' are: ___"
3. **Chain of Thought**: "First identify noun phrases, then classify each..."
4. **Anticipatory**: "A medical expert reading this text would identify..."
5. **Heuristic**: Include domain rules ("Entities must be proper nouns...")
6. **Ensemble**: Combine multiple prompt strategies and vote

Task-specific prompt tailoring is vital — different extraction tasks benefit from different prompt structures.

## Few-Shot vs. Zero-Shot

Few-shot extraction provides 1-10 labeled examples in the prompt. This often substantially improves extraction quality:
- Demonstrates expected output format
- Shows edge cases and how to handle them
- Provides implicit entity type definitions

The boundary between zero-shot and few-shot is fluid in practice — most production systems use 2-5 examples.

## Limitations

- Lower precision than supervised models on well-resourced tasks
- Sensitive to prompt phrasing
- May hallucinate entities/relations not in the source text
- Performance degrades on highly specialized domains without examples
- Cost: each extraction requires an LLM API call

## Relevance to Wiki Compilation

The [[concepts/wiki-compilation]] pipeline is inherently zero-shot: it must extract entities, concepts, and relationships from diverse source material (articles, papers, repo READMEs, tweets) without task-specific training data. The prompt-based approach described in CLAUDE.md's compilation rules is zero-shot IE in practice.

## Sources

- [[sources/gpt-ner-named-entity-recognition]] — zero/few-shot NER via task reformulation
- [[sources/ontogpt-ontology-extraction]] — SPIRES zero-shot knowledge base population
- [[sources/llm-kg-construction-survey]] — survey of zero/few-shot IE approaches

## Related Concepts

- [[concepts/information-extraction]] — parent discipline
- [[concepts/named-entity-recognition]] — zero-shot NER specifically
- [[concepts/relation-extraction]] — zero-shot RE specifically
- [[concepts/schema-guided-extraction]] — schemas improve zero-shot extraction
