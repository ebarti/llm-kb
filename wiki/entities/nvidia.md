---
title: "Nvidia"
type: entity
entity_type: org
sources: ["[[sources/cfr-china-ai-chip-deficit-huawei-nvidia]]", "[[sources/time-us-china-ai-race-graphs]]", "[[sources/csis-deepseek-breakthrough-redefining-ai-race]]", "[[sources/nvidia-gpu-specs-ai-training-2026]]", "[[sources/ai-hardware-accelerators-2026-guide]]", "[[sources/hbm-memory-wall-roadmap]]", "[[sources/ai-inference-accelerators-compared]]"]
related: ["[[entities/huawei]]", "[[concepts/ai-chip-export-controls]]", "[[concepts/semiconductor-supply-chain]]", "[[concepts/us-china-ai-race]]", "[[concepts/ai-hardware-landscape]]", "[[concepts/ai-accelerators]]", "[[concepts/memory-bandwidth-wall]]", "[[entities/amd]]", "[[entities/cerebras]]", "[[entities/groq]]"]
last_compiled: 2026-04-05
summary: "Dominant AI chip company (~80% market share); Blackwell architecture (B200: 1800 TFLOPS FP8, 192GB HBM3e, 208B transistors); acquired Groq for $20B; Vera Rubin (3.6 EFLOPS, late 2026); CUDA ecosystem is the primary moat; geopolitically central to US-China AI race."
---

## Overview

Nvidia is the world's dominant designer of AI accelerator chips, commanding ~80% of the AI accelerator market. Founded by Jensen Huang in 1993, the company is a central player in both [[concepts/ai-hardware-landscape]] and [[concepts/ai-geopolitics]]. The company's GPUs — from the H100 through the Blackwell B200 and upcoming Vera Rubin — are the de facto standard for AI training and inference worldwide. The CUDA software ecosystem, with over a decade of optimized libraries, is NVIDIA's strongest competitive moat.

## GPU Architecture Evolution

| Generation | Flagship | Year | FP8 TFLOPS | Memory | Bandwidth | TDP |
|-----------|----------|------|-----------|--------|-----------|-----|
| Ampere | A100 | 2020 | ~624 (INT8) | 80GB HBM2e | 2.0 TB/s | 400W |
| Hopper | H100 | 2022 | 3,958 | 80GB HBM3 | 3.35 TB/s | 700W |
| Hopper+ | H200 | 2024 | 3,958 | 141GB HBM3e | 4.8 TB/s | 700W |
| Blackwell | B200 | 2024 | 1,800 | 192GB HBM3e | 8.0 TB/s | 1,000W |
| Blackwell Ultra | B300 | H2 2025 | Higher | HBM3e | Higher | 1,000W+ |
| Vera Rubin | TBD | Late 2026 | 3.6 EFLOPS FP4 | HBM4 | TBD | TBD |

The B200 features 208 billion transistors and a second-generation Transformer Engine with FP4 precision support. The GB200 NVL72 rack system connects 36 Grace CPUs + 72 Blackwell GPUs with 13.5 TB HBM3e and 130 TB/s NVLink. As of February 2026, Blackwell is in full-scale volume production — ending the "scarcity era" of 2024-2025.

## Key Facts

- **Market share**: ~80% of AI accelerators
- **Chip performance**: approximately 5x more powerful than China's best (Huawei Ascend 910C), widening to 17x by 2027
- **Production**: 4.5 million chips in 2025, scaling to 10+ million by 2027
- **Manufacturing partner**: TSMC (advanced 3-5nm nodes)
- **Groq acquisition**: $20B — integrating deterministic scheduling into Vera Rubin
- **Jensen Huang estimate**: $3-4 trillion AI infrastructure spending by end of decade
- **Market event**: Lost $600 billion in market value on January 27, 2025 after DeepSeek announcement

## Geopolitical Significance

Nvidia sits at the intersection of the [[concepts/ai-chip-export-controls]] debate:
- **H200 export decision**: Trump administration moved to allow case-by-case H200 sales to China (with 25% fee)
- **Risk assessment**: Exporting 3 million H200 chips would give China compute power it couldn't produce domestically until 2028-2029
- **CFR position**: "Huawei is not a threat that justifies loosening controls; it is evidence that the controls are working"
- **Revenue tension**: Nvidia faces commercial pressure to sell to China vs. national security concerns

## Mentioned In

- [[sources/nvidia-gpu-specs-ai-training-2026]] — detailed hardware specifications
- [[sources/ai-hardware-accelerators-2026-guide]] — landscape and cost comparison
- [[sources/hbm-memory-wall-roadmap]] — HBM progression per GPU generation
- [[sources/ai-inference-accelerators-compared]] — inference benchmark comparison
- [[sources/ai-infrastructure-investment-2026]] — capex driver
- [[sources/cfr-china-ai-chip-deficit-huawei-nvidia]] — quantitative chip gap analysis
- [[sources/time-us-china-ai-race-graphs]] — market data
- [[sources/csis-deepseek-breakthrough-redefining-ai-race]] — market impact of DeepSeek
