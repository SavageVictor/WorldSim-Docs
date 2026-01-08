---
layout: default
title: Occupation System
parent: AI Systems
grand_parent: Documentation
nav_order: 6
---

**Related Documents:**
- AI Systems - Enhancements (future features)
- Economic Systems - Core (economic behavior integration)
- Economic Systems - Enhancements (future economic features)


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

