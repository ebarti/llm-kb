---
title: "Grouped Query Attention (GQA): Efficient Inference for LLMs"
source: "https://www.ibm.com/think/topics/grouped-query-attention"
author: "IBM / Ainslie et al. (Google)"
date_published: 2023-05-01
date_ingested: 2026-04-05
tags: [GQA, MQA, multi-head-attention, KV-cache, efficient-inference]
type: article
status: raw
discovered_via: search
---

# Grouped Query Attention (GQA)

## Overview

Grouped Query Attention (GQA) increases the efficiency of the attention mechanism in transformer models, enabling faster inference from large language models.

## GQA as a Generalization

GQA is a generalization of multi-head attention (MHA) and multi-query attention (MQA):
- GQA with same number of KV head groups as attention heads = standard MHA
- GQA with 1 head group = MQA

## Multi-Query Attention (MQA)

MQA uses a single key-value head, drastically speeding up decoder inference. However, MQA can lead to quality degradation and may not be desirable for training separate models.

## How GQA Works

GQA divides query heads into G groups, each sharing a single key and value head. This provides an intermediate tradeoff between MHA (full KV heads) and MQA (single KV head).

## Key Advantages

- Nearly as accurate as MHA while nearly as fast as MQA
- Reduces KV cache size by up to 90% vs MHA
- 30-40% faster inference speed than MHA
- Can uptrain existing MHA checkpoints to GQA using only 5% of original pre-training compute

## Adoption in Major Models

- Meta Llama 2 and Llama 3 (July 2023, 2024)
- Mistral 7B (September 2023)
- IBM Granite 3.0
- Google Gemma models
- DeepSeek models

## Performance Impact

GQA significantly reduces the number of intermediate calculations that must be computed, stored, and retrieved at inference time, making it the dominant approach for production LLM deployment.
