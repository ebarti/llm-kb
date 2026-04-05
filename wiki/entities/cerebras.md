---
title: "Cerebras Systems"
type: entity
entity_type: org
url: "https://www.cerebras.ai"
related: ["[[concepts/wafer-scale-computing]]", "[[concepts/ai-accelerators]]", "[[concepts/ai-hardware-landscape]]", "[[entities/nvidia]]"]
tags: [cerebras, wafer-scale, wse, asic, ai-hardware]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Creator of the world's largest chip (WSE-3: 4T transistors, 900K cores, 46,225 mm²); $10B+ OpenAI deal; IPO targeting $22B in Q2 2026; AWS partnership for cloud access; deployed at Oak Ridge, Argonne, DARPA."
---

## Overview

Cerebras Systems is a Silicon Valley AI hardware company that designs the world's largest processor: the Wafer Scale Engine (WSE). Rather than cutting a silicon wafer into hundreds of individual chips, Cerebras uses the entire 300mm wafer as a single monolithic processor, a radical approach to eliminating inter-chip communication bottlenecks. See [[concepts/wafer-scale-computing]].

## Key Facts

- **Type**: Organization (AI chip startup)
- **Founded**: 2016
- **HQ**: Sunnyvale, California
- **Flagship product**: WSE-3 (Wafer Scale Engine 3)
- **Valuation**: Targeting $22B at IPO (Q2 2026)
- **Latest funding**: $1.1B (September 2025) at $8.1B valuation
- **Key investors**: Fidelity, Atreides, SoftBank, 1789 Capital

## WSE-3 Specifications

| Specification | Value |
|--------------|-------|
| Die size | 46,225 mm² (entire 300mm wafer) |
| Transistors | 4 trillion |
| AI cores | 900,000 |
| On-chip SRAM | 44 GB |
| Process node | TSMC 3nm |
| Interconnect | SwarmX mesh |
| External memory | MemoryX clusters |
| Power | 20-50 kW per system |

## Key Deals and Deployments

- **OpenAI**: $10B+ contract for 750 MW of computing power through 2028 (January 2026)
- **AWS**: Multi-year partnership bringing WSE-3 to cloud; developing "disaggregated architecture" for inference
- **DARPA MAPLE**: $45M contract integrating WSE-3 with optical interconnects for battlefield simulation
- **Stargate UAE**: Infrastructure supplier for 5GW AI campus in Abu Dhabi
- **National Labs**: Deployed at Oak Ridge and Argonne for exascale AI research
- **Condor Galaxy 3**: Supercomputer for large-scale model training

## Performance Claims

- 210x speedup over NVIDIA H100 on specific subsurface simulations
- Single CS-2 trains GPT-3 (175B) in 24 hours vs weeks on 1,024 GPUs
- 7,000x bandwidth advantage over H100 for on-chip data access
- Llama-4 models run up to 21x faster than equivalent NVIDIA clusters

## Mentioned In

- [[sources/cerebras-vs-sambanova-vs-groq-chips]] — detailed technical comparison
- [[sources/ai-inference-accelerators-compared]] — inference benchmarks
- [[sources/ai-infrastructure-investment-2026]] — OpenAI deal and IPO
