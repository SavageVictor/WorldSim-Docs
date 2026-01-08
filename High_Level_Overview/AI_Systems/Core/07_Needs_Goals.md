---
layout: default
title: Need & Goal System
parent: Core Systems
grand_parent: AI Systems
nav_order: 7
---

**Related Documents:**
- AI Systems - Enhancements (future features)
- Economic Systems - Core (economic behavior integration)
- Economic Systems - Enhancements (future economic features)


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

