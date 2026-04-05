---
title: "Source: Claude Prompting Best Practices (Anthropic)"
type: source-summary
source: "[[raw/anthropic-claude-prompting-best-practices]]"
related: ["[[concepts/prompt-engineering]]", "[[concepts/system-prompt-design]]", "[[concepts/structured-output-prompting]]", "[[entities/anthropic]]", "[[entities/claude]]"]
last_compiled: 2026-04-05
summary: "Anthropic's official prompting guide for Claude 4.6: XML tags, role assignment, few-shot examples, adaptive thinking, long-context strategies, agentic system design, and output formatting control."
---

## Key Points
- Golden rule: if a colleague with minimal context would be confused by your prompt, Claude will be too
- Use XML tags (<instructions>, <context>, <example>) to structure complex prompts unambiguously
- 3-5 diverse, relevant examples for best few-shot results
- Put longform data at the TOP of prompts; queries at the end improve quality by up to 30%
- Ground long-document responses in quotes before answering
- Tell Claude what TO DO, not what NOT to do
- Adaptive thinking (thinking: {type: "adaptive"}) replaces manual budget_tokens
- "Think thoroughly" produces better reasoning than prescriptive step-by-step plans
- Self-correction chaining: generate → review → refine
- Prefilled responses deprecated in Claude 4.6

## Detailed Summary
This is the authoritative guide to prompting Claude, Anthropic's frontier LLM family. Key themes include clarity (be explicit, provide context for WHY), structure (XML tags, document hierarchy), and examples (few-shot with diverse coverage). The guide also covers advanced topics: adaptive thinking for reasoning, subagent orchestration, long-horizon state management, and hallucination minimization via "investigate before answering."

The guide emphasizes a shift in Claude 4.6: the model is more concise, more proactive, and less tolerant of vague prompts. Instructions designed for older models (aggressive tool-use nudges, anti-laziness prompting) should be dialed back.

## Notable Quotes
> "Show your prompt to a colleague with minimal context on the task and ask them to follow it. If they'd be confused, Claude will be too."

## Related Concepts
- [[concepts/prompt-engineering]] — parent domain
- [[concepts/system-prompt-design]] — system prompt patterns
- [[concepts/structured-output-prompting]] — format control
- [[concepts/few-shot-prompting]] — examples as steering
- [[concepts/prompt-chaining]] — multi-step workflows
