# GSoC Project Proposal

---

## [Mesa-LLM iteration to push to production](https://github.com/mesa/mesa/wiki/GSoC-2026-Project-Ideas#mesa-llms-iteration-to-push-to-production)

**Prepared by:**\
Ilamaran Magesh

**Professional & Academic Details:**\
Applied ML Engineering and Data Professional\
MSc Computer Science\
University of Bristol, United Kingdom\
Expected Graduation: September 2026

**Contact Information:**<br>
[Email](mailto:ilamaran.magesh@gmail.com);
[Github](https://github.com/IlamaranMagesh);
[LinkedIn](https://www.linkedin.com/in/ilamaranmagesh)

---

<details>
<summary><h2>Contents</h2></summary>

[**Mesa-LLM iteration to push to
production**](#mesa-llm-iteration-to-push-to-production)

[**Abstract**](#abstract)

[**Motivation**](#motivation)

[**Scope**](#scope)

[**The Current Landscape**](#the-current-landscape)

[**Simple, Lovable, Complete**](#simple-lovable-complete)

[**User Journey, Epics & User
Stories**](#user-journey-epics-user-stories)

[**Technical Approach / Methodology**](#technical-approach-methodology)

[**Process Flow**](#process-flow)

[**Phase 1: Audit & Code Review**](#phase-1-audit-code-review)

[**Phase 2: Core Stabilisation and
Patching**](#phase-2-core-stabilisation-and-patching)

[**Epic 1: Concept & Setup (Simple
Experience)**](#epic-1-concept-setup-simple-experience)

[**User Story 1.1: Comprehensive Onboarding and
Documentation**](#user-story-1.1-comprehensive-onboarding-and-documentation)

[**User Story 1.2: Bulk Initialisation via
JSON**](#user-story-1.2-bulk-initialisation-via-json)

[**Epic 2: Architecting the \"Brains\" (Complete
Experience)**](#epic-2-architecting-the-brains-complete-experience)

[**User Story 2.1: Deterministic Agent Control (Hallucinations &
Guardrails)**](#user-story-2.1-deterministic-agent-control-hallucinations-guardrails)

[**User Story 2.2: Configurable Fallback
Systems**](#user-story-2.2-configurable-fallback-systems)

[**Epic 3: Observability and Admin Control (Lovable
Experience)**](#epic-3-observability-and-admin-control-lovable-experience)

[**User Story 3.1: Comprehensive Telemetry
Dashboard**](#user-story-3.1-comprehensive-telemetry-dashboard)

[**User Story 3.2: Smooth UI &
Performance**](#user-story-3.2-smooth-ui-performance)

[**Phase 4: Project Management and Developer
Experience**](#phase-4-project-management-and-developer-experience)

[**Project Management / Lifecycle**](#project-management-lifecycle)

[**Documentation**](#Documentation)

[**Deliverables**](#deliverables)

[**Project Timeline**](#project-timeline)

[**Personal Motivation**](#personal-motivation)

[**About Me**](#about-me)

[**Vision**](#vision)

[**Commitments & Availability**](#commitments-availability)

[**Contributions to Mesa**](#contributions-to-mesa)

[**AI & Tool Usage**](#ai--tool-usage)

[**References**](#references)
</details>

---

## Abstract

This proposal presents a structured **16-week plan** to transition
Mesa-LLM into a robust, production-ready framework. The roadmap is
organised into four key phases:

**Phase 1:** Conduct a comprehensive system audit and code review to
address technical debt and align the architecture with the upcoming Mesa
4.0 release.

**Phase 2:** Focus on core stabilisation and patching to resolve
critical defects that impact existing functionality.

**Phase 3:** Modernise the CI/CD pipeline alongside test-driven feature
development, introducing capabilities such as JSON-based bulk
initialisation, robust LLM fallback routing, and high-performance local
inference enabled by a Controller Registry pattern.

**Phase 4:** Enhance developer documentation, tutorials, and establish a
strategic release cadence aimed at delivering a stable Mesa-LLM 1.0
release in alignment with Mesa 4.0.

Ultimately, by leveraging advances in local model optimisation and
applying rigorous software engineering practices, this project aims to
position Mesa-LLM as a leading framework for simulating and analysing
complex, "conscious" agent ecosystems within computationally constrained
environments.

---

## Motivation

Generative AI has transformed paradigms across multiple domains, and
Agent-Based Modelling (ABM) is no exception. Mesa-LLM provides a strong
foundation for enabling AI-driven ABM, where AI serves as the "brains"
of agents, allowing researchers to observe complex emergent behaviours
that closely approximate real-world phenomena.

However, the current state of the Mesa-LLM project remains brittle and
requires significant refinement. Generative models, while highly
capable, are inherently unreliable when used in isolation, exhibiting
issues such as hallucinations and unpredictable edge cases. To fully
realise their potential, they must be integrated within systems that are
both controlled and deterministic, ensuring reliability while preserving
dynamic, *'alive'* behaviour. The proposal aims to resolve issues within
the project improving its reliability and stability, ultimately making
it production ready for the use of researchers and developers.

---

## Scope

The primary objective of this proposal is to transition **Mesa-LLM**
from its current **experimental** state into a **robust,
production-ready** extension. As of March 2026, while the foundation
exists, the framework lacks necessary qualities to be widely adopted by
academic and professionals of different domains.

### The Current Landscape

To move forward, we must acknowledge the current gaps:

**Completeness:** Though the framework has a very strong foundation,
many essential features for agent cognitive architectures are absent or
in-progress.

**Testing:** While basic unit tests exist, the framework lacks
comprehensive End-to-End (E2E) validation and coverage for complex
edge/corner cases (e.g., API failures, rate limiting, or malformed LLM
outputs).

**Stability:** Current bugs in the core logic prevent existing features
from being fully functional in high-stakes simulation environments.

### Simple, Lovable, Complete

The goal is to address the above and make the framework '**S**imple',
'**L**ovable', and '**C**omplete'\[1\]

**Simple** - The software should be '**Simple**' enough for the
researchers to not worry about 'how to implement?' or the process behind
the scenes.

**Lovable** - The software should have features that makes working with
it '**Lovable**' - should solve more problems than it creates, providing
intuitive interfaces, frictionless usage experience, and helpful
debugging tools. It should have detailed on-boarding guide, tutorials,
and API references.

**Complete** - The software should have baseline **completeness** - a
state where the software is functionally entire allowing a user to run a
full simulation without needing external workarounds, ensuring that any
**future capabilities** are perceived as **supplementary advancements**
rather than corrections to an unfinished core.

### User Journey, Epics & User Stories

As a software engineer and user of Mesa-LLM, I see clear use cases that the framework
should address which can benefit my research and similar other researchers.
So rather than just fixing bugs and adding features that makes
the framework 'cool', this proposal is built on **User Journeys.**

Given that my research/interest focuses on implementing AI-as-brains in
games, AI-driven Agent-Based Modelling (ABM) serves as a key tool for
prototyping. As an active user of **Mesa-LLM**, I have outlined my user
journey to inform this proposal. Based on this, I have identified a set
of epics and user stories, which are detailed in the [Methodology](#Technical-Approach-/-Methodology)
section. The complete list can be found [here](/My%20User%20Journey) for reference; while some items
may already exist within Mesa-LLM, they have been retained to ensure
alignment with the **Simple, Lovable,** and **Complete (SLC)**
principle.

Some questions that the proposal addresses -

- How -

  - \...reliable are the simulations?

  - \...I manage the model/agents?

  - \...is the framework fail-safe?

  - \...can I trust the agents are working as expected?

  - \...much complexity it adds compared to traditional frameworks?

- What -

  - \...makes it better than traditional ABM?

  - \...if I'm new to ABM?

  - \...are the best practices to model?

---

## Technical Approach / Methodology

To achieve a \"Production-Ready\" status, this proposal addresses
critical technical questions through a series of **Epics** and **User
Stories** with **SLC** in mind

>[!NOTE]
> **Note:** All the user stories are written from my perspective as a
user of Mesa-LLM. Features that make the software **SLC** according to
me.

### Process Flow

![](media/image1.png)

### Phase 1: Audit & Code Review

While the current codebase provides a robust foundation, a comprehensive
audit is essential to ensure alignment with the upcoming Mesa 4.0.0
architecture. The priority is to establish a high-quality baseline
rather than immediate feature growth. Technical debt in an experimental
codebase acts as a significant barrier to entry for open-source
contributors; therefore, auditing the system for necessary refactoring
early is a fundamental step toward long-term project sustainability. By
prioritising clean, maintainable code, we ensure the framework can scale
effectively without becoming a maintenance burden

```
"The only way to go fast is to go well."
- Robert C.Martin (Clean Code)
```

There are extensive ways to audit the code from documentation to risk
assessment but for the GSoC period, I aim to focus on the critical ones.

>[!NOTE]
> **Note:** Most of the processes mentioned here has already been started
from my side. By the official start of GSoC, I'd be able to provide
clear report of the code base. My findings are in this living document.

**Process:**

![](media/image2.png)

**Deliverables:** Analysis report will be provided by the first week of
the GSoC. This ensures that the next phase is performed aligning with
maintainers' vision and goals of the project.

If you want to skip the details on the process, you can move to the next
**[section (Phase 2)](#phase-2-core-stabilisation-and-patching)**

<a name=audit_process></a>
**Process Details:**

**1. Understanding Architectural Context (In-Progress)**

Questions answered:

- Are there tight couplings?<br>
- Are responsibilities clearly separated?<br>
- How's the control flow?<br>
- Architecture diagram reflecting the current state?<br>

**2. Static Code Analysis (To be started)**

Most of this can be done by the current tool used, Ruff but necessarily
need not to be in CI/CD

Analysis covered:

- Cyclomatic complexity - checks for complex, unmaintainable code<br>
- Code Duplication<br>
- Security issues - dependency vulnerabilities, memory leaks<br>

**3. Test Coverage (To be started)**

The current code base as of Mar 15, 2026 has good unit tests and code
coverage but that doesn't mean all features are tested, with
edge/corner cases and full feature (E2E) testing.

Questions answered & metrics covered:

- Unit tests with agreed upon coverage

- Integration tests for external APIs?

- Critical paths are tested?

- E2E tests

**4. Code Quality & Manual Review (In-Progress)**

Along with understanding the architecture, I'm currently manually
reviewing the code for readability, consistency, Mesa 4.0 compatibility,
docstrings, and code smells.

Questions / Topics answered:

- God classes and long methods

- Duplicate Logic

- Hidden side effects

- Poor naming convention

- Modularity

- Error Handling

- Mesa 4 compatible

**5. Performance & Scalability issues (In-Progress)**

Performance is the critical infrastructure challenge of any
LLM-integrated software. If agent reasoning cycles or simulation in the
UI become a bottleneck, the framework's utility for large-scale
simulations is compromised. It's better to measure areas for improvement
before optimising.

>[!NOTE]
> *Note:** These issues are considered to be resolved in the **Phase 3**

Questions / Topics answered:

- Profiling for non-agent features

- Areas for improvement by caching, efficient algorithms & data
  structures.

- Async operations work as intended?

- Concurrency in local model inference?

- UI performance

### Phase 2: Core Stabilisation and Patching

Following the initial audit, **Phase 2** focuses on stabilising the core
codebase through targeted patches. Findings from the **Phase 1** will be
detailed in a **System Health/Analysis Report**, and send to project
maintainers to collaboratively triage and prioritise critical fixes. By
establishing this alignment early, we ensure that the framework\'s
foundation is structurally sound before any new features are introduced
in Phase 3. This phase is scheduled for ***3 to 5 weeks (tent.)***, with
the exact duration dependent on the triage outcomes and the complexity
of the prioritised issues. See [project timeline](#project-timeline).

![](media/image3.png)

### Phase 3: CI/CD update and Feature Development

Upon stabilising the core in Phase 2, this phase is sub-divided into two
parts.

1. Focuses on fortifying the development pipeline to align with the
core Mesa release cadence.

2. Feature development.

**Part 1**

**First part of Phase 3 -** prioritises the modernisation of the
Mesa-LLM CI/CD infrastructure to meet industry standards. Currently, the
framework\'s automation does not fully cover the complexities of LLM
integrated systems.

<a name=ci_cd_update></a>
My work will focus on:

- **Deployment of Static Analysis:** Transitioning the existing mypy
  configuration into an active CI gate to ensure code quality and
  prevent runtime failures.\
  **Acceptance Criteria -** Activating **mypy** for strict type
  enforcement.


- **Expansion of Test Coverage:** Implementing a suite of integration
  tests that simulate real-world usage patterns, providing a safety net
  that unit tests alone cannot offer.\
  **Acceptance Criteria** **-** Deploy mocked **integration & E2E tests
  suite** for LLM-driven agent architectures.


- **[Documentation](#documentation):** Automating **Sphinx** validation
  builds to ensure that the \"face\" of the project stays in sync with
  the codebase.\
  **Acceptance Criteria** **-** Ensuring Sphinx build success on every
  pull request.


- **Security:** Hardening the repository through automated security
  scanning, mitigating risks associated with dependency vulnerabilities,
  and ensuring the framework\'s long-term integrity.\
  **Acceptance Criteria -** Integrating **CodeQL** and **Dependabot** to
  maintain a secure, production-standard codebase.

![](media/image4.png)

For the release cadence and milestones, see section **[Project
Management](#phase-4-project-management-and-developer-experience)**

**Part Two**

> [!NOTE]
> **Note** - I have prioritised some of the user stories that completes
the core functionalities of Mesa-LLM from my user journey. The user
stories listed have been intentionally defined at a broad level to
encompass the majority of Mesa-LLM's core functionalities, so It is
important to note that, subject to the maintainers' approval and overall
direction, not all proposed user stories may be included in the initial
release. And I intend to carry on with the work **beyond GSoC period**,
provided that the user stories align with the vision of the project.

**The second part of this phase**, focuses on the feature development.
Mesa-LLM has already most of it's basic features, yet it lacks critical
ones to have them sold.

```text
"If you can't ship it, it's not a product.\"\
- Paul Buchheit (Gmail)
```

All the approaches taken to solve the user stories are meant to make the
framework **Simple, Lovable,** & **Complete**

#### Epic 1: Concept & Setup (Simple Experience)

#####  User Story 1.1: Comprehensive Onboarding and Documentation 

- As a researcher , I want access to exhaustive documentation, a
  \"QuickStart\" guide, tutorials for every feature, and a comprehensive
  API reference.


- **Acceptance Criteria:** The documentation includes tutorials for
  every feature and showcases developer-recommended approaches with
  multiple creative strategies to tackle problems by showcasing
  different examples.

For more details on the docs, see section - [Documentation](#documentation)

##### **User Story 1.2: Bulk Initialisation via JSON**

> [!NOTE]
> **Note:** This feature is more aligned to mesa but if it's developed
for mesa-llm, it can be ported back.

- As a researcher, I want to feed the framework a single JSON
  configuration mapping out the agents.


- **Acceptance Criteria:** The framework intelligently parses the JSON
  to cluster static environmental property agents while naturally
  dispersing agents such that they don't overlap on top of other
  property agents. I can declare hundreds of agents without manual
  definition.

**High Level Architecture**

Core Modules -

- ConfigParser (Schema validation)

- AgentFactory (Instantiation)

- SpatialAllocator (The core allocation logic)

- AgentSetRegistry (Register the agents)

Figure 2: File Tree

![](media/image7.png)

![](media/image8.png)

#### **Epic 2: Architecting the \"Brains\" (Complete Experience)**

##### **User Story 2.1: Deterministic Agent Control (Hallucinations & Guardrails)** 

- As a researcher, I want agents to strictly follow system rules and
  agent-wise prompts.


- **Acceptance Criteria:** This actions remain deterministic,
  purpose-driven, and within boundaries without the need for careful
  prompt \"leashing\".

**Approaches (Discussion
[#174](https://github.com/mesa/mesa-llm/discussions/174)):**

There are multiple ways to enforce guardrails and avoid hallucinations,
I have listed some of the methods from industry standards to recent
researches

- Observation Masking by **JetBrains** for context management \[2\]

- **Knowledge graph + RAG** for long-term agent memory storage\
  (Having a hybrid memory storage is a key with short-term being a
  rolling buffer and long term stored in a graph data structure)

- **NeMo** Guardrails toolkit from Nvidia\
  (Industry standard for enforcing guardrails on off-topic detection and
  safety layers)

  <br>Cons:
<p style="padding-left: 40px;">
- Makes the framework heavy<br>
- Tight couple to a third-party tool<br>
- To customise, researchers should know, Colang, a domain specific language<br>
- Out of the box, this causes a problem of making the agents 'robotic'
  and doesn't mimic the real world model.<br>
</p>

I personally used an agent engine behind an AI-narrative game
development studio, **Meaning Machine**[4]. They specialise in
conscious NPCs in video games which are basically agents driven by AI
using a proprietary guardrail framework, Magpie. It brings flexibility
to the agents but also makes sure they don't deviate from their role and
forget their purpose. We can achieve similar kind of fluidity by "first
principle" approach of having pre/post generation guardrails to have the
framework lean and modular.

> [!NOTE]
> ***Note:** New research papers and approaches will be added to the list as I continue to
explore them.*

This is an essential feature to bring the Mesa-LLM production ready. How
it needs to be approached can be discussed with the maintainers and
align before the implementation.

##### **User Story 2.2: Configurable Fallback Systems** 

- As a researcher, I want the flexibility to set default fallback
  actions or a backup 'brain'.


- **Acceptance Criteria:** I can set a default fallback action for an
  agent when it fails to run a step, and set a backup 'brain' for when
  an agent's primary 'brain' stops working.

**Approaches:**

I have broadly classified the errors that can occur during response
generation into 2 categories,

- **API/LLM failure** - The agent tries to think, but the primary LLM is
  unavailable even after exponential back-off (e.g. an OpenAI API
  outage). The system should seamlessly route the prompt to a secondary
  LLM.


- **Agent failure** - The agent fails to execute a step entirely (e.g.
  both brains fail, or the LLM returns an unparsable hallucination). The
  system should execute a safe, deterministic default action (e.g. a
  non-LLM Agent) to keep the simulation running.

**High Level Architecture**
<p style="padding-left: 20px;">
A. The Backup 'Brain' (Composite Pattern)<br>
B. The Default Fallback Action (Agent Level)<br>
</p>

**A. The Backup 'Brain' (Composite Pattern)**

Instead of modifying the core **ModuleLLM** class to handle complex
retry logic, we can create a **FallbackBrain** that takes in the
standard **ModuleLLM** instance as secondary brain. The simulation
model (Mesa.Model) attempts the primary Brain (AI model) and, upon
catching an exception, routes to the backup.

This is incredibly useful for optimisation, the researchers could use
a heavy cloud model as the primary, and if rate-limited, fall back to
a local, quantised GGUF model running via Ollama to keep the
simulation moving without crashing. There are three level of fallback
stages to this design.

![](media/image9.png)

![](media/image10.png)

**Control Flow:**

- The **LLMagent** owns a **primary_brain** and, optionally, a
  **fallback_brain**. The primary brain does not know the fallback
  exists. This way the fallback system is kept modular.


- The **FallbackBrain** tracks failure counts. When the max_retries
  threshold is crossed, it actively intervenes in the agent\'s state by
  setting **agent.brain = None**.


- Once agent.brain is nullified, the agent bypasses the LLM generation
  step entirely in future ticks, relying purely on its fallback_action
  (a standard Python method or function) to interact with the Mesa grid.

**Sample code snippets**

**FallbackBrain Module**

![](media/image11.png)

This system is called inside the **LLMAgent** class, specifically in
`__init__subclass()` wrapper whenever the error is raised and it
triggers the fallback system.

**B. The Default Fallback Action (Agent Level)**

At the agent level, we need a mechanism to catch broader execution
failures during the **step()** function. We can introduce a
fallback_brain parameter to the **LLMAgent** class. This should call a
function or lambda that dictates what the agent does if all cognitive
processes fail.

**LLMAgent Module:**

![](media/image12.png)

The system is designed to **fail fast** in the absence of a configured
fallback. However, it can alternatively be implemented to default to a
**deterministic state** (e.g., a stale or inactive state) when no
fallback is defined. While the exact implementation may vary based on
design decisions, this captures the intended overall behaviour.

#### **Epic 3: Observability and Admin Control (Lovable Experience)**

##### **User Story 3.1: Comprehensive Telemetry Dashboard** 

- As a researcher, I want access to a native dashboard showing a
  real-time breakdown of token usage, average inference latency, and
  hardware utilisation.


- **Acceptance Criteria:** I can see real-time hardware, API/token
  usage, set RPM limits, and have admin control on the backend without
  breaking the simulation loop.

**Approach:**

I have detailed the approach in this **discussion
[#178](https://github.com/mesa/mesa-llm/issues/178#issue-4042295840)**

##### **User Story 3.2: Smooth UI & Performance** 

- As a researcher, I want the simulation and UI to feel smooth even with
  multiple agents. The only constraint should I feel is the hardware.


- **Acceptance Criteria:** The simulation runs without lag or
  stuttering. It runs thousands of steps without any problem.

The performance improvement can be made in two frontiers; **User
Interface** and **Agents Simulation.**

**User Interface**

Mesa-LLM inherits the current UI framework from the core Mesa library.
There is a significant opportunity to optimise how simulations are
rendered. But, I'll make it brief as this is an enhancement to be made
in Mesa not Mesa-LLM. Currently, UI performance in Mesa is limited by
the way visuals are generated; using plotting tools like Matplotlib to
swap images creates a \'choppy\' user experience. Since most models rely
on spatial coordinates rather than traditional functional plots
(y-axis), a real-time HTML Canvas implementation would be a more
efficient architecture. Visual simulation is key for ABM and
prioritising this is important as much as other core module.

I have approaches and ideas on how to improve the existing visual
simulation, some context here on
[Q&A](https://github.com/mesa/mesa/discussions/3517#discussion-9626385),
but provided the proposal is for Mesa-LLM, I'd like to focus on the
backend AI response generation performance for now.

**Agents Simulation (Local Inference)**

Optimisations in local inference is one of the highly researched areas.
There are new approaches and methods everyday but one method stands out
**RadixAttention**.

> [!NOTE]
> ***RadixAttention** - is a technique designed to optimise the Key-Value
(KV) caching mechanism in Large Language Model (LLM) serving. It
addresses the high memory and computational costs of serving LLMs by
automatically identifying and reusing common prefixes across multiple
requests, particularly in multi-turn conversations or prompts utilising
templates.*

**RadixAttention** is primarily developed as part of the **SGLang**
inference engine. The engine doesn't have a direct implementation using
LiteLLM however, it is possible to provide the support as both share
similar API protocol (OpenAI API).

**Why SGLang?**

Built for speed and multi-agent workflows. It uses **RadixAttention**,
which allows agents to share the same \"world state\" memory. If 100
agents all have the same system prompt, SGLang only computes that prompt
once. A devpost comparison
[here](https://dev.to/zkaria_gamal_3cddbbff21c8/concurrent-llm-serving-benchmarking-vllm-vs-sglang-vs-ollama-1cpn).\[3\]

**Process Flow**

![](media/image13.png)

This flow is very similar to other engines like **Ollama, vLLM**. By
leveraging model aliasing within the **LiteLLM config**, an additional
layer of abstraction is introduced, decoupling the agent\'s logic from
the underlying hardware. This is explicitly managed during **Step B** of
the defined process flow.

**Sample config for the router**

![](media/image14.png)

By providing an additional tier of abstraction, this setup ensures that
researchers can focus on high-level experimentation without the
operational overhead of managing engine-specific configurations. It also
allows for seamless transitions between different local and cloud-based
inference providers while maintaining a consistent interface for the
agents. This implementation also fulfils the requirements of [**User
Story 2.2**](#user-story-2.2-configurable-fallback-systems),
demonstrating a multi-engine architecture featuring automated fallback
capabilities.

**Implementation**

**Current Architecture**

![](media/image15.png)

Each **LLMAgent** instance instantiates a separate **ModuleLLM**,
despite identical configuration across agents. Consequently, every
**ModuleLLM** establishes its own HTTP connection to the server,
introducing unnecessary overhead and negatively impacting overall
performance.

**Proposed Architecture (Controller Registry Pattern)**

**Sample code snippets**

![](media/image17.png)

LiteLLM provides robust support on the backend routing via **router**
API.

![](media/image18.png)

By relocating the instantiation of **ModuleLLM** from **LLMAgent** to
the **Mesa.Model** class, simulation-level instances of **ModuleLLM**
can be created. This enables agents with identical configurations to
share a common router instance, thereby significantly reducing overhead
and improving performance.

Below comparison provides a simple view of the different architectures
from current to proposed

  -----------------------------------------------------------------------
  ![](media/image19.png)             ![](media/image20.png)
  ---------------------------------- ------------------------------------

  -----------------------------------------------------------------------

### **Phase 4: Project Management and Developer Experience**

This final phase focuses on the documentations and release
cadences/lifecyle of Mesa-LLM.

#### **Project Management / Lifecycle**

This is comparison on the releases between Mesa and Mesa-LLM

| **Aspect**               | **Mesa**                      | **Mesa-LLM**                  |
|--------------------------|-------------------------------|-------------------------------|
| **Stability**            | Stable                        | Active Development            |
| **Current Version**      | v3.5.1 → v4.0.0a0             | v0.3.0                        |
| **Pre-release Cycle**    | Yes (alpha → beta → RC)       | No (direct releases)          |
| **Maintenance Strategy** | Multiple maintenance branches | Single main branch            |
| **Breaking Changes**     | Only in major releases        | More frequent (0.x phase)     |
| **Deprecation Period**   | ≥1 minor release              | N/A (early stage)             |
| **Release Notes**        | Comprehensive with categories | Detailed changelog generation |


Based on the release cycle of Mesa 3.0, which had a **pre-release
phase** of approximately **four months**, and considering that the
**v4.0 alpha0** was released around **mid-March 2026**, it is reasonable
to anticipate a stable 4.0 release by July or August 2026, coinciding
with the conclusion of the GSoC period. Assuming that Mesa-LLM reaches
production readiness with its core features implemented and major issues
resolved, aligning its first stable release with or within a month of
the Mesa 4.0 release presents a highly strategic opportunity.

With all the considerations and assumptions in mind, I propose the
following plan for the first stable release of Mesa-LLM, along with a
release cadence that aligns closely with Mesa Core.

![](media/image21.png)

Since Mesa serves as the foundation for Mesa-LLM, it is best to align
Mesa-LLM release cadence closely with that of Mesa, allowing for a
buffer of a few weeks. This buffer accounts for ongoing contributions
and integration efforts, although the ideal scenario would be to have
releases on the same day.

Given the limited development window for Mesa-LLM, priority should be
placed on **stability** and the implementation of only **high-impact
features**. It is important to note that, based on the maintainers'
approval and vision, not all of the proposed user stories may be
implemented for the first release. The proposal is intentionally kept
broad aiming to cover most of the core functionalities of Mesa-LLM.

---

## **Documentation**

The current documentation includes all the essential sections expected
of a Python framework; however, the tutorials and getting-started guides
lack clarity and, as of mid-March 2026, are not fully aligned with
recent framework updates.

The following improvements are proposed:

- Enhance tutorials by:

  - Introducing interactive, live tutorials via Google Colab integration

  - Adding visual architecture diagrams and logic flow representations
    of Mesa-LLM

- Conduct a comprehensive review of the documentation to address
  typographical errors, inconsistencies, and clarity issues

- Introduce a dedicated Best Practices / Developer Recommendations
  section, covering:

  - Prompt engineering patterns

  - Cost and latency optimisation strategies

- Add a "What is ABM?" section which provides resources and guides to
  understand ABM that can also be integrated into Mesa's core
  documentation

- Provide a detailed contribution workflow, including clear guidelines
  for pull request (PR) triage and review processes

---

## **Deliverables**

> [!NOTE]
> **Note:** Final implementations are subjected to maintainers' approval
and alignment during the community bonding period of the GSoC program.

This section contains all the listed deliverable across **Phase 1**
through **Phase 4** along with the corresponding criteria used for
defining their completion.


| **Phases** | **Criteria of completion** |
|------------|----------------------------|
| **1: Audit & Code Review** | A formal **System Health Analysis report** provided by the end of Week 1 of the GSoC period to the maintainers. |
| **2: Core Stabilisation & Patching** | **Issues and bugs** listed in the analysis report are **addressed** in alignment with the maintainers.<br><br>Some actionable items (not limited to) are detailed [here](#audit_process). |
| **3: CI/CD updation & Feature Development** | **[0.1.](#ci_cd_details)** Static analysis CI gate, integration & E2E test coverage, automated documentation validation, and security hardening.<br><br>**1.1. Published & refined** full-feature tutorials, and developer best practices with creative problem-solving examples.<br><br>**1.2.** Functional **JSON-driven agent initialisation**, SpatialAllocator clustering & non-overlap logic, and tested core modules.<br><br>**2.1.** Agents enforce strict role adherence with a **lightweight guardrail framework** (pre/post-generation checks) to prevent **hallucinations and drift.**<br><br>**2.2. Robust LLM/API fallback routing** (Composite Pattern with retry + backup model) and deterministic agent fallback actions ensuring simulation stability.<br><br>**3.1.** Real-time native **telemetry dashboard** displaying token usage, latency, hardware metrics, and supporting RPM limits without interrupting the simulation loop.<br><br>**3.2.** High-performance execution with **Controller Registry Pattern** (shared ModuleLLM at Model level), reduced HTTP overhead, and advanced caching compatibility (RadixAttention / prefix caching). |
| **4: Project Management & Developer Experience** | **1.** Release alignment with Mesa, with Mesa-LLM stable release within 1-month buffer of Mesa 4.0 (July/August 2026).<br><br>**2.** Completed codebase/documentation audit, published Best Practices (prompt engineering, cost/latency), added ABM introduction, and defined contributor workflow with PR triage. |

---

## **Project Timeline**

According to the GSoC timeline, the official coding period runs from
**May 1, 2026 to August 24, 2026**, spanning a total of approximately
**16 weeks and 3 days**. As a master's student, I plan to contribute on
a part-time basis, dedicating 20 hours per week, resulting in an
estimated total effort of about **350 hours**.

The project timeline has been structured accordingly, with approximate
allocations of time and effort across phases. Additionally, a buffer of
one week has been kept for each phase, so the phases overlap for a week
to ensure flexibility and continuity.

Each Phases are allocated **tentative hours** based on the deliverables.

| **Phase**                     | **Duration**                  |
|-------------------------------|-------------------------------|
| Phase 1 - Audit & Code Review | Weeks: ~1–2<br>Hours: 20–40   |
| Phase 2 - Core Stabilisation  | Weeks: ~3–5<br>Hours: 60–100  |
| Phase 3 - CI/CD & Feature Dev | Weeks: ~6–7<br>Hours: 120–140 |
| Phase 4 - Project Mgmt & Docs | Weeks: ~1–2<br>Hours: 20–40   |

![](media/image22.png)

---

## **Personal Motivation**

My personal interest towards ABM stems from my current research focus on
the application of AI in games, particularly in areas such as **autonomous
NPC behaviour**, **game world creation**, and **dynamic world updates**. Because
of the power-hungry nature of AI models, my work extends deeply into
space and performance optimisation, specifically focusing on model
quantisation. My goal is to fit these models efficiently on-device while
preserving the intelligence required for these complex NPC interactions.
To say it in short, my two primary interests and works are
implementation of AI game systems and the technical optimisation and
quantisation of models for local, high-performance game environments.

As a reason, AI-driven NPCs still remain in an early stage of
development, with complex emergent behaviours not yet fully understood -
developing experimental prototypes is a necessary first step. This
motivated me to explore **AI-driven ABM** approaches and techniques for
implementing more autonomous, "conscious" NPCs.

This exploration led me to **Mesa** and **Mesa-LLM**. Given that
**Mesa-LLM** is currently in an experimental phase, it presents a
valuable opportunity to contribute to its growth and evolution. This
also aligns well with my research needs, as I require a robust tool for
modelling and simulation. Within the Python ecosystem, I did not
identify other ABM frameworks with a similarly mature foundation as
Mesa, making Mesa-LLM a particularly strong candidate for advancing
AI-driven ABM. Though there are other AI-Agent orchestration tools like
**LangGraph**, and **CrewAI**, they are primarily meant to be for
agentic AI workflows and typically requires building most of the agent
environment from scratch.

As a coincidence, while planning to apply for the GSoC to make
productive use of my summer during my master's programme, I found that
Mesa is a participating organisation.

This is one of the moments where one might say,

```text
"The threads of fate have finally begun to intertwine."
- Igor, Persona 5
```

And regardless of my GSoC, I'd still intend to contribute to the project
as it is directly supports my ongoing work in modelling and
simulation.[]{.mark}

## **About Me**

I am currently pursuing a Master of Science in Computer Science at the
University of Bristol, United Kingdom, and expect to graduate in
September 2026. I have practical experience in AI/ML engineering, data
science, and data engineering.

From June 2026, I will be undertaking my thesis, which focuses on
developing a fully local AI assistant powered by on-device models,
capable of processing and retaining documents, meeting notes, and other
contextual information within local memory. Given that my research
centers on AI agents in games and system optimisation, this work will
provide valuable expertise in local model optimisation - an area
directly relevant to the core challenges need to be addressed in
Mesa-LLM.

In addition to my academic work, I have completed several relevant
personal projects. Notably, I implemented the Word2Vec CBOW model using
only NumPy, demonstrating a strong foundation in first-principles
thinking and a deep understanding of underlying concepts. Another key
project involves a 3D simulation built using WebGL, where my experience
with HTML5 Canvas, front-end development, and rendering techniques can
contribute to optimising agent simulations within Mesa.

---

## **Vision**

My vision of Mesa-LLM is rooted in the belief that the next frontier of
ABM lies in the accessible, efficient integration of AI models within
complex simulation environments. Researchers and developers shouldn't
feel any friction on-boarding and using Mesa-LLM.

**In the short term**, my goal for this GSoC project is to drive
Mesa-LLM toward core stabilisation and production readiness. Mesa offers
a uniquely mature foundation for true environmental simulation. By
leveraging my background in first-principles machine learning and local
model optimisation, I aim to refine Mesa-LLM so that researchers can
seamlessly simulate complex, LLM-driven agent interactions such as
memory retention and context-sharing without prohibitive computational
overhead. Bridging this gap will make Mesa-LLM a robust, immediate asset
for researchers requiring highly optimised, on-device modelling tools.

**In the long term**, I envision Mesa-LLM evolving into the definitive
framework for studying emergent, \"conscious\" agent behaviours in
computationally constrained environments. Drawing from my ongoing
research into autonomous game NPCs and model quantisation, I aim to push
Mesa-LLM beyond just running few tens or hundreds of agents, enabling it
to scale efficiently to thousands by staying aligned with emerging
research and applying robust software engineering practices. By
facilitating complex multi-agent ecosystems to run natively and
efficiently, we can empower the broader research, data science, and
broader communities to build, observe, and interact with dynamic
AI-driven models, fundamentally expanding the scope of ABM to wider
range of industries and applications.

---

## **Commitments & Availability**

I am committed to contributing to the Mesa community **beyond the GSoC**
period. Regardless of whether I pursue a career in research or industry,
I intend to continue exploring and developing AI-driven game systems as
personal projects, and therefore aim to provide sustained, **long-term
contributions** to the project.

During the GSoC period, I will be available on a **part-time** basis,
with an estimated commitment of approximately **350 hours** over the
duration of the programme.

---

## **Contributions to Mesa**

- My introduction --
  [mesa#2465](https://github.com/mesa/mesa/discussions/2465#discussioncomment-15938927)

- My learning space - [mesa-learning-space](https://github.com/IlamaranMagesh/mesa-learning-space)

- My GSoC repo - [GSoC-26-Mesa-LLM](https://github.com/IlamaranMagesh/GSoC-26-Mesa-LLM)

- My forks - [Mesa](https://github.com/IlamaranMagesh/mesa-fork) and [Mesa-LLM](https://github.com/IlamaranMagesh/mesa-llm-fork)

- Issue - [mesa#3516](https://github.com/mesa/mesa/issues/3516)
  (merged)

- Issue - [mesa-llm#172](https://github.com/mesa/mesa-llm/issues/172)
  (open)

- Issue - [mesa-llm#177](https://github.com/mesa/mesa-llm/issues/173)
  (open)

- Issue - [mesa-llm#178](https://github.com/mesa/mesa-llm/issues/178)
  (open)

- Issue - [mesa-llm#218](https://github.com/mesa/mesa-llm/issues/218)
  (open)

- PR - [mesa-llm#177](https://github.com/mesa/mesa-llm/pull/177) (open)

- Q/A - [mesa#3517](https://github.com/mesa/mesa/discussions/3517)
  (answered)

- Discussion -
  [mesa#3402](https://github.com/mesa/mesa/discussions/3402)
  (Proofreading and polishing docs)

- Discussion -
  [mesa-llm#219](https://github.com/mesa/mesa-llm/discussions/219)
  (`recording` module bug)

- Discussion -
  [mesa-llm#174](https://github.com/mesa/mesa-llm/discussions/174)
  (Model hallucinations & guardrails)

> [!NOTE]
> **Note:** I will be updating the list with new contributions as I continue to contribute to the project.

---

## AI & Tool Usage

The following are the areas where AI has been used in this proposal:

- **Documentation:** I wrote the contents of the documentation and
I used Gemini, and ChatGPT to rephrase and enhance the language with the context unchanged.
- **Code:** I wrote the code snippet templates and I used Gemini to add fillers and docstrings.
- **Mermaid Diagrams:** I designed the architecture diagrams. I used Gemini, and ChatGPT to write bolierplates for
Mermaid code and I customised on top of that.
- **Other Charts:** I used [draw.io](https://www.drawio.com) and [Lucidspark](https://lucid.co/lucidspark) to
create the charts. No AI was used in the tools.
- **Learning & Ideation:** I used Gemini only to research and learn concepts, best-practices, and industry approaches
for the project. AI was not used to design the strategies or the architectures proposed.
- **Prototyping:** I used GitHub Copilot to generate a mockup prototype of my design in my forks of the project.

---

## **References**

[1] A software engineering principle, **SLC**, I follow was introduced
to me by an experienced professional named Steve, who brings over 50
years of experience in the field. **SLC** - Any kind of software should
be **Simple**, **Lovable** and **Complete**

[2] JetBrains research -
<https://blog.jetbrains.com/research/2025/12/efficient-context-management>

[3] Devpost comparing performance of local inference engines -
<https://dev.to/zkaria_gamal_3cddbbff21c8/concurrent-llm-serving-benchmarking-vllm-vs-sglang-vs-ollama-1cpn>

[4] Meaning Machine Game Studio - <https://www.meaningmachine.games>
