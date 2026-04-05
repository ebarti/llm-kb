---
title: "Single-Agent vs. Multi-Agent Knowledge Pipelines"
type: comparison
subjects: ["[[concepts/llm-knowledge-base]]", "[[concepts/multi-agent-systems]]"]
sources: ["[[sources/karpathy-llm-knowledge-bases]]", "[[sources/karma-multi-agent-knowledge-graph]]", "[[sources/storm-automated-wiki-creation]]"]
last_compiled: 2026-04-06
summary: "Comparing Karpathy's single-LLM approach (one model per phase) with multi-agent architectures (KARMA's 9 agents, STORM's perspective agents) for knowledge extraction and synthesis."
---

## Overview

LLM-powered knowledge systems can be built with a single LLM handling all tasks sequentially, or with multiple specialized agents collaborating on different phases of the pipeline. Karpathy's workflow uses a single LLM in each phase (compilation, Q&A, linting), while [[entities/karma]] employs nine specialized agents and [[entities/storm]] uses perspective-simulating agents. This comparison examines the tradeoffs between architectural simplicity and task-specific specialization.

## Comparison Table

| Dimension | Single-Agent (Karpathy) | Multi-Agent (KARMA/STORM) |
|-----------|------------------------|--------------------------|
| Architecture | One LLM per phase | Specialized agents per task |
| Complexity | Low | High |
| Conflict detection | Implicit (linting pass) | Explicit (agents challenge each other) |
| Quality ceiling | Limited by single model's capability | Higher (specialization + verification) |
| Scale | Personal (~100 articles) | Research (1000s of papers) |
| Schema enforcement | Convention-based (LLM prompts) | Formal (dedicated schema validator agent) |
| Cost per run | Lower (fewer API calls) | Higher (9x agents, multi-turn conversations) |
| Latency | Lower | Higher (sequential agent handoffs) |
| Error isolation | Difficult (errors propagate silently) | Better (verifier agent catches errors) |
| Infrastructure | Minimal (LLM API + files) | Complex (agent orchestration framework) |
| Best for | Personal knowledge synthesis | Scientific literature, formal KGs |

## Detailed Analysis

**The simplicity advantage**: Karpathy's single-agent approach works because personal-scale knowledge bases (~100 articles) do not require the sophistication of multi-agent pipelines. A single capable LLM can parse documents, extract concepts, create cross-links, and maintain indexes without the coordination overhead of multiple agents. The simplicity also means fewer failure modes: no agent handoff errors, no message format incompatibilities, no orchestration framework to maintain.

**The quality advantage**: KARMA's nine agents achieve 83.1% accuracy and 18.6% conflict reduction specifically because distinct agents independently assess the same facts. When the entity discoverer and the verifier disagree, that disagreement is a signal worth surfacing. In a single-agent system, the same model that generates a claim also evaluates it -- a weaker form of self-verification. Multi-agent conflict detection is architecturally superior for high-stakes knowledge extraction.

**STORM's perspective innovation**: Rather than dividing by task (as KARMA does), STORM divides by perspective. Each agent role-plays a different expert viewpoint, asking different questions about the same topic. This produces more comprehensive coverage because it simulates the diversity of human research approaches. A single agent, no matter how capable, tends to explore from a single perspective.

**The coordination cost**: Multi-agent systems require orchestration frameworks, message passing protocols, and careful prompt engineering for each agent role. KARMA's nine agents must maintain consistent schema understanding across all roles. This coordination overhead is justified at research scale (processing 1,200 PubMed papers) but would be counterproductive for a personal wiki of 100 articles.

## When to Use Each

**Use single-agent when:**
- Knowledge base is personal scale (under ~400 articles)
- Infrastructure simplicity is a priority
- The compilation task does not require formal schema validation
- Budget and latency constraints favor fewer API calls
- The human owner performs manual quality checks

**Use multi-agent when:**
- Processing thousands of documents requiring formal extraction
- Conflict detection and resolution are critical (scientific or medical domains)
- Multiple perspectives are needed for balanced coverage
- Schema adherence must be enforced programmatically
- The quality ceiling of single-agent extraction is insufficient

## Sources

- [[sources/karpathy-llm-knowledge-bases]] -- single-LLM approach to personal knowledge base management
- [[sources/karma-multi-agent-knowledge-graph]] -- nine-agent KG enrichment pipeline (NeurIPS 2025)
- [[sources/storm-automated-wiki-creation]] -- perspective-simulating agents for article generation
