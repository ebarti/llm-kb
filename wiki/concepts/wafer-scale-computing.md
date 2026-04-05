---
title: "Wafer-Scale Computing"
type: concept
sources: ["[[sources/cerebras-vs-sambanova-vs-groq-chips]]", "[[sources/ai-inference-accelerators-compared]]"]
related: ["[[entities/cerebras]]", "[[concepts/ai-accelerators]]", "[[concepts/memory-bandwidth-wall]]", "[[concepts/ai-hardware-landscape]]"]
tags: [wafer-scale, cerebras, architecture, ai-hardware]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Cerebras's radical approach: using an entire 300mm silicon wafer as a single processor (46,225 mm², 4 trillion transistors, 900,000 cores) — eliminating inter-chip communication and the memory bandwidth wall for models that fit in 44GB on-chip SRAM."
---

## Overview

Wafer-scale computing is a radical processor design approach pioneered by [[entities/cerebras]] that uses an entire silicon wafer — normally diced into hundreds of individual chips — as a single monolithic processor. The Cerebras WSE-3 (Wafer Scale Engine 3) measures 46,225 mm² and contains 4 trillion transistors and 900,000 AI-optimized cores, making it the largest chip ever manufactured.

The key insight is eliminating the inter-chip communication bottleneck. In conventional GPU clusters, data must traverse PCIe buses, NVLink connections, or InfiniBand networks between separate chips. In a wafer-scale processor, all cores communicate via an on-die mesh interconnect (SwarmX) with bandwidth and latency orders of magnitude better than any off-chip connection.

## Key Ideas

### Architecture

The WSE-3 is manufactured on TSMC's 3nm process. It contains:
- **900,000 AI-optimized cores** with local memory
- **44 GB of on-chip SRAM** — no HBM required for models that fit
- **SwarmX mesh interconnect** for intra-wafer communication
- **MemoryX external memory clusters** for models exceeding on-chip capacity
- **7,000x bandwidth advantage** over H100 for on-chip data access

The decoupled memory architecture is key: model parameters can live in external MemoryX clusters while compute elements on the wafer handle processing, enabling support for models larger than on-chip SRAM.

### Advantages

1. **Eliminated memory wall**: For models fitting in 44GB SRAM, the [[concepts/memory-bandwidth-wall]] simply does not exist — all data is on-chip
2. **No inter-chip communication overhead**: What requires NVLink or InfiniBand in GPU clusters happens at on-die speed
3. **Massive parallelism**: 900,000 cores executing simultaneously
4. **Claims**: 210x speedup over H100 on specific simulations; single-system GPT-3 (175B) training in 24 hours vs weeks on 1,024 GPUs

### Challenges

1. **Manufacturing yield**: A single defect on a 46,225 mm² wafer is far more impactful than on a ~800 mm² GPU die. Cerebras uses redundant cores and dynamic routing to work around defects.
2. **Exotic cooling**: 20-50 kW per system requires specialized liquid cooling infrastructure
3. **Limited ecosystem**: Custom software stack (CSP) rather than CUDA; smaller developer community
4. **Cost**: Each CS-2/CS-3 system is significantly more expensive than individual GPU nodes
5. **Scalability**: Multi-system scaling is more complex than GPU cluster scaling

### Business Position (2026)

- OpenAI signed $10B+ deal for 750 MW of compute through 2028
- IPO targeting $22B valuation in Q2 2026
- AWS partnership to bring WSE-3 to cloud (disaggregated inference architecture)
- Deployed at Oak Ridge and Argonne National Labs
- DARPA MAPLE Project: $45M contract for battlefield simulation

## How It Connects

Wafer-scale computing represents the most radical attack on the [[concepts/memory-bandwidth-wall]] — rather than making memory faster, it moves computation to where the data already lives. It occupies a unique niche in the [[concepts/ai-hardware-landscape]], complementing rather than replacing [[concepts/ai-accelerators]] like GPUs for workloads that benefit from its architecture.

## Sources

- [[sources/cerebras-vs-sambanova-vs-groq-chips]] — technical specifications and comparison
- [[sources/ai-inference-accelerators-compared]] — inference performance data
