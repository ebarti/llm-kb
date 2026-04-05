---
title: "Neural-Symbolic Integration"
type: concept
sources: ["[[sources/wikipedia-symbolic-ai]]", "[[sources/llm-enhanced-knowledge-representation-survey]]", "[[sources/outsiderart-cyc-forgotten-ai]]", "[[sources/llms-as-reliable-knowledge-bases]]"]
related: ["[[concepts/symbolic-vs-connectionist]]", "[[concepts/symbolic-ai]]", "[[concepts/knowledge-representation]]", "[[concepts/knowledge-graph]]", "[[concepts/llm-knowledge-base]]"]
last_compiled: 2026-04-05
summary: "The emerging paradigm combining symbolic reasoning (explainable, compositional, precise) with neural networks (learnable, perceptual, scalable) — six architectures catalogued, from language models with symbolic tokens to neural models calling symbolic engines."
---

## Overview

Neural-symbolic integration (also called neuro-symbolic AI) is the research program combining the strengths of [[concepts/symbolic-ai]] (explainability, compositionality, formal reasoning) with neural networks (learning from data, handling perception, scaling with compute). It represents the resolution of the [[concepts/symbolic-vs-connectionist]] debate toward complementarity.

## Six Integration Architectures

Research identifies six patterns for combining symbolic and neural components:

| Architecture | Pattern | Example |
|-------------|---------|---------|
| Symbolic\<Neural\> | Neural components within symbolic framework | BERT, GPT-3 using symbolic tokens |
| Symbolic[Neural] | Symbolic search directing neural evaluation | AlphaGo's Monte Carlo tree search + neural networks |
| Neural\|Symbolic | Neural perception feeding symbolic reasoning | Vision systems producing logical descriptions |
| Neural:Symbolic->Neural | Symbolic systems generating neural training data | Knowledge-guided data augmentation |
| Neural_{Symbolic} | Networks constructed from logical rules | Logic tensor networks |
| Neural[Symbolic] | Neural models calling symbolic engines | LLMs invoking calculators, databases, provers |

## Key Motivations

1. **LLM limitations**: Only ~32% consistently correct as knowledge bases; hallucinate confidently
2. **Symbolic limitations**: Knowledge acquisition bottleneck, brittleness, cannot handle perception
3. **Complementary strengths**: Neural systems learn what symbolic systems cannot specify; symbolic systems verify what neural systems cannot guarantee

## Modern Examples

- **LLM + Knowledge Graph**: Survey evidence shows LLM-enhanced KG embeddings outperform either approach alone, especially on zero-shot and low-resource scenarios
- **Cyc + LLM**: [[entities/doug-lenat]]'s final vision: Cyc's auditable reasoning chains + LLM fluency and breadth
- **LLM-maintained wiki** ([[concepts/llm-knowledge-base]]): Structured markdown (symbolic) + LLM compilation and reasoning (neural)
- **Tool-using LLMs**: GPT-4 calling calculators, code interpreters, and search engines (Neural[Symbolic] architecture)
- **AlphaProof / AlphaGeometry**: Neural systems guided by formal mathematical reasoning

## The LLM-KB Connection

[[concepts/llm-knowledge-base]] systems are a practical neural-symbolic architecture: the wiki provides structured, explicit, auditable knowledge (the symbolic component), while the LLM provides compilation, reasoning, and natural language interaction (the neural component). This directly addresses the finding from [[sources/llms-as-reliable-knowledge-bases]] that pure parametric knowledge is unreliable.

## Sources
- [[sources/wikipedia-symbolic-ai]] — six architecture taxonomy
- [[sources/llm-enhanced-knowledge-representation-survey]] — LLM+KG integration evidence
- [[sources/outsiderart-cyc-forgotten-ai]] — Lenat's Cyc+LLM vision
- [[sources/llms-as-reliable-knowledge-bases]] — evidence motivating hybrid approaches

## Related Concepts
- [[concepts/symbolic-vs-connectionist]] — the debate this resolves
- [[concepts/symbolic-ai]] — one input to integration
- [[concepts/knowledge-graph]] — a common symbolic component
- [[concepts/llm-knowledge-base]] — a practical neural-symbolic system
- [[concepts/llms-as-knowledge-bases]] — the limitation motivating integration
