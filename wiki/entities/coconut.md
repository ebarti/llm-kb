---
title: "COCONUT (Chain of Continuous Thought)"
type: entity
entity_type: paper
sources: ["[[sources/hao-coconut-latent-reasoning]]"]
related: ["[[concepts/latent-reasoning]]", "[[concepts/chain-of-thought]]", "[[concepts/test-time-compute]]"]
last_compiled: 2026-04-05
summary: "Meta research paper introducing latent reasoning via continuous hidden state feedback instead of token generation, enabling implicit breadth-first search and more efficient test-time compute."
---

## Overview

COCONUT (Chain of Continuous Thought) by Hao et al. (2024, Meta) is the most prominent approach to [[concepts/latent-reasoning]]. It replaces explicit chain-of-thought token generation with reasoning in continuous hidden state space, feeding the last hidden state directly back as the next input embedding.

## Key Innovation

Instead of decoding hidden states into word tokens and re-encoding them, COCONUT keeps reasoning in the continuous representation space. This "continuous thought" carries richer information than a single discrete token and can encode multiple alternative reasoning paths simultaneously, enabling implicit breadth-first search.

## Significance

COCONUT challenges the assumption that language space is optimal for reasoning. If successful at scale, it could dramatically reduce the token overhead of [[concepts/test-time-compute]] while preserving or improving reasoning quality.

## Mentioned In

- [[sources/hao-coconut-latent-reasoning]] -- the original paper
