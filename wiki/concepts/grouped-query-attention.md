---
title: "Grouped-Query Attention (GQA)"
type: concept
sources: ["[[sources/kv-cache-optimization-techniques]]", "[[sources/gqa-grouped-query-attention-overview]]"]
related: ["[[concepts/multi-head-attention]]", "[[concepts/kv-cache]]", "[[concepts/transformer-architecture]]", "[[concepts/attention-mechanisms]]", "[[comparisons/mha-vs-gqa-vs-mqa]]"]
last_compiled: 2026-04-05
summary: "Attention variant sharing KV heads across groups of query heads — interpolating between full multi-head attention (MHA) and multi-query attention (MQA) to reduce KV cache memory with minimal quality loss."
---

## Overview

Grouped-Query Attention (GQA) is an optimization of [[concepts/multi-head-attention]] that reduces [[concepts/kv-cache]] memory by sharing key-value (KV) heads across multiple query heads. It was introduced by Ainslie et al. (2023) as a generalization that interpolates between:

- **Multi-Head Attention (MHA)**: Each query head has its own KV head (standard, maximum quality)
- **Multi-Query Attention (MQA)**: All query heads share a single KV head (maximum efficiency, some quality loss)
- **GQA**: Query heads divided into G groups, each group sharing one KV head

## How It Works

In standard MHA with H query heads, there are H KV head pairs. In GQA with G groups:
- H query heads (unchanged)
- G KV head pairs (G < H)
- Each group of H/G query heads shares one KV pair
- Cache reduction factor: H/G

## Adoption

| Model | Query Heads | KV Heads | Groups | Cache Reduction |
|-------|-------------|----------|--------|-----------------|
| Llama-2-7B | 32 | 32 | 32 (MHA) | 1x |
| Llama-2-70B | 64 | 8 | 8 | 8x |
| Mistral-7B | 32 | 8 | 8 | 4x |
| Mixtral 8x7B | 32 | 8 | 8 | 4x |
| Falcon-40B | 64 | 8 | 8 | 8x |
| Gemma-2B | 16 | 2 | 2 | 8x |

## Quality-Speed Tradeoff

The Llama-2 paper reports that "key and value projections can be shared across multiple heads without much degradation." GQA achieves quality close to MHA with speed comparable to MQA.

Uptraining from existing MHA checkpoints to GQA is possible: start with a pre-trained MHA model, mean-pool the KV heads within each group, and continue training briefly.

## Sources

- [[sources/kv-cache-optimization-techniques]] — GQA in context of full KV cache optimization stack

## Related Concepts

- [[concepts/multi-head-attention]] — the standard attention GQA optimizes
- [[concepts/kv-cache]] — the memory bottleneck GQA addresses
- [[concepts/sliding-window-attention]] — complementary optimization (often combined)
