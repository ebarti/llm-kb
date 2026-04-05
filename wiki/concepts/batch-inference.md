---
title: "Batch Inference"
type: concept
sources: ["[[sources/premai-llm-cost-optimization-guide]]", "[[sources/bentoml-batching-strategies]]"]
related: ["[[concepts/llm-cost-optimization]]", "[[concepts/continuous-batching]]", "[[concepts/llm-serving-frameworks]]"]
last_compiled: 2026-04-05
summary: "Processing LLM requests in bulk rather than real-time: API batch endpoints offer 50% price discounts for jobs that can wait hours, while server-side continuous batching achieves 23x throughput improvement."
---

## Overview

Batch inference operates at two levels: **API-level batching** (submitting bulk jobs to providers at discounted rates) and **server-level batching** (scheduling multiple requests together on GPUs for efficiency). Both reduce per-token costs significantly, but through different mechanisms.

## API-Level Batch Endpoints

Major providers offer batch APIs with significant discounts for non-real-time workloads:

- **OpenAI Batch API**: 50% cost reduction for jobs that can wait up to 24 hours
- **Anthropic Batch API**: Halves pricing (e.g., Claude Sonnet from $3/$15 to $1.50/$7.50 per MTok)

Ideal for: bulk content generation, dataset processing, offline analysis, [[concepts/wiki-compilation|wiki compilation]] tasks

## Server-Level Batching

When self-hosting, [[concepts/continuous-batching|continuous batching]] at the serving layer achieves dramatic efficiency gains:
- Batch of ~32 requests reduces per-token cost by **~85%** with modest latency increase
- GPU utilization: **90%+** vs ~40% in naive single-request serving
- All major [[concepts/llm-serving-frameworks|frameworks]] (vLLM, SGLang, TensorRT-LLM) implement this

## Relevance to LLM-KB System

The [[concepts/llm-knowledge-base|LLM-KB]] system has natural batch opportunities:
- **COMPILE operations**: Processing multiple raw files into wiki articles can be batched
- **LINT operations**: Scanning many articles for issues can use batch APIs
- **RESEARCH ingestion**: Fetching and summarizing multiple sources sequentially is batchable
- Real-time Q&A is the main operation that requires synchronous inference

## Sources
- [[sources/premai-llm-cost-optimization-guide]] — batch API pricing and discounts
- [[sources/bentoml-batching-strategies]] — server-level batching strategies

## Related Concepts
- [[concepts/llm-cost-optimization]] — batching as a cost lever
- [[concepts/continuous-batching]] — server-level iteration scheduling
- [[concepts/llm-serving-frameworks]] — frameworks implementing batch optimization
