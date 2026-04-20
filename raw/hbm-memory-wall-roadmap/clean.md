---
title: "Scaling the Memory Wall: The Rise and Roadmap of HBM"
source: "https://newsletter.semianalysis.com/p/scaling-the-memory-wall-the-rise-and-roadmap-of-hbm"
author: "SemiAnalysis"
date_published: 2025-12-15
date_ingested: 2026-04-05
tags: [hbm, memory, memory-wall, sk-hynix, samsung, micron]
type: article
status: raw
discovered_via: search
---

# Scaling the Memory Wall: The Rise and Roadmap of HBM

## The Memory Wall Problem

As model sizes scale from millions to hundreds of billions of parameters, the memory wall — the gap between processor speed and memory throughput — becomes the dominant performance bottleneck. During training, large datasets are repeatedly processed, imposing extremely high demands on memory bandwidth. Insufficient bandwidth causes compute units to remain idle.

A "memory-Parkinson" dynamic exists: neural-network architectures relentlessly grow to occupy whatever HBM becomes available. Each capacity increase immediately encourages larger models, longer context lengths, and expanded KVCache footprints, ensuring memory remains a bottleneck.

## HBM Architecture

HBM combines vertically stacked DRAM chips with ultra-wide data paths. Uses through-silicon vias (TSVs) for 3D stacking, with current configurations reaching 12-13 layers total (8-12 DRAM layers plus logic base die). Compared with conventional DRAM, HBM features a 1024-bit ultra-wide interface providing far exceeding bandwidth.

HBM3E: Reduced peripheral area and introduced all-around power TSVs on the die, achieving 75% lower voltage drop for power delivery.

Placement constraint: HBM needs to be placed directly adjacent to the shoreline of the SOC, limiting it to two chip edges while reserving two edges for off-package I/O.

## HBM Generations on NVIDIA GPUs

- A100: 80 GB HBM2e, ~2 TB/s bandwidth
- H100: 80 GB HBM3, 3.35 TB/s bandwidth
- H200: 141 GB HBM3e, 4.8 TB/s bandwidth
- B200: 192 GB HBM3e, 8.0 TB/s bandwidth
- Rubin Ultra (upcoming): 1024 GB HBM4E

## Manufacturers

SK Hynix: Dominates current HBM supply, especially for NVIDIA. Advanced TSV design and MR-MUF packaging (molded reflow underfill) with higher productivity and better thermal performance.

Micron: Skipped standard HBM3 directly to HBM3E, achieving 30% lower power consumption through advanced TSV networks.

Samsung: Faces significant yield challenges, yields even worse than competitors. Creates paradoxical supply-tightening effect raising overall DRAM pricing.

## Yield Challenges

For an 8-layer stack with 99% per-layer yield, total yield drops to 92%; a 12-layer stack yields 87%. Defects compound across layers.

## AI Workload Demands

Training: Compute-bound, requiring weights, activations, gradients, and optimizer statistics in HBM.

Inference: Bandwidth-bound, especially for reasoning models with expanding context windows. Deep Research can think for tens of minutes, vastly exceeding GPT-4's capacity.

Reinforcement Learning: Drives heavy inference loads for synthetic data generation and LLM-as-judge evaluation, amplifying memory pressure.

## Memory Offload Strategies

KVCache offloading to cheaper DDR or NVMe is standard practice. NVIDIA's Dynamo framework manages multi-tier memory: hot KVs in HBM, infrequent data to DDR, rarely used data on NVMe.

## Future Roadmap

HBM4 & Custom Base Dies: Revolutionary changes with custom base dies designed specifically for HBM. Better integration and optimized power delivery.

Stack Height: JEDEC relaxed standard from 720 to 775 micrometers, accommodating higher layer counts without hybrid bonding.

Hybrid Bonding Hesitation: Manufacturers shifting adoption to HBM4E or later. If 2-layer D2W bonding struggles, scaling to 16+ layers is prohibitively difficult.

## China's Domestic HBM

CXMT plans HBM2 8-high mass production in H1 2025. Huawei operates proprietary HBM production at R&D scale. Export controls have triggered domestic push, as banned HBM is still being reexported to China through intermediaries.

## Supply Chain

TSV capacity and packaging throughput are primary bottlenecks. SK Hynix's Hanmi dominated thermocompression bonder supply until recently. Competing tools from Hanwha and ASMPT now qualifying.
