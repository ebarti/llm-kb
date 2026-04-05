---
title: "Source: Let's Build the GPT Tokenizer — Karpathy minbpe"
type: source-summary
source: "[[raw/karpathy-minbpe-lecture]]"
related: ["[[concepts/byte-pair-encoding]]", "[[concepts/tokenization]]", "[[entities/andrej-karpathy]]", "[[entities/minbpe]]"]
last_compiled: 2026-04-05
summary: "Karpathy's 2h13m lecture building a GPT tokenizer from scratch, demonstrating BPE and cataloging LLM problems (spelling, arithmetic, non-English) that trace back to tokenization."
---

## Key Points

- Many apparent LLM limitations actually stem from tokenization, not neural architecture flaws
- GPT-2 popularized byte-level BPE with 50,257 tokens and 1,024 context length
- Numbers are split arbitrarily (677 → " 6"+"77" but 127 stays whole)
- Whitespace significantly affects tokenization but remains invisible
- LLM problems traced to tokenization: spelling failures, string reversal, arithmetic struggles, poor non-English performance, unexpected halting at special tokens
- The minbpe repository provides minimal, clean BPE code with train/encode/decode functions
- Karpathy suggests someone should ideally find a way to delete tokenization entirely

## Detailed Summary

[[entities/andrej-karpathy]]'s lecture is the most widely-cited educational resource on [[concepts/tokenization]]. Starting from naive character-level encoding (65 unique characters in Shakespeare), he builds up to [[concepts/byte-pair-encoding]], the algorithm behind GPT-2/3/4. The most valuable contribution is his systematic catalog of LLM problems attributable to tokenization: models struggle with spelling because they don't see individual characters; arithmetic fails because numbers are tokenized inconsistently; non-English languages get fragmented into more tokens; and special tokens like "<|endoftext|>" can cause unexpected halting. The accompanying [[entities/minbpe]] repository provides the cleanest reference implementation. Karpathy's conclusion that tokenization should ideally be eliminated foreshadows work on [[concepts/byte-level-models]].

## Notable Quotes

> "Many weird behaviors and problems of LLMs trace back to tokenization."

## Related Concepts

- [[concepts/byte-pair-encoding]] — the algorithm built from scratch
- [[concepts/tokenization]] — the process critiqued as a necessary evil
- [[concepts/byte-level-models]] — the direction Karpathy's critique points toward
- [[entities/andrej-karpathy]] — the lecturer
