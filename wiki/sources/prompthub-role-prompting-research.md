---
title: "Source: Role-Prompting Research (PromptHub)"
type: source-summary
source: "[[raw/prompthub-role-prompting-research]]"
related: ["[[concepts/role-prompting]]", "[[concepts/prompt-engineering]]"]
last_compiled: 2026-04-05
summary: "PromptHub research review: role/persona prompting helps for creative/style tasks but provides no consistent improvement (and sometimes hurts) on factual accuracy tasks, especially with newer models."
---

## Key Points
- Role prompting effectiveness depends heavily on task type
- Works for: creative writing, tone/style control, security guardrails
- Fails for: accuracy-based tasks, simple persona definitions, predicting optimal personas
- ExpertPrompting (LLM-generated detailed personas) significantly outperforms basic human-written personas
- An "idiot" persona outperformed a "genius" persona on MMLU (GPT-4-turbo)
- Direct assignment ("You are an X") more effective than imaginative ("Imagine you are...")
- LLM-generated personas outperform human-written ones

## Detailed Summary
This article synthesizes multiple research papers on [[concepts/role-prompting]] and reaches a nuanced conclusion: persona prompting is real and measurable for stylistic/creative tasks, but unreliable for factual accuracy. The finding that "none of the strategies for picking personas outperformed random selection" on accuracy tasks is particularly sobering. The practical takeaway is to use role prompting for tone and format control, but don't rely on it for correctness.

## Related Concepts
- [[concepts/role-prompting]] — the core technique
- [[concepts/prompt-engineering]] — parent domain
- [[concepts/system-prompt-design]] — role assignment in system prompts
