---
title: "π0 (Pi-Zero)"
type: entity
entity_type: paper
url: "https://www.pi.website/blog/pi0"
related: ["[[concepts/vision-language-action-models]]", "[[concepts/flow-matching]]", "[[concepts/dexterous-manipulation]]", "[[concepts/cross-embodiment-transfer]]", "[[entities/physical-intelligence]]", "[[entities/rt-2]]"]
tags: [pi0, vla, flow-matching, physical-intelligence, robotics]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Physical Intelligence's 3B-parameter VLA model using flow matching for 50Hz robot control; trained on 7-8 robot types across 68 tasks; first system to achieve complex dexterous tasks (laundry folding at 1.0 success); open-sourced via Hugging Face LeRobot."
---

## Overview

π0 (pi-zero) is a general-purpose robot [[concepts/foundation-models-for-robotics]] developed by [[entities/physical-intelligence]]. It is a 3 billion parameter [[concepts/vision-language-action-models]] that uses [[concepts/flow-matching]] to generate smooth, continuous motor commands at 50Hz. It was the first system to achieve complex [[concepts/dexterous-manipulation]] tasks like laundry folding and box assembly.

## Key Facts

- **Type**: paper / model
- **Organization**: [[entities/physical-intelligence]]
- **Published**: October 31, 2024
- **Parameters**: 3B (full), 470M (π0-small)
- **Backbone**: PaliGemma (Google, 3B VLM)
- **Action Generation**: [[concepts/flow-matching]] at 50Hz
- **Training Data**: Open X-Embodiment + internet VLM data + π Dataset (8 robots, 68 tasks)
- **Open Source**: Yes (Hugging Face LeRobot, openpi on GitHub)
- **Notable for**: First system to fold laundry, assemble boxes; near-perfect scores where prior models score zero

## Performance

| Task | π0 | OpenVLA | Octo |
|------|-----|---------|------|
| Table Bussing (Easy) | 0.971 | 0 | 0.043 |
| Table Bussing (Hard) | 0.875 | 0 | 0 |
| Shirt Folding | 1.0 | 0 | 0 |
| Grocery Bagging | 0.786 | 0 | 0 |

## Variants

- **π0**: Flow matching, smooth continuous actions
- **π0-small**: 470M params, no VLM pre-training
- **π0-FAST**: Autoregressive with DCT-based FAST tokenization, 5x faster training

## Role in Knowledge Base

π0 represents the current state of the art in [[concepts/foundation-models-for-robotics]] for dexterous manipulation. It demonstrates that the LLM paradigm (pre-train broadly, fine-tune cheaply) works for physical skills. Its open-source release via Hugging Face democratizes access.

## Mentions

- [[sources/physical-intelligence-pi0-foundation-model]] -- primary source
- [[sources/llms-for-robotics-survey-2025]] -- in VLA evolution survey
