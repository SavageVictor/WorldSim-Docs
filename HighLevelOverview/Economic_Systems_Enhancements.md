# **Economic Systems - Enhancements (Future)**

**Version:** 1.0  
**Last Updated:** 2025-01-XX  
**Document Type:** Enhancement Specification  
**Target Audience:** Development Team  
**Status:** Post-MVP Features

**Related Documents:**
- Economic Systems - Core (MVP) (foundational systems)
- AI Systems - Core (AI behavior integration)
- AI Systems - Enhancements (future AI features)
- [Future] Resource Encyclopedia (detailed resource specs)

---

## **Table of Contents**

### **PART 1: OVERVIEW**
1.1 Enhancement Philosophy  
1.2 Priority Tiers  
1.3 Dependencies

### **PART 2: TIER 1 ENHANCEMENTS (High Priority)**
2.1 Market-Responsive Production  
2.2 Dynamic Pricing System  
2.3 Negotiation System  
2.4 Resource Spoilage & Decay

### **PART 3: TIER 2 ENHANCEMENTS (Medium Priority)**
3.1 Barter System  
3.2 Gossip Accuracy Degradation  
3.3 Trade Reputation & Scamming  
3.4 Personality-Driven Consumption  
3.5 Memory Decay for Supplier Knowledge

### **PART 4: TIER 3 ENHANCEMENTS (Polish)**
4.1 Emergent Currency Types  
4.2 Advanced Information Spread System  
4.3 Employment & Wage System  
4.4 Investment & Banking  
4.5 Trade Routes & Caravans  
4.6 Economic Policies & Regulations

### **PART 5: IMPLEMENTATION GUIDANCE**
5.1 When to Implement Each Enhancement  
5.2 Testing Requirements  
5.3 Integration Challenges

### **APPENDICES**
A. Market-Responsive Production Examples  
B. Dynamic Pricing Examples  
C. Negotiation Examples  
D. Barter Examples  
E. Advanced Systems Examples

---

# **PART 1: OVERVIEW**

## **1.1 Enhancement Philosophy**

**Build on Solid Core**

Enhancements add depth and realism to the core economic systems but are not required for a functional, emergent economy. They should be implemented only after core systems are proven stable and performant.

**Key Principles:**

**1. Core First, Depth Later**
- MVP must work without enhancements
- Enhancements refine, don't replace
- Each enhancement standalone (can implement independently)

**2. Incremental Complexity**
- Add one enhancement at a time
- Test thoroughly before adding next
- Monitor performance impact

**3. Optional Features**
- Players/designers can enable/disable certain enhancements
- Not all enhancements necessary for all playstyles
- Modular implementation

**4. Maintain Emergence**
- Enhancements should increase emergence, not script behavior
- Avoid creating "correct" strategies
- Preserve player discovery

---

## **1.2 Priority Tiers**

### **TIER 1: High Priority (Implement First)**

**Timeline:** 3-6 months post-MVP

**Features:**
- Market-Responsive Production (makes economy more dynamic)
- Dynamic Pricing (realistic market behavior)
- Negotiation System (deeper player/NPC interaction)
- Resource Spoilage (prevents infinite hoarding)

**Why High Priority:**
- High value-to-complexity ratio
- Significantly improve realism
- Create more interesting economic stories
- Relatively contained systems

---

### **TIER 2: Medium Priority (Implement Second)**

**Timeline:** 6-12 months post-MVP

**Features:**
- Barter System (currency alternative)
- Gossip Accuracy Degradation (information realism)
- Trade Reputation & Scamming (relationship depth)
- Personality-Driven Consumption (behavior variety)
- Memory Decay for Supplier Knowledge (realism)

**Why Medium Priority:**
- Moderate value-to-complexity ratio
- Add polish and depth
- Not essential but improve experience
- More complex implementation

---

### **TIER 3: Polish (Implement Last, Optional)**

**Timeline:** 12+ months post-MVP

**Features:**
- Emergent Currency Types (very complex)
- Advanced Information Spread (dedicated system)
- Employment & Wage System (labor market)
- Investment & Banking (capital markets)
- Trade Routes & Caravans (infrastructure)
- Economic Policies & Regulations (faction integration)

**Why Low Priority:**
- High complexity
- Low immediate value (nice-to-have)
- May not be worth development cost
- Major features requiring extensive design

---

## **1.3 Dependencies**

**Enhancement Dependencies:**

```
Core Systems (MVP) REQUIRED for ALL enhancements
    ↓
TIER 1 ENHANCEMENTS
    ├─ Market-Responsive Production → Requires: Dynamic Pricing
    ├─ Dynamic Pricing → Standalone
    ├─ Negotiation System → Standalone
    └─ Resource Spoilage → Standalone
    
TIER 2 ENHANCEMENTS
    ├─ Barter System → Requires: Currency System (core)
    ├─ Gossip Accuracy → Requires: Information Spread (core)
    ├─ Trade Reputation → Requires: Reputation System (AI Systems - Core, Section 2.9)
    ├─ Personality Consumption → Requires: Personality System (core)
    └─ Memory Decay → Requires: Acquaintance Network (core)
    
TIER 3 ENHANCEMENTS
    ├─ Emergent Currency → Requires: Faction System, Trade Routes
    ├─ Advanced Info Spread → Requires: All info systems
    ├─ Employment System → Requires: Dynamic Pricing, Faction System
    ├─ Investment/Banking → Requires: Employment, Wealth accumulation
    ├─ Trade Routes → Requires: Market-Responsive Production, Dynamic Pricing
    └─ Economic Policies → Requires: Faction System, Political power
```

**Implementation Order Recommendation:**
1. Core Systems (see Core document)
2. Dynamic Pricing (Tier 1)
3. Negotiation System (Tier 1)
4. Resource Spoilage (Tier 1)
5. Market-Responsive Production (Tier 1)
6. Tier 2 enhancements (as needed)
7. Tier 3 enhancements (optional)

---

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

---

# **PART 3: TIER 2 ENHANCEMENTS**

## **3.1 Barter System**

**Status:** 🟡 Enhancement - Tier 2  
**Complexity:** High  
**Value:** Low-Medium  
**Timeline:** 5-6 months post-MVP

### **Purpose**

NPCs trade goods directly without currency, evaluating "Is X worth Y to me?" based on personal needs, creating alternative economic system.

**When Relevant:**
- Currency scarce (economic crisis)
- Primitive civilizations (early game)
- Remote regions (currency doesn't reach)
- Player preference (disable currency)

---

### **Mechanics**

**Barter Evaluation:**

```
Farmer Marcus has: 50 wheat
Craftsman Elena has: 3 tools

Elena approaches Marcus:
  "I'll trade 1 tool for 20 wheat"

Marcus evaluates:
  My value for their item (tool):
    - Need urgency: HIGH (profession requirement)
    - Baseline value: 15 coins
    - Personal value: 25 coins (I NEED this)
  
  My value for my item (20 wheat):
    - Baseline value: 6 coins (20 wheat × 0.3 coins each)
    - Personal value: 4 coins (I have surplus, worth less to me)
  
  Comparison:
    Tool worth 25 to me
    20 wheat worth 4 to me
    25 > 4 → ACCEPT (I gain more than I lose)

Marcus: "Deal!"
```

See **Appendix D: Barter Examples** for detailed scenarios including:
- D.1: Successful Barter (Mutual Benefit)
- D.2: Failed Barter (Unequal Value)
- D.3: Multi-Item Barter
- D.4: Barter Chain

---

### **Personal Valuation**

**How NPCs Value Items:**

```
Item_Value = Baseline_Value × Need_Multiplier × Scarcity_Multiplier

Need_Multiplier (AI Systems - Core, Section 2.6):
  SURVIVAL need (starving): 5-10× (food is CRITICAL)
  SECURITY need: 2-3× (tools are important)
  BELONGING need: 1-2× (gifts matter somewhat)
  ESTEEM need: 0.5-1× (luxuries nice but not urgent)

Scarcity_Multiplier:
  Have 0 of item: 3× (desperately need)
  Have 1-2: 1.5× (want backup)
  Have 3+: 0.5× (surplus, worth less)
```

**Example:**

```
Starving NPC evaluates food:
  Baseline: 5 coins per 10 food
  Need: SURVIVAL (10× multiplier)
  Scarcity: Has 0 food (3× multiplier)
  Personal Value: 5 × 10 × 3 = 150 coins equivalent
  
Result: Will trade ANYTHING affordable for food
```

---

### **Barter Negotiation**

```
1. INITIAL OFFER
   Elena: "1 tool for 20 wheat"

2. EVALUATION
   Marcus: Tool worth 25, Wheat worth 4
   Marcus thinks: "Unfair to me, but I need the tool"
   Decision: COUNTER-OFFER

3. COUNTER-OFFER
   Marcus: "1 tool for 10 wheat"
   
4. ELENA EVALUATION
   Elena: Tool worth 15 (baseline, not urgent), 10 wheat worth 3
   Elena thinks: "Still profitable, but I wanted more"
   Decision: SPLIT DIFFERENCE

5. COMPROMISE
   Elena: "15 wheat, final offer"
   Marcus: Tool 25, 15 wheat worth 6
   Marcus: 25 > 6 → ACCEPT
   
6. TRADE EXECUTED
   Marcus: -15 wheat, +1 tool
   Elena: -1 tool, +15 wheat
```

---

### **Emergent Patterns**

**Barter Chains:**

```
Marcus (wheat) → Elena (tool) → Thomas (ore) → Sarah (weapon)

Marcus needs weapon (indirectly):
  1. Trades wheat to Elena for tool
  2. Trades tool to Thomas for ore
  3. Trades ore to Sarah for weapon
  
Multi-step barter creates trade network!
```

**Barter Inefficiency:**
- Requires "double coincidence of wants" (Marcus has what Elena wants AND vice versa)
- Currency more efficient (universal medium)
- Barter emerges when currency fails

**Currency Re-Emergence:**
- If barter too inefficient, NPCs may create currency substitute
- "Everyone wants salt, so I'll trade for salt to use as money"
- Leads to emergent currency types (Tier 3 enhancement)

---

### **Implementation Requirements**

**Data Tracking:**
- Personal valuation calculations per NPC
- Need multipliers (from AI Doc 2.6)
- Scarcity tracking per NPC inventory
- Barter negotiation state machine

**Performance:**
- Complex calculations (only for significant trades)
- Tier 1 NPCs use simplified barter (accept/reject only, no negotiation)
- Cache valuations (don't recalculate every tick)

**Balancing:**
- Personal valuation formulas must be fair but varied
- Barter should be less efficient than currency (to justify currency use)
- Personality affects barter willingness

---

## **3.2 Gossip Accuracy Degradation**

**Status:** 🟡 Enhancement - Tier 2  
**Complexity:** Medium  
**Value:** Low  
**Timeline:** 4-5 months post-MVP

### **Purpose**

Information becomes less accurate with distance in gossip chains, creating realistic "telephone game" effect and information friction.

**Current State (Core):**
- Gossip spreads perfectly (no degradation)
- "Thomas has ruby" remains accurate across 100 NPCs

**Enhanced State:**
- Direct witnesses: 100% accurate
- 1 hop: 90% accurate (minor details lost)
- 2 hops: 70% accurate (vague)
- 3+ hops: 50% accurate (unreliable rumors)

---

### **Mechanics**

**Accuracy Degradation:**

```
Direct Witness (0 hops):
  Information: "Thomas the merchant has a ruby worth 500 coins at the city market"
  Accuracy: 100%

1 Hop Away (heard from witness):
  Information: "I heard Thomas has a ruby, very valuable, at the market"
  Accuracy: 90%
  Lost: Exact price, Thomas's profession

2 Hops Away (heard from someone who heard):
  Information: "Someone said there's a ruby somewhere in the city"
  Accuracy: 70%
  Lost: Thomas's name, exact location, value estimate

3 Hops Away (third-hand):
  Information: "I think there's a valuable gem, not sure who has it"
  Accuracy: 50%
  Lost: Type of gem, seller identity
```

---

### **Implementation**

**Information Packet:**

```
Gossip_Info {
  core_fact: "Thomas has ruby"
  details: {
    seller_name: "Thomas" (accuracy: 100%)
    item_type: "ruby" (accuracy: 100%)
    value: 500 (accuracy: 90%)
    location: "city market" (accuracy: 80%)
  }
  hop_count: 2
  
  Degradation per hop:
    detail_accuracy -= 10% per hop
    If accuracy < 50%: Detail may be forgotten
}
```

**Propagation:**

```
Marcus (witness) tells Sarah:
  Sarah receives: Accuracy 90% (1 hop)
  Sarah.gossip_info["ruby"].hop_count = 1

Sarah tells John:
  John receives: Accuracy 80% (2 hops)
  John.gossip_info["ruby"].hop_count = 2
  Some details lost (value becomes "very expensive" instead of "500 coins")
```

---

### **Behavioral Effects**

**Distant NPCs Have Vague Information:**

```
NPC 3 hops away:
  "I heard there's a ruby somewhere"
  
Behavior:
  1. Travel to city (knows general area)
  2. Arrive at market
  3. Ask around: "Who has the ruby?"
  4. Directed to Thomas by locals (they know precisely)
  5. Find Thomas, complete trade

Result: Information friction creates delays, not impossibility
```

**Rumors vs Facts:**

```
Close to source: Facts (high accuracy)
Far from source: Rumors (low accuracy)

NPCs distinguish:
  High accuracy (>80%): "I know Thomas has a ruby"
  Low accuracy (<60%): "I heard a rumor about a ruby"
```

---

### **Implementation Requirements**

**Data Tracking:**
- Hop count per gossip packet
- Accuracy degradation per detail
- Personality effects (Honest spreads more accurately, Deceitful distorts)

**Performance:**
- Only track accuracy for high-value gossip (>100 coins)
- Low-value info doesn't need accuracy tracking
- Batch updates during gossip spread

**Balancing:**
- Degradation rate (10% per hop feels realistic)
- Minimum accuracy (50%, never complete misinformation)
- Personality variation (Social NPCs spread faster but less accurately)

---

## **3.3 Trade Reputation & Scamming**

**Status:** 🟡 Enhancement - Tier 2  
**Complexity:** High  
**Value:** Medium  
**Timeline:** 5-6 months post-MVP

### **Purpose**

Deceitful NPCs can scam customers, damaging reputation when discovered, creating trust dynamics and economic risk.

**Current State (Core):**
- Trades are honest (no scamming)
- Prices may vary but quality is standard

**Enhanced State:**
- Deceitful sellers overcharge, sell defective goods
- Buyers may discover scam later
- Reputation damaged, customers lost
- Creates risk/reward for dishonesty

---

### **Mechanics**

**Types of Scams:**

**1. Overcharging (Price Scam):**
```
Seller (Deceitful 60):
  - Market price: 5 coins
  - Tells buyer: "This is worth 8 coins"
  - Hopes buyer doesn't know market price

Buyer (Rational):
  - Knows market price
  - "That's too expensive" → Rejects

Buyer (Cautious):
  - Doesn't know prices well
  - Trusts seller → Pays 8 coins (scammed!)
```

**2. False Quality (Defective Goods):**
```
Seller (Deceitful 70):
  - Sells "high quality tool"
  - Actually: Durability 50 instead of 100
  - Buyer doesn't know until uses it

Discovery:
  - Tool breaks after 50 uses (should be 100)
  - Buyer realizes: "I was scammed!"
```

**3. Short-Changing (Quantity Scam):**
```
Seller:
  - Says "10 wheat for 3 coins"
  - Actually gives 8 wheat
  - Hopes buyer doesn't count

Buyer may or may not notice immediately
```

---

### **Discovery & Consequences**

**Immediate Discovery (Noticed at Trade):**
```
Buyer (Rational) counts:
  "You said 10 wheat, this is only 8!"
  
Seller (caught):
  Option 1: Apologize, correct ("Sorry, mistake!")
  Option 2: Double down ("That's all you get")
  
If Seller refuses correction:
  - Buyer: Trust in Seller -80
  - Buyer: Affection -40
  - Buyer spreads warning to acquaintances
```

**Delayed Discovery (Noticed Later):**
```
Week 1: Buyer purchases "good tool" for 20 coins
Week 4: Tool breaks (durability 50, should be 100)
Buyer: "Wait, this was defective!"

Buyer evaluates:
  - Was this accident or scam?
  - Seller personality: Deceitful 70 → "Probably scam!"
  
Consequences:
  - Trust in Seller -90 (betrayal discovered)
  - Remove Seller from supplier_knowledge (never buy again)
  - Spread warning to all acquaintances (gossip)
  - Seller gains "Scammer" reputation
```

---

### **Reputation Spread**

**If Buyer is Social (>50):**
```
Buyer tells all 10 acquaintances:
  "Don't buy from Marcus, he sells defective tools!"
  
Those 10 NPCs:
  - Add Marcus to "avoid" list
  - May spread to THEIR acquaintances (if Social)
  
Within 1-2 weeks:
  - 30-50 NPCs know "Marcus is a scammer"
  - Marcus loses customer base
```

**Reputation Damage:**
```
Marcus's Reputation (AI Systems - Core, Section 2.9):
  Honor: 60 → 20 (dishonest)
  Trustworthiness: 70 → 10 (betrayed customer)
  
NPCs who hear about scam:
  - Start with negative bias (-30 Trust)
  - Avoid trading with Marcus
  - Marcus must rebuild reputation (very hard)
```

---

### **Scammer's Dilemma**

**Short-Term Gain vs Long-Term Loss:**

```
Scam 1 customer:
  Gain: +5 coins (overcharged)
  Loss: -1 customer permanently

If Social customer:
  Loss: -1 customer + their 10 acquaintances = -11 potential customers

Is scamming worth it?
  - For Deceitful + Ambitious: Maybe (short-term thinker)
  - For Rational: No (long-term loss exceeds gain)
  - For Honest: Never (morally opposed)
```

**When Scamming Works:**
- One-time customers (traveling merchants, no repeat business)
- Desperate buyers (will pay anything)
- Information asymmetry (buyer has no way to verify)

**When Scamming Fails:**
- Repeat customers (lose future business)
- Social buyers (spread bad reputation)
- Informed buyers (know market prices)

---

### **Redemption Path**

**Can scammer rebuild reputation?**

```
Year 1: Marcus scams customer, reputation ruined
Year 2-3: Marcus tries honest trades
  - Few customers (reputation lingers)
  - Honest trades with brave/desperate buyers
  - Slowly rebuilds Trust (+5 per honest trade)
  
Year 5: Marcus's reputation recovering
  - Honor: 20 → 40
  - Trust: 10 → 35
  - Some NPCs willing to try him again
  
Year 10: Fully redeemed (if consistent honesty)
  - Honor: 60 (back to neutral)
  - Trust: 60
  - Normal customer base

But:
  - Some NPCs never forgive (memory persists)
  - Takes 5-10 years to rebuild fully
  - Much harder than maintaining honesty
```

---

### **Implementation Requirements**

**Data Tracking:**
- Item quality (durability, defect flags)
- Scam discovery events
- Reputation integration (AI Systems - Core, Section 2.9)
- Gossip propagation of scam warnings

**Performance:**
- Only Tier 2/3 track scams (Tier 1 abstracted)
- Scam checks on use (tools breaking) not every tick
- Reputation spread uses existing gossip system

**Balancing:**
- Scam detection chance (Rational NPCs detect more)
- Reputation damage severity (must outweigh scam profit)
- Redemption difficulty (possible but hard)

---

## **3.4 Personality-Driven Consumption**

**Status:** 🟡 Enhancement - Tier 2  
**Complexity:** Medium  
**Value:** Low  
**Timeline:** 3-4 months post-MVP

### **Purpose**

Personality affects how NPCs spend currency beyond basic needs, creating behavioral variety in consumption patterns.

**Current State (Core):**
- NPCs buy what they need (profession requirements, food)
- Surplus currency accumulates
- No personality-driven spending

**Enhanced State:**
- Ambitious buy status goods (luxury display)
- Cautious hoard savings (emergency fund)
- Social spend on gifts (relationship building)
- Content spend minimally (satisfied with basics)

---

### **Mechanics**

**Spending Priority by Personality:**

**AMBITIOUS:**
```
After basic needs met:
  - Buy luxury goods (display wealth)
  - Invest in business opportunities
  - Hoard wealth for status
  
Example:
  Ambitious merchant with 500 coins:
    - Buys fine clothes (50 coins) for status
    - Buys rare gem (200 coins) to display
    - Saves rest for investment
```

**CAUTIOUS:**
```
After basic needs met:
  - Save aggressively (emergency fund)
  - Avoid unnecessary spending
  - Only buy essentials
  
Example:
  Cautious farmer with 200 coins:
    - Saves 180 coins (90% of surplus)
    - Only buys critical repairs
    - "Need savings for bad harvest"
```

**SOCIAL:**
```
After basic needs met:
  - Buy gifts for friends (+Affection)
  - Host gatherings (future enhancement)
  - Spend on social activities
  
Example:
  Social merchant with 300 coins:
    - Buys gift for friend (20 coins)
    - Throws feast (50 coins)
    - Enjoys socializing
```

**CONTENT:**
```
After basic needs met:
  - Spend minimally
  - Satisfied with simple life
  - Savings accumulate by default
  
Example:
  Content craftsman with 150 coins:
    - "I have enough"
    - Spends only on necessities
    - Wealth grows passively
```

**KIND:**
```
After basic needs met:
  - Donate to poor
  - Help struggling NPCs
  - Charitable spending
  
Example:
  Kind farmer with 250 coins:
    - Gives food to starving NPC (free)
    - Donates 50 coins to faction charity
    - Helps rebuild neighbor's farm
```

---

### **Consumption Behaviors**

**Luxury Goods Demand:**
```
Ambitious + Rich NPCs:
  - Primary buyers of luxury goods
  - Drive luxury market
  - Create demand for rare items
  
Result: Luxury goods prices increase (scarcity + high demand)
```

**Savings Accumulation:**
```
Cautious + Content NPCs:
  - Accumulate wealth passively
  - Large savings pools
  - May become investors (future enhancement)
  
Result: Wealth concentration among savers
```

**Gift Economy:**
```
Social + Kind NPCs:
  - Active gift-giving
  - Strengthen relationships
  - Reduce wealth inequality (redistribute)
  
Result: Relationship networks strengthened
```

---

### **Implementation Requirements**

**Data Tracking:**
- Surplus currency calculation (income - basic needs)
- Personality-driven spending rules
- Gift tracking (who gave to whom)

**Performance:**
- Calculate spending decisions monthly (not every tick)
- Tier 1 uses simplified rules
- Tier 2/3 more nuanced spending

**Balancing:**
- Spending rates per personality
- Luxury goods availability
- Gift economy impact on relationships

---

## **3.5 Memory Decay for Supplier Knowledge**

**Status:** 🟡 Enhancement - Tier 2  
**Complexity:** Low  
**Value:** Low  
**Timeline:** 2-3 months post-MVP

### **Purpose**

NPCs forget old supplier knowledge if not used recently, creating more realistic information persistence and forcing re-discovery.

**Current State (Core):**
- Supplier knowledge never decays
- NPCs remember forever (unless reliability <20)

**Enhanced State:**
- Unused knowledge fades over time
- Must re-learn if not used in 6+ months
- Creates information churn

---

### **Mechanics**

**Decay System:**

```
Supplier_Knowledge {
  supplier_id: Marcus
  resource: "wheat"
  reliability: 75
  last_accessed: Year 2, Month 3
}

Current time: Year 2, Month 9
Time since last access: 6 months

Decay calculation:
  If last_accessed > 6 months ago:
    reliability -= 5 per month past 6 months
  
  Month 7: 75 - 5 = 70
  Month 8: 70 - 5 = 65
  Month 9: 65 - 5 = 60
  
  If reliability drops below 20:
    Remove entry (forgotten)
```

**Access Resets Decay:**
```
If NPC goes to Marcus and buys wheat:
  - last_accessed = current_time
  - Decay timer resets
  - Knowledge refreshed
```

---

### **Behavioral Effects**

**Long-Term Customers:**
```
Farmer who buys tools every 3 months:
  - Knowledge never decays (accessed regularly)
  - Stable supplier relationship
```

**Occasional Buyers:**
```
NPC who bought wheat once 2 years ago:
  - Knowledge decayed and forgotten
  - Next time needs wheat: Must ask around again
  - "Who sells wheat these days?"
```

**Seasonal Goods:**
```
NPC who buys winter clothes once per year:
  - Knowledge decays slightly between uses
  - May need to verify supplier still exists
```

---

### **Implementation Requirements**

**Data Tracking:**
- Last accessed timestamp per supplier knowledge entry
- Monthly decay calculation

**Performance:**
- Update monthly (not every tick)
- Batch process for all NPCs
- Minimal overhead

**Balancing:**
- Decay start time (6 months reasonable)
- Decay rate (5 points/month)
- Never instant forget (gradual)

---

# **PART 4: TIER 3 ENHANCEMENTS (POLISH)**

## **4.1 Emergent Currency Types**

**Status:** 🟢 Polish - Tier 3  
**Complexity:** Very High  
**Value:** Low (nice-to-have)  
**Timeline:** 8+ months post-MVP

### **Purpose**

Different regions/factions develop own currencies, creating exchange rates, currency conversion, and arbitrage opportunities.

**Scope:** Very complex, major feature. See **Appendix E.1: Emergent Currency** for full design.

**Key Concepts:**
- Kingdom A uses gold coins
- Kingdom B uses silver coins
- Tribal region uses bead currency
- Exchange rates emerge from trade
- Merchants become money changers
- Currency strength tied to faction power

**Implementation Challenge:**
- Requires multi-region economy
- Complex exchange rate calculations
- Faction power integration
- High development cost for limited benefit

**Recommendation:** Only implement if multi-kingdom gameplay is core focus.

---

## **4.2 Advanced Information Spread System**

**Status:** 🟢 Polish - Tier 3  
**Complexity:** Very High  
**Value:** Medium  
**Timeline:** 8+ months post-MVP

### **Purpose**

Dedicated information spread mechanics including rumors, false information, information as commodity, espionage.

See **Appendix E.2: Advanced Information Spread** for full design.

**Key Features:**
- Rumor system (false information spreads)
- Information trading (sell secrets for profit)
- Espionage (gather intelligence)
- Propaganda (spread false info intentionally)
- Information networks (spy rings)

**Implementation Challenge:**
- Requires truth vs false tracking
- Motivation for information gathering
- Integration with faction politics
- Very complex system

**Recommendation:** Only if narrative/political gameplay is primary focus.

---

## **4.3 Employment & Wage System**

**Status:** 🟢 Polish - Tier 3  
**Complexity:** High  
**Value:** Medium  
**Timeline:** 6-8 months post-MVP

### **Purpose**

NPCs can employ other NPCs for wages, creating labor market, employer-employee relationships, wage negotiation.

See **Appendix E.3: Employment System** for full design.

**Key Features:**
- Employers hire workers (farms hire laborers)
- Wage negotiation (supply/demand for labor)
- Employment contracts
- Strikes and labor disputes
- Class consciousness emerges

**Implementation Challenge:**
- Requires dynamic pricing (wages fluctuate)
- Employer-employee relationship tracking
- Contract management
- Balance issues (wage vs profit)

**Recommendation:** Implement after dynamic pricing stable.

---

## **4.4 Investment & Banking**

**Status:** 🟢 Polish - Tier 3  
**Complexity:** Very High  
**Value:** Low  
**Timeline:** 10+ months post-MVP

### **Purpose**

Wealthy NPCs invest in businesses, lend money, earn passive income, creating capital markets.

**Key Features:**
- Loans with interest
- Business investments
- Banking institutions emerge
- Wealth compounds
- Economic inequality increases

**Implementation Challenge:**
- Requires employment system
- Complex interest calculations
- Risk management (loans default)
- Balance issues (runaway wealth)

**Recommendation:** Only if economic simulation is core gameplay.

---

## **4.5 Trade Routes & Caravans**

**Status:** 🟢 Polish - Tier 3  
**Complexity:** High  
**Value:** Medium  
**Timeline:** 6-8 months post-MVP

### **Purpose**

Established trade routes between cities, organized caravans, route safety affects trade, infrastructure investment.

**Key Features:**
- Physical trade routes (roads, paths)
- Caravans (group of merchants travel together)
- Bandit threats (raid routes)
- Route investment (factions build roads)
- Trade volume increases with safety

**Implementation Challenge:**
- Requires pathfinding infrastructure
- Bandit AI (target routes)
- Faction investment mechanics
- Route maintenance

**Recommendation:** Implement if map size large with distant regions.

---

## **4.6 Economic Policies & Regulations**

**Status:** 🟢 Polish - Tier 3  
**Complexity:** Very High  
**Value:** Medium  
**Timeline:** 8-10 months post-MVP

### **Purpose**

Factions implement economic policies (tariffs, regulations, price controls), affecting trade and economy.

**Key Features:**
- Tariffs (taxes on imports/exports)
- Price controls (max/min prices)
- Trade restrictions (ban certain goods)
- Monopoly grants (exclusive rights)
- Guild regulations

**Implementation Challenge:**
- Requires faction political system
- Policy effects on markets
- Enforcement mechanics
- Player interaction with policies

**Recommendation:** Only if faction politics is major gameplay element.

---

# **PART 5: IMPLEMENTATION GUIDANCE**

## **5.1 When to Implement Each Enhancement**

**Decision Framework:**

**Implement Enhancement IF:**
1. Core systems stable (no major bugs)
2. Performance acceptable (60 FPS with 10k NPCs)
3. Economic patterns as expected (emergent balance)
4. Team has bandwidth (not blocking other work)
5. Enhancement adds significant value (playtesting feedback)

**Prioritization:**

**TIER 1 (Implement First):**
1. **Dynamic Pricing** - Enables market-responsive production
2. **Negotiation** - Adds interaction depth
3. **Resource Spoilage** - Creates urgency
4. **Market-Responsive Production** - Makes economy dynamic

**Order:** Dynamic Pricing → Negotiation → Spoilage → Market-Responsive

**TIER 2 (Implement Second):**
- Based on playtesting feedback
- Choose enhancements that address player pain points
- Skip if not adding value

**TIER 3 (Implement Last, Optional):**
- Only if core gameplay focuses on that system
- Most can be skipped without loss

---

## **5.2 Testing Requirements**

**Per Enhancement Testing:**

**Dynamic Pricing:**
- Test: Price oscillations stabilize over time
- Test: Boom-bust cycles emerge but dampen
- Test: Local price variations make sense
- Test: No infinite price spirals

**Negotiation:**
- Test: Personality differences visible in negotiation
- Test: Relationship effects function correctly
- Test: Negotiations resolve (don't loop forever)
- Test: Performance acceptable (not too slow)

**Resource Spoilage:**
- Test: Spoilage creates urgency (NPCs sell before spoiling)
- Test: Seasonal price variations emerge
- Test: Tool degradation creates steady demand
- Test: No exploit (infinite fresh food tricks)

**Market-Responsive Production:**
- Test: NPCs switch crops based on prices
- Test: Supply adjusts to demand over time
- Test: Market finds equilibrium (eventually)
- Test: No degenerate strategies (all-wheat then all-vegetable flip-flopping)

---

## **5.3 Integration Challenges**

**Common Integration Issues:**

**Dynamic Pricing + Market-Responsive Production:**
- **Issue:** Positive feedback loops (price rises → more production → oversupply → crash)
- **Solution:** Damping factors, switching costs, personality variation

**Negotiation + Relationship System:**
- **Issue:** Too many relationship updates (performance)
- **Solution:** Only significant trades affect relationships (>10 coins)

**Resource Spoilage + Storage:**
- **Issue:** NPCs lose all food to spoilage (frustrating)
- **Solution:** AI prioritizes selling perishables first

**Barter + Currency:**
- **Issue:** Which system to use when?
- **Solution:** Currency preferred, barter fallback when currency scarce

---

# **APPENDICES**

## **Appendix A: Market-Responsive Production Examples**

### **A.1: Vegetable Boom-Bust Cycle**

[Full detailed example with year-by-year progression, price changes, NPC decisions, and market equilibration]

### **A.2: Tool Market Equilibration**

[Example of craftsmen responding to tool shortage, oversupply correction, finding balance]

### **A.3: Cascading Production Shifts**

[Example of how wheat shortage affects food prices, which affects vegetable prices, creating cascade]

---

## **Appendix B: Dynamic Pricing Examples**

### **B.1: Famine Price Spike**

[Detailed example of bad harvest causing food shortage, price spike, economic crisis, recovery]

### **B.2: Regional Price Differences**

[Example of Village A vs Village B price differences creating merchant arbitrage opportunity]

### **B.3: Price Equilibration Over Time**

[Example showing how prices oscillate and eventually stabilize near equilibrium]

---

## **Appendix C: Negotiation Examples**

### **C.1: Honest vs Honest (Quick Agreement)**

[Two honest NPCs negotiate, reach fair price quickly, both satisfied]

### **C.2: Ambitious vs Rational (Calculated Haggling)**

[Ambitious seller wants profit, Rational buyer calculates fair price, negotiation process]

### **C.3: Deceitful Manipulation**

[Deceitful seller tries to overcharge, different buyer reactions based on personality]

### **C.4: High-Trust Relationship (Flexible Terms)**

[Two NPCs with high Trust negotiate, flexible payment, relationship strengthens]

---

## **Appendix D: Barter Examples**

### **D.1: Successful Barter (Mutual Benefit)**

[Farmer and Craftsman trade wheat for tool, both value what they get more than what they give]

### **D.2: Failed Barter (Unequal Value)**

[Attempted barter fails because valuations don't align, no mutual benefit]

### **D.3: Multi-Item Barter**

[Complex barter involving 3+ items, NPCs negotiate bundle deals]

### **D.4: Barter Chain**

[NPC trades through intermediaries to eventually get what they need]

---

## **Appendix E: Advanced Systems Examples**

### **E.1: Emergent Currency**

[Full example of how Kingdom A gold vs Kingdom B silver creates exchange rates, money changers]

### **E.2: Advanced Information Spread**

[Example of rumor spreading, false information, espionage, information trading]

### **E.3: Employment System**

[Example of employer hiring laborers, wage negotiation, labor strike]

---

**END OF DOCUMENT**

---

## **Document Revision History**

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-01-XX | Initial enhancements document created |

---

**Implementation Priority:** Focus on Core systems first (see Economic Systems - Core document). Only implement enhancements after Core is stable and proven.