---
title: "Megatron-LM"
type: entity
entity_type: tool
sources: ["[[sources/deepspeed-megatron-frameworks]]", "[[sources/jeremy-jordan-distributed-training]]"]
related: ["[[concepts/tensor-parallelism]]", "[[concepts/pipeline-parallelism]]", "[[concepts/distributed-training]]", "[[entities/deepspeed]]"]
last_compiled: 2026-04-05
summary: "NVIDIA's framework for training large transformer models, pioneering efficient tensor parallelism (splitting weight matrices within layers) and interleaved pipeline parallelism. Often combined with DeepSpeed as Megatron-DeepSpeed."
---

## Overview

Megatron-LM is NVIDIA's open-source framework for training very large transformer language models. It pioneered efficient [[concepts/tensor-parallelism]] — splitting individual weight matrices across GPUs within transformer layers — and advanced [[concepts/pipeline-parallelism]] with interleaved scheduling to reduce pipeline bubbles.

## Key Contributions

### Tensor Parallelism
Megatron-LM introduced the technique of splitting weight matrices in transformer layers across GPUs:
- Column partitioning on the first linear layer, row partitioning on the second
- This pairing eliminates one all-reduce per transformer block (50% communication reduction)
- Requires high-bandwidth NVLink connections (used within nodes)

### Interleaved Pipeline Parallelism
Instead of assigning contiguous layers to each GPU, assign non-contiguous layers. This creates more pipeline stages with smaller granularity, reducing bubble overhead.

### Integration Requirements
Unlike [[entities/deepspeed]], Megatron-LM requires modifying model code to use specialized layers that embed parallelism logic. This deeper integration yields higher efficiency but increases implementation complexity.

## Notable Training Runs

- **Megatron-Turing NLG 530B**: Joint NVIDIA-Microsoft training, combining Megatron's tensor parallelism with DeepSpeed's ZeRO
- **BLOOM 176B**: Trained using Megatron-DeepSpeed by BigScience
- Demonstrated 502 petaFLOP/s on 3072 GPUs for a 1T parameter model

## Mentioned In

- [[sources/deepspeed-megatron-frameworks]] — comparison with DeepSpeed, integration approach
- [[sources/jeremy-jordan-distributed-training]] — tensor parallelism mechanics
