---
title: "Detecting Hallucinations with LLM-as-a-Judge: Prompt Engineering and Beyond"
source: "https://www.datadoghq.com/blog/ai/llm-hallucination-detection/"
author: "Datadog AI Research"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [hallucination-detection, LLM-as-judge, faithfulness, RAG, evaluation]
type: article
status: raw
discovered_via: search
---

# Hallucination Detection Methods

## Categories of Detection Approaches

### White-Box and Gray-Box Methods (require model internals)
- **Token probability**: Estimates confidence using final-layer logits
- **Sparse autoencoders & attention mapping**: Identifies neural activations correlated with hallucinations
- **Semantic entropy**: Measures uncertainty in model outputs

### Black-Box Methods (only observe input/output)
- **Perturbation-based**: Measure reproducibility by regenerating answers (5-10x cost increase)
- **SLM-as-a-judge**: Smaller language models (BERT-style) for evaluation
- **LLM-as-a-judge**: Distinct judge model assesses correctness

## Datadog's Rubric-Based Approach

Key principle: "LLMs are better at guided summarization than complex reasoning."

### Implementation
- **Disagreement claims** identifying where context and answer conflict
- **Quote extraction** from both context and answer
- **Disagreement classification**:
  - Contradictions: Claims directly opposing provided context
  - Unsupported claims: Assertions not grounded in context
  - Agreements: Claims initially flagged but reasoned to be acceptable

### Technical Enhancements
- **Structured output**: Finite state machines enforce JSON compliance
- **Two-stage prompting**: Unrestricted chain-of-thought reasoning, then structured reformatting with smaller LLM
- **Semantic framing**: Context as "expert advice", answer as "candidate answer"

## Evaluation Results

| Benchmark | Method | Precision | Recall | F1 |
|-----------|--------|-----------|--------|-----|
| HaluBench (n=14,900) | Datadog/GPT-4o | 0.869 | 0.819 | 0.844 |
| HaluBench | Patronus/Lynx 8B | 0.831 | 0.841 | 0.836 |
| HaluBench | Patronus/GPT-4o | 0.885 | 0.841 | 0.862 |
| RAGTruth (n=2,700) | Datadog/GPT-4o | 0.788 | 0.833 | 0.810 |
| RAGTruth | Patronus/Lynx 8B | 0.637 | 0.861 | 0.733 |
| RAGTruth | Patronus/GPT-4o | 0.905 | 0.681 | 0.777 |

Key finding: Datadog's method shows smallest F1 drop between benchmarks, indicating robustness on harder datasets.

## Scope

Focuses on faithfulness in RAG systems—ensuring LLM answers align with retrieved context. Assumes context accuracy; doesn't address source document validation.
