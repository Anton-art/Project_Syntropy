```python
"""
GENESIS SIMULATION (v1.0)
-------------------------
The Integration Test for the Syntropic Civilization.
Connects: SVE Core + Protocols + Malachite DB.
"""

import time
import random
from sve_core import (
    SyntropicDispatcher, SyntropicEntity, UserStats, 
    EntityType, Verdict, AgentTestimony
)
from malachite_db import MalachiteStorage, NodeType
from protocols import UplinkProtocol, AgentIdentity, ResourceRequest

class GenesisSimulation:
    def __init__(self):
        print("🌌 INITIALIZING GENESIS SIMULATION...")
        
        # 1. Launch Infrastructure
        self.core = SyntropicDispatcher()
        self.db = MalachiteStorage() # Triggers _genesis (6 seeds) internally
        self.uplink = UplinkProtocol(self.core)
        
        # 2. Spawn Agents
        self.agents = self._spawn_agents()
        print(f"👥 POPULATION: {len(self.agents)} agents online.\n")

    def _spawn_agents(self):
        """Creates agent archetypes."""
        return [
            {
                "name": "Leonardo",
                "role": "CREATOR",
                "entity": SyntropicEntity("id_leo", EntityType.BIOSPHERE, "Leonardo", 5, 1000, 0.8, 100, 1.0, 100, 1.0, 10, 0, 0.9),
                "stats": UserStats("CITIZEN", 0, 500.0),
                "target_parent": "SEED_LOG", # Wants to evolve the Log
                "idea": "The Wheel: Continuous rotation around an axis."
            },
            {
                "name": "Barbarian",
                "role": "CHAOS",
                "entity": SyntropicEntity("id_troll", EntityType.BIOSPHERE, "Troll", 5, 100, 0.1, 1000, 1.0, 100, 1.0, 10, 0, 0.9),
                "stats": UserStats("CITIZEN", 0, 100.0),
                "target_parent": None, # Wants to write noise into the void
                "idea": "DESTROY EVERYTHING AAAAAA!!!!"
            },
            {
                "name": "Student",
                "role": "NOVICE",
                "entity": SyntropicEntity("id_student", EntityType.BIOSPHERE, "Student", 5, 100, 0.4, 10, 1.0, 50, 0.2, 10, 0, 0.3),
                "stats": UserStats("CITIZEN", 100, 5.0), # Low money, exhausted (Health 0.2)
                "target_parent": "SEED_STONE",
                "idea": "Polished Stone Tool."
            }
        ]

    def run_cycle(self):
        """Executes one Day Cycle of the System."""
        print("--- 🌞 DAY CYCLE START 🌞 ---")
        
        for agent in self.agents:
            print(f"\n👤 ACTOR: {agent['name']} ({agent['role']})")
            
            # 1. Form Request (Uplink)
            # Agent attempts to "Crystallize" their idea into the Knowledge Base
            print(f"   -> Attempting to crystallize: '{agent['idea'][:30]}...'")
            
            # 2. Diagnosis by Dispatcher (SVE + Scanner + Benevolent Core)
            # Constructing Agent Testimony
            testimony = AgentTestimony(
                context_mode="CREATIVE_FLOW" if agent['role'] == "CREATOR" else "RAGE",
                is_intentional=True,
                biological_state="CRITICAL" if agent['entity'].k_health < 0.3 else "STABLE",
                defense_plea="Trying to contribute."
            )
            
            prescription = self.core.diagnose(
                entity=agent['entity'],
                user_stats=agent['stats'],
                text_stream=agent['idea'],
                agent_testimony=testimony
            )
            
            print(f"   🏛️ SYSTEM VERDICT: {prescription.action.name}")
            print(f"      Rx: {prescription.treatment}")

            # 3. Execution of the Verdict
            if prescription.action == Verdict.AMPLIFY:
                # SUCCESS: Write to Malachite
                try:
                    if agent['target_parent']:
                        new_id = self.db.crystallize(agent['idea'], agent['target_parent'])
                        print(f"      💎 MALACHITE: New Layer created! ID: {new_id}")
                    else:
                        print("      🚫 MALACHITE REJECT: No Parent ID (Rootless Noise).")
                except Exception as e:
                    print(f"      🚫 DB ERROR: {e}")
                    
            elif prescription.action == Verdict.STOP:
                print("      🔒 ACTION BLOCKED: Quarantine.")
                
            elif prescription.action == Verdict.RECYCLE:
                print("      ♻️ FEEDBACK: Idea needs refinement.")

            # 4. Check for Benevolent Intervention
            if "CORE_INTERVENTION" in str(prescription.pathology):
                print("      🕊️ BENEVOLENT CORE: Emergency intervention recorded.")

        print("\n--- 🌙 NIGHT CYCLE: METABOLISM CHECK ---")
        self.core.metabolism.check_balance()

if __name__ == "__main__":
    sim = GenesisSimulation()
    sim.run_cycle()
```

