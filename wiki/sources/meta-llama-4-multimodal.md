---
title: "Source: Llama 4 — Natively Multimodal AI"
type: source-summary
source: "[[raw/meta-llama-4-multimodal]]"
related: ["[[entities/meta-llama]]", "[[concepts/mixture-of-experts]]", "[[concepts/open-source-llms]]"]
last_compiled: 2026-04-05
summary: "Meta's Llama 4 introduces MoE to the Llama line: Scout (109B, 10M context), Maverick (400B, multimodal), Behemoth (2T, teacher model) — trained on 30T+ tokens across 200 languages."
---

## Key Points
- First Llama family to use [[concepts/mixture-of-experts]] architecture
- Scout: 17B active / 109B total, fits single H100, 10M token context window (longest of any open model)
- Maverick: 17B active / 400B total, natively multimodal (image+text), ELO 1417 on LMArena
- Behemoth: 288B active / ~2T total, outperforms GPT-4.5 and Claude Sonnet 3.7 on STEM
- iRoPE architecture: interleaved attention without positional embeddings for length generalization
- Trained on 30T+ tokens, 200 languages (100+ with 1B+ tokens)
- Early fusion: text and vision tokens in unified backbone

## Detailed Summary

Llama 4, released April 2025, marked [[entities/meta-llama]]'s transition to MoE architecture and native multimodality. The Scout variant's 10M token context window represents a breakthrough for open models — enabling entire codebases or book-length documents in a single prompt.

The training pipeline evolved to use lightweight SFT, online RL, and lightweight DPO, with aggressive data filtering removing 50%+ of easy examples. FP8 precision training achieved 390 TFLOPs/GPU utilization.

Both Scout and Maverick are available on Hugging Face and llama.com under Meta's community license.

## Related Concepts
- [[concepts/open-source-llms]] — Llama 4 as Meta's flagship contribution
- [[concepts/mixture-of-experts]] — first Llama to use MoE
- [[concepts/local-llm-inference]] — Scout fits single GPU with quantization
