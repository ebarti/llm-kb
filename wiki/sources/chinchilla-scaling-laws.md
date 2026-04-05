---
title: "Source: Training Compute-Optimal Large Language Models"
type: source-summary
source: "[[raw/chinchilla-scaling-laws]]"
related: ["[[concepts/scaling-laws]]", "[[entities/chinchilla]]", "[[concepts/transformer-architecture]]"]
last_compiled: 2026-04-05
summary: "DeepMind's Chinchilla paper: 20:1 token-to-parameter optimal ratio, 400+ experiments proving models were undertrained, 70B Chinchilla beating 280B Gopher with 4x more data on same compute budget."
---

## Key Points

- Optimal ratio: ~20 tokens per parameter for compute-optimal training
- 400+ models (70M to 16B params, 5B to 500B tokens) used for estimation
- Three independent estimation approaches all converge on same conclusion
- Models like GPT-3 (175B) were significantly undertrained
- Chinchilla (70B, 1.4T tokens) outperforms Gopher (280B), GPT-3 (175B), Jurassic-1 (178B), Megatron-Turing NLG (530B)
- Loss(N, D) = E + A/N^alpha + B/D^beta — parametric scaling law
- Post-Chinchilla: industry now often overtrains smaller models for inference cost savings

## Detailed Summary

The [[concepts/scaling-laws]] paper from DeepMind fundamentally changed LLM training strategy. By training over 400 language models across a wide range of sizes and data quantities, researchers established that model size and training data should scale equally — for every doubling of parameters, training tokens should also double.

The practical implication was that existing frontier models were massively undertrained. GPT-3 at 175B parameters was trained on only ~300B tokens, far below the Chinchilla-optimal ~3.5T tokens. [[entities/chinchilla]], trained with 70B parameters on 1.4T tokens (same compute as 280B Gopher), uniformly outperformed all larger competitors.

Post-Chinchilla, the industry adjusted: Llama 2 70B was trained on 2T tokens (over-trained relative to Chinchilla-optimal), because smaller models that cost less per inference query justify spending more compute during training.

## Related Concepts

- [[concepts/scaling-laws]] — the theoretical framework
- [[concepts/transformer-architecture]] — the architecture being scaled
- [[concepts/mixture-of-experts]] — alternative scaling approach (more params, same compute)
