---
title: "InstructGPT"
type: entity
entity_type: paper
sources: ["[[sources/huggingface-rlhf-illustrated]]"]
related: ["[[concepts/rlhf]]", "[[concepts/reward-model]]", "[[concepts/instruction-tuning]]", "[[concepts/ppo-for-llms]]", "[[entities/openai]]"]
last_compiled: 2026-04-05
summary: "OpenAI's 2022 paper that demonstrated the three-step RLHF pipeline (SFT, reward model training, PPO) at scale, producing a 1.3B parameter model preferred over the 175B GPT-3 -- the direct precursor to ChatGPT."
---

## Overview

InstructGPT (Ouyang et al., 2022) was the first major demonstration of [[concepts/rlhf]] applied to large language models. Published by OpenAI, it showed that a 1.3B parameter model fine-tuned with RLHF was preferred by human evaluators over the 175B parameter GPT-3 -- proving that alignment techniques could be more impactful than raw scale.

## Key Contributions

- Established the three-step pipeline: SFT on demonstrations, [[concepts/reward-model]] training on comparisons, [[concepts/ppo-for-llms]] optimization
- Showed 175B LM could be aligned using a 6B reward model
- Demonstrated that aligned small models outperform unaligned large models
- Used ~50k preference comparisons for reward model training
- Directly led to ChatGPT (November 2022), which used the same RLHF pipeline

## Historical Impact

InstructGPT proved the viability of RLHF at scale and triggered the entire field of LLM alignment research. Every major RLHF paper since 2022 builds on this foundation.

## Mentioned In
- [[sources/huggingface-rlhf-illustrated]] -- as the foundational RLHF application
