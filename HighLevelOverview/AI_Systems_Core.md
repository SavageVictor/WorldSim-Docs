# **AI Systems - Core (MVP)**

**Version:** 1.0  
**Last Updated:** 2025-01-XX  
**Document Type:** Core System Specification  
**Target Audience:** Development Team  
**Status:** Ready for Implementation

**Related Documents:**
- AI Systems - Enhancements (future features)
- Economic Systems - Core (economic behavior integration)
- Economic Systems - Enhancements (future economic features)

---

## **Table of Contents**

### **PART 1: EXECUTIVE SUMMARY**

1.1 Core Philosophy  
1.2 Key Numbers & Ratios  
1.3 Implementation Priorities

### **PART 2: CORE SYSTEMS**

**2.1 NPC Tiering System**
- 2.1.1 Tier 1: The Masses (90%)
- 2.1.2 Tier 2: Notable Figures (9%)
- 2.1.3 Tier 3: Major Players (1%)
- 2.1.4 Basic Promotion Concept

**2.2 Personality System**
- 2.2.1 Core 3-Trait System (All NPCs)
- 2.2.2 Extended 7-Trait System (All NPCs)
- 2.2.3 Personality-Behavior Matrix
- 2.2.4 Trait Modification Over Time

**2.3 Relationship System**
- 2.3.1 Multi-Dimensional Relationships (Tier 2/3)
- 2.3.2 Relationship Dimensions
- 2.3.3 Emergent Relationship States
- 2.3.4 Relationship Memory
- 2.3.5 Relationship Scope Limits

**2.4 Faction System**
- 2.4.1 Faction Types
- 2.4.2 NPC-Faction Relationships
- 2.4.3 Faction-to-Faction Relationships
- 2.4.4 Factional Dynamics

**2.5 Occupation System**
- 2.5.1 Occupation as Dynamic State
- 2.5.2 Major Occupation Types
- 2.5.3 Occupation Emergence Conditions
- 2.5.4 Supply/Demand System (See Economic Systems - Core)
- 2.5.5 Occupation Satisfaction & Loyalty (Placeholder)
- 2.5.6 Career Progression Paths (Placeholder)

**2.6 Need & Goal System**
- 2.6.1 Modified Maslow Hierarchy
- 2.6.2 Personality-Modified Priorities
- 2.6.3 Dynamic Goal Generation
- 2.6.4 Goal Conflicts

**2.7 Interaction System**
- 2.7.1 Interaction Probability
- 2.7.2 Interaction Types
- 2.7.3 Interaction Resolution
- 2.7.4 Outcome Processing

**2.8 Memory & Learning System**
- 2.8.1 Memory Types
- 2.8.2 Memory Storage Limits
- 2.8.3 Memory-Driven Behavior Changes
- 2.8.4 Pattern Recognition
- 2.8.5 Trauma & Formative Events

**2.9 Reputation & Gossip System**
- 2.9.1 Reputation Dimensions
- 2.9.2 Information Flow
- 2.9.3 Gossip Mechanics
- 2.9.4 Reputation Effects

**2.10 Conflict Resolution System**
- 2.10.1 Conflict Types
- 2.10.2 Resolution Methods
- 2.10.3 Outcome Consequences

**2.11 Civilization-Level Dynamics**
- 2.11.1 Occupation Ratios & Health
- 2.11.2 Factional Power Balance
- 2.11.3 Cultural/Religious Movements
- 2.11.4 Population Dynamics

### **PART 3: DESIGN RATIONALE**

3.1 Emergence Philosophy  
3.2 Why These Systems Create Stories  
3.3 Scalability Considerations  
3.4 Expected Emergence Patterns  
3.5 Design Goals & Success Metrics

### **APPENDICES**

A. Personality Behavior Examples  
B. Relationship Examples  
C. Goal Generation Examples  
D. Conflict Resolution Examples  
E. Memory & Learning Examples  
F. Emergence Pattern Examples  
G. Quick Reference Tables

---

# **PART 1: EXECUTIVE SUMMARY**

## **1.1 Core Philosophy**

**Stories emerge from systems, not scripts.**

In this civilization simulation, thousands of NPCs create dynamic narratives through:

* **Deep relationships** that evolve over time  
* **Personalities** that shape every decision  
* **Emergent occupations** that respond to world conditions  
* **Factional dynamics** that drive civilizations  
* **Memories** that inform future actions

The simulation creates conditions. The NPCs write the story.

**Key Principles:**

1. **No pre-scripted stories** - All narratives emerge from system interactions  
2. **Personality drives behavior** - Every decision filtered through personality traits  
3. **Scale through tiering** - Balance depth (notable NPCs) with performance (masses)  
4. **Cascading effects** - Individual decisions create civilization-level changes  
5. **Player as conductor** - Set conditions, observe emergence, intervene strategically

---

## **1.2 Key Numbers & Ratios**

### **Population Distribution**

Total NPCs per Civilization: ~10,000

```
Tier 1 (Masses):           9,000 NPCs (90%)
  - 3-trait + 7-trait personality
  - Faction relationships only (no individual tracking)
  - Class-based goals

Tier 2 (Notable):            900 NPCs (9%)
  - Full 7-trait personality
  - Track up to 20 individual relationships
  - Dynamic personal goals

Tier 3 (Major Players):      100 NPCs (1%)
  - Full 7-trait personality
  - Track up to 50-100 individual relationships
  - Multiple concurrent goals (personal + factional + dynastic)
```

### **Healthy Civilization Occupation Ratios**

```
Farmers:     60-70%  (Food security)
Craftsmen:   10-15%  (Goods production)
Soldiers:     5-10%  (Defense without over-militarization)
Merchants:    5-10%  (Trade flowing)
Bandits:      <2%    (Crime controlled)
Nobles:       <1%    (Governance)
Others:       3-8%   (Servants, laborers, specialized roles)
```

### **Faction Distribution per Civilization**

```
Major Factions:    3-5   (Noble, Merchant, Clergy, Military, Regional)
Minor Factions:   10-20  (Specific houses, guilds, cults, movements)

Each NPC belongs to: 1-3 factions
```

### **Relationship Tracking Limits**

```
Tier 1: No individual relationships (only faction relationships)
Tier 2: Max 20 tracked relationships
Tier 3: Max 50-100 tracked relationships
```

### **Memory Storage Limits**

```
Tier 1: Last 5 major civilization events
Tier 2: Last 20 events + 10 memories per relationship
Tier 3: Last 50 events + 10 memories per relationship
```

### **Time & Aging**

```
Aging Speed: Approximate to Rimworld pace
- 1 year = ~12-60 real-time minutes (adjustable)
- NPCs age, have children, die
- Generational shifts occur (30-year cycles)
```

---

## **1.3 Implementation Priorities**

### **CORE SYSTEMS (MVP - Must Have)**

**Phase 1: Foundation**
* NPC Tiering System (all 3 tiers)  
* Personality System (3-trait + 7-trait for all NPCs)  
* Faction System (all NPCs)  
* Basic Occupation System (emergence conditions)  
* Need & Goal System (Maslow hierarchy)  
* Civilization-Level Dynamics (occupation ratios, faction balance)

**Phase 2: Depth**
* Multi-Dimensional Relationships (Tier 2/3)  
* Interaction System (NPCs talk and affect each other)  
* Memory & Learning (past informs future)  
* Conflict Resolution (how goals clash)

**Phase 3: Social**
* Reputation & Gossip (information spreads socially)  
* Basic Promotion System (Tier 1 → Tier 2 → Tier 3)

**Why Core:** These systems create the basic simulation loop. NPCs have personality, belong to factions, choose occupations based on needs, and affect civilization health.

---

# **PART 2: CORE SYSTEMS**

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

## **2.2 Personality System**

### **Purpose**

Personality drives every decision an NPC makes. All NPCs have 7 personality traits that shape their behavior.

---

### **2.2.1 Core 3-Trait System (Foundation)**

**ALL NPCs have these three core traits:**

#### **COURAGE (-100 to +100)**

```
High (+):  Brave, confrontational, takes risks, faces danger
Low (-):   Cautious, avoids conflict, prioritizes safety, flees
```

**Affects:**
- Willingness to fight vs flee  
- Occupation choice (soldier vs farmer)  
- Confrontation behavior  
- Risk tolerance in decisions

---

#### **LOYALTY (-100 to +100)**

```
High (+):  Loyal to faction, keeps oaths, traditional values
Low (-):   Self-serving, opportunist, betrays easily
```

**Affects:**
- Faction switching probability  
- Betrayal likelihood  
- Following orders  
- Oath-keeping

---

#### **AMBITION (-100 to +100)**

```
High (+):  Wants power/status, competitive, restless, seeks change
Low (-):   Content with station, simple needs, peaceful, stable
```

**Affects:**
- Goal hierarchy (pursue Esteem vs Belonging)  
- Occupation advancement desire  
- Political scheming  
- Satisfaction with current state

---

### **2.2.2 Extended 7-Trait System (Full Personality)**

**ALL NPCs also have these four additional traits:**

#### **KIND ↔ CRUEL (-100 to +100)**

```
Kind (+):   Help others, forgive easily, sacrifice, charitable
Cruel (-):  Exploit weakness, hold grudges, selfish, enjoy suffering
```

**Affects:**
- Treatment of inferiors  
- Forgiveness of wrongs  
- Charitable behavior  
- Cruelty in conflict

---

#### **HONEST ↔ DECEITFUL (-100 to +100)**

```
Honest (+):     Keep word, direct speech, value honor, transparent
Deceitful (-):  Lie easily, manipulate, pragmatic, hidden agendas
```

**Affects:**
- Promise keeping  
- Manipulation tactics  
- Reputation for honor  
- Trustworthiness  
- Trade behavior (Economic Systems - Core, Section 7.3)

---

#### **RATIONAL ↔ EMOTIONAL (-100 to +100)**

```
Rational (+):   Logic-driven, calculating, cold analysis, long-term
Emotional (-):  Feelings-driven, passionate, impulsive, immediate
```

**Affects:**
- Decision speed  
- Persuasion methods  
- Goal consistency  
- Conflict approach  
- Trade decisions (Economic Systems - Core, Section 7.3)

---

#### **TRADITIONAL ↔ PROGRESSIVE (-100 to +100)**

```
Traditional (+):  Follow customs, respect hierarchy, preserve past
Progressive (-):  Challenge norms, egalitarian, innovate, change
```

**Affects:**
- Response to reforms  
- Cultural movement alignment  
- Religious orthodoxy  
- Social structure support

---

#### **SOCIAL ↔ SOLITARY (-100 to +100)**

```
Social (+):    Need company, many relationships, talkative, groups
Solitary (-):  Need alone time, few deep bonds, quiet, individual
```

**Affects:**
- Relationship formation rate  
- Gossip spreading (Section 2.9.3)  
- Group vs individual activities  
- Leadership style  
- Trade network size (Economic Systems - Core, Section 4.1)

---

### **2.2.3 Personality-Behavior Matrix**

**How Trait Combinations Create Behavior:**

See **Appendix A: Personality Behavior Examples** for comprehensive tables including:
- A.1: 3-Trait Core Combinations
- A.2: Leadership Archetypes
- A.3: Conflict Resolution Styles
- A.4: Relationship Formation Patterns
- A.5: Occupation Natural Fits

**Example - Simple Combination:**

```
NPC: High Courage (+60), High Loyalty (+70), Low Ambition (-40)

Result: STEADFAST DEFENDER
- Brave and loyal but content
- Protects faction without personal ambition
- Reliable warrior, won't seek promotion
- Happy as foot soldier serving cause
```

**Example - Complex Combination:**

```
NPC: Brave (+60), Ambitious (+70), Deceitful (+50), Rational (+60)

Result: MACHIAVELLIAN WARLORD
- Brave enough to take risks
- Ambitious enough to seek power
- Deceitful enough to manipulate
- Rational enough to calculate moves
- Dangerous political player
```

---

### **2.2.4 Trait Modification Over Time**

**Traits can shift based on experiences:**

**Formative Experiences:**

| Experience | Trait Effect | Magnitude |
|------------|-------------|-----------|
| Near-death survival | Courage -10 to -30 | Immediate, fades 1-3 years |
| Repeated combat victories | Courage +5 to +15 | Gradual, permanent if consistent |
| Betrayed by trusted ally | Loyalty -20, Honest -10 | Immediate, permanent |
| Witnessed extreme cruelty | Kind ±10 | Immediate, long-lasting |
| Years of stable prosperity | Ambition -10 | Gradual, reversible |
| Long period of hardship | Ambition +10 | Gradual, reversible |
| Religious conversion | Traditional ±20 | Major event, permanent |
| Successful manipulation | Deceitful +5 | Gradual, reinforces behavior |
| Failed deception exposed | Honest +10 | Immediate, may be permanent |

**Age Effects:**

| Age Range | Typical Trait Shifts |
|-----------|---------------------|
| Young (15-25) | Ambitious +10, Brave +5, Rational -5 |
| Middle (30-50) | Balanced, minimal shifts |
| Elderly (60+) | Ambitious -10, Cautious +10, Traditional +5 |

**Limits:**
- Traits cannot exceed -100 to +100 range  
- Core personality remains recognizable  
- Maximum shift per year: ±20 points per trait

See **Appendix A.6: Trait Modification Examples** for detailed scenarios.

---

## **2.3 Relationship System**

### **Purpose**

Track complex relationships between Tier 2/3 NPCs. Multiple independent dimensions create realistic interpersonal dynamics.

**Scope:** Only Tier 2 and Tier 3 NPCs track individual relationships. Tier 1 uses faction relationships only (though they have lightweight acquaintance networks for trade - see Economic Systems - Core, Section 4.1).

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
  - NO individual relationship tracking
  - Only faction relationships
  - Can still be in relationships (spouse, family) but not mechanically tracked
  - Use lightweight acquaintance network for trade (Economic Systems - Core)

Tier 2 NPCs:
  - Track up to 20 individual relationships
  - Prioritize: Other Tier 2/3, faction leaders, family, frequent contacts
  - Everyone else abstracted as class sentiment

Tier 3 NPCs:
  - Track up to 50-100 individual relationships
  - Prioritize: All Tier 3, important Tier 2, faction leaders, rivals, allies
  - More relationships = more political complexity
```

**Relationship Formation:**
- Tier 2 can form relationship with Tier 1 (tracked on Tier 2's side only)  
- Tier 3 can form relationship with anyone (tracked on Tier 3's side only)  
- Mutual tracking only when both are Tier 2+

---

## **2.4 Faction System**

### **Purpose**

Abstract mass relationships. Instead of tracking millions of individual relationships, track NPCs' relationships to **factions** (groups).

**Applies to:** ALL NPCs (Tier 1, 2, and 3)

---

### **2.4.1 Faction Types**

**Major Factions (3-5 per civilization):**

| Faction Type | Role | Power Source |
|-------------|------|--------------|
| **Noble Houses** | Political power, land control | Hereditary title, military force |
| **Guilds** | Economic power, trade control | Wealth, market monopoly |
| **Military Organizations** | Martial power, force projection | Weapons, training, discipline |
| **Regional/Cultural Groups** | Identity, cultural preservation | Shared heritage, language, customs |

**Minor Factions (10-20 per civilization):**
- Specific noble families (House Varlen, House Marcus)  
- Craft guilds (Blacksmiths, Carpenters, Weavers)  
- Bandit gangs (Red Hand Gang, Forest Outlaws)  
- Mercenary companies (Iron Legion, Silver Swords)  
- Secret societies (Mage Circle, Thieves Guild)  
- Revolutionary movements (Peasant Reform Front)  
- Regional clans and tribes

**Faction Lifecycle:**
- Factions can be created dynamically (rebellion forms new faction)  
- Factions can merge (alliance becomes single faction)  
- Factions can dissolve (defeat, irrelevance, absorption)

---

### **2.4.2 NPC-Faction Relationships**

**Every NPC belongs to 1-3 factions:**

**Example:**

```
Peasant John {
  factions: [
    {id: House_Varlen, loyalty: 45},
    {id: Northerners, loyalty: 60}
  ]
}
```

**Loyalty Score (-100 to +100):**

```
+100 = Fanatical devotion, will die for faction  
+70  = Strong loyalty, very reliable  
+30  = Mild loyalty, generally supportive  
0    = Neutral, no strong feelings  
-30  = Mild opposition, quietly resist  
-70  = Strong opposition, actively undermine  
-100 = Hatred, seek faction's destruction
```

**Loyalty Modifiers:**

| Event | Loyalty Change |
|-------|---------------|
| Faction helps NPC directly | +10 to +30 |
| Faction harms NPC directly | -20 to -60 |
| Faction wins major victory | +5 to all members |
| Faction suffers major defeat | -10 to all members |
| Faction leader changes | -10 to +10 (personality dependent) |
| Ideology conflict with NPC | -5 per conflict |
| Ideology alignment with NPC | +5 per alignment |
| Years of membership | +2 per year (max +30) |

**Multiple Faction Conflicts:** 

If NPC's factions go to war with each other, NPC must choose based on:
1. Higher loyalty score (primary factor)
2. Personality (Loyalty trait reinforces, Low Loyalty makes betrayal easy)
3. Personal relationships (Tier 2/3 might follow a person, not faction)
4. Survival (which side more likely to win?)

---

### **2.4.3 Faction-to-Faction Relationships**

**Factions have relationships with each other (-100 to +100):**

**Example:**

```
House Varlen ↔ Merchants Guild: +60 (trade alliance)
House Varlen ↔ House Marcus: -40 (political rivalry)
House Varlen ↔ Royal Army: +70 (loyal vassal)
```

**Relationship Effects:**

| Relationship Score | Effect |
|-------------------|--------|
| +80 to +100 | **Alliance** - Fight together, share resources |
| +50 to +79 | **Cooperation** - Work together on common goals |
| +20 to +49 | **Friendly** - Trade, minor cooperation |
| -19 to +19 | **Neutral** - No special relationship |
| -20 to -49 | **Tension** - Avoid each other, minor conflicts |
| -50 to -79 | **Hostility** - Active opposition, sabotage |
| -80 to -100 | **War** - Open conflict, violence |

**Faction Relationship Changes:**

| Event | Relationship Change |
|-------|-------------------|
| Military alliance formed | +30 to +50 |
| Trade agreement signed | +10 to +20 |
| Border dispute | -10 to -20 |
| One faction attacks other | -40 to -70 |
| One faction betrays other | -70 to -90 |
| Shared enemy defeated together | +20 to +30 |
| Leadership change | -10 to +10 (partial reset) |

---

### **2.4.4 Factional Dynamics**

**How Factions Create Emergent Behavior:**

See **Appendix F.1: Faction Conflict Examples** for detailed scenarios including:
- Faction conflict affecting individuals
- Individual actions affecting faction relationships
- Faction power balance scenarios

**Basic Pattern:**

```
Faction Event (war, alliance, betrayal)
    ↓
Affects all faction members (loyalty shifts, mood changes)
    ↓
Individual NPCs respond based on personality
    ↓
Aggregate individual responses affect faction strength
    ↓
New faction event emerges from collective action
```

---

## **2.5 Occupation System**

### **Purpose**

Occupations are **not assigned** - they emerge from environmental conditions, personal capability, personality, and opportunity. NPCs change occupations dynamically as world conditions change.

---

### **2.5.1 Occupation as Dynamic State**

**Every NPC has:**

```
Current Occupation: String (Farmer, Soldier, Bandit, Merchant, etc.)
Occupation History: Array of past occupations with dates
Occupation Loyalty: 0-100 (how committed to current role)
Occupation Satisfaction: -100 to +100 (happiness with current role)
```

**Occupations can change when:**
- Environmental conditions change (famine makes farming impossible)  
- Better opportunity appears (lord offers soldier position)  
- Forced change (conscription, exile, imprisonment)  
- Personal crisis (spouse murdered → revenge seeker)  
- Ambition realizes opportunity (sees chance for power)

**Example:**

```
{
  current: "Bandit Leader",
  loyalty: 70,
  satisfaction: 45,
  history: [
    {occupation: "Peasant", start: Year 1, end: Year 4},
    {occupation: "Soldier", start: Year 4, end: Year 6, reason: "Conscripted"},
    {occupation: "Deserter", start: Year 6, end: Year 6, reason: "Unpaid"},
    {occupation: "Bandit", start: Year 6, end: Year 8, reason: "Survival"},
    {occupation: "Bandit Leader", start: Year 8, reason: "Promoted"}
  ]
}
```

---

### **2.5.2 Major Occupation Types**

**Primary Occupations:**
1. **Farmers/Laborers** - Food production, manual labor  
2. **Craftsmen/Artisans** - Goods production, skilled trades  
3. **Soldiers/Warriors** - Military service, defense  
4. **Bandits/Outlaws** - Criminal activity, raiding  
5. **Merchants/Traders** - Commerce, trade  
6. **Nobles/Rulers** - Governance, leadership (special case)

**Secondary/Specialized Occupations:**
- Scholars/Mages (if magic exists)  
- Mercenaries (soldiers for hire)  
- Guards (city/trade protection)  
- Servants (domestic service)  
- Entertainers (bards, actors)  
- Assassins (murder for hire)  
- Spies (information gathering)

---

### **2.5.3 Occupation Emergence Conditions**

**Each occupation has emergence conditions based on:** Environment, Personality, Alternatives, Needs

#### **FARMERS/LABORERS**

**Required:**
- Land available OR employer needs workers
- Peaceful region (can work safely)

**Personality Fit:**
- Low Ambition (content with simple life)
- OR Desperate (any personality if starving)

**Satisfaction Factors:**

Positive: Food security (+20), Fair treatment (+15), Peace (+10), Good harvest (+10)
Negative: Heavy taxation (-20), Conscription threats (-15), Poor harvests (-30), War (-40)

**Likely Transitions:**
- → Soldier (if conscripted, war glory appeals, high courage)  
- → Bandit (if starving + lawless region)  
- → Refugee (if war/famine destroys livelihood)

---

#### **SOLDIERS/WARRIORS**

**Required:**
- Threat exists (war, bandits, expansion ambition)
- Recruitment happening (lord needs army)

**Personality Fit:**
- High Courage + (High Loyalty OR Desperate OR High Ambition)

**Recruitment Methods:**
- Voluntary: Glory seekers, loyal servants, ambitious youth
- Conscription: Forced (creates Low Loyalty soldiers)
- Mercenary: Hired professionals (purely economic)

**Satisfaction Factors:**

Positive: Regular pay (+20), Victory (+30), Loot/glory (+25), Comradeship (+10)
Negative: Unpaid wages (-40), Boredom in peacetime (-20), Poor leadership (-25), High casualties (-30)

**Likely Transitions:**
- → Veteran/Knight (if heroic, promoted to Tier 2)  
- → Bandit (if unpaid, Low Loyalty, peacetime boredom)  
- → Mercenary (if army disbands)  
- → Farmer (if maimed, tired, seeking peace)  
- → Dead (high mortality rate)

---

#### **BANDITS/OUTLAWS**

**Required:**
- Desperation (poverty, starvation) OR
- Opportunity (weak law, rich targets) OR
- Grievance (unjust treatment, revenge)

**Personality Fit:**
- High Courage (willing to risk)
- Low Loyalty (no moral barrier)
- Lawless region

**Types:**
- Desperate Bandits: Starving farmers turned criminal
- Professional Bandits: Career criminals, organized
- Political Bandits: Rebels, revolutionaries (ideological)

**Satisfaction Factors:**

Positive: Successful raids (+30), Strong leader (+20), Freedom (+15)
Negative: High death risk (-30), Hunted (-25), Moral conflict if Kind (-20)

**Likely Transitions:**
- → Warlord/Rebel Leader (if successful, Tier 2/3)  
- → Soldier (if offered amnesty)  
- → Dead (very high mortality)  
- → Mercenary (if professionalize)

See **Appendix C.3: Occupation Emergence Examples** for detailed scenarios of each occupation type.

---

### **2.5.4 Supply/Demand System**

**See Economic Systems - Core, Section 2.5.4 for full economic mechanics.**

**Basic Integration:**
- Occupation attractiveness affected by economic conditions
- Wages, scarcity, opportunity drive occupation choice
- NPCs switch occupations based on market signals (Economic Systems - Enhancements for market-responsive behavior)

---

### **2.5.5 Occupation Satisfaction & Loyalty (Placeholder)**

**Purpose:** Track how happy NPCs are with their current occupation and likelihood of changing careers.

**To be designed:**
- Satisfaction calculation (income, status, safety, personality fit)  
- Loyalty to occupation (commitment level)  
- Dissatisfaction consequences (career changes, unrest)

**Status:** Core concept, detailed mechanics to be implemented based on Economic System integration.

---

### **2.5.6 Career Progression Paths (Placeholder)**

**Purpose:** NPCs can advance within occupations and transition between careers.

**To be designed:**
- Promotion triggers (Tier 1 → Tier 2 → Tier 3)  
- Common career paths (Peasant → Soldier → Knight)  
- Occupation mobility matrix

**Status:** Core concept, detailed mechanics in AI Systems - Enhancements.

---

## **2.6 Need & Goal System**

### **Purpose**

NPCs pursue goals based on unmet needs. Hierarchy of needs determines priority, but personality modifies which needs matter most.

---

### **2.6.1 Modified Maslow Hierarchy**

NPCs have 5 tiers of needs:

#### **TIER 1: SURVIVAL (Most Urgent)**

**Needs:** Food, water, shelter, immediate safety from threats

**If Threatened:**
- ALL other goals suspended  
- Survival becomes sole focus

**Behaviors:**
- Find food by any means (farm, beg, steal)  
- Flee danger immediately  
- Seek protection from powerful  

**Relationship Effects:**
- Will betray others to survive (if Cruel/Cautious)  
- Might sacrifice self for loved ones (if Kind + high Affection)

**Occupation:** Any that provides survival (farmer, servant, bandit, mercenary)

**Satisfaction Threshold:** Food >50% needs met, Shelter exists, No immediate threat

**Economic Integration:** See Economic Systems - Core, Section 7.1 for trade behavior when survival threatened.

---

#### **TIER 2: SECURITY**

**Needs:** Stable income, safe home, predictable life, protection from future threats

**Behaviors:**
- Get steady job  
- Build relationships with powerful for protection  
- Avoid unnecessary risks  
- Save resources

**Occupation:** Stable trades (farmer, craftsman, guard, servant)

**Satisfaction Threshold:** Steady income for 3+ months, Safe location, No major debts

---

#### **TIER 3: BELONGING**

**Needs:** Friends, romance, family, community acceptance, social connections

**Behaviors:**
- Socialize actively  
- Help others to be liked  
- Seek romantic partner  
- Join groups/factions  
- Maintain family bonds

**Relationship Effects:**
- Deepen existing bonds  
- Start romances  
- Mend rifts with estranged friends/family

**Occupation:** Social roles (merchant, priest, entertainer, guild member)

**Satisfaction Threshold:** 3+ friends (Affection >50), Romantic partner (if desired), Community acceptance

---

#### **TIER 4: ESTEEM**

**Needs:** Respect from others, status and recognition, achievement and competence, reputation

**Behaviors:**
- Compete for position  
- Display skills publicly  
- Gain honors and titles  
- Accumulate wealth/power  
- Network with powerful

**Relationship Effects:**
- Network with powerful (Respect >50 relationships)  
- Rival those of equal status  

**Occupation:** Prestigious roles (knight, guild master, noble, wealthy merchant)

**Satisfaction Threshold:** Reputation scores >60, Title or recognized achievement, Respect from peers

---

#### **TIER 5: SELF-ACTUALIZATION**

**Needs:** Legacy and lasting impact, purpose and meaning, personal excellence, ideological fulfillment

**Behaviors:**
- Pursue passions regardless of cost  
- Mentor others (pass on knowledge)  
- Create lasting change  
- Philosophical pursuits  
- Art, invention, revolution

**Relationship Effects:**
- Deep mentorships  
- Philosophical bonds  
- Legacy planning (children, students, monuments)

**Occupation:** Purpose-driven roles (reformer, artist, revolutionary, scholar, master craftsman)

**Satisfaction Threshold:** Achieved something lasting, Created meaningful change, Left legacy

---

### **2.6.2 Personality-Modified Priorities**

**Not everyone pursues needs the same way:**

**Ambitious Characters:**
- Prioritize: Esteem > Belonging  
- Willing to sacrifice friendships for status  
- Never satisfied with Security alone

**Content Characters:**
- Satisfied at: Security or Belonging  
- Don't need Esteem  
- Happy with stable, simple life

**Social Characters:**
- Need Belonging Intensely  
- Suffer greatly without friends (Mood -40)  
- May pursue Belonging even at cost of Security

**Solitary Characters:**
- Can Skip Belonging  
- Comfortable alone  
- Jump from Security → Esteem

**Brave Characters:**
- Willing to risk Security for Esteem  
- Glory over safety

**Cautious Characters:**
- Won't pursue Esteem if Security threatened  
- Safety first, always

**Kind Characters:**
- Belonging includes helping others  
- Satisfaction from friendships AND being helpful

**Cruel Characters:**
- Esteem through domination  
- Respect via fear acceptable

See **Appendix C.1: Personality-Modified Need Priorities** for detailed examples.

---

### **2.6.3 Dynamic Goal Generation**

**Goals emerge from:** Personality + Current Need Level + Relationships + Faction + Occupation

**Goal Generation Algorithm:**

```
1. Identify highest unmet need tier
2. Filter by personality (modify priority)
3. Check relationships (obligations, opportunities)
4. Check faction (faction goals influence personal goals)
5. Generate 1-3 concurrent goals
```

See **Appendix C.2: Goal Generation Examples** for detailed scenarios including:
- Survival-driven goal (starving peasant)
- Esteem-driven goal (ambitious knight)
- Belonging-driven goal (lonely merchant)

---

### **2.6.4 Goal Conflicts**

**When NPC goals conflict with each other or others:**

**Internal Goal Conflict:**

Example: "Advance in faction" (Esteem) vs "Protect friend from faction" (Belonging)

Resolution:
1. Check personality priorities (Ambitious vs Social)
2. Check relationship strength
3. Generate compromise if possible
4. Choose primary goal if forced

**External Goal Conflict:** See Section 2.10 (Conflict Resolution System)

---

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

## **2.10 Conflict Resolution System**

### **Purpose**

When NPC goals collide, the conflict must resolve somehow. Resolution method emerges from personality, power, relationships, and environment.

---

### **2.10.1 Conflict Types**

**RESOURCE CONFLICT:** Both want the same limited thing
- Position, person, land, object

**IDEOLOGICAL CONFLICT:** Different values/beliefs clash
- Progressive vs Traditional, religious orthodoxy vs heresy

**PERSONAL CONFLICT:** Grudge, revenge, rivalry, jealousy
- Past betrayal, romantic jealousy, family feud

**GOAL CONFLICT:** One's goal directly prevents the other's
- One wants war/other wants peace, one hides secret/other wants to reveal

---

### **2.10.2 Resolution Methods (Emergent)**

**Methods emerge from NPC personalities and circumstances:**

#### **AVOIDANCE**
**Conditions:** Cautious personality + Power disadvantage
**Process:** Character backs down, goal abandoned or delayed
**Consequences:** Resentment builds (Affection -10, Mood -15)

#### **CONFRONTATION**
**Conditions:** Brave personality + Similar power levels
**Process:** Challenge issued, outcome determined by power/skill
**Winner:** Respect +20, Power dynamic +30, Goal achieved
**Loser:** Respect -30, Power dynamic -30, Humiliation

#### **COMPROMISE**
**Conditions:** High mutual affection/trust, Rational personalities
**Process:** Discussion, find middle ground
**Consequences:** Neither fully satisfied but relationship strengthens (Trust +10, Respect +10)

#### **MANIPULATION**
**Conditions:** Deceitful personality + Power/knowledge advantage
**Process:** Manipulate victim into serving manipulator's interest
**If Discovered:** Trust -90, Affection -60, Reputation damage

#### **THIRD PARTY MEDIATION**
**Conditions:** Both respect third party, Traditional values
**Process:** Mediator judges, parties decide to accept or defy
**Consequences:** If accept, conflict resolved; If defy, lose faction Respect

#### **VIOLENCE**
**Conditions:** Cruel + Brave, Desperate, Low consequences
**Process:** Physical conflict, outcome based on combat ability
**Winner:** Goal achieved, Reputation (Danger) +30
**Loser:** Trauma, Courage -20, seeks revenge or avoids forever

See **Appendix D: Conflict Resolution Examples** for comprehensive scenarios of each method.

---

### **2.10.3 Outcome Consequences**

**All conflict resolutions affect:**

**Relationships:**
- Winner/manipulator gains power dynamic  
- Loser loses respect, possibly affection  
- Witnesses form opinions

**Goals:**
- Winner: Goal achieved, generate new goal  
- Loser: Goal blocked, find new approach or abandon

**Reputation:**
- Violence increases Danger  
- Manipulation (if discovered) decreases Honor  
- Compromise increases reputation for reasonableness

**Future Conflicts:**
- Past resolutions set patterns  
- NPCs remember what worked  
- Relationships fundamentally changed

---

## **2.11 Civilization-Level Dynamics**

### **Purpose**

Individual NPC decisions aggregate into civilization-level patterns. Healthy civilizations maintain balance; unhealthy ones spiral into dysfunction.

---

### **2.11.1 Occupation Ratios & Health**

**Healthy Civilization Balance:**

| Occupation | Healthy % | Function |
|-----------|----------|----------|
| Farmers | 60-70% | Food production, stability |
| Craftsmen | 10-15% | Goods production, infrastructure |
| Soldiers | 5-10% | Defense without over-militarization |
| Merchants | 5-10% | Trade, wealth circulation |
| Bandits | <2% | Crime controlled, law functional |
| Nobles | <1% | Governance, leadership |
| Others | 3-8% | Servants, laborers, specialized roles |

**Warning Signs:**

| Imbalance | Symptom | Consequences |
|-----------|---------|-------------|
| Farmers <50% | Food shortage | Famine, unrest, death spiral |
| Soldiers >20% | Over-militarization | Economic drain, aggressive policy |
| Bandits >5% | Lawlessness | Trade collapse, state failure |
| Craftsmen <5% | No goods | Infrastructure decay, poverty |

See **Appendix F.2: Civilization Death Spirals** for detailed examples including over-militarization and wise governance cycles.

---

### **2.11.2 Factional Power Balance**

**Power Distribution Effects:**

**One Faction Dominates (>70% influence):**
- Other factions resentful  
- Revolutionary sentiment builds  
- Tyranny OR Benevolent dictatorship (personality dependent)

**Balanced Power (No faction >40%):**
- Cooperation necessary  
- Compromise governance  
- Stability through checks and balances

**Chaotic Fragmentation (Many factions <20%):**
- Constant infighting  
- Weak central authority  
- Vulnerable to external threats

See **Appendix F.3: Faction Power Struggle Examples** for Noble-Merchant conflict scenarios.

---

### **2.11.3 Cultural/Religious Movements**

**How Movements Start:**

```
1. CRISIS creates need
2. CHARISMATIC FIGURE emerges (Tier 3 NPC)
3. MESSAGE resonates with specific personalities
4. FACTION SPLITS or NEW FACTION forms
5. CONFLICT RESOLUTION (any method from Section 2.10)
6. OUTCOME shapes civilization
```

**Pattern:**
- Traditional NPCs resist change  
- Progressive NPCs embrace new ideas  
- Outcome depends on faction power and conflict resolution

See **Appendix F.4: Political Reform Movement Example** for detailed year-by-year progression.

---

### **2.11.4 Population Dynamics**

**Birth/Death Affects Composition:**

**Peace + Prosperity:**
- High birth rate → Young population  
- More Ambitious personalities  
- Pressure for expansion/change

**War + Famine:**
- High death rate → Aging population  
- More Cautious personalities  
- Conservative, risk-averse culture

**Generational Shifts (30-year cycles):**

```
GENERATION 1: FOUNDERS
- Values: Brave, Ambitious, Traditional
- Memories: Hardship, struggle

GENERATION 2: INHERITORS
- Values: Content, Social, Progressive
- Forgets founding lessons

GENERATION 3: CRISIS GENERATION
- Values: Return to Brave, Ambitious
- Relearn lessons of Generation 1
```

**Population Pressure:**
- Overpopulation → Competition, unrest, expansion, war
- Underpopulation → Labor shortage, vulnerable, cultural stagnation

---

# **PART 3: DESIGN RATIONALE**

## **3.1 Emergence Philosophy**

**Why Emergent AI Instead of Scripted Stories?**

**1. Replayability:**
- Scripted: Play once, know all outcomes  
- Emergent: Every playthrough unique

**2. Player Agency:**
- Scripted: Player follows predetermined path  
- Emergent: Player's actions have unpredictable consequences

**3. Scale:**
- Scripted: Must write every possible story (impossible at this scale)  
- Emergent: Systems generate infinite variations

**4. Authenticity:**
- Scripted: NPCs feel like actors following script  
- Emergent: NPCs feel like real people with agency

**5. Development Efficiency:**
- Scripted: Years of writing dialogue and branching paths  
- Emergent: Design robust systems once, stories generate forever

---

## **3.2 Why These Systems Create Stories**

**Personality → Character:**
- Every NPC has distinct character  
- Behavior is consistent but not predictable

**Relationships → Drama:**
- Love, betrayal, loyalty, rivalry emerge naturally  
- Multi-dimensional relationships create complexity  
- Past affects future (memory system)

**Factions → Politics:**
- Noble houses, guilds compete  
- NPCs caught between loyalties  
- Power struggles drive macro-narrative

**Occupations → Social Mobility:**
- Peasant can become king  
- Success and failure feel earned  
- Career paths tell personal stories

**Needs & Goals → Motivation:**
- NPCs have reasons for actions  
- Goals conflict creating natural drama

**Conflicts → Plot:**
- Goals collide naturally  
- Resolution methods create different story arcs  
- Consequences cascade into new conflicts

**Memory → Continuity:**
- NPCs remember and hold grudges  
- Past events inform future behavior  
- Story has weight and consequences

**Reputation → Social Dynamics:**
- Actions have social consequences  
- Fame and infamy spread

**Civilization Dynamics → Epic Scale:**
- Individual stories aggregate into history  
- Dynasties rise and fall

---

## **3.3 Scalability Considerations**

**Why Tiering Works:**

**Performance:**
- 9,000 Tier 1 NPCs: Simple calculations, DOTS batch processing  
- 900 Tier 2 NPCs: Moderate complexity, acceptable overhead  
- 100 Tier 3 NPCs: Full complexity, justify computation cost

**Narrative Focus:**
- Players care most about notable figures  
- Masses provide context and population dynamics  
- Tier 3 NPCs drive stories players remember

**Promotion Creates Stars:**
- Any NPC can become important  
- Player watches nobodies become heroes

**Why Factions Abstract Relationships:**

**Mathematical Impossibility:**
- 10,000 NPCs × 10,000 relationships = 100 million relationships (can't compute)

**Faction System:**
- 10,000 NPCs × 5 factions = 50,000 faction relationships (feasible)

**Best of Both:**
- Tier 1: Faction relationships (abstract, scalable)  
- Tier 2/3: Individual relationships (personal, deep)

---

## **3.4 Expected Emergence Patterns**

**Micro Stories (Individual Level):**
- Betrayals and revenge arcs  
- Rags-to-riches career paths  
- Forbidden romances across faction lines  
- Loyal servants rising through ranks  
- Bandits becoming revolutionaries  
- Tragic deaths cutting short arcs

**Meso Stories (Factional Level):**
- House rivalries spanning generations  
- Guild power struggles  
- Religious schisms and reformations  
- Military coups and counter-coups  
- Merchant oligarchies forming  
- Secret societies manipulating events

**Macro Stories (Civilization Level):**
- Civil wars over succession  
- Cultural golden ages and dark ages  
- Economic booms and depressions  
- Territorial expansion and collapse  
- Generational cycles (strong → weak → strong)  
- Foreign invasions exploiting weakness

**Meta Stories (Player-Influenced):**
- Player intervention creates legends  
- Blessed individuals rising to power  
- Divine miracles changing culture

---

## **3.5 Design Goals & Success Metrics**

**Primary Goals:**

**1. Believability:**
- NPCs feel like real people, not algorithms  
- Behavior consistent with personality  
- Surprising but never random

**Success Metric:** Players describe NPCs as characters with names/personalities

**2. Emergence:**
- Stories arise without scripting  
- No two playthroughs identical  
- Cascading consequences create narratives

**Success Metric:** Players share unique stories developers didn't anticipate

**3. Scale:**
- Thousands of NPCs simulated  
- Performance stays smooth (60 FPS target)  
- Depth where it matters, abstraction where it doesn't

**Success Metric:** 10,000 NPCs at 60 FPS, Tier 2/3 feel fully realized

**4. Player Engagement:**
- Players care about NPCs  
- Players remember stories  
- Players replay to see new outcomes

**Success Metric:** Average playtime >50 hours, high replay rate

**5. Systemic Integrity:**
- Systems interact logically  
- No exploits or degenerate strategies  
- Emergent balance (civilization health matters)

**Success Metric:** Civilizations can thrive or fail based on systemic logic

---

# **APPENDICES**

## **Appendix A: Personality Behavior Examples**

### **A.1: 3-Trait Core Combinations**

| Courage | Loyalty | Ambition | Behavioral Pattern |
|---------|---------|----------|-------------------|
| High (+) | High (+) | High (+) | **Heroic Leader** - Brave loyal servant seeking advancement through honorable deeds |
| High (+) | High (+) | Low (-) | **Steadfast Defender** - Brave and loyal but content, protects without ambition |
| High (+) | Low (-) | High (+) | **Ambitious Warlord** - Brave self-server, switches sides for power |
| Low (-) | High (+) | High (+) | **Ambitious Schemer** - Cautious loyal climber, advances within faction through cunning |
| Low (-) | High (+) | Low (-) | **Dutiful Follower** - Cautious, loyal, content - stable reliable servant |
| Low (-) | Low (-) | High (+) | **Backstabbing Manipulator** - Cautious, self-serving, ambitious - dangerous opportunist |
| Low (-) | Low (-) | Low (-) | **Survival Coward** - Cautious, self-serving, content - hides, flees, survives |

[Additional tables in full document...]

---

## **Appendix B: Relationship Examples**

### **B.1: Emergent Relationship State Table**

| Affection | Respect | Trust | Power | Emergent Label |
|-----------|---------|-------|-------|---------------|
| High (+60) | High (+60) | High (+60) | Equal | **Close Friend** |
| High (+60) | High (+60) | High (+60) + High Attraction | Equal | **Love/Soulmate** |
| Low (<-30) | High (+60) | Low (<30) | Equal | **Respected Rival** |
| Low (<-30) | Low (<-30) | Low (<-30) | Them +50 | **Fear-Based Relationship** |

[Additional examples in full document...]

---

## **Appendix C: Goal Generation Examples**

### **C.1: Personality-Modified Need Priorities**

[Detailed examples of how Ambitious, Cautious, Social, Solitary, Brave, Kind, and Cruel personalities modify need hierarchy...]

### **C.2: Goal Generation Examples**

**Example 1: Starving Peasant (SURVIVAL Need)**

```
NPC: Anna
Personality: Cautious 60, Loyalty -40, Ambition 50
Current State: Starving (SURVIVAL threatened)
Relationships: None significant
Faction: House Varlen (Loyalty 45)

Need: TIER 1 SURVIVAL (food)
Goal Generation:
  - Cautious 60: Avoid risky solutions
  - Low Loyalty: Not bound by morality
  - Faction Loyalty 45: Not high enough to expect help
Generated Goal: "Steal food from wealthy, but carefully"
Behavior: Scout for easy targets, avoid guards, take small amounts
```

[Additional examples in full document...]

---

## **Appendix D: Conflict Resolution Examples**

### **D.1: Interaction Type Examples**

[Detailed scenarios for each interaction type: Friendly Chat, Strategic Conversation, Favor Request, etc...]

### **D.2: Interaction Resolution Examples**

[Step-by-step resolution of interactions with different personality combinations...]

### **D.3: Conflict Resolution Method Examples**

**Avoidance Example:**
[Detailed scenario...]

**Confrontation Example:**
[Detailed scenario...]

**Compromise Example:**
[Detailed scenario...]

**Manipulation Example:**
[Detailed scenario...]

**Third Party Mediation Example:**
[Detailed scenario...]

**Violence Example:**
[Detailed scenario...]

---

## **Appendix E: Memory & Learning Examples**

### **E.1: Recent Betrayal Memory**

```
Event: Character B betrayed Character A's trust
Immediate Effects:
  - Trust in B: -80
  - Affection in B: -50
  - Memory created (emotional_weight: 95, permanent)

Long-Term Behavior Changes:
  1. A becomes cautious around B forever
  2. A becomes slightly more cautious toward similar NPCs
  3. If A is Social: Shares betrayal story
  4. If A is Brave + Cruel: New goal "Revenge on B"
  5. If A is Cautious + Kind: Avoids B but doesn't seek revenge
```

[Additional memory examples in full document...]

---

## **Appendix F: Emergence Pattern Examples**

### **F.1: Faction Conflict Examples**

[Detailed scenarios of faction events affecting individuals and vice versa...]

### **F.2: Civilization Death Spirals**

**Over-Militarization Death Spiral:**

```
Year 1: External threat → King recruits heavily
        Soldiers: 10% → 20%

Year 2: Too many soldiers taken from farms
        Farmers: 65% → 55%
        Food production: -15%

Year 3: Famine begins
        Desperate peasants → Bandits (survival)
        Bandits: 2% → 8%

Year 4: Need more soldiers to fight bandits
        Soldiers: 20% → 30%
        Even fewer farmers: 55% → 45%

Year 5: Mass starvation, total collapse
```

**Wise Governance Cycle:**

```
Year 1: Drought threatens → King opens granaries
Year 2: Merchants import food → Crisis averted
Year 3: Farmers stable, peasants grateful
Year 4: Prosperity returns
Year 5: Golden age
```

[Additional patterns in full document...]

---

## **Appendix G: Quick Reference Tables**

### **G.1: Personality Trait Effects Summary**

| Trait | High (+) | Low (-) |
|-------|----------|---------|
| **Courage** | Confronts threats, takes risks | Avoids conflict, flees danger |
| **Loyalty** | Keeps oaths, follows faction | Betrays easily, opportunist |
| **Ambition** | Seeks power/status, restless | Content with station, peaceful |
| **Kind** | Helps others, forgives | Exploits weakness, cruel |
| **Honest** | Keeps word, direct | Lies easily, manipulates |
| **Rational** | Logic-driven, calculating | Feeling-driven, impulsive |
| **Traditional** | Follows customs, respects hierarchy | Challenges norms, progressive |
| **Social** | Needs company, talkative | Needs solitude, quiet |

---

### **G.2: Relationship Dimension Effects**

| Dimension | Effect on Behavior |
|-----------|-------------------|
| **Affection** | Time spent together, help willingness, forgiveness |
| **Respect** | Follow their lead, listen to advice, emulate |
| **Trust** | Share secrets, vulnerability, rely on promises |
| **Attraction** | Romantic pursuit, jealousy, chemistry |
| **Power** | Who dominates conflicts, who submits |

---

### **G.3: Need Hierarchy Quick Reference**

| Tier | Need | Satisfied When | Behaviors |
|------|------|---------------|-----------|
| 1 | Survival | Food >50%, Shelter, No threat | Find food, flee danger |
| 2 | Security | Steady income 3+ months, Safe location | Get steady job, avoid risks |
| 3 | Belonging | 3+ friends, Partner, Acceptance | Socialize, join groups |
| 4 | Esteem | Reputation >60, Title, Respect | Compete, display skills |
| 5 | Self-Actualization | Lasting achievement, Legacy | Pursue passions, mentor |

---

### **G.4: Conflict Resolution Method Selection**

| Personality Combination | Typical Resolution |
|------------------------|-------------------|
| Cautious + Power Disadvantage | Avoidance |
| Brave + Similar Power | Confrontation |
| High Affection/Trust + Rational | Compromise |
| Deceitful + Power Advantage + Private | Manipulation |
| Respect Mediator + Traditional | Third Party |
| Cruel + Brave + Desperate | Violence |

---

**END OF DOCUMENT**

---

## **Document Revision History**

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-01-XX | Initial AI Systems - Core document created, split from combined document |

---

**Related Documents:**
- **AI Systems - Enhancements:** Detailed promotion system, future systems integration, polish features
- **Economic Systems - Core:** Economic behavior integration, trade mechanics
- **Economic Systems - Enhancements:** Future economic features

**For Implementation Questions:** Reference appendices for detailed examples. See Enhancement document for advanced features.