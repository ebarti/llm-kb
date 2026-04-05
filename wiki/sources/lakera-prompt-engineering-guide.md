---
title: "Source: The Ultimate Guide to Prompt Engineering (Lakera)"
type: source-summary
source: "[[raw/lakera-prompt-engineering-guide]]"
related: ["[[concepts/prompt-engineering]]", "[[concepts/prompt-injection]]", "[[concepts/structured-output-prompting]]"]
last_compiled: 2026-04-05
summary: "Lakera's 2026 guide covering 9 essential techniques (clarity, CoT, format constraints, prompt combinations, output anchoring, iteration, compression, multi-turn memory, scaffolding) plus model-specific tips and security."
---

## Key Points
- Identifies 9 essential prompt engineering techniques
- Emphasizes "clear structure and context matter more than clever wording"
- Prompt component structure: system message, instruction, context, examples, output constraints, delimiters
- Model-specific: GPT prefers numeric constraints/markdown; Claude prefers XML tags; Gemini prefers hierarchical markdown
- Adversarial prompting section covers indirect phrasing, roleplay exploits, progressive extraction, obfuscation
- Prompt scaffolding wraps user inputs in guarded templates as a security measure

## Detailed Summary
This comprehensive guide from Lakera (an AI security company) provides a practitioner-oriented overview of [[concepts/prompt-engineering]] that notably bridges the gap between quality prompting and security. The dual focus on effectiveness AND adversarial robustness makes it uniquely valuable. The model-specific tips (Claude likes XML, GPT likes markdown, Gemini likes hierarchy) are immediately actionable.

## Related Concepts
- [[concepts/prompt-engineering]] — parent domain
- [[concepts/prompt-injection]] — security concerns
- [[concepts/structured-output-prompting]] — format control techniques
