---
title: "Source: Demystifying Synthetic Data in LLM Pre-training"
type: source-summary
source: "[[raw/synthetic-data-llm-pretraining-study]]"
related: ["[[concepts/synthetic-data-in-pretraining]]", "[[concepts/model-collapse]]", "[[concepts/scaling-laws]]", "[[concepts/training-data-curation]]"]
last_compiled: 2026-04-05
summary: "Systematic study (1,000+ model variants, 100K GPU hours) finding that 30% high-quality rephrased synthetic data mixed with 70% natural web text is optimal, while pure synthetic or textbook-style data shows model collapse patterns."
---

## Key Points

- 1,000+ model variants up to 3B parameters on datasets up to 200B tokens
- **Optimal mixture**: 30% HQ rephrased synthetic + 70% natural web text → 5-10x speedup to target loss
- Pure synthetic data is NOT superior to CommonCrawl
- Textbook-style data shows model collapse patterns at small data budgets
- Rephrased data shows no degradation at foreseeable scales
- **8B generators outperform both 3B and 70B** — larger is not always better
- Synthetic data benefits are conditional: better for data scaling than model scaling
- 33% HQ rephrased + 67% CC shows lowest projected irreducible loss

## Detailed Summary

This is the most comprehensive empirical study of synthetic data in LLM pretraining to date. The researchers tested three types of synthetic data (HQ rephrasing, QA rephrasing, textbook generation) at four mixture ratios (0%, 33%, 67%, 100%) across multiple model and data scales.

The headline finding — that ~30% rephrased synthetic mixed with ~70% natural data is optimal — holds remarkably consistently across scales. Pure synthetic data never beats natural data, and textbook-style generation (inspired by the [[entities/microsoft-phi]] approach) shows troubling patterns at smaller scales that resemble theoretical predictions of [[concepts/model-collapse]].

A counterintuitive finding about generator model size: 8B-parameter generators consistently produce better training data than 70B-parameter generators. The authors speculate this relates to diversity-quality tradeoffs — larger models may produce more polished but less diverse outputs.

The work also establishes that synthetic data is more beneficial for data scaling (training on more tokens) than for model scaling (training larger models), suggesting that as frontier models grow, the marginal value of synthetic data may diminish.

## Notable Quotes

> "Synthetic data requires careful, empirically-informed deployment, rather than being a universal solution to data constraints."

## Related Concepts

- [[concepts/synthetic-data-in-pretraining]] — the definitive empirical guide to mixture ratios
- [[concepts/model-collapse]] — textbook data shows collapse; rephrased data does not
- [[concepts/scaling-laws]] — synthetic data scaling differs from natural data scaling
- [[concepts/training-data-curation]] — synthetic data as one tool in the curation arsenal
