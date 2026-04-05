---
title: "Mixture of Experts (MoE)"
type: concept
sources: ["[[sources/huggingface-mixture-of-experts]]", "[[sources/moe-models-comparison-2025]]", "[[sources/vlms-2025-huggingface]]", "[[sources/bentoml-open-source-llms-2026]]", "[[sources/meta-llama-4-multimodal]]", "[[sources/deepseek-revolution-2026]]"]
related: ["[[concepts/transformer-architecture]]", "[[concepts/scaling-laws]]", "[[concepts/sparse-attention]]", "[[concepts/open-source-llms]]", "[[concepts/quantization]]", "[[entities/deepseek]]", "[[entities/meta-llama]]", "[[entities/qwen]]", "[[entities/switch-transformer]]", "[[entities/mixtral]]"]
last_compiled: 2026-04-05
summary: "Sparse transformer architecture replacing dense FFN layers with multiple expert networks + learned router — scaling model capacity without proportional inference cost. By 2025, the default for all frontier LLMs."
---

## Overview

Mixture of Experts (MoE) is a neural network architecture where each input token is processed by only a subset of the model's total parameters. A router network selects which "expert" sub-networks to activate for each token, typically 1-2 experts out of many. This means a model with 400 billion total parameters might activate only 17 billion per token, achieving the quality of a very large model at the inference cost of a much smaller one.

By 2026, MoE has become the dominant architecture for frontier [[concepts/open-source-llms]]. Every S-tier open model uses it.

## Key Ideas

### Architecture Deep Dive

MoE replaces the dense FFN in a [[concepts/transformer-architecture]] layer with N expert FFNs plus a gating network. The routing formula: y = sum_i(G(x)_i * E_i(x)) where G(x) = Softmax(x * W_g). Only top-k experts with highest gate values are computed.

**Two Routing Strategies (2025):**
- **Top-k Only** (Qwen3, GPT-OSS): Tokens route exclusively to selected experts. Maximizes specialization.
- **Shared + Routed** (DeepSeek, Llama 4): One shared expert processes every token for stable generalization, plus routed experts for specialization.

**Load Balancing** is the central engineering challenge. Tokens cluster to popular experts. Solutions: auxiliary loss (uniform utilization), expert capacity limits (CF = 1.0-1.25), and Router Z-Loss (penalizes large gate logits, more effective than aux loss alone).

**Training**: 4x pretraining speedup vs dense equivalents. MoEs benefit MORE from instruction tuning than dense models (breakthrough finding). Overfit more on reasoning tasks without instruction tuning.

**Expert Specialization**: Encoder experts specialize (punctuation, proper nouns); decoder experts show less clear patterns.

### How MoE Works

1. Input token arrives at a "gate" or "router" layer
2. Router assigns the token to the top-K experts (usually 1-2)
3. Only selected experts compute activations for that token
4. Outputs from selected experts are combined (usually weighted sum)
5. Other experts remain idle, saving compute

### MoE in Frontier Models (2026)

| Model | Total Params | Active Params | Experts | Efficiency Ratio |
|-------|-------------|---------------|---------|-----------------|
| [[entities/meta-llama]] 4 Scout | 109B | 17B | 16 | 6.4x |
| [[entities/meta-llama]] 4 Maverick | 400B | 17B | 128 | 23.5x |
| [[entities/deepseek]] V3.2 | 671B | ~37B | MoE | ~18x |
| [[entities/qwen]] 3.5-397B | 397B | 17B | MoE | 23.4x |
| Kimi-K2.5 | 1T | 32B | MoE | 31.3x |
| GLM-5 | 744B | 40B | MoE | 18.6x |
| Mistral Large 3 | 675B | 41B | MoE | 16.5x |

### Advantages for Local Inference

MoE is particularly beneficial for [[concepts/local-llm-inference]] because:
- **Reduced compute**: Only active parameters need computation
- **Memory bandwidth**: The bottleneck shifts from compute to memory, which Apple Silicon's unified memory handles well
- **Quantization synergy**: With [[concepts/quantization]], a 400B MoE model might fit in 50-60GB at Q4

### DeepSeek Sparse Attention (DSA)

[[entities/deepseek]] introduced Sparse Attention as a complementary technique, reducing inference costs by approximately 70% compared to standard attention. This innovation, combined with MoE, makes frontier models accessible to a much wider range of hardware.

### Tradeoffs

- **Memory**: MoE models require loading all parameters into memory, even though only a fraction activates. A 400B MoE model needs similar storage to a 400B dense model.
- **Routing overhead**: The gating mechanism adds latency per token
- **Expert utilization**: Poor routing can leave some experts under-utilized, wasting capacity

## Sources
- [[sources/huggingface-mixture-of-experts]] — comprehensive architecture guide (routing, load balancing, training)
- [[sources/moe-models-comparison-2025]] — 2025 frontier model comparison with specs
- [[sources/vlms-2025-huggingface]] — MoE in multimodal/VLM context
- [[sources/bentoml-open-source-llms-2026]] — MoE dominance in 2026 model landscape
- [[sources/meta-llama-4-multimodal]] — Llama 4's first-time MoE adoption
- [[sources/deepseek-revolution-2026]] — DeepSeek's MoE + Sparse Attention innovations

## Related Concepts
- [[concepts/transformer-architecture]] — the base architecture MoE extends
- [[concepts/scaling-laws]] — MoE as scaling without proportional compute
- [[concepts/sparse-attention]] — related sparsity concept in attention
- [[concepts/open-source-llms]] — MoE as the enabling architecture
- [[concepts/quantization]] — combined with MoE for local deployment
- [[concepts/local-llm-inference]] — MoE reduces compute requirements
