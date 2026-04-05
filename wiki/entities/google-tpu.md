---
title: "Google TPU"
type: entity
entity_type: tool
url: "https://cloud.google.com/tpu"
related: ["[[concepts/custom-silicon]]", "[[concepts/ai-accelerators]]", "[[concepts/ai-hardware-landscape]]", "[[entities/nvidia]]"]
tags: [google, tpu, asic, custom-silicon, gemini]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Google's custom AI accelerator: 7 generations (2015-2025); Ironwood v7 at 4,614 TFLOPS and 42.5 exaFLOPS per pod; Gemini 3 trained entirely on TPUs; optical circuit switching (v4+); ~3x energy efficiency over GPUs."
---

## Overview

The Tensor Processing Unit (TPU) is Google's custom-designed AI accelerator, representing the most mature custom silicon program in the industry. Spanning seven generations from 2015 to 2025, the TPU program demonstrates the power of hardware-software co-design: each generation is optimized in tandem with Google's ML frameworks (JAX, XLA, Pathways), enabling optimizations impossible on general-purpose hardware.

Google trained Gemini 3 entirely on TPU v5e and v6e pods without any GPU fallback — a statement of strategic independence from [[entities/nvidia]].

## Key Facts

- **Type**: Custom AI accelerator (ASIC)
- **Owner**: Google / Alphabet
- **Generations**: 7 (v1 through Ironwood v7)
- **Available via**: Google Cloud Platform
- **Software stack**: XLA compiler, JAX, Pathways
- **Notable for**: Most mature hyperscaler custom silicon; Gemini 3 training infrastructure

## Generational Evolution

| Generation | Year | Focus | Peak Performance | Memory | Key Innovation |
|-----------|------|-------|-----------------|--------|----------------|
| v1 | 2015 | Inference | 92 TOPS (8-bit) | 28 MB on-chip | Systolic array ASIC |
| v2 | 2017 | Training | 45 TFLOPS BF16 | 8 GB HBM | First training TPU |
| v3 | 2018 | Training | 420 TFLOPS BF16 | 128 GB HBM | 100+ PFLOPS pods |
| v4 | 2020 | Both | ~1 PFLOPS | HBM | Optical circuit switching |
| v5e/v5p | 2023 | Split | 393 TOPS INT8 | HBM | Split training/inference |
| v6e "Trillium" | 2024 | Both | 4.7x vs v5 | 2x HBM | Jupiter 13 Pb/s fabric |
| v7 "Ironwood" | 2025 | Inference | 4,614 TFLOPS | 192 GB HBM | 42.5 exaFLOPS pod |

## Key Architectural Innovations

- **Systolic arrays**: 65,536 multiply-accumulate units per chip (v1), optimized for dense matrix operations
- **Optical Circuit Switching (v4+)**: Reconfigurable optical interconnects replacing fixed electrical fabrics
- **SparseCores**: Specialized processors for embedding tables, 5-7x speedup on sparse operations
- **Jupiter fabric (v6)**: 13 petabit/s bisectional bandwidth connecting 100,000+ chips

## Performance vs GPUs

- TPU v4 vs A100: 1.2-1.7x higher throughput at 53-77% of A100 power
- ~3x less electricity and ~20x less CO2 than on-premise GPU clusters
- Cost: $2.00/FLOPS-hour (vs $2.80 for NVIDIA B100 on cloud)
- AssemblyAI: 4x performance per dollar on v5e; Gridspace: 5x training speedup

## Mentioned In

- [[sources/google-tpu-architecture-gemini]] — comprehensive architecture deep dive
- [[sources/ai-hardware-accelerators-2026-guide]] — cost comparison
