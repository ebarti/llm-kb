---
title: "RLHF Alternatives: DPO vs KTO vs IPO vs ORPO vs SPIN"
type: comparison
subjects: ["[[concepts/rlhf]]", "[[concepts/dpo]]", "[[concepts/kto]]", "[[concepts/ipo]]", "[[concepts/orpo]]"]
sources: ["[[sources/argilla-rlhf-alternatives-overview]]", "[[sources/argilla-kto-kahneman-tversky]]", "[[sources/wolfe-direct-preference-optimization]]", "[[sources/dpo-vs-ppo-comprehensive-study]]"]
last_compiled: 2026-04-05
summary: "Systematic comparison of 9+ preference alignment methods across data requirements, compute costs, pipeline complexity, and performance -- no single method wins everywhere; data quality and use case determine the best choice."
---

## Overview

Since DPO's publication in 2023, the landscape of LLM alignment methods has exploded. Each method makes different trade-offs between performance, simplicity, data requirements, and compute. This page provides a systematic comparison to guide method selection.

## Master Comparison Table

| Method | Data Format | Min Data | Pipeline Steps | Compute | Reference Model? |
|--------|-----------|----------|----------------|---------|-----------------|
| **RLHF (PPO)** | Pairwise preferences | ~10K | 3 (SFT → RM → PPO) | High | Yes (frozen) |
| **[[concepts/dpo]]** | Pairwise preferences | ~12K | 2 (SFT → DPO) | Medium | Yes (frozen) |
| **[[concepts/kto]]** | Binary signals | ~12K | 1-2 (optional SFT → KTO) | Medium/Low | Yes (frozen) |
| **[[concepts/ipo]]** | Pairwise preferences | ~12K | 2 (SFT → IPO) | Medium | Yes (frozen) |
| **[[concepts/orpo]]** | Pairwise preferences | ~7K | 1 (combined SFT+ORPO) | Low | No |
| **SPIN** | Chosen only | ~1.8K | Self-play iterations | High | Previous version |
| **CoH** | Conversational feedback | ~300K | 2 | Medium | No |
| **[[concepts/rlaif]]** | AI-generated pairs | ~125K | 3 (SFT → AI labels → PPO) | High | Yes |
| **SimPO** | Pairwise preferences | ~200K | 2 | Low | No |

## Decision Framework

### By Data Availability

**You have pairwise preference data:**
- Clean, transitive, high-quality → **DPO** or **IPO**
- Noisy, real-world → **KTO** (more robust to noise)
- Very small dataset (<10K) → **ORPO** (works with 7K)

**You have binary feedback only (thumbs up/down):**
- → **KTO** (designed for this case)

**You have no preference data:**
- Can generate from a strong LLM → **RLAIF** or **SPIN**
- Have only demonstrations → **SFT**, then consider **SPIN**

### By Compute Budget

| Budget | Recommended |
|--------|-------------|
| Maximum performance, unlimited compute | **PPO (RLHF)** |
| Good performance, moderate compute | **DPO** or **KTO** |
| Minimal compute, single GPU | **ORPO** |
| Need to bootstrap from scratch | **SPIN** |

### By Pipeline Simplicity

| Simplicity Level | Method |
|-----------------|--------|
| Simplest (1 step) | **ORPO** -- combines SFT + alignment |
| Simple (2 steps) | **DPO**, **KTO**, **IPO** -- SFT then align |
| Complex (3 steps) | **RLHF**, **RLAIF** -- SFT → RM → RL |

### By Robustness

- **Most robust to noisy data**: KTO (prospect theory handles noise)
- **Most robust to distribution shift**: PPO (online learning)
- **Most robust to overfitting**: IPO (explicit regularization)
- **Most robust without prior SFT**: KTO (DPO degrades without SFT)

## Key Insight: Data Quality Dominates

Across all methods, the single most important factor is **data quality**:
- SPIN: 1.8K well-curated prompts matched 50K standard prompts
- ORPO: 7K high-quality examples matched 200K
- UltraFeedback dramatically outperforms legacy datasets regardless of method

This means the choice of alignment method matters less than the quality of preference data. Invest in data curation first, then choose the simplest method that works.

## No Single Winner

The Argilla/MantisNLP survey concludes: "there isn't a single method that addresses all aspects effectively. Each approach has its advantages and disadvantages, and their effectiveness varies across different scenarios." HuggingFace experiments confirmed this -- IPO helped Zephyr but not OpenHermes.

Production recommendation: start with DPO (simplest good-enough method), graduate to PPO if performance is insufficient, and always invest more in data quality than method sophistication.

## Sources
- [[sources/argilla-rlhf-alternatives-overview]] -- the primary systematic comparison
- [[sources/argilla-kto-kahneman-tversky]] -- KTO-specific analysis
- [[sources/wolfe-direct-preference-optimization]] -- DPO details
- [[sources/dpo-vs-ppo-comprehensive-study]] -- PPO vs DPO empirical comparison
