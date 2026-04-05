---
title: "DeepSeek"
type: entity
entity_type: org
sources: ["[[sources/deepseek-revolution-2026]]", "[[sources/bentoml-open-source-llms-2026]]", "[[sources/coding-models-comparison-2026]]", "[[sources/adaline-inside-reasoning-models]]", "[[sources/li-system1-system2-reasoning-survey]]"]
related: ["[[concepts/open-source-llms]]", "[[concepts/mixture-of-experts]]", "[[entities/qwen]]", "[[concepts/reasoning-models]]", "[[concepts/reinforcement-learning-for-reasoning]]", "[[entities/openai]]"]
last_compiled: 2026-04-05
summary: "Chinese AI lab whose R1 model (Jan 2025) triggered the 'DeepSeek moment' — demonstrating frontier reasoning at dramatically lower cost; V3.2 (685B, MIT) surpassed GPT-5-High on math."
---

## Overview

DeepSeek is a Chinese artificial intelligence research company that became a household name in January 2025 when its R1 model demonstrated ChatGPT-level reasoning capabilities at significantly lower training costs. This "DeepSeek moment" catalyzed a wave of open-source AI releases globally and challenged the assumption that frontier AI requires massive proprietary investment.

## Key Contributions

### DeepSeek R1 (January 2025)
- ChatGPT-level reasoning at fraction of the training cost
- Triggered global reassessment of AI economics
- Distilled 32B variant captures step-by-step reasoning
- **Architecture**: 671B MoE parameters with gating mechanism activating only relevant experts
- **Training**: 4-phase [[concepts/reinforcement-learning-for-reasoning|RL pipeline]] (cold start SFT on ~1K samples, GRPO RL, rejection sampling of 600K examples, diverse RL)
- **Training cost**: 2.66M H800 GPU hours
- **Benchmarks**: AIME 79.8%, MATH-500 97.3%, SWE-bench ~49%
- **Key feature**: Explicit, visible [[concepts/chain-of-thought|chain-of-thought]] (vs. OpenAI's hidden CoT)

### DeepSeek R1-Zero
Most scientifically significant result: pure RL training (no supervised fine-tuning) produced emergent reasoning behaviors including self-verification, backtracking, and error reflection. Demonstrates [[concepts/reinforcement-learning-for-reasoning|RL alone]] suffices for reasoning capability development.

### DeepSeek V3.2 (Late 2025)
- 685 billion total parameters, [[concepts/mixture-of-experts]] architecture
- MIT license (fully permissive)
- Gold-medal performance on International Math Olympiad
- Surpassed GPT-5-High on certain math benchmarks
- DeepSeek Sparse Attention (DSA): reduces inference costs by ~70%
- LMArena Elo ~1421

### DeepSeek Coder V2 Lite
- 14B active / 236B MoE total
- 338 programming languages
- Runs on consumer GPUs with 10-12GB VRAM
- Strong [[concepts/open-source-coding-models]] contender

### DeepSeek V4 (Expected 2026)
- Targeting 1 trillion total parameters with 32B active
- Native multimodality, 1M-token context window
- Training on Huawei Ascend chips (not NVIDIA)
- Hardware independence milestone

## Innovations

- **Sparse Attention (DSA)**: Reduces inference costs ~70% vs standard attention
- **Efficient MoE routing**: Optimized expert selection for high utilization
- **Distillation pipeline**: Compact models that preserve reasoning chains
- **Hardware diversification**: V4 proves frontier training possible without NVIDIA

## Impact

DeepSeek's releases catalyzed the release of 1,500+ open LLMs from Chinese organizations by mid-2025, making the open-source frontier ecosystem genuinely competitive. Five independent families (DeepSeek, [[entities/qwen]], Kimi, GLM, Mistral) simultaneously reached frontier quality.

## Mentioned In
- [[sources/deepseek-revolution-2026]] — primary profile of impact
- [[sources/bentoml-open-source-llms-2026]] — V3.2 ranked as S-tier model
- [[sources/coding-models-comparison-2026]] — Coder V2 Lite benchmarks
- [[sources/adaline-inside-reasoning-models]] — detailed technical analysis of R1 training pipeline
- [[sources/li-system1-system2-reasoning-survey]] — R1 in the context of System 2 reasoning
