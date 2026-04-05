---
title: "Source: Prompt Chaining (Prompt Engineering Guide)"
type: source-summary
source: "[[raw/promptingguide-prompt-chaining]]"
related: ["[[concepts/prompt-chaining]]", "[[concepts/prompt-engineering]]", "[[concepts/multi-agent-systems]]"]
last_compiled: 2026-04-05
summary: "DAIR.AI overview of prompt chaining: decomposing complex tasks into sequential LLM calls where each output feeds the next, improving transparency and controllability."
reading_time: "1 min"
---

## Key Points
- Breaks complex tasks into subtasks with each LLM response feeding the next prompt
- Improves performance, transparency, controllability, and debuggability
- Primary pattern: extraction → synthesis (e.g., extract quotes then compose answer)
- Most common chaining pattern: self-correction (generate → review → refine)
- Can be implemented with basic scripting or frameworks like LangChain

## Detailed Summary
Prompt chaining is the engineering practice of decomposing a complex task into a pipeline of simpler LLM calls. Rather than cramming everything into one massive prompt, each step has a focused objective and clean input/output contract. This is foundational to [[concepts/multi-agent-systems]] and production LLM applications. The self-correction pattern (generate draft → review against criteria → refine) is particularly powerful and widely used.

## Related Concepts
- [[concepts/prompt-chaining]] — the core technique
- [[concepts/prompt-engineering]] — parent domain
- [[concepts/multi-agent-systems]] — prompt chaining at scale
