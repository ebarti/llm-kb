---
title: "Static, Dynamic and Continuous Batching — LLM Inference Handbook"
source: "https://bentoml.com/llm/inference-optimization/static-dynamic-continuous-batching"
author: "BentoML"
date_published: 2025-06-01
date_ingested: 2026-04-05
tags: [batching, continuous-batching, inference-optimization, throughput]
type: article
status: raw
discovered_via: search
---

# Static, Dynamic and Continuous Batching

## Static Batching
Server waits for a fixed number of requests before processing. Limitations:
- Early requests forced to wait for batch to fill
- All requests must wait until slowest one finishes
- Wasted compute resources and increased latency

## Dynamic Batching
Sets a time window and processes whatever requests arrive in that frame. Launches immediately if batch size limits reached first. Better throughput-latency balance than static, but doesn't achieve full GPU efficiency.

## Continuous Batching (In-Flight Batching)
Each sequence in a batch finishes independently and is immediately replaced with a new one. The batch composition changes dynamically at each decoding iteration. Key benefits:
- Maximizes GPU occupancy
- Eliminates idle time
- Combines KV caching, chunked prefill, and ragged batching

## Performance
- vLLM achieves 23x LLM inference throughput with continuous batching
- Batch of ~32 requests reduces per-token costs by ~85% with modest latency increase
- GPUs at 90%+ utilization vs ~40% in naive setups

## Framework Support
Major frameworks supporting continuous batching:
- vLLM
- SGLang
- TensorRT-LLM (in-flight batching)
- LMDeploy (persistent batching)
- Hugging Face TGI
