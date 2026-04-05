---
title: "Textbooks Are All You Need — Microsoft Phi Models"
source: "https://www.microsoft.com/en-us/research/publication/textbooks-are-all-you-need/"
author: "Microsoft Research (Yuanzhi Li et al.)"
date_published: 2023-06-20
date_ingested: 2026-04-05
tags: [phi, synthetic-data, textbook-quality, small-language-models, microsoft]
type: paper
status: raw
discovered_via: search
---

# Textbooks Are All You Need — Microsoft Phi Models

## Overview

Microsoft Research paper introducing phi-1, a compact language model specializing in code generation. The work challenges the assumption that larger models are always superior by demonstrating strong performance from a relatively modest architecture.

## Model Architecture

Phi-1 employs a Transformer-based design with 1.3 billion parameters. Despite its small size compared to contemporary large language models, the architecture achieves notable coding capabilities through careful training methodology.

## Training Methodology & Data Strategy

**Training Resources:** 4 days on 8 A100 GPUs. Total tokens: 7 billion (6B web-sourced + 1B synthetic).

**Data Composition — dual-source approach:**
- **High-quality web data (6B tokens):** Carefully curated "textbook quality" content filtered from the internet
- **Synthetic data (1B tokens):** Programmatically generated textbooks and coding exercises created using GPT-3.5

This hybrid strategy prioritized data quality over quantity, focusing on fundamental programming concepts rather than broad world knowledge.

## The Phi Model Series

- **Phi-1 (1.3B):** 50.6% HumanEval, 55.5% MBPP pass@1
- **Phi-1-small (350M):** 45% HumanEval — demonstrating scalability
- **Phi-1.5 (1.3B):** Extended "textbook quality" approach to common sense reasoning in natural language
- **Phi-2 (2.7B):** Matches or outperforms models up to 25x larger on complex benchmarks
- **Phi-3:** Small language models with "big potential"
- **Phi-4:** Strategically incorporates synthetic data throughout training; substantially surpasses its teacher model (GPT-4) on STEM-focused QA — evidence that data-generation and post-training techniques go beyond distillation

## Synthetic Data Pipeline

Researchers repeatedly filtered the resulting content before feeding it back into an LLM for further synthesizing, building up a corpus large enough to train a more capable small language model. Care went into producing synthetic data by looking it over and filtering it, dubbing this dataset "CodeTextbook."

## Key Finding

Efficient training data selection outperforms scale. Data quality — not model size — is the decisive factor in model performance.
