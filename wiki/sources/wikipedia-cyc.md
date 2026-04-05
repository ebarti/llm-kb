---
title: "Source: Cyc Knowledge Base (Wikipedia)"
type: source-summary
source: "[[raw/wikipedia-cyc]]"
related: ["[[entities/cyc-project]]", "[[entities/doug-lenat]]", "[[concepts/knowledge-representation]]", "[[concepts/symbolic-ai]]", "[[concepts/ontology]]"]
last_compiled: 2026-04-05
summary: "Comprehensive history of the Cyc project (1984-present): 40 years, $60M+, 24.5M assertions encoding common-sense knowledge in CycL, with microtheories, 1000+ inference engines, and the ongoing debate about its legacy."
---

## Key Points
- Started 1984 at MCC by Doug Lenat; became Cycorp in 1995
- Scale: 1.5M terms, 24.5M assertions, 2,000 person-years of effort by 2017
- CycL language evolved from RLL to higher-order logic
- Microtheories allow internally consistent but globally contradictory knowledge
- Applications: Cleveland Clinic (biomedical), terrorism KB, network security
- "One of the most controversial endeavors of artificial intelligence history"

## Detailed Summary

[[entities/cyc-project]] is AI's longest-running knowledge engineering effort. [[entities/doug-lenat]] started it in 1984 at MCC to counter Japan's fifth-generation computing initiative. The goal: encode the common-sense knowledge that humans take for granted — implicit reasoning about time, causality, physics, and intentions.

CycL, the representation language, evolved from Lenat's earlier RLL work at Stanford. By 1989 it supported higher-order logic. The knowledge base is organized into microtheories, each internally consistent but allowing contradictions across theories (e.g., "the Earth is flat" can be true in a medieval-European microtheory while false in the modern-physics microtheory).

By 2002, the project had consumed $60 million and 600 person-years. By 2017, 1.5 million terms and 24.5 million assertions were encoded by "ontological engineers" who manually analyzed English text for ambiguous pronouns and implied relationships.

OpenCyc was released in 2002 (6,000 concepts) and grew to 239,000 concepts by 2012, but was shut down in 2017. ResearchCyc offered a richer version for academic use.

Pedro Domingos called it a "catastrophic failure"; Gary Marcus saw it as a fundamentally different approach from deep learning. Lenat's final paper before his 2023 death proposed integrating Cyc's auditable reasoning with LLMs' fluency — a vision that mirrors the broader [[concepts/neural-symbolic-integration]] trend.

## Related Concepts
- [[concepts/knowledge-representation]] — Cyc is the ultimate KR project
- [[concepts/ontology]] — Cyc's ontology is among the largest ever built
- [[concepts/symbolic-ai]] — Cyc represents the symbolic approach's most extreme ambition
- [[concepts/neural-symbolic-integration]] — Lenat's final proposal
- [[concepts/cheap-ontology]] — the LLM-era alternative to Cyc's approach
