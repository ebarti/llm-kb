---
title: "Infinite Context Approaches: StreamingLLM, Infini-attention, Ring Attention, InfLLM"
source: "multiple"
author: "Various researchers"
date_published: 2024-04-01
date_ingested: 2026-04-05
tags: [infinite-context, streaming, ring-attention, infini-attention, architecture]
type: article
status: raw
discovered_via: search
---

# Infinite Context Approaches for LLMs

## StreamingLLM (MIT Han Lab, ICLR 2024)

An efficient framework enabling LLMs trained with finite-length attention windows to generalize to infinite sequence length without fine-tuning.

- **Mechanism**: Maintains "attention sinks" (KV states of initial tokens) plus a rolling window caching the most recent tokens' KV states.
- **Key insight**: Initial tokens serve as attention sinks regardless of their semantic content; removing them causes attention scores to collapse.
- **Result**: Enables streaming inference with stable perplexity over unlimited sequence lengths.
- **Limitation**: Cannot attend to tokens outside the current window — no long-range retrieval.

## Infini-attention (Google, 2024)

Incorporates compressive memory into vanilla attention, combining local and long-term attention in a single Transformer block.

- **Architecture**: Combines masked local attention (nearby tokens) with long-term linear attention (extended context).
- **Compressive memory**: Bounded memory system storing compressed representations of prior context.
- **Results**: Effective on 1M-token passkey retrieval, 500K-token book summarization. Tested on 1B and 8B parameter LLMs.
- **Key advantage**: Minimal bounded memory parameters, enables fast streaming inference. Scales to infinitely long context with bounded memory and compute.

## Ring Attention (UC Berkeley, 2023)

Distributes long sequences across multiple devices through blockwise computation.

- **Mechanism**: Leverages blockwise computation of self-attention and feedforward, distributing across devices while fully overlapping communication of KV blocks with attention computation.
- **Key advantage**: No approximations required — maintains full accuracy. Zero communication overhead.
- **Scalability**: Enables sequences up to device-count times longer than single-device memory-efficient Transformers.
- **Authors**: Hao Liu, Matei Zaharia, Pieter Abbeel. arXiv:2310.01889.

## InfLLM (Training-Free)

A training-free method for long-context extrapolation.

- **Mechanism**: Stores distant contexts in additional memory units. Employs efficient lookup mechanism to retrieve token-relevant units for attention computation.
- **Advantage**: No fine-tuning required; works with existing pretrained models.

## Comparison

| Approach | Training Required | Memory Bound | Retrieval Capability | Multi-Device |
|----------|------------------|--------------|---------------------|--------------|
| StreamingLLM | No | Fixed window | No (recent only) | No |
| Infini-attention | Yes | Bounded | Yes (compressive) | No |
| Ring Attention | Yes | Scales with devices | Yes (full) | Yes |
| InfLLM | No | External memory | Yes (lookup) | No |
