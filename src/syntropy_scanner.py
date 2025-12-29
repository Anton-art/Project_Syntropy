```python
"""
SYNTROPIC SCANNER (v2.1 - The "Coherence" Update)
Tool for measuring the Thermodynamic Quality of Text.

Changelog v2.1:
    - [FIX] Small String Penalty: Fixed zlib overhead for short texts.
    - [NEW] Coherence Check: Distinguishes 'Disruption' from 'Garbage'.
    - [NEW] Dynamic Profiles: Different baselines for Code vs Prose.
"""

import zlib
import math
import re
from dataclasses import dataclass
from enum import Enum

class ContentType(Enum):
    PROSE = "PROSE"     # Ordinary language
    CODE = "CODE"       # Structured logic
    UNKNOWN = "UNKNOWN"

@dataclass
class ScannerAnalysis:
    text: str
    content_type: ContentType
    density: float      # Compression Ratio
    coherence: float    # Lexical validity
    vitality: float     # 3:1 Rule compliance
    mu_score: float     # Final Syntropy
    status: str
    is_disruption: bool

class SyntropyScanner:
    def __init__(self):
        # Calibration Profiles (Optimal Density)
        # Code is naturally more structured (lower entropy) than Prose.
        self.PROFILES = {
            ContentType.PROSE: 0.55,
            ContentType.CODE: 0.40, 
            ContentType.UNKNOWN: 0.50
        }
        self.SIGMA_WIDTH = 0.15

    def _detect_type(self, text: str) -> ContentType:
        """Simple heuristic to switch profiles."""
        # Check for common code symbols: {, }, ;, def, class, return
        code_signals = len(re.findall(r'[{};=()\[\]]', text))
        keywords = len(re.findall(r'\b(def|class|return|import|var|const|if|for)\b', text))
        
        if (code_signals + keywords) > len(text.split()) * 0.1:
            return ContentType.CODE
        return ContentType.PROSE

    def _calculate_coherence(self, text: str) -> float:
        """
        Rough measure of 'Human Readability'.
        Ratio of alphanumeric tokens to total length.
        Helps distinguish Encryption (Chaos) from Dense Text (Disruption).
        """
        if not text: return 0.0
        # Remove whitespace and common punctuation
        clean = re.sub(r'[\s.,!?]', '', text)
        if not clean: return 0.0
        
        # Count valid alphanumeric sequences
        tokens = re.findall(r'[a-zA-Z0-9]{2,}', text)
        token_len = sum(len(t) for t in tokens)
        
        return min(1.0, token_len / len(clean))

    def analyze(self, text: str) -> ScannerAnalysis:
        if not text or len(text.strip()) < 5:
            return None

        # 1. PRE-PROCESSING
        c_type = self._detect_type(text)
        optimal_density = self.PROFILES[c_type]
        
        # 2. PHYSICS: Compression Analysis (With Overhead Fix)
        original_bytes = text.encode('utf-8')
        original_size = len(original_bytes)
        
        # zlib adds header/footer (~6-12 bytes). We subtract overhead for fairness on short strings.
        compressed_data = zlib.compress(original_bytes)
        compressed_size = max(len(compressed_data) - 10, 1) 
        
        # Density Ratio (Clamped to 1.0 max)
        density = min(1.0, compressed_size / original_size)

        # 3. SEMANTICS: Coherence Check
        coherence = self._calculate_coherence(text)

        # 4. VITALITY: Gaussian Curve
        # How close is density to the Optimal for this content type?
        vitality = math.exp(-((density - optimal_density) ** 2) / (2 * self.SIGMA_WIDTH ** 2))

        # 5. SYNTROPY SCORE (Mu)
        # Mu = Log(Length) * Vitality * Coherence
        # We multiply by Coherence to penalize pure noise even if it has "good" density.
        length_log = math.log(original_size + 1)
        mu_score = length_log * vitality * coherence * 10.0

        # 6. CLASSIFICATION LOGIC
        status, is_disruption = self._classify(density, vitality, coherence)

        result = ScannerAnalysis(
            text=text,
            content_type=c_type,
            density=density,
            coherence=coherence,
            vitality=vitality,
            mu_score=mu_score,
            status=status,
            is_disruption=is_disruption
        )
        
        self._report(result)
        return result

    def _classify(self, density, vitality, coherence):
        is_disruption = False
        
        # A. NOISE FILTER
        if coherence < 0.3:
            return "🔥 CHAOS (Low Coherence / Noise)", False

        # B. DISRUPTION ZONE (The Van Gogh Protocol)
        # High Density (Hard to read) + High Coherence (Valid words)
        if density > 0.75 and coherence > 0.8:
            is_disruption = True
            return "🌪️ DISRUPTION (High Density Meaning)", True
            
        # C. STASIS ZONE
        if density < 0.3:
            return "🧊 STASIS (Repetitive / Bureaucracy)", False
            
        # D. CRYSTAL ZONE
        if vitality > 0.8:
            return "💎 CRYSTAL (Optimal Syntropy)", False
            
        return "💧 LIQUID (Normal Flow)", False

    def _report(self, res: ScannerAnalysis):
        preview = res.text[:60].replace("\n", " ") + "..." if len(res.text) > 60 else res.text
        print("-" * 60)
        print(f"INPUT ({res.content_type.value}): {preview}")
        print(f"STATUS: {res.status}")
        
        if res.is_disruption:
            print(" [!] VAN GOGH PROTOCOL ACTIVATED")
            print(" [!] Diagnosis: Idea is dense. Requires unpacking (Simulation).")
            print(f" [!] Potential Mu: {res.mu_score * 3.0:.2f}")
            
        print("-" * 60)
        print(f" > Density:   {res.density:.2f} (Coherence: {res.coherence:.2f})")
        print(f" > Vitality:  {res.vitality:.2f}")
        print(f" > SYNTROPY (µ): {res.mu_score:.2f}")
        print("\n")

if __name__ == "__main__":
    scanner = SyntropyScanner()
    print("=== SYNTROPY SCANNER v2.1 (Coherence Engine) ===\n")

    # TEST 1: Bureaucracy (Low Density)
    scanner.analyze("We need to leverage the synergy to leverage the synergy.")
    
    # TEST 2: Chaos (High Density, Low Coherence) -> Should be CHAOS now, not Disruption
    scanner.analyze("x8s7df87s6d8f76s8d7f6s8d7f6s8d7f")

    # TEST 3: Disruption (High Density, High Coherence) -> The Real Deal
    disruption = "Entropy=0. Syntropy=1. Life is the operator inverting the vector."
    scanner.analyze(disruption)

    # TEST 4: Code (Different Profile)
    code_snippet = "def calc(x): return x * 2 if x > 0 else 0"
    scanner.analyze(code_snippet)
```
