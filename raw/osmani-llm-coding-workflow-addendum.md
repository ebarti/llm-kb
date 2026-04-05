---
title: "My LLM Coding Workflow Going Into 2026"
source: "https://addyosmani.com/blog/ai-coding-workflow/"
author: "Addy Osmani"
date_published: 2025-12-15
date_ingested: 2026-04-05
tags: [ai-coding, developer-workflow, pair-programming, best-practices]
type: article
status: raw
discovered_via: search
---

# Addy Osmani's LLM Coding Workflow for 2026

## Core Philosophy

Osmani advocates for "AI-augmented software engineering" rather than autonomous AI development. He emphasizes that "the human engineer remains the director of the show," treating LLMs as powerful pair programmers requiring clear direction, context, and oversight.

## Workflow Stages

### 1. Planning Before Code
The process begins with detailed specification work. Osmani describes brainstorming requirements with the AI iteratively, then compiling findings into a comprehensive spec.md. He then requests the model generate a project plan -- what he calls doing a "waterfall in 15 minutes."

### 2. Breaking Work Into Small Chunks
Rather than requesting large monolithic outputs, Osmani divides projects into manageable iterations. He reports developers found that massive AI-generated code led to duplication and architectural confusion.

### 3. Providing Extensive Context
Osmani emphasizes feeding models all relevant information using context-packing tools like gitingest or repo2txt. He's optimistic about Claude Skills for packaging reusable domain expertise.

## Models and Tools

- Primary choice: Gemini for natural interaction and first-try understanding
- Secondary: Claude, GitHub Copilot Agent, Google's Jules
- Strategy: "Model musical chairs" -- switching between models when one gets stuck

Key statistic: At Anthropic, approximately 90% of Claude Code's implementation is written by Claude Code itself.

## Code Quality and Review

Osmani treats AI output as coming from an "over-confident" junior developer. Every AI-generated snippet requires review, testing, and validation. He uses Chrome DevTools MCP for browser access.

Multi-model review: Spawning secondary AI sessions to critique code from the first -- having Gemini review Claude's work.

## Version Control

Frequent commits as "save points in a game." Branches/worktrees to isolate concurrent AI experiments.

## Key Concerns

Osmani warns against "vibe coding" without quality oversight. One developer's cautionary tale: rushing with AI generated an "inconsistent mess" requiring painful refactoring.

## Bottom Line

Disciplined software engineering practices with aggressive AI tool use, keeping humans decisively in control while dramatically accelerating mechanical coding tasks.
