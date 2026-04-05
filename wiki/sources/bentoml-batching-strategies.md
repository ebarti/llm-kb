---
title: "Source: Static, Dynamic and Continuous Batching"
type: source-summary
source: "[[raw/bentoml-batching-strategies]]"
related: ["[[concepts/continuous-batching]]", "[[concepts/llm-inference-optimization]]", "[[concepts/llm-serving-frameworks]]"]
last_compiled: 2026-04-05
summary: "BentoML handbook: evolution from static to continuous batching, achieving 23x throughput and 90%+ GPU utilization via iteration-level scheduling in vLLM, SGLang, and TensorRT-LLM."
---

## Key Points
- Static batching: simplest but wasteful — all requests wait for slowest one
- Dynamic batching: time-window based, better but not optimal
- Continuous batching: iteration-level scheduling, sequences replaced as they complete
- vLLM achieves 23x throughput improvement with continuous batching
- Batch of ~32 requests reduces per-token cost by ~85%
- GPU utilization: 90%+ with continuous batching vs ~40% in naive setups

## Detailed Summary

BentoML's handbook traces the evolution of [[concepts/continuous-batching|batching strategies]] for LLM serving. Static batching waits for a fixed number of requests, forcing early arrivals to wait and wasting compute when requests have different lengths. Dynamic batching improves by using time windows, but still processes entire batches together.

[[concepts/continuous-batching|Continuous batching]] (also called in-flight batching) represents the breakthrough: the batch composition changes at every decoding iteration. When a sequence finishes, a new request immediately takes its slot, maximizing GPU occupancy. This combines three key techniques: [[concepts/kv-cache|KV caching]], chunked prefill for variable-length prompts, and ragged batching to eliminate padding waste.

All major [[concepts/llm-serving-frameworks|serving frameworks]] now support continuous batching: [[entities/vllm|vLLM]], [[entities/sglang|SGLang]], TensorRT-LLM, LMDeploy, and TGI.

## Related Concepts
- [[concepts/continuous-batching]] — the core technique
- [[concepts/kv-cache]] — enabling infrastructure for continuous batching
- [[concepts/llm-serving-frameworks]] — frameworks implementing this technique
