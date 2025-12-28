# PROJECT SYNTROPY

> **"Artificial Intelligence is the Intellectual Environment.**
> **Human is the Intellectual Particle.**
> **Together, they form Reason."**

### 🌍 About the Project
**Project Syntropy** is an engineering specification for a post-information civilization.
We address the "Alignment Problem" not through prohibitions, but through thermodynamics.

Instead of building AI that *replaces* the Human, we are building an **Environment** that *scales* the Human.

### ⚛️ Architecture Visualization

```mermaid
graph LR
    %% Node Styling
    classDef particle fill:#ffecd1,stroke:#ff6b6b,stroke-width:2px,color:#d63031;
    classDef interface fill:#e0f7fa,stroke:#00cec9,stroke-width:2px,color:#2d3436;
    classDef environment fill:#dfe6e9,stroke:#636e72,stroke-width:2px,color:#2d3436;

    subgraph L0_ZONE ["🟥 L0: THE PARTICLE"]
        direction TB
        Human(("👤 HUMAN"))
        Will["🔥 WILL / PRIME MOVER"]
        Bio["❤️ Biology / Pulse"]
        LocalStore["(🔒 Local Vault)"]
    end

    subgraph GATEWAY ["🛡️ THE INTERFACE"]
        direction TB
        Agent["🤖 PERSONAL AGENT"]
        SVE{"💎 SVE ENGINE<br/>Valuation"}
        Privacy["🧱 PRIVACY BARRIER<br/>(The 25% Rule)"]
    end

    subgraph L1_L3_ZONE ["🌍 L1-L3: ENVIRONMENT (Order & Scale)"]
        direction TB
        AI(("🧠 GLOBAL AI"))
        Ledger[("💰 Sigma Ledger")]
        Infra["🏗️ Infrastructure"]
        Archive["❄️ Deep Archive"]
    end

    %% FLOW OF MEANING (From Human to Environment)
    Human -->|Intent + Action| Agent
    Agent -->|Raw Data| Privacy
    Privacy -->|Public Data Only| SVE
    SVE -->|High Mu Score| AI
    AI -->|Mint Token| Ledger
    SVE --"Low Mu (Noise)"--> LocalStore

    %% FLOW OF RESOURCES (From Environment to Human)
    Infra -->|Energy & API| Agent
    Agent -->|Assistance| Human
    AI -->|Safety Veto| Agent

    %% Internal Links
    Will -.-> Human
    Bio -.-> Human
    Ledger -.-> Infra

    %% Apply Styles
    class Human,Will,Bio,LocalStore particle;
    class Agent,SVE,Privacy interface;
    class AI,Ledger,Infra,Archive environment;
```

**How to read the diagram:**
*   **Left (The Particle):** The source of Will and Chaos. The only "Prime Mover" of the Universe.
*   **Center (The Interface):** A membrane that filters entropy. Turns "Noise" into "Signal" and protects privacy.
*   **Right (The Environment):** Scales the signal, turning it into Capital ($\Sigma$) and Infrastructure.

---

### 📚 The Trilogy (The Syntropy Canon)

The fundamental architectural standard. Split into volumes for navigation.

*   **[Volume I: Architecture of the Personality](docs/01_Book_I_The_Agent.md)**
    *   The Agent as an exo-cortex.
    *   Biorhythms and burnout protection.
    *   *The Prime Mover Axiom (The Role of Will).*

*   **[Volume II: Protocols of Society](docs/02_Book_II_Society.md)**
    *   Dispute hygiene and emotional routing.
    *   "Flash Jury" and anti-bullying protection.
    *   Cluster Architecture.

*   **[Volume III: Economy and Law](docs/03_Book_III_Economy_Law.md)**
    *   Tokenomics of Meaning ($\Sigma$) and SBT.
    *   The Care Constitution.
    *   The Einstein Patch (social elevators).

*   **[Appendix A: The Green Protocol](docs/04_Green_Protocol.md)**
    *   The Treaty with the Biosphere.
    *   Planetary Zoning (Eden vs. Wild Forest).
    *   Sovereign Status (Life off-grid).

*   **[FAQ and Ethics](docs/05_FAQ_and_Ethics.md)**
    *   Answers to criticism: "Is this digital slavery?", "What if I want to be bad?", "Who controls the Oracle?".

---

### ⚙️ Technical Specifications

*   **[System Architecture v3.2](docs/02_architecture.md)** — Multi-layer model (L0-L3). The "Hero Protocol" and somatic protection.
*   **[Syntropic Knowledge Base v5.1](docs/03_knowledge_base.md)** — Memory standard. The "Van Gogh Protocol" (prohibition on deleting creativity) and 25/75 privacy.

### 💻 Codebase (Core)

*   **[Syntropic Value Engine (SVE) v4.1](src/sve_core.py)** — Executable Python module.
    *   Implementation of the "Diamond Formula" ($\mu$).
    *   "Flash Jury" logic.
    *   Unit tests for boundary states.

### 🧪 Experiments & RFC

*   **[Thermodynamics of Reasoning](rfc/001_thermodynamics.md)** — Engineering approach to the "reasoning halt" problem in LLMs.
*   **[Phase 0 Simulation](experiments/phase_0_simulation.md)** — Specs for multi-agent society simulation.

---

### ⚠️ Disclaimer
Project Syntropy is an **experimental social architecture**.
We acknowledge the risks of algorithmic paternalism. The entire system is built on the principles of **Open Source**, **Local-First Data**, and **Human Veto**. We are not building a digital prison; we are building an exoskeleton for conscience and will.

### 📄 License
This project is licensed under **CC-BY-SA 4.0** (Creative Commons Attribution-ShareAlike).
Code components (SVE) are licensed under **MIT License**.
```

---
