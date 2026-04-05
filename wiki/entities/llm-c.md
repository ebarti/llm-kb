---
title: "llm.c"
type: entity
entity_type: tool
url: "https://github.com/karpathy/llm.c"
sources: ["[[sources/karpathy-educational-projects]]"]
related: ["[[entities/andrej-karpathy]]", "[[entities/nanogpt]]", "[[concepts/software-2-0]]"]
tags: [karpathy, C, CUDA, GPT, training, performance, open-source]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "LLM training in pure C/CUDA: ~3,000 lines reproducing GPT-2 (124M) in 90 minutes for $20, running 7% faster than PyTorch — Karpathy's proof that frameworks are optional."
---

## Overview

llm.c is [[entities/andrej-karpathy]]'s project for training large language models in simple, raw C and CUDA — eliminating the need for PyTorch (245MB) or Python (107MB). It represents both a pedagogical statement (the "real" program is the math, not the framework) and a practical achievement (faster than PyTorch Nightly).

## Key Facts

- **Type**: LLM training framework
- **Author**: [[entities/andrej-karpathy]]
- **Language**: C and CUDA
- **Code Size**: ~1,000 lines (CPU fp32 reference), ~3,000 lines (multi-GPU)
- **Performance**: ~7% faster than PyTorch Nightly, ~60% model flops utilization
- **Cost**: Reproduces GPT-2 (124M) in ~90 minutes for ~$20 on 8xA100 80GB
- **Supported Models**: GPT-2 (124M-1.6B), GPT-3 miniseries, Llama3
- **URL**: https://github.com/karpathy/llm.c

## Design Philosophy

The codebase maintains a clean separation between simplicity and optimization:
- Root-level files prioritize readability
- `/dev/cuda` houses increasingly sophisticated kernel implementations
- Multiple precision levels: fp32, bfloat16, mixed precision
- Distributed training via MPI+NCCL across GPUs and nodes
- Integrates cuBLAS, cuDNN, CUTLASS, and Flash Attention

## Significance

llm.c embodies [[concepts/software-2-0]] in a meta sense: by stripping away all framework abstraction, it reveals that LLM training is fundamentally just matrix operations. The fact that 3,000 lines of C/CUDA can match or beat PyTorch demonstrates how much of the deep learning stack is convenience wrapper rather than essential logic.

## Mentioned In

- [[sources/karpathy-educational-projects]] — project catalog
