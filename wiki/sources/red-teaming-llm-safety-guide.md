---
title: "Source: LLM Red Teaming — Complete Step-By-Step Guide"
type: source-summary
source: "[[raw/red-teaming-llm-safety-guide]]"
related: ["[[concepts/red-teaming]]", "[[concepts/ai-safety]]", "[[concepts/ai-safety-benchmarks]]"]
last_compiled: 2026-04-05
summary: "Confident AI's comprehensive guide to LLM red teaming: 5 vulnerability categories, single/multi-turn attacks, PAIR algorithm, DeepTeam framework, and regulatory requirements."
---

## Key Points
- Five vulnerability domains: Responsible AI, illegal activities, brand image, data privacy, unauthorized access
- Single-turn attacks (prompt injection, encoding) and multi-turn attacks (PAIR, progressive manipulation)
- Distinguishes model-level vs. system-level weaknesses
- PAIR algorithm achieved 50% jailbreak on GPT-4, 73% on Gemini
- DeepTeam: open-source framework with 50+ vulnerability types and 40+ metrics
- EU AI Act and NIST AI RMF both mandate or recommend red teaming

## Detailed Summary

This guide provides a practitioner-focused methodology for LLM red teaming in three phases: baseline attack generation, attack enhancement (encoding, injection, multilingual variants), and execution with metric-based evaluation.

The distinction between model-level weaknesses (bias, hallucinations, jailbreak susceptibility) and system-level weaknesses (API security, tool integrations, prompt template flaws) is critical — many organizations focus only on the model while neglecting the infrastructure.

Key statistics reveal alarming attack surface: prompt injections achieve 86.1% success rate when properly constructed, and the PAIR algorithm (using attacker-target-judge model chains) achieves 50% jailbreak success on GPT-3.5/GPT-4 and 73% on Gemini.

## Related Concepts
- [[concepts/red-teaming]] — the practice described in detail
- [[concepts/ai-safety]] — red teaming as a pillar of AI safety
- [[concepts/ai-governance]] — regulatory mandates for red teaming
- [[concepts/human-in-the-loop]] — human oversight complementing automated testing
