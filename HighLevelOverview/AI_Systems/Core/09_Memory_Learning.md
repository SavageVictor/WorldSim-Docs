---
layout: default
title: Memory & Learning System
parent: AI Systems
grand_parent: Documentation
nav_order: 9
---

**Related Documents:**
- AI Systems - Enhancements (future features)
- Economic Systems - Core (economic behavior integration)
- Economic Systems - Enhancements (future economic features)


## **2.8 Memory & Learning System**

### **Purpose**

NPCs remember past events and learn from experience. Memory informs future decisions, creates grudges, builds trust, and shapes personality over time.

---

### **2.8.1 Memory Types**

**Three categories:**

**Relationship Memories (Tier 2/3 only):**
- Stored per relationship (Section 2.3.4)
- Key moments with specific individuals  
- Max 10 per relationship

**World Event Memories (All tiers):**
- Major civilization events
- Wars, famines, plagues, reforms  
- Who was responsible  
- How it affected the NPC

**Personal Experience Memories (All tiers):**
- Individual learning
- What strategies worked/failed  
- Who proved trustworthy/treacherous  
- Pattern recognition

---

### **2.8.2 Memory Storage Limits**

| Tier | Relationship Memories | World Event Memories | Personal Memories |
|------|---------------------|-------------------|------------------|
| Tier 1 | None | Last 5 major events | Last 10 experiences |
| Tier 2 | 10 per relationship (max 20 relationships) | Last 20 major events | Last 30 experiences |
| Tier 3 | 10 per relationship (max 50-100 relationships) | Last 50 major events | Last 50 experiences |

**Memory Prioritization (when at limit):**
1. Keep betrayals (never forget)  
2. Keep life-saving events  
3. Keep most recent  
4. Keep highest emotional weight  
5. Delete oldest neutral memories

---

### **2.8.3 Memory-Driven Behavior Changes**

**How memories affect future behavior:**

See **Appendix E: Memory & Learning Examples** for comprehensive scenarios including:
- E.1: Recent Betrayal Memory Effects
- E.2: Victory Pattern Learning
- E.3: Class Betrayal Pattern
- E.4: Trauma Recovery

**Basic Pattern:**

```
Experience → Memory Created → Behavior Modified
    ↓
Future similar situation
    ↓
Memory recalled → Decision influenced
```

**Example:**

```
NPC betrayed by ally
  → Memory: "Never trust X again" (emotional_weight: 95)
  → Future: Trust in X permanently lowered (-80)
  → Even if Affection recovers, Trust remains damaged
```

---

### **2.8.4 Pattern Recognition**

**NPCs learn from repeated experiences:**

**Pattern Formation:**

```
If similar outcome occurs 3+ times:
  → Pattern recognized
  → Behavior probability shifts
  → New modifier created
```

**Examples:**
- "Trusting X type always fails" → Don't trust X type  
- "Fighting in Y situation wins" → Fight in Y situations  
- "Being honest causes problems" → Become more Deceitful

**Pattern Strength:**

```
3 occurrences: Weak pattern (±10% behavior shift)
5 occurrences: Moderate pattern (±20% behavior shift)
10+ occurrences: Strong pattern (±40% behavior shift, trait shift possible)
```

**Pattern Breaking:**

```
If pattern violated 2+ times:
  → Pattern weakens
  → Behavior modifier reduces
  → "Maybe I was wrong about X"
```

---

### **2.8.5 Trauma & Formative Events**

**Extreme events create lasting changes:**

**Types:**
- Near-Death Experience (Courage -20, permanent unless conquered)
- Witnessed Extreme Cruelty (Kind ±10, Mood -10 permanent)
- Great Success (Confidence boost, Brave +10, Ambitious +10)

See **Appendix E.5: Trauma & Formative Event Examples** for detailed scenarios including:
- Near-death survival and recovery
- Witnessing cruelty (Kind vs Cruel reactions)
- Great success and overconfidence

---

