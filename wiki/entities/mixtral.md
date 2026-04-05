---
title: "Mixtral 8x7B"
type: entity
entity_type: tool
sources: ["[[sources/huggingface-mixture-of-experts]]", "[[sources/moe-models-comparison-2025]]"]
related: ["[[concepts/mixture-of-experts]]", "[[concepts/transformer-architecture]]", "[[concepts/grouped-query-attention]]"]
last_compiled: 2026-04-05
summary: "Mistral AI's 2023 open-weight MoE model: 47B total parameters, 8 experts with 2 active per token (~12B FLOPs), outperforming Llama 2 70B while running at 12B-model speed."
---

## Overview

Mixtral 8x7B (Mistral AI, December 2023) was the breakthrough open-weight [[concepts/mixture-of-experts]] model that proved MoE's practical value. With 47B total parameters but only ~12B FLOPs per token (2 of 8 experts active), it outperformed the 70B-parameter Llama 2 while running at the speed of a 12B model.

## Architecture

- **Total parameters**: 47B
- **Active per token**: ~12-14B
- **Experts per layer**: 8
- **Active experts**: 2 (top-2 routing)
- **Attention**: [[concepts/grouped-query-attention]] with 8 KV groups
- **VRAM requirement**: 47B (all experts always loaded)

## Performance

- Outperforms Llama 2 70B on most benchmarks
- Inference latency comparable to a 12B dense model
- Available as both base and instruct variants under Apache 2.0

## Impact

Mixtral demonstrated that MoE was not just a research curiosity but a practical architecture for deployment. It directly influenced the MoE adoption wave: DeepSeek V2/V3/R1, Llama 4, Qwen3 all followed the MoE path.

## Mentioned In

- [[sources/huggingface-mixture-of-experts]] — architecture details and benchmarks
- [[sources/moe-models-comparison-2025]] — in context of 2025 MoE model landscape
