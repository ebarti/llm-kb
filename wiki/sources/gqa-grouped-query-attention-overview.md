---
title: "Source: Grouped Query Attention (GQA) Overview"
type: source-summary
source: "[[raw/gqa-grouped-query-attention-overview]]"
related: ["[[concepts/grouped-query-attention]]", "[[concepts/multi-head-attention]]", "[[concepts/kv-cache]]", "[[comparisons/mha-vs-gqa-vs-mqa]]"]
tags: [GQA, MQA, multi-head-attention, KV-cache, efficient-inference]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "IBM overview of Grouped Query Attention: GQA generalizes MHA and MQA by sharing KV heads across query head groups — reducing KV cache by up to 90%, 30-40% faster inference, with only 5% of pre-training compute needed to uptrain existing MHA checkpoints."
---

## Key Points

- GQA is a generalization: MHA (all unique KV heads) and MQA (single KV head) are special cases
- Divides query heads into G groups, each sharing one KV head
- Reduces KV cache size by up to 90% vs MHA
- 30-40% faster inference than MHA while retaining near-equivalent accuracy
- Existing MHA checkpoints can be uptrained to GQA with only 5% of original pre-training compute
- Adopted by Llama 2/3, Mistral 7B, IBM Granite 3.0, Google Gemma, DeepSeek

## Detailed Summary

The IBM article provides a clear overview of Grouped Query Attention, the attention variant that has become the default for production LLM deployment. GQA addresses the fundamental inference bottleneck of [[concepts/multi-head-attention]]: the [[concepts/kv-cache]] stores separate Key and Value tensors for every attention head, consuming memory proportional to the number of heads.

GQA's solution is elegant: divide the query heads into G groups, and within each group share a single set of Key and Value heads. This creates a smooth spectrum between full MHA (G = number of heads, each with unique KV) and MQA (G = 1, single shared KV for all queries). In practice, models like Llama 2 use 8 KV heads for 32 query heads (4:1 grouping).

The practical benefit is a 30-40% inference speedup with negligible quality loss. More importantly, existing MHA-trained checkpoints can be converted to GQA through "uptraining" with only 5% of original pre-training compute, avoiding the need to retrain from scratch.

By 2024-2025, GQA became the standard: Llama 2/3, Mistral, Gemma, Granite, and DeepSeek all use GQA, making full MHA effectively obsolete for inference-optimized models.

## Concepts Introduced or Discussed

- [[concepts/grouped-query-attention]] — the core technique
- [[concepts/multi-head-attention]] — the original mechanism being optimized
- [[concepts/kv-cache]] — the memory bottleneck being addressed

## Metadata

- **Author**: IBM / based on Ainslie et al. (Google)
- **Date Published**: 2023-05
- **Format**: article
- **URL**: https://www.ibm.com/think/topics/grouped-query-attention
