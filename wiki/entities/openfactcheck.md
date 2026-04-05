---
title: "OpenFactCheck"
type: entity
entity_type: tool
sources: ["[[sources/openfactcheck-factuality-framework]]"]
related: ["[[concepts/automated-fact-checking]]", "[[concepts/hallucination-detection]]", "[[concepts/faithfulness-and-groundedness]]"]
last_compiled: 2026-04-05
summary: "Open-source unified framework for LLM factuality evaluation with three modules: ResponseEvaluator (claim-level fact-checking), LLMEvaluator (FactQA, 6,480 examples), and FactCheckerEvaluator (FactBench, 4,507 annotated examples)."
---

## Overview

OpenFactCheck is an open-source framework that unifies LLM factuality evaluation, addressing the problem that different papers use different benchmarks, making results incomparable. It provides three complementary evaluation modules.

## Architecture

### ResponseEvaluator
Three-step pipeline for checking individual LLM responses:
1. **Claim Processor**: Decomposes documents into individual verifiable claims
2. **Retriever**: Gathers relevant evidence for each claim
3. **Verifier**: Assesses claim accuracy based on evidence

Supports mixing components from RARR, FacTool, and FactCheckGPT via YAML configuration.

### LLMEvaluator
Assesses LLM factual ability using **FactQA**: 6,480 examples across 482 domains from seven sources (Snowball, SelfAware, FreshQA, etc.).

### FactCheckerEvaluator
Meta-evaluation of fact-checking systems using **FactBench**: 4,507 human-annotated examples with precision, recall, and F1 metrics.

## Access

- Python: `pip install openfactcheck`
- Web: app.openfactcheck.com

## Mentioned In

- [[sources/openfactcheck-factuality-framework]] — architecture and datasets
