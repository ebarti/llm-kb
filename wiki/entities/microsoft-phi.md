---
title: "Microsoft Phi Models"
type: entity
entity_type: paper
sources: ["[[sources/textbooks-are-all-you-need-phi]]"]
related: ["[[concepts/synthetic-data-generation]]", "[[concepts/data-quality-bottleneck]]", "[[concepts/knowledge-distillation]]"]
last_compiled: 2026-04-05
summary: "Microsoft Research model family (phi-1 through phi-4) demonstrating that 'textbook quality' synthetic data enables small models (1.3B-14B) to rival or surpass models 10-25x larger."
---

## Overview

The Phi model series from Microsoft Research is the strongest empirical evidence that training data quality outperforms model scale. Beginning with phi-1 for code generation, the series has systematically demonstrated that carefully curated "textbook quality" data — combining filtered web content with LLM-generated synthetic textbooks and exercises — enables small language models to achieve performance competitive with much larger models.

## Model Timeline

| Model | Parameters | Key Achievement | Year |
|-------|-----------|-----------------|------|
| Phi-1 | 1.3B | 50.6% HumanEval (code) with only 7B tokens | 2023 |
| Phi-1-small | 350M | 45% HumanEval — scaling approach works at tiny size | 2023 |
| Phi-1.5 | 1.3B | Common sense reasoning matching 5x larger models | 2023 |
| Phi-2 | 2.7B | Matches/outperforms models up to 25x larger | 2023 |
| Phi-3 | 3.8B-14B | "Small language models with big potential" | 2024 |
| Phi-4 | 14B | Surpasses GPT-4 (its teacher) on STEM QA | 2024 |

## The "Textbook Quality" Methodology

### Data Curation
1. **Web filtering**: Select "textbook quality" content from internet (6B tokens for phi-1)
2. **Synthetic generation**: Use GPT-3.5 to create textbooks and exercises (1B tokens for phi-1)
3. **Iterative refinement**: Generate → filter → feed back → generate more
4. **Quality over quantity**: 7B total tokens vs. hundreds of billions for comparable models

### Key Insight: Beyond Distillation
Phi-4 is particularly significant because it surpasses its teacher model (GPT-4) on STEM benchmarks. This demonstrates that [[concepts/synthetic-data-generation]] combined with rigorous filtering goes beyond simple [[concepts/knowledge-distillation]] — it creates novel capabilities through data quality amplification.

## Training Efficiency

Phi-1 was trained in 4 days on 8 A100 GPUs — a tiny fraction of typical LLM training cost. This makes the approach accessible to research labs and organizations without hyperscaler-scale compute.

## Significance for the Field

The Phi models established several principles now considered foundational:
1. Data quality > data quantity > model size (for a given compute budget)
2. Synthetic data can be better than web-scraped data if carefully generated and filtered
3. Small models can be practical alternatives to large models for specific domains
4. The teacher-surpassing-student result challenges assumptions about [[concepts/knowledge-distillation]] limits

## Mentioned In

- [[sources/textbooks-are-all-you-need-phi]] — primary source on methodology and results
- [[concepts/synthetic-data-generation]] — phi as canonical example of synthetic data success
- [[concepts/data-quality-bottleneck]] — phi proves data quality > scale
