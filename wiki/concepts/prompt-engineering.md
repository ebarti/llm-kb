---
title: "Prompt Engineering"
type: concept
sources: ["[[sources/anthropic-claude-prompting-best-practices]]", "[[sources/lakera-prompt-engineering-guide]]", "[[sources/promptingguide-chain-of-thought]]", "[[sources/promptingguide-few-shot]]"]
related: ["[[concepts/chain-of-thought-prompting]]", "[[concepts/few-shot-prompting]]", "[[concepts/system-prompt-design]]", "[[concepts/structured-output-prompting]]", "[[concepts/role-prompting]]", "[[concepts/meta-prompting]]", "[[concepts/prompt-injection]]", "[[concepts/llm-knowledge-base]]"]
last_compiled: 2026-04-05
summary: "The discipline of designing inputs to LLMs that reliably produce high-quality, accurate, and well-structured outputs — encompassing techniques from simple clarity principles to advanced reasoning scaffolds."
---

## Overview

Prompt engineering is the discipline of crafting inputs to large language models to achieve optimal results. Far from "just asking questions," it is the practice of designing the types of instructions, context, examples, and constraints that guide models toward accurate, relevant, and actionable outputs. As Lakera frames it: "telling the model what to do in a way it truly understands."

In the context of this knowledge base, prompt engineering is especially meta-relevant: the KB system itself is driven by prompts at every stage ([[concepts/wiki-compilation]], [[concepts/llm-qa-over-documents]], [[concepts/linting-and-health-checks]]), so understanding prompting deeply improves everything the system does.

## Core Principles

**Clarity and Directness.** The single most important principle. Anthropic's golden rule: "Show your prompt to a colleague with minimal context on the task and ask them to follow it. If they'd be confused, Claude will be too." Being specific about desired output format, constraints, and behavior consistently outperforms vague or clever prompts. As Lakera notes: "Clear structure and context matter more than clever wording."

**Context and Motivation.** Explaining WHY behind instructions helps models generalize. Instead of "NEVER use ellipses," say "Your response will be read aloud by a TTS engine, so never use ellipses since TTS won't know how to pronounce them." The model can then generalize this reasoning to similar situations.

**Positive Instructions.** Tell the model what TO DO rather than what NOT to do. Instead of "Do not use markdown," say "Write in smoothly flowing prose paragraphs." Negative instructions are harder for models to follow reliably.

**Iterative Refinement.** Treat prompting as an interactive development process. Test, observe failures, refine. The best prompts emerge from iteration, not from first attempts.

## Prompt Component Structure

A well-designed prompt typically includes these components, not all required for every task:

| Component | Purpose | Example |
|-----------|---------|---------|
| System message | Sets behavior, tone, role | "You are a helpful coding assistant" |
| Instruction | Clear task direction | "Summarize this article in 3 bullet points" |
| Context | Background information | Documents, prior conversation, metadata |
| Examples | Few-shot demonstrations | Input-output pairs showing desired behavior |
| Output constraints | Format specifications | "Respond in JSON with fields: title, summary" |
| Delimiters | Section separation | XML tags, triple backticks, markdown headers |

## The Technique Landscape

Prompt engineering encompasses a hierarchy of techniques, from simple to advanced:

**Foundation Techniques:**
- [[concepts/zero-shot-prompting]] — Direct instruction without examples
- [[concepts/few-shot-prompting]] — Learning from demonstration examples
- [[concepts/role-prompting]] — Persona/expertise assignment

**Reasoning Techniques:**
- [[concepts/chain-of-thought-prompting]] — Step-by-step reasoning
- [[concepts/self-consistency-prompting]] — Multiple reasoning paths + voting
- [[concepts/tree-of-thoughts-prompting]] — Branching exploration with search

**Workflow Techniques:**
- [[concepts/prompt-chaining]] — Sequential multi-step pipelines
- [[concepts/structured-output-prompting]] — Format control (JSON, XML, tables)
- [[concepts/rag-prompting]] — Prompting within retrieval-augmented systems

**Advanced Techniques:**
- [[concepts/meta-prompting]] — Self-improving prompts and optimization
- [[concepts/system-prompt-design]] — Architecture-level prompt patterns

**Security:**
- [[concepts/prompt-injection]] — Attacks and defenses

## Practical Sweet Spots

Research identifies several practical guidelines:
- **Prompt length**: Performance starts degrading around 3,000 tokens; sweet spot is 150-300 words for most tasks
- **Few-shot examples**: 3-5 examples for best results
- **Self-consistency samples**: Plateau around 40 reasoning paths
- **Long context**: Put documents at top, queries at bottom (up to 30% quality improvement)

## Model-Specific Considerations

Different models respond best to different prompt formats:
- **Claude (Anthropic)**: Prefers XML-style tags and explicit boundary definitions
- **GPT (OpenAI)**: Responds well to numeric constraints and markdown formatting
- **Gemini (Google)**: Excels with hierarchical structure and markdown-style organization

## The 2025-2026 Shift

Prompt engineering is evolving from artisanal prompt crafting toward systematic practices:
- **Structured outputs APIs** (e.g., OpenAI's JSON schema enforcement) constrain generation at the token level
- **Context engineering** replaces prompt engineering — designing entire context assembly systems
- **Evaluation-driven development** — writing evals matters more than clever wording
- **Meta-prompting** — using LLMs to optimize their own prompts
- **Prompt scaffolding** — wrapping user inputs in guarded templates for security

## Sources
- [[sources/anthropic-claude-prompting-best-practices]] — Authoritative Claude-specific guide with XML tags, adaptive thinking, agentic patterns
- [[sources/lakera-prompt-engineering-guide]] — Comprehensive 2026 guide bridging quality and security
- [[sources/promptingguide-chain-of-thought]] — CoT as the foundational reasoning technique
- [[sources/promptingguide-few-shot]] — Few-shot as the highest-ROI technique

## Related Concepts
- [[concepts/llm-knowledge-base]] — This KB system is itself a prompt engineering artifact
- [[concepts/wiki-compilation]] — The compile pipeline depends on well-designed prompts
- [[concepts/data-quality-bottleneck]] — Bad prompts are a form of low data quality
- [[concepts/hallucination-contamination]] — Poor prompting increases hallucination risk
