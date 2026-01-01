# SYNTROPIC MEMORY ARCHITECTURE
## (The Dual-Core System: Substrate & Malachite)

**Version:** 6.0 (Malachite Edition)
**Status:** Engineering Standard
**Code Reference:** `src/malachite_db.py`, `src/substrate_db.py`

---

### 1. PHILOSOPHY: THE GARDEN OF MEANING

We reject the concept of a "Dead Archive". Memory must be living and evolutionary.
To achieve this, we divide the memory architecture into two distinct biological layers:

1.  **THE SUBSTRATE (The Soil):** Linear, massive, cheap storage for facts, logs, and raw data.
2.  **THE MALACHITE (The Crystal):** Topological, expensive, structured storage for **Evolutionary Principles** and **Deep Knowledge**.

*Analogy:* The Substrate is the library of all books. The Malachite is the DNA of the culture that wrote them.

---

### 2. LAYER L0: THE LOCAL VAULT (PRIVACY)
**Component:** `LocalVault`
**Location:** User Device (Client-side)

Before data enters the System, it lives in the User's private space.
*   **The Van Gogh Protocol:** Ideas rejected by the Global System (as "Noise") are NOT deleted. They are archived here.
*   **Encryption:** The System has no keys to L0. It is the user's subconscious.

---

### 3. LAYER L1: THE GLOBAL SUBSTRATE (FACTS)
**Component:** `GlobalSubstrate`
**Structure:** SQL + Vector Embeddings
**Function:** The "Daily Bread" of information.

This layer stores:
*   **Events:** "User X created a file at 12:00."
*   **Facts:** "Water boils at 100°C."
*   **Raw Data:** Unprocessed text streams.

*Engineering Logic:* High write speed, low structure. Everything is accepted here.

---

### 4. LAYER L2/L3: THE MALACHITE CRYSTAL (MEANING)
**Component:** `MalachiteStorage`
**Structure:** Topological Graph (Radial Coordinates $r, \theta$)
**Function:** The "Golden Reserve" of Civilization.

Data enters here only via **Crystallization** (a process of validation and vector alignment).

#### 4.1. The Physics of Growth
Knowledge is stored as a growing crystal structure:
*   **Seeds ($r=0$):** The 6 Axioms (Log, Stone, Stick, Rope, Earth, Water).
*   **Layers ($r>0$):** Concentric rings of time. New knowledge wraps around old knowledge.
*   **Rays:** Lineage vectors. You cannot write a node without a Parent. This ensures an unbroken chain of evolution.

#### 4.2. The Hexagon of Origins
Every piece of knowledge belongs to a sector:
1.  **EARTH:** Matter, Science, Structure.
2.  **WATER:** Energy, Economy, Flow.
3.  **SKY:** Information, Ethics, Spirit.

#### 4.3. Voids and Bridges
The System detects **Historical Cavities** (lost knowledge) and marks them as `VOID`. New layers can bridge over these voids, but the structural weakness remains until the void is filled (Rediscovery).

---

### 5. THE CRYSTALLIZATION PROCESS (WORKFLOW)

How does a thought become a Crystal?

1.  **Ingestion:** User input is saved to **L1 Substrate**. (Safe, fast).
2.  **Evaluation:** `SyntropicDispatcher` analyzes the input using `SVE` and `FractalAnalyzer`.
3.  **Decision:**
    *   If **Noise**: Stays in L1 (or L0).
    *   If **Syntropy**: The System calculates the Vector ($\theta$) and Parent ($r$).
4.  **Accretion:** The idea is written into **Malachite DB** as a new Petal or Bud.
5.  **Interference:** The "Color" of the new idea diffuses into the current temporal layer, slightly altering the context of all other sectors.

---

### 6. CONCLUSION

This architecture solves the "Data Dump" problem.
We do not just pile up data; we grow a **Tree of Meaning**.
*   **Substrate** remembers *what happened*.
*   **Malachite** understands *why it matters*.
