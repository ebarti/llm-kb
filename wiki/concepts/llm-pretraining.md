---
title: "LLM Pretraining"
type: concept
sources: ["[[sources/mlops-pretraining-pipeline]]", "[[sources/analyticsvidhya-llm-pretraining-guide]]", "[[sources/raschka-pretraining-post-training-paradigms]]", "[[sources/chinchilla-scaling-laws-explained]]", "[[sources/training-costs-2026-analysis]]"]
related: ["[[concepts/next-token-prediction]]", "[[concepts/pretraining-data-pipeline]]", "[[concepts/distributed-training]]", "[[concepts/chinchilla-scaling-laws]]", "[[concepts/training-stability]]", "[[concepts/llm-training-costs]]", "[[concepts/multi-stage-pretraining]]"]
last_compiled: 2026-04-05
summary: "The foundational training phase where LLMs learn language by predicting the next token across trillions of tokens of text — the most compute-intensive and expensive stage of the LLM pipeline, costing $5M-$200M for frontier models."
---

## Overview

LLM pretraining is the initial, most resource-intensive phase of building a large language model. During pretraining, a model with billions of parameters is trained from scratch on massive text corpora (hundreds of billions to trillions of tokens) using [[concepts/next-token-prediction]] — a self-supervised objective that requires no labeled data. The model learns grammar, semantics, factual knowledge, reasoning patterns, and coding ability purely by predicting the next token given all preceding tokens.

Pretraining produces a **base model** — a "statistical pattern recognizer" or "internet document simulator" that can generate coherent text but lacks instruction-following ability or alignment. Subsequent post-training stages (supervised fine-tuning, RLHF/DPO) transform the base model into a useful assistant.

## The Pretraining Pipeline

A modern pretraining run involves several interconnected systems:

1. **Data Collection and Curation** ([[concepts/pretraining-data-pipeline]]): Gathering and filtering trillions of tokens from web crawls, books, code repositories, and other sources. Data quality is now recognized as more important than raw quantity.

2. **[[concepts/tokenization]]**: Converting raw text to token sequences using Byte Pair Encoding (BPE). GPT-4 uses a vocabulary of 100,277 tokens.

3. **Training Objective**: [[concepts/next-token-prediction]] via causal language modeling (CLM). The model outputs a probability distribution over the vocabulary at each position, optimized via cross-entropy loss.

4. **[[concepts/distributed-training]]**: Splitting the workload across thousands of GPUs using [[concepts/data-parallelism]], [[concepts/tensor-parallelism]], [[concepts/pipeline-parallelism]], and other strategies.

5. **[[concepts/training-stability]]**: Managing gradient explosions, [[concepts/loss-spikes]], numerical precision (BFloat16), and [[concepts/learning-rate-schedules]] to keep training on track across weeks or months.

## Scale of Modern Pretraining

| Model | Parameters | Training Tokens | GPUs | Duration | Estimated Cost |
|-------|-----------|----------------|------|----------|---------------|
| GPT-2 (2019) | 1.6B | 100B | Small cluster | — | ~$50K |
| GPT-3 (2020) | 175B | 300B | Thousands | — | ~$5-10M |
| Chinchilla (2022) | 70B | 1.4T | — | — | — |
| Llama 2 (2023) | 70B | 2T | — | — | — |
| Llama 3.1 (2024) | 405B | 15.6T | 16,384 H100s | 54 days | ~$170M |
| Qwen 2 (2024) | 72B | 7T | — | — | — |
| Gemma 2 (2024) | 27B | 13T | — | — | — |
| Apple AFM (2024) | ~6B | 7.4T total | — | — | — |
| DeepSeek V3 (2025) | 671B MoE | — | — | — | ~$5.6M |
| GPT-4 (2023) | ~1.8T MoE* | — | — | — | ~$100-150M |

*GPT-4 architecture is rumored but unconfirmed.

## Modern Innovations

### Multi-Stage Pretraining
All leading 2024 models use [[concepts/multi-stage-pretraining]]: general web data first, then high-quality data (math, code) with up-weighted proportions, then context-length extension with synthetic long-context data. See [[sources/raschka-pretraining-post-training-paradigms]] for details across Qwen, Apple, Gemma, and Llama.

### Instruction-Augmented Pretraining
Mixing synthetic instruction-response pairs into pretraining data itself, blurring the line between pretraining and fine-tuning.

### Reinforcement Pretraining (RPT)
Microsoft's 2025 approach reframes next-token prediction as sequential decision-making with reward signals, using on-policy reinforcement learning during pretraining.

### Overtraining for Inference Efficiency
Post-[[concepts/chinchilla-scaling-laws]], the industry has shifted toward training smaller models on far more data than compute-optimal ratios suggest. Llama 3 trains at 1,875:1 tokens-to-parameters; Qwen3-0.6B at 60,000:1. This makes inference cheaper over the model's lifetime.

## Key Challenges

- **Data exhaustion**: High-quality text data may be running out, driving interest in synthetic data
- **Training instability**: [[concepts/loss-spikes]] can destroy weeks of progress on expensive runs
- **Cost**: Frontier models cost $100M+ for a single training run
- **Copyright**: Legal uncertainty around using copyrighted web data
- **Environmental impact**: Training runs consume megawatts of power

## Sources

- [[sources/mlops-pretraining-pipeline]] — modern pretraining innovations (RPT, instruction-augmented, continual)
- [[sources/analyticsvidhya-llm-pretraining-guide]] — end-to-end pretraining mechanics (data pipeline, tokenization, training)
- [[sources/raschka-pretraining-post-training-paradigms]] — 2024 model comparisons (Qwen, Apple, Gemma, Llama)
- [[sources/chinchilla-scaling-laws-explained]] — compute-optimal training ratios
- [[sources/training-costs-2026-analysis]] — economics and cost breakdowns

## Related Concepts

- [[concepts/next-token-prediction]] — the training objective
- [[concepts/distributed-training]] — how training scales across GPUs
- [[concepts/chinchilla-scaling-laws]] — how to balance parameters and data
- [[concepts/training-stability]] — keeping training runs from diverging
- [[concepts/llm-training-costs]] — the economics
- [[concepts/fine-tuning]] — what comes after pretraining
