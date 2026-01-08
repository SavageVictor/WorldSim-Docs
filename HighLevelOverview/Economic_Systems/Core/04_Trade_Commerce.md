---
layout: default
title: Trade & Commerce
parent: Core Systems
grand_parent: Economic Systems
nav_order: 4
---

**Related Documents:**
- AI Systems - Core (main AI behavior systems)
- AI Systems - Enhancements (future AI features)
- Economic Systems - Enhancements (future economic features)
- [Future] Resource Encyclopedia (detailed resource specs, interactions, visuals)


# **PART 4: TRADE & COMMERCE**

## **4.1 Acquaintance & Knowledge Networks**

**Purpose:** Enable NPCs to discover trade partners without centralized matchmaking.

**Reference: Extends AI Systems - Core, Section 2.3 (Relationship System) for Tier 1 NPCs**

### **Lightweight Acquaintance System (Tier 1)**

**Data Structure:**
```
Tier_1_NPC {
  acquaintances: Array<NPC_ID>
    - Max: 5-10 NPCs
    - Oldest inactive replaced when at capacity
  
  supplier_knowledge: Map {
    resource_type: {
      supplier_id: NPC_ID,
      reliability: 0-100,
      last_checked: timestamp
    }
  }
}
```

**How Acquaintances Form:**

| Event | Acquaintance Added | Probability |
|-------|-------------------|-------------|
| **Trade together** | Both add each other | 100% (always) |
| **Work in same area** | May add | 30% per week if nearby |
| **Same faction** | May add | 20% per month |
| **Introduced by mutual friend** | Social NPC introduces | 40% if Social > 50 |
| **Live in same district** | May add | 15% per month |

**Acquaintance Replacement:**
- When at max capacity, calculate "activity score" for each
- Activity = trades_in_last_year + (same_faction ? 10 : 0) + (nearby ? 5 : 0)
- Remove lowest activity acquaintance
- Add new acquaintance
- **Result:** NPCs maintain relationships with people they actually interact with

### **Extended Network (Tier 2/3)**

**Tier 2 NPCs:**
- **Acquaintances:** Max 20-50 NPCs
- **Supplier Knowledge:** Tracks more resources, more suppliers per resource
- **Advantage:** Know more suppliers, can broker introductions, better trade network efficiency

**Tier 3 NPCs:**
- **Acquaintances:** Max 50-100 NPCs
- **Supplier Knowledge:** Extensive tracking
- **Advantage:** Major trade hubs in network, can leverage full relationship system (Trust, Respect), may become "merchant lords" naturally

**Integration with Relationship System (AI Systems - Core, Section 2.3):**
- For Tier 2/3: Acquaintances can become full tracked relationships if trade frequently (5+ trades)
- Full relationship affects trade: High Trust = better deals, flexible payment

---

## **4.2 Trade Discovery System**

**How NPCs Find What They Need:**

### **STEP 1: Check Own Knowledge**

NPC checks `supplier_knowledge[needed_resource]`:

**Case A:** Entry exists AND reliability > 20
- → Go directly to known supplier
- Skip to transaction

**Case B:** Entry doesn't exist OR reliability ≤ 20
- → Don't know reliable supplier
- Proceed to STEP 2

### **STEP 2: Ask Acquaintances**

- Select nearest acquaintance
- Walk to their current location
- Initiate conversation (speech bubble: "Do you know who has [resource]?")

**If Acquaintance Knows:**
- Acquaintance responds with supplier info (speech bubble)
- NPC updates knowledge: `supplier_id, reliability = 50, timestamp`
- NPC thanks acquaintance (Affection +2 if tracked relationship)
- NPC proceeds to supplier

**If Acquaintance Doesn't Know:**
- Acquaintance responds: "Sorry, I don't know"
- NPC tries next acquaintance
- If all exhausted → Proceed to STEP 3

### **STEP 3: Go to Market (Fallback)**

- NPC walks to nearest market location
- Browses stalls (walks between sellers)
- Checks each stall for needed item
- When found: Update knowledge, initiate trade
- If not found: Return home disappointed, try again later

**Observable Elements:**
- NPCs walking to each other
- Speech bubbles showing questions/answers
- Information visibly spreading through network

See **Appendix B: Trade Discovery Examples** for detailed scenarios including:
- B.1: Successful Direct Knowledge (John knows Marcus)
- B.2: Ask Acquaintance Chain (John asks Sarah asks Thomas)
- B.3: Market Fallback (No one knows, browse market)

---

## **4.3 Supplier Reliability Tracking**

**Purpose:** NPCs learn who actually has stock, forget unreliable suppliers.

**Reliability Score (0-100):**
- 100 = Always has stock (highly reliable)
- 50 = Sometimes has stock (new supplier or inconsistent)
- 20 = Rarely has stock (unreliable threshold)
- 0 = Never has stock (will be removed)

**Reliability Updates:**

### **Positive Reinforcement**
- When NPC successfully buys from supplier: `reliability = min(100, reliability + 10)`
- Reasoning: "They had what I needed, they're dependable"

### **Negative Reinforcement**
- When supplier is OUT OF STOCK: `reliability -= 30`
- Reasoning: "They wasted my time, they're unreliable"

### **Removal Threshold**
- If `reliability < 20`: Remove entry from `supplier_knowledge`
- Reasoning: "I won't bother going to them anymore"

**Redemption Path:**
- Supplier restocks, brings goods to market
- Someone buys from them → Re-added to their knowledge
- Word spreads gradually, supplier rebuilds customer base

**Emergent Effects:**
- Reliable suppliers build loyal customer base
- Unreliable suppliers lose customers naturally
- Seasonal producers (farmers) have fluctuating reliability
- Year-round producers (craftsmen) maintain high reliability
- Creates competitive pressure to maintain stock

See **Appendix B.4: Supplier Reliability Lifecycle** for detailed example of Marcus losing and regaining customers.

---

## **4.4 Information Spread (Local vs Global)**

**Purpose:** Different goods spread information differently, creating local vs global markets.

**Reference: Integrates with Gossip System (AI Core 2.9)**

### **LOCAL SPREAD: Low-Value, High-Volume Goods**

**Applies to:** Wheat, wood, stone, basic food, common tools, everyday goods

**Spread Mechanism:**
- **Trigger:** NONE (doesn't auto-spread)
- **Spread:** Only when NPC specifically asks "Who has [resource]?"
- **Range:** Immediate acquaintance network (1-2 hops)
- **Result:** Information stays LOCAL

**Why This Makes Sense:**
- Boring to gossip about ("Marcus has wheat again" - nobody cares)
- Everyone needs these goods but they're not noteworthy
- Local suppliers sufficient (no need to know distant suppliers)

**Emergent Pattern:**
- Villages develop local economies for basics
- Villagers buy locally, rarely travel for common goods
- Regional price variations possible

### **GLOBAL SPREAD: High-Value, Low-Volume Goods**

**Applies to:** Rare gems, masterwork weapons, exotic spices, legendary items, unique artifacts

**Spread Mechanism:**
- **Trigger:** Item value > GOSSIP_THRESHOLD (e.g., 100+ coins)
- **Spread:** Automatic, exponential via social networks
- **Range:** Entire faction, possibly civilization-wide
- **Result:** Information travels FAR

**Gossip Cascade Mechanic:**
1. Witness sees high-value item at market
2. Each witness (if Social > 30) tells all acquaintances
3. Those acquaintances tell THEIR acquaintances (if Social)
4. Continues cascading
5. Within 3-5 days: 100-200 NPCs know about item
6. Distant merchants travel to find seller

**Observable Elements:**
- Speech bubbles: "Did you hear about the ruby?!"
- NPCs gossiping in taverns, markets
- Distant NPCs arriving asking for seller location
- Information visualization: Ripples spreading across map

**Personality Effects on Gossip:**

| Personality | Gossip Behavior |
|------------|------------------|
| **Social > 60** | Tells 100% of acquaintances, spreads fast |
| **Social 30-60** | Tells 50% of acquaintances, moderate spread |
| **Social < 30** | Tells 10% of acquaintances, slow spread |
| **Solitary < 20** | Doesn't spread gossip at all |

**Emergent Market Structure:**
- Basic goods: Local markets dominate, price variations by region
- Luxury goods: Global markets emerge, merchants travel long distances
- Trade hubs form naturally in cities with wealthy NPCs

See **Appendix B.5: Information Spread Comparison** for side-by-side wheat vs ruby examples.