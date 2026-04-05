---
title: "Source: Karpathy's LLM OS Concept"
type: source-summary
source: "[[raw/karpathy-llm-os-concept]]"
related: ["[[entities/andrej-karpathy]]", "[[concepts/llm-os]]", "[[concepts/software-2-0]]", "[[concepts/context-windows]]"]
tags: [karpathy, LLM-OS, operating-system, software-3.0]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Karpathy's vision of LLMs as the kernel of a new operating system: CPU (reasoning), RAM (context window), filesystem (RAG), with Software 3.0 (prompts) as the programming interface."
---

## Key Points

- LLMs are not chatbots but "the kernel process of a new Operating System"
- OS analogy: CPU (reasoning), RAM (context window, 128K tokens), filesystem (RAG)
- Draws parallel: GPT/PaLM/Claude/Llama = Windows/macOS/Linux
- Evolution: Software 1.0 (code) → Software 2.0 (weights) → Software 3.0 (prompts)
- "The hottest new programming language is English"
- Advocates "Iron Man suit" architecture: partial autonomy with human-AI verification loops
- Describes LLMs as "fallible savants" — brilliant but unreliable

## Detailed Summary

In September 2023, Karpathy articulated one of his most influential metaphors: the LLM as Operating System. Rather than thinking of ChatGPT as a chat interface, he reframed the LLM as the kernel of an entirely new computing platform. The LLM orchestrates input/output across modalities, executes code, accesses the internet, and manages memory — exactly like an OS kernel manages hardware resources.

The architectural mapping is precise: the LLM's reasoning capability functions as the CPU, the context window (128K tokens) serves as RAM, RAG-enabled knowledge stores function as the filesystem, and specialized prompts/tools act as applications. The "heartbeat" of ~20 tokens/second gives the system a consistent processing rhythm.

This metaphor has profound implications. If LLMs are operating systems, then the competitive landscape mirrors the OS wars: GPT, Claude, Gemini, and Llama compete like Windows, macOS, and Linux. Application developers build on top of these "platforms" rather than building their own intelligence from scratch.

The evolution from Software 1.0 (explicit code) through Software 2.0 (trained weights, from Karpathy's 2017 essay) to Software 3.0 (natural language prompts) completes Karpathy's intellectual arc. Each transition abstracts away more implementation detail, moving from syntax to optimization to intent.

## Concepts Introduced or Discussed

- [[concepts/llm-os]] — The core metaphor
- [[concepts/software-2-0]] — Historical predecessor
- [[concepts/context-windows]] — The "RAM" of the LLM OS
- [[concepts/virtual-context-management]] — OS-inspired memory techniques

## Quotes & Evidence

> "With many puzzle pieces dropping recently, a more complete picture is emerging of LLMs not as a chatbot, but the kernel process of a new Operating System."

> "The hottest new programming language is English."

## Metadata

- **Author**: Andrej Karpathy
- **Date Published**: 2023-09-28
- **Format**: X/Twitter thread
- **URL**: https://x.com/karpathy/status/1707437820045062561
