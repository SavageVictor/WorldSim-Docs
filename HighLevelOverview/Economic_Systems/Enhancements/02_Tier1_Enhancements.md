---
layout: default
title: Tier 1 Enhancements
parent: Enhancements
grand_parent: Economic Systems
nav_order: 2
---

**Related Documents:**
- Economic Systems - Core (MVP) (foundational systems)
- AI Systems - Core (AI behavior integration)
- AI Systems - Enhancements (future AI features)
- [Future] Resource Encyclopedia (detailed resource specs)


# **PART 2: TIER 1 ENHANCEMENTS**

## **2.1 Market-Responsive Production**

**Status:** 🟡 Enhancement - Tier 1  
**Complexity:** Medium  
**Value:** High  
**Timeline:** 3-4 months post-MVP

### **Purpose**

NPCs observe market conditions and adjust what they produce based on scarcity and prices, creating boom-bust cycles and market equilibration.

**Current State (Core):**
- Farmers grow wheat (70%), vegetables (20%), animals (10%) - fixed assignment
- Craftsmen produce generalist goods - simple heuristic
- Extractors extract their resource type - no decisions

**Enhanced State:**
- Farmers observe wheat vs vegetable prices, switch crops next season
- Craftsmen prioritize high-demand goods
- Production decisions emerge from market observation

---

### **Mechanics**

**Step 1: Market Observation**

NPCs at market observe:
- **Supply:** How many sellers have resource X?
- **Demand:** How many buyers asking for resource X?
- **Price:** What price is resource X selling for?

**Observation Data Structure:**
```
NPC {
  market_observations: Map {
    "wheat": {
      sellers_count: 15,        // Counted at market
      buyers_count: 30,         // Counted at market
      average_price: 2.8,       // Observed transactions
      scarcity: 2.0             // buyers/sellers ratio
    },
    "vegetables": {
      sellers_count: 5,
      buyers_count: 8,
      average_price: 5.2,
      scarcity: 1.6
    }
  }
}
```

**Update Frequency:**
- NPCs at market update observations weekly
- Stores last 4 weeks of data (rolling average)

---

**Step 2: Production Decision**

**For Farmers (Seasonal Decision):**

At end of harvest season, farmer evaluates:

```
Calculate profit potential for each crop:
  
Wheat profit = (yield × price) - (seed_cost + labor_time)
Vegetable profit = (yield × price) - (seed_cost + labor_time)
Animal profit = (yield × price) - (feed_cost + labor_time)

Compare:
  If (vegetable_profit > wheat_profit × 1.3):
    // 30% premium required to switch (switching cost)
    Next season: Grow vegetables
  Else:
    Continue wheat
```

**Personality Modifiers:**
- **Rational:** Calculates precisely, switches if >20% profit gain
- **Traditional:** Resists switching, requires >50% profit gain ("My family always grew wheat")
- **Cautious:** Requires >40% profit gain AND 2+ seasons of high prices (fear volatility)
- **Ambitious:** Switches aggressively at >10% profit gain

---

**For Craftsmen (Weekly Decision):**

Craftsman observes demand at market:

```
Items with high demand (many buyers, few sellers):
  - Tools: 20 buyers, 3 sellers → Scarcity 6.7
  - Weapons: 5 buyers, 1 seller → Scarcity 5.0
  - Goods: 10 buyers, 8 sellers → Scarcity 1.25

Priority this week:
  1. Tools (highest scarcity)
  2. Weapons (second highest)
  3. Goods (lowest)

Craftsman focuses on tools this week
```

**Material Availability Check:**
- Can only craft what materials are available
- If materials scarce for high-demand item → Craft second choice

---

### **Emergent Boom-Bust Cycles**

See **Appendix A: Market-Responsive Production Examples** for:
- A.1: Vegetable Boom-Bust Cycle
- A.2: Tool Market Equilibration
- A.3: Cascading Production Shifts

**Key Emergent Patterns:**
- Overshooting (everyone switches at once)
- Market correction (prices crash, people switch back)
- Equilibration (oscillates toward balance)
- Information lag (decisions based on past, not future)

---

### **Implementation Requirements**

**Data Tracking:**
- Market observation counters (sellers/buyers per resource)
- Price history (rolling 4-week average)
- Production decision timers (seasonal for farmers, weekly for craftsmen)

**Performance:**
- Only NPCs who visit market update observations
- Calculations once per decision period (not every tick)
- Tier 1 NPCs use simplified calculations

**Balancing:**
- Switching cost thresholds (prevent constant flip-flopping)
- Personality variation (not everyone responds same)
- Material constraints (can't switch if no materials)

---

## **2.2 Dynamic Pricing System**

**Status:** 🟡 Enhancement - Tier 1  
**Complexity:** Medium  
**Value:** High  
**Timeline:** 2-3 months post-MVP

### **Purpose**

Prices fluctuate based on observed supply and demand at markets, creating realistic economic signals that drive NPC behavior.

**Current State (Core):**
- Baseline prices fixed per resource
- Simple modifiers (Ambitious seller +20%, Desperate -20%)
- No market-wide price changes

**Enhanced State:**
- Market-wide prices adjust based on scarcity
- Local price variations (Village A vs Village B)
- Price signals drive production decisions (prerequisite for Market-Responsive Production)

---

### **Mechanics**

**Price Calculation Formula:**

```
Current_Price = Baseline_Price × Scarcity_Multiplier × Local_Modifier

Where:
  Scarcity_Multiplier = Demand / Supply
  
  If Scarcity < 0.8:  (Oversupply)
    Multiplier = 0.5 to 0.8
  
  If Scarcity 0.8-1.2: (Balanced)
    Multiplier = 0.9 to 1.1
  
  If Scarcity > 1.2: (Shortage)
    Multiplier = 1.2 to 3.0+
```

**Supply/Demand Measurement:**

At each market, track:
```
Market_Data {
  supply: Sum of all units available at seller stalls
  demand: Sum of all buyers seeking this resource
  
  Example:
    Wheat supply: 500 units (from 15 sellers)
    Wheat demand: 800 units (30 buyers want wheat)
    Scarcity = 800/500 = 1.6 (SHORTAGE)
    Price_Multiplier = 1.6
    Wheat_Price = 3 coins × 1.6 = 4.8 coins per 10 units
}
```

**Update Frequency:**
- Recalculate once per market day
- Uses rolling 3-day average (smooths volatility)

---

### **Local Price Variations**

Different markets have different prices based on local conditions:

```
Village A (agricultural):
  Wheat supply: HIGH (local farmers produce)
  Wheat price: 2.5 coins (LOW, oversupply)
  Tools supply: LOW (few craftsmen)
  Tools price: 22 coins (HIGH, scarcity)

Village B (industrial):
  Wheat supply: LOW (few farmers)
  Wheat price: 5 coins (HIGH, scarcity)
  Tools supply: HIGH (many craftsmen)
  Tools price: 12 coins (LOW, abundant)

Result: ARBITRAGE OPPORTUNITY
  Merchants buy wheat at 2.5 in A, sell at 5 in B
  Merchants buy tools at 12 in B, sell at 22 in A
  Price differences drive trade!
```

See **Appendix B: Dynamic Pricing Examples** for detailed scenarios including:
- B.1: Famine Price Spike
- B.2: Regional Price Differences
- B.3: Price Equilibration Over Time

---

### **Seller Pricing Behavior**

NPCs set prices based on market price + personality:

```
Market_Price = 4.8 coins (calculated from scarcity)

Seller personalities:
  Honest: Sets exactly market price (4.8)
  Ambitious: Sets 10-20% above (5.3-5.8)
  Cautious: Sets 5% below if desperate to sell (4.6)
  Deceitful: May set much higher, hoping buyer doesn't know (6.0+)
```

**Buyer Response:**
- Rational buyers compare prices between sellers
- Cautious buyers accept first reasonable offer
- Social buyers prefer acquaintances even if higher price

---

### **Integration with Market-Responsive Production**

```
High wheat prices (scarcity) 
  → Farmers observe "Wheat is profitable!"
  → More farmers grow wheat
  → Wheat supply increases
  → Wheat price drops
  → Farmers switch to vegetables (now more profitable)
  → Cycle continues
```

**Dependency:** Market-Responsive Production REQUIRES Dynamic Pricing to function properly.

---

### **Implementation Requirements**

**Data Tracking:**
- Supply/demand counters per market per resource
- Price history (rolling averages)
- Market-specific pricing (not civilization-wide)

**Performance:**
- Calculate once per market day (not every transaction)
- Cache prices, update periodically
- Tier 1 NPCs use market average (don't calculate individually)

**Balancing:**
- Price volatility limits (max 3× baseline, min 0.5× baseline)
- Smoothing (rolling averages prevent wild swings)
- Personality variation (not everyone responds to price signals)

---

## **2.3 Negotiation System**

**Status:** 🟡 Enhancement - Tier 1  
**Complexity:** High  
**Value:** Medium  
**Timeline:** 3-4 months post-MVP

### **Purpose**

Buyers and sellers haggle over prices, creating dynamic interactions, relationship effects, and personality-driven trade outcomes.

**Current State (Core):**
- Seller sets price
- Buyer accepts or declines
- No back-and-forth

**Enhanced State:**
- Multi-turn negotiation
- Offers and counter-offers
- Personality-driven strategies
- Relationship effects (Trust, Respect, Affection)

---

### **Mechanics**

**Negotiation Flow:**

```
1. OPENING OFFER
   Seller: "10 wheat for 5 coins"
   
2. BUYER RESPONSE
   Option A: Accept immediately (if fair)
   Option B: Counter-offer
   Option C: Walk away
   
3. COUNTER-OFFER (if Option B)
   Buyer: "I'll pay 3 coins"
   
4. SELLER RESPONSE
   Option A: Accept
   Option B: Counter-counter-offer
   Option C: Refuse, end negotiation
   
5. REPEAT until agreement or impasse (max 5 rounds)
```

**Personality-Driven Strategies:**

See **Appendix C: Negotiation Examples** for detailed scenarios including:
- C.1: Honest vs Honest (quick agreement)
- C.2: Ambitious vs Rational (calculated haggling)
- C.3: Deceitful Manipulation
- C.4: High-Trust Relationship (flexible terms)

---

**Opening Offer Strategy:**

| Seller Personality | Opening Offer |
|--------------------|---------------|
| **Honest** | Baseline price (fair) |
| **Ambitious** | +20-30% above baseline (wants profit) |
| **Cautious** | -10% below baseline (wants quick sale) |
| **Deceitful** | +50%+ (tests buyer) |
| **Rational** | Baseline + market scarcity multiplier |

**Counter-Offer Strategy:**

| Buyer Personality | Counter-Offer |
|-------------------|---------------|
| **Honest** | Fair price based on need |
| **Ambitious** | -30-40% below asking (aggressive) |
| **Cautious** | Accept first reasonable offer (avoid conflict) |
| **Deceitful** | Lies about budget, claims poverty |
| **Rational** | Calculates fair price, offers that |

---

### **Relationship Effects**

**If both have tracked relationship (Tier 2/3):**

```
High Trust (>60):
  - Both more flexible
  - Accept reasonable offers quickly
  - May offer credit ("Pay me later")
  
Low Trust (<20):
  - Demand full payment upfront
  - Suspicious of offers
  - Hard negotiation
  
High Affection (>60):
  - May give discount to friend
  - "For you, 4 coins instead of 5"
  
Low Affection (<-20):
  - May charge premium
  - "For you? 6 coins"
```

**Negotiation Outcome Affects Relationship:**

```
Fair deal (both satisfied):
  Affection +5, Trust +5, Respect +5
  
Hard negotiation (one feels exploited):
  Winner: Respect +10 (got better deal)
  Loser: Affection -10, Trust -5 (feels taken advantage of)
  
Scammed (deception discovered later):
  Trust -50, Affection -30, relationship damaged
```

---

### **Negotiation Outcomes**

**SUCCESS: Agreement Reached**
- Both parties accept final offer
- Trade proceeds
- Relationship updated

**FAILURE: Impasse**
- Neither willing to compromise further
- Trade cancelled
- Buyer may try other sellers
- Seller may try other buyers

**FAILURE: Walk Away**
- One party refuses to negotiate
- Relationship may be damaged (if insulting)
- Both move on

---

### **Implementation Requirements**

**Data Tracking:**
- Negotiation state machine (track current offer, round count)
- Personality-driven decision trees
- Relationship integration (Trust, Affection effects)

**Performance:**
- Negotiation only for significant trades (>10 coins)
- Small trades skip negotiation (too expensive computationally)
- Tier 1 NPCs use simplified negotiation (1-2 rounds max)

**Balancing:**
- Negotiation time limits (5 rounds max, prevent infinite loops)
- Personality variation (not everyone negotiates same)
- Relationship thresholds (when to be flexible)

---

## **2.4 Resource Spoilage & Decay**

**Status:** 🟡 Enhancement - Tier 1  
**Complexity:** Medium  
**Value:** Medium  
**Timeline:** 2-3 months post-MVP

### **Purpose**

Resources deteriorate over time, creating urgency to trade/consume, preventing infinite hoarding, and making storage management critical.

**Current State (Core):**
- Resources never spoil
- NPCs can hoard indefinitely
- No urgency to sell

**Enhanced State:**
- Food spoils over weeks/months
- Tools degrade with use
- Storage quality matters
- Urgency drives trade behavior

---

### **Mechanics**

**Spoilage Rates:**

| Resource | Spoilage Time | Storage Extension | Notes |
|----------|---------------|-------------------|-------|
| **Wild Food** | 1 week | +1 week in home storage | Berries, foraged items |
| **Crops (Wheat)** | 2 months | +2 months in barn | Grain can be stored longer |
| **Prepared Food** | 3 days | +4 days in cold storage | Cooked meals |
| **Wood** | Never | - | Doesn't spoil |
| **Stone** | Never | - | Doesn't spoil |
| **Ore** | Never | - | Doesn't spoil |

**Tool Degradation:**

```
Tool {
  durability: 100 (starts at 100)
  
  Each use: durability -= 1
  
  At durability 0: Tool breaks, must be replaced
}

Average tool lifespan: 100 uses = ~1 year of farming
```

---

### **Spoilage Detection:**

```
Every day (game time):
  For each food item in NPC inventory/storage:
    age++
    
    If age > spoilage_time:
      Item spoils → Removed from inventory
      NPC mood -10 (wasted food!)
```

**Visual Indicators:**
- Food items change color as they age (fresh → old → rotten)
- Tooltip shows "Spoils in 3 days"
- NPCs react visually when food spoils (disappointment animation)

---

### **Behavioral Effects**

**Urgency to Sell:**

```
Farmer has 100 wheat harvested
Wheat spoils in 2 months

Week 1-4: Normal selling behavior
Week 5-6: "Wheat will spoil soon, must sell!"
  → Lower prices (desperate)
  → More frequent market trips
Week 7-8: "Almost spoiled!"
  → Sells at any price
  → May give away to friends (better than wasting)
Week 8+: Wheat spoils if unsold
```

**Storage Management:**

```
NPC evaluates storage:
  
If perishable goods > 50% of storage:
  → "Too much food, need to sell or it'll spoil"
  → Prioritize selling perishables
  
If tools breaking frequently:
  → "Need to buy replacement tools"
  → Increases demand for craftsmen
```

---

### **Economic Effects**

**Prevents Infinite Hoarding:**
- NPCs can't stockpile thousands of wheat indefinitely
- Creates natural upper limit on wealth (perishables)
- Forces active trading economy

**Creates Urgency:**
- Time pressure drives market activity
- Desperate sellers create buyer opportunities
- Price variations increase (spoilage urgency)

**Seasonal Dynamics:**
- Harvest season (fall): Massive supply, low prices
- Winter: Food scarce, high prices (spoiled or eaten)
- Spring: Pre-harvest shortage, highest prices

**Tool Economy:**
- Constant tool demand (degradation)
- Craftsmen have steady customers
- Tool scarcity more impactful (can't hoard extras)

---

### **Implementation Requirements**

**Data Tracking:**
- Age timestamp for each food item
- Durability counter for each tool
- Storage quality modifiers

**Performance:**
- Daily spoilage check (not every tick)
- Batch processing for Tier 1 NPCs (check class averages)
- Only track perishables (skip wood/stone/ore)

**Balancing:**
- Spoilage rates must allow trade (not instant rot)
- Tool durability balanced to create demand without being annoying
- Storage upgrades provide meaningful extension