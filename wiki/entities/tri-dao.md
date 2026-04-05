---
title: "Tri Dao"
type: entity
entity_type: person
sources: ["[[sources/flashattention-3-paper]]", "[[sources/mamba-state-space-models-visual-guide]]", "[[sources/flashattention-3-tri-dao-blog]]", "[[sources/mamba-visual-guide-grootendorst]]"]
related: ["[[concepts/flash-attention]]", "[[concepts/mamba]]", "[[concepts/state-space-models]]", "[[entities/flashattention]]", "[[concepts/attention-mechanisms]]"]
last_compiled: 2026-04-05
summary: "Co-creator of FlashAttention (IO-aware attention optimization) and Mamba (selective state space models) — two of the most impactful systems contributions to modern LLM efficiency."
---

## Overview

Tri Dao is a researcher (Princeton PhD, Stanford postdoc, now at Together AI) who has made two of the most impactful contributions to efficient deep learning:

1. **[[concepts/flash-attention]]** (2022-2024): IO-aware attention algorithm that reduces memory from O(N^2) to O(N) and speeds up training 2-4x. Now the default attention implementation in all major frameworks.

2. **[[concepts/mamba]]** (2023, with Albert Gu): Selective state space model with input-dependent state transitions and hardware-aware kernel fusion. The leading alternative to transformer attention.

Both contributions share a philosophy: optimize for the **GPU memory hierarchy** (SRAM vs HBM) rather than theoretical FLOP counts.

## Mentioned In

- [[sources/flashattention-3-paper]] — FlashAttention-3 paper
- [[sources/mamba-state-space-models-visual-guide]] — Mamba architecture
