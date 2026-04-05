---
title: "Leveraging Large Language Models for Data Analysis Automation"
source: "https://pmc.ncbi.nlm.nih.gov/articles/PMC11844886/"
author: "PMC / Multiple Authors"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [data-analysis, automation, bioinformatics, LLM-applications, code-generation]
type: paper
status: raw
discovered_via: search
---

# Leveraging Large Language Models for Data Analysis Automation

## Overview

Researchers developed **mergen**, an R package that uses LLMs to generate executable data analysis code from natural language descriptions. The study evaluates how effectively GPT-3.5-turbo and GPT-4 perform on bioinformatics tasks of varying complexity.

## Methodology

Tasks ranked 1-5 by complexity based on required components: file reading, data wrangling, visualization, statistical/ML applications, and multi-dataset handling. 20 prompts tested 10 times each.

## Key Findings

### Task Complexity Impact
Code executability decreases significantly with task complexity. Executable responses averaged 607 characters versus 963 for non-executable code.

### Prompt Engineering Results
- Simple prompting: baseline performance
- "Act As" and "Chain of Thought" strategies: did not increase code executability for more complex tasks
- File content inclusion: improved complexity 2-3 tasks by 15-20%, but hindered complexity 4-5 performance

### Self-Correction Mechanism (Most Effective)
- Complexity 2: 22.5% improvement
- Complexity 3: 52.5% improvement
- Complexity 4: 27.5% improvement
- Complexity 5: 15% improvement

### Code Correctness (Critical Finding)
Executable code does not equal correct code:
- Complexity 1: 60% correct
- Complexity 2: 88% correct
- Complexity 3: 25% correct
- Complexity 4: 13% correct
- Complexity 5: 0% correct

### Model Comparison
GPT-4 showed 10-17.5% improvement over GPT-3.5-turbo on complexity 2 and 4 tasks, but both models struggle with complex bioinformatics code generation.

## Practical Implications

LLMs are effective for simple-to-moderate data analysis tasks. Humans remain essential for complex analyses requiring domain expertise. Self-correction loops are the most impactful technique.
