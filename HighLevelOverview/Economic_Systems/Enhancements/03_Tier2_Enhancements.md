---
layout: default
title: Tier 2 Enhancements
parent: Enhancements
grand_parent: Economic Systems
nav_order: 3
---

**Related Documents:**
- Economic Systems - Core (MVP) (foundational systems)
- AI Systems - Core (AI behavior integration)
- AI Systems - Enhancements (future AI features)
- [Future] Resource Encyclopedia (detailed resource specs)


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