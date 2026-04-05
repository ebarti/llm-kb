---
title: "The Illustrated Transformer"
source: "https://jalammar.github.io/illustrated-transformer/"
author: "Jay Alammar"
date_published: 2018-06-27
date_ingested: 2026-04-05
tags: [transformer, attention, self-attention, multi-head-attention, encoder-decoder, positional-encoding]
type: article
status: raw
discovered_via: search
---

# The Illustrated Transformer

## High-Level Architecture

The Transformer consists of two main components: an encoder stack and a decoder stack. The encoding component is a stack of encoders (the paper stacks six of them on top of each other) with identical decoders matching in number. Each processes sequential input into meaningful representations.

## Encoder Structure

Each encoder contains two sub-layers:

1. **Self-Attention Layer**: Allows the encoder to examine other words in the input sentence when encoding a specific word.
2. **Feed-Forward Network**: The exact same feed-forward network is independently applied to each position.

The architecture enables parallelization because the feed-forward layer does not have dependencies between positions.

## Self-Attention Mechanism

The self-attention calculation involves creating three vectors for each input:

**Query (Q), Key (K), and Value (V) Vectors**: For each word, we create a Query vector, a Key vector, and a Value vector. These vectors are created by multiplying the embedding by three matrices that we trained during the training process.

The dimensionality is 64 (rather than 512 from embeddings) to optimize multi-head attention computation.

**Attention Scoring Process**:
- Calculate dot products between query and key vectors to produce scores
- Divide scores by 8 (sqrt(64)) for stability
- Apply softmax normalization
- Multiply value vectors by softmax scores
- Sum weighted values to produce output

In matrix form: **Attention(Q,K,V) = softmax(QK^T / sqrt(dk)) V**

## Multi-Head Attention

Rather than single attention, the model uses eight attention heads. With multi-headed attention, we maintain separate Q/K/V weight matrices for each head resulting in different Q/K/V matrices.

The eight resulting matrices are concatenated and multiplied by a weight matrix WO to produce the final output. Benefits include:
- Expanding focus ability across different positions
- Providing multiple representation subspaces for the model

## Positional Encoding

To give the model a sense of the order of the words, we add positional encoding vectors whose values follow a specific pattern. These vectors follow sinusoidal functions (sine for the left half, cosine for the right half of the 512-dimensional vectors), enabling the model to handle sequences longer than those in training data.

## Residual Connections and Layer Normalization

Each sub-layer (self-attention, FFN) in each encoder has a residual connection around it, and is followed by a layer-normalization step. This architecture stabilizes training and allows deeper networks.

## Decoder Structure

The decoder contains three sub-layers:

1. **Self-Attention**: In the decoder, the self-attention layer is only allowed to attend to earlier positions in the output sequence. This is done by masking future positions (setting them to -inf) before the softmax step.
2. **Encoder-Decoder Attention**: Uses queries from the decoder but keys/values from the encoder output.
3. **Feed-Forward Network**: Identical to encoder.

## Output Generation

The decoder produces a vector transformed by a final linear layer into logits (one score per vocabulary word). A softmax layer converts these to probabilities, with the highest-probability word selected as output.

## Training Process

Training involves comparing model outputs against expected translations:
- Input embeddings receive positional encodings
- Forward pass through encoder-decoder stack
- Loss calculated using cross-entropy between predicted probability distributions and target one-hot encodings
- Backpropagation adjusts weights

For decoding, two strategies exist: greedy decoding (select highest probability word) or beam search (maintain multiple hypotheses and select the best overall sequence).
