---
title: "Few-Shot vs Zero-Shot Prompting"
type: comparison
subjects: ["[[concepts/few-shot-prompting]]", "[[concepts/zero-shot-prompting]]"]
sources: ["[[sources/promptingguide-few-shot]]", "[[sources/anthropic-claude-prompting-best-practices]]", "[[sources/lakera-prompt-engineering-guide]]"]
last_compiled: 2026-04-05
summary: "Zero-shot is simpler and cheaper (try first); few-shot is more reliable for format control and edge cases (3-5 examples). Research shows few-shot format matters more than label accuracy."
---

## Overview

The choice between zero-shot and few-shot prompting is the most fundamental decision in [[concepts/prompt-engineering]]. Modern instruction-tuned models are remarkably capable in zero-shot settings, making few-shot less necessary than in earlier model generations — but still valuable for specific use cases.

## Comparison Table

| Dimension | Zero-Shot | Few-Shot |
|-----------|-----------|----------|
| **Examples provided** | None | 3-5 typically |
| **Prompt length** | Short | Longer (examples add tokens) |
| **Cost per call** | Lower | Higher (more input tokens) |
| **Format control** | Limited | Strong (examples demonstrate format) |
| **Setup effort** | Minimal | Requires curating examples |
| **Edge case handling** | Model's default | Can demonstrate edge cases |
| **Generalization** | Relies on pre-training | Steered by examples |
| **Recommended first try** | Yes | Only if zero-shot fails |

## When to Use Each

### Zero-Shot
- Simple, well-defined tasks
- When the instruction is unambiguous
- Initial exploration before investing in examples
- Cost-sensitive applications
- Tasks where the model already excels (summarization, translation)

### Few-Shot
- Specific formatting requirements (JSON schemas, custom tables)
- Classification with custom categories
- Domain-specific conventions
- When zero-shot produces inconsistent results
- Complex tone/style requirements

## Key Research Insight

Min et al. (2022) found that in few-shot prompting, **format and distribution of examples matter more than label accuracy**. Random labels from the true distribution outperform uniform random labels. This suggests few-shot works by activating the right "task mode" rather than teaching new knowledge.

## Sources
- [[sources/promptingguide-few-shot]] — Research findings on example selection
- [[sources/anthropic-claude-prompting-best-practices]] — "Try zero-shot before few-shot" guidance
- [[sources/lakera-prompt-engineering-guide]] — Both types in the technique taxonomy
