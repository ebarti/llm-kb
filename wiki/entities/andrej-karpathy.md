---
title: "Andrej Karpathy"
type: entity
entity_type: person
url: "https://karpathy.ai/"
sources: ["[[sources/karpathy-llm-knowledge-bases]]", "[[sources/dairai-llm-knowledge-bases-architecture]]", "[[sources/glenrhodes-karpathy-workflow]]", "[[sources/antigravity-post-code-ai-workflow]]", "[[sources/pebblous-cheap-ontology]]", "[[sources/karpathy-minbpe-lecture]]", "[[sources/karpathy-wikipedia-biography]]", "[[sources/karpathy-software-2-0]]", "[[sources/karpathy-recipe-training-neural-networks]]", "[[sources/karpathy-vibe-coding]]", "[[sources/karpathy-2025-llm-year-review]]", "[[sources/karpathy-llm-os-concept]]", "[[sources/karpathy-eureka-labs]]", "[[sources/karpathy-state-of-gpt]]", "[[sources/karpathy-educational-projects]]"]
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/post-code-ai-workflow]]", "[[concepts/wiki-compilation]]", "[[concepts/obsidian-as-ide]]", "[[concepts/software-2-0]]", "[[concepts/vibe-coding]]", "[[concepts/llm-os]]", "[[concepts/context-engineering]]", "[[concepts/ai-native-education]]", "[[concepts/data-quality-bottleneck]]", "[[concepts/ai-code-generation]]", "[[concepts/natural-language-programming]]", "[[concepts/agentic-coding]]", "[[entities/obsidian]]", "[[entities/openai]]", "[[entities/tesla]]", "[[entities/eureka-labs]]", "[[entities/micrograd]]", "[[entities/nanogpt]]", "[[entities/minbpe]]", "[[entities/llm-c]]"]
last_compiled: 2026-04-05
summary: "Slovak-Canadian AI researcher, educator, and entrepreneur: OpenAI co-founder, Tesla AI Director, creator of Software 2.0 and vibe coding, builder of micrograd/nanoGPT/llm.c, founder of Eureka Labs, and originator of the LLM knowledge base methodology that inspired this wiki."
reading_time: "12 min"
---

## Overview

Andrej Karpathy (born October 23, 1986, Bratislava, Slovakia) is one of the most influential figures in modern AI — as a researcher, engineer, educator, and public intellectual. His career spans the founding team of [[entities/openai]], the directorship of AI at [[entities/tesla]], and the creation of some of the most widely-used educational resources in deep learning. He is the originator of the LLM-maintained personal knowledge base methodology that serves as the central framework for this entire wiki.

What sets Karpathy apart is the breadth of his contributions across four distinct domains: **frontier research** (OpenAI, Tesla Autopilot), **paradigm-defining writing** (Software 2.0, vibe coding, LLM OS), **open-source education** (micrograd, nanoGPT, llm.c, Zero to Hero), and **applied AI vision** (the LLM knowledge base, Eureka Labs). Each domain reinforces the others, creating a body of work that has shaped how an entire generation thinks about AI.

His observation that "a large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge" captures a broader shift in how AI practitioners relate to their tools — a shift this knowledge base exists to document.

---

## Biography

### Early Life and Education

Karpathy was born in Bratislava, Czechoslovakia (now Slovakia) and moved to Toronto, Canada at age 15. Before his AI career, he ran a popular YouTube channel ("badmephisto") for Rubik's cube tutorials — used by world-class speedcubers including Feliks Zemdegs — accumulating over 9 million views. This early foray into educational content creation foreshadowed his later impact as an AI educator.

- **Bachelor's degree**: Computer Science and Physics, University of Toronto (2009)
- **Master's degree**: University of British Columbia (2011), focused on physically-simulated figures under Michiel van de Panne
- **PhD**: Stanford University (2015), supervised by [[entities/fei-fei-li]] at the Stanford Vision Lab. Dissertation: "Connecting Images and Natural Language" — research at the intersection of computer vision and NLP

### Stanford and CS 231n (2012-2017)

While pursuing his PhD, Karpathy created and became the primary instructor of **CS 231n: Convolutional Neural Networks for Visual Recognition** — Stanford's first deep learning course. The course grew from 150 enrolled students in 2015 to 330 in 2016 and 750 in 2017, becoming one of Stanford's largest classes. The freely available lecture videos, notes, and assignments transformed CS 231n into a global resource, with videos garnering over 800,000 views. For many practicing ML engineers, CS 231n was their entry point into deep learning.

### OpenAI — Founding Member (2015-2017)

Karpathy joined [[entities/openai]] as a founding research scientist in 2015, working on deep learning, generative models (including GANs), and deep reinforcement learning. His time at OpenAI coincided with the organization's foundational period, when the team was exploring the research directions that would eventually lead to GPT.

### Tesla — Director of AI (June 2017 – July 2022)

As Director of Artificial Intelligence and Autopilot Vision at [[entities/tesla]], Karpathy led the computer vision team responsible for Tesla's self-driving technology. Reporting directly to Elon Musk, his team handled:

- **All in-house data labeling** for Autopilot training data
- **Neural network training** for the vision pipeline
- **Deployment** on Tesla's custom inference chip (FSD Computer)
- Brief involvement with **Tesla Optimus** (humanoid robot project)

The Tesla period was formative for Karpathy's thinking about [[concepts/software-2-0]] at industrial scale. Tesla's approach — replacing radar and lidar with pure vision (camera-only) powered by massive neural networks trained on fleet data — was Software 2.0 in its most extreme and consequential form. The challenges of scaling data labeling, managing dataset quality, and deploying models to millions of vehicles directly informed his later writings on the [[concepts/data-quality-bottleneck]].

He departed Tesla in July 2022 after a several-month sabbatical.

### OpenAI — Return (February 2023 – February 2024)

Karpathy returned to OpenAI in February 2023, building a new team focused on **midtraining and synthetic data generation** to improve GPT-4. This second stint was shorter (about one year) but positioned him at the center of the most consequential model development of the era. He departed again in February 2024.

### Eureka Labs (July 2024 – Present)

In July 2024, Karpathy founded [[entities/eureka-labs]], an AI education company building "a new kind of school that is AI native." The first product is **LLM101n** ("Let's Build A Storyteller"), an undergraduate-level course guiding students through building a complete LLM from scratch in Python, C, and CUDA. The model: human instructors design curriculum, AI Teaching Assistants provide personalized guidance at scale.

---

## Intellectual Contributions

### Software 2.0 (November 2017)

Karpathy's most paradigm-defining essay, published on Medium. The core argument: neural networks are not just another ML tool — they constitute a **fundamentally new programming paradigm** where optimization replaces explicit coding. In Software 1.0, humans write instructions. In Software 2.0, the "code" is neural network weights discovered through backpropagation and gradient descent.

Key insights:
- "Software 1.0 easily automates what you can specify, while Software 2.0 easily automates what you can verify"
- Data labelers are the new programmers
- Eight advantages of Software 2.0: computational homogeneity, silicon integration, predictable performance, memory efficiency, portability, agility, module composition, superior performance
- Warning about the interpretability crisis: "90% accurate model we understand, or 99% accurate model we don't"

The essay later extended into a three-stage evolution: **Software 1.0** (code) → **Software 2.0** (weights) → **Software 3.0** (natural language prompts). See [[concepts/software-2-0]].

### LLM OS (September 2023)

Karpathy articulated the vision of LLMs as **the kernel of a new operating system** rather than chatbots. The architectural mapping: CPU (reasoning), RAM ([[concepts/context-windows]], 128K tokens), filesystem (RAG), applications (specialized prompts/tools), heartbeat (~20 tokens/second). He drew the parallel to OS competition: "Windows, OS X, and Linux corresponding to GPT, PaLM, Claude, and Llama/Mistral."

This reframing had practical implications: if LLMs are platforms, then developers should build applications on top of them rather than creating intelligence from scratch. The [[concepts/llm-knowledge-base]] is one such application. See [[concepts/llm-os]].

### A Recipe for Training Neural Networks (April 2019)

A widely-cited practical guide offering a six-stage recipe: (1) become one with the data, (2) establish infrastructure, (3) overfit, (4) regularize, (5) tune, (6) squeeze performance. The essay's most quoted advice: **"Don't be a hero"** — copy proven architectures rather than inventing new ones. Its emphasis on data inspection as the essential first step anticipated the broader [[concepts/data-quality-bottleneck]] insight.

### State of GPT (May 2023)

Karpathy's keynote at Microsoft Build 2023 became the canonical accessible introduction to the GPT training pipeline: **pretraining → SFT → RLHF**. The talk clearly explained that pretraining consumes the vast majority of compute while SFT and RLHF are comparatively lightweight but critical for usability and alignment. It remains one of the most widely referenced explanations of how ChatGPT works.

### Vibe Coding (February 2025)

Coined in a viral X post (4.5M+ views): **"fully give in to the vibes, embrace exponentials, and forget that the code even exists."** The term captured the moment when LLMs made code generation accessible to non-programmers. Collins English Dictionary named it Word of the Year for 2025. Karpathy later acknowledged the approach suits throwaway projects, and by January 2026 proposed "agentic engineering" as the mature successor. See [[concepts/vibe-coding]].

### Context Engineering (June 2025)

Karpathy endorsed and popularized the term **"context engineering"** as the successor to prompt engineering: "the delicate art and science of filling the context window with just the right information for the next step." This reframing shifted the focus from crafting individual prompts to the systems-level challenge of managing everything an LLM sees during inference — retrieval, memory, tool outputs, conversation history, and compression. See [[concepts/context-engineering]].

### LLM Knowledge Base Methodology (April 2026)

On April 2, 2026, Karpathy published the Twitter thread that inspired this entire wiki. He described his workflow for using LLMs to build and maintain structured markdown wikis from raw ingested sources, with [[entities/obsidian]] as the viewing IDE. Key innovations:

- **Raw-to-wiki compilation pipeline**: LLM ingests documents and incrementally compiles them into cross-linked wiki articles
- **The filing loop**: Query outputs are filed back into the wiki, making every exploration additive
- **Index-based retrieval**: At personal scale (~100 articles, ~400K words), LLM-maintained summaries replace vector database RAG
- **Human as curator**: The human asks questions and directs research; the LLM handles all authoring
- **Product gap acknowledgment**: Called it "a hacky collection of scripts" and identified the opportunity for a polished product

### 2025 LLM Year in Review

Karpathy's retrospective identified key paradigm shifts:
- **RLVR** (Reinforcement Learning from Verifiable Rewards) replacing RLHF as the dominant training stage
- **"Jagged intelligence"**: LLMs are "ghosts," not animals — genius in some domains, grade-school in others
- **Benchmark skepticism**: "General apathy and loss of trust in benchmarks"
- **Unrealized potential**: Industry has captured "nowhere near 10% of their potential"
- **Cursor and Claude Code** as the emerging LLM middleware/app layer

---

## Open-Source Educational Projects

Karpathy's open-source projects form a coherent educational stack that teaches deep learning from first principles:

| Project | Description | Key Metric |
|---------|-------------|-----------|
| [[entities/micrograd]] | Autograd engine + neural net library | ~150 lines of Python |
| [[entities/nanogpt]] | GPT training/fine-tuning | Reproduces GPT-2 (124M) in ~4 days |
| [[entities/minbpe]] | BPE tokenizer implementation | 3 variants including GPT-4 reproduction |
| [[entities/llm-c]] | LLM training in pure C/CUDA | ~3,000 lines, 7% faster than PyTorch |
| **minGPT** | Minimal PyTorch GPT | Education-first predecessor to nanoGPT |
| **build-nanogpt** | Video+code lecture | From empty file to GPT-2 |
| **nanochat** | "The best ChatGPT $100 can buy" | Minimal chat implementation |

### Neural Networks: Zero to Hero (YouTube Series)

Eight lectures building from backpropagation to GPT, requiring only Python and basic calculus:

1. Building micrograd: backpropagation (2h25m)
2. Building makemore: bigram language model (1h57m)
3. Makemore Part 2: MLP (1h15m)
4. Makemore Part 3: Activations, Gradients, BatchNorm (1h55m)
5. Makemore Part 4: Becoming a Backprop Ninja (56m)
6. Makemore Part 5: Building a WaveNet (56m)
7. Building GPT from scratch (1h56m)
8. Building the GPT Tokenizer (2h13m)

The series has become a de facto standard for self-taught ML engineers. The pedagogical philosophy — "implement everything from scratch to truly understand it" — carries through all of Karpathy's work.

---

## Awards and Recognition

- **MIT Technology Review Innovators Under 35** (2020)
- **TIME 100 Most Influential People in AI** (2024)

---

## The Karpathy Intellectual Arc

Karpathy's contributions form a coherent intellectual trajectory:

| Year | Contribution | Core Shift |
|------|-------------|-----------|
| 2015 | CS 231n at Stanford | Making deep learning accessible |
| 2015 | OpenAI founding | Building frontier AI |
| 2017 | Tesla AI Director | [[concepts/software-2-0]] at industrial scale |
| 2017 | Software 2.0 essay | Neural networks as new programming paradigm |
| 2019 | Recipe for Training NNs | Practical wisdom: data quality > model cleverness |
| 2022 | Zero to Hero series | From-scratch implementations as pedagogy |
| 2023 | State of GPT talk | Demystifying the training pipeline |
| 2023 | LLM OS concept | LLMs as computing platforms, not chatbots |
| 2024 | llm.c | Proving frameworks are optional |
| 2024 | Eureka Labs | AI-native education as a company |
| 2025 | Vibe coding | Code generation commoditized |
| 2025 | Context engineering | The real discipline of working with LLMs |
| 2026 | LLM Knowledge Base | From manipulating code to manipulating knowledge |

The through-line: **progressive abstraction**. Each contribution moves the human further from low-level implementation toward high-level intent. From writing C++ (Software 1.0) to curating datasets (Software 2.0) to speaking English (Software 3.0) to orchestrating knowledge (the LLM KB). The destination is always the same: humans should focus on what matters (understanding, judgment, direction) while machines handle the rest.

---

## Notable Quotes

> "A large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge." — April 2026

> "Software 1.0 easily automates what you can specify, while Software 2.0 easily automates what you can verify." — November 2017

> "The hottest new programming language is English." — 2023

> "Fully give in to the vibes, embrace exponentials, and forget that the code even exists." — February 2025

> "Context engineering is the delicate art and science of filling the context window with just the right information for the next step." — June 2025

> "Don't be a hero." — April 2019

---

## Role in This Knowledge Base

Karpathy is the central figure in this knowledge base. His April 2026 thread is the primary source document, and virtually every other source in the wiki either directly analyzes his approach (DAIR.AI, Glen Rhodes, Antigravity Codes, Pebblous) or provides contrasting systems compared against his methodology ([[entities/storm]], [[entities/karma]], [[entities/graphiti]]). His design choices — markdown as substrate, Obsidian as viewer, LLM as sole author, filing loop for compounding — define the reference architecture against which all alternatives are measured.

His intellectual trajectory also illustrates the broader theme of [[concepts/post-code-ai-workflow]]: the shift from using AI to write code toward using AI to compile and manage knowledge.

---

## Mentioned In

- [[sources/karpathy-llm-knowledge-bases]] — original Twitter thread describing the full workflow
- [[sources/karpathy-wikipedia-biography]] — comprehensive biography
- [[sources/karpathy-software-2-0]] — the paradigm-defining 2017 essay
- [[sources/karpathy-recipe-training-neural-networks]] — practical training guide
- [[sources/karpathy-vibe-coding]] — origin and cultural impact of vibe coding
- [[sources/karpathy-2025-llm-year-review]] — 2025 retrospective on LLM progress
- [[sources/karpathy-llm-os-concept]] — LLM as operating system kernel
- [[sources/karpathy-eureka-labs]] — AI-native education company
- [[sources/karpathy-state-of-gpt]] — Microsoft Build 2023 keynote on GPT training
- [[sources/karpathy-educational-projects]] — micrograd, nanoGPT, minbpe, llm.c catalog
- [[sources/karpathy-minbpe-lecture]] — 2h13m lecture building a GPT tokenizer from scratch
- [[sources/dairai-llm-knowledge-bases-architecture]] — Elvis Saravia's system architecture analysis
- [[sources/glenrhodes-karpathy-workflow]] — Glen Rhodes' technical walkthrough
- [[sources/antigravity-post-code-ai-workflow]] — Antigravity Codes' broadest analysis
- [[sources/pebblous-cheap-ontology]] -- Pebblous positions Karpathy's approach as "Cheap Ontology"
- [[sources/wikipedia-vibe-coding]] -- comprehensive history of vibe coding and its evolution to agentic engineering
- [[sources/greptile-state-of-ai-coding-2025]] -- adoption data showing CLAUDE.md in 75% of organizations

## External References

- https://karpathy.ai/ — Personal website
- https://github.com/karpathy — GitHub profile
- https://karpathy.ai/zero-to-hero.html — Zero to Hero course page
- https://eurekalabs.ai/ — Eureka Labs
