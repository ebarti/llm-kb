---
title: "Source: Meta-Prompting — LLMs Crafting & Enhancing Their Own Prompts (IntuitionLabs)"
type: source-summary
source: "[[raw/intuitionlabs-meta-prompting]]"
related: ["[[concepts/meta-prompting]]", "[[concepts/prompt-engineering]]", "[[entities/dspy]]", "[[entities/textgrad]]"]
last_compiled: 2026-04-05
summary: "IntuitionLabs deep dive on meta-prompting: self-improving prompt loops, DSPy (46%→64% accuracy), TextGrad (Nature 2025), Self-Refine (~20% improvement), recursive meta-prompting, and future multimodal directions."
---

## Key Points
- Meta-prompting: "prompts that write other prompts" through iterative refinement
- DSPy: Compiler-based prompt optimization, raised accuracy from 46.2% to 64.0%
- TextGrad: Natural language feedback as gradient descent over prompt text (Nature 2025)
- Self-Refine: Generate → critique → improve cycle, ~20% absolute improvement across 7 tasks
- Cross-Refine: Separate generator and critic LLMs, works with less powerful models
- Qwen-72B with meta-prompt: 46.3% MATH, 83.5% GSM8K (outperforming fine-tuned models)
- Risks: increased costs, error propagation, prompt injection across multiple turns

## Detailed Summary
This is the most comprehensive treatment of [[concepts/meta-prompting]] in the KB. The key insight is that LLMs themselves can be the best prompt engineers — DSPy and TextGrad formalize this into optimization frameworks that measurably outperform manual prompt crafting. The Self-Refine technique (generate → critique → improve) is immediately practical and requires no special tooling. Future directions suggest meta-prompting will become internalized in model architectures.

## Related Concepts
- [[concepts/meta-prompting]] — the core technique
- [[concepts/prompt-engineering]] — parent domain
- [[concepts/prompt-chaining]] — meta-prompting often uses chaining
