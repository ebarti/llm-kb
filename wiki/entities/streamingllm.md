---
title: "StreamingLLM"
type: entity
entity_type: framework
url: "https://github.com/mit-han-lab/streaming-llm"
related: ["[[concepts/attention-sinks]]", "[[concepts/kv-cache]]", "[[concepts/infinite-context]]", "[[concepts/self-attention]]"]
tags: [streaming, attention-sinks, window-attention, infinite-context, MIT]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "MIT HAN Lab framework enabling LLMs to generate over infinite-length sequences by preserving attention sink tokens plus a rolling KV window — no fine-tuning required, validated across Llama-2, MPT, Falcon, and Pythia up to 4M+ tokens with 22.2x speedup."
---

## Overview

StreamingLLM is a framework from MIT's HAN Lab that enables pre-trained LLMs to process and generate text over arbitrarily long sequences without fine-tuning or architectural modifications. It exploits the [[concepts/attention-sinks]] phenomenon: preserving the first few tokens' KV cache alongside a rolling window of recent tokens maintains stable generation quality.

## Key Facts

- **Type**: Framework / research system
- **URL**: https://github.com/mit-han-lab/streaming-llm
- **Notable for**: Discovering attention sinks and enabling infinite-length generation
- **Authors**: Xiao et al. (MIT HAN Lab)
- **Published**: September 2023 (ICLR 2024 accepted)

## How It Works

1. Maintain two-part KV cache: 4 attention sink tokens + rolling recent window
2. Recalculate positional embeddings relative to cache contents
3. Discard intermediate tokens to maintain constant memory
4. No fine-tuning or model modification required

## Performance

- Stable perplexity over 4M+ tokens (vs catastrophic failure with pure window attention)
- Up to 22.2x speedup in decoding latency vs recomputation baselines
- Validated across: Llama-2 (7B-70B), MPT (7B-30B), Falcon (7B-40B), Pythia (2.9B-12B)

## Limitations

- Does not extend the effective context window
- Cannot enhance long-term memory or recall distant information
- Best for streaming applications where recent context dominates (chat, monitoring)

## Mentioned In

- [[sources/streamingllm-attention-sinks]] — discovery paper
- [[concepts/attention-sinks]] — the phenomenon enabling StreamingLLM
- [[concepts/kv-cache]] — the memory challenge being addressed

## External References

- [GitHub Repository](https://github.com/mit-han-lab/streaming-llm)
- [arXiv Paper](https://arxiv.org/abs/2309.17453)
- [HAN Lab Project Page](https://hanlab.mit.edu/projects/streamingllm)
