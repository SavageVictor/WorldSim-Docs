---
layout: default
title: Faction System
parent: Core Systems
grand_parent: AI Systems
nav_order: 5
---

**Related Documents:**
- AI Systems - Enhancements (future features)
- Economic Systems - Core (economic behavior integration)
- Economic Systems - Enhancements (future economic features)


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

