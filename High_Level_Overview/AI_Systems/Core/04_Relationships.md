---
layout: default
title: Relationship System
parent: Core Systems
grand_parent: AI Systems
nav_order: 4
---

**Related Documents:**
- AI Systems - Enhancements (future features)
- Economic Systems - Core (economic behavior integration)
- Economic Systems - Enhancements (future economic features)


## **2.3 Relationship System**

### **Purpose**

Track relationships between NPCs at all tiers. Multiple independent dimensions create realistic interpersonal dynamics.

**Scope:** 
- Tier 1 NPCs: Track up to 5-10 relationships using simplified 3-dimensional model
- Tier 2 NPCs: Track up to 20 relationships using full 5-dimensional model
- Tier 3 NPCs: Track up to 50-100 relationships using full 5-dimensional model

---

### **2.3.1 Multi-Dimensional Relationships (Tier 2/3)**

Each tracked relationship has **5 independent axes:**

1. Affection (-100 to +100): How much they like each other emotionally
2. Respect (-100 to +100): How much they value the other's abilities/status
3. Trust (-100 to +100): How much they rely on honesty/reliability
4. Attraction (0 to 100): Physical/romantic interest *(optional)*
5. Power Dynamic (-100 to +100): Who has power over whom

---

### **2.3.2 Relationship Dimensions**

#### **AFFECTION (-100 to +100)**

**Definition:** How much they like each other emotionally

**Influences:**
- Shared positive experiences (+)  
- Shared negative experiences (-)  
- Personality compatibility (+/-)  
- Gifts and kindness (+)  
- Insults and cruelty (-)  
- Time spent together (+)

**Change Rate:** Slow (±5 per significant interaction)

**Notes:**
- Can respect someone you dislike (low affection, high respect)  
- Can like someone you don't respect (high affection, low respect)

---

#### **RESPECT (-100 to +100)**

**Definition:** How much they value the other's abilities, status, competence

**Influences:**
- Demonstrations of skill (+)  
- Failures and incompetence (-)  
- Social status and achievements (+)  
- Humiliation and public failure (-)  
- Shared challenges overcome (+)

**Change Rate:** Moderate (±10 per demonstration)

**Notes:**
- Can coexist with low affection (respected enemy)  
- Essential for following someone's leadership  
- Based on observable competence, not emotion

---

#### **TRUST (-100 to +100)**

**Definition:** How much they rely on each other, believe in honesty

**Influences:**
- Kept promises (+)  
- Broken promises (-)  
- Consistency over time (+)  
- Betrayals (---)  
- Secrets shared (+)  
- Vulnerability shown (+)

**Change Rate:** Builds slowly (+3 per positive), destroyed quickly (-50 per betrayal)

**Notes:**
- Can distrust someone you like (complicated friendship)  
- Essential for sharing secrets, making alliances  
- Hardest to rebuild once broken  
- Affects trade behavior (Economic Systems - Core, Section 7.3)

---

#### **ATTRACTION (0 to 100) - Optional**

**Definition:** Physical/romantic interest

**Influences:**
- Physical appearance  
- Personality compatibility  
- Mystery and intrigue  
- Circumstantial chemistry (shared danger, festivals)

**Change Rate:** Can spike quickly (+30 in single encounter), fades over time without reinforcement

**Notes:**
- Can exist without affection or trust (dangerous attraction)  
- Required for romantic relationships  
- Optional system - can disable entirely

---

#### **POWER DYNAMIC (-100 to +100)**

**Definition:** Who has power over whom

**Scale:**
```
-100 = They completely dominate me  
-50  = They have significant power over me  
0    = Equal relationship  
+50  = I have significant power over them  
+100 = I completely dominate them
```

**Influences:**
- Social status difference  
- Knowledge of damaging secrets  
- Debts owed (financial, life-debt)  
- Physical strength/combat ability  
- Position in hierarchy  
- Control of resources

**Change Rate:** Changes with circumstances (power shifts, revelations)

**Notes:**
- Affects how conflicts resolve (powerful party usually wins)  
- Can be hidden (secret blackmail creates hidden power)  
- Mutual power imbalance rare

---

### **2.3.3 Emergent Relationship States**

**The system does NOT assign relationship labels.** Labels emerge from dimension combinations.

**Example Emergent States:**

```
High Affection + High Respect + High Trust = "Close Friend"
High all + High Attraction = "Love/Soulmate"
Low Affection + High Respect + Low Trust = "Respected Rival"
Low all + High Power (them) = "Fear-Based Relationship"
```

See **Appendix B: Relationship Examples** for comprehensive relationship state table and scenarios including:
- B.1: Emergent Relationship State Table
- B.2: Relationship Evolution Over Time
- B.3: Complicated Relationship Scenarios

---

### **2.3.4 Relationship Memory**

Each tracked relationship stores **up to 10 significant memories** (most recent + most impactful):

**Memory Structure:**

```
Memory {
  event: String description
  impact: String (which dimensions changed, by how much)
  date: Timestamp
  witnesses: Array of NPC IDs (spreads gossip)
  emotional_weight: 0-100 (how much this memory matters)
}
```

**Example:**

```
{
  event: "Marcus paid off my family's debt, saving us from ruin",
  impact: "trust +50, affection +40, power_dynamic -30",
  date: "Year 3, Month 7, Day 12",
  witnesses: [],
  emotional_weight: 95
}
```

**Memory Effects on Behavior:**
- NPCs reference memories when making decisions  
- "Last time I trusted him, he betrayed me" → cautious despite current high affection  
- Witnesses can spread memories as gossip (Section 2.9)

**Memory Decay:**
- Emotional weight decreases 5% per year for neutral memories  
- Betrayals never decay (permanent scarring)  
- Life-saving events decay slower (2% per year)

See **Appendix B.4: Relationship Memory Examples** for detailed scenarios.

---

### **2.3.5 Relationship Scope Limits**

```
Tier 1 NPCs:
  - Track up to 5-10 individual relationships (lightweight)
  - Simplified 3-dimensional model: Affection, Respect, Trust only
  - NO Attraction or Power Dynamic tracking
  - NO relationship memory storage
  - Prioritize: Spouse, family members, close friends, regular trade partners
  - Everyone else abstracted as faction/class sentiment

Tier 2 NPCs:
  - Track up to 20 individual relationships (full model)
  - Full 5-dimensional model with all dimensions
  - Store up to 10 relationship memories per relationship
  - Prioritize: Other Tier 2/3, faction leaders, family, frequent contacts
  - Everyone else abstracted as class sentiment

Tier 3 NPCs:
  - Track up to 50-100 individual relationships (full model)
  - Full 5-dimensional model with all dimensions
  - Store up to 10 relationship memories per relationship
  - Prioritize: All Tier 3, important Tier 2, faction leaders, rivals, allies
  - More relationships = more political complexity
```

**Relationship Formation:**
- Tier 1 can form relationships with other Tier 1 NPCs (mutual tracking if both have capacity)
- Tier 2 can form relationship with anyone (tracked on Tier 2's side, mutual if other is Tier 1+)
- Tier 3 can form relationship with anyone (tracked on Tier 3's side, mutual if other is Tier 1+)
- When Tier 1 relationship slots are full, oldest/weakest relationships may be dropped

---

