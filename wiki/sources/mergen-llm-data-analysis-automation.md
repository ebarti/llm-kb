---
title: "Source: Leveraging LLMs for Data Analysis Automation"
type: source-summary
source: "[[raw/mergen-llm-data-analysis-automation]]"
related: ["[[concepts/llm-data-analysis]]", "[[concepts/llm-applications-beyond-code]]"]
tags: [data-analysis, automation, bioinformatics, code-generation]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "PMC study on 'mergen' R package: LLMs generate executable code for data analysis, but correctness drops from 88% (simple tasks) to 0% (complex tasks) — self-correction loops improve performance by up to 52.5%."
---

## Key Points

- mergen: R package using LLMs to generate data analysis code from natural language
- Code executability decreases significantly with task complexity
- Critical finding: executable code does not equal correct code
- Correctness rates: Complexity 1 (60%), 2 (88%), 3 (25%), 4 (13%), 5 (0%)
- Self-correction mechanism is the most effective technique: up to 52.5% improvement
- "Act As" and chain-of-thought prompting did not help for complex tasks
- GPT-4 showed 10-17.5% improvement over GPT-3.5-turbo on moderate tasks

## Detailed Summary

This PMC paper provides rigorous empirical evidence about LLM capabilities and limitations for automated data analysis. The researchers built **mergen**, an R package that translates natural language descriptions into executable bioinformatics code via GPT-3.5-turbo and GPT-4.

The most important finding is the **executability-correctness gap**: even when LLM-generated code runs without errors, it may produce incorrect results. At complexity level 2, 88% of executable code was correct; by complexity 5, the correctness rate dropped to 0%. This has profound implications for [[concepts/llm-data-analysis]] in any domain — users cannot assume that code that runs is code that works.

The **self-correction mechanism** emerged as the most impactful technique, improving executability by 22.5-52.5% across task complexities. This aligns with the [[concepts/reflection-pattern]] in agentic AI: generating output, evaluating it, and iterating.

Conventional [[concepts/prompt-engineering]] techniques ("Act As," [[concepts/chain-of-thought-prompting]]) did not meaningfully improve performance on complex tasks, suggesting that for data analysis, structural scaffolding (iterative correction) outperforms prompt sophistication.

## Concepts Introduced or Discussed

- [[concepts/llm-data-analysis]] -- automated code generation for analytics
- [[concepts/reflection-pattern]] -- self-correction as the most effective technique
- [[concepts/llm-applications-beyond-code]] -- data analysis as knowledge manipulation

## Metadata

- **Author**: Multiple (PMC)
- **Date Published**: 2025
- **Format**: paper
- **URL**: https://pmc.ncbi.nlm.nih.gov/articles/PMC11844886/
