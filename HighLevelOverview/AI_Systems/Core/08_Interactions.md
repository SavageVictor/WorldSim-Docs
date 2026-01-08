---
layout: default
title: Interaction System
parent: AI Systems
grand_parent: Documentation
nav_order: 8
---

**Related Documents:**
- AI Systems - Enhancements (future features)
- Economic Systems - Core (economic behavior integration)
- Economic Systems - Enhancements (future economic features)


## **2.7 Interaction System**

### **Purpose**

Define how NPCs interact with each other. Interactions change relationships, spread information, form alliances, create conflicts.

**Scope:** Primarily Tier 2/3 NPCs (who track individual relationships). Tier 1 NPCs interact at faction level.

---

### **2.7.1 Interaction Probability**

**When two NPCs are in same location, check if they interact:**

**Probability Formula:**

```
Interaction_Probability = 
  (Relationship_Factor + 
   Personality_Factor + 
   Goal_Factor + 
   Environment_Factor) / 4

If result > 50: Interaction occurs
```

**Factors:**

**Relationship Factor (-100 to +100):**
- If tracked relationship exists: (Affection + Respect) / 2
- If only faction relationship: Faction_Relationship score
- If rivals (Affection < -30): Brave +50 (confront), Cautious -50 (avoid)

**Personality Factor (0 to +100):**
- Social personality: +50
- Solitary personality: -30
- Brave personality: +20
- Cautious personality: -20

**Goal Factor (0 to +100):**
- Goal requires interacting with this NPC: +100
- Goal opposes this NPC: +50 (must confront or avoid)
- Goal unrelated: 0

**Environment Factor (0 to +50):**
- Tavern/social space: +30
- Private location: +20
- Public space: +10
- Battlefield/danger: +50 (intense bonding or conflict)

---

### **2.7.2 Interaction Types**

**Based on: Relationship dimensions + Personalities + Goals + Environment**

| Type | Conditions | Purpose |
|------|-----------|---------|
| **Friendly Chat** | Affection >40, no pressing goals | Maintain relationship, socialize |
| **Strategic Conversation** | Respect >40, goals align | Form alliance, coordinate |
| **Favor Request** | Trust >40, need help | Get assistance |
| **Secret Sharing** | Trust >60, Affection >50, private | Deepen bond, seek advice |
| **Confrontation** | Affection <0, goals conflict, Brave | Challenge, resolve conflict |
| **Manipulation Attempt** | Deceitful, power advantage, private | Achieve hidden goal |
| **Gossip** | Social, public/tavern, third party topic | Spread information, bond |
| **Reconciliation** | Past conflict, Affection >0 despite low Trust | Heal relationship |

See **Appendix D.1: Interaction Type Examples** for detailed scenarios.

---

### **2.7.3 Interaction Resolution**

**Each interaction plays out based on:**

**1. Personality-Driven Approach:**

| Personality | Approach Style |
|------------|---------------|
| Honest | States intentions directly |
| Deceitful | Hides true purpose, manipulates |
| Brave | Direct, confrontational if needed |
| Cautious | Indirect, feels situation out |
| Kind | Considerate, non-threatening |
| Cruel | Dismissive, harsh, dominating |
| Rational | Logical arguments |
| Emotional | Passionate appeals |

**2. Goal-Driven Content:** What does each NPC want from this interaction?

**3. Relationship History:** Past betrayals, support, memories affect current interaction

See **Appendix D.2: Interaction Resolution Examples** for step-by-step scenarios.

---

### **2.7.4 Outcome Processing**

**After interaction completes:**

**1. Relationship Dimension Updates:**
- Affection: ±5 to ±30 (based on pleasantness)  
- Respect: ±5 to ±20 (based on competence)  
- Trust: ±3 to ±50 (builds slow, destroyed quick)  
- Power Dynamic: ±5 to ±30 (if one dominated)

**2. Memory Creation (if significant):**
- If interaction emotional_weight > 50, create memory

**3. Goal Updates:**
- If goal achieved: Remove, generate new goal
- If goal blocked: Modify approach or abandon
- If new information: Goals may shift

**4. Gossip Propagation (if witnessed):**
- If public AND significant: Witnesses form opinions, Social NPCs spread stories

---

