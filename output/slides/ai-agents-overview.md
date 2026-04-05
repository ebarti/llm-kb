---
marp: true
theme: default
paginate: true
---

# AI Agents Overview
## LLM-Powered Autonomous Systems
### Architecture, Patterns, and Real-World Applications

---

## Agenda

1. What Are LLM Agents?
2. The Four-Component Architecture
3. The ReAct Pattern
4. Tool Use and Function Calling
5. Model Context Protocol (MCP)
6. Agent Memory Systems
7. Planning and Reflection
8. Andrew Ng's Four Design Patterns
9. Multi-Agent Systems
10. Agent Design Pattern Spectrum
11. Real-World Agent Applications
12. Challenges and Limitations

---

## What Are LLM Agents?

**LLM agents** are AI systems that combine an LLM with:
- **Planning** -- decompose complex problems into steps
- **Memory** -- retain information across interactions
- **Tools** -- interact with external systems and APIs
- **Reflection** -- evaluate and improve their own outputs

> "LLM agents represent sophisticated AI systems engineered to handle complex tasks requiring sequential reasoning capabilities."
> -- SuperAnnotate

---

## Agents vs LLMs vs RAG

| Capability | Raw LLM | RAG System | LLM Agent |
|-----------|---------|-----------|-----------|
| Static Q&A | Yes | Yes | Yes |
| External knowledge | No | Yes | Yes |
| Multi-step reasoning | Limited | No | **Yes** |
| Tool interaction | No | No | **Yes** |
| Self-correction | No | No | **Yes** |
| Persistent memory | No | No | **Yes** |
| Dynamic planning | No | No | **Yes** |

---

## The Four-Component Architecture

```
+--------------------------------------------------+
|                   LLM AGENT                       |
|                                                   |
|  +----------+  +---------+  +---------+  +------+ |
|  |  Brain   |  | Memory  |  |Planning |  | Tools| |
|  |  (LLM)   |  | STM+LTM |  |CoT/ToT  |  | APIs | |
|  +----------+  +---------+  +---------+  +------+ |
|                                                   |
|  System prompt defines role, constraints, format  |
+--------------------------------------------------+
```

1. **Brain**: the LLM foundation with customizable prompts
2. **Memory**: short-term (conversation) + long-term (cross-session)
3. **Planning**: formulation (CoT/ToT) + reflection (ReAct/Reflexion)
4. **Tools**: external APIs, databases, code execution

---

## The ReAct Pattern

**Yao et al. (2022)**: the foundational agent loop -- interleaving reasoning and acting.

```
Thought: I need to find the population of France.
Action: search("population of France 2026")
Observation: France has approximately 68.4 million people.

Thought: Now I need to compare with Germany.
Action: search("population of Germany 2026")
Observation: Germany has approximately 84.1 million people.

Thought: I can now answer the comparison question.
Answer: Germany (84.1M) has about 23% more people than France (68.4M).
```

---

## ReAct: Why It Works

| Approach | Strength | Weakness |
|----------|----------|----------|
| CoT only | Good reasoning | Hallucinates facts (no grounding) |
| Action only | Accesses real data | Poor planning (no reasoning trace) |
| **ReAct** | **Both reasoning + grounding** | **Mitigates both weaknesses** |

- Reasoning traces help the model **track and update plans**
- Actions allow **real-world information retrieval**
- **ReAct + Reflexion** completes **130/134 tasks** vs ReAct alone

---

## Tool Use and Function Calling

LLM agents interact with external systems via **function calling**:

```json
{
  "name": "search_knowledge_base",
  "description": "Search wiki articles by topic",
  "parameters": {
    "query": "string",
    "max_results": "integer"
  }
}
```

The LLM decides **when** to call tools and with **what parameters** -- not hardcoded.

**Frameworks**: MRKL (Modular Reasoning, Knowledge and Language), Toolformer, function calling APIs.

---

## Tool Use: Security Considerations

| Risk | Description | Mitigation |
|------|-------------|------------|
| Over-permissioning | Tool does more than needed | Principle of least privilege |
| Injection via tools | Malicious data in tool response | Sanitize tool outputs |
| Unauthorized actions | Agent takes harmful action | Human-in-the-loop for risky ops |
| Data exfiltration | Agent sends data to external APIs | Output filtering, sandboxing |
| Cost explosion | Agent calls expensive APIs in loop | Rate limiting, budget caps |

---

## Model Context Protocol (MCP)

**Anthropic (Nov 2024)**: open standard for LLM-to-tool integration.

**The problem**: M x N integration -- every AI app needs custom connectors for every data source.

**The solution**: universal protocol (like LSP for programming languages).

```
Host (LLM App)  -->  Client (Connector)  -->  Server (Tool/Data)
```

- **JSON-RPC 2.0** transport
- Server features: Resources, Prompts, Tools
- **97 million monthly SDK downloads** by December 2025
- Adopted by OpenAI, Google DeepMind, Microsoft
- Donated to **Linux Foundation** (December 2025)

---

## MCP Architecture

```
+-------------------+
|   Claude / GPT    |    Host
+-------------------+
         |
    MCP Protocol (JSON-RPC 2.0)
         |
+--------+---------+--------+
|        |         |        |
v        v         v        v
GitHub  Slack    Database  Search
Server  Server   Server    Server
```

Each MCP server exposes **tools**, **resources**, and **prompts** via a standard interface.

Security: user consent for all operations, data privacy, tool safety gates.

---

## Agent Memory: The Stateless Problem

LLMs are **stateless** -- they retain nothing between API calls.

**Agent memory systems** solve this:

| Memory Type | Scope | Duration | Analogy |
|-------------|-------|----------|---------|
| **Working** | Current task | Single session | RAM |
| **Short-term** | Conversation | Session | Cache |
| **Episodic** | Past experiences | Long-term | Event log |
| **Semantic** | Learned abstractions | Permanent | Knowledge |
| **Archival** | External storage | Permanent | Disk |

---

## AgeMem: Memory as Tool Use

**AgeMem (2026)**: unified framework exposing memory operations as callable tools:

| Operation | Description |
|-----------|-------------|
| `store()` | Save information to long-term memory |
| `retrieve()` | Search memory for relevant past context |
| `update()` | Modify existing memory entries |
| `summarize()` | Compress memories into abstractions |
| `discard()` | Remove outdated or irrelevant memories |

Trained via **three-stage reinforcement learning** -- the agent learns **when and what** to memorize.

---

## MemGPT: Virtual Context Management

**OS-inspired** approach to agent memory:

```
+----------------------------+
|  Core Memory (in-context)  |  <-- "RAM" (always available)
+----------------------------+
|  Recall Memory (search)    |  <-- "Cache" (recent conversations)
+----------------------------+
|  Archival Memory (vector)  |  <-- "Disk" (everything ever stored)
+----------------------------+
```

The agent **pages** information in and out of context, like an OS manages virtual memory.

Evolved into the **Letta platform** for production deployment.

---

## Hierarchical Memory (H-MEM)

**EACL 2026**: four-layer architecture inspired by human cognition:

1. **Buffer** -- raw recent interactions
2. **Working Memory** -- current task context (limited capacity)
3. **Episodic Memory** -- past experience summaries
4. **Semantic Memory** -- abstracted, generalized knowledge

**Sleep-time compute**: during idle periods, the agent consolidates episodic memories into semantic knowledge -- analogous to human memory consolidation during sleep.

---

## Planning: How Agents Think

| Planning Method | Description | Use Case |
|----------------|-------------|----------|
| **Chain of Thought** | Linear step-by-step reasoning | General reasoning |
| **Tree of Thoughts** | Branching exploration with backtracking | Complex planning |
| **ReAct** | Interleaved reasoning + action | Information-gathering tasks |
| **Reflexion** | Self-critique and retry | Learning from mistakes |
| **Plan-and-Execute** | Generate full plan, then execute | Multi-step workflows |

---

## The Reflection Pattern

**Andrew Ng**: "relatively quick to implement with surprising performance gains."

```
Generator Agent                    Critic Agent
     |                                  |
     +--- Generate draft output ------->|
     |                                  |
     |<-- Critique: "Missing X, Y" ----+
     |                                  |
     +--- Revised output with X, Y --->|
     |                                  |
     |<-- "Approved" ------------------+
     |
     v
  Final Output
```

Can be extended with **tool integration** (e.g., run code against tests, verify claims).

---

## Andrew Ng's Four Design Patterns

| Pattern | Description | Key Insight |
|---------|-------------|-------------|
| **Reflection** | Generate, critique, refine | Quick to implement, high ROI |
| **Tool Use** | Access external APIs and data | Grounds reasoning in reality |
| **Planning** | Decompose into sub-tasks | Enables complex workflows |
| **Multi-Agent** | Specialized agents collaborate | Division of labor |

> "GPT-3.5 with an agentic workflow could outperform a more advanced model like GPT-4 using a zero-shot approach."

**Architecture > Model Size**.

---

## Multi-Agent Systems

**2025 survey**: five-dimension taxonomy of multi-agent collaboration:

| Dimension | Options |
|-----------|---------|
| Actors | Homogeneous vs heterogeneous agents |
| Types | Cooperation, competition, **coopetition** |
| Structures | Peer-to-peer, centralized, distributed |
| Strategies | Task decomposition, debate, voting |
| Protocols | Natural language, structured messages |

**Key insight**: natural language as universal coordination medium enables **emergent behaviors**.

---

## Multi-Agent Orchestration Patterns

| Pattern | Description | When to Use |
|---------|-------------|-------------|
| **Orchestrator-Worker** | Central planner assigns tasks | Most deployed in production |
| **Supervisor** | Monitor evaluates worker outputs | Quality-critical tasks |
| **Router** | Dispatch to specialized agents | Varied query types |
| **Debate** | Agents argue to refine answers | High-stakes decisions |
| **Pipeline** | Sequential agent handoffs | Document processing |

**Frameworks**: CAMEL (role-playing), AutoGen (flexible), CrewAI (task-oriented).

---

## Agent Design Pattern Spectrum (Databricks)

```
Simple -----------------------------------------> Complex

LLM + Prompt      Chain           Single Agent    Multi-Agent
     |               |                 |               |
  Direct call    Deterministic     Dynamic logic    Orchestrated
  No tools       Fixed pipeline    Tool selection   Specialized roles
  No memory      No branching      ReAct loop       State sharing
     |               |                 |               |
  Chatbots      Document proc.    Research agents   Enterprise AI
```

**Best practice**: start with simplest pattern, add complexity gradually.

---

## Single Agent: Often Optimal

Databricks highlights the **single-agent system** as often optimal for enterprise:

- Complex enough for **dynamic decision-making**
- Simpler than multi-agent overhead
- One LLM with tools, memory, and ReAct loop
- Easier to debug, monitor, and maintain
- Sufficient for most real-world use cases

**Multi-agent** is justified when:
- Tasks require genuinely different expertise
- Parallel processing provides speed benefits
- Quality benefits from adversarial review

---

## Real-World Agent Applications

| Domain | Agent Application | Key Benefit |
|--------|------------------|-------------|
| Software engineering | Devin, Claude Code | Autonomous coding |
| Knowledge management | KARMA (9 agents) | Automated KG enrichment |
| Research | STORM | Multi-perspective article generation |
| Customer support | RAG + tool-use agents | Contextual, action-capable |
| Data analysis | Code interpreter agents | Automated EDA + visualization |
| Document processing | Pipeline agents | Multi-format extraction |

---

## Devin: Autonomous Software Engineer

**First autonomous AI software engineer** (2024):

- Plans, codes, debugs, and deploys autonomously
- SWE-bench progression: proof that agents can handle real software tasks
- Uses long-running shell sessions, browser, and code editor
- Demonstrates the full agent loop: plan, execute, observe, reflect, iterate

**Claude Code** (Anthropic): $2.5B revenue in 2025, eight trends in agentic coding.

---

## KARMA: 9-Agent KG Enrichment

**NeurIPS 2025 Spotlight**: multi-agent knowledge graph construction.

```
  Paper 1 ----+
  Paper 2 ----+---> [9 Collaborative Agents] ---> Knowledge Graph
  Paper 3 ----+          |
  ...                    |
  Paper 1200             v
                  83.1% accuracy
                  38,230 new entities
                  18.6% conflict reduction
```

Specialized agents: entity discovery, relation extraction, schema alignment, conflict resolution, verification, integration, coordination.

---

## Challenges and Limitations

| Challenge | Description | Mitigation |
|-----------|-------------|------------|
| Context window limits | Agent loses track of long tasks | Hierarchical memory (H-MEM) |
| Planning horizon | Difficulty maintaining extended plans | Plan-and-execute, checkpoints |
| Output inconsistency | Non-deterministic behavior | Self-consistency, validation |
| Resource costs | Many LLM calls per task | Caching, smaller models for routing |
| Hallucination in actions | Agent acts on false beliefs | Grounding via tool use, verification |
| Coordination overhead | Multi-agent communication costs | Start with single agent |

---

## The Agentic AI Framework Landscape

**Three paths in autonomous AI** (Pebblous):

1. **Reinforcement Learning**: agents learn from environment feedback
2. **Self-Improvement**: agents optimize their own prompts and tools
3. **TDD Frameworks**: test-driven development patterns for agent reliability

**The explosion**: dozens of frameworks (LangChain, LlamaIndex, CrewAI, AutoGen, Haystack, Bee, MindSearch...) -- consolidation expected by 2027.

---

## MCP: The Emerging Standard

The **Model Context Protocol** is consolidating the tool ecosystem:

| Before MCP | After MCP |
|-----------|-----------|
| M x N custom integrations | M + N universal connections |
| Vendor lock-in | Open standard |
| Fragmented security | Built-in consent model |
| No discovery | Standard registry |

**Timeline**: Anthropic (Nov 2024) --> OpenAI (Mar 2025) --> Google (Apr 2025) --> Linux Foundation (Dec 2025).

---

## Agent Memory: The Frontier

| Approach | Year | Key Innovation |
|----------|------|---------------|
| MemGPT | 2023 | OS-inspired paging |
| Graphiti | 2025 | Temporal graph with validity windows |
| AgeMem | 2026 | Memory as RL-trained tool use |
| H-MEM | 2026 | 4-layer cognitive architecture |
| Sleep-time compute | 2026 | Idle consolidation of memories |

**Trend**: from fixed heuristics to **learned, adaptive** memory behavior.

---

## Key Takeaways

1. **Four components**: brain, memory, planning, tools -- the universal agent blueprint
2. **ReAct** is the foundational loop: think, act, observe, repeat
3. **Architecture > model size**: agentic GPT-3.5 can outperform zero-shot GPT-4
4. **MCP** is the emerging universal standard for tool integration (97M monthly downloads)
5. **Start simple**: single agent with tools often beats complex multi-agent systems
6. **Memory is the frontier**: RL-trained memory management (AgeMem) and temporal graphs (Graphiti)
7. **Real applications exist**: Devin, Claude Code, KARMA demonstrate production agent value

---

## References

- Yao, S. et al. (2022). "ReAct: Synergizing Reasoning and Acting." ICLR.
- Ng, A. (2024). "Agentic Design Patterns." DeepLearning.AI.
- SuperAnnotate (2026). "LLM Agents: The Ultimate Guide."
- Anthropic (2024). "Model Context Protocol Specification."
- Databricks (2025). "Agent System Design Patterns."
- arXiv (2025). "Multi-Agent Collaboration Mechanisms Survey."
- arXiv (2026). "AgeMem: Unified Agentic Memory Framework."
- Packer, C. et al. (2023). "MemGPT: Towards LLMs as Operating Systems."
- EACL (2026). "H-MEM: Hierarchical Memory for LLM Agents."
