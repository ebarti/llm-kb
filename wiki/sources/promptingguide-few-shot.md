---
title: "Source: Few-Shot Prompting (Prompt Engineering Guide)"
type: source-summary
source: "[[raw/promptingguide-few-shot]]"
related: ["[[concepts/few-shot-prompting]]", "[[concepts/zero-shot-prompting]]", "[[concepts/prompt-engineering]]"]
last_compiled: 2026-04-05
summary: "DAIR.AI overview of few-shot prompting: in-context learning via demonstration examples, with research showing format and label distribution matter more than label accuracy."
reading_time: "1 min"
---

## Key Points
- Few-shot prompting enables in-context learning through demonstration examples
- Few-shot properties first appeared when models were scaled to sufficient size
- Min et al. (2022): Label accuracy matters less than format consistency and input distribution
- 3-5 examples recommended for best results
- Remains one of the highest-ROI prompt engineering techniques
- Insufficient for complex multi-step reasoning — use CoT instead

## Detailed Summary
Few-shot prompting is the bread-and-butter of [[concepts/prompt-engineering]]. By showing the model a handful of input-output examples, you can steer format, tone, classification behavior, and more without any fine-tuning. Research reveals a counterintuitive finding: the format and distribution of examples matters more than whether the labels are actually correct. This suggests few-shot works partly by activating the right "task mode" in the model rather than teaching it new knowledge.

## Related Concepts
- [[concepts/few-shot-prompting]] — the core technique
- [[concepts/zero-shot-prompting]] — prompting without examples
- [[concepts/chain-of-thought-prompting]] — extends few-shot with reasoning chains
- [[concepts/prompt-engineering]] — parent domain
