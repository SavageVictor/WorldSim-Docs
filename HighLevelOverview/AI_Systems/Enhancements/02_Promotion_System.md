---
layout: default
title: Promotion System
parent: Enhancements
grand_parent: AI Systems
nav_order: 2
---

**Related Documents:**
- AI Systems - Core (foundational AI behavior systems)
- Economic Systems - Core (economic integration)
- Economic Systems - Enhancements (future economic features)


# **PART 2: PROMOTION SYSTEM (DETAILED)**

## **2.1 Tier 1 → Tier 2 Promotion**

### **Purpose**

Recognize when a Tier 1 NPC achieves something significant enough to warrant individual tracking and deeper simulation.

### **Promotion Triggers**

| Achievement | Occupation Result | Requirements | Probability |
|------------|------------------|--------------|-------------|
| **Kill 5+ enemies in battle** | War Hero | Combat participation + kills tracked | Common in wars |
| **Accumulate 10× average wealth** | Rich Merchant | Wealth threshold | ~1% per year |
| **Survive 5+ major disasters** | Lucky/Cursed One | Survival tracking | Rare (~0.1%/year) |
| **Lead bandit gang (20+ raids)** | Infamous Outlaw | Bandit leadership | Rare (~0.5%/year) |
| **High piety + miracle** | Blessed One | Piety + rare event | Very rare (~0.01%/year) |
| **Gain local political position** | Local Lord/Guild Master | Appointed/elected | ~2% per year |
| **Master craftsman (100+ items)** | Master Craftsman | Craft tracking | ~0.5% per year |
| **Heroic rescue (save 10+ lives)** | Heroic Figure | Major event | Rare (~0.1%/year) |
| **Lead successful revolt** | Revolutionary Leader | Rebellion success | Very rare |
| **Random legendary event** | Various | 0.01% chance/year/NPC | Background rate |

### **Promotion Process**

**On Promotion to Tier 2:**

```
1. Generate 4 additional personality traits
   - Sample from distribution influenced by existing traits
   
2. Expand core trait ranges (-50/+50 → -100/+100)
   - Maintain relative position on scale
   
3. Activate individual relationship tracking (max 20)
   - Initialize empty, will form over time
   
4. Generate dynamic personal goals
   - Based on full personality + current state
   
5. Allocate more computation time
   - Move to Tier 2 processing queue
   
6. Assign title/role based on achievement

7. Initialize reputation scores (start at 50, adjust for achievement)
```

**Example:**

```
Tier 1 Peasant John (Courage 40, Loyalty 60, Ambition 30)
  → Kills 7 enemies in battle
  → PROMOTED to War Hero

New traits generated:
  - Kind: 20, Honest: 50, Rational: -10, Traditional: 40, Social: 30
  
Core traits expanded:
  - Courage: 40 → 80 (combat reinforced)
  - Loyalty: 60 → 60
  - Ambition: 30 → 30

Title: "War Hero John"
Reputation: Competence 70, Danger 70, Loyalty 70
```

See **Appendix A.1** for detailed promotion examples.

---

### **Promotion Rate Targets**

**Target:** ~1% of Tier 1 NPCs promoted to Tier 2 per year

```
Starting: 9,000 Tier 1, 900 Tier 2, 100 Tier 3
After 5 years: ~450 promotions
Equilibrium (20+ years): Ratio stabilizes at ~90%/9%/1%
```

---

## **2.2 Tier 2 → Tier 3 Promotion**

### **Purpose**

Recognize when a Tier 2 NPC gains civilization-level influence.

### **Promotion Triggers**

| Achievement | Requirements | Probability |
|------------|-------------|-------------|
| **Major political position** | Duke, general, archbishop, king | ~5% of Tier 2 per generation |
| **Legendary military status** | Win 10+ major battles as commander | ~1% of Tier 2 per generation |
| **Control regional economy** | Dominate city trade (>30% market share) | ~2% of Tier 2 merchants |
| **Lead mass movement** | Rebellion/reformation with 1000+ followers | Very rare (~0.1%) |
| **Legendary deed** | Slay dragon, save civilization | Extremely rare |
| **Found new faction** | Create major faction from scratch | ~0.5% per generation |
| **Achieve dynasty status** | 3 generations of power/wealth | ~1% per generation |

### **Promotion Process**

**On Promotion to Tier 3:**

```
1. Increase relationship tracking (20 → 50-100)
   
2. Add civilization-level decision capabilities
   - Can declare wars, form alliances, initiate reforms
   
3. Unlock factional leadership options
   
4. Generate dynasty/legacy goals
   
5. Add multiple concurrent goal tracking (personal, factional, dynastic, ideological)
   
6. Allocate maximum computation time
```

**Example:**

```
Tier 2 General Marcus (12 major victories, controls 2,000 soldiers)
  → Defeats invasion, saves civilization
  → PROMOTED to Supreme Commander (Tier 3)

Relationship capacity: 20 → 100
Civilization powers: ACTIVATED
Dynasty goals: "Establish House Marcus as noble family"
Multiple goals: Personal, Factional, Dynastic, Ideological
Title: "Supreme Commander Marcus the Legendary"
```

See **Appendix A.2** for detailed promotion scenarios.

---

### **Promotion Rate Targets**

**Target:** ~10% of Tier 2 NPCs promoted to Tier 3 per generation (30 years)

```
Tier 2: 900 NPCs
Promotions over 30 years: ~90
Deaths: ~50
Demotions: ~40
Result: Tier 3 remains at ~100 (equilibrium)
```

---

## **2.3 Demotion System**

### **Demotion Triggers**

**Tier 3 → Tier 2:**
- Loss of major position (duke loses lands)
- Catastrophic failure (general loses 5 battles)
- Faction collapse
- Prolonged irrelevance (10+ years no significant actions)
- Voluntary retirement

**Tier 2 → Tier 1:**
- Loss of notable status
- Prolonged irrelevance (20+ years)
- Bankruptcy (wealthy merchant goes broke)
- Social ostracism (reputation destroyed)

**Special Case: Death**
- Relationships preserved for history
- Reputation preserved as "legacy"
- Dynasty continues if children exist
- Resources freed immediately

### **Demotion Process**

```
1. Reduce relationship tracking
2. Simplify goal tracking
3. Reduce computation allocation
4. Update title/role ("Former Duke", "Disgraced General")
5. Reputation impact (Competence -30)
6. Emotional impact (Mood -50)
```

---

## **2.4 Promotion Effects & Consequences**

### **Gameplay Effects**

```
Early Game (Year 1-5):
  - Mostly Tier 1 NPCs
  - Promotion events exciting

Mid Game (Year 10-20):
  - Tier 2 population grows
  - Many notable figures with stories
  - Tier 3 become "main characters"

Late Game (Year 30+):
  - Established dynasties
  - Multi-generational stories
  - Legendary NPCs remembered
```

### **Emergent Stories Example**

```
Marcus's Rise:
Year 1: Born Tier 1 peasant
Year 6: Kills 7 enemies → Tier 2 War Hero
Year 16: Wins legendary battle → Tier 3 General
Year 20: Dies in battle → Legacy established
Year 50: House Marcus is major noble family

Player watched Marcus rise from nothing to legend!
```

### **Performance Considerations**

```
Computational Budget:
Tier 1: 1 unit
Tier 2: 5 units
Tier 3: 20 units

Starting: 15,500 units total
After stabilization: 19,000 units (~23% increase)

Must ensure performance scales gracefully
```

**Optimization:**
- Batch process promotions weekly
- Tier 2/3 decisions update monthly
- Demote inactive NPCs aggressively
- Cap Tier 3 at 150 maximum