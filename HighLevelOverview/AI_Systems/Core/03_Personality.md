---
layout: default
title: Personality System
parent: Core Systems
grand_parent: AI Systems
nav_order: 3
---

**Related Documents:**
- AI Systems - Enhancements (future features)
- Economic Systems - Core (economic behavior integration)
- Economic Systems - Enhancements (future economic features)


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

