---
title: "Few-Shot Prompting"
type: concept
sources: ["[[sources/promptingguide-few-shot]]", "[[sources/anthropic-claude-prompting-best-practices]]", "[[sources/lakera-prompt-engineering-guide]]"]
related: ["[[concepts/prompt-engineering]]", "[[concepts/zero-shot-prompting]]", "[[concepts/chain-of-thought-prompting]]", "[[concepts/structured-output-prompting]]"]
last_compiled: 2026-04-05
summary: "In-context learning via demonstration examples within prompts — the highest-ROI prompt engineering technique, where format and distribution matter more than label accuracy."
---

## Overview

Few-shot prompting is the practice of providing a small number of input-output examples (typically 3-5) within a prompt to steer the model's behavior. It is widely considered the highest-ROI technique in [[concepts/prompt-engineering]] because it reliably controls format, tone, classification behavior, and reasoning patterns without any fine-tuning.

The technique leverages the in-context learning capability of large language models — the ability to adapt behavior based on examples provided in the prompt, without updating model weights. Few-shot properties first appeared when models were scaled to sufficient size, making it an emergent capability of large-scale LLMs.

## How It Works

The basic pattern is straightforward: show the model what you want, then ask for it.

```
Classify the sentiment of each review:
Review: "The food was amazing!" → Positive
Review: "Terrible service, never again." → Negative
Review: "It was okay, nothing special." → Neutral
Review: "Best experience of my life!" → [Model completes]
```

Examples can be:
- **Static**: Manually written and hardcoded in the prompt
- **Dynamic**: Retrieved from a vector store based on similarity to the current query

## Key Research Findings

Min et al. (2022) discovered counterintuitive properties of few-shot learning:
- **Format matters most**: The structure and distribution of examples is more important than whether labels are correct
- **Random labels work surprisingly well**: Random labels from the true distribution outperform uniform random labels
- **Label accuracy is secondary**: The examples activate the right "task mode" more than they teach new knowledge

This suggests few-shot works partly by cueing the model into the right behavioral pattern rather than genuinely teaching it from the examples.

## Best Practices

Anthropic recommends:
- **3-5 examples** for best results
- Make examples **relevant** (mirror actual use case), **diverse** (cover edge cases), and **structured**
- Wrap examples in `<example>` tags to distinguish them from instructions
- Consider asking the model to evaluate or generate additional examples from your initial set
- Try zero-shot first — only add examples if needed

## Limitations

Few-shot prompting is insufficient for:
- Complex multi-step reasoning (use [[concepts/chain-of-thought-prompting]] instead)
- Advanced arithmetic problems
- Tasks requiring deep analytical thinking

Too many examples can also hurt: they increase prompt length (cost and latency) and may introduce unintended patterns the model overfits to.

## Relationship to Other Techniques

Few-shot serves as a foundation that combines with other techniques:
- **Few-shot + CoT**: Examples include reasoning chains, not just answers
- **Few-shot + structured output**: Examples show the exact format (JSON, XML, tables)
- **Few-shot + role prompting**: Examples demonstrate the persona's style
- **Dynamic few-shot**: Examples retrieved via RAG based on query similarity

## Sources
- [[sources/promptingguide-few-shot]] — Research findings on what matters in example selection
- [[sources/anthropic-claude-prompting-best-practices]] — Claude-specific guidance on example formatting
- [[sources/lakera-prompt-engineering-guide]] — Few-shot in the broader technique taxonomy

## Related Concepts
- [[concepts/prompt-engineering]] — parent domain
- [[concepts/zero-shot-prompting]] — prompting without examples
- [[concepts/chain-of-thought-prompting]] — extends few-shot with reasoning chains
- [[concepts/structured-output-prompting]] — few-shot as format control mechanism
