---
title: "Few-Shot Prompting"
source: "https://www.promptingguide.ai/techniques/fewshot"
author: "DAIR.AI / Prompt Engineering Guide"
date_published: 2024-01-01
date_ingested: 2026-04-05
tags: [prompt-engineering, few-shot, in-context-learning, examples]
type: article
status: raw
discovered_via: search
---

# Few-Shot Prompting: Comprehensive Overview

## Definition & Core Concept
Few-shot prompting enables in-context learning by providing demonstration examples within prompts to improve model performance on complex tasks. Few-shot properties first appeared when models were scaled to a sufficient size.

## How It Works
The technique conditions language models through examples before requesting responses to target queries. Examples can be:
- Static: Manually written examples included directly in the prompt
- Dynamic: Fetched from a vector store using semantic similarity

## Key Research Findings

Min et al. (2022) identifies critical factors:
- The label space and the distribution of the input text specified by the demonstrations are both important
- Format consistency matters significantly, even with randomized labels
- Random labels from true distributions outperform uniform distributions
- Label accuracy matters less than having structured examples

## Best Practices
- Examples should be directly relevant to the problem at hand
- Cover edge cases and vary enough that the model doesn't pick up unintended patterns
- Keep the number of examples at a normal level (3-5 for best results)
- Use structured tags like <example> to distinguish examples from instructions
- Few-shot remains one of the highest-ROI techniques available

## Limitations
- Insufficient for complex reasoning requiring multiple logical steps
- Advanced arithmetic problems
- Tasks requiring deeper analytical thinking
- These constraints suggest transitioning to chain-of-thought prompting for demanding applications
