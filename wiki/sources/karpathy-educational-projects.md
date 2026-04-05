---
title: "Source: Karpathy's Educational Open-Source Projects"
type: source-summary
source: "[[raw/karpathy-educational-projects]]"
related: ["[[entities/andrej-karpathy]]", "[[entities/eureka-labs]]", "[[concepts/software-2-0]]", "[[entities/nanogpt]]", "[[entities/micrograd]]", "[[entities/minbpe]]", "[[entities/llm-c]]"]
tags: [karpathy, education, open-source, micrograd, nanoGPT, minbpe, llm.c]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Catalog of Karpathy's educational open-source projects: micrograd (autograd in 100 lines), nanoGPT (GPT-2 reproduction), minbpe (BPE tokenizer), llm.c (LLM training in pure C/CUDA), and the Zero to Hero YouTube series."
---

## Key Points

- **micrograd**: Autograd engine in ~100 lines + neural net library in ~50 lines; demonstrates backpropagation at scalar level for pedagogy
- **nanoGPT**: Reproduces GPT-2 (124M) on OpenWebText in ~4 days on 8xA100; efficiency-focused rewrite of minGPT
- **minbpe**: Clean BPE tokenizer implementation with BasicTokenizer, RegexTokenizer, and GPT4Tokenizer; allows training custom tokenizers unlike tiktoken
- **llm.c**: LLM training in pure C/CUDA (~3,000 lines), ~7% faster than PyTorch Nightly; reproduces GPT-2 (124M) in 90 minutes for $20
- **Zero to Hero**: 8-lecture YouTube series building from micrograd to GPT, requiring only Python and basic calculus

## Detailed Summary

Karpathy's open-source projects form a coherent educational stack that teaches deep learning from first principles. They share a philosophy: strip away framework abstractions to reveal the essential mechanisms, then gradually build complexity.

**micrograd** is the foundation — a scalar-valued autograd engine that decomposes neural networks into individual adds and multiplies. By operating at scalar granularity, it eliminates tensor complexity while maintaining the exact same mathematical principles that power PyTorch. The accompanying YouTube lecture is widely considered the best-ever explanation of backpropagation.

**nanoGPT** and its predecessor **minGPT** demonstrate the Transformer architecture at production quality. nanoGPT prioritizes efficiency, achieving GPT-2 reproduction on a single node. The build-nanogpt companion project starts from an empty file and builds up to the full model.

**minbpe** fills the tokenization gap that most courses skip. It implements BPE from scratch, including a GPT4Tokenizer wrapper that exactly reproduces tiktoken's behavior — but with the crucial addition of training capability.

**llm.c** represents Karpathy's most ambitious educational project: proving that LLM training requires only C and CUDA, no frameworks. At ~3,000 lines of code, it is faster than PyTorch while remaining readable. This project embodies [[concepts/software-2-0]] in a meta sense — showing that the "real" program is the optimization process, not the framework surrounding it.

The **Neural Networks: Zero to Hero** YouTube series weaves these projects together into an 8-lecture curriculum that has become a de facto standard for self-taught ML engineers.

## Concepts Introduced or Discussed

- [[concepts/software-2-0]] — All projects demonstrate the paradigm
- [[concepts/context-engineering]] — minbpe illuminates tokenization's role in context
- [[concepts/fine-tuning]] — nanoGPT supports both training and fine-tuning

## Metadata

- **Author**: Andrej Karpathy
- **Format**: GitHub repositories + YouTube series
- **URL**: https://github.com/karpathy
