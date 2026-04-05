---
title: "TextGrad"
type: entity
entity_type: tool
sources: ["[[sources/intuitionlabs-meta-prompting]]"]
related: ["[[concepts/meta-prompting]]", "[[concepts/prompt-engineering]]", "[[entities/dspy]]"]
last_compiled: 2026-04-05
summary: "Gradient-based prompt optimization framework that uses natural language feedback instead of numeric scores — published in Nature (2025), excels at instance-level refinement for coding and scientific Q&A."
---

## Overview

TextGrad is a [[concepts/meta-prompting]] framework that replaces traditional numeric optimization scores with natural language feedback. The model receives feedback like "the output missed the key detail about X" and uses that feedback to perform gradient descent in the space of prompt text.

## Key Innovation

Traditional optimization uses numeric loss functions. TextGrad's insight is that for prompt optimization, natural language feedback is more informative than a scalar score. The "gradients" are textual descriptions of what went wrong and how to improve.

## Performance

Published in Nature (2025), validating its significance as a research contribution. Excels at:
- Instance-level refinement for hard tasks
- Coding problems
- Scientific Q&A

## Complementary to DSPy

- **TextGrad**: Instance-level refinement, best for hard specific problems
- **[[entities/dspy]]**: Pipeline-level optimization, best for reusable systems

## Mentioned In
- [[sources/intuitionlabs-meta-prompting]] — TextGrad as Nature-published [[concepts/meta-prompting]] framework
