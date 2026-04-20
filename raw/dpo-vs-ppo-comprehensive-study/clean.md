---
title: "Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study"
source: "https://arxiv.org/abs/2404.10719"
author: "Shusheng Xu et al."
date_published: 2024-04-16
date_ingested: 2026-04-05
tags: [dpo, ppo, alignment, comparison, benchmark]
type: paper
status: raw
discovered_via: search
---

# Is DPO Superior to PPO for LLM Alignment?

## Key Finding
PPO emerges as the superior approach across all tested scenarios, achieving state-of-the-art results particularly in challenging code competition tasks.

## Main Conclusions
- PPO consistently outperforms DPO across all experiments
- DPO may have fundamental limitations when examined theoretically and empirically
- Production systems leveraging PPO-based approaches have sound foundations
- Discrepancy between DPO's benchmark popularity and PPO's real-world effectiveness

## Experimental Scope
- Dialogue systems
- Code generation tasks
- Multiple RLHF testbeds

## PPO Advantages
- Robust to distribution shifts
- Performs well in complex tasks
- State-of-the-art on challenging code competitions

## DPO Limitations
- Sensitive to distribution shifts
- Best suited when training and preference data are well-aligned
- Suffers from out-of-distribution data
- Performance degrades when instruction data differs from preference data

## Practical Implications
- PPO is better for production systems requiring robustness
- DPO is easier to implement and more accessible
- Choice depends on specific use cases and available resources
- Code publicly released for reproducibility
