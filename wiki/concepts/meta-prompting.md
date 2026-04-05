---
title: "Meta-Prompting"
type: concept
sources: ["[[sources/intuitionlabs-meta-prompting]]", "[[sources/promptingguide-few-shot]]"]
related: ["[[concepts/prompt-engineering]]", "[[concepts/prompt-chaining]]", "[[concepts/chain-of-thought-prompting]]", "[[entities/dspy]]", "[[entities/textgrad]]"]
last_compiled: 2026-04-05
summary: "The practice of using LLMs to generate, evaluate, and optimize prompts for LLMs — 'prompts that write other prompts' — with frameworks like DSPy (46%→64% accuracy) and TextGrad (Nature 2025) formalizing the approach."
---

## Overview

Meta-prompting is the practice of using LLMs to generate, modify, or optimize prompts for other (or the same) LLMs. The central question is: what if the model itself designed the prompt? This self-referential approach turns [[concepts/prompt-engineering]] from a manual craft into an automated optimization process.

The field has matured rapidly, with frameworks like [[entities/dspy]] and [[entities/textgrad]] providing principled optimization methods that measurably outperform manual prompt crafting. Meta-prompting represents the cutting edge of prompt engineering — the point where it becomes prompt engineering engineering.

## Core Mechanisms

### Self-Refine (Generate → Critique → Improve)
The simplest and most immediately practical meta-prompting technique:
1. Model produces an initial answer
2. Model is prompted: "Critique your answer and improve it"
3. Improved answer generated
4. Cycle can repeat for multiple iterations

Performance: ~20% absolute improvement on average across seven diverse tasks. Outputs preferred by both humans and automatic metrics.

### Recursive Meta-Prompting
A meta-prompt transforms a broad task into a sequence of focused sub-prompts:
- "First, list major factors; then, for each factor, propose solutions; finally, evaluate feasibility"
- AutoGPT exemplifies this: the system continually generates new prompts based on evolving state

### DSPy (Declarative Self-improving Python)
A "compiler" for prompts that optimizes entire prompt pipelines at compile-time:
- Bootstraps few-shot examples from data
- Includes automatic instruction optimization
- Raised accuracy from 46.2% to 64.0% on prompt evaluation tasks
- Superior for building robust, scalable, reusable systems

### TextGrad
Replaces numeric optimization scores with natural language feedback:
- Model receives feedback like "the output missed key detail about X"
- Uses that feedback to "gradient-descent in the space of prompt text"
- Published in Nature (2025)
- Excels at instance-level refinement for coding and scientific Q&A

### Cross-Refine
Uses separate generator and critic LLMs:
- The critic can be a different (potentially cheaper) model
- Performs effectively even with less powerful models
- Enables cost-effective quality improvement

## Advantages Over Manual Prompting

- **Token efficiency**: Well-crafted meta-prompts provide reusable scaffolds
- **Consistency**: Avoids biases inherent in few-shot examples
- **Zero-shot generalization**: Enhanced capability without task-specific examples
- **Dynamic adaptation**: Can modify prompts in response to intermediate results

## Risks and Limitations

- **Increased costs**: Multiple LLM calls per task (higher latency and cost)
- **Error propagation**: Flawed meta-prompts amplify errors rather than correcting them
- **Prompt injection surface**: Multiple prompt turns increase attack opportunities
- **Complexity overhead**: Requires deep understanding of both domain and LLM behavior
- **Agent loop issues**: Systems can get stuck in unproductive refinement loops

## Application to This KB

The KB system could benefit from meta-prompting in several ways:
- **Self-improving compilation**: After generating wiki articles, a critique step could identify gaps
- **Query optimization**: Meta-prompting could generate better search queries during RESEARCH
- **Lint-driven improvement**: The LINT operation is essentially meta-prompting applied to the KB

## Sources
- [[sources/intuitionlabs-meta-prompting]] — Comprehensive deep dive on mechanisms, frameworks, results
- [[sources/promptingguide-few-shot]] — Meta-prompting as structure-focused alternative to few-shot

## Related Concepts
- [[concepts/prompt-engineering]] — parent domain
- [[concepts/prompt-chaining]] — meta-prompting typically uses chaining
- [[concepts/chain-of-thought-prompting]] — reasoning within the meta-loop
- [[entities/dspy]] — leading meta-prompting framework
- [[entities/textgrad]] — gradient-based prompt optimization
