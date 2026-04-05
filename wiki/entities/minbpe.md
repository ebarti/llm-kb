---
title: "minbpe"
type: entity
entity_type: tool
sources: ["[[sources/karpathy-minbpe-lecture]]", "[[sources/karpathy-educational-projects]]"]
related: ["[[concepts/byte-pair-encoding]]", "[[concepts/tokenization]]", "[[entities/andrej-karpathy]]", "[[entities/nanogpt]]", "[[entities/micrograd]]", "[[concepts/context-windows]]"]
last_compiled: 2026-04-05
summary: "Karpathy's minimal, clean reference implementation of BPE tokenization — the most widely-cited educational codebase for understanding LLM tokenization."
---

## Overview

minbpe is a GitHub repository by [[entities/andrej-karpathy]] containing minimal, clean code for the Byte Pair Encoding (BPE) algorithm commonly used in LLM tokenization. Released alongside Karpathy's 2-hour 13-minute tokenization lecture, it has become the most popular educational reference for understanding how LLM tokenizers work.

## Key Features

- Two tokenizer implementations with three core functions: train, encode, decode
- Builds from character-level encoding up to GPT-2-compatible BPE
- Prioritizes clarity and readability over performance
- Designed to be studied, not used in production (unlike [[entities/tiktoken]])

## Mentioned In

- [[sources/karpathy-minbpe-lecture]] — built from scratch during the accompanying lecture
