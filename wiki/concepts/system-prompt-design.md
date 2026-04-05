---
title: "System Prompt Design"
type: concept
sources: ["[[sources/anthropic-claude-prompting-best-practices]]", "[[sources/lakera-prompt-engineering-guide]]", "[[sources/lakera-prompt-injection-guide]]"]
related: ["[[concepts/prompt-engineering]]", "[[concepts/role-prompting]]", "[[concepts/prompt-injection]]", "[[concepts/structured-output-prompting]]"]
last_compiled: 2026-04-05
summary: "Architectural patterns for system prompts that define consistent LLM behavior, roles, and constraints — the foundation layer that shapes all subsequent interactions."
---

## Overview

System prompt design is the practice of crafting the foundational instructions that define an LLM's behavior across all interactions. System prompts establish the persistent "personality," capabilities, constraints, and operational rules that apply regardless of what the user asks. They are the architecture of an LLM application — everything else builds on top.

In the context of this [[concepts/llm-knowledge-base]], the CLAUDE.md file is itself a system prompt: it defines the LLM's role, operations, conventions, and constraints for all wiki operations.

## Key Design Patterns

### Role-Based Templates
Assign a specific role with defined responsibilities:
```
You are a research assistant specializing in AI/ML literature.
Your role is to analyze papers, extract key findings, and
synthesize them into clear summaries.
```

### Behavioral Constraints
Define what the model should and should not do:
```
<default_to_action>
Implement changes rather than only suggesting them.
</default_to_action>
```

### Safety Boundaries
Establish guardrails for autonomous operation:
```
Consider the reversibility and potential impact of your actions.
For hard-to-reverse actions, ask the user before proceeding.
```

### Format Specifications
Define output structure expectations:
```
<avoid_excessive_markdown>
Write in clear, flowing prose. Avoid bullet-point lists
unless presenting truly discrete items.
</avoid_excessive_markdown>
```

## Best Practices (from Anthropic)

1. **Clarity over cleverness**: Write instructions that are clear, concise, and unambiguous
2. **Context for WHY**: Explain motivation behind rules so the model can generalize
3. **Positive framing**: "Do X" rather than "Don't do Y"
4. **XML structure**: Use consistent tag names across prompts for unambiguous parsing
5. **Evolve with the model**: Instructions designed for older models may need dialing back for newer ones (e.g., Claude 4.6 is more proactive and may overtrigger on aggressive tool-use nudges)
6. **Test across scenarios**: Run prompts through various situations and monitor consistency

## System Prompt as Security Layer

System prompts are the first line of defense against [[concepts/prompt-injection]]:
- Define clear role boundaries that resist override attempts
- Use instruction layering to reinforce behavioral constraints
- Keep sensitive information outside the prompt itself
- Anticipate adversarial inputs in the design

However, system prompts alone are insufficient for security — they must be combined with model-level training, input filtering, and output validation.

## Sources
- [[sources/anthropic-claude-prompting-best-practices]] — Claude system prompt patterns
- [[sources/lakera-prompt-engineering-guide]] — System message as prompt component
- [[sources/lakera-prompt-injection-guide]] — System prompts as defense layer

## Related Concepts
- [[concepts/prompt-engineering]] — parent domain
- [[concepts/role-prompting]] — role assignment within system prompts
- [[concepts/prompt-injection]] — attacks that attempt to override system prompts
- [[concepts/structured-output-prompting]] — format rules in system prompts
