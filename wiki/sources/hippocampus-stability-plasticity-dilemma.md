---
title: "Source: Neuroplasticity Meets AI — Hippocampus-Inspired Stability-Plasticity"
type: source-summary
source: "[[raw/hippocampus-stability-plasticity-dilemma]]"
related: ["[[concepts/complementary-learning-systems]]", "[[concepts/continual-learning]]", "[[concepts/catastrophic-forgetting]]", "[[concepts/sleep-consolidation-ai]]"]
tags: [hippocampus, continual-learning, stability-plasticity, complementary-learning-systems]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Proposes using the hippocampus-cortex dual-process system as a blueprint for AI continual learning: fast hippocampal encoding + slow cortical consolidation + SWR-BARR sleep dynamics for balanced stability and plasticity."
---

## Key Points

- The stability-plasticity dilemma: AI must learn new information without forgetting old knowledge
- Hippocampus = fast-learning module; neocortex = slow-learning module
- Sharp-Wave Ripples (SWRs) strengthen recent patterns; Barrages (BARRs) provide inhibition
- SWR-BARR alternation is key to graceful continual learning
- Proposes dual learning rates, offline consolidation, dynamic plasticity modulation
- Presents seven testable hypotheses

## Detailed Summary

This paper provides a detailed biological roadmap for implementing brain-like [[concepts/continual-learning]] in AI, using the [[concepts/complementary-learning-systems]] theory as its foundation.

The biological blueprint involves the hippocampus acting as a fast-learning module that captures new experiences quickly, with information gradually transferred to the neocortex (slow-learning module) during offline consolidation periods. Recent neuroscience discoveries reveal two complementary sleep processes: Sharp-Wave Ripples (SWRs) that strengthen recently learned patterns through replay, and Barrages (BARRs) that provide selective inhibition to prevent runaway excitation and maintain network stability.

The proposed AI implementations include: dual learning rates with fast and slow components, alternating strengthening and inhibition phases mirroring SWR-BARR dynamics, dedicated offline processing periods for consolidation, dynamic plasticity modulation that decreases as knowledge consolidates, and hierarchical networks with regulated plasticity at different levels.

Compared to existing approaches like Elastic Weight Consolidation (which slows learning on important weights) and simple memory replay, the hippocampus-inspired approach integrates these ideas into a more biologically coherent framework.

## Concepts Introduced or Discussed

- [[concepts/complementary-learning-systems]] — the core biological framework
- [[concepts/continual-learning]] — the AI capability being targeted
- [[concepts/catastrophic-forgetting]] — the problem being solved

## Metadata

- **Author**: PMC/Frontiers
- **Date Published**: 2024-11-15
- **Format**: paper
- **URL**: https://pmc.ncbi.nlm.nih.gov/articles/PMC11591613/
