---
title: "Source: Detecting Hallucinations with LLM-as-a-Judge"
type: source-summary
source: "[[raw/datadog-hallucination-detection]]"
related: ["[[concepts/hallucination-detection]]", "[[concepts/faithfulness-and-groundedness]]", "[[concepts/llm-as-judge]]", "[[concepts/rag-evaluation]]"]
last_compiled: 2026-04-05
summary: "Datadog's production hallucination detection system: rubric-based LLM-as-a-Judge with structured output, two-stage prompting, and semantic framing achieving 0.81-0.84 F1 on HaluBench/RAGTruth benchmarks."
---

## Key Points

- Three categories of hallucination detection: white-box (token probability, attention mapping), gray-box (semantic entropy), black-box (perturbation, SLM/LLM-as-judge)
- Perturbation-based methods incur 5-10x cost increase through multiple regenerations
- Key insight: "LLMs are better at guided summarization than complex reasoning"
- Rubric-based approach classifies disagreements as contradictions, unsupported claims, or agreements
- Two-stage prompting: unrestricted chain-of-thought, then structured reformatting with smaller LLM
- Achieved 0.844 F1 on HaluBench (n=14,900) and 0.810 F1 on RAGTruth (n=2,700)
- Smallest F1 drop between benchmarks, indicating robustness on harder datasets

## Detailed Summary

Datadog's [[concepts/hallucination-detection]] system represents the state of the art in production-grade faithfulness evaluation for [[concepts/rag-evaluation]] systems.

The article provides the clearest taxonomy of detection approaches. **White-box methods** (token probability, sparse autoencoders, attention mapping) require model internals. **Black-box methods** include perturbation-based approaches (expensive at 5-10x cost), SLM-as-judge (BERT-style, limited reasoning), and LLM-as-judge (best accuracy).

Datadog's innovation is the **rubric-based evaluation** that decomposes hallucination detection into guided summarization steps: identify disagreement claims, extract quotes from context and answer, then classify each disagreement. This avoids asking the LLM to perform complex reasoning in a single step.

Technical enhancements include **finite state machines** to enforce structured JSON output and **semantic framing** (context as "expert advice," answer as "candidate answer") to establish the right asymmetry for faithfulness checking.

## Related Concepts

- [[concepts/hallucination-detection]] — the core technique detailed here
- [[concepts/faithfulness-and-groundedness]] — what the system measures
- [[concepts/llm-as-judge]] — the evaluation paradigm used
- [[concepts/hallucination-contamination]] — the broader risk this mitigates
