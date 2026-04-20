---
title: "LLM Evaluation Metrics: The Ultimate LLM Evaluation Guide"
source: "https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation"
author: "Confident AI"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [llm-evaluation, metrics, G-Eval, faithfulness, hallucination, RAG, DeepEval]
type: article
status: raw
discovered_via: search
---

# LLM Evaluation Metrics: The Ultimate LLM Evaluation Guide

## Overview

LLM evaluation metrics quantify system output quality across dimensions like correctness, relevance, and factual accuracy. The field distinguishes between single-turn metrics (evaluating individual interactions) and multi-turn metrics (incorporating conversation history).

## Metric Categories

### Statistical Scorers

Traditional approaches with limited semantic understanding:

- **BLEU**: Measures n-gram precision between outputs and ground truth, applying brevity penalties
- **ROUGE**: Calculates recall via n-gram overlap proportions (0-1 scale)
- **METEOR**: Combines precision/recall assessment, leveraging linguistic databases like WordNet for synonym matching
- **Levenshtein Distance**: Counts minimum character edits needed between texts

Limitation: "Statistical methods performs poorly whenever reasoning is required," making them inadequate for complex LLM evaluation.

### Model-Based Scorers (Non-LLM)

- **NLI (Natural Language Inference)**: Classifies outputs as entailment, contradiction, or neutral
- **BLEURT**: Uses BERT-based pre-trained models
- **BERTScore**: Computes cosine similarity between contextual embeddings
- **MoverScore**: Applies Earth Mover's Distance to word distributions

These struggle with accuracy on lengthy texts and suffer from training data limitations.

### LLM-as-a-Judge Methods

These leverage LLM reasoning capabilities for superior accuracy:

#### G-Eval
Uses chain-of-thought reasoning before scoring:
1. Generates evaluation steps from task criteria
2. Creates prompts incorporating those steps
3. Produces scores (typically 1-5 scale)
4. Optionally normalizes using token probabilities

#### DAG (Deep Acyclic Graph)
Decision tree-based evaluation where each node represents an LLM judgment and edges represent decisions. Returns hard-coded or G-Eval-based scores at leaf nodes. Ideal for scenarios with clear success criteria requiring deterministic outputs.

#### QAG (Question Answer Generation) Score
Avoids direct LLM scoring through:
1. Extracting claims from outputs
2. Asking binary yes/no questions about claims
3. Computing final scores from proportions

#### Prometheus
Open-source LLM fine-tuned on 100K GPT-4 feedback samples. Requires explicit rubrics and reference answers.

#### SelfCheckGPT
Reference-less hallucination detection via sampling. Assumes hallucinated outputs lack consistency across samples.

## Domain-Specific Metrics

### RAG Metrics

- **Faithfulness**: Proportion of truthful claims in outputs relative to retrieval context
- **Answer Relevancy**: Relevant sentence proportions relative to input and context
- **Contextual Precision**: How well relevant context nodes rank above irrelevant ones
- **Contextual Recall**: Percentage of expected output content in retrieved nodes
- **Contextual Relevancy**: Proportion of retrieval context sentences relevant to query

### AI Agent Metrics

- **Task Completion**: End-to-end evaluation of whether agents accomplish objectives
- **Tool Correctness**: Exact-match assessment comparing actual vs expected tool invocations
- **Argument Correctness**: Validates tool parameter appropriateness
- **Plan Quality**: Evaluates completeness, logic, and efficiency
- **Plan Adherence**: Whether agents follow their own plans
- **Step Efficiency**: Penalizes redundant operations

### Foundational Model Metrics

- **Hallucination**: SelfCheckGPT for zero-shot detection or NLI with ground truth
- **Toxicity**: Detoxify (BERT-based) or G-Eval for nuanced definitions
- **Bias**: G-Eval recommended given bias's highly subjective nature

### The 5-Metric Rule

Maintain evaluation efficiency with:
- 1-2 custom metrics (G-Eval/DAG) targeting use-case specifics
- 2-3 generic metrics matching system architecture (RAG, agentic, conversational)
