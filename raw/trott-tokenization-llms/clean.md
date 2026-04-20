---
title: "Tokenization in Large Language Models"
source: "https://seantrott.substack.com/p/tokenization-in-large-language-models"
author: "Sean Trott"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [tokenization, llm, morphology, subword]
type: article
status: raw
discovered_via: search
---

# Tokenization in Large Language Models

## Core Concept

Modern LLMs predict "tokens" rather than words. Tokenization is the process of breaking text sequences into discrete components that form the model's vocabulary. Without tokenization, computers only see raw character sequences.

## Three Approaches

**Word-based tokenization:** Simple space-delimited splits produce huge vocabularies but struggle with unknown words and non-space-separated languages.

**Character-based tokenization:** Offers flexibility and handles novel sequences but requires longer context windows and makes learning higher-level patterns harder.

**Subword tokenization:** The modern hybrid approach uses frequent recurring substrings. If a word is extremely frequent, the tokenizer will probably use a single token to represent it. If less frequent, it breaks the word into subwords.

## Byte-Pair Encoding (BPE)

This popular technique starts with individual characters, then iteratively merges the most common adjacent token pairs until reaching a target vocabulary size. Researchers balance lexical coverage against computational efficiency.

## Subwords vs. Morphemes

Critically, subword tokens don't necessarily align with morphemes — the meaningful linguistic units. A word like "racket" might tokenize as "rack" + "##et" despite having one morpheme, while "dogs" remains a single token despite containing two morphemes.

## Morphological Impact on Performance

Research findings are mixed:
- One study found morphological tokenization didn't significantly impact Spanish article-noun agreement tasks
- Contrasting research showed "alien tokenization leads to poorer generalizations compared to morphological tokenization" across BERT, RoBERTa, DeBERTa
- Languages with richer inflectional morphology show different BPE learning patterns than analytic languages

## Character-Level Knowledge in Tokens

Despite tokens being opaque identifiers, models develop implicit character knowledge. Research demonstrates that GPT-J embeddings can identify character presence with 80% accuracy, likely through learning relationships between different tokenizations of the same root word.

## Open Questions

The field still lacks comprehensive analysis of how tokenization choices affect downstream task performance across different languages and contexts.
