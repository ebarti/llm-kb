---
title: "LLM Hallucination"
type: concept
sources: ["[[sources/llm-hallucination-comprehensive-survey]]", "[[sources/lakera-llm-hallucinations-2026]]", "[[sources/international-ai-safety-report-2026]]"]
related: ["[[concepts/hallucination-contamination]]", "[[concepts/ai-content-verification]]", "[[concepts/grounding-and-faithfulness]]", "[[concepts/calibrated-uncertainty]]", "[[concepts/ai-safety]]", "[[concepts/data-quality-bottleneck]]"]
last_compiled: 2026-04-05
summary: "When LLMs generate fluent but factually incorrect or unsupported text — classified by type (factuality vs. faithfulness, intrinsic vs. extrinsic), caused across the full development lifecycle, and addressed through detection and mitigation taxonomies."
---

## Overview

LLM hallucination is the phenomenon where language models generate text that is syntactically fluent and superficially plausible but factually incorrect or unsupported by evidence. Unlike creative fiction (which is intentional), hallucinations are unintended fabrications that the model presents as factual. This is the **single most important challenge** for any system that uses LLMs to generate knowledge, including LLM-authored wikis.

## Classification

### By Relationship to Source
- **Intrinsic hallucinations**: Directly contradict source documents or input context
- **Extrinsic hallucinations**: Introduce claims that cannot be verified from any provided source — may be true or false, but are ungrounded

### By Error Type
- **Factuality hallucinations**: Divergence from real-world facts (contradiction or fabrication)
- **Faithfulness hallucinations**: Drift from the original input, including instruction inconsistencies, context distortion, and logical errors

([[sources/llm-hallucination-comprehensive-survey]])

## Root Causes

The 2025 comprehensive survey identifies causes at every stage of the LLM lifecycle:

### Data Curation
- **Biased training data** reflecting societal imbalances
- **Imitative falsehoods**: Models reproducing misinformation present in training data
- **Knowledge conflicts**: Contradictory information from multiple sources
- **Temporal misalignment**: Outdated facts beyond training cutoff
- **Long-tail knowledge**: Underrepresentation of rare entities and domains

### Architecture
- **Attention limitations**: Soft attention distributes focus diffusely over long sequences
- **MLE objective**: Maximum likelihood estimation lacks factual consistency penalties
- **Autoregressive generation**: Unidirectional context misses bidirectional signals

### Training
- **Exposure bias**: Teacher forcing during training creates a gap with autoregressive inference
- **Cascade effects**: Early token errors compound through the rest of generation
- **Sycophantic behavior**: Fine-tuning incentivizes generating responses evaluators approve regardless of accuracy
- **Capability misalignment**: Alignment training encourages definitive answers even when the model lacks sufficient knowledge

### Inference
- **Sampling randomness**: Top-k and nucleus sampling increase selection of low-probability tokens
- **Ambiguous prompts**: Vague inputs lead the model to rely on priors rather than user intent
- **Softmax bottleneck**: Inability to represent multiple equally probable continuations

### Fundamental Reframing (2025)
OpenAI's 2025 research reframes hallucination as **incentive-driven guessing**: "Next-token objectives and common leaderboards reward confident guessing over calibrated uncertainty." Models learn to bluff when uncertain rather than abstain ([[sources/lakera-llm-hallucinations-2026]]).

## Detection Methods

Five primary detection families have emerged:

| Approach | How It Works | Strengths | Limitations |
|----------|-------------|-----------|-------------|
| **Retrieval-Based** | Verify claims against external knowledge (FAVA, KnowHalu) | Direct factuality verification | Quality-limited by retrieved docs |
| **Uncertainty-Based** | Flag low-confidence outputs (semantic entropy, BTPROP) | Works without external knowledge | Over-predicts; misses confident errors |
| **Embedding-Based** | Measure semantic similarity shifts (HalluShift) | Captures subtle distributional changes | Degrades on out-of-domain data |
| **Learning-Based** | Trained detectors (ExHalder, PRISM, Lookback Lens) | Can capture complex patterns | Requires labeled data; poor generalization |
| **Self-Consistency** | Generate multiple responses, check agreement (SelfCheckGPT, MetaQA) | Works on closed-source models | Fails with consistently wrong outputs |

Notable detection tools:
- **CLAP** (Cross-Layer Attention Probing): Real-time detection via lightweight classifiers on model activations
- **MetaQA**: Prompt mutations revealing inconsistencies in closed-source models

([[sources/llm-hallucination-comprehensive-survey]], [[sources/lakera-llm-hallucinations-2026]])

## Mitigation Strategies

### Prompt-Based
- Chain-of-Thought reasoning for logical coherence
- Explicit instructions constraining response scope
- In-context learning with verified examples

### Retrieval-Based
- **RAG** (Retrieval-Augmented Generation): Ground responses in retrieved documents
- **RAG-HAT**: Hallucination-aware tuning with detection/rewriting/mitigation
- **Knowledge graph grounding**: ERNIE 3.0, KGLM, FOLK for structured verification
- See [[concepts/grounding-and-faithfulness]] for detailed treatment

### Reasoning-Based
- **Chain-of-Verification (CoV)**: Verification steps following initial generation
- **Self-consistency**: Majority voting among multiple reasoning paths
- **Iterative refinement**: Multi-pass correction with explicit error categorization

### Model-Centric
- **Calibration-aware rewards**: Penalize overconfidence; credit uncertainty signaling
- **Targeted finetuning**: Training on hallucination-prone scenarios (90-96% reduction)
- **Refusal training**: Steer models to abstain when knowledge is insufficient
- **Contrastive learning**: Differentiating faithful from hallucinated content

### Key Finding
No single approach eliminates hallucination. The most effective strategy combines multiple techniques: retrieval with reasoning, learning with uncertainty quantification ([[sources/llm-hallucination-comprehensive-survey]]).

## Benchmarks

| Benchmark | Focus | Year |
|-----------|-------|------|
| TruthfulQA | Factual accuracy across domains | 2022 |
| HaluEval | Hallucination evaluation | 2023 |
| Mu-SHROOM | Multilingual hallucination (SemEval) | 2025 |
| CCHall | Multimodal reasoning hallucinations (ACL) | 2025 |
| REFIND | Span-level verification (SemEval) | 2025 |

## Real-World Impact
- **Mata v. Avianca**: Lawyer sanctioned for submitting fabricated ChatGPT citations to court
- **Medical domain**: GPT-4o hallucination rate of 53%, reduced to 23% with prompt-based mitigation (npj Digital Medicine, 2025)
- **Consumer apps**: ~1.75% of mobile-app complaints involve hallucination-like errors

## Relevance to LLM Knowledge Bases

Hallucination is the existential risk for LLM-authored wikis. See [[concepts/hallucination-contamination]] for how errors propagate. Mitigation for knowledge bases requires:

1. **Source attribution**: Every claim traces to `raw/` source files
2. **[[concepts/ai-content-verification]]**: Automated and human verification pipelines
3. **[[concepts/calibrated-uncertainty]]**: The system should signal doubt rather than confabulate
4. **[[concepts/linting-and-health-checks]]**: Regular scans for contradictions and unsourced claims

## Sources
- [[sources/llm-hallucination-comprehensive-survey]] — exhaustive taxonomy of causes, detection, and mitigation
- [[sources/lakera-llm-hallucinations-2026]] — practitioner guide with CLAP, MetaQA, and calibration shift
- [[sources/international-ai-safety-report-2026]] — performance described as "jagged" with persistent false statements

## Related Concepts
- [[concepts/hallucination-contamination]] — propagation of hallucinations through knowledge bases
- [[concepts/ai-content-verification]] — methods for verifying AI-generated content
- [[concepts/grounding-and-faithfulness]] — techniques for anchoring outputs to source material
- [[concepts/calibrated-uncertainty]] — the new goal replacing zero-hallucination targets
- [[concepts/data-quality-bottleneck]] — garbage in, garbage out
- [[concepts/ai-safety]] — hallucination as a core safety concern
