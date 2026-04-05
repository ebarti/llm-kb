---
title: "OpenFactCheck: A Unified Framework for Factuality Evaluation of LLMs"
source: "https://openfactcheck.com/"
author: "OpenFactCheck Team"
date_published: 2024-06-01
date_ingested: 2026-04-05
tags: [fact-checking, factuality, evaluation, hallucination, verification]
type: article
status: raw
discovered_via: search
---

# OpenFactCheck: Unified LLM Factuality Evaluation

## Overview

Open-source framework addressing the problem that "different papers use different evaluation benchmarks and measures, which makes them hard to compare."

## Three Core Modules

### 1. Response Evaluator
Customized fact-checking through a three-step pipeline:
- **Claim Processor**: Decomposes documents into individual claims
- **Retriever**: Gathers relevant evidence for each claim
- **Verifier**: Assesses claim accuracy based on evidence

Supported systems: RARR, FacTool, FactCheckGPT. Users can mix components via YAML configuration.

### 2. LLM Evaluator
Introduces **FactQA**: unified dataset of 6,480 examples across 482 domains from seven sources (Snowball, SelfAware, FreshQA, etc.) assessing three types of factual errors.

Evaluation methods:
- Exact matching for yes/no and short-answer questions
- FreshEval for time-sensitive content
- Automatic fact-checking for open-domain responses

### 3. Fact Checker Evaluator
Uses **FactBench**: 4,507 human-annotated examples across claims, segments, and documents. Metrics: precision, recall, F1-score.

## Key Features

- Customizable pipelines through YAML configuration
- Extensible design
- Python library (PyPI) and web dashboard
- pip install openfactcheck
