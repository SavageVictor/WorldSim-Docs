---
layout: default
title: Reputation & Gossip System
parent: AI Systems
grand_parent: Documentation
nav_order: 10
---

**Related Documents:**
- AI Systems - Enhancements (future features)
- Economic Systems - Core (economic behavior integration)
- Economic Systems - Enhancements (future economic features)


## **2.9 Reputation & Gossip System**

### **Purpose**

Information spreads socially. NPCs form opinions about people they've never met based on stories. Reputation affects how strangers approach you.

---

### **2.9.1 Reputation Dimensions**

**Every Tier 2/3 NPC has reputation scores (0-100):**

**HONOR (0-100):** Do they keep their word?
- Based on: Kept promises, betrayals, oath-breaking  
- Impact: Affects initial Trust in new relationships

**COMPETENCE (0-100):** Are they good at what they do?
- Based on: Successes, failures, demonstrations of skill  
- Impact: Affects initial Respect in new relationships

**DANGER (0-100):** Are they a threat?
- Based on: Violence, threats, power displays, combat victories  
- Impact: Affects approach behavior (avoid, submit, or challenge)

**KINDNESS (0-100):** Do they help others?
- Based on: Charitable acts, cruelty, indifference  
- Impact: Affects how NPCs approach for help

**LOYALTY (0-100):** Can they be trusted with allegiance?
- Based on: History of betrayals, long-term relationships, faction switches  
- Impact: Affects recruitment, alliance offers

---

### **2.9.2 Information Flow**

**How reputation spreads:**

```
Character A has experience with Character B
    ↓
A forms opinion based on personal relationship/observation
    ↓
A shares opinion with Character C (if conditions met)
Conditions: Trust C, A is Social, Info significant, Appropriate environment
    ↓
C's opinion of B is modified
Weighting: High Trust in A = Believe more (×1.5)
           Low Trust in A = Skeptical (×0.5)
    ↓
C might share with Character D
    ↓
B's REPUTATION emerges from network of opinions
```

---

### **2.9.3 Gossip Mechanics**

**Gossip Triggers:**

| Location | Gossip Multiplier |
|----------|------------------|
| Taverns | +50% spread rate |
| Markets | +30% spread rate |
| Courts | +20% spread rate |
| Private | No gossip |

**Personality Effects:**

| Personality | Gossip Behavior |
|------------|-----------------|
| Social | Gossips 3× more than average |
| Solitary | Gossips 0.3× (rarely shares) |
| Honest | Accurate gossip (no embellishment) |
| Deceitful | May intentionally distort |
| Kind | Shares positive gossip more |
| Cruel | Shares negative gossip more |

**Gossip Spread Rate:**

```
Spread_Speed = 
  Event_Significance × 
  Spreader_Social_Trait × 
  Trust_in_Spreader × 
  Environmental_Factor
```

**Integration with Economic Systems:**
- High-value trade goods spread via gossip (Economic Systems - Core, Section 4.4)
- Trade reputation spreads socially (Economic Systems - Enhancements, Section 3.3)

---

### **2.9.4 Reputation Effects**

**How reputation affects new interactions:**

**High Honor (80+):** Strangers trust more initially (+20 base Trust), promises taken seriously

**Low Honor (20-):** Approached with caution (-20 base Trust), promises doubted

**High Danger + High Honor (80+, 80+):** Feared but respected, "Dangerous but fair"

**High Danger + Low Honor (80+, 20-):** Feared AND distrusted, constantly plotted against

See **Appendix F.4: Reputation Effect Examples** for detailed scenarios.

---

