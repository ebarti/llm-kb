---
title: "Google TPUs Explained: Architecture & Performance for Gemini 3"
source: "https://intuitionlabs.ai/articles/google-tpu-architecture-gemini-3"
author: "IntuitionLabs"
date_published: 2025-12-01
date_ingested: 2026-04-05
tags: [google, tpu, gemini, custom-silicon, asic]
type: article
status: raw
discovered_via: search
---

# Google TPU Architecture & Gemini 3

## TPU Generations

TPU v1 (2015-2017): Inference-focused ASIC with 256x256 systolic array, 92 TOPS (8-bit), 28 MB on-chip memory. 15-30x throughput advantage over contemporaneous GPUs with 30-80x superior TOPS/Watt.

TPU v2 (2017): First training-capable generation with four chips per board (~45 TFLOPS bfloat16), 8GB HBM. Pods of 64 boards reached ~11.5 petaflops.

TPU v3 (2018): 128GB HBM per board, 420 TFLOPS per 4-chip board in bfloat16. Over 100 petaflops in 1024-chip pods using 2D torus networking.

TPU v4 (2020): Optical circuit switching (OCS) for dynamic reconfiguration, ~1 petaflops per chip, SparseCores for embedding operations. 2.1x higher perf than TPU v3 and 2.7x better perf/W.

TPU v5e/v5p (2023): Split design — v5e optimized for inference (393 TOPS int8), v5p for training. 256-chip pods reach 100 petaops. 2.5x inference throughput/$ over v4, 1.7x lower latency.

TPU v6e "Trillium" (2024): 4.7x peak per chip vs v5, doubled HBM capacity, 67% energy efficiency gains. Jupiter fabric supports 100,000+ chips at 13 petabit/s bisectional bandwidth.

TPU v7x "Ironwood" (2025): Inference-focused with ~4,614 TFLOPS per chip and 192GB HBM. ~42.5 exaFLOPS per pod.

## Architectural Innovations

- Systolic Arrays: Large matrix multiplication units (v1 had 65,536 MACs)
- High-Bandwidth Memory: Direct attachment for full-speed data feeds
- Optical Circuit Switching: v4+ uses reconfigurable OCS instead of fixed electrical fabrics
- SparseCores: Specialized processors for embedding tables, 5-7x speedup on sparse operations
- Unified Software Stack: XLA compiler, JAX, Pathways frameworks tightly integrated

## Gemini 3 Implementation

Google trained Gemini 3 entirely on TPU v5e and v6e pods without GPU fallback. Supports:
- Trillion-parameter sparse models with selective activation
- 1-million-token context window
- Multimodal processing (text, image, audio, video)
- Embedded reasoning loops ("Deep Think" mode)
- Real-time inference with sub-second latency

## Performance vs. GPUs

TPU v4 vs. Nvidia A100: 1.2-1.7x higher throughput while consuming 53-77% of A100 power. Against Graphcore IPU: 4.3-4.5x higher performance.

Energy Efficiency: TPU v4 deployments use ~3x less electricity and emit ~20x less CO2 than on-premise GPU clusters.

Customer Results: AssemblyAI reported up to 4x greater performance per dollar on v5e; Gridspace achieved 5x training speedups and 6x larger inference scale.
