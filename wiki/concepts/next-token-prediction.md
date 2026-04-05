---
title: "Next-Token Prediction"
type: concept
sources: ["[[sources/mlops-pretraining-pipeline]]", "[[sources/analyticsvidhya-llm-pretraining-guide]]"]
related: ["[[concepts/llm-pretraining]]", "[[concepts/tokenization]]"]
last_compiled: 2026-04-05
summary: "The self-supervised training objective for autoregressive LLMs: predict the next token given all preceding tokens, optimized via cross-entropy loss. Requires no labeled data — the next token in the sequence is the label."
---

## Overview

Next-token prediction (also called causal language modeling, CLM) is the training objective that powers all modern autoregressive LLMs. Given a sequence of tokens [t1, t2, ..., tn], the model learns to predict tn+1 by outputting a probability distribution over the entire vocabulary at each position.

## How It Works

1. **Input**: A sequence of tokens from the training corpus
2. **Forward pass**: The model processes the sequence through transformer layers
3. **Output**: At each position i, a probability distribution P(ti+1 | t1, ..., ti) over the vocabulary
4. **Loss**: Cross-entropy between predicted distribution and actual next token
5. **Backpropagation**: Gradients flow back to update all model parameters
6. **Self-supervised**: No external labels needed — the next token in the sequence IS the label

## Why It Works

Despite its simplicity, next-token prediction forces the model to learn:
- **Grammar and syntax**: To predict the next word correctly
- **Semantics**: To understand meaning and context
- **World knowledge**: Facts appear in training text and must be modeled
- **Reasoning patterns**: Logical sequences in text require internal reasoning
- **Code**: Programming patterns follow predictable structures

The model becomes a "compressed representation" of the training data's statistical patterns.

## Variants

- **Masked Language Modeling (MLM)**: BERT-style bidirectional prediction of masked tokens. Not used for generative models.
- **Reinforcement Pretraining (RPT)**: Microsoft's 2025 approach treating next-token prediction as sequential decision-making with reward signals
- **Instruction-Augmented Pretraining**: Mixing instruction-response pairs into the pretraining data

## Sources

- [[sources/mlops-pretraining-pipeline]] — training objectives and CLM
- [[sources/analyticsvidhya-llm-pretraining-guide]] — training mechanics

## Related Concepts

- [[concepts/llm-pretraining]] — the process using this objective
- [[concepts/tokenization]] — converting text to tokens for prediction
