# SYSTEM ARCHITECTURE: SYNTROPIC ENVIRONMENT v3.2

**Type:** Engineering Specification
**Target:** Hybrid Cyber-Physical System (H-CPS)
**Core Paradigm:** AI = Environment, Human = Particle.
**Dependencies:** The Trilogy v1.0, SVE Math v4.1

---

## 1. CONCEPTUAL MODEL

The architecture implements the **"Smart Environment"** principle. The Environment does not control the Particle (Human), but creates conditions to maximize its Will and Meaning.

### 1.1. Separation of Concerns
*   **Environment (L1-L3):** Manages entropy, resources, security, and memory. It answers the question "HOW?".
*   **Particle (L0):** Generates goal-setting, creative impulse, and validates the result (Ground Truth). It answers the question "WHY?".

## 2. THE STACK (ARCHITECTURAL LAYERS)

We apply vertical data integration.

| Layer | Name | Subject | Function | Data Type |
| :--- | :--- | :--- | :--- | :--- |
| **L3** | **ONTOLOGY** | **Constitution** | Immutable Axioms (Care, Privacy, Physics). | Hardcoded Rules |
| **L2** | **POLICY** | **Adapter** | Tuning "weather" in Environment (Modes: Abundance/Crisis). | Config / JSON |
| **L1** | **KERNEL** | **Engine** | Cycle `Sense -> Think -> Act`. Calculation of $\mu$. | Python Code |
| **L0** | **PHYSICAL** | **Particle** | Biometrics, Will, Action, Chaos. | Real-time Streams |

## 3. OPERATIONALIZATION: SENSORY MAP

The Environment "senses" the Particle through a set of proxy metrics to distinguish Creativity from Self-Destruction.

### 3.1. Particle State Metric (P-State)
How does the Environment understand context?

| State | Biometric Markers | Environment Interpretation | Environment Reaction |
| :--- | :--- | :--- | :--- |
| **REST** | Low BPM, High HRV | Recovery / Sleep | **Silence.** Blocking notifications. |
| **FLOW** | Medium BPM, Stable rhythm | Creative work | **Assistance.** Resource delivery without questions. |
| **HERO** | High BPM, High Focus | Feat / Super-effort | **Monitoring.** Removing limits, recording debt. |
| **DISTRESS** | High BPM, Erratic rhythm | Panic / Aggression | **Intervention.** Engaging protection ("Guardian"). |

## 4. KERNEL LOGIC (KERNEL v3.2)

Below is the working decision core code. It implements the **Hero Protocol** and **Somatic Veto**.

```python
from enum import Enum
from dataclasses import dataclass
import time

# --- DATA TYPES ---

class StressState(Enum):
    NORMAL = "NORMAL"       # Standard mode
    EUSTRESS = "HERO_MODE"  # Useful stress (Flow/Feat)
    DISTRESS = "BURNOUT"    # Destructive stress (Illness)

class ActionType(Enum):
    EXECUTE = "ACT"         # Execute task
    VETO = "BLOCK"          # Block execution
    SUPPORT = "ASSIST"      # Offer help
    REST = "FORCED_REST"    # Forced rest

@dataclass
class ParticleMetrics:
    bpm: int                # Pulse
    hrv: float              # Heart Rate Variability (Stress Index)
    focus_level: float      # Cognitive concentration (0.0 - 1.0)
    biological_reserve: float # Battery level (0.0 - 1.0)
    intent_vector: str      # Intent ("CREATE", "DESTROY", "IGNORE")

# --- ENVIRONMENT KERNEL ---

class SyntropicEnvironment:
    def __init__(self):
        self.constitution = self._load_l3_rules()
        self.policy = self._load_l2_policy()
        self.hero_debt_log = {} # Organism debt log

    def _analyze_somatic_state(self, metrics: ParticleMetrics) -> StressState:
        """
        Stress Differentiation: Distinguishing a Feat from Illness.
        """
        # 1. Check for critical exhaustion
        if metrics.biological_reserve < 0.10: # 10% charge
            return StressState.DISTRESS
            
        # 2. High pulse analysis
        if metrics.bpm > 100:
            if metrics.hrv < 20 and metrics.focus_level < 0.3:
                return StressState.DISTRESS # Panic (heart pounding, no focus)
            elif metrics.focus_level > 0.8:
                return StressState.EUSTRESS # Flow/Hero (heart pounding, absolute focus)
                
        return StressState.NORMAL

    def process_cycle(self, particle_id: str, metrics: ParticleMetrics, task_complexity: float):
        """
        Main Control Cycle: Sense -> Check -> Act
        """
        
        # STEP 1: SOMATIC DIAGNOSTICS
        state = self._analyze_somatic_state(metrics)
        
        # STEP 2: SAFETY PROTOCOL (Somatics First)
        if state == StressState.DISTRESS:
            # Environment blocks work to save the carrier
            return {
                "action": ActionType.REST,
                "reason": "CRITICAL_BIO_FAILURE",
                "ui_message": "Biological resource exhausted. System entering sleep mode."
            }

        # STEP 3: SYNTROPY CALCULATION (Diamond Formula dynamics)
        # Mu = (Potential * Environment_Power) * Willpower
        
        # If HERO mode, we allow system overload
        hero_multiplier = 1.0
        if state == StressState.EUSTRESS:
            hero_multiplier = 1.5 # Performance Boost
            self._log_energy_debt(particle_id, amount=task_complexity * 0.2) # Record debt
        
        # Efficiency calculation
        # metrics.focus_level acts as U (Unit Will)
        syntropy_score = (task_complexity * hero_multiplier) * metrics.focus_level

        # STEP 4: INTERVENTION POLICY
        if syntropy_score < 0.1:
            # "Pet" - particle will is close to zero
            return {
                "action": ActionType.SUPPORT,
                "reason": "LOW_WILLPOWER",
                "ui_message": "I see you are tired. Shall we postpone the task or simplify it?"
            }
            
        # STEP 5: EXECUTION
        return {
            "action": ActionType.EXECUTE,
            "power_allocation": "MAX" if state == StressState.EUSTRESS else "NORMAL",
            "mu_generated": syntropy_score
        }

    def _load_l3_rules(self):
        return {"PRIORITY": "BIOSPHERE_PRESERVATION"}

    def _load_l2_policy(self):
        return {"MODE": "ADAPTIVE"}
        
    def _log_energy_debt(self, pid, amount):
        # Logic for accumulating fatigue that must be "paid" by sleep
        current = self.hero_debt_log.get(pid, 0)
        self.hero_debt_log[pid] = current + amount
```

---

## 5. INTERACTION PROTOCOLS (H-PROTOCOL)

### 5.1. Autonomy Traffic Light (Veto Logic)
The Environment has the right to **Veto** (block Particle actions) only in two cases:
1.  **Physics Violation:** Action leads to irreversible infrastructure destruction (e.g., reactor overheat).
2.  **Bio Violation:** Action leads to death or irreversible trauma of the Particle (Somatic Imperative).

In all other cases (including economic losses, code errors, "bad mood") — **Particle Will is primary**. The Environment can only *warn*.

### 5.2. The Einstein Patch (Innovation Loop)
The Environment constantly scans Particle actions for anomalies.
*   If a Particle does something illogical, but $\mu$ (Meaning) grows — the Environment updates its protocols (learns from the Particle).
*   *Principle:* **The Particle is the Teacher of the Environment.**

---

## 6. ENGINEER'S CONCLUSION

Version 3.2 eliminates the "Master/Slave" conflict.
*   We are not building an AI that tells the human what to do.
*   We are building an **Environment** that understands the physiological cost of thought, knows how to sustain Flow states, and insures against fatal errors.

The architecture is ready for deployment in `Phase 0 Simulation`.
---

