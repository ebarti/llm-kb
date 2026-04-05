---
title: "Source: Pretraining — Breaking Down the Modern LLM Training Pipeline"
type: source-summary
source: "[[raw/mlops-pretraining-pipeline]]"
related: ["[[concepts/llm-pretraining]]", "[[concepts/next-token-prediction]]", "[[concepts/pretraining-data-pipeline]]", "[[concepts/continual-pretraining]]"]
last_compiled: 2026-04-05
summary: "MLOps Community overview of the modern pretraining pipeline: next-token prediction foundations, data curation at trillion-token scale, and emerging innovations including instruction-augmented pretraining and reinforcement pretraining (RPT)."
---

## Key Points

- Pretraining is self-supervised next-token prediction requiring no labeled data
- Modern corpora span hundreds of billions to over 10 trillion tokens from web, books, code
- Data curation is one of the primary non-compute costs
- [[concepts/chinchilla-scaling-laws]] showed more data can outperform simply scaling model size
- Causal language modeling (CLM) is the standard objective for generative models

## Detailed Summary

The article traces pretraining from ULMFiT (2018) through modern innovations. The core task remains next-token prediction, but the ecosystem around it has become far more sophisticated.

**Data preparation** now involves deduplication, domain balancing, and curriculum learning rather than naive web scraping. Organizations invest heavily in data curation pipelines.

**Modern innovations** include:
- **Instruction-Augmented Pretraining**: Mixing synthetic instruction-response pairs with raw text during pretraining itself
- **Multi-Phase Pretraining**: Sequential phases with different data distributions (general -> high-quality)
- **[[concepts/continual-pretraining]]**: Extending existing checkpoints with new data, achieving ~2x cost reduction
- **Reinforcement Pretraining (RPT)**: Reframing next-token prediction as sequential decision-making with reward signals

Key challenges include copyright concerns, harmful content, and the risk of [[concepts/catastrophic-forgetting]] during continual pretraining.

## Notable Quotes

> "Next-token prediction, a self-supervised task that does not require labeled data."

> "Data curation has become one of the primary non-compute costs in LLM training."

## Related Concepts

- [[concepts/llm-pretraining]] — the core topic
- [[concepts/next-token-prediction]] — the fundamental training objective
- [[concepts/pretraining-data-pipeline]] — data preparation and curation
- [[concepts/continual-pretraining]] — extending existing model checkpoints
