---
title: "DeepSpeed"
type: entity
entity_type: tool
sources: ["[[sources/deepspeed-megatron-frameworks]]"]
related: ["[[concepts/zero-optimizer]]", "[[concepts/distributed-training]]", "[[concepts/data-parallelism]]", "[[entities/megatron-lm]]"]
last_compiled: 2026-04-05
summary: "Microsoft's open-source deep learning optimization library, best known for the ZeRO optimizer that progressively shards optimizer states, gradients, and parameters to enable training of models that exceed single-GPU memory."
---

## Overview

DeepSpeed is Microsoft's open-source library for efficient large-scale deep learning training and inference. Its flagship contribution is the [[concepts/zero-optimizer]] (Zero Redundancy Optimizer), which eliminates memory redundancy in [[concepts/data-parallelism]] by progressively sharding optimizer states, gradients, and model parameters across GPUs.

## Key Features

- **ZeRO Stages 1-3**: Progressive memory optimization (see [[concepts/zero-optimizer]])
- **ZeRO-Offload**: Extend to CPU/NVMe storage for extreme model sizes
- **Pipeline parallelism**: Micro-batch scheduling with interleaved stages
- **Mixed-precision training**: Automatic FP16/BF16 with loss scaling
- **Gradient accumulation and checkpointing**: Built-in memory optimization
- **Simple integration**: Wraps PyTorch models via `deepspeed.initialize()`, configured via JSON

## Integration with Megatron-LM

DeepSpeed and [[entities/megatron-lm]] are complementary rather than competing. **Megatron-DeepSpeed** combines ZeRO sharding + DeepSpeed pipeline parallelism + Megatron tensor parallelism for [[concepts/3d-parallelism]], enabling training of trillion-parameter models.

## Used By

BLOOM (176B), Megatron-Turing NLG (530B), and many other large-scale training runs have used DeepSpeed.

## Mentioned In

- [[sources/deepspeed-megatron-frameworks]] — ZeRO stages, integration, operational complexity
