---
layout: default
title: NPC Tiering System
parent: AI Systems
grand_parent: Documentation
nav_order: 2
---

**Related Documents:**
- AI Systems - Enhancements (future features)
- Economic Systems - Core (economic behavior integration)
- Economic Systems - Enhancements (future economic features)


## **2.1 NPC Tiering System**

### **Purpose**

Balance simulation depth with performance by intelligently allocating computational resources. Most NPCs use simplified systems; notable figures get full complexity.

**Note:** Tiering is purely technical and should be masked from players. Players should not see "Tier 1" labels - they should only notice that some NPCs are more developed than others organically.

---

### **2.1.1 Tier 1: The Masses (90% of population)**

**Identity Data:**

```
- Class: Peasant | Craftsman | Soldier | Merchant | Servant
- Culture/Religion: String identifier
- Age: Integer (years)
- Family Ties: Spouse ID (if any), Children count
- Personality: 3 Core + 4 Extended traits (see Section 2.2)
```

**Relationship Data:**

NO individual relationship tracking.

Instead:
- Faction Memberships: Array of 1-3 Faction IDs
- Faction Loyalty: (-100 to +100) per faction
- Class Sentiment: (-100 to +100) toward each major class
- Mood: (0-100) current happiness
- Grievances: Array (max 5) of recent anger triggers

**Note:** For economic trade, Tier 1 NPCs use lightweight acquaintance network (5-10 contacts) - see Economic Systems - Core, Section 4.1.

**Goal System:** Goals are **class-based**, not individual:

* Peasants: Survive, feed family, avoid conscription  
* Craftsmen: Earn wealth, gain guild status  
* Soldiers: Glory, loot, survival  
* Merchants: Wealth, trade routes, influence  
* Servants: Job security, decent treatment

**Behavior Patterns:** Behavior emerges from personality combinations (see Section 2.2.3)

**Performance Note:** Tier 1 NPCs can be processed in batches using DOTS Jobs. No pathfinding or complex AI needed for most.

---

### **2.1.2 Tier 2: Notable Figures (9% of population)**

**Identity Data:**

All Tier 1 data +

```
- 7 Full Personality Traits (same as Tier 1, but more nuanced)
- Title/Role: String (Knight, Guild Master, Local Lord, Bishop, War Hero)
- Reputation Scores (see Section 2.9.1):
  * Honor (0-100)
  * Competence (0-100)
  * Danger (0-100)
  * Kindness (0-100)
  * Loyalty (0-100)
```

**Relationship Data:**

- Track up to **20 individual relationships** (multi-dimensional, see Section 2.3)
- Everyone else: Abstracted
  * "Popular with peasants" (+60 mood modifier)
  * "Hated by clergy" (-40 relationship to priest class)

**Goal System:** Dynamic personal goals generated from:
* Personality traits  
* Current need level  
* Relationship pressures  
* Faction objectives

**Behavior Patterns:** Full personality system affects all decisions. More nuanced than Tier 1.

---

### **2.1.3 Tier 3: Major Players (1% of population)**

**Identity Data:**

All Tier 2 data +

```
- Title/Role: Major positions only
  * Kings, Dukes, Archbishops, Supreme Commanders, Legendary Heroes
- Multiple Concurrent Goals:
  * Personal goals
  * Factional goals
  * Dynastic goals (legacy, succession)
  * Ideological goals
```

**Relationship Data:**

- Track up to **50-100 individual relationships**
  * All other Tier 3 NPCs
  * Important Tier 2 NPCs
  * Key faction leaders

**Civilization Impact:** These NPCs can:
* Declare wars  
* Form/break alliances  
* Initiate reforms  
* Start religious/cultural movements  
* Create/destroy dynasties  
* Shape civilization policies

**Behavior Patterns:** Most complex. Every decision can have civilization-wide consequences.

---

### **2.1.4 Basic Promotion Concept**

**Purpose:** NPCs can rise from masses to notable figures through achievements.

**Core Concept:**
- Tier 1 NPCs who achieve significant things → Promoted to Tier 2
- Tier 2 NPCs who gain major power → Promoted to Tier 3

**Promotion Triggers:** See AI Systems - Enhancements for detailed triggers and mechanics.

**Basic Examples:**
- Peasant kills 5+ enemies in battle → War Hero (Tier 2)
- Merchant accumulates 10× average wealth → Rich Merchant (Tier 2)
- War Hero wins 10+ major battles → Legendary General (Tier 3)

**On Promotion:**
- Allocate more computational resources
- Begin tracking individual relationships (if moving to Tier 2/3)
- Generate dynamic personal goals
- Player may notice this NPC more (emergent "main character")

**Demotion:** Possible through death, loss of position, or prolonged irrelevance.

---

