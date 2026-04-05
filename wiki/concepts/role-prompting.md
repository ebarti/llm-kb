---
title: "Role Prompting"
type: concept
sources: ["[[sources/prompthub-role-prompting-research]]", "[[sources/anthropic-claude-prompting-best-practices]]", "[[sources/lakera-prompt-engineering-guide]]"]
related: ["[[concepts/prompt-engineering]]", "[[concepts/system-prompt-design]]", "[[concepts/few-shot-prompting]]"]
last_compiled: 2026-04-05
summary: "Assigning a persona or expert identity to an LLM — effective for tone/style control and creative tasks, but unreliable for factual accuracy where 'none of the strategies outperformed random selection.'"
---

## Overview

Role prompting (also called persona prompting) is the technique of explicitly assigning a specific role, persona, or expert identity to an LLM before it performs a task. Common patterns include "You are a senior Python developer" or "Act as a medical professional specializing in cardiology."

The technique is intuitive and widely used, but research reveals a nuanced picture: role prompting measurably helps for some task types while providing no benefit (or even hurting) for others.

## When Role Prompting Works

Research confirms role prompting is effective for:

- **Creative writing and open-ended tasks**: Personas reliably shape tone, voice, and style
- **Tone and style control**: "Talk like a pirate" or "Write in the style of a technical manual" works consistently
- **Security guardrails**: System-level role definitions help establish behavioral boundaries
- **Format steering**: Domain-specific personas can guide output structure (e.g., "You are a JSON structurer")

## When Role Prompting Fails

Multiple studies show role prompting does not help (and may hurt) for:

- **Factual accuracy tasks**: Across 4 LLM families and 2,410 factual questions, "none of the strategies for picking personas outperformed random selection"
- **Simple persona definitions**: Basic prompts like "You are a lawyer" have minimal effect
- **Expert personas on fact-based tasks**: Expert personas "consistently degraded performance in categories that rely on precise fact retrieval or strict logic"
- **Predicting the optimal persona**: Results are highly unpredictable — in one experiment, an "idiot" persona outperformed a "genius" persona on MMLU

## Best Practices

If using role prompting:

1. **Be specific and domain-aligned**: Narrow, detailed roles outperform generic ones
2. **Use detailed descriptions**: Comprehensive persona descriptions beat one-word labels
3. **Prefer LLM-generated personas**: The ExpertPrompting framework shows LLM-generated detailed personas significantly outperform human-written ones
4. **Use direct assignment**: "You are an X" works better than "Imagine you are an X"
5. **Prefer gender-neutral, work-related roles**: These show slightly better performance (small effect sizes)
6. **Don't rely on personas for accuracy**: Use [[concepts/chain-of-thought-prompting]] or [[concepts/few-shot-prompting]] instead

## Risks

LLMs can inadvertently adopt stereotypes from training data. Assigning roles associated with specific professions, genders, or nationalities can activate and amplify biases in model outputs.

## Sources
- [[sources/prompthub-role-prompting-research]] — Comprehensive research synthesis showing mixed effectiveness
- [[sources/anthropic-claude-prompting-best-practices]] — Role assignment in Claude system prompts
- [[sources/lakera-prompt-engineering-guide]] — Role-based as one of the prompt type categories

## Related Concepts
- [[concepts/prompt-engineering]] — parent domain
- [[concepts/system-prompt-design]] — role assignment typically lives in system prompts
- [[concepts/few-shot-prompting]] — more reliable for format/behavior steering
