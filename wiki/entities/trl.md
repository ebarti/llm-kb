---
title: "TRL (Transformers Reinforcement Learning)"
type: entity
entity_type: tool
sources: ["[[sources/huggingface-rlhf-illustrated]]", "[[sources/argilla-rlhf-alternatives-overview]]", "[[sources/wolfe-direct-preference-optimization]]"]
related: ["[[concepts/rlhf]]", "[[concepts/dpo]]", "[[concepts/kto]]", "[[concepts/ppo-for-llms]]", "[[entities/huggingface]]"]
last_compiled: 2026-04-05
summary: "HuggingFace's library for LLM alignment training, supporting SFT, PPO, DPO, IPO, KTO, and ORPO -- the de facto standard open-source toolkit for preference optimization."
---

## Overview

TRL (Transformers Reinforcement Learning) is HuggingFace's open-source library for training language models with reinforcement learning and preference optimization. It has become the de facto standard for implementing alignment methods in the open-source ecosystem.

## Supported Methods
- **SFT** (Supervised Fine-Tuning)
- **PPO** ([[concepts/ppo-for-llms]])
- **DPO** ([[concepts/dpo]])
- **IPO** ([[concepts/ipo]])
- **KTO** ([[concepts/kto]])
- **ORPO** ([[concepts/orpo]])

## Usage Example (DPO)
```python
from trl import DPOConfig, DPOTrainer
trainer = DPOTrainer(model, args, train_dataset=preferences)
trainer.train()
```

## Mentioned In
- [[sources/huggingface-rlhf-illustrated]] -- as an open-source RLHF tool
- [[sources/argilla-rlhf-alternatives-overview]] -- as the standard implementation library
- [[sources/wolfe-direct-preference-optimization]] -- DPOTrainer usage
