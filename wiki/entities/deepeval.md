---
title: "DeepEval"
type: entity
entity_type: tool
sources: ["[[sources/confident-ai-llm-evaluation-metrics]]", "[[sources/eugeneyan-llm-evaluators]]"]
related: ["[[concepts/llm-evaluation-metrics]]", "[[concepts/llm-as-judge]]", "[[concepts/rag-evaluation]]", "[[concepts/hallucination-detection]]", "[[entities/ragas]]"]
last_compiled: 2026-04-05
summary: "Open-source LLM evaluation framework by Confident AI with 14+ built-in metrics (hallucination, faithfulness, toxicity, bias), Pytest-like unit testing paradigm, and CI/CD integration."
---

## Overview

DeepEval is an open-source evaluation framework for LLMs, designed to make it easy to "unit test" LLM outputs in a similar way to Pytest. Built by Confident AI, it provides 14+ built-in metrics covering hallucination, toxicity, bias detection, and RAG-specific evaluation.

## Key Features

- **14+ built-in metrics**: Hallucination, faithfulness, toxicity, bias, contextual precision/recall/relevancy, answer relevancy, task completion, tool correctness
- **Pytest-like API**: Familiar testing paradigm for developers
- **LLM-as-a-Judge**: Uses [[concepts/llm-as-judge]] and NLP models (some run locally)
- **Framework-agnostic**: Integrates with OpenAI Agents, LangChain, CrewAI, LlamaIndex
- **CI/CD ready**: Run evaluations in continuous integration pipelines
- **Multi-turn support**: Evaluate conversation-level quality

## Metric Implementation

DeepEval implements multiple scoring approaches from [[concepts/llm-evaluation-metrics]]:

- **[[entities/g-eval]]**: Chain-of-thought reasoning with probability normalization
- **DAG**: Decision-tree-based deterministic evaluation
- **QAG**: Question-answer generation for claim-level verification
- **SelfCheckGPT**: Reference-free hallucination detection via sampling consistency
- **NLI**: Natural language inference for entailment classification

## Ecosystem

- **DeepEval** (open-source): Local evaluation framework
- **Confident AI** (cloud): Collaboration, dataset management, tracing, real-time monitoring, dashboards

## Mentioned In

- [[sources/confident-ai-llm-evaluation-metrics]] — comprehensive metric guide from the DeepEval team
- [[sources/eugeneyan-llm-evaluators]] — mentioned as evaluation framework option
