---
title: "Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)"
source: "https://eugeneyan.com/writing/llm-evaluators/"
author: "Eugene Yan"
date_published: 2024-06-01
date_ingested: 2026-04-05
tags: [llm-as-judge, evaluation, bias, human-evaluation, LLM-evaluation]
type: article
status: raw
discovered_via: search
---

# Evaluating the Effectiveness of LLM-Evaluators

## Effectiveness Data

- GPT-4 achieved 85% agreement with human experts on MT-Bench (excluding ties), exceeding human-human agreement of 81%
- On Chatbot Arena, GPT-4, GPT-3.5, and Claude-v1 showed 83-87% agreement with human ratings
- Prometheus (finetuned llama-2-chat) achieved 0.897 Pearson correlation with human judgments
- GPT-3.5-turbo achieved only 30-60% recall for identifying inconsistencies despite >95% precision
- Best models achieved 58.5% accuracy distinguishing factual vs. hallucinated summaries
- GPT-4 achieved 0.67 Spearman's ρ for correctness, 0.55 for faithfulness

## Bias Types

- **Position Bias**: GPT-3.5 biased 50% of the time, Claude-v1 biased 70% of the time toward first-position responses
- **Verbosity Bias**: Both Claude-v1 and GPT-3.5 preferred longer response >90% of the time
- **Self-Enhancement Bias**: GPT-4 favored itself with 10% higher win rate; Claude-v1 with 25% higher win rate
- **Superficial Quality Preference**: Finetuned evaluators worse than random guessing on fairness tasks

## Mitigation Strategies

- Chain-of-Thought reasoning improved accuracy
- Few-shot prompting with diverse examples
- Reference-based evaluation more reliable than direct scoring
- Panel of diverse LLMs (PoLL): ensemble of smaller models at 1/7th cost
- Binary classification over Likert scales
- Cohen's κ instead of percentage agreement
- Position switching trick

## Key Frameworks and Tools

- **EvalLM**: Interactive system for iterative prompt refinement; 91.4% logical explanations
- **EvalGen**: Simultaneous criteria and implementation refinement; 0.73 recall
- **Prometheus 2**: Reference-based with fine-grained rubrics; finetuned on 100k GPT-4 examples
- **CriticGPT**: Specialized code-critique model; 80-85% bug detection vs 65-70% for humans
- **PoLL**: Ensemble of command-r, gpt-3.5-turbo, haiku with max voting
- **LM vs LM Cross-Examination**: Multi-turn interaction; 0.75-0.84 recall, 0.82-0.87 precision

## Key Benchmarks

- MT-Bench (80 multi-turn questions across 8 categories)
- Chatbot Arena (3k+ user preference votes)
- SummEval, FRANK, HaluEval (domain-specific)
- LLMBar (fairness assessment)
