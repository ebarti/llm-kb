---
title: "Source: Scaling the Memory Wall — The Rise and Roadmap of HBM"
type: source-summary
source: "[[raw/hbm-memory-wall-roadmap]]"
related: ["[[concepts/memory-bandwidth-wall]]", "[[concepts/ai-accelerators]]", "[[entities/nvidia]]"]
tags: [hbm, memory, memory-wall, sk-hynix, samsung, micron]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "SemiAnalysis deep dive on HBM: the memory-Parkinson dynamic where models grow to fill available memory; HBM3e at 8 TB/s (B200); HBM4 with custom base dies; yield challenges (87% for 12-layer stacks); China's domestic HBM efforts."
---

## Key Points

- The memory wall — gap between processor speed and memory throughput — is the dominant AI performance bottleneck
- "Memory-Parkinson" dynamic: models relentlessly grow to consume whatever HBM becomes available
- HBM architecture: 3D-stacked DRAM with TSVs, 1024-bit ultra-wide interface, 8-12 DRAM layers + logic base die
- NVIDIA HBM progression: A100 (80GB, 2 TB/s) → H100 (80GB, 3.35 TB/s) → H200 (141GB, 4.8 TB/s) → B200 (192GB, 8 TB/s) → Rubin Ultra (1024GB HBM4E)
- SK Hynix dominates supply with MR-MUF packaging; Micron skipped to HBM3E with 30% lower power; Samsung has yield problems
- Yield drops: 92% for 8-layer stack (at 99% per-layer), 87% for 12-layer stack
- Inference is bandwidth-bound; training is compute-bound — different bottlenecks for each workload
- KVCache offloading to DDR/NVMe is standard practice; NVIDIA Dynamo manages multi-tier memory
- HBM4 will feature custom base dies designed specifically for HBM — revolutionary integration improvement
- China (CXMT, Huawei) developing domestic HBM to circumvent export controls

## Detailed Summary

This SemiAnalysis article provides the most technically detailed public analysis of the [[concepts/memory-bandwidth-wall]]. The central insight is that the memory wall is not a temporary problem to be solved — it is a permanent feature of AI compute. Every advance in HBM capacity and bandwidth is immediately consumed by larger models, longer context windows, and expanded KVCache.

The supply chain picture is equally important: HBM production is constrained by through-silicon via (TSV) capacity and advanced packaging throughput, not by DRAM wafer production. SK Hynix's dominance creates single-vendor risk for the entire AI industry. Samsung's yield challenges paradoxically benefit the market by tightening supply and supporting prices. China's domestic HBM programs represent a geopolitically significant effort to build an independent AI hardware supply chain.

## Concepts Introduced or Discussed

- [[concepts/memory-bandwidth-wall]] — the fundamental bottleneck of AI compute
- [[concepts/ai-accelerators]] — HBM as a critical component
- [[concepts/ai-hardware-landscape]] — supply chain dynamics

## Metadata

- **Author**: SemiAnalysis
- **Date Published**: 2025-12-15
- **Format**: article (newsletter)
- **URL**: https://newsletter.semianalysis.com/p/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm
