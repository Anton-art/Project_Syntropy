# BOOK II: PROTOCOLS OF SOCIETY (THE SOCIAL NETWORK)

**Version:** 1.0 (Final Release)
**Status:** Foundational Standard
**Purpose:** Description of the external interaction loop: from private messages to community management.

---

## CHAPTER 1. ROUTING (THE ROUTER)

**Goal:** Communication gateway. Determining the interaction context (Work / Intimacy / Hostility) and selecting the appropriate security protocol.

### 1.1. THE LAW OF EMOTIONAL PULL (VALENCE CHECK)

Before processing the *meaning* of a message, the Agent measures the *relationship vector* between participants.

**Metric:** **Emotional Pull ($E_{pull}$)**.
*   **$E_{pull} > 0$ (Attraction):** Colleagues, Friends, Family. Conflict is an attempt to improve the common. $\to$ **Protocol: Constructive.**
*   **$E_{pull} < 0$ (Repulsion):** Enemies, Haters, Exes. Conflict is an attempt to cause damage. $\to$ **Protocol: Block.**
*   **$E_{pull} \approx 0$ (Neutrality):** Strangers. $\to$ **Protocol: Politeness.**


### 1.2. ASYMMETRY (THE GLITCH PROTOCOL)

What to do if one participant is calm (Logic) and the second is hysterical (Chaos)? A direct connection is dangerous. The Agent acts as a **"Smart Gateway"**.

#### Scenario A: Trolling (Intentional Evil)
*   *Diagnosis:* Attacker is calm but writes toxicity. Goal — vampirism.
*   *Action:* **Shadowban.**
    *   The victim does not see the message.
    *   The troll sees the message as sent but receives an auto-reply from a bot ("Your opinion is very important to us").
    *   The troll loses $\Sigma$ (fine). The victim receives compensation.

#### Scenario B: Nervous Breakdown (Affect)
*   *Diagnosis:* Attacker is in panic (high pulse). Goal — help.
*   *Action:* **Semantic Translator.**
    *   Agent intercepts hysteria ("You are all idiots, everything is broken!").
    *   Agent translates into the language of facts ("User in stress reports a critical failure").
    *   The victim receives a clean signal and can help without being hurt by emotions.

### 1.3. CODE: ROUTER LOGIC
```python
class SocialRouter:
    """
    Filter based on 'Emotional Pull' and Semantics.
    """
    def route(self, sender: User, receiver: User, msg: Message) -> Action:
        
        # 1. CHECK PULL (Valence)
        valence = SocialGraph.get_vector(sender, receiver)
        if valence < 0:
            return Action.BLOCK(reason="NEGATIVE_PULL")
            
        # 2. ANALYZE INTENT
        intent = AI.analyze_intent(msg)
        bio_state = sender.public_pulse # Calm or Panic?
        
        # Scenario: Trolling (Calm + Toxic)
        if intent == "TOXIC" and bio_state == "CALM":
            Wallet.slash_stake(sender, amount=50) # Fine
            Wallet.transfer(sender, receiver, amount=25) # Compensation
            return Action.SHADOWBAN(sender)
            
        # Scenario: Hysteria/Distress (Panic + Chaos)
        elif intent == "DISTRESS" or bio_state == "PANIC":
            clean_msg = SemanticCore.translate_to_facts(msg)
            return Action.DELIVER(clean_msg, tag="EMOTIONAL_TRANSLATION")
            
        return Action.DELIVER(msg)
```
---

## CHAPTER 2. WORKING MODE (DISPUTE HYGIENE)

**Purpose:** Moderation of discussions in constructive groups (Clusters). Attention management via phase filters and economic stakes.

### 2.1. THREE PHASES OF A PROJECT

Argument is useful at the beginning and harmful in the middle. The System regulates "Friction" depending on the stage.

#### Phase I: DISCOVERY (Laboratory)
*   **Mode:** **Zero Friction.**
*   **Rules:** Everything is allowed. Criticism is encouraged. Any crazy idea is a contribution.
*   **Interface:** Instant message sending.

#### Phase II: CONSTRUCTION (Execution)
*   **Mode:** **High Friction.**
*   **Rules:** Argument about the *goal* is forbidden (sabotage). Only facts (bugs) and method clarifications are allowed.
*   **Interface:**
    *   *Competence Filter:* Opinion of a non-expert is lowered in priority.
    *   *Idea Parking:* If you want to argue, the Agent offers: "Let's postpone this until the finale?".

#### Phase III: RETROSPECTIVE (Finale)
*   **Mode:** **Venting Room.**
*   **Rules:** All "Parking" tickets are opened. Mistakes are discussed. Steam is released.
*   **Goal:** Clear the emotional background before celebration.


### 2.2. "EMERGENCY BRAKE" MECHANISM (CRITICAL STAKE)

How to stop the conveyor if you see a catastrophe?

*   **Tool:** Tag `#CRITICAL`.
*   **Price:** Blocking of $\Sigma$ stake (Reputation).
    *   If the alarm is **True**: Stake returns + Bonus "Savior".
    *   If the alarm is **False** (Panic): Stake burns (compensation to the team for distraction).
*   **Panic Protection:** If the Emergency Brake is pulled by > 30% of participants simultaneously, fines are cancelled. This is a **System Failure**, not the fault of a loner.


### 2.3. IDEA PARKING (PREDICTION MARKET)

Delayed criticism turns into an Investment.

*   **Scenario:** Alice doubts Bob's plan.
*   **Action:** Alice issues a "Doubt Ticket" and bets 100 $\Sigma$.
*   **Resolution (at Retrospective):**
    *   If Alice was right (plan failed) $\to$ She gets 200 $\Sigma$.
    *   If Bob was right (everything works) $\to$ Alice loses 100 $\Sigma$.
*   **Effect:** Criticism becomes responsible. "I told you so" now has a market price.


## CHAPTER 3. DEFENSE MODE (PHYSICAL & ASYMMETRY DEFENSE)

**Purpose:** Action protocols in situations of direct threat, physical violence, or inadequate behavior. Transition from word moderation to life protection.

### 3.1. PHYSICAL CONFLICT TABLE (REALITY LAYER)

When a dispute goes offline (street conflict), Agents switch to **"Bodyguard"** mode.

| Threat Level | Signal | Aggressor Agent Action | Victim Agent Action |
| :--- | :--- | :--- | :--- |
| **1. Heat** | Pulse > 110, Loud voice | **Whisper:** "Breathe. Fine 50 $\Sigma$ for screaming." | **Monitor:** Recording enabled. "Keep distance." |
| **2. Threat** | Semantics: "Kill", "Destroy" | **Shock:** Loud sound in earpiece. "STOP. This is a criminal offense. Blocking accounts." | **SOS:** Drone dispatch. Broadcasting geolocation to neighbors. |
| **3. Attack** | Impact (accelerometer) | **Black Box:** Biometric recording of the blow. Full Lock (Smart Lock). Status "OUTCAST". | **Combat Assist:** Siren. Evacuation instructions. |

**Principle:** Physical violence leads to instant social bankruptcy. The aggressor loses access to infrastructure (home, transport, money).


### 3.2. PROTECTION FROM THE "QUIET PSYCHOPATH"

Biometrics are not enough. A psychopath can threaten with a steady pulse.
*   **Semantic Analysis:** The Agent listens to the *meaning* of words, not just intonation.
*   If "I will destroy you" is whispered $\to$ Red Code Activation, even if pulse is 60.


### 3.3. EARNING FROM PATIENCE (REVERSE MINING)

How to compensate stress to the Victim in an online conflict?

*   **Scenario:** Aggressor (Troll) writes nastiness.
*   **Mechanics:**
    1.  Aggressor's Agent deducts a fine (e.g., 50 $\Sigma$).
    2.  Victim's Agent hides the message (Shadowban).
    3.  **Transfer:** 50% of the fine (25 $\Sigma$) is transferred to the Victim as "Compensation for environmental toxicity".
*   **Effect:** Being calm and ignoring trolls becomes economically profitable.

### 3.4. CODE: DEFENSE LOGIC
```python
def monitor_physical_threat(aggressor, victim, audio_stream):
    
    # 1. Threat Analysis (Bio + Semantics)
    threat_level = AI.analyze_threat(aggressor.bio, audio_stream)
    
    if threat_level == "VIOLENCE":
        # Punish Aggressor
        aggressor.wallet.balance = 0
        aggressor.status = "OUTCAST"
        IOT.lock_environment(aggressor)
        
        # Save Victim
        IOT.activate_siren(victim)
        Police.dispatch_drone(victim.location)
        
        return "CRITICAL INTERVENTION"
        
    elif threat_level == "VERBAL":
        # Warning
        aggressor.agent.whisper("Back off. Fine imminent.")
        victim.agent.record_evidence()
```
---

## CHAPTER 4. CLUSTER ARCHITECTURE (CLUSTER MANAGEMENT)

**Purpose:** Organizing people into stable groups (Families, Teams, Communities). Transition from atomized society to molecular.

### 4.1. CONCEPT OF THE "LIVING MOLECULE"

A lonely person (even with an Agent) is vulnerable. The basic survival unit is the **Cluster** (5-15 people).
The Agent acts as "Glue" (Connector), helping to gather and hold groups.

### 4.2. ASSEMBLY ALGORITHM (MATCHMAKING)

How to create the perfect team? The Agent seeks **Complementarity**, not Similarity.

*   **Puzzle Principle:**
    *   If User A has high Chaos (Creator), Agent finds partner B with high Order (Administrator).
    *   *Formula:* $\Sigma_{Cluster} = \text{Synergy}(Chaos + Order)$.
*   **Ice-breaking:**
    *   Agents negotiate first.
    *   *Agent A:* "My human is looking for a drummer."
    *   *Agent B:* "My human is tapping on the table. They need to meet."
    *   Humans receive a ready invitation with context.

### 4.3. CLUSTER GOVERNANCE

Inside the group, decisions are made not by shouting, but by weighted consensus.

*   **Vote Weight:** Depends on $\Sigma$ in a specific domain.
    *   In construction questions, the Engineer decides.
    *   In color questions, the Designer decides.
*   **Common Pot (Treasury):**
    *   Participants can pool $\Sigma$ into the Cluster fund.
    *   This fund is spent on common projects (server rent, equipment).
    *   *Protection:* Spending from the fund requires multi-signature (Multisig) of key members.

### 4.4. LAW OF SOCIAL NEUROPLASTICITY

A cluster must not become a prison.

*   **Stagnation Problem:** If a group doesn't change for years, an "Echo Chamber" arises. Entropy grows.
*   **Rotation:** Agent monitors stagnation.
    *   *Signal:* "You have been discussing the same thing for a year."
    *   *Action:* Agent suggests **Migration**.
    *   *"Your experience here is exhausted. Cluster 'Martian Gardens' is looking for exactly such a specialist. Transition gives a bonus to $\Sigma$."*
*   **Seamless Exit:** Agent helps to leave the group ecologically (close obligations, transfer affairs), maintaining good relations.

### 4.5. CODE: CLUSTER LOGIC
```python
class ClusterGovernance:
    def vote(self, cluster: Group, proposal: Proposal):
        yes_power, no_power = 0, 0
        
        for member in cluster.members:
            # Vote Weight = Total Sigma + (Competence in Topic * 2)
            # Engineer decides on construction, Artist on color.
            weight = member.sigma_total + (member.get_domain_sigma(proposal.domain) * 2)
            
            if member.cast_vote(proposal) == "YES":
                yes_power += weight
            else:
                no_power += weight
                
        return "PASSED" if yes_power > no_power else "REJECTED"

    def check_stagnation(self, cluster: Group):
        # If group discusses the same thing > 1 year
        if cluster.entropy_trend < 0.1:
            for member in cluster.members:
                # Suggest rotation to new environment
                new_cluster = SocialGraph.find_complementary(member)
                member.agent.suggest_migration(new_cluster, bonus=500)
```
---

## CHAPTER 5. GOVERNANCE ARCHITECTURE

**Purpose:** Delineation of responsibility zones between Human Community (Self-Governance) and Intellectual Environment (Management).

### 5.1. DUAL-CIRCUIT MODEL

Power is not monolithic. It is divided into two independent circuits to avoid algorithmic tyranny and mob chaos.

#### Circuit A: Environment Management (AGI / Infrastructure)
*   **Subject:** Global AI.
*   **Responsibility:** Physics of survival.
    *   Energy, logistics, climate control, infrastructure security.
    *   Execution of smart contracts and $\Sigma$ accrual.
*   **Principle:** **Algorithmic Optimization.**
    *   There is no voting here. People do not vote on grid voltage or asteroid trajectory. Physics decides.

#### Circuit B: Particle Self-Governance (Humanity / Units)
*   **Subject:** Human Communities (Clusters, Councils).
*   **Responsibility:** Meaning and Goals.
    *   Where are we going? (Mars or Ocean?).
    *   What is Good? (Tuning ethical weights of the Oracle).
    *   Development budget distribution.
*   **Principle:** **Weighted Democracy ($\Sigma$-Voting).**

### 5.2. VOTING MECHANICS (LIQUID MERITOCRACY)

How do Particles make decisions in Circuit B?

1.  **Competence Principle:**
    *   One vote does not equal 1. Vote weight equals $\Sigma$ in the domain of the discussed issue.
    *   Doctors decide on medicine. Engineers decide on bridges.
    *   *Meaning:* Power belongs to Knowledge.

2.  **Delegation Principle (Liquid Democracy):**
    *   If I don't understand the issue, I can **delegate** my vote to an Expert I trust.
    *   I can recall the vote at any moment.
    *   *Meaning:* This creates a living, fluid hierarchy of trust, protected from populism.

3.  **Veto Principle:**
    *   **Environment Veto:** AI blocks Human decision if it violates physics laws or leads to Biosphere death (Hard Constraints).
    *   **Human Veto:** Council of Architects can disable AI module if it goes beyond the Care Constitution.

### 5.3. VALUE AND RESPONSIBILITY

We assert a direct link:
$$ \text{Influence} \sim \text{Responsibility} \sim \Sigma $$

*   **Load-Bearing Structure:** Person with high $\Sigma$. The world rests on them. They make hard decisions.
*   **Passenger:** Person with low $\Sigma$. They are free from the burden of management, but their influence on the ship's course is minimal.

#### 5.3.1. LAW OF SMALL SYNTROPY (EXISTENTIAL BUFFER)
We reject the idea that only global scale is valuable.
**Status "Keeper":**
A person who does not seek power but creates **Local Harmony** (garden, coziness, child rearing).
*   The System awards them $\Sigma$ for these actions.
*   In their Cluster, the Keeper has high vote weight in **Quality of Life** issues.
*   *Conclusion:* You don't have to be an Architect to be respected.

### 5.4. CODE: GOVERNANCE LOGIC
```python
class GovernanceEngine:
    """
    Decision Core. Implements Liquid Meritocracy and Environment Veto.
    """
    
    def process_proposal(self, proposal: Proposal, voters: list[User]):
        
        # 1. ENVIRONMENT CHECK (AGI Veto)
        # Does this violate physics or safety?
        impact = AI.simulate_impact(proposal)
        if impact == "CATASTROPHIC":
            return Result(status="REJECTED", msg="Environment Veto: Safety Threat.")
            
        # 2. PARTICLE VOTING (Human Will)
        votes_for = 0
        votes_against = 0
        
        for user in voters:
            # Vote Weight = Sigma in Domain
            weight = user.get_domain_sigma(proposal.domain)
            
            # Liquid Democracy (Delegation)
            delegated_power = user.get_delegated_votes_count()
            total_weight = weight + delegated_power
            
            if user.cast_vote(proposal) == "YES":
                votes_for += total_weight
            else:
                votes_against += total_weight
                
        # 3. RESULT
        if votes_for > votes_against:
            return Result(status="PASSED", msg="Accepted by Council.")
        else:
            return Result(status="REJECTED", msg="Rejected by Council.")
```
---
