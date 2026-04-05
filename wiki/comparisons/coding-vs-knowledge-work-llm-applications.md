---
title: "Coding vs Knowledge Work LLM Applications"
type: comparison
subjects: ["[[concepts/agentic-coding]]", "[[concepts/llm-applications-beyond-code]]"]
sources: ["[[sources/assemblyai-llm-use-cases-2026]]", "[[sources/microsoft-research-ai-2026-frontiers]]", "[[sources/gavel-law-firm-llm-guide-2026]]"]
last_compiled: 2026-04-05
summary: "Comparing LLM applications in code generation vs. knowledge work domains (writing, research, law, medicine, education) — shared patterns, different maturity levels, and the convergence toward knowledge orchestration."
---

## Overview

Karpathy's observation that his token throughput shifted "from manipulating code to manipulating knowledge" points to a fundamental question: how do LLM applications in code generation compare to applications in other knowledge domains? This comparison maps the shared patterns and divergences.

## Comparison Table

| Dimension | Code Generation | Knowledge Work (Writing, Research, Law, Medicine, Education) |
|-----------|----------------|--------------------------------------------------------------|
| **Maturity** | Most mature; SWE-bench 80.9% (Claude Opus 4.5) | Rapidly growing; varies by domain |
| **Benchmark** | SWE-bench, HumanEval, MBPP | USMLE (93.1%), LegalBench, LM Arena Creative Writing |
| **Adoption rate** | Very high among developers | Legal: 19% to 79% in one year; healthcare growing |
| **Output verifiability** | Tests pass/fail; CI/CD validates | Domain expert review required; harder to automate |
| **Hallucination risk** | Code either works or doesn't (mostly) | High-stakes: medical errors, legal fabrications |
| **Human role shift** | Coder to curator/reviewer | Drafter to curator/reviewer (identical pattern) |
| **Agentic maturity** | Claude Code, Devin, Cursor | Claude Cowork (Jan 2026) — first non-coding agent |
| **Revenue** | Claude Code: $2.5B (2026) | Emerging but growing fast |
| **Evaluation** | Automated (tests, linters, benchmarks) | Requires human judgment; some automated metrics |
| **Self-correction** | Compile errors feed back to LLM | Self-correction loops (mergen: +52.5%) |

## Shared Patterns

Both domains follow the same three-phase adoption:

1. **Automation**: LLM handles routine tasks (boilerplate code / document drafts)
2. **Augmentation**: Human-AI collaboration on complex reasoning (architecture / diagnosis)
3. **Orchestration**: Multi-agent systems managing workflows (CI/CD agents / clinical agents)

Both domains see the same human role transformation: from producing output to curating, reviewing, and directing AI-generated output. The [[concepts/post-code-ai-workflow]] applies universally.

## Key Differences

### Verifiability
Code has a natural verification loop: tests pass or fail. Knowledge work output (legal briefs, medical diagnoses, research papers) requires human expert review, making quality assurance harder to automate.

### Stakes
A bug in code is usually fixable. A hallucinated medical diagnosis or fabricated legal citation can cause irreversible harm. This drives the different regulatory postures: code generation is largely unregulated, while medical AI may require SaMD clearance.

### The Correctness Gap
The mergen study shows that even for code (data analysis), correctness drops from 88% (simple tasks) to 0% (complex tasks). In knowledge domains without automated testing, this gap is invisible — making it potentially more dangerous.

### Diversity Cost
The [[concepts/ai-creativity-paradox]] is more significant in creative and analytical domains than in code, where functional correctness matters more than stylistic diversity.

## When to Use Each

- **Code generation**: When output can be automatically tested and iterated
- **Knowledge work LLMs**: When human expert review is available and the domain benefits from scale/speed
- **Both**: When the task involves translating knowledge into structured artifacts (the [[concepts/llm-knowledge-base]] sweet spot)

## The Convergence

Both code generation and knowledge work are converging on the same infrastructure: knowledge bases, agentic workflows, and multi-agent orchestration. The [[concepts/llm-knowledge-base]] is the shared substrate — whether the knowledge being manipulated is about software architecture or medical protocols.

## Sources

- [[sources/assemblyai-llm-use-cases-2026]] — seven enterprise use cases across domains
- [[sources/microsoft-research-ai-2026-frontiers]] — convergence of AI across all domains
- [[sources/gavel-law-firm-llm-guide-2026]] — legal adoption parallels developer adoption
