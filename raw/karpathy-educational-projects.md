---
title: "Karpathy's Educational Open-Source Projects"
source: "https://github.com/karpathy"
author: "Andrej Karpathy"
date_published: 2024-04-01
date_ingested: 2026-04-05
tags: [karpathy, micrograd, nanoGPT, minbpe, llm.c, education, open-source]
type: article
status: raw
discovered_via: search
---

# Karpathy's Educational Open-Source Projects

## micrograd
- **Repository**: github.com/karpathy/micrograd
- **Description**: A tiny scalar-valued autograd engine (~100 lines) and neural net library (~50 lines) with PyTorch-like API
- **Purpose**: Educational — demonstrates backpropagation at scalar level so students don't need to deal with tensor complexity
- **Features**: Reverse-mode automatic differentiation over dynamically built DAG, graphviz visualization, binary classification demo
- **License**: MIT

## nanoGPT
- **Repository**: github.com/karpathy/nanoGPT
- **Description**: Simplest, fastest repository for training/finetuning medium-sized GPTs
- **Performance**: Reproduces GPT-2 (124M) on OpenWebText on a single 8xA100 40GB node in ~4 days
- **Rewrite of**: minGPT (prioritizes efficiency over education)
- **Related**: build-nanogpt (video+code lecture building nanoGPT from scratch)

## minGPT
- **Repository**: github.com/karpathy/minGPT
- **Description**: Minimal PyTorch re-implementation of the OpenAI GPT training
- **Purpose**: Educational focus over performance

## minbpe
- **Repository**: github.com/karpathy/minbpe
- **Description**: Minimal, clean code for the BPE algorithm used in LLM tokenization
- **Components**:
  - BasicTokenizer: Simplest BPE running directly on text
  - RegexTokenizer: Splits input by regex before tokenization (like GPT-4's tiktoken)
  - GPT4Tokenizer: Light wrapper reproducing GPT-4's tokenization exactly
- **Key Feature**: Unlike tiktoken, allows training your own tokenizer
- **Accompanies**: "Let's Build the GPT Tokenizer" video lecture

## llm.c
- **Repository**: github.com/karpathy/llm.c
- **Description**: LLM training in simple, raw C/CUDA — no PyTorch, no Python needed
- **Performance**: ~7% faster than PyTorch Nightly, ~60% model flops utilization
- **Achievement**: Reproduces GPT-2 (124M) in ~90 minutes for ~$20 on 8xA100 80GB
- **Code Size**: ~1,000 lines (CPU reference), ~3,000 lines (multi-GPU C/CUDA)
- **Supports**: GPT-2, GPT-3 miniseries, Llama3, multiple precisions (fp32, bfloat16, mixed)
- **Goal**: Reliable, stable, minimal, hardened LLM stack in pure C/CUDA

## nanochat
- **Repository**: github.com/karpathy/nanochat
- **Description**: "The best ChatGPT that $100 can buy"

## Neural Networks: Zero to Hero (YouTube Series)
- **URL**: karpathy.ai/zero-to-hero.html
- **Videos**: 8 lectures, building from micrograd through makemore to GPT
- **Prerequisites**: Basic Python, vague calculus recollection
- **Content**:
  1. Building micrograd (backpropagation, 2h25m)
  2. Building makemore (bigram language model, 1h57m)
  3. Makemore Part 2: MLP (1h15m)
  4. Makemore Part 3: Activations, Gradients, BatchNorm (1h55m)
  5. Makemore Part 4: Becoming a Backprop Ninja (56m)
  6. Makemore Part 5: Building a WaveNet (56m)
  7. Building GPT from scratch (1h56m)
  8. Building the GPT Tokenizer (2h13m)
