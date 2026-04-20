---
title: "Let's Build the GPT Tokenizer — Karpathy minbpe Lecture"
source: "https://github.com/karpathy/minbpe/blob/master/lecture.md"
author: "Andrej Karpathy"
date_published: 2024-02-01
date_ingested: 2026-04-05
tags: [tokenization, bpe, minbpe, karpathy, tutorial, gpt]
type: video
status: raw
discovered_via: search
---

# Let's Build the GPT Tokenizer — Karpathy minbpe Lecture

## Overview

Andrej Karpathy's 2-hour 13-minute lecture introduces tokenization as a critical but complex component of large language models. Many apparent LLM limitations actually stem from tokenization rather than neural architecture flaws.

## Core Topics

### Character-Level Tokenization Foundation
Begins with a review of naive character-level encoding. Demonstrates constructing a vocabulary by identifying unique characters in training data (Shakespeare example yields 65 characters), then creating lookup tables to convert between characters and integer indices.

### Byte Pair Encoding (BPE) Algorithm
Progresses to practical tokenization using BPE, which operates on character chunks rather than individual characters. OpenAI's GPT-2 paper (2019) popularized byte-level BPE, expanding vocabularies to approximately 50,257 tokens with context lengths of 1024.

### Real-World Tokenization Complexities
Highlights inconsistent tokenization patterns through concrete examples:
- Numbers split arbitrarily (677 becomes " 6" + "77" while 127 remains single token)
- Whitespace presence significantly affects tokenization but remains invisible
- Word boundaries and language-specific characters create unpredictable token boundaries

## Key Insights: LLM Issues Traced to Tokenization

Karpathy catalogs problems attributable to tokenization:
- **Spelling difficulties** and string reversal failures
- **Poor performance on non-English languages**
- **Arithmetic computation struggles**
- **Unexpected halting** at special tokens like "<|endoftext|>"
- **Inconsistent behavior** with specific text patterns

## The minbpe Repository

Released alongside the lecture, minbpe contains minimal, clean code for BPE commonly used in LLM tokenization. Two tokenizers implement three primary functions:
1. **Training** the tokenizer vocabulary and merges on a given text
2. **Encoding** from text to tokens
3. **Decoding** from tokens to text

## Interactive Resources

References tiktokenizer.vercel.app for real-time visualization of how text encodes into tokens using GPT-2's tokenizer.

## Key Takeaway

Karpathy discusses how many weird behaviors and problems of LLMs trace back to tokenization and why someone ideally finds a way to delete this stage entirely.
