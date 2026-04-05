---
title: "Attention Is All You Need"
type: entity
entity_type: paper
sources: ["[[sources/illustrated-transformer-jalammar]]"]
related: ["[[concepts/transformer-architecture]]", "[[concepts/self-attention]]", "[[concepts/multi-head-attention]]", "[[concepts/positional-encoding]]"]
last_compiled: 2026-04-05
summary: "The 2017 paper by Vaswani et al. introducing the Transformer architecture — the most cited ML paper of the 21st century, replacing RNNs/CNNs with pure attention and enabling all modern LLMs."
---

## Overview

"Attention Is All You Need" was published on June 12, 2017, by Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin at Google Brain/Google Research. It introduced the [[concepts/transformer-architecture]], a sequence-to-sequence model based entirely on [[concepts/self-attention]], dispensing with recurrence and convolution.

## Key Contributions

1. **[[concepts/self-attention]]** as the sole sequence modeling mechanism
2. **[[concepts/multi-head-attention]]** with 8 parallel heads
3. **Sinusoidal [[concepts/positional-encoding]]** for sequence order
4. **Scaled dot-product attention**: Attention(Q,K,V) = softmax(QK^T / sqrt(d_k)) V
5. Encoder-decoder architecture with 6 layers each, ~100M parameters

## Impact

The Transformer now powers every major language model (GPT, Claude, Gemini, Llama), and has expanded beyond text into vision (ViT), audio (Whisper), protein structure (AlphaFold 2), and robotics. It is the most cited machine learning paper of the 21st century.

## Mentioned In

- [[sources/illustrated-transformer-jalammar]] — canonical visual explanation of the paper
- [[sources/raschka-self-attention-coding]] — implementation of the attention mechanisms
- [[sources/unite-ai-bert-gpt-t5-comparison]] — context for the three variant families
