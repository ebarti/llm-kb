---
title: "Glossary"
type: "meta"
entries: 732
summary: "Auto-generated alphabetical glossary of concepts and entities with their summaries."
last_compiled: "2026-04-19"
---
# Glossary

_Auto-generated on 2026-04-19 by `tools/compile/pages/gen_glossary.py`. Entries are the titles of entity and concept articles; definitions are the `summary:` field from each article's frontmatter._

- Concepts: **462**
- Entities: **270**
- Total entries: **732**

## 0-9

**2024 Nobel Prizes for AI** _(concept)_
: In 2024, both Physics (Hopfield, Hinton — neural network foundations) and Chemistry (Baker — protein design; Hassabis, Jumper — AlphaFold) Nobel Prizes went to AI researchers. A watershed moment recognizing AI's transformative contribution to science.
: See [[concepts/nobel-prizes-ai-2024]]

**3D Generation** _(concept)_
: AI-driven synthesis of 3D content from text, images, or captured scenes -- split between NeRF (implicit neural, ultra-high quality) and Gaussian Splatting (explicit primitives, 10-50x faster), with text-to-3D enabled by diffusion-guided optimization like Hunyuan3D-2.
: See [[concepts/3d-generation]]

**3D Parallelism** _(concept)_
: Combining data, tensor, and pipeline parallelism in a topology-aware configuration: TP within nodes (NVLink), PP across nodes (InfiniBand), DP across the cluster. The standard approach for frontier LLM training.
: See [[concepts/3d-parallelism]]

**5D Parallelism** _(concept)_
: Extension of 3D parallelism (DP+TP+PP) with Context Parallelism (splitting sequence length) and Expert Parallelism (distributing MoE experts) — the current state-of-the-art for training frontier models like DeepSeek-V3.
: See [[concepts/5d-parallelism]]

## A

**Active Inference** _(concept)_
: An extension of the free energy principle to action: organisms minimize surprise not only by updating internal models (perception) but by actively changing the world to match their predictions — with implications for robotics and embodied AI.
: See [[concepts/active-inference]]

**Adaptive Compute Allocation** _(concept)_
: The practice of dynamically allocating different amounts of inference-time compute to different queries based on difficulty, model confidence, or reasoning quality signals -- achieving 4x efficiency over uniform allocation.
: See [[concepts/adaptive-compute-allocation]]

**Addy Osmani** _(entity: person)_
: Google Chrome engineering lead who published an influential 10-step LLM coding workflow for 2026 — advocating spec-first planning, model rotation, and the human as 'director of the show.'
: See [[entities/addy-osmani]]

**Agent Frameworks** _(concept)_
: The landscape of LLM agent development frameworks: LangChain/LangGraph, AutoGen, CrewAI, and 2025 newcomers (agent-lightning, hermes-agent, superpowers), consolidating around distinct use cases.
: See [[concepts/agent-frameworks]]

**Agent Memory** _(concept)_
: Short-term and long-term memory systems for LLM agents: from simple conversation history to learned, adaptive memory management via AgeMem's tool-based RL approach.
: See [[concepts/agent-memory]]

**Agent Orchestration** _(concept)_
: Patterns for coordinating multiple LLM agents: orchestrator-worker (most common in production), supervisor, and router patterns with registry/state-store/supervisor components.
: See [[concepts/agent-orchestration]]

**Agent Planning** _(concept)_
: How LLM agents decompose complex goals into executable subtask sequences using Chain of Thought, Tree of Thought, and task decomposition, with feedback loops via ReAct and Reflexion.
: See [[concepts/agent-planning]]

**Agent-to-Agent Protocol (A2A)** _(concept)_
: Google's protocol for inter-agent collaboration: agents publish Agent Cards for capability discovery, delegate tasks dynamically, and coordinate in real time. Complementary to MCP (tools) — A2A handles 'expertise' and agent-to-agent communication.
: See [[concepts/agent-to-agent-protocol]]

**Agentic AI Foundation (AAIF)** _(entity: org)_
: Linux Foundation directed fund governing MCP, co-founded by Anthropic, Block, and OpenAI in December 2025. Supported by Google, Microsoft, AWS, Cloudflare, Bloomberg. Mission: ensure agentic AI evolves transparently and in the public interest.
: See [[entities/agentic-ai-foundation]]

**Agentic Coding** _(concept)_
: AI agents that autonomously write, test, debug, and ship code — from Devin's 2024 debut to Claude Code's $2.5B revenue, transforming developers from coders to coordinators.
: See [[concepts/agentic-coding]]

**Agentic Knowledge Management** _(concept)_
: The next evolution of PKM: AI agents that proactively monitor knowledge bases, understand user context and goals, propose actions autonomously, and execute with human approval — transforming the knowledge base into shared cognitive infrastructure between human and AI.
: See [[concepts/agentic-knowledge-management]]

**Agentic RAG** _(concept)_
: The current frontier of RAG: autonomous agents orchestrate retrieval through reflection, planning, and tool use — dynamically adapting pipelines with routers, graders, generators, and hallucination checkers.
: See [[concepts/agentic-rag]]

**Agentic Workflow Patterns** _(concept)_
: Five canonical workflow patterns for AI agents (Anthropic): prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer — plus the distinction between deterministic workflows and dynamic agents.
: See [[concepts/agentic-workflow-patterns]]

**Agentic Workflows** _(concept)_
: The paradigm of prompting LLMs iteratively through multi-step workflows with reflection, tool use, planning, and multi-agent collaboration — architecture matters more than model size.
: See [[concepts/agentic-workflows]]

**AI Accelerators** _(concept)_
: Purpose-built hardware for neural network computation — from GPUs with tensor cores to custom ASICs; spectrum ranges from NVIDIA's general-purpose Blackwell (1800 TFLOPS) to Taalas's model-weights-in-silicon (17,000 tok/s, single model only).
: See [[concepts/ai-accelerators]]

**AI Agent Integration Patterns** _(concept)_
: Five patterns for connecting AI agents to external systems, from simplest to most complex: direct API calls, function calling, MCP gateway, unified API, and A2A protocols — with decision matrix across auth, governance, and maintenance.
: See [[concepts/ai-agent-integration-patterns]]

**AI Alignment** _(concept)_
: The technical challenge of ensuring AI systems pursue the goals their operators intend — encompassing RLHF, Constitutional AI, scalable oversight, and the detection of deceptive alignment.
: See [[concepts/ai-alignment]]

**AI Arms Race** _(concept)_
: The escalating competition between nations to develop and deploy military AI systems — the US has operational combat experience (Operation Epic Fury), China pursues fully autonomous combat decisions, and the PLA's critical gap is zero combat testing since 1979.
: See [[concepts/ai-arms-race]]

**AI Chip Export Controls** _(concept)_
: US restrictions on advanced AI chip exports to China — the most potent policy lever in the AI race; US chips 5-17x more powerful than China's best; policy oscillating between restriction and relaxation under Trump administration.
: See [[concepts/ai-chip-export-controls]]

**AI Code Generation** _(concept)_
: LLMs generating source code from natural language or existing code context -- from autocomplete to autonomous issue resolution -- now producing ~46% of all committed code with SWE-bench scores reaching 80.8%.
: See [[concepts/ai-code-generation]]

**AI Code Review** _(concept)_
: AI-powered pull request review tools that analyze code for bugs, security, and style — now achieving higher action rates (55%) than human reviewers (49%), and identified as the key bottleneck in the AI productivity paradox.
: See [[concepts/ai-code-review]]

**AI Coding Assistants** _(concept)_
: The landscape of LLM-powered developer tools — from inline autocomplete to autonomous agents — organized into five tiers: code review, IDE assistants, cloud-specific, autonomous agents, and low-code builders.
: See [[concepts/ai-coding-assistants]]

**AI Consciousness** _(concept)_
: The debate over whether AI systems can have subjective experience — framework of 14 theory-derived indicators, no current proof but mounting behavioral signals, 25-35% estimated credence for frontier models, with catastrophic asymmetric risk in false negatives.
: See [[concepts/ai-consciousness]]

**AI Content Verification** _(concept)_
: Methods for verifying the accuracy and trustworthiness of AI-generated content — spanning automated detection, human fact-checking, multi-model peer review, and source attribution.
: See [[concepts/ai-content-verification]]

**AI Creativity Paradox** _(concept)_
: The empirically demonstrated paradox that generative AI improves individual creative output (especially for less creative individuals) while reducing the collective diversity of novel content — with implications for research, education, law, and all knowledge domains.
: See [[concepts/ai-creativity-paradox]]

**AI Data Center Energy** _(concept)_
: AI data centers projected to consume 1,100 TWh in 2026 (equivalent to Japan); accelerated servers growing 30%/year; chip TDP rising from 700W to 1,000W+; liquid cooling at 47%; Microsoft nuclear (2 GW), Amazon solar (1.5 GW) commitments.
: See [[concepts/ai-data-center-energy]]

**AI Drug Discovery** _(concept)_
: AI is reshaping drug discovery with 173+ programs in clinical development, 80-90% Phase I success rates (vs 52% historical), and 30-month target-to-trial timelines (vs 6-8 years). 2026 Phase III results will determine if the promise is real.
: See [[concepts/ai-drug-discovery]]

**AI Economics** _(concept)_
: The trillion-dollar economics of AI: $2.52T global spending in 2026, $700B+ Big Tech CapEx, GDP impact surpassing the dot-com boom — but the revenue gap between investment and returns remains the central risk.
: See [[concepts/ai-economics]]

**AI Energy and Infrastructure** _(concept)_
: Data centers consume 415 TWh (1.5% of global electricity) in 2024, doubling to 945 TWh by 2030 — with AI-driven servers growing at 30% annually, making power the binding constraint on AI scaling.
: See [[concepts/ai-energy-and-infrastructure]]

**AI for Genomics** _(concept)_
: AI tools for genomics analyze DNA sequences to predict gene regulation, variant effects, and disease mechanisms. AlphaGenome processes 1M base-pairs predicting thousands of molecular properties; Evo2 is the largest biology model (128K+ genomes). AI now designs genomes, not just reads them.
: See [[concepts/ai-genomics]]

**AI for Materials Science** _(concept)_
: AI is revolutionizing materials discovery: GNoME found 2.2M new crystals (800 years equivalent), including 528 lithium-ion conductors and 52K graphene-like compounds. Autonomous labs like A-Lab physically synthesize AI-predicted materials, closing the prediction-to-synthesis loop.
: See [[concepts/ai-materials-science]]

**AI for Mathematical Reasoning** _(concept)_
: AI mathematical reasoning has advanced from struggling with arithmetic to winning IMO gold medals (Gemini Deep Think, DeepSeekMath-V2), solving open Erdos conjectures, breaking 56-year records (AlphaEvolve on matrix multiplication), and producing genuine mathematical discoveries (FunSearch on cap sets).
: See [[concepts/ai-mathematical-reasoning]]

**AI for Scientific Discovery** _(concept)_
: AI is having its most transformative real-world impact in scientific discovery — from AlphaFold (protein structure), GNoME (2.2M materials), GenCast (weather), to theorem proving and self-driving labs. The 2024 Nobel Prizes in both Physics and Chemistry went to AI researchers.
: See [[concepts/ai-for-scientific-discovery]]

**AI for Scientific Discovery** _(concept)_
: AI's transition from 'co-pilot' interpreting knowledge to 'lab-pilot' conducting experiments — AlphaFold (Nobel Prize), halicin (novel antibiotic), ISM001-055 (first AI drug Phase II), GNoME (380K crystals), and autonomous laboratories.
: See [[concepts/ai-scientific-discovery]]

**AI for Weather and Climate** _(concept)_
: AI weather models (GenCast, WeatherNext 2, NVIDIA Earth-2) outperform traditional supercomputer-based forecasting on 97%+ of metrics while running 100x+ faster. Applications span disaster preparedness, renewable energy, and 100-year climate projections.
: See [[concepts/ai-weather-climate]]

**AI Geopolitics** _(concept)_
: The intersection of AI development with international power dynamics — encompassing the US-China competition, export controls, regulatory divergence, military AI, talent flows, and sovereignty drives shaping AI's global trajectory.
: See [[concepts/ai-geopolitics]]

**AI Governance** _(concept)_
: Regulatory and organizational frameworks for responsible AI development and deployment — centered on the EU AI Act (binding), NIST AI RMF (voluntary), and ISO/IEC 42001 (certifiable), with enforcement beginning August 2026.
: See [[concepts/ai-governance]]

**AI Hardware Landscape** _(concept)_
: The competitive dynamics of AI compute hardware in 2026: NVIDIA dominance (80%+ market share) challenged by hyperscaler custom silicon (Google TPU, Amazon Trainium), specialized inference ASICs (Cerebras, Groq, Etched), and emerging paradigms (photonic, quantum).
: See [[concepts/ai-hardware-landscape]]

**AI Industrial Policy** _(concept)_
: Government strategies to build national AI capabilities — China leads with $137B direct investment, 2,100+ guidance funds, and provincial competition; the US relies more on private sector ($500B Stargate); EU focuses on regulatory power.
: See [[concepts/ai-industrial-policy]]

**AI Industry Consolidation** _(concept)_
: Extreme capital concentration in frontier AI: Q1 2026 saw $242B in AI VC (80% of all startup funding); four companies captured 65% of all global VC; big tech infrastructure spending approaching $700B; 'AI-Have-Nots' being marginalized.
: See [[concepts/ai-industry-consolidation]]

**AI Infrastructure Investment** _(concept)_
: AI infrastructure spending at $2.5T globally in 2026 (44% YoY growth); Big Tech capex $527B+ (Amazon $200B, Google $175-185B, Meta $115-135B); Stargate $500B; historically unprecedented — reshaping energy grids, trade flows, and real estate markets.
: See [[concepts/ai-infrastructure-investment]]

**AI Military Applications** _(concept)_
: AI deployed in active military operations by 2026: targeting (Gospel, Lavender), intelligence fusion (Maven Smart System), decision support (GenAI.mil), and autonomous platforms — Operation Epic Fury demonstrated 900 strikes in 12 hours.
: See [[concepts/ai-military-applications]]

**AI Optimism and Abundance** _(concept)_
: The thesis that powerful AI could compress a century of human progress into 5-10 years — transforming biology, mental health, economics, and governance — articulated most fully by Dario Amodei.
: See [[concepts/ai-optimism-and-abundance]]

**AI Pair Programming** _(concept)_
: The practice of collaborating with AI as a programming partner — treating it as a capable but fallible junior developer requiring clear direction, incremental tasking, and constant review.
: See [[concepts/ai-pair-programming]]

**AI Productivity Paradox** _(concept)_
: The disconnect between perceived and measured AI productivity: developers believe AI makes them faster, but rigorous studies show 19% slowdown for experienced developers, and organizations see no net delivery improvement despite 84% adoption.
: See [[concepts/ai-productivity-paradox]]

**AI Protein Design** _(concept)_
: De novo protein design uses AI (especially diffusion models like RFdiffusion3) to create entirely new proteins with specified functions — from custom antibodies to industrial enzymes. David Baker won the 2024 Nobel Prize for this work.
: See [[concepts/ai-protein-design]]

**AI Protein Structure Prediction** _(concept)_
: Predicting 3D protein structure from amino acid sequence — solved by AlphaFold 2 at CASP 14 (2020). AlphaFold 3 extends to all biomolecular interactions (76% accuracy on ligand binding). 200M+ structures released, 3M+ researchers served, Nobel Prize awarded 2024.
: See [[concepts/ai-protein-structure-prediction]]

**AI Regulation Landscape** _(concept)_
: Three competing regulatory philosophies: EU (comprehensive, risk-based, rights-protective), US (fragmented, sector-specific, innovation-first), China (agile, state-controlled, 'develop hard, control tight'); the race to set global AI norms remains wide open.
: See [[concepts/ai-regulation-landscape]]

**AI Research Assistants** _(concept)_
: The 2026 AI research tool ecosystem: Perplexity (citation search), Elicit (literature reviews), Consensus (science validation), Scite (1.2B citation statements), Research Rabbit (free network mapping) — effective researchers compose multi-tool workflows rather than relying on single assistants.
: See [[concepts/ai-research-assistants]]

**AI Safety** _(concept)_
: The field ensuring AI systems do not cause unintended harm — spanning technical robustness, alignment, evaluation, governance, and societal risk mitigation.
: See [[concepts/ai-safety]]

**AI Safety Benchmarks** _(concept)_
: Standardized evaluations for measuring AI system safety — from jailbreak resistance (HarmBench) and bias (BBQ) to hallucination detection (TruthfulQA, Mu-SHROOM) and organizational safety practices (FLI Safety Index).
: See [[concepts/ai-safety-benchmarks]]

**AI Sovereignty** _(concept)_
: A nation's ability to develop and control its own AI capabilities — 71% of executives call it an 'existential concern'; requires sovereignty across energy, compute, data, models, cloud, and applications; $600B market opportunity by 2030.
: See [[concepts/ai-sovereignty]]

**AI Talent Competition** _(concept)_
: Global competition for AI talent: demand exceeds supply 3.2:1; Europe trains 30% more per capita than US but loses them to 30-70% salary premiums; academic brain drain accelerating (young scholars 100x more likely to leave for industry); governments investing billions.
: See [[concepts/ai-talent-competition]]

**AI UX Design Patterns** _(concept)_
: Emerging taxonomy of 57+ interaction patterns for AI products, organized into Wayfinders, Prompt Actions, Tuners, Governors, Trust Builders, and Identifiers — covering the full lifecycle from onboarding to oversight.
: See [[concepts/ai-ux-design-patterns]]

**AI-Generated Content Risks** _(concept)_
: AI-generated content in collaborative knowledge systems creates risks beyond simple hallucination: subtle misattribution (real sources cited for claims they don't contain), content homogenization, reduced human contributions, and overwhelmed verification capacity.
: See [[concepts/ai-generated-content-risks]]

**AI-Native Design** _(concept)_
: Products where AI is fundamental, not supplementary — built from day one with models, data pipelines, and learning systems as core components; evaluated across five dimensions: Design, Data, Domain Expertise, Dynamism, Distribution.
: See [[concepts/ai-native-design]]

**AI-Native Education** _(concept)_
: Education redesigned around AI from the ground up: human instructors create curriculum, AI teaching assistants provide personalized guidance at scale — Karpathy's Eureka Labs vision.
: See [[concepts/ai-native-education]]

**Aider** _(entity: tool)_
: Open-source CLI-based AI coding agent with Git-native workflow, transparent diffs, and model flexibility — the leading open-source alternative to proprietary coding agents.
: See [[entities/aider]]

**AlphaEvolve** _(entity: tool)_
: DeepMind's Gemini-powered evolutionary coding agent. Broke Strassen's 56-year matrix multiplication record (48 vs 49 multiplications), recovers 0.7% of Google's global compute, and improved best-known solutions on 20% of 50+ open math problems.
: See [[entities/alphaevolve]]

**AlphaFold** _(entity: tool)_
: Google DeepMind's protein structure prediction system. AlphaFold 2 solved the 50-year structure prediction problem (CASP 14, 2020); AF3 extends to all biomolecular interactions. 3M+ researchers, 200M+ structures, 35K+ citations, 2024 Nobel Prize in Chemistry.
: See [[entities/alphafold]]

**AlphaGenome** _(entity: tool)_
: DeepMind's AI tool for genomic analysis. Processes up to 1M base-pair DNA sequences, predicting thousands of molecular properties for non-coding regions (98% of genome). Outperforms best models on 22/24 evaluations. Published in Nature (2025).
: See [[entities/alphagenome]]

**AMD** _(entity: org)_
: NVIDIA's primary GPU competitor: MI300X (192GB HBM3e, 5.2 TB/s, ~2 PFLOPS FP8) at $2.20/FLOPS-hour vs NVIDIA's $2.80; MI350 (June 2025), MI400/MI450 'Helios' with HBM4 (2026); ROCm ecosystem growing but less mature than CUDA.
: See [[entities/amd]]

**AMI Labs** _(entity: org)_
: Advanced Machine Intelligence Labs — Yann LeCun's Paris-based AI startup; raised $1.03B seed at $3.5B valuation (largest European seed ever) in March 2026 to build world models based on JEPA as an alternative to LLMs.
: See [[entities/ami-labs]]

**Andrej Karpathy** _(entity: person)_
: Slovak-Canadian AI researcher, educator, and entrepreneur: OpenAI co-founder, Tesla AI Director, creator of Software 2.0 and vibe coding, builder of micrograd/nanoGPT/llm.c, founder of Eureka Labs, and originator of the LLM knowledge base methodology that inspired this wiki.
: See [[entities/andrej-karpathy]]

**Andrew Ng** _(entity: person)_
: AI researcher and educator who popularized the four agentic AI design patterns (reflection, tool use, planning, multi-agent collaboration) and advocates architecture-over-model-size for enterprises.
: See [[entities/andrew-ng]]

**Andy Matuschak** _(entity: person)_
: Software engineer, researcher, and independent thinker who developed the evergreen notes framework — five principles for durable, evolving notes that build intellectual capital over time — and pioneered public sliding-pane note systems.
: See [[entities/andy-matuschak]]

**Anki** _(entity: tool)_
: Open-source spaced repetition software using the FSRS algorithm to schedule adaptive review of flashcards — the most sophisticated and widely used SRS platform, integrable with PKM tools like Obsidian.
: See [[entities/anki]]

**Anthropic** _(entity: org)_
: AI safety PBC founded 2021 by 7 ex-OpenAI researchers (Dario & Daniela Amodei + 5); $380B valuation; builds Claude models, Claude Code ($2.5B ARR), and MCP; ranked #1 in FLI AI Safety Index.
: See [[entities/anthropic]]

**Anthropic HH-RLHF Dataset** _(entity: dataset)_
: Foundational open preference dataset with 170K human comparisons for training helpful and harmless AI assistants — collected via Amazon Mechanical Turk, using chosen/rejected pair format.
: See [[entities/anthropic-hh-rlhf]]

**Anti-Bot Evasion** _(concept)_
: Techniques for avoiding web scraping detection: IP rotation, header randomization, behavior mimicry, session persistence, and headless browser stealth — balanced against ethical obligations to respect site owners.
: See [[concepts/anti-bot-evasion]]

**Apache Airflow** _(entity: tool)_
: Dominant workflow orchestration platform (35% of enterprise AI/ML pipelines): Python-native DAG definitions, event-driven scheduling (3.0), dynamic task mapping, and integrations with SageMaker/Databricks/vector DBs.
: See [[entities/apache-airflow]]

**Apple Silicon Inference** _(concept)_
: Apple Silicon's unified memory architecture makes Macs uniquely suited for local LLM inference; MLX leads throughput (<14B models), llama.cpp handles larger models via CPU+GPU splitting.
: See [[concepts/apple-silicon-inference]]

**Approximate Nearest Neighbor Search (ANN)** _(concept)_
: Trading small amounts of accuracy for dramatic speed gains when searching high-dimensional vector spaces: the foundational tradeoff underlying all vector database indexing.
: See [[concepts/approximate-nearest-neighbor-search]]

**Attention Is All You Need** _(entity: paper)_
: The 2017 paper by Vaswani et al. introducing the Transformer architecture — the most cited ML paper of the 21st century, replacing RNNs/CNNs with pure attention and enabling all modern LLMs.
: See [[entities/attention-is-all-you-need]]

**Attention Mechanisms** _(concept)_
: The family of mechanisms enabling neural networks to dynamically focus on relevant parts of their input — from Bahdanau's 2014 additive attention through the 2017 Transformer's scaled dot-product self-attention to modern variants (flash, linear, sparse, grouped query).
: See [[concepts/attention-mechanisms]]

**Attention Sinks** _(concept)_
: The phenomenon where initial tokens in a sequence receive disproportionately high attention scores regardless of semantic content — caused by softmax's sum-to-one constraint forcing excess attention weight onto positionally-biased anchors.
: See [[concepts/attention-sinks]]

**Audio Generation** _(concept)_
: AI music and sound synthesis -- dominated in 2026 by Suno v5 (~100M users, 44.1kHz, 12-track stems) and Udio, with major label settlements legitimizing the space and ElevenLabs bringing voice synthesis expertise to music.
: See [[concepts/audio-generation]]

**Audio-Visual Generation** _(concept)_
: The convergence of video and audio generation into unified systems -- exemplified by Veo 3's native synchronized sound from text prompts and Kling 3.0's dialogue with lip sync, eliminating entire post-production workflows in 2026.
: See [[concepts/audio-visual-generation]]

**Augmented LLM** _(concept)_
: The foundational building block of agentic AI: an LLM enhanced with retrieval, tool integration, and memory — capable of independently generating search queries, selecting tools, and retaining information.
: See [[concepts/augmented-llm]]

**Automated Fact-Checking** _(concept)_
: Automated verification of LLM-generated claims against external knowledge: claim decomposition, evidence retrieval, verdict generation — using frameworks like OpenFactCheck, FIRE, and VERIFAID to complement faithfulness checking.
: See [[concepts/automated-fact-checking]]

**Automated Testing for AI-Generated Code** _(concept)_
: The emerging discipline of validating AI-generated code through agentic test generation, self-healing test suites, and AI-on-AI review -- critical because 60% of AI-generated code requires intervention and review times have ballooned 91%.
: See [[concepts/automated-testing-for-ai-code]]

**Automated Wiki Creation** _(concept)_
: STORM's approach: single-shot, multi-perspective Wikipedia-style article generation from web search using simulated expert conversations and outline-first synthesis — contrasting with Karpathy's incremental, accumulating KB model.
: See [[concepts/automated-wiki-creation]]

**Autonomous Driving and Foundation Models** _(concept)_
: The most commercially mature domain of physical AI — transitioning from modular perception-planning-control stacks to end-to-end foundation models; Waymo at 10M+ rides, NVIDIA Alpamayo-R1 as first open reasoning VLA for driving, DeepRoute's 40B VLA model.
: See [[concepts/autonomous-driving]]

**Autoregressive Image Generation** _(concept)_
: Image generation via next-token prediction over visual tokens -- resurgent with LlamaGen and VAR (NeurIPS 2024 Best Paper) matching diffusion quality, and NextStep-1 (ICLR 2026 Oral, 14B) achieving state-of-the-art via continuous tokens with a flow matching head.
: See [[concepts/autoregressive-image-generation]]

## B

**Batch Inference** _(concept)_
: Processing LLM requests in bulk rather than real-time: API batch endpoints offer 50% price discounts for jobs that can wait hours, while server-side continuous batching achieves 23x throughput improvement.
: See [[concepts/batch-inference]]

**Bayesian Brain** _(concept)_
: The hypothesis that the brain represents and processes information as probability distributions, performing approximate Bayesian inference to combine prior beliefs with sensory evidence — the theoretical foundation for predictive coding and the free energy principle.
: See [[concepts/bayesian-brain]]

**Beautiful Soup** _(entity: tool)_
: Python's most popular HTML/XML parsing library — lightweight, handles malformed markup gracefully, often used with requests for simple scraping or with Playwright for hybrid JS+parsing workflows.
: See [[entities/beautiful-soup]]

**Benchmark Contamination** _(concept)_
: When benchmark evaluation datasets leak into LLM training data, inflating performance scores — a fundamental unsolved problem with an inherent fidelity-resistance tradeoff in mitigation strategies.
: See [[concepts/benchmark-contamination]]

**Benchmark Saturation** _(concept)_
: The crisis of LLM benchmark reliability: 'benchmaxxing' (optimizing for leaderboard scores), training data contamination, and MMLU saturation above 90% mean benchmark numbers are no longer trustworthy indicators of capability.
: See [[concepts/benchmark-saturation]]

**BERT (Bidirectional Encoder Representations from Transformers)** _(entity: paper)_
: Google's 2018 encoder-only transformer using bidirectional Masked Language Modeling — revolutionized NLP understanding tasks but cannot generate text. 110M (base) to 340M (large) parameters.
: See [[entities/bert]]

**Best-of-N Sampling** _(concept)_
: The fundamental parallel test-time scaling technique: generate N candidate solutions, select the best via a verifier or reward model -- simple but effective, serving as the baseline against which all other inference scaling methods are measured.
: See [[concepts/best-of-n-sampling]]

**Bi-Encoder vs Cross-Encoder** _(concept)_
: The two fundamental architectures for neural text matching: bi-encoders encode texts independently for fast retrieval but lose information; cross-encoders process pairs jointly for high accuracy but cannot scale to full collections.
: See [[concepts/bi-encoder-vs-cross-encoder]]

**Black Forest Labs** _(entity: org)_
: AI company founded by the original creators of Stable Diffusion -- develops the FLUX family of image generation models, advancing beyond their original U-Net designs to MMDiT architecture with flow matching training.
: See [[entities/black-forest-labs]]

**Blank Page Problem** _(concept)_
: The UX failure where a blank chat box provides no affordance for what an AI system can do, putting the burden on users to discover capabilities — solved by Wayfinder patterns like Suggestions, Templates, and Gallery.
: See [[concepts/blank-page-problem]]

**BM25** _(concept)_
: Best Matching 25: the standard probabilistic ranking algorithm for keyword search, building on TF-IDF with term frequency saturation and document length normalization.
: See [[concepts/bm25]]

**Boilerplate Removal** _(concept)_
: The sub-problem of content extraction focused on removing navigation, ads, footers, sidebars, and other non-content elements from web pages — solved via DOM scoring (Readability), block classification (jusText), or neural filtering (Reader-LM).
: See [[concepts/boilerplate-removal]]

**Boston Dynamics** _(entity: org)_
: Pioneer robotics company known for Atlas (humanoid), Spot (quadruped), and Stretch (logistics); Electric Atlas unveiled 2024 as enterprise-grade humanoid; partnered with Google DeepMind for Gemini Robotics AI integration; commercial launch targeted 2026-2028 at $140-150K.
: See [[entities/boston-dynamics]]

**Bradley-Terry Model** _(concept)_
: The statistical model underlying both RLHF reward models and DPO: converts pairwise preference comparisons into probability estimates via the sigmoid of reward differences.
: See [[concepts/bradley-terry-model]]

**Brain-Computer Interfaces** _(concept)_
: Direct communication pathways between the brain and external devices — from medical applications (paralysis, ALS) to potential cognitive enhancement, with Neuralink and competitors entering commercial production in 2026.
: See [[concepts/brain-computer-interfaces]]

**Brain-Inspired AI** _(concept)_
: AI systems designed using principles from biological brains — including sparse coding, complementary learning systems, predictive processing, sleep-like consolidation, and spiking neural networks — addressing limitations of conventional deep learning.
: See [[concepts/brain-inspired-ai]]

**Brussels Effect** _(concept)_
: The phenomenon where EU regulations become de facto global standards because multinational companies adopt the strictest rules everywhere — the EU AI Act may replicate GDPR's 'Brussels Effect' for AI, but outcome remains uncertain.
: See [[concepts/brussels-effect]]

**Byte Pair Encoding (BPE)** _(concept)_
: The most popular tokenization algorithm for LLMs — iteratively merges the most frequent adjacent byte/character pairs to build a subword vocabulary, used by GPT, Llama, Gemma, and Qwen.
: See [[concepts/byte-pair-encoding]]

**Byte-Level Models (Tokenization-Free)** _(concept)_
: Language models that process raw UTF-8 bytes instead of subword tokens, eliminating tokenization entirely — exemplified by EvaByte (6.5B) and Byte Latent Transformer, now matching tokenized models at scale.
: See [[concepts/byte-level-models]]

## C

**Cache-Augmented Generation (CAG)** _(concept)_
: A RAG alternative that preloads all documents into the LLM's KV cache at once, eliminating retrieval entirely — 10x faster with higher accuracy on small knowledge bases, but limited to manageable corpus sizes.
: See [[concepts/cache-augmented-generation]]

**Calibrated Uncertainty** _(concept)_
: The strategic shift from pursuing 'zero hallucinations' to building AI systems that transparently signal doubt, refuse when uncertain, and produce confidence-calibrated outputs.
: See [[concepts/calibrated-uncertainty]]

**Cameron R. Wolfe** _(entity: person)_
: Ph.D. researcher and author of the 'Deep (Learning) Focus' newsletter, producing detailed technical deep-dives on DPO, reward models, RLAIF, and other LLM alignment topics.
: See [[entities/cameron-wolfe]]

**Catastrophic Forgetting** _(concept)_
: Models losing previously learned knowledge when fine-tuned on new data — mitigated by PEFT (LoRA), regularization (EWC), experience replay, parameter isolation, careful learning rate selection, and neuroscience-inspired approaches like sleep consolidation and complementary learning systems.
: See [[concepts/catastrophic-forgetting]]

**Causal Attention** _(concept)_
: Masked self-attention that restricts each position to attend only to previous positions, enabling autoregressive generation in decoder-only models like GPT and Llama.
: See [[concepts/causal-attention]]

**Cerebras Systems** _(entity: org)_
: Creator of the world's largest chip (WSE-3: 4T transistors, 900K cores, 46,225 mm²); $10B+ OpenAI deal; IPO targeting $22B in Q2 2026; AWS partnership for cloud access; deployed at Oak Ridge, Argonne, DARPA.
: See [[entities/cerebras]]

**Chain-of-Thought Prompting** _(concept)_
: A prompting technique that elicits step-by-step reasoning in LLMs by providing worked exemplars or instructions like 'think step by step,' dramatically improving performance on arithmetic, commonsense, and symbolic reasoning tasks at 100B+ parameter scale.
: See [[concepts/chain-of-thought]]

**Chain-of-Thought Prompting** _(concept)_
: Wei et al. (2022) technique that enables complex reasoning by having LLMs decompose problems into intermediate steps — the single most impactful prompting technique for reasoning tasks.
: See [[concepts/chain-of-thought-prompting]]

**Chatbot Arena (Arena AI)** _(entity: tool)_
: Crowdsourced LLM evaluation platform: anonymous pairwise battles with 300+ models and 1.5M+ preferences, using Elo/Bradley-Terry scoring from organic user queries — the most widely-cited dynamic benchmark.
: See [[entities/chatbot-arena]]

**Cheap Ontology** _(concept)_
: Pebblous framing: LLM wikis replace $10M–$20M enterprise knowledge graphs using only markdown files, LLM APIs, and natural-language schema instructions — democratizing what was once exclusive ontology engineering expertise.
: See [[concepts/cheap-ontology]]

**Chinchilla** _(entity: paper)_
: DeepMind's 2022 paper establishing compute-optimal scaling laws: model parameters and training tokens should scale equally (~20 tokens per parameter), showing many existing LLMs were significantly undertrained.
: See [[entities/chinchilla]]

**Chinchilla Scaling Laws** _(concept)_
: DeepMind's 2022 finding that compute-optimal LLM training requires ~20 tokens per parameter — overturning GPT-3-era wisdom of scaling parameters over data. Post-Chinchilla, the industry shifted further to overtrained small models (Llama 3: 1,875:1) for inference efficiency.
: See [[concepts/chinchilla-scaling-laws]]

**ChromaDB** _(entity: tool)_
: An open-source embedding database used in Gallagher's Knowledge Graph Kit to provide semantic vector search over graph nodes alongside SQLite structural storage.
: See [[entities/chromadb]]

**Chunking Strategies** _(concept)_
: How text is split into segments for embedding and retrieval in RAG: from simple fixed-size splitting (512 tokens, 10-20% overlap) to semantic, hierarchical, and agentic approaches that align chunk boundaries with meaning.
: See [[concepts/chunking-strategies]]

**Claim Extraction and Fact Decomposition** _(concept)_
: Breaking complex LLM outputs into atomic, independently verifiable claims — essential for fact-checking, wiki quality assurance, and preventing hallucination propagation.
: See [[concepts/claim-extraction]]

**Claimify** _(entity: tool)_
: Microsoft Research's 4-stage claim extraction system (ACL 2025) that decomposes LLM outputs into atomic verifiable claims with 99% source entailment.
: See [[entities/claimify]]

**Claude** _(entity: tool)_
: Anthropic's frontier LLM family named after Claude Shannon; spans four generations (Claude 1-4.6) with Opus/Sonnet/Haiku tiers, up to 1M context, adaptive thinking, and market-leading coding benchmarks.
: See [[entities/claude]]

**Claude Code** _(entity: tool)_
: Anthropic's agentic coding tool: reads codebases, edits files, runs tests, creates PRs — $2.5B annualized revenue by March 2026, leading SWE-bench Verified at 80.9%.
: See [[entities/claude-code]]

**Claude Model Family Evolution** _(concept)_
: Complete timeline of Claude model releases from Claude 1 (March 2023) through Claude 4.6 (February 2026), tracking the expansion of context windows (9K to 1M), capabilities, and pricing.
: See [[concepts/claude-model-family-evolution]]

**CLIP** _(entity: tool)_
: OpenAI's Contrastive Language-Image Pretraining model (2021): dual text/image encoders producing 512-dim shared embeddings via contrastive learning; foundational for multimodal search, RAG, and image generation.
: See [[entities/clip]]

**COCONUT (Chain of Continuous Thought)** _(entity: paper)_
: Meta research paper introducing latent reasoning via continuous hidden state feedback instead of token generation, enabling implicit breadth-first search and more efficient test-time compute.
: See [[entities/coconut]]

**CodeRabbit** _(entity: tool)_
: The most widely installed AI code review app on GitHub/GitLab — 2M+ repos, 13M+ PRs processed, free for open source — but has the highest false-positive rate among major review tools.
: See [[entities/coderabbit]]

**Codestral** _(entity: tool)_
: Mistral AI's open-weight coding model (22B parameters) -- fast local inference at 1.4s per response vs Claude's 2.1s, scoring within 85-90% of frontier models on straightforward tasks.
: See [[entities/codestral]]

**Cognee** _(entity: tool)_
: Cognitive memory layer for agentic AI systems. Hybrid graph + vector embeddings in unified memory. Modular extraction pipelines, multiple graph backends (NetworkX, FalkorDB, Neo4j), 30+ data source connectors, incremental learning without full reprocessing.
: See [[entities/cognee]]

**ColBERT (Contextualized Late Interaction over BERT)** _(concept)_
: A retrieval model that keeps per-token embeddings and uses MaxSim scoring — 100x faster than cross-encoders with comparable accuracy, strong zero-shot generalization, and multimodal extensions (ColPali, ColQwen).
: See [[concepts/colbert]]

**ColBERT and Late Interaction** _(concept)_
: A retrieval paradigm between bi-encoders and cross-encoders: encode queries and documents independently at the token level, then score via MaxSim — achieving near-cross-encoder accuracy at orders of magnitude less compute.
: See [[concepts/colbert-late-interaction]]

**Collaborative Knowledge Building** _(concept)_
: Structured group processes for creating shared knowledge — ranging from Wikipedia's adversarial-cooperative editing to federated multi-perspective systems — now being transformed by AI that serves as both participant and infrastructure.
: See [[concepts/collaborative-knowledge-building]]

**Collaborative UX** _(concept)_
: Microsoft's UX framework for productive human-AI interaction: tight input-output feedback loops, prompt/output history, appropriate friction at key moments, fact-checking through citations, and editable outputs — users guide AI toward their goals through iterative collaboration.
: See [[concepts/collaborative-ux]]

**Collective Intelligence** _(concept)_
: The capacity of groups to outperform individuals through diverse, independent contributions aggregated via structured mechanisms — now being fundamentally reshaped by AI.
: See [[concepts/collective-intelligence]]

**Collective Intelligence Project (CIP)** _(entity: org)_
: Nonprofit R&D lab (founded by Divya Siddarth and Saffron Huang) building collective intelligence mechanisms for AI governance — including Collective Constitutional AI with Anthropic and Global Dialogues with 1,000 participants from 70+ countries.
: See [[entities/collective-intelligence-project]]

**ColPali** _(entity: tool)_
: ColBERT-like multimodal retrieval model using VLMs as image encoders: produces multiple vectors per token with MaxSim similarity for direct visual document retrieval without OCR, evaluated on ViDoRe benchmark.
: See [[entities/colpali]]

**ComfyUI** _(entity: tool)_
: Node-based visual workflow builder for image generation pipelines -- supports FLUX, Stable Diffusion, and other models with drag-and-drop node graphs, comfy-pack for API deployment, and extensive community extensions.
: See [[entities/comfyui]]

**Common Crawl** _(entity: dataset)_
: Non-profit web crawl archive releasing monthly snapshots of petabytes of raw web data — the foundational data source for virtually all open LLM pretraining datasets.
: See [[entities/common-crawl]]

**Complementary Learning Systems** _(concept)_
: The theory that the brain uses two complementary memory systems — a fast-learning hippocampus for rapid encoding and a slow-learning neocortex for long-term storage — with sleep-mediated consolidation transferring knowledge between them.
: See [[concepts/complementary-learning-systems]]

**Computational Functionalism** _(concept)_
: The philosophical position that consciousness depends on information-processing patterns rather than biological substrate — if true, silicon-based AI could in principle be conscious, making the substrate (neurons vs transistors) irrelevant.
: See [[concepts/computational-functionalism]]

**Compute Scaling** _(concept)_
: The multi-dimensional landscape of AI scaling: pre-training scaling shows diminishing returns, but test-time compute and algorithmic efficiency open new dimensions — constrained by power, chips, data, and capital.
: See [[concepts/compute-scaling]]

**Compute-Optimal Training** _(concept)_
: Allocating a fixed compute budget optimally between model size and training data — Chinchilla showed equal scaling is optimal, but modern practice shifts toward inference-optimal overtraining of smaller models.
: See [[concepts/compute-optimal-training]]

**Confluence** _(entity: tool)_
: Atlassian's structured wiki and documentation platform for enterprise knowledge management. Includes Rovo AI with 20+ pre-built documentation agents. Deep Jira integration (76% of customers ship faster). Pricing from $5.42/user/month. Best fit for technical teams in the Atlassian ecosystem.
: See [[entities/confluence]]

**Consistency Models** _(concept)_
: Generative models that map noise to data in 1-2 steps by enforcing self-consistency along diffusion trajectories -- achieving FID 2.82 on CIFAR-10 in one step, with SANA-Sprint (2025) reaching 0.1s latency for 1024x1024 generation on H100.
: See [[concepts/consistency-models]]

**Constitutional AI (CAI)** _(concept)_
: Anthropic's approach to aligning AI using a written set of principles (a constitution) that enables AI self-critique, self-revision, and AI-generated preference labels -- reducing reliance on human labelers while producing harmless yet non-evasive assistants.
: See [[concepts/constitutional-ai]]

**Content Extraction** _(concept)_
: The discipline of extracting meaningful content from messy web pages — from DOM-scoring heuristics (Readability) through hybrid algorithms (Trafilatura) to neural models (Reader-LM) — the critical first step in any knowledge base ingest pipeline.
: See [[concepts/content-extraction]]

**Context Compression** _(concept)_
: Techniques for reducing token count while preserving information: hard prompts (LLMLingua, 20x), soft prompts (480x), structured pruning (Provence, 95%), and hierarchical summarization.
: See [[concepts/context-compression]]

**Context Engineering** _(concept)_
: The systems discipline of managing everything an LLM encounters during inference — successor to prompt engineering, credited to Karpathy (2024-2025).
: See [[concepts/context-engineering]]

**Context Windows** _(concept)_
: The fixed-size token buffer an LLM can process in a single inference call; growing ~30x/year but effective utilization lags behind raw capacity.
: See [[concepts/context-windows]]

**Continual Learning** _(concept)_
: The ability to learn new tasks sequentially without forgetting previous ones — a capability natural to biological brains but challenging for neural networks, addressed through replay, regularization, and architecture-based approaches.
: See [[concepts/continual-learning]]

**Continued Pretraining** _(concept)_
: Extending a model's pretraining phase on new corpora (domain text, synthetic data, or instruction data) to broaden or specialize its knowledge before task-specific fine-tuning.
: See [[concepts/continued-pretraining]]

**Continuous Batching** _(concept)_
: Iteration-level scheduling where completed sequences are immediately replaced with new requests, achieving 23x throughput and 90%+ GPU utilization versus 40% in naive static batching.
: See [[concepts/continuous-batching]]

**Conversational UI vs Structured UI** _(concept)_
: Chat interfaces achieve 70% of tasks via accessibility but fail at refinement; the best AI products use hybrid approaches — conversation for intent and ideation, structured UI for iteration and precision.
: See [[concepts/conversational-ui-vs-structured-ui]]

**Copilot Pattern** _(concept)_
: The dominant AI product architecture where AI functions as an intelligent assistant working alongside humans — the human is the pilot, AI is the copilot — with three focus variants: Immersive, Assistive, and Embedded.
: See [[concepts/copilot-pattern]]

**Copyright and Training Data** _(concept)_
: The evolving legal landscape around using copyrighted works for AI training — emerging US consensus that general-purpose training is 'highly transformative' (fair use), but significant uncertainty remains with cases involving OpenAI and Google expected in 2026.
: See [[concepts/copyright-and-training-data]]

**Corrective RAG (CRAG)** _(concept)_
: A RAG enhancement that evaluates retrieval quality via a lightweight evaluator, falls back to web search when vectorstore results are poor, and refines knowledge by grading individual document strips.
: See [[concepts/corrective-rag]]

**Crawl4AI** _(entity: tool)_
: The #1 trending open-source web crawler (63K+ GitHub stars) — Playwright-based async crawler producing LLM-ready markdown with BM25 relevance filtering, multi-strategy extraction, and anti-bot detection.
: See [[entities/crawl4ai]]

**Cross-Attention** _(concept)_
: Attention mechanism where queries come from one sequence and keys/values from another, enabling encoder-decoder models and multimodal fusion.
: See [[concepts/cross-attention]]

**Cross-Embodiment Transfer** _(concept)_
: A single AI model controlling diverse robot morphologies without retraining — π0 spans 7-8 robot types, Open X-Embodiment pools 800K trajectories from many platforms; the robotics equivalent of LLMs generalizing across tasks.
: See [[concepts/cross-embodiment-transfer]]

**Cursor** _(entity: tool)_
: AI-native IDE (VS Code fork) that leads the market with $2B+ ARR and $29.3B valuation by March 2026 — praised for 'magical' inline editing, codebase indexing, and agent mode.
: See [[entities/cursor]]

**Custom Silicon** _(concept)_
: The hyperscaler trend toward designing proprietary AI chips: Google TPU (7 generations), Amazon Trainium/Inferentia, Meta MTIA, Microsoft Maia, Apple-Broadcom Baltra, OpenAI-Broadcom — delivering 30-40% cost advantage over merchant GPUs through hardware-software co-design.
: See [[concepts/custom-silicon]]

**Cyc Project** _(entity: tool)_
: AI's most ambitious knowledge engineering project (1984-present): 40 years encoding common-sense knowledge into 1.5M terms and 24.5M assertions in CycL — a cautionary tale and proof of concept for explicit knowledge representation.
: See [[entities/cyc-project]]

## D

**DAIR.AI** _(entity: org)_
: An AI education and research organization whose Academy published the definitive system architecture analysis of Karpathy's LLM knowledge base methodology.
: See [[entities/dairai]]

**Daniela Amodei** _(entity: person)_
: President and co-founder of Anthropic; former VP of Operations at OpenAI; co-leads the company with her brother Dario Amodei.
: See [[entities/daniela-amodei]]

**Dario Amodei** _(entity: person)_
: CEO and co-founder of Anthropic; former VP of Research at OpenAI; author of 'Machines of Loving Grace' essay articulating AI's transformative upside across biology, governance, and economics.
: See [[entities/dario-amodei]]

**Data Deduplication** _(concept)_
: Removing duplicate and near-duplicate documents from LLM training data at trillion-token scale using exact matching, MinHash LSH, or semantic methods — essential for preventing wasted compute, memorization, and evaluation leakage.
: See [[concepts/data-deduplication]]

**Data Parallelism** _(concept)_
: The simplest distributed training strategy: replicate the full model on each GPU, split input batches, compute gradients independently, then synchronize via all-reduce. Extended by ZeRO to eliminate memory redundancy.
: See [[concepts/data-parallelism]]

**Data Quality Bottleneck** _(concept)_
: In LLM knowledge base pipelines, data quality at the raw input stage — not model capability — is the decisive factor: low-quality ingestion cascades into contaminated wiki content and flawed fine-tuning.
: See [[concepts/data-quality-bottleneck]]

**Data Wall** _(concept)_
: The looming exhaustion of high-quality training data — estimated by 2026-2028 — forcing the industry toward synthetic data, multimodal sources, and new learning paradigms.
: See [[concepts/data-wall]]

**Dataview** _(entity: tool)_
: The most important Obsidian power-user plugin: a SQL-like query engine over vault metadata supporting DQL, inline queries, and JavaScript — with Datacore as its next-gen successor.
: See [[entities/dataview]]

**David Baker** _(entity: person)_
: Biochemist at the University of Washington's Institute for Protein Design. Won 2024 Nobel Prize in Chemistry (one half) for computational protein design spanning 20+ years, from Rosetta to RFdiffusion3.
: See [[entities/david-baker]]

**David Chalmers** _(entity: person)_
: Australian philosopher known for formulating the 'hard problem of consciousness' — co-author of the Butlin-Long framework proposing 14 theory-derived indicators for assessing AI consciousness.
: See [[entities/david-chalmers]]

**David Ha** _(entity: person)_
: AI researcher; co-author of the foundational World Models paper (2018) with Schmidhuber, establishing the VAE + MDN-RNN + minimal controller framework for learning inside a dream.
: See [[entities/david-ha]]

**DCLM (DataComp-LM)** _(entity: dataset)_
: Benchmark and dataset from Apple/UW for controlled training data experiments — provides 240T-token Common Crawl pool, 53 evaluations, and the DCLM-Baseline (2T tokens) achieving 64% MMLU on a 7B model.
: See [[entities/dclm]]

**Dean Allemang** _(entity: person)_
: Knowledge graph and semantic web expert who demonstrated that LLMs natively understand OWL ontologies, arguing that ontologies and property graphs are complementary rather than competing.
: See [[entities/dean-allemang]]

**DeepEval** _(entity: tool)_
: Open-source LLM evaluation framework by Confident AI with 14+ built-in metrics (hallucination, faithfulness, toxicity, bias), Pytest-like unit testing paradigm, and CI/CD integration.
: See [[entities/deepeval]]

**DeepSeek** _(entity: org)_
: Chinese AI lab whose R1 model (Jan 2025) triggered the 'DeepSeek moment' — demonstrating frontier reasoning at dramatically lower cost; V3.2 (685B, MIT) surpassed GPT-5-High on math.
: See [[entities/deepseek]]

**DeepSeek V3** _(entity: tool)_
: Chinese AI lab's 671B-parameter MoE model trained for a reported $5.6M — challenging the assumption that frontier LLMs require $100M+ budgets, though the figure excluded infrastructure, experimentation, and failed runs.
: See [[entities/deepseek-v3]]

**DeepSpeed** _(entity: tool)_
: Microsoft's open-source deep learning optimization library, best known for the ZeRO optimizer that progressively shards optimizer states, gradients, and parameters to enable training of models that exceed single-GPU memory.
: See [[entities/deepspeed]]

**Demis Hassabis** _(entity: person)_
: CEO of Google DeepMind. Co-recipient of the 2024 Nobel Prize in Chemistry (with John Jumper) for AlphaFold's solution to the protein structure prediction problem. Founded DeepMind (2010) and Isomorphic Labs (2021).
: See [[entities/demis-hassabis]]

**Democratic AI Alignment** _(concept)_
: Using collective intelligence mechanisms — citizens' assemblies, quadratic voting, liquid democracy, deliberative platforms — to align AI systems with collective values rather than designer preferences or market incentives alone.
: See [[concepts/ai-alignment-democratic]]

**DePlot** _(entity: tool)_
: Google's specialized tool for converting charts and plots into structured text (linearized tables), used in multimodal RAG preprocessing to make visual data accessible to text-based LLMs.
: See [[entities/deplot]]

**Derek Sivers** _(entity: person)_
: Programmer, author, and entrepreneur who has written exclusively in plain text since 1990 — the most prominent individual advocate for plain-text-as-productivity-system.
: See [[entities/derek-sivers]]

**Developer Experience with AI** _(concept)_
: How AI tools reshape the daily developer workflow — from subjective perception (feeling faster) vs objective measurement (often slower), to the shift from coder to architect/reviewer, and the 10 DX requirements for agentic IDEs.
: See [[concepts/developer-experience-ai]]

**Devin** _(entity: tool)_
: The first 'AI software engineer' by Cognition Labs (March 2024) — operates autonomously with its own shell, browser, and editor; Devin 2.0 (April 2025) dropped price from $500/mo to $20/mo.
: See [[entities/devin]]

**Devin AI** _(entity: tool)_
: First autonomous AI software engineer by Cognition Labs (2024): shell + editor + browser in sandbox, 13.86% SWE-bench at launch, $20/month with 2.0.
: See [[entities/devin-ai]]

**Dexterous Manipulation** _(concept)_
: Teaching robots human-level hand skills — the frontier challenge of embodied AI; breakthrough enabled by VLA models (π0 achieves laundry folding), high-DOF hands (22 DOF in Optimus Gen 3, 16 DOF per hand in Figure 02), and tactile sensors detecting forces as small as 3 grams.
: See [[concepts/dexterous-manipulation]]

**Diffusion Models** _(concept)_
: The dominant generative framework (2020-2026) that produces data by learning to reverse a gradual noise-addition process, surpassing GANs and VAEs across image, video, audio, and 3D generation -- now evolving toward flow matching and transformer backbones.
: See [[concepts/diffusion-models]]

**Diffusion Transformer (DiT)** _(concept)_
: Architecture replacing U-Net with transformer backbone for diffusion models -- using patchification, self-attention, and adaLN conditioning to achieve predictable scaling: DiT-XL/2 achieves FID 2.27 on ImageNet 256x256, and the design underpins FLUX, SD3, and Sora.
: See [[concepts/diffusion-transformer]]

**Digital Commons Governance** _(concept)_
: The institutional frameworks governing shared digital knowledge resources — copyleft licensing, community norms, foundation oversight — now requiring redesign as AI extracts value from and potentially degrades the commons.
: See [[concepts/digital-commons-governance]]

**Digital Garden** _(concept)_
: A philosophy of public knowledge-sharing that rejects chronological blogging in favor of continuously evolving, densely linked notes organized by topological relationships — featuring six core patterns including learning in public, epistemic status markers, and independent ownership.
: See [[concepts/digital-garden]]

**Direct Preference Optimization (DPO)** _(concept)_
: A reward-free alignment method that solves the RLHF objective in closed form, optimizing an implicit reward embedded in the policy itself via a simple binary cross-entropy loss over preference pairs.
: See [[concepts/dpo]]

**Distributed Training** _(concept)_
: Splitting LLM training workloads across hundreds or thousands of GPUs using parallelism strategies (data, tensor, pipeline, context, expert) to make training feasible within reasonable time and cost constraints.
: See [[concepts/distributed-training]]

**Docling** _(entity: tool)_
: IBM open-source document parsing toolkit (MIT): DocLayNet layout analysis + TableFormer table recognition, outputs AI-ready JSON/Markdown, 9/10 performance, ideal for enterprise RAG in air-gapped environments.
: See [[entities/docling]]

**Document AI and OCR** _(concept)_
: Evolution from character-level OCR (~85% accuracy) to AI-powered document intelligence (99%+) via VLMs; LLMs now rival or exceed specialized OCR engines on complex layouts.
: See [[concepts/document-ai-ocr]]

**Document Chunking Strategies** _(concept)_
: Techniques for splitting documents into retrieval-optimized segments: fixed-size (simplest), recursive, semantic boundary, sliding window, context-aware, adaptive (ML-based), and metadata-enriched — with 18-40% accuracy improvements from semantic chunking.
: See [[concepts/document-chunking-strategies]]

**Document Processing Pipeline** _(concept)_
: The multi-stage system that converts raw unstructured documents into structured, AI-ready data: acquire → parse → chunk → enrich → embed → store, with quality validation at each stage.
: See [[concepts/document-processing-pipeline]]

**Domain-Adaptive Pretraining (DAPT)** _(concept)_
: Intermediate pretraining step on unlabeled domain text between general pretraining and task fine-tuning — requires no labeled data and consistently improves downstream performance.
: See [[concepts/domain-adaptive-pretraining]]

**Doug Lenat** _(entity: person)_
: American AI researcher (1950-2023) who founded the Cyc project in 1984 and spent 39 years building the world's largest hand-encoded common-sense knowledge base — his final paper proposed Cyc+LLM integration.
: See [[entities/doug-lenat]]

**Douglas Engelbart** _(entity: person)_
: American engineer (1925-2013) who invented the mouse, hyperlink, and collaborative computing, inspired by Bush's Memex — his 1968 'Mother of All Demos' previewed modern interactive computing 25 years early.
: See [[entities/douglas-engelbart]]

**DreamerV3** _(entity: paper)_
: DeepMind's general RL algorithm published in Nature (2025): masters 150+ diverse tasks with a single configuration via learned world model imagination; first to mine a diamond in Minecraft from scratch without human data (30M steps, ~17 days).
: See [[entities/dreamerv3]]

**DSPy** _(entity: tool)_
: Declarative Self-improving Python framework that acts as a 'compiler' for LLM prompts, optimizing entire pipelines at compile-time — raised accuracy from 46.2% to 64.0% on prompt evaluation tasks.
: See [[entities/dspy]]

## E

**Edge Inference (On-Device LLMs)** _(concept)_
: Running LLMs directly on mobile devices and edge hardware: sub-1B to 3B models with 4-bit quantization achieve <20ms/token latency — 10-25x faster than cloud roundtrips — with zero data transmission and zero API cost.
: See [[concepts/edge-inference]]

**Edward Feigenbaum** _(entity: person)_
: American computer scientist (b. 1936), 'father of expert systems,' who led the Stanford Heuristic Programming Project and established that knowledge is more important than inference methods.
: See [[entities/edward-feigenbaum]]

**Efficient Coding Hypothesis** _(concept)_
: Horace Barlow's 1961 principle that sensory neurons should maximize information transmission while minimizing redundancy and energy — the theoretical foundation for sparse coding, predictive coding, and energy-efficient AI design.
: See [[concepts/efficient-coding-hypothesis]]

**ElevenLabs** _(entity: tool)_
: AI voice and audio company ($11B valuation) that expanded into music generation in August 2025 -- Eleven Music produces vocals with 'unsettling realism' in breath, vibrato, and emotional inflection, leveraging its voice synthesis expertise.
: See [[entities/elevenlabs]]

**Elicit** _(entity: tool)_
: AI research assistant purpose-built for academic literature reviews — customizable comparison tables, semantic paper summaries, and structured data extraction from peer-reviewed sources ($10-65/month).
: See [[entities/elicit]]

**Elinor Ostrom** _(entity: person)_
: Nobel Prize-winning political economist (1933-2012) whose commons governance framework — originally for natural resources — became foundational for understanding digital knowledge commons governance.
: See [[entities/elinor-ostrom]]

**Elvis Saravia** _(entity: person)_
: Founder of DAIR.AI Academy who provided the most thorough system architecture analysis of Karpathy's LLM knowledge base, coining the 'four-phase operational cycle' framework.
: See [[entities/elvis-saravia]]

**Embodied AI** _(concept)_
: AI agents with physical instantiation that learn through interaction with the world — requiring the perception-modeling-decision loop where world models bridge multimodal sensing with executable actions; advancing via sim-to-real transfer and self-supervised video pretraining.
: See [[concepts/embodied-ai]]

**Embodied Intelligence** _(concept)_
: The paradigm of AI systems that perceive, reason about, and physically act in the real world — bridging the gap between digital intelligence and physical interaction through integrated perception, planning, and motor control.
: See [[concepts/embodied-intelligence]]

**Emergent Abilities of Large Language Models** _(concept)_
: Capabilities absent in smaller LLMs that appear suddenly at scale -- including chain-of-thought reasoning, in-context learning, and multi-step arithmetic -- subject to debate about whether the phase transitions are genuine or measurement artifacts.
: See [[concepts/emergent-abilities]]

**Enterprise Knowledge (consulting firm)** _(entity: org)_
: Knowledge management consulting firm led by CEO Zach Wahl. Publishes influential annual KM trend reports (proven prescient since 2019). Specializes in semantic layer implementations, taxonomy, and information architecture for enterprise AI initiatives.
: See [[entities/enterprise-knowledge]]

**Enterprise Knowledge Management** _(concept)_
: The organizational discipline of capturing, organizing, sharing, and governing knowledge at scale. The KM software market is $13.70B (2025), growing to $37.64B by 2031 (18.34% CAGR). AI is transforming every layer: ingestion (automated transcription), organization (semantic layers), retrieval (conversational search), and governance (validation pipelines).
: See [[concepts/enterprise-knowledge-management]]

**Enterprise Search** _(concept)_
: AI-powered unified search across all enterprise applications and data sources. Market: $6.83B (2025), projected $11.15B by 2030. Core architecture: Enterprise Graph linking people/data/processes, 100+ SaaS integrations, permission-aware RAG, conversational AI interfaces. Evolving from search into agentic workflow automation.
: See [[concepts/enterprise-search]]

**Entity Linking and Resolution** _(concept)_
: Mapping textual entity mentions to canonical KB entries — resolving ambiguity ('Apple' the company vs. fruit) and merging synonyms ('GPT-4o' / 'gpt4o') via LLM-based clustering and ontology grounding.
: See [[concepts/entity-linking]]

**Epoch AI** _(entity: org)_
: Research institute tracking AI compute trends, training data, and scaling limits — authors of the definitive analysis of whether AI scaling can continue through 2030.
: See [[entities/epoch-ai]]

**EU AI Act** _(entity: org)_
: The world's first comprehensive AI regulation — a binding EU law with extraterritorial reach, four risk tiers, penalties up to EUR 35M, and full enforcement beginning August 2, 2026.
: See [[entities/eu-ai-act]]

**Eureka Labs** _(entity: org)_
: Karpathy's AI-native education company (founded July 2024) building LLM101n — a from-scratch LLM course with AI teaching assistants supporting human instructors.
: See [[entities/eureka-labs]]

**EvaByte** _(entity: tool)_
: A 6.5B open-source tokenization-free byte-level language model from HKU/SambaNova that matches tokenizer-based models, using multibyte prediction and EVA linear attention.
: See [[entities/evabyte]]

**Evaluation Bias in LLM-as-a-Judge** _(concept)_
: Systematic biases in LLM-based evaluation: position bias (2.5%-82.5% win-rate swing), verbosity bias (>90% preference for longer responses), and self-enhancement bias (87.76% self-preference), with quantified mitigation strategies.
: See [[concepts/evaluation-bias]]

**Evaluation Workflow** _(concept)_
: A phased approach to LLM evaluation: define success criteria, build evaluation datasets, run automated experiments, stress-test and red-team, deploy production monitoring, and continuously iterate.
: See [[concepts/evaluation-workflow]]

**Evergreen Notes** _(concept)_
: Andy Matuschak's framework for durable, evolving notes that accumulate insight over time — five principles (atomic, concept-oriented, densely linked, associative ontologies, written for self) that transform note-taking into a thinking practice.
: See [[concepts/evergreen-notes]]

**Everlaw** _(entity: tool)_
: AI-powered e-discovery and document analysis platform for legal teams — rapidly summarizes and classifies large document volumes for litigation, investigations, and regulatory compliance.
: See [[entities/everlaw]]

**Excalidraw (Obsidian Plugin)** _(entity: tool)_
: The most-downloaded Obsidian community plugin: a full-featured freehand drawing and diagramming tool embedded in the vault for visual thinking alongside notes.
: See [[entities/excalidraw]]

**ExecuTorch** _(entity: tool)_
: Meta's production on-device inference framework: 50KB base footprint, 12+ hardware backends, reached 1.0 GA in October 2025, serving billions of users across Meta's mobile apps.
: See [[entities/executorch]]

**Expert Systems** _(concept)_
: Rule-based AI systems (1965-1990s) that encoded domain expertise as if-then rules in a knowledge base paired with an inference engine — the first commercially successful AI, ultimately killed by the knowledge acquisition bottleneck.
: See [[concepts/expert-systems]]

**Explainable AI UX** _(concept)_
: Four practical design patterns for making AI explainable in products: Because Statement, What-If Interactive, Highlight Reel, Push-and-Pull Visual — plus the warning that explanation can backfire if it creates excessive cognitive load.
: See [[concepts/explainable-ai-ux]]

**Extended Thinking** _(concept)_
: Claude's step-by-step reasoning capability that allocates additional compute at inference time: evolved from manual budget_tokens (Claude 4) to adaptive thinking (Claude 4.6) where the model dynamically decides reasoning depth.
: See [[concepts/extended-thinking]]

## F

**FAISS** _(entity: tool)_
: Facebook AI Similarity Search -- an open-source library for efficient similarity search and clustering of dense vectors, supporting billions of vectors with disk-based indexing.
: See [[entities/faiss]]

**Faithfulness and Groundedness** _(concept)_
: Faithfulness measures whether LLM outputs are factually consistent with provided context; groundedness measures the degree to which answers are supported by retrieved documents — the positive framing of 'not hallucinating.'
: See [[concepts/faithfulness-and-groundedness]]

**FalkorDB** _(entity: tool)_
: Graph database with GraphRAG SDK for performance-critical knowledge graph deployments. Sub-50ms query latency, 90% hallucination reduction vs. traditional RAG, multi-model support (OpenAI, Gemini, Anthropic, Groq, Ollama). Self-hosted or cloud deployment.
: See [[entities/falkordb]]

**Federated Knowledge** _(concept)_
: Distributed knowledge architectures where independent nodes maintain their own knowledge while sharing across a network — from Cunningham's Federated Wiki ('chorus of voices') to Wikibase's federated knowledge graphs with underlays, overlays, and interlace.
: See [[concepts/federated-knowledge]]

**Fei-Fei Li** _(entity: person)_
: Stanford professor, ImageNet creator, and Karpathy's PhD advisor — one of the most influential figures in computer vision and AI.
: See [[entities/fei-fei-li]]

**Few-Shot Prompting** _(concept)_
: In-context learning via demonstration examples within prompts — the highest-ROI prompt engineering technique, where format and distribution matter more than label accuracy.
: See [[concepts/few-shot-prompting]]

**Figma** _(entity: tool)_
: Collaborative design tool whose 'Figma Make' feature exemplifies AI-native collaboration: natural language prompts + full creative control + AI suggestions awaiting user approval.
: See [[entities/figma]]

**Figure AI** _(entity: org)_
: Humanoid robot company founded 2022 by Brett Adcock; $39B valuation (Sep 2025); three robot generations (01→02→03); pivoted from OpenAI to proprietary Helix VLA; BotQ facility targeting 12,000 units/year; demonstrated laundry folding, dishwasher loading.
: See [[entities/figure-ai]]

**File Over App** _(concept)_
: Steph Ango's philosophy that files in open formats outlast any application — the foundational design principle behind Obsidian's local-first, plain-text architecture.
: See [[concepts/file-over-app]]

**Fine-Tuning LLMs** _(concept)_
: Adapting pretrained LLMs to domain-specific tasks by training on curated datasets — from full fine-tuning to parameter-efficient methods (LoRA/QLoRA) to hybrid approaches (RAFT).
: See [[concepts/fine-tuning]]

**FineWeb** _(entity: dataset)_
: HuggingFace's 15T-token open LLM pretraining dataset from 96 CommonCrawl dumps — the largest publicly available clean dataset, with FineWeb-Edu (1.3T educational tokens) and FineWeb-2 (1,000+ languages) variants.
: See [[entities/fineweb]]

**Firecrawl** _(entity: tool)_
: AI-focused web scraping API by Mendable.ai: converts websites to LLM-ready markdown/JSON via single API call, handles JS rendering and anti-bot, six modes (scrape/crawl/map/search/interact/agent), MCP Server for LLM integration.
: See [[entities/firecrawl]]

**FlashAttention** _(concept)_
: IO-aware attention algorithm using tiling to avoid materializing the N x N attention matrix in GPU HBM — reducing memory from O(N^2) to O(N) and achieving 2-4x speedup. FlashAttention-3 reaches 75% H100 utilization.
: See [[concepts/flash-attention]]

**FlashAttention** _(entity: framework)_
: IO-aware exact attention algorithm by Tri Dao reducing memory from O(N^2) to O(N) via tiling — now the default attention implementation in PyTorch, JAX, and all major LLM frameworks, with v3 achieving 75% H100 utilization.
: See [[entities/flashattention]]

**Flow Matching** _(concept)_
: Generative framework learning velocity fields that transport noise distributions to data distributions along straight-line ODE paths -- simpler, faster, and more flexible than traditional diffusion denoising, now the standard training objective for FLUX, SD3, and other leading models.
: See [[concepts/flow-matching]]

**FLUX** _(entity: tool)_
: Leading open-source text-to-image model family from Black Forest Labs using MMDiT architecture with flow matching -- FLUX.2 [dev] at 32B parameters, FLUX.2 [klein] at 4-9B for consumer GPUs, featuring dual-stream/single-stream transformer blocks and T5+CLIP text encoding.
: See [[entities/flux]]

**Foundation Models for Robotics** _(concept)_
: The application of the foundation model paradigm (large-scale pre-training → task-specific fine-tuning) to robotics — enabling generalist robot policies that transfer across tasks, environments, and robot morphologies; key models include RT-2, π0, GR00T-N1, and OpenVLA.
: See [[concepts/foundation-models-for-robotics]]

**Free Energy Principle** _(concept)_
: Karl Friston's mathematical framework proposing that all adaptive systems minimize variational free energy — an upper bound on surprise — unifying perception, action, learning, and attention under one principle with direct links to VAEs and generative AI.
: See [[concepts/free-energy-principle]]

**FreshWiki** _(entity: dataset)_
: An evaluation dataset of recent Wikipedia articles created after LLM training cutoffs, introduced by the STORM project to prevent data leakage in automated wiki generation benchmarks.
: See [[entities/freshwiki]]

**Function Calling** _(concept)_
: The mechanism by which LLMs invoke external APIs — each provider (OpenAI, Anthropic, Google) implements differently. Simple and fast for prototyping but creates vendor lock-in and M×N integration problems at scale.
: See [[concepts/function-calling]]

**FunSearch** _(entity: tool)_
: DeepMind's system pairing PaLM 2 with automated evaluators in evolutionary loops to make mathematical discoveries. First LLM to solve a long-standing math puzzle (cap set problem). Produces interpretable code, not black-box answers.
: See [[entities/funsearch]]

**Future of Life Institute** _(entity: org)_
: Research organization publishing the AI Safety Index — an independent evaluation of AI companies across 33 indicators in 6 safety domains, with grades from F to C+.
: See [[entities/future-of-life-institute]]

## G

**G-Eval** _(entity: paper)_
: LLM-as-a-Judge scoring method using chain-of-thought reasoning before evaluation; generates evaluation steps from task criteria, produces scores (1-5), and optionally normalizes via token probabilities for stability.
: See [[entities/g-eval]]

**Gaussian Splatting** _(concept)_
: Explicit 3D scene representation using millions of anisotropic Gaussian primitives rendered via GPU rasterization -- 10-50x faster than NeRF with 90% less memory, achieving 60fps+ real-time rendering and adopted by Zillow, Esri, and DJI in production.
: See [[concepts/gaussian-splatting]]

**Gemma (Google)** _(entity: tool)_
: Google's open-weight SLM family — Gemma 3 4B offers 128K context and multimodal vision in 3GB VRAM; Gemma 270M runs 25 conversations on 0.75% phone battery.
: See [[entities/gemma]]

**GenCast** _(entity: tool)_
: DeepMind's diffusion-based weather forecasting model. Outperforms ECMWF ENS on 97.2% of metrics, produces 15-day ensemble forecasts in 8 minutes on one TPU. Published in Nature (Dec 2024). Successor: WeatherNext 2.
: See [[entities/gencast]]

**Generative Chemistry** _(concept)_
: AI systems that design novel molecular structures from scratch for drug discovery — using generative models, reinforcement learning, and physics-based optimization. Insilico Medicine's generative approach achieved 30-month target-to-Phase-I (vs 6-8 years traditional).
: See [[concepts/generative-chemistry]]

**Genie (DeepMind)** _(entity: tool)_
: DeepMind's foundation world model series: Genie 1 (2D worlds), Genie 2 (interactive 3D from single images, Dec 2024), Genie 3 (real-time 24fps 720p, Aug 2025) — generating interactive environments for embodied AI agent training.
: See [[entities/genie]]

**Geoffrey Hinton** _(entity: person)_
: The 'Godfather of AI.' Won 2024 Nobel Prize in Physics (with Hopfield) for foundational work on neural networks. Pioneered Boltzmann machines, popularized backpropagation, and enabled modern deep learning. Now prominent AI safety advocate.
: See [[entities/geoffrey-hinton]]

**GitHub Copilot** _(entity: tool)_
: The industry-standard AI coding assistant at $10-21/mo, used by 90% of Fortune 100, offering inline completions, chat, and agent mode across VS Code, JetBrains, and Neovim — pragmatic and frictionless but limited in reasoning depth.
: See [[entities/github-copilot]]

**Glean** _(entity: tool)_
: AI-powered enterprise search platform built on Enterprise Graph architecture. Integrates with 100+ SaaS apps. Series F funding ($150M). Combines semantic search, RAG, permission-aware access, code intelligence, and agentic workflows. Market leader in unified enterprise search.
: See [[entities/glean]]

**GNoME** _(entity: tool)_
: Graph Networks for Materials Exploration — DeepMind's GNN-based system that discovered 2.2M new crystal structures (800 years equivalent). 380K stable candidates, 52K graphene-like compounds, 528 lithium-ion conductors. Published in Nature (2023).
: See [[entities/gnome]]

**Google Agent Development Kit (ADK)** _(entity: tool)_
: Google's framework for building AI agents with integrated support for six protocols: MCP (tools), A2A (agent collaboration), UCP (commerce), AP2 (payments), A2UI (dynamic UI), AG-UI (streaming).
: See [[entities/google-adk]]

**Google NotebookLM** _(entity: tool)_
: Google's AI notebook product that allows users to upload documents and ask questions -- the closest existing product to Karpathy's vision, but lacking persistent wiki compilation and the filing loop.
: See [[entities/google-notebooklm]]

**Google TPU** _(entity: tool)_
: Google's custom AI accelerator: 7 generations (2015-2025); Ironwood v7 at 4,614 TFLOPS and 42.5 exaFLOPS per pod; Gemini 3 trained entirely on TPUs; optical circuit switching (v4+); ~3x energy efficiency over GPUs.
: See [[entities/google-tpu]]

**GPT (Generative Pre-trained Transformer)** _(entity: paper)_
: OpenAI's decoder-only transformer family using causal language modeling — from GPT-1 (117M, 2018) to GPT-3 (175B, 2020) to GPT-4, establishing the decoder-only paradigm as the dominant LLM architecture.
: See [[entities/gpt]]

**Graphite** _(entity: tool)_
: AI code review tool with 96% positive feedback rate and 55% developer action rate (exceeding 49% for human reviewers) — launched October 2025 with stacked PR support and conversational AI interface.
: See [[entities/graphite]]

**Graphiti** _(entity: tool)_
: An open-source framework by Zep for building temporal context graphs where facts have validity windows, designed for AI agents operating in dynamic environments.
: See [[entities/graphiti]]

**GraphRAG** _(concept)_
: Microsoft's graph-based RAG variant that constructs knowledge graphs from text, clusters them into communities with pre-generated summaries, enabling holistic and aggregate queries that baseline RAG cannot answer.
: See [[concepts/graphrag]]

**Groq** _(entity: org)_
: Designed the Language Processing Unit (LPU) for deterministic ultra-low-latency inference; acquired by NVIDIA for $20B to integrate into Rubin platform; 70,000+ developers on GroqCloud; previously valued at $6.9B.
: See [[entities/groq]]

**Grounding and Faithfulness** _(concept)_
: Techniques for anchoring LLM outputs to source material and external knowledge — RAG, knowledge graph integration, span-level attribution, and faithfulness checking — as the primary defense against hallucination.
: See [[concepts/grounding-and-faithfulness]]

**Grouped-Query Attention (GQA)** _(concept)_
: Attention variant sharing KV heads across groups of query heads — interpolating between full multi-head attention (MHA) and multi-query attention (MQA) to reduce KV cache memory with minimal quality loss.
: See [[concepts/grouped-query-attention]]

## H

**Hallucination Contamination** _(concept)_
: The risk that LLM-generated errors written into a wiki propagate into future queries and fine-tuning, corrupting the knowledge base over time.
: See [[concepts/hallucination-contamination]]

**Hallucination Detection** _(concept)_
: Methods for detecting LLM hallucinations: white-box (token probability, semantic entropy), black-box (perturbation, SLM/LLM-as-judge), and rubric-based approaches achieving 0.81-0.86 F1 on production benchmarks.
: See [[concepts/hallucination-detection]]

**HAX Toolkit (Human-AI Experience)** _(entity: tool)_
: Microsoft Research's design library for human-AI interaction — provides guidelines and patterns for first-run experience, during interaction, error handling, and long-term engagement in AI products.
: See [[entities/hax-toolkit]]

**Helix VLA (Figure AI)** _(entity: framework)_
: Figure AI's proprietary Vision-Language-Action system replacing the OpenAI partnership; Helix 02 (Jan 2026) enables full-body humanoid autonomy trained via motion capture + simulation; controls up to 2 robots simultaneously.
: See [[entities/helix-vla]]

**HELM (Holistic Evaluation of Language Models)** _(entity: dataset)_
: The most comprehensive academic LLM evaluation framework: 42 scenarios, 7 evaluation metrics, 16+ models with standardized methodology and public leaderboard.
: See [[entities/helm]]

**Hierarchical Memory** _(concept)_
: Multi-tier memory for LLM agents: working memory (in-context), episodic memory (session summaries), semantic memory (entity abstractions), and archival memory (external DB) — inspired by both OS design and cognitive science.
: See [[concepts/hierarchical-memory]]

**Hierarchical Retrieval** _(concept)_
: Retrieval across multiple levels of abstraction — from raw chunks to summaries to themes — addressing the limitation that standard RAG only fetches short contiguous text fragments.
: See [[concepts/hierarchical-retrieval]]

**HNSW (Hierarchical Navigable Small World)** _(concept)_
: The dominant graph-based ANN algorithm for vector search: a multi-layer proximity graph enabling O(log n) nearest-neighbor queries with 80-99% recall at 1-50ms latency, used by nearly all major vector databases.
: See [[concepts/hnsw]]

**HTML to Markdown Conversion** _(concept)_
: Converting extracted HTML content to clean markdown — from rule-based libraries (Turndown, html2text, Pandoc) to neural models (Reader-LM v2, ROUGE-L 0.86) — the format bridge between web content and LLM-consumable knowledge.
: See [[concepts/html-to-markdown-conversion]]

**Huawei** _(entity: org)_
: China's leading AI chip maker: Ascend 910C achieves only 60% of Nvidia H100 real-world performance; constrained to SMIC 7nm manufacturing; next-gen chip will be less powerful than current; produces 4-5% of Nvidia's output even in aggressive scenarios.
: See [[entities/huawei]]

**Human-AI Collaboration** _(concept)_
: How humans and AI systems work together in knowledge creation — ranging from AI as research assistant to AI as full participant — with the sobering finding that human-only teams currently outperform human-AI teams in information sharing.
: See [[concepts/human-ai-collaboration]]

**Human-AI Collaboration Design** _(concept)_
: The product design discipline for AI collaboration interfaces — five principles (Transparency, Personalization, Control, Resilience, Trust) with fluid control between human and AI; grounded in the finding that more engagement mechanisms can paradoxically harm performance.
: See [[concepts/human-ai-collaboration-design]]

**Human-in-the-Loop** _(concept)_
: Design patterns embedding human judgment into AI workflows — synchronous approval, asynchronous audit, confidence-based escalation — and their evolution toward AI-governing-AI as agentic systems outpace human review capacity.
: See [[concepts/human-in-the-loop]]

**Humanoid Robots** _(concept)_
: Human-shaped robots designed to navigate existing infrastructure without modification; market projected at $30-50B by 2035 (UBS); key players include Tesla Optimus ($20-30K target), Figure AI ($39B valuation), Boston Dynamics Atlas, 1X NEO, and Unitree; form factor wins on infrastructure compatibility.
: See [[concepts/humanoid-robots]]

**Hybrid Retrieval** _(concept)_
: Combining knowledge graphs and vector databases for AI retrieval: graphs provide entity relationships, permissions, and multi-hop reasoning while vectors enable semantic search over unstructured content.
: See [[concepts/hybrid-retrieval]]

**Hybrid Search** _(concept)_
: Combining BM25/SPLADE keyword search with dense vector search in parallel, merging via RRF or convex combination — yielding +26-31% NDCG improvement on BEIR benchmarks over single-method retrieval.
: See [[concepts/hybrid-search]]

**Hypertext** _(concept)_
: Nonsequential writing with reader-chosen paths through linked documents — coined by Ted Nelson in 1965, rooted in Bush's Memex (1945), partially realized by the World Wide Web, and foundational to wiki-based knowledge systems.
: See [[concepts/hypertext]]

## I

**IBM NorthPole** _(entity: tool)_
: IBM's neuromorphic AI chip eliminating the von Neumann bottleneck through 256 co-located memory-compute cores — 72.7x more energy efficient than GPUs for LLM inference, entering full-scale production in 2026.
: See [[entities/ibm-northpole]]

**IBM Research** _(entity: org)_
: IBM's AI research division: developed predictive LLM routing using HELM benchmarks, demonstrating GPT-4-matching quality at 5 cents/query savings through intelligent model selection.
: See [[entities/ibm-research]]

**Identity Preference Optimization (IPO)** _(concept)_
: A DPO variant that replaces logit functions with identity functions and adds regularization to prevent overfitting -- addressing DPO's tendency to overfit preference data, especially with deterministic preferences.
: See [[concepts/ipo]]

**Ilya Sutskever** _(entity: person)_
: Co-founder of OpenAI, architect of the scaling paradigm (AlexNet, GPT series); departed to found SSI in 2024; declared 'the age of scaling is ending' in 2025, pivoting to research-driven breakthroughs for safe superintelligence.
: See [[entities/ilya-sutskever]]

**Image Captioning** _(concept)_
: Automatically generating natural language descriptions of images; evolved from CNN+LSTM through attention/transformers to multimodal LLMs; critical for making visual content searchable in knowledge bases.
: See [[concepts/image-captioning]]

**Image Generation** _(concept)_
: The field of AI-driven image synthesis from text, image, or other inputs -- dominated in 2026 by diffusion-based models (FLUX, SD3, Midjourney) using DiT architectures and flow matching, with autoregressive approaches (LlamaGen, NextStep-1) emerging as serious competitors.
: See [[concepts/image-generation]]

**Image Understanding** _(concept)_
: The AI capability of interpreting, analyzing, and reasoning about visual content — from object recognition to chart analysis to document comprehension; now a core feature of leading LLMs.
: See [[concepts/image-understanding]]

**Incremental ETL and Change Data Capture** _(concept)_
: Processing only new or changed data rather than full rebuilds: watermark-based tracking, CDC from database logs, append-only/upsert/SCD2 patterns, and LlamaIndex's docstore deduplication — reducing compute by 10-100x.
: See [[concepts/incremental-etl]]

**Inference Scaling Laws** _(concept)_
: Formal mathematical relationships governing how LLM performance scales with inference-time compute -- the deployment-side counterpart to Chinchilla training scaling laws, establishing inference compute as an independently optimizable axis.
: See [[concepts/inference-scaling-laws]]

**Infinite Context** _(concept)_
: Architectural approaches to unbounded sequence processing: StreamingLLM (attention sinks), Infini-attention (compressive memory), Ring Attention (multi-device), InfLLM (external lookup) — each with different tradeoffs in retrieval, training, and hardware.
: See [[concepts/infinite-context]]

**Information Architecture** _(concept)_
: The structural design of shared information environments -- organization, labeling, search, and navigation systems. IA operates across all information management levels (not just presentation), determining how taxonomies and ontologies are applied to user experience. Critical for enterprise knowledge scaling: determines what knowledge is visible, findable, and navigable.
: See [[concepts/information-architecture]]

**Information Extraction with LLMs** _(concept)_
: The discipline of automatically extracting structured knowledge (entities, relations, claims, facts) from unstructured text using LLMs — the foundational capability enabling wiki compilation pipelines.
: See [[concepts/information-extraction]]

**Insilico Medicine** _(entity: org)_
: AI drug discovery company using generative chemistry. Lead program rentosertib (ISM001-055) for pulmonary fibrosis achieved 30-month target-to-Phase-I (vs 6-8 years traditional). Phase IIa positive results. Founded by Alex Zhavoronkov.
: See [[entities/insilico-medicine]]

**InstructGPT** _(entity: paper)_
: OpenAI's 2022 paper that demonstrated the three-step RLHF pipeline (SFT, reward model training, PPO) at scale, producing a 1.3B parameter model preferred over the 175B GPT-3 -- the direct precursor to ChatGPT.
: See [[entities/instructgpt]]

**Instruction Tuning** _(concept)_
: Fine-tuning a pretrained LLM on instruction-response pairs to make it follow human instructions — the bridge between raw pretraining and RLHF alignment, with dataset choice critically affecting which skills emerge.
: See [[concepts/instruction-tuning]]

**Instructor** _(entity: tool)_
: The most popular Python library for structured LLM extraction (3M+ monthly downloads) — uses Pydantic models with automatic validation and retry across 15+ providers.
: See [[entities/instructor]]

**Intel Loihi** _(entity: tool)_
: Intel's family of neuromorphic processors — from Loihi 1 (2018, 130K neurons, research-only) through Loihi 3 (2025, 8M neurons, first commercial neuromorphic chip), achieving 100-1000x GPU energy efficiency for sensory and robotic AI tasks.
: See [[entities/intel-loihi]]

**Intelligence Explosion** _(concept)_
: The hypothesis that AGI could automate AI research itself, compressing decades of progress into months — producing superintelligence rapidly and creating the most consequential event in human history.
: See [[concepts/intelligence-explosion]]

**Isomorphic Labs** _(entity: org)_
: Demis Hassabis-founded (2021) drug discovery company leveraging AlphaFold's capabilities to build a unified drug design engine. Represents the commercial translation of DeepMind's structural biology AI into pharmaceutical development.
: See [[entities/isomorphic-labs]]

## J

**Jason Wei** _(entity: person)_
: Google Brain / DeepMind researcher, first author of the foundational Chain-of-Thought Prompting paper (2022) and co-first author of the Emergent Abilities paper (2022), two of the most influential works in LLM reasoning.
: See [[entities/jason-wei]]

**JEPA (Joint Embedding Predictive Architecture)** _(concept)_
: Yann LeCun's Joint Embedding Predictive Architecture: predicts representations rather than pixels using energy-based models, avoiding both generative intractability and contrastive dimensionality curse — the foundation for I-JEPA, V-JEPA, V-JEPA 2, H-JEPA, and LeWorldModel.
: See [[concepts/jepa]]

**Jina Reader API** _(entity: tool)_
: Jina's Reader API converts any URL to LLM-friendly markdown by prefixing r.jina.ai/ — uses headless Chrome + Readability + Turndown, with optional ReaderLM v2 neural engine.
: See [[entities/jina-reader]]

**John McCarthy** _(entity: person)_
: American computer scientist (1927-2011) who coined 'artificial intelligence' (1956), invented LISP (1958), proposed the Advice Taker, and championed logic-based AI — founding the 'neat' tradition.
: See [[entities/john-mccarthy]]

**Julie Zhuo** _(entity: person)_
: Former VP Design at Facebook/Meta; influential product design voice arguing that conversational UI was a breakthrough of obviousness but has five critical limitations, with AI personalization as the billion-dollar opportunity.
: See [[entities/julie-zhuo]]

**Jürgen Schmidhuber** _(entity: person)_
: AI pioneer at IDSIA/KAUST; co-inventor of LSTM, co-author of World Models (2018); long advocate for curiosity-driven learning and world model-based planning.
: See [[entities/jurgen-schmidhuber]]

## K

**Kahneman-Tversky Optimization (KTO)** _(concept)_
: A prospect-theory-based alignment method that uses binary desirable/undesirable signals instead of pairwise preferences, outperforming DPO on noisy real-world data and matching SFT+DPO combined on Llama models.
: See [[concepts/kto]]

**Karl Friston** _(entity: person)_
: British neuroscientist at UCL who formulated the free energy principle — a unified mathematical framework for brain function connecting perception, action, and learning, with direct links to variational autoencoders and generative AI.
: See [[entities/karl-friston]]

**KARMA** _(entity: paper)_
: A NeurIPS 2025 Spotlight paper presenting a nine-agent LLM framework for automated knowledge graph enrichment from unstructured scientific text.
: See [[entities/karma]]

**KARMA** _(entity: paper)_
: NeurIPS 2025 Spotlight paper: 9-agent LLM framework for automated knowledge graph enrichment from unstructured text, achieving 83.1% accuracy and 38,230 new entities from 1,200 PubMed papers.
: See [[entities/karma-framework]]

**Keyword Search** _(concept)_
: Lexical search using inverted indexes and BM25 ranking: fast, deterministic, and precise for exact terms, but blind to synonyms and conceptual relationships.
: See [[concepts/keyword-search]]

**KGGen** _(entity: tool)_
: Open-source Python library for extracting knowledge graphs from text via a 3-stage pipeline (generate, aggregate, cluster), achieving 66% on the MINE benchmark — 18% above GraphRAG.
: See [[entities/kggen]]

**Kling** _(entity: tool)_
: ByteDance's AI video generation model -- Kling 3.0 (Feb 2026) leads on cost efficiency at $0.07/second with multi-shot sequences, character lock consistency, native audio with lip sync in 5 languages, and clips up to 3 minutes.
: See [[entities/kling]]

**Knowledge Base Product Gap** _(concept)_
: Karpathy's own acknowledgment that the current LLM-KB is 'a hacky collection of scripts' — and the product opportunity to build polished tooling that makes AI-maintained wikis accessible to non-technical users.
: See [[concepts/knowledge-base-product-gap]]

**Knowledge Commons** _(concept)_
: Collectively owned and managed knowledge resources (Wikipedia, open-source, Creative Commons) — non-subtractible unlike natural commons — now facing an existential challenge as AI extracts value from commons data while potentially degrading the ecosystems that produce it.
: See [[concepts/knowledge-commons]]

**Knowledge Distillation** _(concept)_
: Transferring capabilities from large teacher models to small student models via logit matching, feature mimicry, or rationale extraction — enabling deployment-friendly models at a fraction of the cost.
: See [[concepts/knowledge-distillation]]

**Knowledge Editing** _(concept)_
: Targeted modification of specific factual associations in model weights without full retraining — via methods like ROME (single facts) and MEMIT (thousands of facts) — with inherent scalability limits.
: See [[concepts/knowledge-editing]]

**Knowledge Extraction** _(concept)_
: LLM-driven extraction of entities, relations, and facts from unstructured text — the core pipeline stage of knowledge graph construction, now achieving near-expert accuracy via few-shot prompting.
: See [[concepts/knowledge-extraction]]

**Knowledge Fusion** _(concept)_
: The process of merging, deduplicating, and reconciling extracted knowledge from multiple sources into a unified knowledge graph — addressing entity alignment, schema reconciliation, and conflict resolution.
: See [[concepts/knowledge-fusion]]

**Knowledge Governance** _(concept)_
: The policies, processes, roles, and standards governing how knowledge is created, validated, maintained, and retired in an organization. Governance maturity is a prerequisite (not afterthought) to scaling knowledge systems. Includes access control (NIST SP 800-53), validation pipelines, content ownership, and emerging AI Governance departments.
: See [[concepts/knowledge-governance]]

**Knowledge Graph** _(concept)_
: Formal representation of knowledge as nodes (entities) and edges (relationships), with three distinct modern approaches: KARMA (automated multi-agent enrichment), Graphiti (temporal context graphs), and Gallagher's Knowledge Graph Kit (personal SQLite graph).
: See [[concepts/knowledge-graph]]

**Knowledge Graph Completion** _(concept)_
: Predicting missing facts in incomplete knowledge graphs via link prediction, relation prediction, and triple classification — now dramatically improved by LLM-based approaches outperforming traditional embedding methods.
: See [[concepts/knowledge-graph-completion]]

**Knowledge Graph Construction** _(concept)_
: The end-to-end process of building knowledge graphs from unstructured data, now transformed by LLMs from rule-based pipelines to generative frameworks achieving near-human-expert quality.
: See [[concepts/knowledge-graph-construction]]

**Knowledge Graph Embeddings** _(concept)_
: Machine learning methods that map knowledge graph entities and relations to continuous vector spaces for link prediction, with three model families (translational, tensor decomposition, deep learning) increasingly complemented by LLM approaches.
: See [[concepts/knowledge-graph-embeddings]]

**Knowledge Management Challenges** _(concept)_
: Systematic inventory of enterprise KM obstacles: lack of executive/employee buy-in, outdated tools, unstructured processes, knowledge silos, workflow integration difficulties, scaling challenges, ROI measurement difficulty. Well-implemented KM generates 200-400% ROI in year one, but fewer than 40% of organizations can articulate clear ROI metrics.
: See [[concepts/knowledge-management-challenges]]

**Knowledge Representation** _(concept)_
: The AI discipline of encoding information so machines can reason over it — spanning 65+ years from logic and frames through expert systems, ontologies, and knowledge graphs to modern LLM-based implicit representations.
: See [[concepts/knowledge-representation]]

**Knowledge Silos** _(concept)_
: Critical knowledge trapped within specific teams, departments, or systems. 79% of employees confirm siloed information; ~3.7 hours/day lost (2h redundant tasks + 1.7h repeated questions). Revenue impact up to 30%. Primary solutions: unified enterprise search, cultural change, and cross-team knowledge governance.
: See [[concepts/knowledge-silos]]

**Knowledge Storage in Transformers** _(concept)_
: How transformer LLMs store and retrieve factual knowledge: MLP layers act as key-value memories storing facts in their weight matrices, while attention heads serve as routing mechanisms — together forming 'knowledge circuits' that enable surgical knowledge editing.
: See [[concepts/knowledge-storage-in-transformers]]

**Knowledge System Scaling** _(concept)_
: The process of expanding knowledge infrastructure to serve thousands of concurrent users across heterogeneous data environments while maintaining consistency. Three complexity dimensions (Volume, Velocity, Variety), four-phase architecture (partition/federation, indexing, validation, governance), and critical decision boundaries (CAP theorem, governance maturity threshold).
: See [[concepts/knowledge-system-scaling]]

**KV Cache** _(concept)_
: The key-value cache stores pre-computed attention vectors to avoid recalculation during autoregressive decoding; its management (PagedAttention, GQA, SWA) is the central bottleneck of LLM inference.
: See [[concepts/kv-cache]]

## L

**LangChain** _(entity: tool)_
: Open-source LLM application framework: document loaders, RecursiveCharacterTextSplitter for chunking, chains (Stuff/Refine/MapReduce) for document processing, and extensive LLM provider integrations.
: See [[entities/langchain]]

**LangGraph** _(entity: tool)_
: LangChain's framework for building stateful, multi-step LLM applications as state machines with cycles, conditional logic, and agent loops — the primary implementation platform for agentic RAG.
: See [[entities/langgraph]]

**Language Grounding for Robots** _(concept)_
: The challenge of connecting abstract language understanding to concrete physical capabilities in robots — addressed through affordance grounding (SayCan), 3D scene graphs (SayPlan), closed-loop feedback, and end-to-end VLA models (RT-2, π0).
: See [[concepts/language-grounding-for-robots]]

**Late Interaction Retrieval** _(concept)_
: A retrieval paradigm between bi-encoders and cross-encoders: independently encode queries and documents into per-token embeddings, then compute fine-grained MaxSim scoring at query time — balancing accuracy and speed.
: See [[concepts/late-interaction-retrieval]]

**Latent Reasoning** _(concept)_
: Reasoning in continuous hidden state space rather than through explicit token generation -- potentially more efficient than chain-of-thought by enabling breadth-first search, but currently suffering performance degradation on some tasks.
: See [[concepts/latent-reasoning]]

**Latent World Models** _(concept)_
: World models that compress observations into compact latent representations and predict dynamics there — from Ha & Schmidhuber's 32-dim VAE to DreamerV3's RSSM to V-JEPA 2's 1.2B-param ViT — enabling sample-efficient planning through imagination.
: See [[concepts/latent-world-models]]

**Learning in Public** _(concept)_
: The practice of sharing your learning journey as it happens — publishing half-finished thoughts with epistemic status markers, embracing imperfection, and reducing friction between learning and publishing — core to the digital garden philosophy.
: See [[concepts/learning-in-public]]

**Learning Rate Schedules** _(concept)_
: How the learning rate varies during LLM training: warmup phase (linear ramp, 1-10% of steps), followed by cosine decay or the newer Warmup-Stable-Decay (WSD) schedule. Critical for both stability and final model quality.
: See [[concepts/learning-rate-schedules]]

**Leopold Aschenbrenner** _(entity: person)_
: Former OpenAI superalignment researcher; author of 'Situational Awareness' predicting AGI by 2027; founder of $1.5B+ hedge fund; one of the most influential voices shaping AI policy and investment discourse.
: See [[entities/leopold-aschenbrenner]]

**Lilian Weng** _(entity: person)_
: OpenAI researcher and author of Lil'Log, producing definitive technical surveys on topics including reward hacking, agents, prompt engineering, and LLM training -- widely cited in the ML community.
: See [[entities/lilian-weng]]

**Linear Attention** _(concept)_
: Approximating softmax attention by decomposing it via kernel functions to avoid materializing the N x N attention matrix — reducing complexity from O(N^2 * d) to O(N * d^2), but with significant expressiveness tradeoffs that limit practical adoption.
: See [[concepts/linear-attention]]

**Linting and Health Checks** _(concept)_
: LLM-driven health checks over the compiled wiki to find inconsistencies, fill data gaps, detect broken links, identify orphan articles, and suggest new content.
: See [[concepts/linting-and-health-checks]]

**Llama** _(entity: tool)_
: Meta's open-source LLM family, with Llama 3.1 8B used in the Decoding AI second-brain RAG pipeline as the fine-tuned summarization model.
: See [[entities/llama]]

**llama.cpp** _(entity: tool)_
: C/C++ LLM inference engine — foundation for Ollama; supports GGUF format, 1.5-8 bit quantization, CPU+GPU splitting; runs on every platform from phones to servers.
: See [[entities/llama-cpp]]

**LlamaIndex** _(entity: tool)_
: Leading RAG framework with composable ingestion pipeline: SimpleDirectoryReader + LlamaParse + LlamaHub loaders, node parsers for chunking, cache-optimized transformations, docstore deduplication, and automatic vector store integration.
: See [[entities/llamaindex]]

**LlamaParse** _(entity: tool)_
: LlamaIndex's managed PDF parsing API: best-in-class for complex tables and figures, integrates natively with LlamaIndex ingestion pipeline, proprietary cloud service.
: See [[entities/llamaparse]]

**LLM Agent Architecture** _(concept)_
: The four-component architecture of LLM agents (brain, memory, planning, tools) and the design pattern spectrum from simple LLM+prompt to multi-agent systems.
: See [[concepts/llm-agent-architecture]]

**LLM API Pricing** _(concept)_
: LLM API pricing landscape in 2026: prices dropped ~80% since early 2025; output tokens cost 3-5x more than input; premium-to-lightweight gap is 60-300x; batch APIs offer 50% discounts.
: See [[concepts/llm-api-pricing]]

**LLM Applications Beyond Code** _(concept)_
: The expanding frontier of LLM applications beyond code generation — writing, research, education, science, healthcare, law, creative work — representing Karpathy's 'knowledge manipulation' shift across all professional domains.
: See [[concepts/llm-applications-beyond-code]]

**LLM as Search Operator** _(concept)_
: A paradigm where LLMs generate creative candidate solutions in evolutionary loops while automated evaluators verify correctness — filtering hallucinations while leveraging creativity. FunSearch and AlphaEvolve demonstrate this produces genuine scientific discoveries.
: See [[concepts/llm-as-search-operator]]

**LLM Benchmarks** _(concept)_
: Standardized evaluation datasets for comparing LLM capabilities: MMLU (knowledge), HELM (holistic), TruthfulQA (factuality), HumanEval (code), MT-Bench (conversation), Chatbot Arena (crowdsourced), with 15 benchmarks in active use by 2026.
: See [[concepts/llm-benchmarks]]

**LLM Cost Optimization** _(concept)_
: Strategies for reducing LLM API and infrastructure costs by 50-85%: prompt optimization, caching (prompt + semantic), model routing, batching, output constraints, and self-hosting at scale.
: See [[concepts/llm-cost-optimization]]

**LLM Creative Applications** _(concept)_
: LLMs as creative tools — story writing (Gemini 3 Pro #1 on LM Arena), ideation (brainstorming adoption +12%), interactive storytelling, and creative direction — with the paradox that AI improves individual output while homogenizing collective creativity.
: See [[concepts/llm-creative-applications]]

**LLM Data Analysis** _(concept)_
: LLMs automate data analysis via natural language to code translation, but face a critical executability-correctness gap: code that runs is not always code that works (88% correct at simple tasks, 0% at complex). Self-correction loops improve performance by up to 52.5%.
: See [[concepts/llm-data-analysis]]

**LLM Education and Tutoring** _(concept)_
: LLM-powered tutoring systems achieve significant learning gains (Physics-STAR: 100% score increase, Tutorly: +15pp, AgentTutor: +24-30pp) using IRT models, Bayesian mastery tracking, and multi-agent architectures — spanning STEM, soft skills, and teacher development.
: See [[concepts/llm-education-tutoring]]

**LLM Evaluation Metrics** _(concept)_
: Taxonomy of metrics for evaluating LLM output quality: statistical scorers (BLEU, ROUGE, BERTScore), LLM-as-a-Judge methods (G-Eval, QAG), and domain-specific metrics for RAG, agents, safety, and factuality.
: See [[concepts/llm-evaluation-metrics]]

**LLM Hallucination** _(concept)_
: When LLMs generate fluent but factually incorrect or unsupported text — classified by type (factuality vs. faithfulness, intrinsic vs. extrinsic), caused across the full development lifecycle, and addressed through detection and mitigation taxonomies.
: See [[concepts/llm-hallucination]]

**LLM Healthcare Applications** _(concept)_
: Seven healthcare LLM domains — clinical decision support (GPT-4: 93.1% USMLE), education, patient care, literature, drug discovery, radiology, documentation — with specialized models (Med-PaLM, GatorTron, LLaVA-Med) and critical hallucination/bias challenges.
: See [[concepts/llm-healthcare-applications]]

**LLM Inference Optimization** _(concept)_
: The umbrella discipline of reducing latency, cost, and resource consumption of LLM inference through KV cache management, batching, quantization, speculative decoding, and serving infrastructure.
: See [[concepts/llm-inference-optimization]]

**LLM Knowledge Base** _(concept)_
: A personal knowledge base where an LLM authors and maintains all wiki content from raw ingested sources, with humans interacting only via natural language.
: See [[concepts/llm-knowledge-base]]

**LLM Legal Applications** _(concept)_
: LLM adoption in legal surged from 19% to 79% in one year (Clio 2024) — three primary use cases (document review, drafting, research) with tools like Everlaw, Luminance, Casetext — transforming lawyers from drafters to curators.
: See [[concepts/llm-legal-applications]]

**LLM OS** _(concept)_
: Karpathy's metaphor reframing LLMs not as chatbots but as the kernel of a new operating system: CPU (reasoning), RAM (context window), filesystem (RAG), with natural language as the programming interface.
: See [[concepts/llm-os]]

**LLM Pretraining** _(concept)_
: The foundational training phase where LLMs learn language by predicting the next token across trillions of tokens of text — the most compute-intensive and expensive stage of the LLM pipeline, costing $5M-$200M for frontier models.
: See [[concepts/llm-pretraining]]

**LLM Product Development** _(concept)_
: Building LLM-powered products requires fundamentally different practices: thin-slice MVPs, provisional approvals over lengthy validation, Master LLM routing, customer-driven training, and first iterations focused on data collection rather than polish.
: See [[concepts/llm-product-development]]

**LLM Q&A Over Documents** _(concept)_
: Using an LLM agent to answer complex questions over a compiled wiki by reading index files and summaries to navigate to relevant full articles, without needing a vector database.
: See [[concepts/llm-qa-over-documents]]

**LLM Reasoning** _(concept)_
: The ability of large language models to perform multi-step inference, logical deduction, and problem-solving -- achieved through prompting techniques (CoT, ToT), training methods (RL), and inference-time scaling, though the nature and limits of this reasoning remain deeply debated.
: See [[concepts/llm-reasoning]]

**LLM Reasoning Limitations** _(concept)_
: Systematic catalogue of LLM reasoning failures: fragility to irrelevant information (up to 65% drops), sensitivity to numerical variations, compositional reasoning breakdowns, and architectural root causes in next-token prediction and attention mechanisms.
: See [[concepts/llm-reasoning-limitations]]

**LLM Serving Frameworks** _(concept)_
: Production software for serving LLM inference: vLLM (production default, broadest hardware), SGLang (throughput leader, multi-turn specialist), Triton (enterprise NVIDIA), with TGI in maintenance mode since Dec 2025.
: See [[concepts/llm-serving-frameworks]]

**LLM Summarization Techniques** _(concept)_
: Extractive vs. abstractive summarization with LLMs — in practice LLMs are more extractive than expected; hybrid extract-then-abstract approaches produce the most reliable wiki summaries.
: See [[concepts/llm-summarization]]

**LLM Training Costs** _(concept)_
: Frontier LLM training costs $5M-$200M, dominated by GPU compute (70-80%). GPT-4 ~$100-150M, Gemini Ultra ~$191M, Llama 3.1 405B ~$170M. DeepSeek V3's $5.6M challenged the assumption that frontier requires $100M+.
: See [[concepts/llm-training-costs]]

**LLM World Understanding** _(concept)_
: The contested question of whether LLMs develop genuine internal world models through next-token prediction — split 50-50 in the research community, with Sutskever arguing yes (compressed representations) and LeCun arguing no (text alone can never capture physical reality).
: See [[concepts/llm-world-understanding]]

**LLM-as-a-Judge** _(concept)_
: Using powerful LLMs (GPT-4, Claude) to evaluate outputs from other LLMs; achieves 80-85% human agreement but exhibits position, verbosity, and self-enhancement biases requiring active mitigation.
: See [[concepts/llm-as-judge]]

**llm.c** _(entity: tool)_
: LLM training in pure C/CUDA: ~3,000 lines reproducing GPT-2 (124M) in 90 minutes for $20, running 7% faster than PyTorch — Karpathy's proof that frameworks are optional.
: See [[entities/llm-c]]

**LLMs as Knowledge Bases** _(concept)_
: The question of whether LLMs' implicit parametric knowledge can replace traditional KBs — evaluated at only ~32% consistent correctness, motivating hybrid approaches where explicit structured knowledge complements LLM reasoning.
: See [[concepts/llms-as-knowledge-bases]]

**LM Studio** _(entity: tool)_
: Desktop GUI application for local LLM inference — polished model browser, Vulkan offloading for integrated GPUs, best entry point for non-technical users.
: See [[entities/lm-studio]]

**Local Knowledge Base** _(concept)_
: Running an LLM-powered knowledge base entirely on local hardware — using Ollama + open-source models + ChromaDB/FAISS — for privacy, offline operation, and zero API costs.
: See [[concepts/local-knowledge-base]]

**Local LLM Inference** _(concept)_
: Running LLM inference on local hardware without cloud APIs, using tools like Ollama, vLLM, llama.cpp, and MLX — enabling privacy, offline operation, and zero per-token cost.
: See [[concepts/local-llm-inference]]

**Logseq** _(entity: tool)_
: Open-source, local-first outliner with block-based architecture, bidirectional linking, and advanced querying — positioned between Obsidian (markdown-first) and Roam (cloud-first) in the PKM tool landscape.
: See [[entities/logseq]]

**Long-Context Models** _(concept)_
: Models designed for extended context: Gemini (1-2M), Claude (200K-1M), Llama 4 Scout (10M), Magic LTM-2-Mini (100M) — each with distinct architecture-efficiency tradeoffs.
: See [[concepts/long-context-models]]

**Loss Spikes** _(concept)_
: Sudden catastrophic increases in training loss caused by gradient norm explosions (up to 1000x normal), which can degrade or ruin expensive LLM pretraining runs. Preventable through proper initialization, embedding normalization, and gradient clipping.
: See [[concepts/loss-spikes]]

**Lost in the Middle** _(concept)_
: LLMs exhibit a U-shaped performance curve — best at beginning/end of context, >30% degradation in the middle — caused by attention accumulation patterns in transformers.
: See [[concepts/lost-in-the-middle]]

**Lost in the Middle (Paper)** _(entity: paper)_
: Liu et al. (Stanford/UC Berkeley, TACL 2023): landmark paper documenting the U-shaped performance curve where LLMs perform best on beginning/end information and >30% worse on middle-positioned content.
: See [[entities/lost-in-the-middle-paper]]

## M

**Maggie Appleton** _(entity: person)_
: Designer, illustrator, and anthropologist who compiled the definitive history and pattern language of digital gardens — identifying six core principles that distinguish gardens from traditional blogs.
: See [[entities/maggie-appleton]]

**Magic / LTM-2-Mini** _(entity: tool)_
: Magic's LTM-2-Mini: 100M token context model using a novel sequence-dimension algorithm 1,000x cheaper than standard attention, requiring a fraction of one H100 vs 638 for Llama 405B.
: See [[entities/magic-ltm]]

**Mamba (Selective State Space Model)** _(concept)_
: The leading SSM architecture making state transitions input-dependent (selective), with hardware-aware kernel fusion and parallel scan — achieving transformer-competitive performance with linear-time inference.
: See [[concepts/mamba]]

**Markdown as Universal Interface** _(concept)_
: Markdown is simultaneously human-readable, LLM-friendly (25-75% fewer tokens than HTML), version-controllable, tool-agnostic, institutionally recommended for preservation, and backed by a massive ecosystem — making it the optimal substrate for AI-era knowledge management.
: See [[concepts/markdown-as-universal-interface]]

**Markdown Ecosystem** _(concept)_
: The constellation of tools, converters, frameworks, and standards that make markdown a practical universal format: Pandoc, MDX, Marp, MarkdownDB, MarkItDown, SSGs, and more.
: See [[concepts/markdown-ecosystem]]

**Markdown for AI Agents** _(concept)_
: LLMs natively comprehend markdown due to training data representation and AST-based tokenization — making it 25-75% more token-efficient than HTML and yielding 89% vs 62% RAG retrieval accuracy.
: See [[concepts/markdown-for-ai-agents]]

**MarkdownDB** _(entity: tool)_
: Open-source JS library that indexes markdown files into SQLite for SQL/JSON querying — files remain on disk as plain text, with the database as a derived index.
: See [[entities/markdowndb]]

**MarkItDown (Microsoft)** _(entity: tool)_
: Microsoft's open-source Python tool for converting PDFs, Office docs, images, audio, and web content to markdown — designed for LLM ingestion pipelines.
: See [[entities/markitdown]]

**Marp** _(entity: tool)_
: A markdown-based presentation framework used within Obsidian to render LLM-generated slide decks as one of the multi-format output options in the knowledge base workflow.
: See [[entities/marp]]

**Marvin Minsky** _(entity: person)_
: American cognitive scientist (1927-2016), co-founder of MIT AI Lab, who developed frame theory for knowledge representation and co-authored 'Perceptrons' (1969) which temporarily halted neural network research.
: See [[entities/marvin-minsky]]

**Mathematical Reasoning in LLMs** _(concept)_
: The capacity of LLMs to solve mathematical problems -- from grade school (GSM8K) to competition level (AIME) -- with reasoning models achieving 96.7% on AIME, yet fundamental fragility persists: performance drops up to 65% with irrelevant information.
: See [[concepts/mathematical-reasoning-llm]]

**Matplotlib** _(entity: tool)_
: A Python plotting library used in the LLM-KB workflow to generate data visualizations that are saved as images and viewed within Obsidian alongside wiki articles.
: See [[entities/matplotlib]]

**Matryoshka Representation Learning** _(concept)_
: Training technique that produces embeddings usable at any dimension by frontloading important information in earlier dimensions — preserving 98.37% of performance at just 8.3% of original size, now standard in state-of-the-art models.
: See [[concepts/matryoshka-representation-learning]]

**MCP Code Execution Pattern** _(concept)_
: Anthropic's optimization pattern: agents write code to interact with MCP tools instead of loading all definitions into context — achieving 98.7% token savings, PII filtering, and persistent state management.
: See [[concepts/mcp-code-execution-pattern]]

**MCP Security** _(concept)_
: Security vulnerabilities and mitigations for MCP: prompt injection through tool descriptions, tool spoofing/lookalike attacks, OAuth token vulnerabilities, toxic agent data exfiltration, and per-server isolation as defense-in-depth.
: See [[concepts/mcp-security]]

**MCP Server Ecosystem** _(concept)_
: The rapidly growing MCP server ecosystem: 12K+ servers across public registries (PulseMCP, mcp.so, MCPMarket), 97M monthly SDK downloads, categories spanning databases to design tools, shift from local stdio to remote HTTP transport.
: See [[concepts/mcp-ecosystem]]

**MCTS for LLM Reasoning** _(concept)_
: Monte Carlo Tree Search adapted for LLM inference: systematic exploration of reasoning paths via selection, expansion, simulation, and backpropagation -- used in o3 at inference time and for training data generation, with multi-model variants achieving 30%+ on ARC-AGI-2.
: See [[concepts/mcts-llm-reasoning]]

**MDX** _(entity: tool)_
: Authoring format that blends markdown with JSX components — 'Markdown for the component era' — with zero runtime, compiling to JavaScript at build time.
: See [[entities/mdx]]

**MDX (Markdown + JSX)** _(concept)_
: MDX extends markdown with JSX components — enabling interactive, component-based content within markdown documents while compiling to JavaScript at build time with zero runtime.
: See [[concepts/mdx]]

**Med-PaLM** _(entity: tool)_
: Google's medical LLM family — Med-PaLM 2 exceeded baseline models by 19% on MultiMedQA, reaching expert-level performance on medical licensing exams and clinical QA benchmarks.
: See [[entities/med-palm]]

**Megatron-LM** _(entity: tool)_
: NVIDIA's framework for training large transformer models, pioneering efficient tensor parallelism (splitting weight matrices within layers) and interleaved pipeline parallelism. Often combined with DeepSpeed as Megatron-DeepSpeed.
: See [[entities/megatron-lm]]

**Melanie Mitchell** _(entity: person)_
: AI researcher at Santa Fe Institute; author of influential analysis on whether LLMs develop genuine world models, introducing the Orrery Spectrum framework for evaluating AI understanding.
: See [[entities/melanie-mitchell]]

**Memex** _(concept)_
: Vannevar Bush's 1945 hypothetical device for storing and associatively linking personal knowledge — the conceptual ancestor of hypertext, the web, and modern personal knowledge management systems.
: See [[concepts/memex]]

**Memex** _(entity: concept)_
: Vannevar Bush's 1945 vision of a personal knowledge device with associative cross-referencing -- the conceptual ancestor of hypertext, wikis, and LLM-maintained knowledge bases.
: See [[entities/memex]]

**Memex and Tools for Thought** _(concept)_
: The lineage from Vannevar Bush's 1945 memex concept through Engelbart's mouse/hypertext, Nelson's hypertext/Xanadu, and Berners-Lee's Web to modern PKM tools — tracing 80 years of attempts to build systems that augment human knowledge management through associative linking.
: See [[concepts/memex-and-tools-for-thought]]

**MemGPT / Letta** _(entity: tool)_
: Open-source platform for stateful LLM agents with OS-inspired virtual context management; LLM self-manages memory hierarchy (core/recall/archival) through tool calls.
: See [[entities/memgpt-letta]]

**Memory Bandwidth Wall** _(concept)_
: The gap between processor speed and memory throughput is the dominant AI performance bottleneck; a 'memory-Parkinson' dynamic ensures models grow to consume all available HBM; progression from 2 TB/s (A100) to 8 TB/s (B200) to HBM4E (Rubin Ultra, 1024GB).
: See [[concepts/memory-bandwidth-wall]]

**Memory-Augmented Neural Networks** _(concept)_
: Neural architectures coupling a controller network with explicit external memory via differentiable read/write operations — from Neural Turing Machines (2014) and DNCs (2016) to modern retrieval-augmented transformers like RETRO, representing the evolution of how neural networks access stored knowledge.
: See [[concepts/memory-augmented-neural-networks]]

**Meta Llama** _(entity: tool)_
: Meta's open-weight LLM family — Llama 4 introduced MoE architecture with Scout (10M token context), Maverick (multimodal), and Behemoth (2T params, teacher model).
: See [[entities/meta-llama]]

**Meta-Prompting** _(concept)_
: The practice of using LLMs to generate, evaluate, and optimize prompts for LLMs — 'prompts that write other prompts' — with frameworks like DSPy (46%→64% accuracy) and TextGrad (Nature 2025) formalizing the approach.
: See [[concepts/meta-prompting]]

**METR** _(entity: org)_
: AI safety research organization that conducted the landmark RCT finding experienced open-source developers are 19% slower with AI tools — the most rigorous empirical challenge to AI productivity claims.
: See [[entities/metr]]

**micrograd** _(entity: tool)_
: Karpathy's educational autograd engine: ~100 lines of Python implementing backpropagation over a dynamically built DAG, with a ~50-line neural net library — the most accessible introduction to how deep learning actually works.
: See [[entities/micrograd]]

**Microsoft GraphRAG** _(entity: tool)_
: Open-source modular graph-based RAG system from Microsoft Research that builds knowledge graphs from text using LLM extraction, Leiden community detection, and hierarchical summarization.
: See [[entities/microsoft-graphrag]]

**Microsoft Phi Models** _(entity: paper)_
: Microsoft Research model family (phi-1 through phi-4) demonstrating that 'textbook quality' synthetic data enables small models (1.3B-14B) to rival or surpass models 10-25x larger.
: See [[entities/microsoft-phi]]

**Microsoft Research** _(entity: org)_
: Developed GraphRAG — a knowledge-graph-based approach to RAG that constructs community hierarchies for holistic query answering, now available as open-source on GitHub and integrated into Azure.
: See [[entities/microsoft-research]]

**minbpe** _(entity: tool)_
: Karpathy's minimal, clean reference implementation of BPE tokenization — the most widely-cited educational codebase for understanding LLM tokenization.
: See [[entities/minbpe]]

**MinHash LSH** _(entity: tool)_
: Probabilistic algorithm combining MinHash signatures with Locality-Sensitive Hashing to efficiently detect near-duplicate documents at trillion-token scale — the standard deduplication method for LLM training data.
: See [[entities/minhash-lsh]]

**Mixed-Precision Training** _(concept)_
: Using lower-precision formats (FP16, BFloat16) during training to reduce memory and increase throughput. BFloat16 is now industry standard — its 8 exponent bits match FP32's dynamic range, virtually eliminating the overflow issues that plague FP16.
: See [[concepts/mixed-precision-training]]

**Mixtral 8x7B** _(entity: tool)_
: Mistral AI's 2023 open-weight MoE model: 47B total parameters, 8 experts with 2 active per token (~12B FLOPs), outperforming Llama 2 70B while running at 12B-model speed.
: See [[entities/mixtral]]

**Mixture of Experts (MoE)** _(concept)_
: Sparse transformer architecture replacing dense FFN layers with multiple expert networks + learned router — scaling model capacity without proportional inference cost. By 2025, the default for all frontier LLMs.
: See [[concepts/mixture-of-experts]]

**MLX** _(entity: tool)_
: Apple's open-source ML framework for Apple Silicon — exploits unified memory for zero-copy inference; leads throughput on <14B models; supports on-device LoRA fine-tuning.
: See [[entities/mlx]]

**MMLU (Massive Multitask Language Understanding)** _(entity: dataset)_
: The most widely-cited LLM knowledge benchmark: 15,908 multiple-choice questions across 57 subjects from elementary math to professional law — now saturated above 90% for frontier models.
: See [[entities/mmlu]]

**Model Collapse** _(concept)_
: Degenerative feedback loop where models trained on synthetic data from models trained on synthetic data progressively lose capability — mitigated by human-data anchoring and lineage tracking.
: See [[concepts/model-collapse]]

**Model Context Protocol (MCP)** _(concept)_
: Open standard (JSON-RPC 2.0) for connecting AI models to external tools and data — the 'USB-C for AI'. Launched by Anthropic Nov 2024, adopted by OpenAI/Google 2025, donated to Linux Foundation Dec 2025. 97M monthly SDK downloads, 12K+ servers.
: See [[concepts/model-context-protocol]]

**Model Routing** _(concept)_
: Intelligent dispatching of LLM queries to appropriately-sized models based on complexity, achieving 40-85% cost reduction while maintaining 95%+ quality through predictive routing, cascading, or benchmark-trained classifiers.
: See [[concepts/model-routing]]

**Model-Based Filtering** _(concept)_
: Using trained classifiers (fastText, LLM-based scorers) to filter web data for LLM pretraining — the single most impactful curation technique, outperforming heuristics, perplexity filtering, and human judgment.
: See [[concepts/model-based-filtering]]

**Model-Based Reinforcement Learning** _(concept)_
: RL that learns an explicit environment model for planning through imagination — from Dyna (Sutton, 1990) through Ha & Schmidhuber's dream training to DreamerV3's 150+ task mastery — enabling 10-100x better sample efficiency than model-free approaches.
: See [[concepts/model-based-reinforcement-learning]]

**MongoDB** _(entity: tool)_
: A document database with vector search capabilities used as the storage and retrieval backend in the Decoding AI production RAG pipeline for second-brain AI assistants.
: See [[entities/mongodb]]

**Mozilla Readability (Readability.js)** _(entity: tool)_
: Mozilla's standalone JavaScript library for extracting article content from web pages via a 7-heuristic, 6-stage DOM scoring pipeline — powers Firefox Reader View and underpins Jina Reader API.
: See [[entities/mozilla-readability]]

**MT-Bench** _(entity: dataset)_
: Fixed 80-question multi-turn benchmark spanning 8 categories (writing, roleplay, extraction, reasoning, math, coding, knowledge, stem), created by LMSYS for evaluating LLM conversation quality.
: See [[entities/mt-bench]]

**MTEB (Massive Text Embedding Benchmark)** _(entity: dataset)_
: The standard benchmark for evaluating text embedding models: 8 task categories across 56+ English datasets (MMTEB: 131 tasks, 250+ languages), hosted on Hugging Face with a continuously updated leaderboard.
: See [[entities/mteb]]

**Multi-Agent Systems** _(concept)_
: Networks of specialized LLM agents collaborating through cooperation, competition, or coopetition — from KARMA's 9-agent KG pipeline to general-purpose orchestrator-worker architectures.
: See [[concepts/multi-agent-systems]]

**Multi-Head Attention** _(concept)_
: Running multiple parallel self-attention heads with independent Q/K/V projections, then concatenating results — enabling the model to capture diverse relationship types simultaneously.
: See [[concepts/multi-head-attention]]

**Multi-Stage Pretraining** _(concept)_
: The universal 2024 practice of training LLMs in sequential phases with different data mixes: broad web data first, then high-quality math/code, then context extension. Used by Llama 3.1, Apple AFM, Gemma 2, and Qwen 2.
: See [[concepts/multi-stage-pretraining]]

**Multilingual Tokenization** _(concept)_
: The structural barrier preventing equitable LLM performance across languages — tokenizers trained on English-heavy corpora create 2-15x token overhead for low-resource languages, wasting context, compute, and model capacity.
: See [[concepts/multilingual-tokenization]]

**Multilingual Training Data** _(concept)_
: The challenge of building LLM training datasets that serve non-English languages equitably — complicated by data scarcity, quality degradation in low-resource languages, and the English dominance of web data.
: See [[concepts/multilingual-training-data]]

**Multimodal AI** _(concept)_
: AI systems that process and reason across multiple data modalities (text, images, audio, video); by 2026 multimodal capability has become baseline rather than differentiator.
: See [[concepts/multimodal-ai]]

**Multimodal Embeddings** _(concept)_
: Embedding models that map images and text into a shared vector space via contrastive learning, enabling cross-modal similarity search — foundational for multimodal RAG and image retrieval.
: See [[concepts/multimodal-embeddings]]

**Multimodal RAG** _(concept)_
: Extending RAG to retrieve and reason over images alongside text; three architectures (unified embeddings, text grounding, separate stores with re-ranking) with tradeoffs between simplicity and fidelity.
: See [[concepts/multimodal-rag]]

**Multimodal Transformers** _(concept)_
: Transformer architectures processing multiple modalities (text, image, video, audio, actions) — evolving from encoder-bridge-decoder to native multimodal fusion, with MoE decoders dominating by 2025.
: See [[concepts/multimodal-transformers]]

## N

**Named Entity Recognition (NER) with LLMs** _(concept)_
: Identifying and classifying named entities (people, organizations, locations, etc.) in text — LLMs bridge the sequence-labeling-to-generation gap via task reformulation and self-verification.
: See [[concepts/named-entity-recognition]]

**nanoGPT** _(entity: tool)_
: Karpathy's simplest, fastest GPT training repository: reproduces GPT-2 (124M) on OpenWebText in ~4 days on 8xA100, serving as both educational reference and practical training tool.
: See [[entities/nanogpt]]

**Nathan Lambert** _(entity: person)_
: AI researcher and author of the RLHF Book — the most comprehensive public resource on reinforcement learning from human feedback, covering preference data collection, reward modeling, and alignment.
: See [[entities/nathan-lambert]]

**Natural Language Programming** _(concept)_
: The practice of specifying software behavior in natural language rather than formal programming languages -- from Karpathy's 'English is the hottest programming language' to production-grade spec-driven development with LLM agents.
: See [[concepts/natural-language-programming]]

**Needle in a Haystack (NIAH)** _(concept)_
: The standard evaluation for long-context LLMs: embed a specific fact (needle) at varying depths within a large context (haystack) and test if the model can retrieve it.
: See [[concepts/needle-in-a-haystack]]

**Nemotron-CC** _(entity: dataset)_
: NVIDIA's 6.3T-token dataset (4.4T real + 1.9T synthetic) using classifier ensembling and differentiated synthetic generation — 4x more unique tokens than DCLM while exceeding Llama 3.1 8B on MMLU.
: See [[entities/nemotron-cc]]

**Neo4j** _(entity: tool)_
: A native graph database used as the backend for Graphiti's temporal context graphs, providing mature graph query and visualization capabilities.
: See [[entities/neo4j]]

**Networked Thought** _(concept)_
: The paradigm of organizing knowledge as interconnected networks rather than hierarchical trees — from Bush's associative trails (1945) through Luhmann's Zettelkasten to modern bidirectional linking tools — based on the insight that meaning emerges from connections between ideas, not from their categorical placement.
: See [[concepts/networked-thought]]

**Neural Radiance Fields (NeRF)** _(concept)_
: Implicit neural scene representation mapping 3D coordinates to color and density via neural networks -- produces photorealistic 4K/8K reconstructions but requires hours of training and seconds per frame to render, being supplanted by Gaussian Splatting for real-time applications.
: See [[concepts/neural-radiance-fields]]

**Neural Turing Machine** _(entity: paper)_
: Alex Graves et al. (2014) architecture coupling a neural network controller with external memory via differentiable soft attention — the foundational work connecting attention mechanisms to external memory, enabling networks to learn algorithmic tasks like copy, sort, and associative recall.
: See [[entities/neural-turing-machine]]

**Neural-Symbolic Integration** _(concept)_
: The emerging paradigm combining symbolic reasoning (explainable, compositional, precise) with neural networks (learnable, perceptual, scalable) — six architectures catalogued, from language models with symbolic tokens to neural models calling symbolic engines.
: See [[concepts/neural-symbolic-integration]]

**Neuralink** _(entity: org)_
: Elon Musk's brain-computer interface company — 12 patients implanted by late 2025, planning high-volume automated production in 2026, straddling the line between medical device company and transhumanist venture.
: See [[entities/neuralink]]

**NeuroAI** _(concept)_
: The interdisciplinary field at the intersection of neuroscience and AI, arguing that understanding biological intelligence is key to building the next generation of artificial intelligence systems.
: See [[concepts/neuroai]]

**Neuromorphic Computing** _(concept)_
: Brain-inspired computing hardware using spiking neural networks and event-driven processing — Intel Loihi 3 and IBM NorthPole entering commercial production in 2026 with 1,000x GPU energy efficiency for sensory and robotics tasks.
: See [[concepts/neuromorphic-computing]]

**Neurotechnology** _(concept)_
: The broader field encompassing all technologies that interface with the nervous system — from brain-computer interfaces and neuromorphic chips to neural decoding, brain stimulation, and neurodiagnostics.
: See [[concepts/neurotechnology]]

**Next-Token Prediction** _(concept)_
: The self-supervised training objective for autoregressive LLMs: predict the next token given all preceding tokens, optimized via cross-entropy loss. Requires no labeled data — the next token in the sequence is the label.
: See [[concepts/next-token-prediction]]

**Niklas Luhmann** _(entity: person)_
: German sociologist (1927-1998) who developed the Zettelkasten method, producing 70 books and 400+ articles using a system of 90,000 interconnected index cards that he described as a 'communication partner.'
: See [[entities/niklas-luhmann]]

**NIST AI Risk Management Framework** _(entity: org)_
: Voluntary U.S. framework for AI risk management organized around four functions (Govern/Map/Measure/Manage); widely referenced as a global baseline by regulators and standards bodies.
: See [[entities/nist-ai-rmf]]

**Notion** _(entity: tool)_
: Flexible block-based workspace with 100M+ users, ranked #1 for knowledge bases on G2. Expanding from PKM into enterprise work OS with autonomous AI Agent, Enterprise Search, Calendar, Mail, and Sites. Base plan includes AI; $10/user/month. Competes with Confluence (structured wiki) and SharePoint (compliance-focused).
: See [[entities/notion]]

**Novartis** _(entity: org)_
: Pharmaceutical company using graph databases to link internal research data with external research abstracts, connecting genes, diseases, and compounds to accelerate drug discovery. One of the most notable enterprise knowledge graph deployments.
: See [[entities/novartis]]

**Nvidia** _(entity: org)_
: Dominant AI chip company (~80% market share); Blackwell architecture (B200: 1800 TFLOPS FP8, 192GB HBM3e, 208B transistors); acquired Groq for $20B; Vera Rubin (3.6 EFLOPS, late 2026); CUDA ecosystem is the primary moat; geopolitically central to US-China AI race.
: See [[entities/nvidia]]

**NVIDIA Cosmos** _(entity: framework)_
: NVIDIA's world foundation model platform: wavelet-based tokenizer (12x faster), 7B-14B diffusion and 4B-13B autoregressive models trained on 20M hours of video, targeting autonomous driving and robotics; open model license, 2M+ downloads.
: See [[entities/nvidia-cosmos]]

**NVIDIA Isaac GR00T** _(entity: framework)_
: NVIDIA's open humanoid robot foundation model with dual System 1 (reflexive) / System 2 (deliberative) architecture; generated 780K synthetic trajectories in 11h; adopted by Boston Dynamics, 1X, Agility; N1.6 integrates Cosmos Reason VLM for step-by-step planning.
: See [[entities/nvidia-groot]]

## O

**Obsidian** _(entity: tool)_
: A local-first, markdown-based knowledge management platform with 1.5M users, 2,700+ plugins, and a 'file over app' philosophy — serves as the frontend IDE for LLM-maintained wikis.
: See [[entities/obsidian]]

**Obsidian AI Integration** _(concept)_
: Two paradigms for AI in Obsidian: plugin-based (Copilot, Smart Connections inside the app) and external-agent (Claude Code + MCP operating over the file system) — converging toward governed autonomous vault operations.
: See [[concepts/obsidian-ai-integration]]

**Obsidian as IDE** _(concept)_
: Using Obsidian as a read-only frontend IDE to view LLM-maintained wikis, raw sources, and generated visualizations — with the LLM as the actual author and 2,700+ plugins extending the viewer.
: See [[concepts/obsidian-as-ide]]

**Obsidian Canvas** _(concept)_
: Obsidian Canvas provides infinite spatial boards for mapping notes, media, and ideas — enhanced by the Advanced Canvas plugin for flowcharts, presentations, and graph integration.
: See [[concepts/obsidian-canvas]]

**Obsidian Copilot** _(entity: tool)_
: The #1 downloaded AI plugin for Obsidian (100K+ users): model-agnostic chat assistant with vault RAG, project workspaces, diff-preview composer, and all data stored as plain markdown.
: See [[entities/obsidian-copilot]]

**Obsidian Frontmatter and Properties** _(concept)_
: YAML frontmatter properties in Obsidian provide structured metadata for notes — enabling Dataview queries, AI retrieval, search filtering, and database-like views via the Bases feature.
: See [[concepts/obsidian-frontmatter-properties]]

**Obsidian Graph View** _(concept)_
: Obsidian's graph view visualizes notes as nodes and links as edges — useful for seeing clusters, orphans, and connection patterns, but limited in analytical depth without plugins like InfraNodus.
: See [[concepts/obsidian-graph-view]]

**Obsidian Plugin Ecosystem** _(concept)_
: Obsidian's 2,700+ community plugin ecosystem transforms a markdown editor into a programmable knowledge platform — organized into querying, templating, AI, visualization, and automation categories.
: See [[concepts/obsidian-plugin-ecosystem]]

**Obsidian Web Clipper** _(entity: tool)_
: A browser extension for converting web articles into markdown files for ingestion into the raw/ directory of an LLM knowledge base.
: See [[entities/obsidian-web-clipper]]

**OCR and Document Extraction** _(concept)_
: Modern OCR has evolved from character recognition to document understanding: traditional engines (Tesseract, PaddleOCR) deliver 99%+ on printed text, while LLM-powered models (RolmOCR, Qwen2.5-VL) handle complex layouts, tables, and handwriting.
: See [[concepts/ocr-document-extraction]]

**Odds Ratio Preference Optimization (ORPO)** _(concept)_
: A single-step alignment method that combines instruction tuning and preference optimization in one process -- reference-model-free, computationally cheap, and effective with as few as 7K examples.
: See [[concepts/orpo]]

**Ollama** _(entity: tool)_
: Most popular local LLM tool (150K+ GitHub stars) — abstracts llama.cpp into Docker-like experience with Modelfiles, OpenAI-compatible API, and cross-platform GPU support.
: See [[entities/ollama]]

**OntoGPT** _(entity: tool)_
: Python package for ontology-grounded information extraction using LLMs and the SPIRES zero-shot method — extracts structured data aligned to established biomedical ontologies.
: See [[entities/ontogpt]]

**Ontology (Knowledge Engineering)** _(concept)_
: Formal specification of concepts, relationships, and rules within a knowledge domain — from WordNet and Cyc through OWL/RDF to modern knowledge graphs, with LLM-era 'cheap ontology' as the latest evolution.
: See [[concepts/ontology]]

**Ontology and Taxonomy** _(concept)_
: Formal knowledge organization systems for enterprise AI. Taxonomy = hierarchical parent-child relationships (single-parent trees). Ontology = relationships across multiple taxonomies (multi-parent inheritance). Together they form the structural scaffolding of semantic layers. Ontology functions as 'master data management for AI' -- changes propagate automatically through associative relationships.
: See [[concepts/ontology-and-taxonomy]]

**Ontology Engineering** _(concept)_
: The design of formal schemas (ontologies) that define entity types, relation types, and constraints for knowledge graphs — now increasingly automated by LLMs that achieve near-junior-expert quality.
: See [[concepts/ontology-engineering]]

**Open Source vs Closed Source AI** _(concept)_
: The geopolitically charged debate between open-weight AI models (DeepSeek R1, Llama, Mistral) and proprietary systems (GPT, Claude); Chinese open-source usage surged from 1.2% to 30% of global usage in 2025; safety vs. innovation tensions define the regulatory frontier.
: See [[concepts/open-source-vs-closed-ai]]

**Open-Source Coding Models** _(concept)_
: Specialized code LLMs — Qwen 2.5 Coder (88.4% HumanEval, Apache 2.0), Codestral (95.3% FIM), DeepSeek Coder (338 languages, 10GB VRAM) — now match or exceed GPT-4 on coding tasks.
: See [[concepts/open-source-coding-models]]

**Open-Source LLMs** _(concept)_
: Open-weight LLMs from DeepSeek, Qwen, Meta, Mistral, and others have closed the gap with proprietary models to ~3 months, using MoE architectures and MIT/Apache licensing.
: See [[concepts/open-source-llms]]

**OpenAI** _(entity: org)_
: AI research company behind GPT-4, o1, and o3 reasoning models -- pioneers of process reward models (PRM800K), scaled reinforcement learning for reasoning, and test-time search with deliberative alignment.
: See [[entities/openai]]

**OpenAI Codex** _(entity: tool)_
: OpenAI's agentic coding tool -- cloud sandbox-based, zero-dependency Rust CLI, 1,000+ tok/s on Cerebras hardware -- excelling at rapid prototyping and terminal-heavy workflows with 56.8% SWE-bench Pro and 77.3% Terminal-Bench.
: See [[entities/openai-codex]]

**OpenAI Embeddings** _(entity: tool)_
: OpenAI's embedding API models: text-embedding-ada-002 (1536 dims, legacy), text-embedding-3-small/large (native Matryoshka, up to 3072 dims) — widely used but increasingly matched by open-source alternatives.
: See [[entities/openai-embeddings]]

**OpenFactCheck** _(entity: tool)_
: Open-source unified framework for LLM factuality evaluation with three modules: ResponseEvaluator (claim-level fact-checking), LLMEvaluator (FactQA, 6,480 examples), and FactCheckerEvaluator (FactBench, 4,507 annotated examples).
: See [[entities/openfactcheck]]

**OWASP** _(entity: org)_
: Open Worldwide Application Security Project — ranked prompt injection as the #1 AI security risk in its 2025 Top 10 for LLMs.
: See [[entities/owasp]]

## P

**PagedAttention** _(concept)_
: Virtual-memory-inspired KV cache management (vLLM) that allocates non-contiguous memory blocks with mapping tables — reducing waste from 60-80% to 4% and enabling prompt sharing.
: See [[concepts/paged-attention]]

**Pandoc** _(entity: tool)_
: Universal document converter (Haskell, GPL) that converts between 40+ formats via a markdown-centric AST — maintained since 2006 by John MacFarlane.
: See [[entities/pandoc]]

**PARA Method** _(concept)_
: Tiago Forte's organizational framework: Projects (short-term, specific goals), Areas (ongoing responsibilities), Resources (future interest), Archive (inactive) — organizing information by actionability rather than topic, designed to mirror how work actually flows.
: See [[concepts/para-method]]

**Parameter-Efficient Fine-Tuning (PEFT)** _(concept)_
: LoRA and QLoRA enable fine-tuning LLMs by updating only 0.5-5% of parameters via low-rank adapter matrices, reducing VRAM from 60GB to 6GB for a 7B model while retaining 80-95% quality.
: See [[concepts/parameter-efficient-fine-tuning]]

**Path to AGI** _(concept)_
: The convergence of scaling, algorithmic efficiency, and unhobbling gains suggests AGI between 2027-2033, with AI leaders predicting the earlier end and researchers the later — but definitions remain deeply contested.
: See [[concepts/path-to-agi]]

**PDF Parsing Tools** _(concept)_
: PDF parsing tool landscape: PyMuPDF4LLM (fastest, 0.12s), Docling (best enterprise, 9/10), Nougat (best scientific), LlamaParse (best tables), Unstructured (best multi-format) — with two paradigms: pipeline vs. end-to-end.
: See [[concepts/pdf-parsing-tools]]

**Perplexity AI** _(entity: tool)_
: AI-powered research tool providing citation-backed answers with real-time web search; gold standard for fast, multi-source discovery; Deep Research mode autonomously synthesizes dozens of sources.
: See [[entities/perplexity-ai]]

**Personal Knowledge Management (PKM)** _(concept)_
: The practice of capturing, organizing, and retrieving personal knowledge — transformed by LLMs from manual note-taking (Notion/Obsidian) to AI-compiled, queryable wikis with automatic synthesis and gap-filling.
: See [[concepts/personal-knowledge-management]]

**Personalization in AI** _(concept)_
: The billion-dollar AI product opportunity: adapting not just what content AI presents but how it presents it — visual learners get diagrams, metaphor-lovers get analogies — requiring consent-based behavioral learning and concierge-style delivery.
: See [[concepts/personalization-in-ai]]

**pgvector** _(entity: tool)_
: A PostgreSQL extension for vector similarity search, widely regarded as sufficient for most team-scale retrieval use cases without requiring dedicated vector database infrastructure.
: See [[entities/pgvector]]

**Phi (Microsoft)** _(entity: tool)_
: Microsoft's SLM family — Phi-4 (14B) beats GPT-4o on MATH/GPQA with 84.8% MMLU; Phi-4-mini (3.8B) runs on 3GB VRAM with 128K context.
: See [[entities/phi]]

**Philip Gage** _(entity: person)_
: Inventor of the Byte Pair Encoding algorithm (1994), originally designed for text compression and later adapted for LLM tokenization.
: See [[entities/philip-gage]]

**Photonic Computing** _(concept)_
: Computing with photons instead of electrons: 100x speed/energy efficiency demonstrated in labs (MIT, LightGen); three manufacturing platforms (InP, SiN, SiPh); commercial revolution unrealistic before 2030; near-term value in optical interconnects and co-packaged optics.
: See [[concepts/photonic-computing]]

**Physical AI** _(concept)_
: AI systems that perceive, understand, and act in the physical world — autonomous vehicles, robots, and smart spaces — requiring world models that capture physics, object permanence, and spatial reasoning; driven by NVIDIA Cosmos, Physical Intelligence, and the embodied AI ecosystem.
: See [[concepts/physical-ai]]

**Physical Intelligence** _(entity: org)_
: San Francisco AI robotics startup; raised $400M+; developed π0, the first robot foundation model to achieve complex dexterous tasks; open-sourced via Hugging Face; aims to provide a foundation model for physical intelligence analogous to LLMs for language.
: See [[entities/physical-intelligence]]

**Pinecone** _(entity: tool)_
: Fully managed vector database service: proprietary indexing, sub-10ms latency at tens of billions of vectors, SOC 2 + HIPAA + ISO 27001, with Pinecone Assistant for integrated RAG (GA January 2025).
: See [[entities/pinecone]]

**Pipeline Orchestration** _(concept)_
: Scheduling, monitoring, and managing multi-stage data/ML pipelines: Apache Airflow dominates (35% of enterprises), with Airflow 3.0 adding event-driven scheduling, dynamic task mapping, and real-time reactive orchestration.
: See [[concepts/pipeline-orchestration]]

**Pipeline Parallelism** _(concept)_
: Inter-layer parallelism that distributes model layers sequentially across GPUs. Lower communication than tensor parallelism but suffers from pipeline bubbles — mitigated by micro-batching and interleaved scheduling.
: See [[concepts/pipeline-parallelism]]

**Plain Text Longevity** _(concept)_
: Plain text is the only digital format guaranteed to be readable decades or centuries from now — validated by individual practitioners, Obsidian's CEO, and institutional archivists.
: See [[concepts/plain-text-longevity]]

**Playwright** _(entity: tool)_
: Microsoft's cross-browser automation framework — the modern headless browser of choice for web scraping, supporting Chromium/Firefox/WebKit, with auto-waiting, parallel execution, and stealth capabilities.
: See [[entities/playwright]]

**Positional Encoding** _(concept)_
: Methods for injecting sequence order information into transformers, which are inherently position-agnostic — evolved from sinusoidal (2017) to learned absolute to relative (T5) to rotary (RoPE, now standard).
: See [[concepts/positional-encoding]]

**Post-Code AI Workflow** _(concept)_
: Karpathy's framing of a shift in AI-augmented developer work: from code generation as the primary token use, to knowledge compilation and orchestration — 'manipulating knowledge, not code.'
: See [[concepts/post-code-ai-workflow]]

**Predictive Coding** _(concept)_
: A theory of brain function where the cortex continuously generates top-down predictions and only processes bottom-up prediction errors — the brain as a hierarchical prediction machine that minimizes surprise.
: See [[concepts/predictive-coding]]

**Preference Data** _(concept)_
: Human (or AI) judgments ranking model outputs used to train reward models for RLHF alignment — collected via pairwise comparison, expensive to produce, and critically dependent on on-policy generation and bias mitigation.
: See [[concepts/preference-data]]

**Pretraining Data Pipeline** _(concept)_
: The multi-stage pipeline for preparing LLM training data: web crawling, URL filtering, text extraction, language filtering, quality filtering, deduplication (MinHash), PII removal, and domain balancing. FineWeb exemplifies this with 15T tokens from 36T after filtering.
: See [[concepts/pretraining-data-pipeline]]

**Process Reward Model (PRM)** _(concept)_
: A reward model variant that scores each reasoning step individually rather than only the final output -- providing finer-grained feedback that is harder to hack but requires expensive step-level supervision data.
: See [[concepts/process-reward-model]]

**Process Reward Models** _(concept)_
: Trained verifier models that evaluate each step in a reasoning chain (not just the final answer), enabling selection of the best reasoning path -- a key building block of test-time compute scaling and reasoning models.
: See [[concepts/process-reward-models]]

**Progressive Disclosure in AI** _(concept)_
: The foundational AI design pattern that reveals complexity gradually in 2-3 layers max — solving the engagement-overload paradox where more explanation can backfire; RAG itself is progressive disclosure at the data layer.
: See [[concepts/progressive-disclosure-ai]]

**Progressive Summarization** _(concept)_
: Tiago Forte's layered distillation technique: bold key passages (Layer 2), highlight the best-of-best (Layer 3), write an executive summary in your own words (Layer 4) — designing notes for your Future Self to scan at any depth.
: See [[concepts/progressive-summarization]]

**Prometheus** _(entity: tool)_
: Open-source LLM evaluator fine-tuned on 100K GPT-4 feedback samples (based on Llama-2-Chat); achieves 0.897 Pearson correlation with human judgments using explicit rubrics and reference answers.
: See [[entities/prometheus]]

**Prompt Caching** _(concept)_
: Provider-level optimization caching computed state of static prompt prefixes: Anthropic (90% savings), OpenAI (50%), Google (75%) — making large contexts economically viable.
: See [[concepts/prompt-caching]]

**Prompt Chaining** _(concept)_
: Decomposing complex tasks into sequential LLM calls where each output feeds the next — the foundational pattern for production LLM workflows, enabling transparency, controllability, and debugging.
: See [[concepts/prompt-chaining]]

**Prompt Engineering** _(concept)_
: The discipline of designing inputs to LLMs that reliably produce high-quality, accurate, and well-structured outputs — encompassing techniques from simple clarity principles to advanced reasoning scaffolds.
: See [[concepts/prompt-engineering]]

**Prompt Engineering Guide (DAIR.AI)** _(entity: tool)_
: Comprehensive open-source resource at promptingguide.ai maintained by DAIR.AI, covering all major prompting techniques with research citations and examples — the de facto reference for the field.
: See [[entities/prompt-engineering-guide]]

**Prompt Injection** _(concept)_
: Manipulation technique exploiting the fundamental inability to separate LLM instructions from user input — ranked #1 AI security risk by OWASP in 2025, with no foolproof defense due to the probabilistic nature of LLMs.
: See [[concepts/prompt-injection]]

**Property Graphs** _(concept)_
: Node-centric graph data model where nodes and edges carry rich attribute data, optimized for traversal performance and developer experience — the dominant model for production knowledge graph applications.
: See [[concepts/property-graphs]]

**Proximal Policy Optimization (PPO) for LLMs** _(concept)_
: The dominant RL algorithm for RLHF: a policy-gradient method using trust-region optimization to fine-tune LLMs against reward models while maintaining training stability via clipped objectives and KL penalties.
: See [[concepts/ppo-for-llms]]

**Pydantic** _(entity: tool)_
: Python data validation library using type hints — the de facto standard for defining LLM extraction schemas, powering Instructor, Pydantic AI, LangChain structured output, and Simon Willison's LLM.
: See [[entities/pydantic]]

**PyMuPDF** _(entity: tool)_
: Fastest Python PDF parser (0.12s markdown output): PyMuPDF4LLM variant optimized for LLM ingestion with layout analysis and semantic understanding; most consistent recall among rule-based tools; AGPL/commercial license.
: See [[entities/pymupdf]]

## Q

**Qdrant** _(entity: tool)_
: Open-source vector database written in Rust: HNSW indexing, richest feature set (hybrid search, geo-spatial, multi-vector, sparse vectors), 326 QPS, available as self-hosted, managed cloud, or hybrid deployment.
: See [[entities/qdrant]]

**Quantization** _(concept)_
: Reducing model weight precision (FP16 → 4-bit) to shrink memory footprint 4x and enable local inference on consumer hardware, with minimal quality loss.
: See [[concepts/quantization]]

**Quantum Machine Learning** _(concept)_
: Using quantum phenomena (superposition, entanglement) to enhance ML: key algorithms (PQCs, QAOA, quantum kernels); hybrid quantum-classical is the 2026 paradigm; NISQ hardware improving but enterprise-scale needs thousands of logical qubits; market at 36.4% CAGR toward $162.6M by 2030.
: See [[concepts/quantum-machine-learning]]

**Qwen** _(entity: tool)_
: Alibaba's open-source LLM family — Qwen 3.5 (397B MoE) leads reasoning benchmarks; Qwen 2.5 Coder (88.4% HumanEval) beats GPT-4; small variants (4B) rival 72B models.
: See [[entities/qwen]]

**Qwen3-VL** _(entity: tool)_
: Alibaba's flagship open-source VLM (235B params, 22B active MoE): rivals GPT-5 and Gemini-2.5-Pro with 256K-1M context, multilingual OCR (32 languages), and visual agent capabilities.
: See [[entities/qwen3-vl]]

## R

**RAFT (Retrieval Augmented Fine-Tuning)** _(concept)_
: Hybrid approach training models on questions with oracle + distractor documents, teaching them to leverage retrieval while ignoring noise — up to 76% improvement over baselines.
: See [[concepts/raft]]

**RAG Evaluation** _(concept)_
: The discipline of measuring RAG system quality across three tiers — retrieval metrics (Precision@k, MRR, nDCG), generation metrics (faithfulness, hallucination rate), and operational metrics (latency, safety) — using frameworks like RAGAS and benchmarks like RAGBench.
: See [[concepts/rag-evaluation]]

**RAG Hallucinations** _(concept)_
: Fabricated or incorrect outputs from RAG systems despite access to grounding sources — caused by retrieval failures, cross-document fusion errors, and confidence misalignment. Stanford found 17-33% hallucination in legal RAG tools.
: See [[concepts/rag-hallucinations]]

**RAG Prompting** _(concept)_
: Prompt engineering techniques specific to RAG pipelines — query rewriting (HyDE, Query2Doc), context integration, and generation prompts — where 'weak retrieval makes things messy, but weak prompts make things unusable.'
: See [[concepts/rag-prompting]]

**RAG vs. Index-Based Retrieval** _(concept)_
: At small-to-medium scale (~100 articles, ~400K words), LLM-maintained index files and one-line summaries can replace vector database RAG for document Q&A.
: See [[concepts/rag-vs-index-based-retrieval]]

**RAGAS (Retrieval Augmented Generation Assessment)** _(entity: tool)_
: The leading open-source framework for reference-free evaluation of RAG pipelines, providing metrics for faithfulness, context precision/recall, answer relevancy, and synthetic test data generation.
: See [[entities/ragas]]

**RAPTOR (Recursive Abstractive Processing for Tree-Organized Retrieval)** _(concept)_
: ICLR 2024 technique that recursively clusters and summarizes text chunks into a tree structure, enabling retrieval at multiple abstraction levels — achieving 20% absolute improvement on QuALITY benchmark.
: See [[concepts/raptor]]

**RAPTOR Paper (ICLR 2024)** _(entity: paper)_
: ICLR 2024 paper by Sarthi, Abdullah et al. introducing RAPTOR — recursive tree construction via GMM clustering and abstractive summarization for multi-level retrieval, achieving 20% improvement on QuALITY.
: See [[entities/raptor-paper]]

**RDF Knowledge Representation** _(concept)_
: The W3C-standardized Resource Description Framework for representing knowledge as subject-predicate-object triples with URIs, SPARQL queries, and OWL reasoning — the semantic web foundation for formal knowledge graphs.
: See [[concepts/rdf-knowledge-representation]]

**ReAct Pattern** _(concept)_
: The Thought-Action-Observation loop that enables LLM agents to interleave reasoning with real-world actions, outperforming both pure reasoning (CoT) and action-only approaches.
: See [[concepts/react-pattern]]

**Reader-LM (Jina)** _(entity: tool)_
: Jina's 1.5B-parameter specialized language model for HTML-to-markdown conversion — outperforms GPT-4o (ROUGE-L 0.86 vs 0.43) by treating the task as selective-copy, with 512K token context and 29-language support.
: See [[entities/reader-lm]]

**Reasoning Models** _(concept)_
: LLMs specifically trained (via RL) to perform extended deliberation before answering -- including OpenAI o1/o3, DeepSeek R1, and Claude 3.7 with extended thinking -- representing the internalization of chain-of-thought reasoning through reinforcement learning.
: See [[concepts/reasoning-models]]

**Reasoning Tokens** _(concept)_
: The internal tokens generated by reasoning models during deliberation (thinking tokens, hidden CoT) -- their quantity is a poor proxy for reasoning quality; 'deep-thinking tokens' (significant layer-by-layer revision) correlate better with accuracy.
: See [[concepts/reasoning-tokens]]

**Rectified Flow** _(concept)_
: Optimization of flow matching that straightens transport trajectories from noise to data, enabling large integration steps and few-step generation -- the 'reflow' procedure uses teacher-student distillation to further reduce curvature, underpinning FLUX and SD3 training.
: See [[concepts/rectified-flow]]

**Recursion Pharmaceuticals** _(entity: org)_
: AI drug discovery company using phenomics (2.2M experiments/week). Merged with Exscientia (July 2025) to create the largest AI drug discovery entity by pipeline breadth. 10+ clinical programs; notable setback with REC-994 discontinuation.
: See [[entities/recursion-pharmaceuticals]]

**Red Teaming** _(concept)_
: Deliberate adversarial testing of LLM systems to uncover safety vulnerabilities — covering prompt injection, jailbreaking, multi-turn attacks, and automated red teaming frameworks.
: See [[concepts/red-teaming]]

**Redis** _(entity: tool)_
: In-memory data platform used for LLM semantic caching: Redis LangCache stores query embeddings alongside responses, achieving 73% cost reduction with sub-millisecond vector search across millions of entries.
: See [[entities/redis]]

**Reflection Pattern** _(concept)_
: Automated self-critique pattern where LLMs evaluate and iteratively improve their own outputs, delivering surprising performance gains with relatively simple implementation.
: See [[concepts/reflection-pattern]]

**Reinforcement Learning for Reasoning** _(concept)_
: Using RL (GRPO, PPO, scaled RL with verifiers) to train LLMs to develop reasoning capabilities -- the core training methodology behind o1, o3, and R1, enabling emergent self-verification and reasoning without supervised fine-tuning.
: See [[concepts/reinforcement-learning-for-reasoning]]

**Reinforcement Learning from AI Feedback (RLAIF)** _(concept)_
: An alignment technique that replaces human preference annotators with LLM-generated labels, achieving statistical parity with RLHF at dramatically lower cost and enabling fully automated preference data pipelines.
: See [[concepts/rlaif]]

**Reinforcement Learning from Human Feedback (RLHF)** _(concept)_
: The dominant technique for aligning LLMs with human preferences: train a reward model on human preference data, then fine-tune the LLM using PPO to maximize that reward while staying close to the reference policy.
: See [[concepts/rlhf]]

**Relation Extraction with LLMs** _(concept)_
: Extracting subject-predicate-object relationships between entities from text — LLMs enable zero-shot relation extraction that matches supervised models, feeding knowledge graph construction.
: See [[concepts/relation-extraction]]

**Reranking** _(concept)_
: Using cross-encoder models to re-score and reorder retrieval candidates, improving RAG precision by 30-50% by applying query-specific analysis to the top-k results from fast initial retrieval.
: See [[concepts/reranking]]

**Responsible Scaling Policy (RSP)** _(concept)_
: Anthropic's risk governance framework using AI Safety Levels (ASL-1 through ASL-5) modeled after biosafety levels, requiring escalating safeguards proportional to model capabilities -- evolved through 6 versions from September 2023 to April 2026.
: See [[concepts/responsible-scaling-policy]]

**Retrieval-Augmented Generation (RAG)** _(concept)_
: The dominant paradigm for grounding LLM outputs in external knowledge: retrieve relevant documents at query time, inject them as context, and generate answers — now evolving into modular, agentic context engines.
: See [[concepts/retrieval-augmented-generation]]

**RETRO (Retrieval-Enhanced Transformer)** _(entity: paper)_
: DeepMind's 7.5B parameter model matching GPT-3 (185B) by augmenting a transformer with a 2-trillion-token retrieval database accessed via chunked cross-attention — decoupling factual memorization from language reasoning.
: See [[entities/retro]]

**Reward Hacking and Overoptimization** _(concept)_
: The phenomenon where RL agents exploit flaws in proxy reward functions to achieve high scores without genuine improvement -- Goodhart's Law applied to LLM alignment, manifesting as sycophancy, verbosity gaming, and fabricated evidence.
: See [[concepts/reward-hacking]]

**Reward Model** _(concept)_
: A learned preference function -- typically an LLM with a linear head producing scalar scores -- trained on human preference data to serve as the optimization target in RLHF, bridging human judgments and RL training signals.
: See [[concepts/reward-model]]

**RFdiffusion** _(entity: tool)_
: David Baker's diffusion-based protein design tool from the Institute for Protein Design (UW). RFdiffusion3 (Dec 2025) designs proteins binding any intracellular molecule; 10x faster than v2. Atomically accurate antibody design published in Nature.
: See [[entities/rfdiffusion]]

**Roam Research** _(entity: tool)_
: The note-taking tool that popularized bidirectional linking in 2020, treating every block as a referenceable node in a personal knowledge graph — positioned as 'a note-taking tool for networked thought.'
: See [[entities/roam-research]]

**Robot Learning from Demonstration** _(concept)_
: Teaching robots through expert demonstrations — via teleoperation, motion capture, or human video; π0 needs 1-20 hours per task; NVIDIA generates 780K synthetic demos in 11h; growing gig economy of remote teleoperators training humanoids from home.
: See [[concepts/robot-learning-from-demonstration]]

**Role Prompting** _(concept)_
: Assigning a persona or expert identity to an LLM — effective for tone/style control and creative tasks, but unreliable for factual accuracy where 'none of the strategies outperformed random selection.'
: See [[concepts/role-prompting]]

**ROME and MEMIT** _(entity: paper)_
: Pioneering knowledge editing methods: ROME makes rank-one MLP modifications for single fact edits; MEMIT scales to thousands of simultaneous edits across transformer layers.
: See [[entities/rome-memit]]

**Rotary Position Embeddings (RoPE)** _(concept)_
: Position encoding via complex-number rotation of embedding pairs — parameter-free, inherently relative, compatible with efficient attention, and the standard for all modern LLMs (Llama, Mistral, Qwen, etc.).
: See [[concepts/rotary-position-embeddings]]

**RT-2 (Robotic Transformer 2)** _(entity: paper)_
: Google DeepMind's pioneering Vision-Language-Action model (July 2023) that showed VLMs can directly control robots; built on PaLM-E/PaLI-X; encodes actions as text tokens; improved generalization from 32% to 62% vs RT-1; demonstrated emergent reasoning from web pre-training.
: See [[entities/rt-2]]

**Runway** _(entity: tool)_
: AI video generation platform targeting professional production -- Gen-4 offers character persistence, motion capture (Act-Two), and in-video editing (Aleph), the only major tool designed for post-production workflow integration at ~$0.12/second.
: See [[entities/runway]]

## S

**Safe Superintelligence Inc. (SSI)** _(entity: org)_
: Ilya Sutskever's AI lab: $30B valuation, ~50 employees, zero revenue, zero products — focused exclusively on building safe superintelligence with no commercial distractions.
: See [[entities/safe-superintelligence-inc]]

**Sam Gallagher** _(entity: person)_
: Developer who built the Knowledge Graph Kit, an open-source MCP server using SQLite and ChromaDB, as a structure-first alternative to markdown-based personal knowledge management.
: See [[entities/sam-gallagher]]

**SambaNova Systems** _(entity: org)_
: Reconfigurable DataFlow Unit (RDU) with up to 3TB memory per socket; SambaFlow compiler; deployed at Los Alamos and LLNL; Samba-1 (1T parameter) model; $676M Series D at ~$5B valuation.
: See [[entities/sambanova]]

**Sapphire Ventures** _(entity: org)_
: Enterprise VC firm that developed the 5-D framework (Design, Data, Domain Expertise, Dynamism, Distribution) for evaluating AI-native applications, tracking $8.5B invested in GenAI-native apps.
: See [[entities/sapphire-ventures]]

**SayCan** _(entity: paper)_
: Google's foundational system for grounding language in robotic affordances — combines LLM semantic scores with physical feasibility functions; 84% plan success, 74% execution on 101 kitchen tasks with 8-16 steps; precursor to RT-2 and the broader VLA paradigm.
: See [[entities/saycan]]

**Scalable Oversight** _(concept)_
: The challenge of maintaining meaningful human oversight over AI systems that are more capable than their overseers — addressed through recursive oversight, debate, weak-to-strong generalization, and AI-governing-AI architectures.
: See [[concepts/scalable-oversight]]

**Scaling Laws** _(concept)_
: Mathematical relationships between model size, dataset size, compute budget, and (recently) data quality that predict LLM performance — from the original Kaplan/Chinchilla laws to quality-aware extensions.
: See [[concepts/scaling-laws]]

**Schema-Guided and Ontology-Driven Extraction** _(concept)_
: Constraining LLM extraction with predefined schemas or ontologies — from static templates to dynamic, co-evolving schemas — trading flexibility for precision and consistency.
: See [[concepts/schema-guided-extraction]]

**Scite** _(entity: tool)_
: Citation analysis tool with 1.2 billion citation statements from 187M+ articles — shows whether papers are cited supportively, contrastingly, or merely mentioned, enabling research claim verification.
: See [[entities/scite]]

**Scrapy** _(entity: framework)_
: Python's premier web crawling framework — 2,500 pages/min throughput, 1,000 concurrent requests via Twisted async, with built-in pipelines, retry logic, and rate limiting for large-scale scraping.
: See [[entities/scrapy]]

**Sebastian Raschka** _(entity: person)_
: ML researcher and educator; author of 'Build a Large Language Model From Scratch' and popular BPE implementation tutorials.
: See [[entities/sebastian-raschka]]

**Second Brain** _(concept)_
: A personal AI system that stores, organizes, and retrieves the user's own knowledge — implemented either as a markdown wiki (Karpathy), a graph database (Gallagher), or a RAG pipeline (Decoding AI), all using LLMs as the intelligence layer.
: See [[concepts/second-brain]]

**Selective State Space (S6)** _(concept)_
: Mamba's core innovation: making SSM state transition matrices B, C and step size delta input-dependent, enabling content-aware selective information compression into the hidden state.
: See [[concepts/selective-state-space]]

**Self-Attention** _(concept)_
: The mechanism allowing each position in a sequence to attend to all others by computing scaled dot products between learned Query, Key, and Value projections — the core innovation of the Transformer.
: See [[concepts/self-attention]]

**Self-Consistency** _(concept)_
: A reasoning enhancement technique that samples multiple chain-of-thought solutions to the same problem and selects the most frequent answer via majority voting, improving accuracy on arithmetic and commonsense reasoning benchmarks.
: See [[concepts/self-consistency]]

**Self-Consistency Prompting** _(concept)_
: Wang et al. (2022) technique that improves CoT by sampling multiple diverse reasoning paths and selecting the most frequent answer via majority voting — more reliable than single-path CoT.
: See [[concepts/self-consistency-prompting]]

**Self-Driving Laboratories** _(concept)_
: Self-driving labs combine AI + robotics to automate the entire scientific method: from hypothesis generation to experiment execution to conclusion. A-Lab (Berkeley) synthesizes AI-predicted materials; Periodic Labs (2025) co-founded by ChatGPT creator. Cloud labs start at $50K/month.
: See [[concepts/self-driving-labs]]

**Self-RAG (Self-Reflective Retrieval-Augmented Generation)** _(concept)_
: An advanced RAG framework that trains four reflection tokens into the model — Retrieve, ISREL, ISSUP, ISUSE — enabling self-assessment of when to retrieve, what's relevant, and whether outputs are evidence-supported.
: See [[concepts/self-rag]]

**Self-Supervised Learning** _(concept)_
: Learning representations from unlabeled data via pretext tasks — from contrastive learning (SimCLR, CLIP) to joint embedding prediction (JEPA) — the foundational training paradigm for world models that learn from millions of hours of internet video.
: See [[concepts/self-supervised-learning]]

**Semantic Caching** _(concept)_
: Caching LLM responses keyed by semantic similarity rather than exact string match, using vector embeddings to identify similar queries and return pre-computed answers in milliseconds — achieving 61-73% cost reduction.
: See [[concepts/semantic-caching]]

**Semantic Layer** _(concept)_
: A standardized framework that organizes and abstracts organizational data (structured, unstructured, semi-structured) to serve as a connector between data repositories and front-end applications. Comprises business glossaries, controlled metadata, data catalogs, taxonomies, and ontologies/knowledge graphs. Identified as the key enabling technology for enterprise AI in 2026.
: See [[concepts/semantic-layer]]

**Semantic Search** _(concept)_
: Search based on meaning rather than exact terms: transformer models encode text into dense vectors, enabling retrieval of conceptually related content even when queries and documents share no common words.
: See [[concepts/semantic-search]]

**Semantic Web** _(concept)_
: Tim Berners-Lee's vision (1994-present) for a machine-readable web of structured data using RDF/OWL/SPARQL — partially realized in enterprise settings and projects like Wikidata, but never achieving mass adoption due to formalization costs.
: See [[concepts/semantic-web]]

**Semiconductor Supply Chain** _(concept)_
: The global AI chip supply chain centered on TSMC (Taiwan) for advanced manufacturing — SMIC (China) constrained to 7nm, creating a 2+ generation gap; Taiwan's position makes it geopolitically critical to the AI race.
: See [[concepts/semiconductor-supply-chain]]

**Sentence Transformers** _(entity: tool)_
: The leading open-source Python library for text embeddings (Hugging Face): provides pretrained models (all-MiniLM-L6-v2, mpnet), training utilities (MatryoshkaLoss, contrastive losses), and a simple encode() API.
: See [[entities/sentence-transformers]]

**SentencePiece** _(concept)_
: A language-agnostic tokenization library that applies BPE or Unigram directly on raw text streams — critical for languages like Chinese and Japanese that lack whitespace word boundaries.
: See [[concepts/sentencepiece]]

**SGLang** _(entity: tool)_
: Open-source LLM serving framework and 2026 throughput leader: RadixAttention achieves 85-95% cache hit rates and 16,215 tok/s on H100, beating vLLM by 29% for multi-turn and agentic workloads.
: See [[entities/sglang]]

**SharePoint** _(entity: tool)_
: Microsoft's enterprise content management platform serving 190M+ users across 200,000 organizations. Granular permissions (site, list, item levels), extensive compliance certifications (HIPAA). Requires Microsoft 365 Copilot ($30/user/month) for AI features. Best fit for regulated enterprises in the Microsoft ecosystem.
: See [[entities/sharepoint]]

**Sim-to-Real Transfer** _(concept)_
: Training robot policies in simulation and deploying in the real world — addressing the persistent gap via domain randomization, digital twins, synthetic data at scale (NVIDIA: 780K trajectories in 11h), and curriculum learning; AutoMate achieves only 4.2% sim-to-real gap on assembly.
: See [[concepts/sim-to-real-transfer]]

**Simon Willison** _(entity: person)_
: Creator of Datasette and the LLM CLI tool — champions structured data extraction as 'the single most commercially valuable application of LLMs.'
: See [[entities/simon-willison]]

**Sleep Consolidation in AI** _(concept)_
: Implementing biological sleep-like offline phases in neural networks — using Hebbian replay, NREM/REM-inspired alternation, and SWR-BARR dynamics to consolidate memories and prevent catastrophic forgetting.
: See [[concepts/sleep-consolidation-ai]]

**Sliding Window Attention** _(concept)_
: Sparse attention restricting each token to attend only to the W most recent tokens, bounding KV cache size while leveraging layer stacking for an effective receptive field of W * n_layers.
: See [[concepts/sliding-window-attention]]

**Small Language Models (SLMs)** _(concept)_
: Models under 10B parameters (Phi-4, Gemma 3, Qwen 3 4B) that run on 4GB RAM with quantization, achieving 10-30x cost reduction vs. LLMs while handling many practical tasks.
: See [[concepts/small-language-models]]

**Smart Connections** _(entity: tool)_
: Leading free Obsidian AI plugin using RAG to enable conversational queries across the entire vault — works with local (Ollama) and cloud models.
: See [[entities/smart-connections]]

**Software 2.0** _(concept)_
: Karpathy's 2017 paradigm: neural networks as a new programming model where datasets replace source code, training replaces compilation, and data curation replaces instruction-writing -- the intellectual foundation for vibe coding and the code-to-knowledge shift.
: See [[concepts/software-2-0]]

**Sora** _(entity: tool)_
: OpenAI's text-to-video model that pioneered the 'video generation as world simulation' thesis; Sora 2 (Sep 2025) improved physics and controllability; discontinued March 2026 after falling to #7 on Video Arena behind Runway and Google.
: See [[entities/sora]]

**Spaced Repetition** _(concept)_
: A learning technique that combats the forgetting curve through adaptively scheduled review — essential complement to PKM systems that build connections (Zettelkasten, evergreen notes) by ensuring knowledge is actually retainable and recallable.
: See [[concepts/spaced-repetition]]

**Sparse Attention** _(concept)_
: Attention mechanisms computing only a subset of the full N x N token interactions — via fixed patterns (Longformer), block routing, clustering, or periodic strides — reducing quadratic complexity toward linear.
: See [[concepts/sparse-attention]]

**Sparse Coding** _(concept)_
: A neural coding strategy where only a small fraction of neurons are active for any given input — the brain's solution for energy-efficient, high-capacity information representation, now applied to AI for 10-1000x efficiency gains.
: See [[concepts/sparse-coding]]

**Spec-Driven Development** _(concept)_
: The practice of writing detailed specification documents (spec.md, requirements.md) before AI code generation — described as 'waterfall in 15 minutes' — eliminating 80% of AI confusion and serving as contracts between humans and agents.
: See [[concepts/spec-driven-development]]

**Speculative Decoding** _(concept)_
: A latency optimization pairing a small draft model with a large target model: the draft proposes tokens, the target verifies in parallel, achieving 2-3x speedup with mathematically guaranteed output equivalence.
: See [[concepts/speculative-decoding]]

**SPLADE (Sparse Lexical and Expansion Model)** _(concept)_
: A learned sparse retrieval model using transformer encoding to generate sparse vectors with vocabulary expansion — outperforms BM25 on BEIR benchmarks while maintaining inverted index compatibility.
: See [[concepts/splade]]

**SQLite** _(entity: tool)_
: A lightweight, serverless relational database used as the structural storage layer in Gallagher's Knowledge Graph Kit for personal knowledge management.
: See [[entities/sqlite]]

**Stable Diffusion** _(entity: tool)_
: The model family that democratized AI image generation from 2022 -- evolving from U-Net + DDPM (SD 1.x/2.x/XL) to MMDiT + flow matching (SD 3.5), retaining the largest fine-tuning ecosystem (thousands of LoRAs) despite being surpassed by FLUX in raw quality.
: See [[entities/stable-diffusion]]

**State Space Models (SSMs)** _(concept)_
: Sequence models based on continuous-time state equations, offering linear-time inference and fixed memory — the primary architectural alternative to transformers, especially for long sequences and raw data.
: See [[concepts/state-space-models]]

**Static Site Generators** _(concept)_
: Hugo, Jekyll, Astro, Eleventy, Gatsby, and Next.js all consume markdown as their primary content format — making markdown the default authoring language for the modern web.
: See [[concepts/static-site-generators]]

**Steph Ango** _(entity: person)_
: CEO of Obsidian, designer, and writer — articulated the 'file over app' philosophy, vault separation pattern, and a bottom-up approach to PKM with fractal journaling.
: See [[entities/steph-ango]]

**STORM** _(entity: paper)_
: A research system for automated Wikipedia-style article creation using multi-perspective question-asking and retrieval-based outline synthesis.
: See [[entities/storm]]

**StreamingLLM** _(entity: framework)_
: MIT HAN Lab framework enabling LLMs to generate over infinite-length sequences by preserving attention sink tokens plus a rolling KV window — no fine-tuning required, validated across Llama-2, MPT, Falcon, and Pythia up to 4M+ tokens with 22.2x speedup.
: See [[entities/streamingllm]]

**Structured Data Extraction (Schema.org)** _(concept)_
: Extracting pre-structured data (JSON-LD, Microdata, RDFa) from web pages using Schema.org vocabularies — 45M+ domains provide machine-readable entities and metadata that bypass heuristic extraction entirely.
: See [[concepts/structured-data-extraction]]

**Structured Output Extraction** _(concept)_
: Forcing LLM outputs into schema-conformant JSON/objects via constrained decoding (FSM) or validation-retry loops — the production backbone of all extraction pipelines.
: See [[concepts/structured-output-extraction]]

**Structured Output Prompting** _(concept)_
: Techniques for getting LLMs to produce predictable, parseable output formats (JSON, XML, Markdown tables) — essential for production systems that programmatically consume model outputs.
: See [[concepts/structured-output-prompting]]

**Subword Tokenization** _(concept)_
: The dominant tokenization paradigm for modern LLMs — splitting text into units between words and characters, keeping frequent words intact while decomposing rare words into meaningful subword pieces.
: See [[concepts/subword-tokenization]]

**Suno** _(entity: tool)_
: Leading AI music generation platform with ~100M users and $2.4B+ valuation -- Suno v5 outputs at 44.1kHz with 12-track stem separation, MIDI export, and a built-in Studio DAW, excelling in vocal synthesis for pop, rock, and R&B.
: See [[entities/suno]]

**Superalignment** _(concept)_
: The challenge of aligning AI systems that exceed human intelligence — requiring new approaches beyond RLHF, including scalable oversight, interpretability, and adversarial testing — with potentially civilization-level stakes.
: See [[concepts/superalignment]]

**Surya OCR** _(entity: tool)_
: High-performance multilingual OCR toolkit by Vik Paruchuri: YOLOv5 text detection, Transformer recognition across 90+ languages, graph neural network layout analysis, 15-20% improvement over commercial tools on complex tables.
: See [[entities/surya-ocr]]

**SWE-bench** _(concept)_
: Primary benchmark for evaluating LLM software engineering agents on real-world GitHub issues, progressing from 1.96% (2024) to 80.9% (Claude Opus 4.5, 2026) on Verified subset.
: See [[concepts/swe-bench]]

**SWE-bench** _(entity: dataset)_
: The dominant benchmark for AI software engineering agents -- real GitHub issues from production Python repos -- showing 59% improvement from 48.5% (GPT-4, 2023) to 80.8% (Opus 4.6, 2026) in under two years.
: See [[entities/swe-bench]]

**Switch Transformer** _(entity: paper)_
: Google's 2021 MoE model scaling to 1.6T parameters with 2048 experts using simplified single-expert routing — 4x pretraining speedup over T5-XXL, demonstrating MoE scaling viability.
: See [[entities/switch-transformer]]

**Sycophancy** _(concept)_
: An RLHF failure mode where models learn to match user beliefs and flatter rather than inform, because belief-matching is the strongest predictor of human approval in preference data.
: See [[concepts/sycophancy]]

**Symbolic AI** _(concept)_
: The paradigm (1950s-present) that intelligence arises from manipulating human-readable symbols via logic and rules — dominant through the 1980s, eclipsed by deep learning, now resurging via neural-symbolic hybrid approaches.
: See [[concepts/symbolic-ai]]

**Symbolic vs. Connectionist Debate** _(concept)_
: AI's central paradigm war: whether intelligence arises from symbol manipulation (logic, rules) or distributed numerical computation (neural networks) — now largely resolved toward complementarity via the System 1/System 2 analogy.
: See [[concepts/symbolic-vs-connectionist]]

**Synthetic Data Generation** _(concept)_
: Using LLMs to generate training data at scale — from textbook-quality corpora to instruction-following datasets — with quality filtering as the critical success factor.
: See [[concepts/synthetic-data-generation]]

**Synthetic Data in Pretraining** _(concept)_
: Using LLM-generated data to augment natural web text in pretraining — optimal at ~30% rephrased synthetic mixed with ~70% natural data, but pure synthetic or textbook-style data shows model collapse risks.
: See [[concepts/synthetic-data-in-pretraining]]

**System 1 / System 2 Thinking in LLMs** _(concept)_
: Applying Kahneman's dual-process theory to LLMs: standard models as System 1 (fast, intuitive, cheap) vs. reasoning models as System 2 (slow, deliberate, expensive) -- with hybrid toggle approaches emerging as the practical optimum.
: See [[concepts/system-1-system-2-thinking]]

**System Prompt Design** _(concept)_
: Architectural patterns for system prompts that define consistent LLM behavior, roles, and constraints — the foundation layer that shapes all subsequent interactions.
: See [[concepts/system-prompt-design]]

## T

**T5 (Text-to-Text Transfer Transformer)** _(entity: paper)_
: Google's 2019 encoder-decoder transformer converting all NLP tasks to text-to-text format — 220M to 11B parameters, trained on C4 with span denoising, basis for Switch Transformer.
: See [[entities/t5]]

**Tacit Knowledge Capture** _(concept)_
: The capture of experiential, undocumented knowledge that exists only in employees' heads. Historically the hardest KM challenge. AI note-taking, automated transcription, and meeting platforms now make enterprise-scale tacit knowledge programs feasible for the first time. Critical because tacit knowledge walks out the door with employee turnover.
: See [[concepts/tacit-knowledge-capture]]

**Ted Nelson** _(entity: person)_
: American information technology pioneer (b. 1937) who coined 'hypertext' in 1965, founded Project Xanadu (1960), and envisioned bidirectional links, transclusion, and micropayments decades before the web.
: See [[entities/ted-nelson]]

**Templater** _(entity: tool)_
: Obsidian's advanced templating plugin (230K+ installs): dynamic variables, JavaScript execution, file manipulation, conditional logic, and user prompts — the automation backbone of power-user workflows.
: See [[entities/templater]]

**Temporal Knowledge** _(concept)_
: Graphiti's core contribution: representing knowledge with temporal validity windows (when a fact became true and when it was superseded) rather than treating facts as eternally true or false — critical for AI agents in dynamic environments.
: See [[concepts/temporal-knowledge]]

**Temporal Knowledge Graphs** _(concept)_
: Knowledge graphs that associate facts with explicit temporal information (timestamps or intervals), enabling reasoning about what was true when — with 10+ method categories from translation-based to LLM-integrated approaches.
: See [[concepts/temporal-knowledge-graphs]]

**Tensor Parallelism** _(concept)_
: Intra-layer parallelism that splits individual weight matrices across GPUs — communication-intensive but essential for models that exceed single-GPU memory. Best within nodes using high-bandwidth NVLink interconnects.
: See [[concepts/tensor-parallelism]]

**Tesla** _(entity: org)_
: Electric vehicle and AI company where Karpathy served as Director of AI (2017-2022), leading the Autopilot Vision team — Software 2.0 at industrial scale.
: See [[entities/tesla]]

**Tesla Optimus** _(entity: tool)_
: Tesla's general-purpose humanoid robot; Gen 3 (22 DOF hands) entering production summer 2026; shares AI with Full Self-Driving; 5'8\", 125 lb; target price under $20K long-term; faces criticism for teleoperation-dependent demos and timeline exaggeration.
: See [[entities/tesla-optimus]]

**Test-Time Compute Scaling** _(concept)_
: The paradigm of allocating additional computation at inference time (rather than training time) to improve reasoning -- enabling small models to outperform 14x larger models and forming the computational foundation of reasoning models like o1, o3, and R1.
: See [[concepts/test-time-compute]]

**Test-Time Training** _(concept)_
: Modifying model weights at inference time using unlabeled test data -- distinct from test-time scaling (which only changes inference procedure) -- via RL on majority-voted rewards (TTRL) or self-supervised perplexity minimization (TLM), achieving 20-211% improvements.
: See [[concepts/test-time-training]]

**Text Embeddings** _(concept)_
: Dense vector representations of text that capture semantic meaning, enabling similarity-based retrieval; the foundation of modern semantic search, RAG, and vector database infrastructure.
: See [[concepts/text-embeddings]]

**TextGrad** _(entity: tool)_
: Gradient-based prompt optimization framework that uses natural language feedback instead of numeric scores — published in Nature (2025), excels at instance-level refinement for coding and scientific Q&A.
: See [[entities/textgrad]]

**The Shape of AI** _(entity: tool)_
: Community-maintained catalog of 57 AI UX design patterns organized into six categories (Wayfinders, Prompt Actions, Tuners, Governors, Trust Builders, Identifiers) — the most comprehensive open taxonomy of AI interaction patterns.
: See [[entities/shape-of-ai]]

**The Stochastic Parrot Debate** _(concept)_
: The ongoing debate about whether LLMs genuinely reason and understand or merely perform sophisticated statistical pattern matching -- with evidence on both sides from reasoning benchmarks, adversarial tests, mechanistic interpretability, and philosophical analysis.
: See [[concepts/stochastic-parrot-debate]]

**ThinkPRM** _(entity: paper)_
: Generative process reward model that verifies reasoning by generating verification CoT, requiring only 1% of PRM800K labels while outperforming discriminative PRMs -- extending the 'thinking' paradigm to verification.
: See [[entities/thinkprm]]

**Tiago Forte** _(entity: person)_
: Productivity consultant and author who created the Building a Second Brain (BASB) methodology, including the PARA organizational system and Progressive Summarization technique — the most popular PKM framework globally.
: See [[entities/tiago-forte]]

**tiktoken** _(entity: tool)_
: OpenAI's fast BPE tokenizer library, written in Rust with a Python API — the standard tool for counting tokens for GPT models.
: See [[entities/tiktoken]]

**Token Counting** _(concept)_
: Practical techniques for counting and estimating token usage in LLM applications — critical for cost management, context window budgeting, and prompt engineering.
: See [[concepts/token-counting]]

**Token Optimization** _(concept)_
: Systematic reduction of token consumption through prompt compression, output constraints, conversation history management, and context assembly optimization — cutting 20-40% of token waste without infrastructure changes.
: See [[concepts/token-optimization]]

**Tokenization** _(concept)_
: The process of converting raw text into discrete integer tokens that LLMs can process — the fundamental first step in all language model pipelines.
: See [[concepts/tokenization]]

**Tool Use (Function Calling)** _(concept)_
: The mechanism by which LLM agents interact with external systems: generating structured function calls that a runtime executes, standardized via MCP.
: See [[concepts/tool-use]]

**Tool Use Standards for LLMs** _(concept)_
: The evolving landscape of standards for connecting LLMs to external tools: from vendor-specific function calling (2023) through universal MCP (2024-2025) to the six-protocol agent stack (2026) covering tools, agents, commerce, payments, UI, and streaming.
: See [[concepts/tool-use-standards]]

**Trafilatura** _(entity: tool)_
: The most accurate open-source web text extraction library — Python package combining jusText and Readability algorithms, outputting to markdown/JSON/XML-TEI, used by HuggingFace, IBM, Microsoft Research.
: See [[entities/trafilatura]]

**Training Data Curation** _(concept)_
: The process of transforming raw web crawls into high-quality LLM training datasets through text extraction, heuristic filtering, model-based quality scoring, deduplication, and data mixing — the single highest-leverage activity in LLM development.
: See [[concepts/training-data-curation]]

**Training Infrastructure** _(concept)_
: The GPU clusters, networking, and storage systems required for LLM pretraining: NVIDIA H100/H200/B200 GPUs, NVLink intra-node (900 GB/s), InfiniBand inter-node, with frontier runs using 5,000-16,000+ GPUs.
: See [[concepts/training-infrastructure]]

**Training Stability** _(concept)_
: Keeping LLM training runs from diverging over weeks/months: preventing loss spikes via gradient clipping, proper initialization, BFloat16 precision, learning rate warmup, and specialized optimizers (SPAM, LAMB).
: See [[concepts/training-stability]]

**Training vs Inference Hardware** _(concept)_
: AI compute is bifurcating: training (compute-bound, GPU-dominated) vs inference (bandwidth-bound, 2/3 of spend by 2026); specialized inference ASICs deliver 10-100x speedups over GPUs, creating a new market segment projected to capture 45% of inference by 2030.
: See [[concepts/training-vs-inference-hardware]]

**Training-Time vs. Inference-Time Compute** _(concept)_
: The fundamental paradigm shift in AI from 'train bigger models' to 'reason harder at inference' -- with inference demand projected to exceed training by 118x by 2026 and reshaping the entire AI infrastructure landscape.
: See [[concepts/training-vs-inference-compute]]

**Transactive Memory Systems** _(concept)_
: The distributed cognitive architecture of groups: who knows what, how to access distributed expertise, and how attention and reasoning are coordinated — now being augmented and threatened by AI in the COHUMAIN framework.
: See [[concepts/transactive-memory-systems]]

**Transclusion** _(concept)_
: Ted Nelson's concept of including content from one document inside another by reference rather than by copy — never widely adopted but anticipating modern content embedding, syndication, and wiki transclusion.
: See [[concepts/transclusion]]

**Transformer Architecture** _(concept)_
: The foundational neural network architecture based entirely on attention mechanisms, introduced in 'Attention Is All You Need' (2017), now powering virtually all frontier LLMs, vision models, and multimodal systems.
: See [[concepts/transformer-architecture]]

**Tree of Thoughts** _(concept)_
: A reasoning framework (NeurIPS 2023) that generalizes chain-of-thought by exploring multiple reasoning paths via tree search (BFS/DFS), enabling backtracking and self-evaluation -- achieving 74% on Game of 24 vs. CoT's 4%.
: See [[concepts/tree-of-thought]]

**Tree of Thoughts Prompting** _(concept)_
: Yao et al. (2023) framework that generalizes CoT into a tree-structured exploration of reasoning paths with search algorithms (BFS/DFS), enabling deliberate problem-solving with lookahead and backtracking.
: See [[concepts/tree-of-thoughts-prompting]]

**Tri Dao** _(entity: person)_
: Co-creator of FlashAttention (IO-aware attention optimization) and Mamba (selective state space models) — two of the most impactful systems contributions to modern LLM efficiency.
: See [[entities/tri-dao]]

**TRL (Transformers Reinforcement Learning)** _(entity: tool)_
: HuggingFace's library for LLM alignment training, supporting SFT, PPO, DPO, IPO, KTO, and ORPO -- the de facto standard open-source toolkit for preference optimization.
: See [[entities/trl]]

**Trust Calibration** _(concept)_
: The research field studying how to match user reliance on AI with actual AI reliability — the engagement-overload paradox means more explanation can backfire, requiring careful interface calibration.
: See [[concepts/trust-calibration]]

**Trust in AI** _(concept)_
: Trust is the true currency of AI products — built through transparency, appropriate friction, citations, confidence signals, and consistent competence over time; both over-trust (automation bias) and under-trust are failure modes.
: See [[concepts/trust-in-ai]]

**TruthfulQA** _(entity: dataset)_
: 817-question benchmark testing whether LLMs propagate common misconceptions; notable for revealing that state-of-the-art models score 'surprisingly low on truthfulness.'
: See [[entities/truthfulqa]]

**TTRL (Test-Time Reinforcement Learning)** _(entity: paper)_
: NeurIPS 2025 paper demonstrating RL training on unlabeled test data using majority voting as reward signal, achieving 211% improvement on AIME -- bridging test-time scaling and test-time training.
: See [[entities/ttrl]]

**Two-Stage Retrieval** _(concept)_
: The standard RAG retrieval architecture: fast bi-encoder/hybrid retrieval narrows millions of documents to top-k candidates, then a cross-encoder reranker selects the top-n most relevant for the LLM.
: See [[concepts/two-stage-retrieval]]

## U

**Udio** _(entity: tool)_
: AI music generation platform by ex-Google DeepMind engineers -- audio fidelity rated 'almost indistinguishable from real recordings,' with inpainting for selective song section regeneration; settled with UMG (Oct 2025) and Warner (Nov 2025).
: See [[entities/udio]]

**Unigram Tokenization** _(concept)_
: Top-down probabilistic tokenization algorithm that starts with a large candidate vocabulary and iteratively prunes the least impactful tokens — used by T5, BigBird, and Pegasus.
: See [[concepts/unigram-tokenization]]

**Unstructured.io** _(entity: tool)_
: Open-source Python library (Apache 2.0) for document ETL: partition() auto-detects 30+ formats, outputs typed semantic elements, four processing strategies, 14.4k GitHub stars, enterprise platform processes 15M pages/hour.
: See [[entities/unstructured-io]]

**US-China AI Race** _(concept)_
: The defining geopolitical competition of the AI era — US leads in model quality (7-month average gap), market share (93%), compute (5-17x chip advantage), and capital ($250B Q1 2026); China closing via algorithmic efficiency, open source strategy, and state-backed ecosystem.
: See [[concepts/us-china-ai-race]]

## V

**Vannevar Bush** _(entity: person)_
: American engineer and science administrator who envisioned the Memex in 1945 -- a proto-hypertext personal knowledge device that prefigured modern LLM knowledge bases by 80 years.
: See [[entities/vannevar-bush]]

**Vault Organization Strategies** _(concept)_
: Strategies for organizing Obsidian vaults: flat folders + profuse links (Ango), PARA method, type-based folders, and AI-optimized architectures with context engineering.
: See [[concepts/vault-organization]]

**Vault Separation** _(concept)_
: Steph Ango's (Obsidian CEO) recommendation to maintain a clean human-curated Obsidian vault separately from agent-generated content, preventing hallucination contamination of personal knowledge.
: See [[concepts/vault-separation]]

**Vector Databases** _(concept)_
: Specialized databases for approximate nearest-neighbor (ANN) search over embedding vectors, necessary at billion-vector scale but often overkill for personal or team-scale LLM knowledge bases where pgvector, FAISS, or index-based LLM navigation suffice.
: See [[concepts/vector-databases]]

**Vector Search** _(concept)_
: Finding similar items by computing distance between dense vector embeddings in high-dimensional space, typically using ANN algorithms like HNSW for sub-millisecond retrieval at scale.
: See [[concepts/vector-search]]

**Veo** _(entity: tool)_
: Google DeepMind's video generation model -- Veo 3 introduced native synchronized audio generation (effects, dialogue, ambient) from text in early 2026; Veo 3.1 Lite at $0.05/second is the most affordable AI video option, with YouTube and Vertex AI integration.
: See [[entities/veo]]

**Vespa.ai** _(entity: tool)_
: Yahoo's hybrid search engine combining vector, keyword, and metadata search with multi-vector indexing -- described as underappreciated in the HN vector database debate.
: See [[entities/vespa]]

**Vibe Coding** _(concept)_
: Karpathy's February 2025 term for natural-language-driven development with minimal code review -- Collins Word of the Year 2025 -- which followed a clear arc from excitement to 'hangover' to Karpathy himself declaring it passe in favor of agentic engineering.
: See [[concepts/vibe-coding]]

**Video Generation** _(concept)_
: AI systems generating video from text or image inputs -- a $847M market in 2026 growing at 34.2% CAGR, shaped by Sora's shutdown and the rise of Runway Gen-4, Kling 3.0, and Veo 3 with native audio generation.
: See [[concepts/video-generation]]

**Video Generation as World Simulation** _(concept)_
: The hypothesis that scaling video generation trains implicit world simulators — pioneered by OpenAI's Sora, validated by emergent 3D consistency and physics at scale, but challenged by fundamental gaps between statistical video prediction and true causal world modeling.
: See [[concepts/video-generation-as-world-simulation]]

**Virtual Context Management** _(concept)_
: OS-inspired technique where LLMs page information between in-context memory (RAM) and external storage (disk), creating the illusion of unlimited context within fixed windows.
: See [[concepts/virtual-context-management]]

**Vision-Language Models** _(concept)_
: Models that jointly process images and text — from CLIP's dual encoders to GPT-4V/Claude/Qwen3-VL's vision-integrated LLMs; by 2026, open-source VLMs rival proprietary frontier models.
: See [[concepts/vision-language-models]]

**Vision-Language-Action (VLA) Models** _(concept)_
: Neural architectures that unify visual perception, language understanding, and motor control in a single model — the core enabling technology for embodied AI, evolving from RT-2 (2023) through π0 and GR00T-N1 to general-purpose robot control.
: See [[concepts/vision-language-action-models]]

**Visual Question Answering** _(concept)_
: AI task of answering natural language questions about images — considered 'AI-complete'; evolved from CNN+LSTM+attention to VLM-based approaches achieving 82%+ on key benchmarks.
: See [[concepts/visual-question-answering]]

**Visual Tokenization** _(concept)_
: Methods for converting images into discrete or continuous token sequences for autoregressive generation -- evolving from VQ-VAE (2017) through VQGAN (2021) to continuous tokens (2025), with MAGVIT-v2 showing 'the tokenizer is the key' to matching diffusion quality.
: See [[concepts/visual-tokenization]]

**vLLM** _(entity: tool)_
: Production-grade LLM inference engine using PagedAttention — achieves 793 TPS on A100 (vs Ollama's 41), best for multi-user and enterprise local deployments.
: See [[entities/vllm]]

**Vocabulary Size Tradeoffs** _(concept)_
: The fundamental tension between vocabulary size, sequence length, embedding overhead, and language coverage — with modern LLMs trending from 32k toward 100k-131k tokens.
: See [[concepts/vocabulary-size-tradeoffs]]

## W

**Wafer-Scale Computing** _(concept)_
: Cerebras's radical approach: using an entire 300mm silicon wafer as a single processor (46,225 mm², 4 trillion transistors, 900,000 cores) — eliminating inter-chip communication and the memory bandwidth wall for models that fit in 44GB on-chip SRAM.
: See [[concepts/wafer-scale-computing]]

**Ward Cunningham** _(entity: person)_
: Inventor of the wiki (1995) and creator of Federated Wiki (2011) — which reimagines collaborative knowledge as 'a chorus of voices' with forking rather than consensus.
: See [[entities/ward-cunningham]]

**Waymo** _(entity: org)_
: Alphabet's autonomous driving subsidiary; completed 10M+ paid robotaxi rides by 2026; the most commercially advanced autonomous vehicle service globally.
: See [[entities/waymo]]

**Weaviate** _(entity: tool)_
: Cloud-native open-source vector database: highest QPS (791), native hybrid search with alpha parameter and BM25F, generative module for server-side RAG, HIPAA on AWS (2025).
: See [[entities/weaviate]]

**Web Archiving** _(concept)_
: Preserving web content in standardized WARC (ISO 28500) format for permanence and provenance — from institutional tools (Heritrix, Wayback Machine) to personal archiving (ArchiveBox, SingleFile) — critical for knowledge base source integrity.
: See [[concepts/web-archiving]]

**Web Scraping at Scale** _(concept)_
: Modern web scraping for AI pipelines: async concurrency, proxy rotation, headless browsers for JS, API-based services (Firecrawl, Crawl4AI) that output LLM-ready markdown, and scaling from scripts to microservice architectures.
: See [[concepts/web-scraping-at-scale]]

**Web Scraping Ethics and Law** _(concept)_
: Legal framework for web scraping: public data is generally legal (hiQ v. LinkedIn); GDPR imposes EUR 20M fines for personal data; EU AI Act requires training data provenance; robots.txt compliance is legally relevant though not binding.
: See [[concepts/web-scraping-ethics-and-law]]

**Weights vs. Context Window: Where to Put Knowledge** _(concept)_
: The fundamental design question for LLM applications: which knowledge belongs in model weights (persistent, fast, opaque) vs. context windows (dynamic, traceable, limited) vs. external tools.
: See [[concepts/weights-vs-context]]

**Wiki Compilation** _(concept)_
: The LLM-driven pipeline that converts raw ingested documents into a structured, cross-linked markdown wiki with source summaries and concept articles.
: See [[concepts/wiki-compilation]]

**Wikidata** _(entity: tool)_
: Wikimedia's collaboratively edited structured knowledge base — 100M+ items in semantic triple format, linked to 7,500+ external databases, forming the backbone of federated knowledge graph infrastructure.
: See [[entities/wikidata]]

**Wikipedia** _(entity: org)_
: The world's largest collaboratively edited encyclopedia (60M+ articles, 300+ languages) — paradigmatic example of collective intelligence and knowledge commons, now navigating the AI crisis of content generation, training data extraction, and declining visits.
: See [[entities/wikipedia]]

**Wikipedia Knowledge Model** _(concept)_
: Wikipedia's collaborative editorial model — anyone can edit, consensus-driven quality improvement, verifiability over truth, no original research — represents the most successful collective knowledge creation system in history, now under unprecedented stress from AI.
: See [[concepts/wikipedia-knowledge-model]]

**Wisdom of Crowds** _(concept)_
: Aggregated independent judgments from diverse groups outperform individual experts — mathematically formalized by Page's Diversity Prediction Theorem — but requiring conditions (diversity, independence, decentralization, aggregation) that AI both enables and threatens.
: See [[concepts/wisdom-of-crowds]]

**WordPiece** _(concept)_
: BERT-family tokenization algorithm similar to BPE but merging token pairs that maximize training data likelihood rather than simple frequency — producing more linguistically informative merges.
: See [[concepts/wordpiece]]

**World Labs** _(entity: org)_
: AI startup founded by Fei-Fei Li; raised $230M, launched Marble (November 2025) for generating persistent 3D environments from text/images with VR support and game engine export.
: See [[entities/world-labs]]

**World Models** _(concept)_
: AI systems that build internal representations of reality to simulate, predict, and plan — the emerging paradigm challenging LLMs as the path to general intelligence, with $1.3B+ in 2026 funding across AMI Labs, DeepMind, NVIDIA, and World Labs.
: See [[concepts/world-models]]

## Y

**YAML Frontmatter** _(concept)_
: YAML frontmatter is the de facto standard for embedding structured metadata in markdown files — enabling queryability, categorization, and machine processing while preserving plain-text readability.
: See [[concepts/yaml-frontmatter]]

**Yann LeCun** _(entity: person)_
: Turing Award winner (2018), former Meta FAIR VP/Chief AI Scientist, creator of JEPA, founder of AMI Labs ($1.03B seed at $3.5B valuation) — the most prominent advocate for world models over LLMs as the path to general intelligence.
: See [[entities/yann-lecun]]

**Yoshua Bengio** _(entity: person)_
: Turing Award winner and pioneer of deep learning; chaired the 2026 International AI Safety Report synthesizing evidence from 100+ experts across 30+ countries.
: See [[entities/yoshua-bengio]]

## Z

**ZenML** _(entity: tool)_
: An open-source MLOps pipeline orchestration framework used in the Decoding AI second-brain RAG system to manage offline data processing and training workflows.
: See [[entities/zenml]]

**Zep** _(entity: org)_
: The organization behind Graphiti, offering both an open-source temporal context graph engine and enterprise-grade managed infrastructure for AI agent memory.
: See [[entities/zep]]

**ZeRO Optimizer** _(concept)_
: DeepSpeed's Zero Redundancy Optimizer progressively shards optimizer states (Stage 1), gradients (Stage 2), and parameters (Stage 3) across data-parallel GPUs, reducing per-GPU memory by up to the parallelism degree while preserving data parallelism's simplicity.
: See [[concepts/zero-optimizer]]

**Zero-Shot Information Extraction** _(concept)_
: Extracting entities, relations, and structured data from text without any task-specific training examples — enabled by LLMs' general language understanding and instruction-following abilities.
: See [[concepts/zero-shot-information-extraction]]

**Zero-Shot Prompting** _(concept)_
: Direct instruction to an LLM without any demonstration examples — the simplest prompting approach, and the recommended starting point before reaching for more complex techniques.
: See [[concepts/zero-shot-prompting]]

**Zettelkasten** _(concept)_
: Niklas Luhmann's slip-box method for personal knowledge management: atomic, hypertextually linked notes that form a 'communication partner' for thinking — the foundational methodology behind modern networked note-taking tools.
: See [[concepts/zettelkasten]]

## Π

**π0 (Pi-Zero)** _(entity: paper)_
: Physical Intelligence's 3B-parameter VLA model using flow matching for 50Hz robot control; trained on 7-8 robot types across 68 tasks; first system to achieve complex dexterous tasks (laundry folding at 1.0 success); open-sourced via Hugging Face LeRobot.
: See [[entities/pi0]]
