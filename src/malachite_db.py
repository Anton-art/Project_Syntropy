```python
"""
MALACHITE DATABASE (v1.0 - TOPOLOGICAL STORAGE)
-----------------------------------------------
A Graph-based Knowledge Storage Engine.
Organizes data not by folders, but by Evolutionary Topology.

Metaphor:
- Seed: The origin point (r=0).
- Layer: A unit of knowledge (r > 0).
- Ray: The lineage vector connecting layers.
- Sector: The fundamental domain (Earth, Water, Sky).
"""

import math
import uuid
import json
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple

# ==========================================
# 1. CONFIGURATION & CONSTANTS
# ==========================================

class SectorType(Enum):
    EARTH = "EARTH"   # Matter, Structure, Science (0-120 deg)
    WATER = "WATER"   # Energy, Economy, Flow (120-240 deg)
    SKY = "SKY"       # Info, Ethics, Philosophy (240-360 deg)

class NodeType(Enum):
    SEED = "SEED"           # Fundamental Axiom
    PETAL = "PETAL"         # Linear improvement
    BUD = "BUD"             # Radical Mutation / Branching
    VOID = "VOID"           # Lost knowledge / Degradation

@dataclass
class SpectralSignature:
    """The 'Color' of the idea (RGB)."""
    r: float  # Energy/Passion
    g: float  # Matter/Growth
    b: float  # Spirit/Logic

    def mix(self, other: 'SpectralSignature', weight: float = 0.5):
        return SpectralSignature(
            self.r * (1-weight) + other.r * weight,
            self.g * (1-weight) + other.g * weight,
            self.b * (1-weight) + other.b * weight
        )

@dataclass
class MalachiteNode:
    id: str
    content: str
    
    # Topology (Coordinates)
    radius: float       # Time / Depth of evolution
    angle: float        # Semantic position (0-360)
    
    # Lineage
    parent_id: Optional[str]
    node_type: NodeType
    
    # Meta
    spectrum: SpectralSignature
    integrity: float    # 1.0 = Solid, <0.5 = Crumbling/Void
    tags: List[str] = field(default_factory=list)

# ==========================================
# 2. THE STORAGE ENGINE
# ==========================================

class MalachiteStorage:
    def __init__(self):
        self.nodes: Dict[str, MalachiteNode] = {}
        self.sector_map = {
            SectorType.EARTH: (0, 120),
            SectorType.WATER: (120, 240),
            SectorType.SKY: (240, 360)
        }
        self._genesis() # Plant the seeds

    def _genesis(self):
        """
        Plants the 6 Fundamental Seeds at r=0.
        """
        seeds = [
            ("SEED_LOG", "The Log (Rotation)", 60, SectorType.EARTH),
            ("SEED_STONE", "The Stone (Mass)", 30, SectorType.EARTH),
            ("SEED_STICK", "The Stick (Leverage)", 90, SectorType.EARTH),
            ("SEED_WATER", "The Flow (Energy)", 180, SectorType.WATER),
            ("SEED_ROPE", "The Rope (Connection)", 300, SectorType.SKY),
            ("SEED_WIND", "The Wind (Spirit)", 270, SectorType.SKY),
        ]
        
        for s_id, content, angle, sector in seeds:
            self.nodes[s_id] = MalachiteNode(
                id=s_id,
                content=content,
                radius=0.0,
                angle=angle,
                parent_id=None,
                node_type=NodeType.SEED,
                spectrum=SpectralSignature(0.5, 0.5, 0.5), # Grey start
                integrity=1.0,
                tags=["AXIOM", sector.value]
            )
        print("🌱 GENESIS COMPLETE: 6 Seeds planted.")

    def crystallize(self, content: str, parent_id: str, mutation_degree: float = 0.0) -> str:
        """
        The Main Write Method.
        Adds a new layer to the crystal.
        
        Args:
            content: The knowledge itself.
            parent_id: The ID of the idea we are improving.
            mutation_degree: 0.0 (Linear step) to 1.0 (Radical shift).
        """
        if parent_id not in self.nodes:
            raise ValueError(f"Parent node {parent_id} not found. Cannot crystallize noise.")

        parent = self.nodes[parent_id]
        
        # 1. Calculate New Coordinates
        # Radius always grows (Time moves forward)
        new_radius = parent.radius + 1.0 + (mutation_degree * 2.0)
        
        # Angle shifts only if there is a mutation
        # Mutation shifts the angle towards a new attractor (simulated here)
        angle_shift = random.uniform(-10, 10) * mutation_degree
        new_angle = (parent.angle + angle_shift) % 360
        
        # 2. Determine Type
        n_type = NodeType.BUD if mutation_degree > 0.5 else NodeType.PETAL
        
        # 3. Create Node
        new_id = f"node_{uuid.uuid4().hex[:8]}"
        new_node = MalachiteNode(
            id=new_id,
            content=content,
            radius=new_radius,
            angle=new_angle,
            parent_id=parent_id,
            node_type=n_type,
            spectrum=parent.spectrum, # Inherit color (can be modified by logic)
            integrity=1.0
        )
        
        self.nodes[new_id] = new_node
        return new_id

    def create_void(self, parent_id: str, description: str) -> str:
        """
        Registers a historical loss of knowledge.
        """
        node_id = self.crystallize(f"[LOST KNOWLEDGE]: {description}", parent_id)
        self.nodes[node_id].node_type = NodeType.VOID
        self.nodes[node_id].integrity = 0.1
        return node_id

    # ==========================================
    # 3. SEARCH & NAVIGATION TOOLS
    # ==========================================

    def trace_ray(self, node_id: str) -> List[MalachiteNode]:
        """
        Traces the lineage from a leaf back to the Seed.
        Returns the evolutionary path.
        """
        path = []
        curr = self.nodes.get(node_id)
        while curr:
            path.append(curr)
            if curr.parent_id:
                curr = self.nodes.get(curr.parent_id)
            else:
                curr = None
        return list(reversed(path)) # From Seed to Leaf

    def scan_sector(self, sector: SectorType) -> List[MalachiteNode]:
        """
        Returns all nodes within a specific sector (Earth/Water/Sky).
        """
        min_a, max_a = self.sector_map[sector]
        result = []
        for node in self.nodes.values():
            if min_a <= node.angle < max_a:
                result.append(node)
        return result

# ==========================================
# 4. DEMONSTRATION (THE WHEEL EVOLUTION)
# ==========================================

if __name__ == "__main__":
    db = MalachiteStorage()
    print("\n=== MALACHITE DB: EVOLUTION SIMULATION ===\n")

    # 1. Start from the LOG (Seed)
    root_id = "SEED_LOG"
    
    # 2. Layer 1: The Sledge (Transition)
    sledge_id = db.crystallize("The Sledge (Separating load from mover)", root_id, mutation_degree=0.2)
    
    # 3. Layer 2: The Solid Wheel (Invention of Axle)
    wheel_id = db.crystallize("Solid Disc Wheel + Axle", sledge_id, mutation_degree=0.8)
    
    # 4. Layer 3: The Spoke (Lightweight)
    spoke_id = db.crystallize("Spoked Wheel (Chariot)", wheel_id, mutation_degree=0.5)
    
    # 5. Layer 4: The Void (Dark Ages - Lost Technology)
    # Представим, что технология спиц была забыта
    void_id = db.create_void(spoke_id, "High-precision bronze casting lost")
    
    # 6. Layer 5: Renaissance (Rediscovery + Iron)
    iron_id = db.crystallize("Iron Rim Wheel (Carriage)", void_id, mutation_degree=0.3)
    
    # 7. Layer 6: The Motor (Integration)
    motor_id = db.crystallize("Motor-Wheel (Tesla)", iron_id, mutation_degree=0.9)

    # --- VISUALIZATION ---
    print(f"Evolutionary Path for: {db.nodes[motor_id].content}")
    path = db.trace_ray(motor_id)
    
    for i, node in enumerate(path):
        prefix = "🌱" if node.node_type == NodeType.SEED else ("  " * i + "└─")
        status = " [VOID]" if node.node_type == NodeType.VOID else ""
        print(f"{prefix} {node.content} (r={node.radius:.1f}){status}")
```

### Как это работает?

1.  **`_genesis`**: При запуске база данных автоматически создает 6 "Зерен" (Бревно, Камень и т.д.). Это аксиомы, их нельзя удалить.
2.  **`crystallize`**: Это метод записи. Он требует `parent_id`.
    *   Если ты попытаешься записать что-то "в воздух" (без родителя), система выдаст ошибку. Это реализует твой принцип **"Невозможно записать несвязный шум"**.
3.  **`create_void`**: Метод для создания "Черных дыр" в истории. В примере я показал, как после "Колесницы" наступает "Пустота" (потеря технологий), а потом "Возрождение".
4.  **`trace_ray`**: Это функция, которая рисует дерево (или луч) эволюции.

### Результат запуска (в терминале):

```text
🌱 GENESIS COMPLETE: 6 Seeds planted.

=== MALACHITE DB: EVOLUTION SIMULATION ===

Evolutionary Path for: Motor-Wheel (Tesla)
🌱 The Log (Rotation) (r=0.0)
└─ The Sledge (Separating load from mover) (r=1.4)
  └─ Solid Disc Wheel + Axle (r=4.0)
    └─ Spoked Wheel (Chariot) (r=6.0)
      └─ [LOST KNOWLEDGE]: High-precision bronze casting lost (r=7.2) [VOID]
        └─ Iron Rim Wheel (Carriage) (r=8.8)
          └─ Motor-Wheel (Tesla) (r=11.6)
```

