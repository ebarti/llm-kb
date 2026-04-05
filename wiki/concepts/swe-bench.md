---
title: "SWE-bench"
type: concept
sources: ["[[sources/devin-ai-software-engineer]]", "[[sources/claude-code-agentic-coding]]", "[[sources/swe-bench-leaderboard-2026]]", "[[sources/morphllm-coding-models-comparison-2026]]", "[[sources/morphllm-codex-vs-claude-code]]"]
related: ["[[concepts/agentic-coding]]", "[[entities/devin-ai]]", "[[entities/claude-code]]", "[[entities/openai-codex]]", "[[entities/swe-bench]]", "[[concepts/ai-code-generation]]"]
last_compiled: 2026-04-05
summary: "Primary benchmark for evaluating LLM software engineering agents on real-world GitHub issues, progressing from 1.96% (2024) to 80.9% (Claude Opus 4.5, 2026) on Verified subset."
---

## Overview

SWE-bench is the dominant benchmark for evaluating [[concepts/agentic-coding]] systems. It tests whether an AI agent can resolve real-world software issues collected from GitHub projects like Django and scikit-learn. Given a codebase and an issue description, the agent must produce a patch that resolves the problem — end-to-end, without human guidance.

SWE-bench has been adopted by all major AI labs (OpenAI, Anthropic, Google, Meta) as the standard measure of software engineering agent capability.

## Variants

| Variant | Description | Size |
|---------|-------------|------|
| SWE-bench (full) | Original dataset | ~2,294 instances |
| SWE-bench Lite | Curated, easier subset | 300 instances |
| SWE-bench Verified | Human-validated for fair evaluation | ~500 instances |
| SWE-bench Pro | Complex, realistic challenges | Varies |
| SWE-bench+ | Enhanced test suites, addresses solution leaks | Varies |

## Performance Timeline

| Date | Agent | Score (Verified) |
|------|-------|-----------------|
| 2024 Q1 | Previous SOTA | 1.96% |
| 2024 Q1 | Devin (Cognition) | 13.86% |
| 2025 | Leading agents | ~75% |
| 2026 Q1 | Claude Opus 4.5 | 80.9% |

The trajectory from 1.96% to 80.9% in roughly two years represents one of the fastest capability improvements in AI benchmarking history.

## Significance

SWE-bench matters because it measures real-world software engineering — not toy problems. Agents must understand large codebases, interpret natural-language issue descriptions, navigate test suites, and produce working patches. This requires the full stack of [[concepts/llm-agent-architecture]]: reasoning, planning, tool use, and code generation.

## Limitations

- Benchmark saturation: as scores approach 100%, the benchmark becomes less discriminating
- Solution leak risks led to SWE-bench+ with enhanced test suites
- Scores don't capture code quality, maintainability, or architectural judgment
- Real software engineering involves requirements gathering, design, and team collaboration — not just bug fixing

## The Scaffold Finding

The most important insight from 2026 benchmarking per [[sources/morphllm-coding-models-comparison-2026]]: identical model weights produce a **22-point performance swing** on SWE-Bench Pro depending on the agent scaffold, IDE, and tooling. This means the engineering around the model -- context management, tool integration, test execution loops, memory management -- matters more than raw model capability.

## Open-Source Convergence

Open-source models are rapidly closing the gap:
- Qwen3-Coder-Next: 70.6% with only 3B active parameters
- MiniMax M2.5: 80.2% as an open-weight model
- DeepSeek V3.2: ~70%

## Sources

- [[sources/devin-ai-software-engineer]] -- Devin's SWE-bench results and the benchmark landscape
- [[sources/claude-code-agentic-coding]] -- Claude Opus 4.5 leading scores
- [[sources/swe-bench-leaderboard-2026]] -- full 2026 leaderboard and evolution analysis
- [[sources/morphllm-coding-models-comparison-2026]] -- scaffold importance finding (22-point swing)
- [[sources/morphllm-codex-vs-claude-code]] -- Codex vs Claude Code benchmark comparison

## Related Concepts

- [[concepts/agentic-coding]] -- what SWE-bench evaluates
- [[concepts/ai-code-generation]] -- the capability being benchmarked
- [[entities/devin-ai]] -- first agent to dramatically improve SWE-bench scores
- [[entities/claude-code]] -- current SWE-bench leader
- [[entities/openai-codex]] -- leading competitor
- [[entities/swe-bench]] -- the benchmark entity page
