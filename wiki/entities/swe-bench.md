---
title: "SWE-bench"
type: entity
entity_type: dataset
url: "https://www.swebench.com/"
sources: ["[[sources/swe-bench-leaderboard-2026]]", "[[sources/morphllm-coding-models-comparison-2026]]", "[[sources/morphllm-codex-vs-claude-code]]"]
related: ["[[concepts/swe-bench]]", "[[concepts/agentic-coding]]", "[[concepts/ai-code-generation]]", "[[entities/claude-code]]", "[[entities/openai-codex]]"]
tags: [benchmark, evaluation, coding, dataset]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "The dominant benchmark for AI software engineering agents -- real GitHub issues from production Python repos -- showing 59% improvement from 48.5% (GPT-4, 2023) to 80.8% (Opus 4.6, 2026) in under two years."
---

## Overview

SWE-bench is the primary evaluation benchmark for AI software engineering agents, created by Princeton University researchers. It tests whether AI systems can autonomously resolve real-world software issues collected from production GitHub repositories including Django, Flask, scikit-learn, and other major Python projects.

## Key Facts

- **Type**: Evaluation benchmark / dataset
- **Created by**: Princeton NLP Group
- **URL**: https://www.swebench.com/
- **Notable for**: Standard measure of AI coding agent capability adopted by all major AI labs

## Variants

| Variant | Size | Description |
|---------|------|-------------|
| SWE-bench (full) | 2,294 issues | Original automated dataset |
| SWE-bench Verified | 500 issues | Hand-reviewed subset, stricter evaluation |
| SWE-bench Pro | Multi-language | Standardized scaffold, cross-language |
| SWE-bench Live | Rolling | Monthly updates to prevent data contamination |

## Performance Timeline

| Date | Model | SWE-bench Verified |
|------|-------|-------------------|
| Nov 2023 | GPT-4 Turbo | 48.5% |
| Aug 2024 | Claude 3.5 Sonnet | 69.1% |
| Oct 2025 | Claude 4 Sonnet | 77.2% |
| Mar 2026 | Claude Opus 4.6 (w/ agent scaffold) | 80.8% |

This 59% improvement in under two years represents one of the fastest capability jumps in AI benchmarking history.

## What It Measures

Given a codebase and an issue description, the agent must:
1. Comprehend often vague problem descriptions
2. Navigate large codebases with minimal guidance
3. Generate patches that resolve the issue
4. Pass existing project test suites
5. Avoid breaking other functionality

A 77% score means a model can autonomously fix approximately 3 out of 4 typical GitHub issues. Models scoring 70%+ are considered production-ready with human oversight.

## Critical Insight: Scaffold > Model

The most important finding from 2026 benchmarking: identical model weights produce a 22-point swing on SWE-Bench Pro depending on the agent scaffold, IDE, and tooling -- demonstrating that the engineering around the model matters more than raw model capability.

## Mentions

- [[sources/swe-bench-leaderboard-2026]] -- full leaderboard and analysis
- [[sources/morphllm-coding-models-comparison-2026]] -- scaffold importance finding
- [[sources/morphllm-codex-vs-claude-code]] -- Codex vs Claude Code benchmarks
