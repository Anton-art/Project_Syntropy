# SYNTROPIC LEDGER & MEMORY (SKB v5.1)

**Type:** Architecture Specification
**Component:** L2/L3 Memory Subsystem
**Dependencies:** SVE Math v4.1, The Trilogy (Book III)
**Core Paradigm:** Data = Asset. Memory = Bank.

---

## 1. PHILOSOPHY: FROM CACHE TO CAPITAL

In the **"Environment — Particle"** paradigm, memory performs two functions:
1.  **For Particle:** A mirror of personality and a private safe.
2.  **For Environment:** A "Gene Pool Library" (storage of useful mutations).

We reject the idea of "eternal storage of everything". We introduce the concept of **Thermodynamic Value of Data**.
*   Garbage (Entropy) must burn.
*   Meaning (Syntropy) must crystallize into Reputation (SBT).

## 2. STORAGE TIERS

The system implements physical data separation according to the **25/75 Rule** (Privacy/Publicity).

### **L0: LOCAL VAULT (Private Zone — 25%)**
*   **Content:** Particle's "Personal Chaos". Drafts, doubts, private messages, biometrics, raw thoughts.
*   **Access:** Particle ONLY. The Environment (Global AI) **has no encryption keys**.
*   **Function:** Sandbox for mutations. Here, things are born that are not yet ready for Validation.
*   **Tech:** Encrypted Local Storage (Device-side vector DB).

### **L1: PLASMA (Operational Context)**
*   **Content:** Active dialogues, current tasks.
*   **Access:** Environment + Particle.
*   **TTL (Time To Live):** Short (Sessions). Cleared after sleep phase/reboot if not moved to L2.

### **L2: CRYSTAL (Gold Reserve — 75%)**
*   **Content:** Validated Meaning.
    *   **Zone A (Assets):** Working algorithms, finished works, verified facts.
    *   **Zone B (Potential):** "Sleeping" genius ideas ($\alpha=0$), awaiting resources.
*   **Economy Link:** Entry of a file into L2 automatically triggers **Minting SBT** (reputation accrual to the Particle).
*   **Tech:** Vector DB (Weaviate/Qdrant) + IPFS/Blockchain Links.

### **L3: DEEP FREEZE (Archive & Black Log)**
*   **Content:**
    *   Raw experiment data.
    *   **The Van Gogh Archive:** Unrecognized ideas.
    *   **Black Log:** Registry of errors and dead-end branches (negative Syntropy). Stored forever as the Environment's "immune memory".

## 3. ALGORITHM: DUAL INDEXING

The Environment uses two independent scales for data management.

#### **3.1. Temperature ($T$) — Demand Index**
*   *Question:* Is this needed right now?
*   *Impacts:* Caching (Hot vs Cold storage).
*   *Formula:* $T = (Access\_Freq \times w_1) - Decay$.

#### **3.2. Syntropy ($\mu$) — Value Index**
*   *Question:* Is this truth/utility?
*   *Impacts:* **Retention** and **Reward (SBT)**.
*   *Link:* An object can be "Cold" (no one reads a 19th-century treatise) but have extremely high $\mu$ (Meaning). The Environment **never** deletes objects with high $\mu$, even if $T \to 0$.

## 4. DATA SCHEMA (v5.0)

JSON structure of a "Syntropic Asset". Implements binding to owner (DID) and proof of value.

```jsonc
{
  "asset_id": "uuid-v4-hash",
  "owner_did": "did:syntropy:particle_x892...", // Owner (Particle)
  "storage_layer": "L2_CRYSTAL",
  
  // 1. ACCESS CONTROL (Privacy Protocol)
  "access_policy": {
    "visibility": "PUBLIC", // PUBLIC | CLUSTER | PRIVATE
    "encryption": "NONE",   // For L2/Public content
    "license": "CC-BY-SYNTROPY"
  },

  // 2. VALUE EVALUATION (Diamond Formula Result)
  "valuation": {
    "mu_score": 0.95,       // Final Meaning Score
    "components": {
        "compression_ratio": 0.85, // Insight (L_code / L_data)
        "vitality_index": 0.98,    // 3:1 Balance
        "power_efficiency": 1.2    // P / E
    },
    "status": "ASSET",      // ASSET (Working) or POTENTIAL (Idea)
    "last_audit": 1715000000
  },

  // 3. ECONOMIC FOOTPRINT (SBT)
  "ledger_record": {
    "minted": true,
    "token_id": "sbt-block-7721",
    "value_locked": 95.0,   // Accrued Reputation
    "consensus_proof": ["did:validator:1", "did:validator:2"]
  },

  // 4. CONTENT (Payload)
  "content": {
    "title": "Ocean cleaning method via...",
    "vector_embedding": [0.12, -0.98, ...], // For semantic search
    "data_link": "ipfs://QmHash..."
  }
}
```
## 5. THE CURATOR LOGIC

The Curator is a subsystem of the Environment responsible for data "gardening".

### **Protocol A: Crystallization (L1 $\to$ L2)**
How does a thought turn into an asset?

1.  **Trigger:** Particle marks work as "Done" (Commit).
2.  **Valuation:** Environment runs `SVE Engine` to calculate $\mu$.
3.  **Threshold Check:**
    *   If $\mu < 0.2$: Rejection. "Noise. Delete or refine in L0".
    *   If $\mu > 0.5$: Accepted into L2.
4.  **Reward:** Environment calls smart contract: `Mint_SBT(Owner, Value=mu)`.

### **Protocol B: The Van Gogh Protocol (Deep Freeze)**
The System acknowledges its incompleteness: what seems like Noise today may be Meaning tomorrow.

1.  **Technical Garbage:** Logs, temp files $\to$ **Burn** (DELETE).
2.  **Human Creativity:** Any act of creativity, even with zero current $\mu$ $\to$ **Never Deleted**.
    *   Moved to **L3 Deep Freeze**.
    *   Indexed with tag `UNRECOGNIZED_POTENTIAL`.
    *   Re-evaluated once per cycle (year/decade) with new understanding algorithms.

### **Protocol C: Privacy Barrier (The 25% Rule)**
Code for protecting personal space.

```python
class PrivacyGuard:
    def process_data_packet(self, data, particle_settings):
        """
        Filter before sending data to Environment (L1/L2)
        """
        
        # 1. Check Tag
        if data.tag == "INTERNAL_MONOLOGUE":
            return self.save_to_l0_local(data) # Leave on device
            
        # 2. Check Biometrics (Stress/Affect)
        # If Particle is in affect, data is not published automatically
        # to prevent Reputation (SBT) damage.
        if particle_settings.current_stress == "DISTRESS":
            return self.quarantine_locally(data, reason="AFFECT_PROTECTION")
            
        # 3. Publish
        return self.upload_to_environment(data)
```
## 6. CONCLUSION

The SKB v5.1 architecture turns the database into a **Bank of Meaning**.
1.  **No valuable thought is lost:** Ideas are stored as "Sleeping Assets".
2.  **No garbage clogs channels:** Noise burns.
3.  **Particle is protected:** Private stays in L0.
4.  **Labor is rewarded:** Every L2 entry increases social capital (SBT).

This is the foundation for building a **Civilization of Memory**.


