---
title: "Continuous Batching"
type: concept
sources: ["[[sources/bentoml-batching-strategies]]", "[[sources/premai-inference-servers-compared]]"]
related: ["[[concepts/llm-inference-optimization]]", "[[concepts/kv-cache]]", "[[concepts/llm-serving-frameworks]]", "[[entities/vllm]]"]
last_compiled: 2026-04-05
summary: "Iteration-level scheduling where completed sequences are immediately replaced with new requests, achieving 23x throughput and 90%+ GPU utilization versus 40% in naive static batching."
---

## Overview

Continuous batching (also called in-flight batching) is the serving technique that replaced static batching as the standard for production LLM inference. Instead of waiting for all sequences in a batch to complete before starting a new batch, continuous batching changes the batch composition at every decoding iteration — completed sequences are immediately replaced with waiting requests.

This eliminates two major sources of waste in static batching: (1) early requests waiting for the batch to fill, and (2) fast-completing requests waiting for the slowest sequence.

## Evolution of Batching

| Strategy | Scheduling | GPU Utilization | Throughput |
|----------|-----------|-----------------|------------|
| Static | Fixed batch, process together | ~40% | 1x baseline |
| Dynamic | Time-window based, launch when full or timeout | ~60% | 2-5x |
| Continuous | Per-iteration, replace completed sequences | 90%+ | **23x** |

## How Continuous Batching Works

Three techniques combine to maximize throughput:

1. **KV Caching**: Avoids recomputing past token representations. Each sequence's [[concepts/kv-cache|KV cache]] is managed independently.
2. **Chunked Prefill**: Variable-length prompts are processed in chunks that fit within memory constraints, preventing long prompts from blocking the batch.
3. **Ragged Batching**: Sequences at different positions in their generation are batched together without padding waste. Dynamic scheduling keeps the GPU fully utilized.

## Performance Impact

- Batch of ~32 requests reduces per-token costs by **~85%** while increasing latency only modestly
- GPUs at **90%+ utilization** vs ~40% in naive setups
- vLLM achieves **23x throughput** improvement with continuous batching enabled

## Framework Support

All major [[concepts/llm-serving-frameworks|inference frameworks]] implement continuous batching:
- [[entities/vllm|vLLM]]: via PagedAttention
- [[entities/sglang|SGLang]]: via RadixAttention + zero-overhead CPU scheduler
- TensorRT-LLM: "in-flight batching"
- LMDeploy: "persistent batching"
- TGI (maintenance mode): basic continuous batching

## Sources
- [[sources/bentoml-batching-strategies]] — evolution from static to continuous batching
- [[sources/premai-inference-servers-compared]] — framework implementations and benchmarks

## Related Concepts
- [[concepts/kv-cache]] — PagedAttention enables memory-efficient continuous batching
- [[concepts/llm-serving-frameworks]] — all modern frameworks implement this
- [[concepts/llm-inference-optimization]] — continuous batching as a throughput technique
