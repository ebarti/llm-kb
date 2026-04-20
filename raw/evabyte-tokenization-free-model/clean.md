---
title: "EvaByte: Efficient Byte-Level Language Models at Scale"
source: "https://hkunlp.github.io/blog/2025/evabyte/"
author: "HKU NLP Group / SambaNova Systems"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [tokenization-free, byte-level, language-model, evabyte, eva-architecture]
type: article
status: raw
discovered_via: search
---

# EvaByte: Efficient Byte-Level Language Models at Scale

## Overview

EvaByte is a 6.5B parameter language model developed by University of Hong Kong and SambaNova Systems that processes raw bytes instead of tokens. Trained on 1.5 trillion bytes. Demonstrates that efficient byte-level processing at scale is not just possible, but practically advantageous.

## Key Performance

- Matches modern tokenizer-based models despite using significantly less training data
- Outperforms similarly-sized models on standard evaluation tasks
- Achieves faster inference — up to 2x speedier than token-based alternatives on a single H800 GPU
- Excels in coding tasks (HumanEval, MBPP) — byte-level processing eliminates domain-specific tokenizer biases

## Architecture Innovations

### Multibyte Prediction
Eight prediction heads simultaneously predict multiple future bytes. During training, losses from all heads are averaged, creating minimal overhead given the small vocabulary (320 tokens: 256 byte values + 64 special tokens). At inference, enables self-speculative decoding where multiple heads combine via Medusa-like tree attention.

### EVA: Efficient Attention Mechanism
Distributes computational state across multiple local memory slots rather than compressing all information into a single global state. Splits key-value pairs into consecutive chunks and applies linearization separately on each chunk, maintaining distinct hidden states per chunk while remaining hardware-compatible. Achieves linear complexity relative to sequence length.

## Addressing Byte-Level Challenges

Byte sequences are naturally 3.8x longer than tokenized equivalents. EvaByte overcomes this with 5-10x faster decoding compared to vanilla architectures.

## Multimodal Capabilities

Naturally extends to multimodal applications by treating images as byte streams (using JPEG encoding), enabling seamless interleaving of image and text bytes without architectural tweaks. After fine-tuning on ~3 million images, demonstrates basic image captioning and visual QA.

## Training Stability

Occasional "byte-level collapses" produced unusual character substitutions. Stabilization required reducing Adam epsilon from 1e-8 to 1e-12, selectively skipping problematic batches, and periodically resetting optimizer states.

## vs. Byte Latent Transformers (BLTs)

EvaByte achieves superior performance with 3-4x fewer training bytes by directly operating on bytes without patchification or external auxiliary models.
