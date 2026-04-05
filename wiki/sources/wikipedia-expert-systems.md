---
title: "Source: Expert Systems (Wikipedia)"
type: source-summary
source: "[[raw/wikipedia-expert-systems]]"
related: ["[[concepts/expert-systems]]", "[[concepts/knowledge-representation]]", "[[entities/edward-feigenbaum]]", "[[concepts/symbolic-ai]]"]
last_compiled: 2026-04-05
summary: "History of expert systems from 1965 Stanford origins through the 1980s commercial boom to their absorption into modern business rules engines, covering DENDRAL, MYCIN, XCON, and the knowledge acquisition bottleneck."
---

## Key Points
- Edward Feigenbaum's 1965 Stanford Heuristic Programming Project founded the field
- Key insight: "intelligent systems derive their power from the knowledge they possess rather than from the specific formalisms"
- 1980s boom saw two-thirds of Fortune 500 adopt expert systems; followed by bust due to brittleness and maintenance costs
- The knowledge acquisition problem (getting experts to encode rules) was never fully solved
- Expert systems didn't die — they were absorbed into business rules management systems (SAP, Oracle)

## Detailed Summary

The article covers the full lifecycle of [[concepts/expert-systems]]. [[entities/edward-feigenbaum]] formally introduced them around 1965, recognizing that domain knowledge matters more than inference mechanisms. Landmark systems proved the concept: DENDRAL identified organic molecules (late 1960s), MYCIN diagnosed bacteremia with 450 rules matching expert performance, and R1/XCON configured DEC VAX computers saving $25M/year.

The 1980s boom saw expert system consultancies (Teknowledge, Intellicorp) go public with soaring valuations. Two-thirds of Fortune 500 companies deployed the technology. The IBM PC (1981) democratized access, enabling organizations to bypass IT departments.

The architecture comprised a knowledge base (facts and rules) and an inference engine (forward and backward chaining). Later systems added truth maintenance, hypothetical reasoning, uncertainty handling, and ontology-based classification.

The bust came from multiple directions: the knowledge acquisition problem made maintenance prohibitively expensive, Lisp's interpreted performance was inadequate, specialized hardware (Lisp machines) was incompatible with corporate IT, and rule consistency verification at scale was NP-complete.

European AI took a different path, focusing on Prolog-based systems rather than Lisp/production rules.

By the 2000s, the technology resurfaced as "business rules management systems" integrated into enterprise platforms — the ultimate vindication of the core idea, even if the original packaging failed.

## Notable Quotes
> "Intelligent systems derive their power from the knowledge they possess rather than from the specific formalisms and inference schemes they use." — Feigenbaum

## Related Concepts
- [[concepts/expert-systems]] — the central topic
- [[concepts/knowledge-representation]] — the underlying discipline
- [[concepts/symbolic-ai]] — the paradigm expert systems belong to
- [[concepts/cheap-ontology]] — modern LLM-based approach to the same problem expert systems tried to solve
