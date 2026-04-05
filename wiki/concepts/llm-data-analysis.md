---
title: "LLM Data Analysis"
type: concept
sources: ["[[sources/mergen-llm-data-analysis-automation]]", "[[sources/assemblyai-llm-use-cases-2026]]"]
related: ["[[concepts/llm-applications-beyond-code]]", "[[concepts/reflection-pattern]]", "[[concepts/prompt-engineering]]"]
tags: [data-analysis, automation, code-generation, analytics]
last_compiled: 2026-04-05
summary: "LLMs automate data analysis via natural language to code translation, but face a critical executability-correctness gap: code that runs is not always code that works (88% correct at simple tasks, 0% at complex). Self-correction loops improve performance by up to 52.5%."
---

## Overview

LLM-powered data analysis represents one of the most practically important — and most overhyped — frontiers of [[concepts/llm-applications-beyond-code]]. The promise is compelling: describe an analysis in natural language and receive executable, correct code. The reality, as demonstrated by the mergen study, reveals a critical gap between what runs and what works.

## The Executability-Correctness Gap

The central finding from the mergen study is that **executable code does not equal correct code**:

| Task Complexity | Executability | Correctness |
|----------------|---------------|-------------|
| 1 (simple) | High | 60% |
| 2 (moderate) | Good | 88% |
| 3 (complex) | Declining | 25% |
| 4 (multi-step) | Low | 13% |
| 5 (expert) | Very low | 0% |

This has profound implications: users who receive running code may trust incorrect results, especially if they lack the domain expertise to validate the output. The risk is particularly high in domains where data analysis informs consequential decisions — healthcare, finance, policy.

## What Works

### Self-Correction (Most Effective)
The [[concepts/reflection-pattern]] applied to data analysis: generate code, execute it, feed errors back to the LLM, iterate. This improved executability by:
- Complexity 2: +22.5%
- Complexity 3: +52.5%
- Complexity 4: +27.5%
- Complexity 5: +15%

### Simple-to-Moderate Tasks
LLMs are genuinely effective for routine data tasks: reading files, basic data wrangling, simple visualizations, and standard statistical tests. These represent a significant fraction of day-to-day data work.

## What Does Not Work

### Complex Multi-Step Analysis
At complexity levels 4-5 (multi-dataset handling, advanced ML, domain-specific bioinformatics), LLMs produce code that either fails to execute or executes incorrectly. Humans remain essential for expert analysis.

### Conventional Prompt Engineering
Surprisingly, "Act As" prompts and [[concepts/chain-of-thought-prompting]] did not improve performance on complex tasks. For data analysis, structural scaffolding (iterative correction) outperforms prompt sophistication.

### Structured Data Prediction
When comparing GPT-4 against XGBoost on structured prediction tasks, XGBoost achieved F1 0.87 while GPT-4 zero-shot achieved 0.43. LLMs are not a substitute for traditional ML on structured data.

## Enterprise Applications

Despite limitations, enterprises report significant productivity gains from LLM-assisted analytics:
- Sales teams: 23% conversion rate improvements from call analysis
- Support centers: 40% reduction in resolution time
- Executives: 2+ hours weekly saved on meeting insights
- Overall: 50-70% task time reduction for routine analytical tasks

## The Right Mental Model

LLMs for data analysis work best as **first-draft generators with mandatory human review** — analogous to how [[concepts/post-code-ai-workflow]] frames AI code generation. The human analyst's role shifts from writing analysis code to reviewing, validating, and refining AI-generated analyses.

## Open Questions

- Can self-correction loops close the correctness gap for complex tasks?
- Should data analysis LLMs include confidence scores for their outputs?
- How can domain expertise be integrated into the correction loop effectively?

## Sources

- [[sources/mergen-llm-data-analysis-automation]] — executability-correctness gap data
- [[sources/assemblyai-llm-use-cases-2026]] — enterprise analytics use cases
