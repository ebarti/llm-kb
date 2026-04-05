---
title: "nanoGPT"
type: entity
entity_type: tool
url: "https://github.com/karpathy/nanoGPT"
sources: ["[[sources/karpathy-educational-projects]]"]
related: ["[[entities/andrej-karpathy]]", "[[entities/micrograd]]", "[[entities/minbpe]]", "[[entities/llm-c]]", "[[concepts/software-2-0]]"]
tags: [karpathy, GPT, transformer, training, education, open-source]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Karpathy's simplest, fastest GPT training repository: reproduces GPT-2 (124M) on OpenWebText in ~4 days on 8xA100, serving as both educational reference and practical training tool."
---

## Overview

nanoGPT is [[entities/andrej-karpathy]]'s repository for training and fine-tuning medium-sized GPT models. It is a rewrite of minGPT that prioritizes training efficiency over pure educational clarity, while remaining readable and well-documented.

## Key Facts

- **Type**: Open-source GPT training framework
- **Author**: [[entities/andrej-karpathy]]
- **Language**: Python (PyTorch)
- **Performance**: Reproduces GPT-2 (124M) on OpenWebText in ~4 days on 8xA100 40GB
- **URL**: https://github.com/karpathy/nanoGPT

## Related Projects

- **minGPT** (predecessor): Minimal PyTorch GPT re-implementation, education-first
- **build-nanogpt**: Video+code lecture building nanoGPT from an empty file — the pedagogical companion
- **[[entities/llm-c]]**: The C/CUDA successor, even faster and framework-free

## Educational Role

nanoGPT bridges the gap between understanding transformers (via [[entities/micrograd]] and the Zero to Hero series) and training production-quality models. The build-nanogpt companion project walks through every line of code in a single lecture, making the full Transformer training pipeline accessible.

## Mentioned In

- [[sources/karpathy-educational-projects]] — project catalog
