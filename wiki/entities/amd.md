---
title: "AMD"
type: entity
entity_type: org
url: "https://www.amd.com"
related: ["[[concepts/ai-hardware-landscape]]", "[[concepts/ai-accelerators]]", "[[entities/nvidia]]"]
tags: [amd, gpu, mi300, rocm, ai-hardware]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "NVIDIA's primary GPU competitor: MI300X (192GB HBM3e, 5.2 TB/s, ~2 PFLOPS FP8) at $2.20/FLOPS-hour vs NVIDIA's $2.80; MI350 (June 2025), MI400/MI450 'Helios' with HBM4 (2026); ROCm ecosystem growing but less mature than CUDA."
---

## Overview

Advanced Micro Devices (AMD) is NVIDIA's primary competitor in the AI accelerator market. Its Instinct MI300 series offers competitive performance at lower cost, and the ROCm software ecosystem provides a CUDA-alternative development platform. While AMD holds a much smaller share of the AI accelerator market than [[entities/nvidia]], its aggressive product roadmap and cost advantage make it an increasingly viable alternative.

## Key Facts

- **Type**: Organization (semiconductor company)
- **CEO**: Lisa Su
- **AI product line**: Instinct MI series
- **Software ecosystem**: ROCm, HIP (CUDA portability layer)
- **Notable for**: Price-competitive NVIDIA alternative; MI300X as first serious GPU challenger

## Product Lineup

| Product | Specs | Target |
|---------|-------|--------|
| MI300X | 192GB HBM3e, 5.2 TB/s, ~2 PFLOPS FP8 | Training + inference |
| MI300A | Integrated CPU-GPU (APU) | Cloud deployment |
| MI350 series | Released June 2025 | Next-gen training |
| MI400/MI450 "Helios" | HBM4, 19.6 TB/s bandwidth | 2026 flagship |
| Ryzen AI Embedded | P100/X100 (Jan 2026) | Edge AI |
| XDNA | Integrated AI engine | Edge/laptop AI |

## Cost Advantage

AMD MI300X cloud instances cost approximately $2.20/FLOPS-hour compared to $2.80 for NVIDIA B100 — a 21% discount. This cost advantage, combined with competitive raw performance, makes AMD the default "second source" for organizations seeking to reduce NVIDIA dependency.

## The ROCm Challenge

AMD's ROCm (Radeon Open Compute) platform provides CUDA portability through HIP (Heterogeneous-Interface for Portability), which can translate CUDA code to run on AMD hardware. However, ROCm remains less mature than CUDA, with gaps in kernel optimization, library support, and developer tooling. The software ecosystem is AMD's primary competitive weakness.

## Mentioned In

- [[sources/ai-hardware-accelerators-2026-guide]] — cost comparison and specifications
