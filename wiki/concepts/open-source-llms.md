---
title: "Open-Source LLMs"
type: concept
sources: ["[[sources/bentoml-open-source-llms-2026]]", "[[sources/deepseek-revolution-2026]]", "[[sources/meta-llama-4-multimodal]]", "[[sources/open-source-vs-closed-llms-enterprise]]", "[[sources/coding-models-comparison-2026]]"]
related: ["[[concepts/mixture-of-experts]]", "[[concepts/local-llm-inference]]", "[[concepts/small-language-models]]", "[[concepts/quantization]]", "[[concepts/open-source-coding-models]]"]
last_compiled: 2026-04-05
summary: "Open-weight LLMs from DeepSeek, Qwen, Meta, Mistral, and others have closed the gap with proprietary models to ~3 months, using MoE architectures and MIT/Apache licensing."
---

## Overview

Open-source large language models are LLMs whose weights (and sometimes training code and data) are publicly available for download, modification, and deployment. By early 2026, open-source models have effectively closed the performance gap with proprietary alternatives, trailing state-of-the-art closed models by approximately three months on average.

The landscape is dominated by [[concepts/mixture-of-experts]] architectures that activate only a fraction of total parameters per token, achieving frontier performance with manageable inference costs. Five independent model families — [[entities/deepseek]], [[entities/qwen]], Kimi, GLM, and Mistral — simultaneously reached frontier quality in 2025-2026, making the open-source advantage structural rather than a one-off event.

## Key Ideas

### The 2025-2026 Open-Source Explosion

The "DeepSeek moment" of January 2025 — when DeepSeek R1 demonstrated ChatGPT-level reasoning at dramatically lower training costs — catalyzed a wave of releases. Chinese organizations alone released 1,500+ open LLMs by mid-2025. By 2026, the ecosystem includes:

**S-Tier General Models (2026)**:
| Model | Total Params | Active Params | Architecture | License |
|-------|-------------|---------------|--------------|---------|
| [[entities/qwen]] 3.5-397B | 397B | 17B | MoE | Open |
| [[entities/deepseek]] V3.2 | 671B | ~37B | MoE | MIT |
| GLM-5 | 744B | 40B | MoE | Open |
| Kimi-K2.5 | 1T | 32B | MoE | Modified MIT |
| MiniMax-M2.5 | — | — | — | Modified MIT |
| gpt-oss-120b (OpenAI) | 117B | — | MoE | Apache 2.0 |

**Flagship Open Models**:
- [[entities/meta-llama]] 4 Scout: 109B total, 17B active, 10M token context window
- [[entities/meta-llama]] 4 Maverick: 400B total, 17B active, natively multimodal
- Mistral Large 3: 675B total, 41B active, Apache 2.0

### Licensing Landscape

The most permissive licenses (MIT, Apache 2.0) allow unrestricted commercial use. Some models use modified licenses requiring attribution above certain revenue thresholds. Key consideration: Codestral uses a non-production license restricting commercial deployment.

### Performance Parity

The benchmark gap between open and closed models has narrowed to:
- **Zero** on knowledge benchmarks (MMLU, etc.)
- **Single digits** on most reasoning tasks
- **Remaining gap** in multimodal (image/video) and extreme long-context reliability

### Cost Advantage

Open-source models offer ~10x cost reduction per token when self-hosted vs. cloud API pricing:
- Llama-3-70B: ~$0.60/M input tokens
- GPT-4: ~$10/M input tokens

At high volume, self-hosting saves 5-10x. However, realistic minimal production deployment costs $125K-$190K/year including staff, infrastructure, and operations.

## Relevance to This Knowledge Base

This KB system currently runs on the Claude API. The open-source LLM landscape creates a viable path to [[concepts/local-knowledge-base]] operation:
- Models like DeepSeek V3.2 or Qwen 3.5 could handle wiki compilation and Q&A
- [[concepts/small-language-models]] (Phi-4, Qwen 3 4B) could handle simpler KB tasks on consumer hardware
- The OpenAI-compatible API standard (via [[entities/ollama]] or [[entities/vllm]]) means minimal code changes to switch

The tradeoff: reduced reasoning quality for complex synthesis tasks, but complete privacy, offline capability, and zero per-token cost.

## Sources
- [[sources/bentoml-open-source-llms-2026]] — comprehensive 2026 model rankings
- [[sources/deepseek-revolution-2026]] — DeepSeek's catalytic impact on the ecosystem
- [[sources/meta-llama-4-multimodal]] — Llama 4's MoE and multimodal innovations
- [[sources/open-source-vs-closed-llms-enterprise]] — enterprise adoption and cost analysis
- [[sources/coding-models-comparison-2026]] — coding-specific open models

## Related Concepts
- [[concepts/mixture-of-experts]] — dominant architecture enabling frontier open models
- [[concepts/local-llm-inference]] — how to actually run these models
- [[concepts/small-language-models]] — lightweight variants for edge/consumer deployment
- [[concepts/quantization]] — making large models fit on smaller hardware
- [[concepts/open-source-coding-models]] — coding-specialized subset
- [[comparisons/open-source-vs-closed-llms]] — detailed tradeoff analysis
