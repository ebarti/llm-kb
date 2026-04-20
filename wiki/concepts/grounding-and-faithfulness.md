---
title: "Grounding and Faithfulness"
type: concept
sources: ["[[sources/llm-hallucination-comprehensive-survey]]", "[[sources/lakera-llm-hallucinations-2026]]"]
related: ["[[concepts/llm-hallucination]]", "[[concepts/ai-content-verification]]", "[[concepts/rag-vs-index-based-retrieval]]", "[[concepts/knowledge-graph]]", "[[concepts/hallucination-contamination]]"]
last_compiled: 2026-04-05
summary: "Techniques for anchoring LLM outputs to source material and external knowledge — RAG, knowledge graph integration, span-level attribution, and faithfulness checking — as the primary defense against hallucination."
---

## Overview

Grounding refers to the practice of anchoring LLM outputs to verifiable external information rather than relying solely on parametric knowledge (information stored in model weights). Faithfulness measures how well the generated output reflects the provided source material without distortion, omission, or fabrication.

Together, grounding and faithfulness form the primary technical defense against [[concepts/llm-hallucination]]. The core principle: **decouple knowledge from model weights** by retrieving facts from external, verifiable sources and constraining generation to those facts.

## Key Techniques

### Retrieval-Augmented Generation (RAG)
The dominant grounding approach. RAG retrieves relevant documents from an external knowledge base and injects them into the prompt context. The model generates responses constrained by the retrieved information rather than relying on probabilistic guessing from training data.

**Limitations**: RAG does not fully eliminate hallucinations. LLMs often introduce details unsupported by retrieved contexts, misrepresent information, or generate contradictions even when grounded. The effectiveness of retrieval-based approaches is fundamentally limited by the quality of retrieved documents ([[sources/llm-hallucination-comprehensive-survey]]).

See [[concepts/rag-vs-index-based-retrieval]] for scale considerations.

### Knowledge Graph Grounding
Using structured knowledge graphs to provide verified facts:

| System | Approach | Stage |
|--------|----------|-------|
| **ERNIE 3.0** | Entity linking during pre-training | Pre-training |
| **KGLM** | Triple integration | Training |
| **KG-Adapter** | Adapter modules for KG injection | Fine-tuning |
| **FOLK** | Fact-verification with explanations | Validation |
| **KAPING** | Zero-shot QA with KG context | Inference |
| **KGR** | Autonomous graph retrofitting | Inference |

Knowledge graphs offer more structured grounding than text retrieval but require maintained graph infrastructure. See [[concepts/knowledge-graph]] for system comparisons.

### Span-Level Attribution
Rather than document-level grounding, span-level attribution matches each generated claim to specific passages in source documents. FAVA and the REFIND benchmark (SemEval 2025) implement fine-grained attribution ([[sources/llm-hallucination-comprehensive-survey]]).

For LLM knowledge bases, this translates to: every factual claim in a wiki article should link to a specific section in a `raw/` source file.

### Faithfulness Checking
Post-generation verification comparing each claim against retrieved context. The most reliable grounding approach according to practitioners: "compare each claim in the answer against the retrieved context" ([[sources/llm-hallucination-comprehensive-survey]]).

### RAG-HAT (Hallucination-Aware Tuning)
A three-stage approach: detect hallucinated spans, rewrite them with grounded alternatives, and train the model to avoid similar hallucinations. Combines grounding with active learning from mistakes.

### Contextual Guardrails
Modern guardrails check whether model responses are factually grounded in provided sources in real time. These act as a last-line defense, rejecting responses that cannot be traced to source material.

## Grounding in LLM Knowledge Bases

For an LLM-maintained wiki, grounding operates at two levels:

### Compilation Grounding
When the LLM compiles wiki articles from `raw/` source files, every claim should trace to specific source passages. The compilation pipeline itself should enforce attribution.

### Query-Time Grounding
When answering questions, the LLM navigates the wiki via indexes and summaries, reads relevant articles, and synthesizes answers. Grounding means citing specific wiki articles with wikilinks rather than generating from parametric knowledge.

### The Grounding Paradox for AI Wikis
An LLM wiki faces a unique challenge: the "ground truth" documents were themselves processed by an LLM. If the compilation step introduces errors, grounding query-time answers in those wiki articles merely propagates the error with a citation ([[concepts/hallucination-contamination]]).

The defense is multi-layered:
1. `raw/` files are immutable source-of-truth
2. Wiki articles maintain provenance links to `raw/`
3. [[concepts/linting-and-health-checks]] verify wiki claims against raw sources
4. [[concepts/ai-content-verification]] catches drift over time

## Sources
- [[sources/llm-hallucination-comprehensive-survey]] — comprehensive taxonomy of grounding techniques
- [[sources/lakera-llm-hallucinations-2026]] — RAG with verification and span-checking in practice

## Related Concepts
- [[concepts/llm-hallucination]] — the problem grounding addresses
- [[concepts/ai-content-verification]] — verification as complement to grounding
- [[concepts/rag-vs-index-based-retrieval]] — retrieval infrastructure choices
- [[concepts/knowledge-graph]] — structured grounding alternative to text retrieval
- [[concepts/hallucination-contamination]] — what happens when grounding fails in a KB
