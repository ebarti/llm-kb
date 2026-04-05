---
title: "Source: Utilizing Frameworks like DeepSpeed and Megatron-LM"
type: source-summary
source: "[[raw/deepspeed-megatron-frameworks]]"
related: ["[[entities/deepspeed]]", "[[entities/megatron-lm]]", "[[concepts/distributed-training]]", "[[concepts/zero-optimizer]]"]
last_compiled: 2026-04-05
summary: "Detailed comparison of DeepSpeed (ZeRO Stages 1-3, Offload) and Megatron-LM (tensor/pipeline parallelism), plus their combination as Megatron-DeepSpeed for 3D parallelism training of trillion-parameter models."
---

## Key Points

- DeepSpeed ZeRO: Stage 1 (optimizer states), Stage 2 (+gradients), Stage 3 (+parameters)
- ZeRO-Offload extends to CPU/NVMe for memory-constrained scenarios
- Megatron-LM: tensor parallelism (split weight matrices) + pipeline parallelism (split layers)
- Megatron-DeepSpeed combines both for 3D parallelism
- DeepSpeed integrates easily (JSON config); Megatron requires model code changes
- Combined approach enables trillion-parameter training

## Detailed Summary

The article explains the complementary roles of [[entities/deepspeed]] and [[entities/megatron-lm]].

**DeepSpeed's ZeRO** progressively eliminates memory redundancy:
- Stage 1: Only partition optimizer states. Each GPU still holds full parameters and gradients.
- Stage 2: Also partition gradients. Significant memory reduction.
- Stage 3: Partition everything. Parameters retrieved just-in-time during forward/backward passes. Maximum memory efficiency.
- Offload: Push to CPU/NVMe when GPU memory is insufficient.

**Megatron-LM** handles models that exceed even ZeRO Stage 3's capacity by splitting computation itself:
- Tensor parallelism: split weight matrices within layers (communication-intensive, requires NVLink)
- Pipeline parallelism: split layers across GPUs (micro-batch scheduling to reduce bubble time)

**Megatron-DeepSpeed** combines ZeRO + pipeline parallelism (DeepSpeed) + tensor parallelism (Megatron-LM) for [[concepts/3d-parallelism]].

Operational complexity: configuration proliferation, distributed debugging across hundreds of GPUs, checkpoint compatibility challenges.

## Related Concepts

- [[entities/deepspeed]] — Microsoft's training framework
- [[entities/megatron-lm]] — NVIDIA's training framework
- [[concepts/zero-optimizer]] — DeepSpeed's memory optimization
- [[concepts/distributed-training]] — the overarching approach
- [[concepts/3d-parallelism]] — the combined strategy
