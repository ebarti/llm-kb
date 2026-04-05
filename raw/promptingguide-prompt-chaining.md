---
title: "Prompt Chaining"
source: "https://www.promptingguide.ai/techniques/prompt_chaining"
author: "DAIR.AI / Prompt Engineering Guide"
date_published: 2024-01-01
date_ingested: 2026-04-05
tags: [prompt-engineering, prompt-chaining, workflows, multi-step]
type: article
status: raw
discovered_via: search
---

# Prompt Chaining: Comprehensive Overview

## Definition
Prompt chaining involves breaking complex tasks into subtasks and using an LLM's response from one prompt as input to another, creating a chain of prompt operations.

## How It Works
1. Identify subtasks from a complex task
2. Prompt with first subtask
3. Use response as input to next prompt
4. Continue until completion

Each chain prompt performs transformations or processes on generated responses before reaching the final desired state.

## Key Benefits
- Improved Performance: Better reliability for complex tasks that struggle with single detailed prompts
- Enhanced Transparency: Makes LLM applications more understandable
- Greater Controllability: Easier to manage and direct outputs
- Better Reliability: Simpler debugging and performance analysis at each stage

## Primary Use Case: Document Question Answering

Two-prompt chain:
- Prompt 1 (Extraction): Extract quotes relevant to the question from the document using XML tags
- Prompt 2 (Synthesis): Takes extracted quotes and original document to compose answers

## Implementation
- Can be implemented with basic scripting using API calls
- Tools like LangChain provide frameworks for managing chains
- The most common chaining pattern is self-correction: generate a draft → review against criteria → refine based on review
- Each step is a separate API call so you can log, evaluate, or branch at any point
