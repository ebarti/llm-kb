---
title: "Training Large Language Models to Reason in a Continuous Latent Space (COCONUT)"
source: "https://arxiv.org/abs/2412.06769"
author: "Shibo Hao, Sainbayar Sukhbaatar, DiJia Su, Xian Li, Zhiting Hu, Jason Weston, Yuandong Tian"
date_published: 2024-12-09
date_ingested: 2026-04-05
tags: [latent-reasoning, test-time-compute, inference-scaling, chain-of-thought, efficiency]
type: paper
status: raw
discovered_via: search
---

# COCONUT: Chain of Continuous Thought

## Core Innovation
COCONUT replaces explicit chain-of-thought token generation with reasoning in continuous latent space. Instead of decoding hidden states into word tokens, it feeds the last hidden state directly back as the next input embedding.

## How It Works
- Utilizes the last hidden state of the LLM as a representation of the reasoning state ("continuous thought").
- Bypasses token sampling, directly feeding hidden states back as next-step representations.
- Hidden states carry richer information than single tokens, increasing bandwidth.
- Enables exploration of more reasoning paths with fewer generation steps.

## Breadth-First Search Capability
A key advantage: continuous thoughts can encode multiple alternative next steps, allowing the model to perform a breadth-first search (BFS) rather than committing prematurely to a single deterministic path as in standard CoT.

## Key Insight
Most word tokens in CoT primarily ensure textual coherence and are not essential for reasoning. By operating in latent space, COCONUT eliminates this overhead.

## Performance
- Superior on logical reasoning tasks requiring substantial backtracking during planning.
- Better trade-off between accuracy and efficiency compared to traditional CoT.
- Fewer thinking tokens needed during inference.

## Current Limitations
- Latent reasoning methods frequently suffer performance degradation compared to explicit reasoning on some tasks.
- Distribution of last-layer hidden states is inconsistent with token embeddings (different means, variances, inter-distribution distances).
- Less interpretable than explicit chain-of-thought.

## Significance
Challenges the assumption that language space is optimal for reasoning. Opens possibilities for more efficient reasoning patterns that don't require verbalizing every step.
