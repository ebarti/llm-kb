---
title: "Transformer Architecture"
type: concept
sources: ["[[sources/illustrated-transformer-jalammar]]", "[[sources/raschka-self-attention-coding]]", "[[sources/unite-ai-bert-gpt-t5-comparison]]", "[[sources/chinchilla-scaling-laws]]", "[[sources/flashattention-3-paper]]"]
related: ["[[concepts/self-attention]]", "[[concepts/multi-head-attention]]", "[[concepts/positional-encoding]]", "[[concepts/mixture-of-experts]]", "[[concepts/state-space-models]]", "[[concepts/scaling-laws]]", "[[concepts/kv-cache]]"]
last_compiled: 2026-04-05
summary: "The foundational neural network architecture based entirely on attention mechanisms, introduced in 'Attention Is All You Need' (2017), now powering virtually all frontier LLMs, vision models, and multimodal systems."
---

## Overview

The Transformer is the dominant neural network architecture for sequence modeling, introduced by Vaswani et al. in the [[entities/attention-is-all-you-need]] paper (2017). It replaced recurrence and convolution with a single mechanism — [[concepts/self-attention]] — enabling massive parallelization and becoming the foundation for GPT, BERT, T5, Claude, Gemini, and virtually every frontier AI model.

The original architecture is an encoder-decoder model with 6 layers each, approximately 100M parameters, designed for machine translation. Since then, three major variants have emerged:

- **Encoder-only** ([[entities/bert]]): bidirectional attention for understanding tasks
- **Decoder-only** ([[entities/gpt]]): causal (left-to-right) attention for generation — now the dominant paradigm
- **Encoder-decoder** ([[entities/t5]]): full architecture for sequence-to-sequence tasks

## Architecture Components

### Encoder

Each encoder layer contains two sub-layers:
1. **[[concepts/multi-head-attention]]**: Each position attends to all other positions in the sequence
2. **Position-wise Feed-Forward Network (FFN)**: Two linear layers with ReLU activation, applied identically to each position

Both sub-layers use **residual connections** (x + sublayer(x)) and **layer normalization** for training stability.

### Decoder

Each decoder layer contains three sub-layers:
1. **Masked [[concepts/self-attention]]**: Attends only to previous positions via [[concepts/causal-attention]] (future positions masked with -inf)
2. **Encoder-Decoder [[concepts/cross-attention]]**: Queries from decoder, keys/values from encoder output
3. **Position-wise FFN**: Identical to encoder

### Input Processing

- **Token embeddings**: Convert tokens to d_model-dimensional vectors (typically 512-4096)
- **[[concepts/positional-encoding]]**: Inject sequence order (originally sinusoidal; modern models use [[concepts/rotary-position-embeddings]])
- **Output projection**: Linear layer + softmax over vocabulary for next-token prediction

### The Attention Formula

The core computation is scaled dot-product attention:

**Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V**

Where Q, K, V are query, key, and value matrices projected from inputs. The sqrt(d_k) scaling prevents dot products from growing too large in high dimensions.

## Architectural Evolution

### Phase 1: Original Transformer (2017)
- Encoder-decoder for translation
- Sinusoidal positional encoding
- 6 layers, 512-dim, 8 heads, ~100M parameters

### Phase 2: Variant Explosion (2018-2020)
- [[entities/bert]] (2018): Encoder-only, bidirectional MLM pre-training
- [[entities/gpt]] (2018-2020): Decoder-only, causal LM, scaling to 175B (GPT-3)
- [[entities/t5]] (2019): Text-to-text framework, encoder-decoder

### Phase 3: Scaling Era (2020-2023)
- [[concepts/scaling-laws]]: Kaplan (2020) and [[entities/chinchilla]] (2022) establish compute-optimal training
- Models scale to hundreds of billions of parameters
- [[concepts/flash-attention]] (2022) makes training tractable at scale

### Phase 4: Efficiency & Alternatives (2023-present)
- [[concepts/mixture-of-experts]]: Scale parameters without proportional compute (Mixtral, DeepSeek, Llama 4)
- [[concepts/state-space-models]] / [[concepts/mamba]]: Linear-complexity alternatives to attention
- [[concepts/grouped-query-attention]]: Reduce KV cache memory
- [[concepts/rotary-position-embeddings]]: Replace sinusoidal/learned encodings
- [[concepts/speculative-decoding]]: Parallelize autoregressive generation
- [[concepts/multimodal-transformers]]: Extend to vision, audio, video, robotics

## Why Transformers Won

1. **Parallelization**: Unlike RNNs, all positions compute simultaneously during training
2. **Long-range dependencies**: Attention connects any two positions in O(1) operations
3. **Scalability**: Performance improves predictably with scale ([[concepts/scaling-laws]])
4. **Hardware fit**: Matrix multiplications map efficiently to GPUs/TPUs
5. **Transfer learning**: Pre-trained transformers fine-tune effectively to downstream tasks

## Current Limitations

- **Quadratic attention complexity**: O(N^2) in sequence length, addressed by [[concepts/flash-attention]], [[concepts/sparse-attention]], and [[concepts/state-space-models]]
- **KV cache memory**: Grows linearly with context length during inference ([[concepts/kv-cache]])
- **Autoregressive bottleneck**: Sequential token generation, addressed by [[concepts/speculative-decoding]]
- **Position extrapolation**: Difficulty generalizing to longer sequences than training, partially addressed by [[concepts/rotary-position-embeddings]]

## Sources

- [[sources/illustrated-transformer-jalammar]] — canonical visual walkthrough of the architecture
- [[sources/raschka-self-attention-coding]] — code-level implementation of attention variants
- [[sources/unite-ai-bert-gpt-t5-comparison]] — comparison of three transformer variant families
- [[sources/chinchilla-scaling-laws]] — compute-optimal scaling for transformers
- [[sources/flashattention-3-paper]] — systems-level optimization enabling scale

## Related Concepts

- [[concepts/self-attention]] — the core mechanism
- [[concepts/multi-head-attention]] — parallel attention for diverse representations
- [[concepts/mixture-of-experts]] — sparse scaling of the FFN component
- [[concepts/state-space-models]] — the primary architectural alternative
- [[concepts/scaling-laws]] — governing how transformers improve with scale
- [[concepts/kv-cache]] — the inference memory bottleneck
- [[concepts/flash-attention]] — the key systems optimization
