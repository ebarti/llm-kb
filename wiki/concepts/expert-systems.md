---
title: "Expert Systems"
type: concept
sources: ["[[sources/wikipedia-expert-systems]]", "[[sources/wikipedia-symbolic-ai]]", "[[sources/wikipedia-knowledge-representation-reasoning]]"]
related: ["[[concepts/knowledge-representation]]", "[[concepts/symbolic-ai]]", "[[entities/edward-feigenbaum]]", "[[concepts/cheap-ontology]]", "[[concepts/llm-knowledge-base]]"]
last_compiled: 2026-04-05
summary: "Rule-based AI systems (1965-1990s) that encoded domain expertise as if-then rules in a knowledge base paired with an inference engine — the first commercially successful AI, ultimately killed by the knowledge acquisition bottleneck."
---

## Overview

Expert systems were the first commercially successful form of artificial intelligence, dominating AI from the late 1970s through the late 1980s. They encoded human domain expertise as production rules (if-then statements) in a knowledge base, paired with an inference engine that applied those rules to derive conclusions.

Their rise, success, and fall represent one of AI's most instructive episodes — and their legacy directly informs why modern [[concepts/llm-knowledge-base]] systems exist.

## Architecture

An expert system has two core components:

1. **Knowledge Base**: A repository of facts and rules representing domain expertise. Rules take the form of if-then productions (e.g., "IF patient has fever AND positive blood culture THEN suspect bacteremia").

2. **Inference Engine**: Applies rules to known facts via:
   - **Forward chaining** (data-driven): When conditions are met, fire the rule and assert conclusions
   - **Backward chaining** (goal-driven): Start from a hypothesis and work backward to find supporting facts

Later systems added truth maintenance (tracking rule dependencies), hypothetical reasoning, uncertainty handling (probability, fuzzy logic), and ontology-based classification.

## Key Insight

[[entities/edward-feigenbaum]]'s foundational observation: "Intelligent systems derive their power from the knowledge they possess rather than from the specific formalisms and inference schemes they use." This "knowledge is power" principle drove the entire expert systems movement — and remains true in the LLM era, where data quality trumps model scale ([[concepts/data-quality-bottleneck]]).

## Landmark Systems

| System | Domain | Achievement |
|--------|--------|-------------|
| DENDRAL | Chemistry | Identified organic molecules from mass spectrometry (late 1960s) |
| MYCIN | Medicine | Diagnosed bacteremia with 450 rules, matched expert performance |
| R1/XCON | Computing | Configured DEC VAX computers, saved $25M/year |
| SID | Hardware design | Generated 93% of VAX 9000 CPU logic gates (1982) |
| GARVAN-ES1 | Endocrinology | One of first expert systems in daily clinical use |
| REACTOR | Nuclear | Nuclear plant monitoring |

## The Boom (1980s)

Two-thirds of Fortune 500 companies deployed expert systems. Consultancies (Teknowledge, Intellicorp, Inference Corporation) went public with soaring valuations. Universities created expert system courses. The IBM PC (1981) democratized access.

## The Bust (Late 1980s-1990s)

Multiple factors converged:

- **Knowledge acquisition bottleneck**: Getting domain experts to articulate and encode their knowledge as rules was chronically expensive and time-consuming. This was never solved.
- **Brittleness**: Systems could not extrapolate beyond their explicit rules. Novel situations caused failures.
- **Maintenance cost**: Updating large rule bases was prohibitively expensive. Consistency verification of thousands of rules was NP-complete.
- **Integration problems**: Lisp and Prolog were incompatible with corporate IT infrastructure.
- **Hardware obsolescence**: Specialized Lisp machines (Symbolics, LMI) couldn't compete with general-purpose Unix workstations.

## Legacy

Expert systems didn't truly die — they were absorbed. By the 2000s, the core ideas reappeared as:
- **Business rules management systems** (SAP, Oracle, Siebel)
- **Clinical decision support systems** in healthcare
- **Fraud detection engines** in finance

The knowledge acquisition bottleneck they exposed is precisely what [[concepts/llm-knowledge-base]] systems aim to solve through automated extraction and compilation.

## Connection to Modern LLM Knowledge Bases

| Expert Systems | LLM Knowledge Bases |
|---------------|---------------------|
| Manual rule encoding by knowledge engineers | Automated extraction + LLM compilation |
| Formal if-then rules | Natural language in markdown |
| Inference engine (forward/backward chaining) | LLM reasoning over context |
| Knowledge acquisition bottleneck | Solved by web search + LLM processing |
| Brittle to novel situations | LLMs generalize from training data |
| Explainable reasoning chains | Source citations via wikilinks |

## Sources
- [[sources/wikipedia-expert-systems]] — comprehensive history
- [[sources/wikipedia-symbolic-ai]] — places expert systems in the symbolic AI timeline
- [[sources/wikipedia-knowledge-representation-reasoning]] — theoretical foundations

## Related Concepts
- [[concepts/knowledge-representation]] — the discipline expert systems applied
- [[concepts/symbolic-ai]] — the paradigm they belong to
- [[concepts/cheap-ontology]] — the LLM-era alternative
- [[concepts/llm-knowledge-base]] — modern successor that solves the knowledge acquisition problem
- [[concepts/data-quality-bottleneck]] — the modern version of the knowledge acquisition challenge
