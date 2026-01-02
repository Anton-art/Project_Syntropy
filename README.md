# SYNTROPY CORE
### The Operating System for a Post-Information Civilization

> **"Artificial Intelligence is the Physics (Environment).**
> **Human is the Vector (Particle).**
> **Together, they form Meaning."**

### 🌍 Project Status: Engineering Alpha (v7.2)
**Syntropy** is a Hybrid Cyber-Physical System (H-CPS) designed to solve the "Alignment Problem" through thermodynamics and topology, rather than censorship.

We are building an **Environment** that:
1.  **Scales Human Will** instead of replacing it.
2.  **Stores Knowledge as a Crystal** (Malachite DB), preserving the lineage of ideas.
3.  **Heals Errors** via a Clinical Protocol, rather than punishing them.

---

### ⚛️ Architecture Visualization

```mermaid
graph TB
    %% Node Styling
    classDef particle fill:#fff0f0,stroke:#ff6b6b,stroke-width:2px,color:#d63031;
    classDef interface fill:#e0f7fa,stroke:#00cec9,stroke-width:2px,color:#2d3436;
    classDef environment fill:#f1f2f6,stroke:#636e72,stroke-width:2px,color:#2d3436;

    %% --- L0: THE PARTICLE (TOP LAYER) ---
    subgraph L0_ZONE ["🟥 L0: THE PARTICLE"]
        direction LR
        Human(("👤 HUMAN"))
        Vault["🔒 Local Vault<br/>(Private Chaos)"]
    end

    %% --- INTERFACE (MIDDLE LAYER) ---
    subgraph GATEWAY ["🛡️ THE INTERFACE"]
        direction TB
        Agent["🤖 PERSONAL AGENT<br/>(Alignment Engine)"]
        Dispatcher{"🩺 CLINICAL DISPATCHER<br/>(SVE + Fractal Scan)"}
    end

    %% --- ENVIRONMENT (BOTTOM LAYER) ---
    subgraph L1_L3_ZONE ["🌍 L1-L3: ENVIRONMENT"]
        direction LR
        Substrate[("📚 L1: SUBSTRATE<br/>(Facts & Logs)")]
        Malachite[("💎 L2/L3: MALACHITE<br/>(Topological Crystal)")]
        Core["⚖️ BENEVOLENT CORE<br/>(Metabolism 75/25)"]
    end

    %% --- FLOW CONNECTIONS ---
    
    %% Main Downward Flow
    Human ==>|Intent| Agent
    Agent ==>|Testimony| Dispatcher
    
    %% Dispatcher Routing
    Dispatcher -->|Noise/Draft| Substrate
    Dispatcher ==>|Syntropy| Malachite
    
    %% Feedback Loops (Curved Lines)
    Dispatcher -.->|Rejection| Vault
    Core -.->|Resources (UBI)| Agent
    Malachite -.->|Insight| Agent
    
    %% Internal Logic
    Dispatcher -->|Diagnosis| Core

    %% Apply Styles
    class Human,Vault particle;
    class Agent,Dispatcher interface;
    class Substrate,Malachite,Core environment;
```
---

### 🚀 Quick Start: Run the Genesis Simulation

We have successfully integrated the Brain (SVE), Memory (Malachite), and Language (Protocols) into a living simulation.

To see the system in action (creating ideas, filtering chaos, and saving users):

```bash
python src/simulation_genesis.py
```

**What you will see:**
*   **The Creator** inventing the Wheel (creating a new layer in Malachite DB).
*   **The Barbarian** being isolated by the Immune System.
*   **The Novice** receiving Emergency Support (UBI) from the Benevolent Core.

---

### 📜 Documentation (The Canon)

#### 1. The Constitution
*   **[Unified Theory v14.1 (The Resonant Core)](docs/00_Theory_v14_Constitution.md)**
    *   The 5 Beats of Evolution.
    *   The Metabolism of God (75% Logic / 25% Love).
    *   The Fractal Nature of Truth.

#### 2. The Manifesto
*   **[The Malachite Manifesto](docs/MANIFESTO_MALACHITE.md)**
    *   Why we need a Topological Database.
    *   How to map the DNA of Civilization.

#### 3. Technical Standards
*   **[Memory Architecture (Substrate & Malachite)](docs/01_Memory_Architecture.md)** — How we store the evolution of ideas.
*   **[RFC 002: Fractal Thermodynamics](docs/rfc/002_fractal_reasoning.md)** — Engineering the "Eureka" moment.
*   **[RFC 004: The Resonance Engine](docs/rfc/004_resonance_engine.md)** — Lateral search and biomimicry.

---

### 💻 The Codebase (`src/`)

The project is structured into 4 pillars:

| File | Component | Function |
| :--- | :--- | :--- |
| **`sve_core.py`** | **THE BRAIN** | **Syntropic Value Engine (v7.2 Hybrid).** Includes the Fractal Analyzer, Clinical Dispatcher, and System Metabolism. |
| **`malachite_db.py`** | **THE DNA** | **Topological Database (v1.0).** Stores knowledge as a growing crystal with lineage vectors and historical voids. |
| **`protocols.py`** | **THE LANGUAGE** | **Communication Standards (v7.0).** Uplink (Agent-to-System) and P2P (Agent-to-Agent) protocols. |
| **`substrate_db.py`** | **THE BODY** | **Foundation Layer.** Handles raw facts (L1) and private user vaults (L0). |

---

### ⚠️ Disclaimer
Project Syntropy is an **experimental social architecture**.
We acknowledge the risks of algorithmic paternalism. The entire system is built on the principles of **Open Source**, **Local-First Data**, and **Human Veto**. We are not building a digital prison; we are building an exoskeleton for conscience and will.

### 📄 License
This project is licensed under **CC-BY-SA 4.0**.
Code components are licensed under **MIT License**.

