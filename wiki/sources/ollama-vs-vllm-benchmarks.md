---
title: "Source: Ollama vs. vLLM Performance Benchmarking"
type: source-summary
source: "[[raw/ollama-vs-vllm-benchmarks]]"
related: ["[[entities/ollama]]", "[[entities/vllm]]", "[[concepts/local-llm-inference]]"]
last_compiled: 2026-04-05
summary: "Red Hat benchmarks show vLLM achieves 793 TPS vs Ollama's 41 TPS on A100 with Llama 3.1 8B; Ollama best for single-user dev, vLLM for production."
---

## Key Points
- vLLM peak throughput: 793 TPS vs [[entities/ollama]]'s 41 TPS on identical hardware (A100 40GB)
- vLLM P99 latency: 80ms vs Ollama's 673ms at peak throughput
- vLLM scales linearly with concurrent users; Ollama plateaus at 4 parallel requests (default)
- Even with Ollama tuned to 32 parallel requests, it cannot match vLLM for concurrent workloads
- Testing used Llama-3.1-8B-instruct on NVIDIA A100-PCIE-40GB

## Detailed Summary

Red Hat's August 2025 benchmark provides the most rigorous comparison of the two dominant [[concepts/local-llm-inference]] tools. The test used identical hardware (A100 40GB) and model (Llama 3.1 8B) to isolate the serving framework's impact.

[[entities/vllm]] uses PagedAttention and continuous batching to handle concurrent requests efficiently, achieving nearly 20x the throughput of [[entities/ollama]] under load. Ollama's architecture, built on llama.cpp, is optimized for simplicity and single-user experience rather than concurrent serving.

The key insight: these tools serve fundamentally different use cases. Ollama excels at local development and prototyping where simplicity matters. vLLM is the choice when serving multiple users or running production workloads.

## Related Concepts
- [[concepts/local-llm-inference]] — both tools enable cloud-free LLM deployment
- [[comparisons/ollama-vs-vllm]] — dedicated comparison page
- [[concepts/local-knowledge-base]] — infrastructure choice impacts KB performance
