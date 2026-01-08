---
layout: default
title: Appendices
parent: Economic Systems
grand_parent: Documentation
nav_order: 9
---

**Related Documents:**
- AI Systems - Core (main AI behavior systems)
- AI Systems - Enhancements (future AI features)
- Economic Systems - Enhancements (future economic features)
- [Future] Resource Encyclopedia (detailed resource specs, interactions, visuals)


# **APPENDICES**
A. Observable Flow Examples  
B. Trade Discovery Examples  
C. Market Behavior Examples  
D. Economic Pattern Examples  
E. Integration Examples  
F. Quick Reference Tables

---

# **PART 1: CORE PHILOSOPHY**

## **1.1 Design Principles**

**Observable, Physical, Emergent**

The economic system is built on three foundational principles:

**1. OBSERVABLE**
- Every resource has physical presence in the game world
- Players can see NPCs extract, carry, store, and trade resources
- Resource flow is traceable from source to destination
- No hidden abstractions - if you can't see it, it doesn't exist

**2. PHYSICAL**
- Resources exist as actual items in inventories
- NPCs must physically travel to extract resources
- NPCs must physically carry resources to storage
- Markets are physical locations where NPCs gather
- Trades happen face-to-face between NPCs

**3. EMERGENT**
- No centralized "market price" system
- Economy arises from individual NPC production, consumption, and trade decisions
- Supply and demand emerge from aggregate NPC behavior
- Merchants aren't assigned - they emerge from NPCs who trade frequently
- Economic health is consequence of NPC choices, not scripted balance

---

## **1.2 Observable Economy**

**What "Observable" Means in Practice:**

Players should be able to watch and understand the complete economic lifecycle. See **Appendix A: Observable Flow Examples** for detailed scenarios including:
- A.1: Complete Wheat Lifecycle (field to bread)
- A.2: Tool Production Chain (ore to farm)
- A.3: Resource Extraction Sequence

**Core Goal:** Player should be able to answer "Where did this resource come from and where is it going?" by watching the game.

---

## **1.3 Integration with AI Systems**

**This economic system integrates directly with AI systems from AI Systems - Core:**

**With Need & Goal System (AI Core 2.6):**
- NPCs produce/trade to satisfy need hierarchy
- SURVIVAL need → Must acquire food (drives farming/foraging)
- SECURITY need → Must acquire stable income (drives profession choice)
- Professional needs create derived demand

**With Occupation System (AI Core 2.5):**
- Occupations determine what NPCs produce
- Professional requirements drive trade
- Economic conditions affect occupation attractiveness
- Surplus production happens naturally

**With Personality System (AI Core 2.2):**
- Ambitious NPCs seek high-value trades
- Cautious NPCs prefer local reliable suppliers
- Social NPCs spread information faster
- Rational NPCs calculate trade value

**With Relationship/Acquaintance System:**
- Tier 1 NPCs: Lightweight acquaintance network (5-10 contacts)
- Tier 2/3 NPCs: Leverage full relationship system for trade
- Trust affects trade willingness
- Repeat trades strengthen bonds

**With Faction System (AI Core 2.4):**
- Faction members prefer trading with each other
- Faction stockpiles serve as communal resources

See **Appendix E: Integration Examples** for detailed scenarios.

---

# **PART 2: RESOURCE SYSTEMS**

## **2.1 Resource Categories**

### **PRIMARY RESOURCES (Extracted from Environment)**

**Renewable Resources:**

| Resource | Source Location | Extraction Method | Regeneration |
|----------|----------------|-------------------|--------------|
| **Food (Wild)** | Wilderness, forests | Foraging | Seasonal (spring/summer) |
| **Food (Crops)** | Farmland | Farming (plant → harvest) | Annual crop cycle |
| **Wood** | Forests | Logging | Trees regrow over years |

**Non-Renewable Resources:**

| Resource | Source Location | Extraction Method | Notes |
|----------|----------------|-------------------|-------|
| **Stone** | Mountains, quarries | Mining/Quarrying | Finite deposits |
| **Ore (Iron)** | Mountains, mines | Mining | Finite deposits, deeper = richer |
| **Ore (Precious)** | Rare veins | Mining | Very rare, valuable |

### **PROCESSED RESOURCES (Crafted from Primary)**

**Crafted Goods:**

| Resource | Input Resources | Crafter | Production Time |
|----------|----------------|---------|-----------------|
| **Tools** | Wood (2) + Iron (1) | Craftsman | 1 week |
| **Weapons** | Wood (1) + Iron (2) | Craftsman | 2 weeks |
| **Basic Goods** | Wood (3) OR Stone (2) | Craftsman | 3-5 days |
| **Building Materials** | Wood (10) + Stone (5) | Craftsman | 2 weeks |

**Note:** Specific quantities, recipes, and production times will be detailed in the Resource Encyclopedia document.

---

## **2.2 Physical Inventory System**

**Storage Hierarchy:**

### **Personal Inventory**
- **Capacity:** 20-50 units (depending on NPC strength/equipment)
- **Access:** Individual NPC only
- **Visibility:** Resources visible on NPC's person (carried items, backpack)
- **Movement:** NPC carries everywhere
- **Use Cases:** Currently gathering, traveling to market, personal consumption

### **Home Storage**
- **Capacity:** 50-100 units
- **Access:** NPC + family members
- **Visibility:** Visible pile/chest inside home building
- **Movement:** Stationary at home location
- **Use Cases:** Personal long-term storage, family food reserves, crafting materials

### **Professional Building Storage**
- **Capacity:** 200-500 units
- **Access:** Building owner (and employees, future)
- **Visibility:** Large visible stockpiles at building
- **Movement:** Stationary at profession building
- **Types:** Barn (farmers), Workshop (craftsmen), Warehouse (merchants), Armory (soldiers)
- **Use Cases:** Professional production materials, finished goods awaiting sale, tools and equipment

### **Faction Stockpile**
- **Capacity:** 1000+ units
- **Access:** All faction members (permission-based)
- **Visibility:** Massive visible resource piles in designated area
- **Movement:** Stationary at faction headquarters/warehouse
- **Use Cases:** Emergency reserves, communal resources, large-scale construction, military supplies

**Storage Priority (when NPC needs to store):**
1. Professional Building (if owns one and resource is profession-related)
2. Home Storage (if has space)
3. Faction Stockpile (if faction member and allowed)
4. Sell/Trade immediately (if all storage full)

---

## **2.3 Resource Flow Visualization**

**Observable Resource Lifecycle:**

```
EXTRACTION → CARRY → STORAGE → TRADE → CONSUMPTION
   ↓           ↓         ↓         ↓          ↓
 Visible    Visible   Visible   Visible   Resource
 action     in hand    pile     exchange  disappears
```

See **Appendix A.1: Complete Wheat Lifecycle** for detailed step-by-step example.

---

# **PART 3: PRODUCTION SYSTEMS**

## **3.1 Extraction & Gathering**

**General Extraction Mechanics:**

**Step 1: NPC Identifies Need**
- NPC checks profession goal (e.g., Farmer needs to produce wheat)
- Verifies resources: "Do I have seeds? Storage space?"
- If ready → Begin production cycle

**Step 2: Travel to Resource Location**
- NPC walks from home/building to resource site (Field, Forest, Mountain/Mine)
- Visible: NPC traveling with tools

**Step 3: Extraction Action**
- NPC performs extraction animation (Planting/Harvesting, Chopping, Pickaxe swinging)
- Duration varies by resource and skill
- Resource appears in NPC inventory when complete

**Step 4: Return to Storage**
- NPC walks back to storage location
- Deposits resources
- Inventory visible decreases, storage pile visible increases

**Step 5: Repeat or Rest**
- If still time in workday AND inventory not full → Repeat
- Else → Rest, socialize, fulfill other needs

See **Appendix A.2: Resource Extraction Sequence** for visual breakdown.

---

## **3.2 Crafting & Processing**

**Crafting Workflow:**

**Step 1: Check Requirements**
- Craftsman verifies: Input materials available? Workshop exists? Professional tools available?
- If ALL requirements met → Begin crafting
- If missing materials → Must acquire through trade/extraction

**Step 2: Crafting Action**
- Craftsman at workshop performs crafting animation
- Duration: 1-2 weeks (game time)
- Input materials consumed from inventory
- Output item appears when complete

**Step 3: Storage or Sale**
- If needed personally → Keep in inventory/home
- If surplus → Store in workshop OR take to market immediately

**Crafting Bottleneck:**
- Can only craft one item at a time
- Professional tool requirement limits who can craft
- Material scarcity limits production volume

---

## **3.3 Professional Requirements**

**Reference: Integrates with Occupation System (AI Systems - Core, Section 2.5)**

Each profession has **required items** to function. Without them, productivity drops to zero.

### **FARMER**
- **Required Items:** Tools (hoe, scythe) - 1 set per farmer; Seeds - consumed each planting season
- **Productivity:**
  - With tools + seeds: 100% (full harvest yield)
  - With tools only: 30% (can only forage wild food)
  - Without tools: 0% (cannot farm at all)
- **Economic Effect:** Farmers MUST buy/trade for tools from craftsmen (creates natural interdependence)

### **CRAFTSMAN**
- **Required Items:** Tools (hammer, saw, anvil) - 1 set; Raw Materials (wood + ore) - consumed per item
- **Productivity:**
  - With tools + materials: 100% (can craft)
  - With tools only: 0% (nothing to craft with)
  - Without tools: 0% (cannot craft)
- **Economic Effect:** Craftsmen MUST buy/trade for raw materials from extractors

### **SOLDIER**
- **Required Items:** Weapon - 1 per soldier; Armor (optional) - increases survival
- **Combat Effectiveness:**
  - With weapon + armor: 100%
  - With weapon only: 70%
  - Without weapon: 30% (nearly defenseless)
- **Economic Effect:** Military creates demand for weapons/armor

### **MERCHANT**
- **Required Items:** Starting Inventory (diverse goods to sell); Transport (cart/pack animal) - increases capacity
- **Trading Ability:**
  - With diverse inventory: Can trade actively
  - With limited inventory: Few trade opportunities
  - Without inventory: Cannot trade
- **Economic Effect:** Merchants need capital to start, creating barriers to entry

**Integration with Occupation System:**
- If NPC lacks professional requirements → Occupation satisfaction drops (AI Systems - Core, Section 2.5.5)
- May switch professions if cannot acquire needed items
- Professional needs drive trade patterns naturally

See **Appendix A.2: Tool Production Chain** for how professional requirements create economic flow.

---

## **3.4 Simple Production AI**

**NPCs produce their profession's default output automatically:**

### **FARMERS**
- **Default Production:** Wheat
  - 70% of farmers grow wheat
  - 20% grow vegetables
  - 10% raise animals
- **Assignment:** Random on becoming farmer, rarely changes
- **Production Cycle:** Spring (plant) → Summer (tend) → Fall (harvest) → Winter (store/sell)
- **Yield:** 100-200 units per farmer per year (varies by skill/land)

### **CRAFTSMEN**
- **Default Production:** Generalist (tools, weapons, goods)
- **No specialization** (yet)
- **Production Decisions:**
  - Prioritize items they personally need first
  - Then craft items in demand at market (simple heuristic)
  - Default to tools (always needed)
- **Yield:** 1 tool/week OR 1 weapon/2 weeks OR 2-3 basic goods/week

### **EXTRACTORS (Woodcutters, Miners)**
- **Default Production:** Their resource type
- **No decision-making:** Extract continually during work hours
- **Process:** Extract until inventory full → Return → Store → Repeat
- **Yield:** 50-100 units per worker per week

**Why Simple for Core:**
- Predictable, stable production
- Easy to balance and test
- Sufficient for emergent economy
- NPCs still respond to trade opportunities even if production is fixed

---

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
|------------|-----------------|
| **Social > 60** | Tells 100% of acquaintances, spreads fast |
| **Social 30-60** | Tells 50% of acquaintances, moderate spread |
| **Social < 30** | Tells 10% of acquaintances, slow spread |
| **Solitary < 20** | Doesn't spread gossip at all |

**Emergent Market Structure:**
- Basic goods: Local markets dominate, price variations by region
- Luxury goods: Global markets emerge, merchants travel long distances
- Trade hubs form naturally in cities with wealthy NPCs

See **Appendix B.5: Information Spread Comparison** for side-by-side wheat vs ruby examples.

---

# **PART 5: MARKET SYSTEMS**

## **5.1 Physical Market Locations**

**Markets as Designated Spaces:**

Markets are physical locations where NPCs gather to trade, not abstract matchmaking systems.

**Market Types:**

| Market Type | Location | Frequency | Traders | Coverage |
|-------------|----------|-----------|---------|----------|
| **Village Market** | Village square | Daily | 10-20 | Local (5-mile radius) |
| **Town Market** | Town center | Daily | 50-100 | Regional (20-mile radius) |
| **City Market** | Market district | Daily | 100-200 | Regional/civilizational |
| **Weekly Fair** | Town/City | Weekly | 100-300 | Draws from 50+ miles |
| **Monthly Fair** | Major city | Monthly | 300-500 | Entire civilization |
| **Crossroads Market** | Trade routes | Sporadic | 20-50 | Traveling merchants |

**Market Schedule:**
- Village Market: Opens 9 AM, closes 5 PM, peak at noon
- Weekly Fair: Saturday-Sunday, dawn to dusk, special goods variety
- Monthly Fair: Special festival atmosphere, rare items

---

## **5.2 Market Behavior**

### **SELLERS**

**Market Participation Decision:**
- NPC goes to market IF: Has surplus goods AND (needs currency OR needs different goods) AND market is open
- **Frequency:** Farmers (weekly), Craftsmen (2-3x/week), Merchants (daily), Miners/Woodcutters (weekly)

**Setting Up Stall:**
1. NPC walks to market carrying goods (visible)
2. Finds empty stall space
3. Places goods visibly (on table, ground, cart)
4. Stands at stall
5. Optional: Thought bubble "Selling wheat" or sign

**Waiting for Buyers:**
- NPC stays at stall (mostly stationary)
- May call out to passersby (speech bubble)
- May chat with neighboring sellers (social behavior)
- Social personalities actively engage customers
- Solitary personalities passively wait

**Patience:**
- Ambitious: Stays longer, wants to sell everything
- Content: Leaves if no buyers after 2-3 hours
- Cautious: May lower asking price if desperate

### **BUYERS**

**Market Visit Decision:**
- NPC goes to market IF: Needs something AND doesn't know reliable supplier OR market is only option OR browsing (Social personality, leisure)
- **Frequency:** Varies by need urgency (desperate: daily until solved; casual: monthly)

**Market Browsing:**
1. NPC arrives at market
2. Walks through market area (pathfinding between stalls)
3. For each stall: Look at goods, check "Do I need this?"
4. If yes → Approach seller; If no → Continue
5. Repeat until finds item OR exhausts all stalls

See **Appendix C: Market Behavior Examples** for detailed scenarios.

---

## **5.3 Transaction Mechanics**

**Observable Trade Sequence:**

### **STEP 1: Negotiation Initiation**
- Buyer and seller face each other at stall
- Speech bubbles appear: Buyer "I'd like to buy wheat" / Seller "I have 50 units available"

### **STEP 2: Price Discussion (Simple)**
- Seller: "10 wheat for 5 coins"
- Buyer evaluates: Can I afford? (check currency), Do I need urgently? (affects willingness)
- Buyer: "Deal" OR "No thanks"

### **STEP 3: Exchange**
If agreed:
1. Exchange animation plays (both extend hands, swap simultaneously)
2. Inventories update (visible): Buyer (+10 wheat, -5 coins), Seller (-10 wheat, +5 coins)
3. Stall display: Wheat pile shrinks
4. Both update knowledge: Buyer marks supplier reliable (+10), Seller remembers buyer

### **STEP 4: Departure**
- Speech bubbles: "Thank you" / "Come again"
- Buyer walks away (visible wheat in inventory)
- Seller remains at stall (continues waiting)
- If significant trade: Affection +5, Acquaintance added

**Trade Failure Scenarios:**
- **Can't afford:** Buyer walks away, may return with more currency
- **Out of stock:** Reliability -30, buyer tries other sellers
- **Price too high:** Buyer walks away, tries other sellers or returns if desperate

See **Appendix C.2: Transaction Examples** for success and failure scenarios.

---

## **5.4 Market Frequency & Scale**

**Market Scaling by Civilization Size:**

### **Small Village (100-500 NPCs)**
- **Market Size:** 10-20 stalls
- **Frequency:** Daily (small, informal)
- **Goods:** Basics only (food, simple tools, wood)
- **Coverage:** Local (5-mile radius)
- **Typical Sellers:** 5-8 farmers, 2-3 craftsmen, 1-2 woodcutters, occasional traveling merchant
- **Peak Hours:** Noon (20-30 NPCs present)

### **Town (500-2000 NPCs)**
- **Market Size:** 50-100 stalls
- **Frequency:** Daily + Weekly fair
- **Goods:** Basics + some luxuries, specialized tools
- **Coverage:** Regional (20-mile radius)
- **Typical Sellers:** 20-30 farmers, 10-15 craftsmen, 5-10 merchants, 3-5 miners
- **Weekly Fair:** 2x sellers (traveling merchants), special goods, festival atmosphere
- **Peak Hours:** Noon daily (80-100 NPCs), Fair (200-300 NPCs)

### **City (2000-10000 NPCs)**
- **Market Size:** 100-200+ stalls
- **Frequency:** Daily + Monthly grand fair
- **Goods:** Everything (basics to exotic luxuries)
- **Coverage:** Entire civilization
- **Market Districts:** Food, Craft, Luxury, Raw Materials markets
- **Typical Sellers:** 50+ farmers, 30+ craftsmen, 20+ full-time merchants, traveling merchants
- **Monthly Fair:** 500+ stalls, draws from 100+ miles, rare items, entertainment
- **Peak Hours:** Constant activity (200-300 NPCs always present)

**Market Emergence Patterns:**
- **Early Civilization (Year 1-5):** Informal markets, ad-hoc trading, no designated stalls
- **Established (Year 5-20):** Designated market squares, regular schedules, semi-permanent stalls
- **Mature (Year 20+):** Multiple market districts, specialization, professional merchant class

---

# **PART 6: CURRENCY & VALUE**

## **6.1 Simple Currency System**

**Core Assumptions:**
- Everyone has currency (coins)
- Currency appears/disappears as needed (abstracted economy)
- NPCs earn currency from selling goods
- NPCs spend currency to buy goods

**Currency Mechanics:**

**NPC Wealth (Abstract):**
- `currency: Integer (0 to 10,000+)`

**Earning:**
- Sell goods at market → +currency
- Work for wages (future: employment system)

**Spending:**
- Buy goods at market → -currency
- Pay taxes (faction system integration)
- Pay for services (future)

**Bankruptcy:**
- If `currency <= 0`: Cannot buy goods, must sell something or switch profession, may become bandit (desperation, AI Doc 2.5.3)

**Wealth Tiers:**

| Wealth Tier | Currency Range | Economic Status |
|-------------|---------------|-----------------|
| **Destitute** | 0-10 | Cannot afford basics, starvation risk |
| **Poor** | 10-50 | Barely surviving, basic needs met |
| **Working Class** | 50-200 | Comfortable, can afford some luxuries |
| **Wealthy** | 200-1000 | Significant surplus, invest in business |
| **Rich** | 1000-5000 | Land ownership, political influence |
| **Very Rich** | 5000+ | Noble-level wealth, faction power |

---

## **6.2 Baseline Value System**

**Items have baseline prices:**

| Resource | Baseline Price | Notes |
|----------|---------------|-------|
| Food (10 units) | 5 coins | Basic sustenance |
| Wheat (10 units) | 3 coins | Raw crop, cheaper than prepared |
| Wood (10 units) | 2 coins | Common, abundant |
| Stone (10 units) | 3 coins | Heavier, harder to extract |
| Ore (10 units) | 8 coins | Rarer, valuable for crafting |
| Tool | 15 coins | Crafted good, requires materials |
| Weapon | 25 coins | Crafted, combat-critical |
| Luxury Good | 50-500 coins | Rare, high-value items |

**Price Variation (Simple Modifiers):**
- Baseline price × 1.0 (default)
- Ambitious seller: Baseline × 1.2 (wants more profit)
- Desperate seller: Baseline × 0.8 (needs currency quickly)
- Rare item: Baseline × 2.0 (scarcity multiplier)

---

## **6.3 Simple Pricing Mechanics**

**Seller Sets Price, Buyer Accepts/Declines:**

1. Seller at stall: "10 wheat for 5 coins" (baseline price)
2. Buyer evaluates: "Can I afford? Do I need it?"
   - If yes → Buy
   - If no → Walk away
3. No negotiation (simple)

**Buyer Decision Logic:**

**Affordability Check:**
- If `buyer.currency < price`: Cannot buy, walk away

**Need Urgency Evaluation:**
- Based on Need Hierarchy (AI Systems - Core, Section 2.6)
- **CRITICAL** (starving): Buy at any affordable price
- **HIGH** (security need): Buy if price ≤ baseline × 1.5
- **MODERATE** (luxury want): Buy if price ≤ baseline × 1.0
- **LOW** (just browsing): Buy if price ≤ baseline × 0.8 (looking for deals)

---

# **PART 7: SYSTEM INTEGRATION**

## **7.1 Integration with Need & Goal System**

**Reference: AI Systems - Core, Section 2.6**

Economic behavior is driven by the Need Hierarchy:

### **TIER 1: SURVIVAL**
- **Economic Behavior:** MUST acquire food immediately, pay any affordable price, steal if cannot afford
- **Trade Priority:** Food above all else
- **Price Sensitivity:** ZERO (will pay anything available)

### **TIER 2: SECURITY**
- **Economic Behavior:** Seek steady profession, buy professional requirements, save surplus
- **Trade Priority:** Professional needs (tools, materials)
- **Price Sensitivity:** MODERATE (will pay premium for critical items)

### **TIER 3: BELONGING**
- **Economic Behavior:** Trade at loss to build relationships, give gifts to friends
- **Trade Priority:** Social goods (gifts, festival items)
- **Price Sensitivity:** HIGH (willing to overpay for relationship building)

### **TIER 4: ESTEEM**
- **Economic Behavior:** Accumulate wealth, buy luxury goods (display wealth), invest in business
- **Trade Priority:** Wealth accumulation, luxury display
- **Price Sensitivity:** LOW for luxuries (status symbols worth premium)

### **TIER 5: SELF-ACTUALIZATION**
- **Economic Behavior:** Fund projects, mentor others, create lasting change
- **Trade Priority:** Ideological goals over profit
- **Price Sensitivity:** ZERO (will spend everything on purpose)

See **Appendix E.1: Need-Driven Trade Decisions** for detailed scenario examples.

---

## **7.2 Integration with Occupation System**

**Reference: AI Systems - Core, Section 2.5**

**Professional Requirements Drive Trade:**
- Farmers need tools → Must buy from craftsmen
- Craftsmen need materials → Must buy from miners/woodcutters
- Soldiers need weapons → Must buy from craftsmen
- **Result:** Occupational interdependence creates natural trade networks

**Occupation Emergence from Economic Conditions:**
- High demand for wheat → Wheat price rises → Farming more profitable → Ambitious NPCs switch to farmer
- See AI Doc 2.5.3: Occupation Emergence Conditions

**Occupation Satisfaction Affected by Economics:**
- Materials abundant → Craftsman can craft → Steady income → Satisfaction +30
- Materials scarce → Cannot craft → No income → Satisfaction -40 → May switch profession

See **Appendix E.2: Professional Requirements Economic Chain** for tool production example.

---

## **7.3 Integration with Personality System**

**Reference: AI Systems - Core, Section 2.2**

Personality shapes economic behavior:

### **AMBITIOUS**
- **Trade:** Seeks high-value trades, travels far, becomes merchant easily
- **Occupation:** Prefers profitable professions, switches for higher income
- **Market:** Stays longer, sets higher prices

### **CAUTIOUS**
- **Trade:** Prefers local reliable suppliers, accepts first reasonable offer
- **Occupation:** Prefers stable professions, rarely switches
- **Market:** Leaves if no buyers quickly, lowers price to sell fast

### **RATIONAL**
- **Trade:** Calculates fair value, seeks optimal trades, long-term plans
- **Occupation:** Chooses profession based on economic analysis
- **Market:** Observes supply/demand, adjusts prices logically

### **SOCIAL**
- **Trade:** Spreads information rapidly, builds large network, trades to strengthen relationships
- **Market:** Spends time chatting, attracts customers through friendliness

### **HONEST**
- **Trade:** Sets fair prices, keeps promises, builds trustworthiness
- **Market:** Transparent about stock, builds repeat customer base

### **DECEITFUL**
- **Trade:** May set deceptive prices, breaks promises if profitable
- **Market:** Short-term profit over trust, loses customers when caught

See **Appendix E.3: Personality-Driven Economic Behavior** for comparison scenarios.

---

## **7.4 Emergent Economic Patterns**

**What Naturally Emerges from These Systems:**

### **PATTERN 1: Local Specialization**
- Village A (good farmland) → Many farmers → Wheat abundant
- Village B (near forest/mountains) → Many extractors → Wood/ore abundant
- **Result:** Trade interdependence, merchants connect them, regional economy

### **PATTERN 2: Merchant Class Emergence**
- Ambitious + Rational NPCs observe price differences
- Buy low, travel, sell high
- Become known as traders
- Others imitate → More merchants → Market efficiency increases

### **PATTERN 3: Boom-Bust Cycles**
- Tool prices high → NPCs switch to craftsman → Tool supply increases → Prices drop
- Eventually finds equilibrium through oscillation

### **PATTERN 4: Trade Hub Emergence**
- Central city with many NPCs → Diverse goods → Information spreads
- Reputation: "City has everything" → More merchants attracted
- Positive feedback loop → Trade capital

### **PATTERN 5: Economic Stratification**
- After 20 years: Rich (successful merchants/landowners), Middle Class (working professions), Poor (laborers), Destitute (bandits/beggars)

### **PATTERN 6: Economic Crises**
- Famine → Food prices skyrocket → Poor cannot afford → Starvation → Banditry
- Recovery paths: Faction reserves, imports, emergency farming, population decline

See **Appendix D: Economic Pattern Examples** for detailed scenarios of each pattern.

---

# **PART 8: IMPLEMENTATION PLAN**

## **8.1 Implementation Phases**

### **Phase 1: Basic Resource Flow (2-3 months)**
**Priority:** HIGHEST

**Deliverables:**
- Physical resources exist in game (inventory items)
- Extraction mechanics (farming, mining, logging, foraging)
- Visible carrying (NPCs walk with resources)
- Storage locations (home, profession building, stockpiles)
- Resource piles visually update

**Test:** Can player watch wheat go from field → barn → market → baker?

---

### **Phase 2: Professional Requirements (1-2 months)**
**Priority:** HIGH

**Deliverables:**
- Farmers require tools (productivity 0% without)
- Craftsmen require materials
- Soldiers require weapons
- Occupation satisfaction affected by missing requirements
- NPCs switch professions if cannot acquire

**Test:** Do farmers seek tools? Do they fail if can't get them?

---

### **Phase 3: Acquaintance Network (2-3 months)**
**Priority:** HIGH

**Deliverables:**
- Tier 1 NPCs track 5-10 acquaintances
- Tier 2/3 track 20-100 acquaintances
- Acquaintances form through trades, proximity, faction
- `supplier_knowledge` map implementation
- Reliability tracking (0-100 score)
- Reliability updates (+10 success, -30 failure)
- Removal at reliability < 20

**Test:** Do NPCs remember reliable suppliers? Forget unreliable ones?

---

### **Phase 4: Trade Discovery (2-3 months)**
**Priority:** HIGH

**Deliverables:**
- STEP 1: Check own knowledge for supplier
- STEP 2: Ask acquaintances (visible speech bubbles)
- STEP 3: Go to market as fallback
- Information updates after asking
- NPCs walk between locations seeking trades

**Test:** Can player watch John ask Sarah "Who has wheat?" → Sarah responds → John goes to Marcus?

---

### **Phase 5: Physical Markets (2-3 months)**
**Priority:** HIGH

**Deliverables:**
- Market location entities (designated spaces)
- Stall placement (sellers set up visible goods)
- Buyer browsing (walk between stalls)
- Face-to-face transactions
- Exchange animations
- Inventory updates visible
- Market schedules (daily, weekly, monthly)

**Test:** Can player watch full market scene from arrival to transaction?

---

### **Phase 6: Simple Currency & Pricing (1-2 months)**
**Priority:** MEDIUM

**Deliverables:**
- NPCs have currency (integer value)
- Baseline prices for all resources
- Seller sets price (baseline × personality modifier)
- Buyer accepts/declines (affordability + need urgency)
- Currency earned from sales
- Currency spent on purchases
- Bankruptcy handling

**Test:** Do NPCs earn/spend currency? Do prices make sense?

---

### **Phase 7: Information Spread (1-2 months)**
**Priority:** MEDIUM

**Deliverables:**
- Low-value goods: Asked directly only (local spread)
- High-value goods: Gossip cascade (global spread)
- Gossip threshold (value > 100 coins triggers)
- Social NPCs spread gossip more
- Solitary NPCs don't spread
- Visible gossip (speech bubbles)

**Test:** Does wheat stay local? Does ruby news spread everywhere?

---

### **Phase 8: Integration Testing (Ongoing)**
**Priority:** HIGHEST

**Tests:**
- Full resource lifecycle observable
- Professions function correctly
- Trade networks form naturally
- Markets operate smoothly
- Economic interdependence creates stories
- No major exploits
- Performance acceptable (10,000 NPCs at 60 FPS)

**Success:** Player can follow 10 different resource chains from extraction → consumption

---

## **8.2 Success Metrics**

### **Observable Stories**
**Metric:** Can players describe economic narratives?
- Example: "Marcus became the town's main wheat supplier because he's reliable"
- **Success:** Players naturally narrate economic cause-and-effect chains

### **Emergent Balance**
**Metric:** Do healthy occupation ratios emerge?
- After 10-20 years: Farmers 60-70%, Craftsmen 10-15%, Soldiers 5-10%, Merchants 5-10%, Bandits <2%
- **Success:** Civilization self-balances 80%+ of the time

### **No Degenerate Strategies**
**Metric:** Can players "break" the economy?
- Test: Infinite currency, resource duplication, trade loops, market deadlock
- **Success:** No major exploits in 100+ hours of testing

### **Trade Network Formation**
**Metric:** Do NPCs naturally find trade partners?
- After 5-10 years: Average NPCs have 5-10 known suppliers, markets have regular customers
- **Success:** 90%+ of NPCs successfully acquire needed goods

### **Personality-Driven Behavior**
**Metric:** Can you identify NPC personality from economic behavior?
- Ambitious become merchants, Cautious stay local, Social spread information
- **Success:** Personality patterns visible in economic choices

### **Economic Crisis Recovery**
**Metric:** Can civilizations recover from shocks?
- Test famine (destroy 50% farms), kill all craftsmen
- **Success:** Civilization recovers through emergent adaptation 70%+ of the time

### **Player Understanding**
**Metric:** Can players explain why economic events happened?
- Example: "Wheat prices rose because bad harvest reduced supply"
- **Success:** Players understand causal relationships without tutorials

---

## **8.3 Performance Targets**

**Required Performance:**
- **NPCs:** 10,000 simulated
- **Markets:** 200+ NPCs per market
- **Trades:** 50+ per minute
- **Frame Rate:** 60 FPS stable
- **Update Frequency:** Market prices once per week, NPCs check occupation change once per month

**Optimization Strategies:**
- Batched calculations for Tier 1 NPCs
- Tier 1 don't track individual wealth (class-average)
- Only Tier 2/3 track individual transactions
- Spatial partitioning for market browsing
- Event-driven updates (not every tick)

---

# **APPENDICES**

## **Appendix A: Observable Flow Examples**

### **A.1: Complete Wheat Lifecycle**

**DAY 1 (Spring):**
- Farmer Marcus plants wheat in field
- **Visible:** Marcus walks to field, planting animation

**DAY 90 (Fall):**
- Marcus harvests wheat
- **Visible:** Marcus in field, harvesting animation, wheat appears in hands
- Marcus carries wheat to barn
- **Visible:** Marcus walks holding wheat bundle
- Marcus stores wheat in barn
- **Visible:** Wheat pile grows at barn location

**DAY 91:**
- Baker Anna needs wheat for bread
- Anna checks knowledge: "Who has wheat?" → Knows Marcus
- Anna walks to Marcus's barn
- **Visible:** Anna walking across map
- Anna and Marcus trade (wheat for currency)
- **Visible:** Face-to-face, exchange animation, speech bubbles
- Anna carries wheat to bakery
- **Visible:** Anna walking with wheat

**DAY 92:**
- Anna bakes bread (consumes wheat)
- **Visible:** Anna at oven, wheat disappears, bread appears

**Player can follow entire chain: field → barn → bakery → bread**

---

### **A.2: Tool Production Chain**

**PHASE 1: Resource Extraction**
- Miner Thomas extracts iron ore from mountain
- **Visible:** Thomas at mine, pickaxe animation, ore appears
- Thomas carries ore to stockpile
- **Visible:** Thomas walking with ore, ore pile grows

- Woodcutter Elena chops trees
- **Visible:** Elena at forest, chopping animation, wood appears
- Elena carries wood to stockpile
- **Visible:** Elena walking with wood, wood pile grows

**PHASE 2: Crafting**
- Craftsman Marcus needs to make tools
- Marcus retrieves wood (2 units) + iron (1 unit) from stockpile
- **Visible:** Marcus walking to stockpile, gathering materials
- Marcus at workshop performs crafting
- **Visible:** Marcus at anvil, hammering animation
- 1 week later: Tool appears in Marcus's inventory
- **Visible:** Tool in Marcus's hands, he places in workshop storage

**PHASE 3: Distribution**
- Farmer John needs tool (profession requirement)
- John asks around, learns Marcus sells tools
- John walks to Marcus's workshop
- **Visible:** John traveling
- John and Marcus trade (tool for 15 coins)
- **Visible:** Exchange animation
- John walks away with tool
- **Visible:** Tool visible in John's inventory

**PHASE 4: Use**
- John uses tool to farm
- **Visible:** John in field with tool, harvesting efficiently
- Without tool: John's productivity would be 0%

**Player can trace: Ore/Wood extraction → Crafting → Trade → Farm use**

---

### **A.3: Resource Extraction Sequence**

**FARMING (Wheat):**
1. Farmer checks: "Do I have seeds? Storage space?"
2. Walks to field (visible travel with hoe)
3. Planting animation (spring)
4. Waiting period (summer - tending crops)
5. Harvesting animation (fall)
6. Wheat appears in inventory
7. Walks back to barn
8. Stores wheat (pile grows)

**MINING (Iron Ore):**
1. Miner checks: "Do I have pickaxe? Storage space?"
2. Walks to mine entrance (visible travel with pickaxe)
3. Enters mine (disappears into entrance)
4. Mining animation inside (if visible) or time passes
5. Emerges with ore in inventory
6. Walks to stockpile
7. Stores ore (pile grows)
8. Repeats if inventory not full

**LOGGING (Wood):**
1. Woodcutter checks: "Do I have axe? Storage space?"
2. Walks to forest (visible travel with axe)
3. Targets tree
4. Chopping animation (tree shakes, eventually falls)
5. Wood appears in inventory
6. Walks to stockpile
7. Stores wood (pile grows)
8. Repeats if inventory not full

**FORAGING (Wild Food):**
1. Forager (anyone) walks to wilderness
2. Searches (walking animation, looking around)
3. Finds berry bush/mushrooms
4. Gathering animation
5. Food appears in inventory
6. Walks home
7. Stores in home storage

---

## **Appendix B: Trade Discovery Examples**

### **B.1: Successful Direct Knowledge**

**Scenario:** John needs wheat, already knows Marcus sells it

**Sequence:**
1. John checks `supplier_knowledge["wheat"]`
   - Entry exists: Marcus (supplier_id: 47), reliability: 75
   - Reliability > 20 ✅
2. John thinks: "I'll go to Marcus's farm"
3. John walks directly to Marcus's barn
   - **Visible:** John traveling across map
4. John arrives at barn
5. Trade initiation (see Transaction Examples)

**No asking needed - direct knowledge is efficient**

---

### **B.2: Ask Acquaintance Chain**

**Scenario:** John needs tools, doesn't know any supplier

**Sequence:**
1. John checks `supplier_knowledge["tools"]`
   - Entry doesn't exist
2. John thinks: "I'll ask someone"
3. John selects nearest acquaintance: Sarah (20 meters away)
4. John walks to Sarah
   - **Visible:** John approaching Sarah
5. John initiates conversation
   - Speech bubble (John): "Do you know who has tools?"
6. Sarah checks HER `supplier_knowledge["tools"]`
   - Sarah knows Elena sells tools
7. Sarah responds
   - Speech bubble (Sarah): "Elena the craftsman has tools, her workshop is west of the market"
8. John updates knowledge:
   - `supplier_knowledge["tools"] = {Elena, reliability: 50, timestamp}`
9. John thanks Sarah
   - If Tier 2+ relationship tracked: Affection +2
10. John walks to Elena's workshop
    - **Visible:** John traveling west
11. Trade initiation with Elena

**Information successfully passed through network**

---

### **B.3: Market Fallback**

**Scenario:** John needs rare gem, no one knows who has it

**Sequence:**
1. John checks `supplier_knowledge["gem"]`
   - Entry doesn't exist
2. John asks acquaintance #1 (Sarah)
   - Sarah doesn't know
3. John asks acquaintance #2 (Marcus)
   - Marcus doesn't know
4. John asks acquaintance #3 (Elena)
   - Elena doesn't know
5. All acquaintances exhausted
6. John thinks: "I'll check the market"
7. John walks to nearest market location
   - **Visible:** John traveling to market square
8. John arrives at market (50+ stalls)
9. John begins browsing
   - **Visible:** John walking between stalls, looking at goods
10. Stall 1: Farmer (wheat) - Not needed, continue
11. Stall 2: Craftsman (tools) - Not needed, continue
12. ...
13. Stall 15: Merchant Thomas (various goods including gem)
    - John sees gem!
14. John approaches Thomas
15. John updates knowledge:
    - `supplier_knowledge["gem"] = {Thomas, reliability: 50, timestamp}`
16. Trade initiation

**Market serves as discovery mechanism when networks fail**

---

### **B.4: Supplier Reliability Lifecycle**

**Scenario:** Marcus the wheat farmer gains and loses customers

**WEEK 1: Initial Discovery**
- John asks around, learns "Marcus sells wheat"
- John's knowledge: `{Marcus, reliability: 50}` (secondhand info)

**WEEK 2: First Success**
- John goes to Marcus's barn
- Marcus has wheat ✅
- Trade succeeds
- John's knowledge: `{Marcus, reliability: 60}` (+10)

**WEEK 3: Second Success**
- John returns to Marcus
- Marcus has wheat ✅
- Trade succeeds
- John's knowledge: `{Marcus, reliability: 70}` (+10)

**WEEK 4: Bad Harvest - Out of Stock**
- John returns to Marcus
- Marcus: "Sorry, bad harvest, sold out"
- John disappointed
- John's knowledge: `{Marcus, reliability: 40}` (-30)

**WEEK 5: Still Out of Stock**
- John tries Marcus again (reliability still > 20)
- Marcus: "Still no wheat"
- John frustrated
- John's knowledge: `{Marcus, reliability: 10}` (-30)
- **Reliability < 20 → Entry REMOVED**

**WEEK 6: Finding New Supplier**
- John asks around again
- Learns about new farmer Anna
- John's knowledge: `{Anna, reliability: 50}`
- Trades with Anna successfully
- Anna becomes John's new wheat source

**WEEK 10: Marcus Redeems**
- Marcus has good harvest, brings wheat to market
- Different NPC (Elena) buys from Marcus
- Elena's knowledge: `{Marcus, reliability: 50}` (fresh start)
- Elena tells her acquaintances about Marcus
- Word spreads gradually

**WEEK 15: Marcus Rebuilds**
- 10-15 NPCs now know Marcus sells wheat again
- Marcus back in business, reliability scores increasing
- Loyal customers (if any remained) have high reliability scores
- New customers starting at 50, building up

**Lesson: Reliability creates loyalty, but must be maintained**

---

### **B.5: Information Spread Comparison**

**SCENARIO A: Wheat (Low-Value, Local Spread)**

**Initial Event:**
- Marcus brings 100 wheat to village market
- Price: 3 coins per 10 units (baseline)

**Information Spread:**
- **TRIGGER:** NONE (wheat is boring)
- **Spread Method:** Asked directly only

**Week 1:**
- 3 NPCs buy wheat from Marcus at market
- Only these 3 NPCs add Marcus to `supplier_knowledge["wheat"]`
- No gossip occurs

**Week 2:**
- John (one of the 3) needs wheat again
- Goes directly to Marcus
- Sarah asks John: "Who has wheat?"
- John tells Sarah: "Marcus"
- Sarah adds Marcus to knowledge

**Week 4:**
- Total NPCs who know: 8-10
- All within 1-2 hops of Marcus's customers
- Information radius: ~10-15 NPCs in immediate area

**Week 12:**
- Total NPCs who know: 15-20
- Still local, slow organic growth through direct questioning
- Distant village (5 miles away) has NO knowledge of Marcus

**Result: LOCAL MARKET**
- Only nearby NPCs know Marcus
- Each village has own local wheat suppliers
- No distant NPCs travel for wheat

---

**SCENARIO B: Ruby (High-Value, Global Spread)**

**Initial Event:**
- Thomas brings RUBY (value: 500 coins) to city market
- Displays it at his stall

**Information Spread:**
- **TRIGGER:** Item value > 100 coins → GOSSIP CASCADE
- **Spread Method:** Automatic via social networks

**Hour 1 (Immediate witnesses at market):**
- 5 NPCs at market see ruby
- All react: "WOW! A ruby!"
- Speech bubbles appear
- Each witness (if Social > 30) tells all their acquaintances
- 5 witnesses × 5 acquaintances = 25 NPCs learn

**Hour 3 (Wave 2 - 1 hop away):**
- Of the 25 who learned, 12 are Social personalities
- Each tells THEIR acquaintances
- 12 × 5 = 60 more NPCs learn
- Total: 90 NPCs know about ruby

**Day 1 (Wave 3 - 2 hops away):**
- Social NPCs continue spreading
- Gossip reaches taverns, other markets
- Total: 150-200 NPCs know
- News has spread to neighboring towns (20 miles away)

**Day 3:**
- Total: 300+ NPCs know
- Distant merchants arrive: "I heard there's a ruby!"
- They ask around: "Where's the seller?"
- Directed to Thomas's stall
- Price negotiations begin (multiple interested buyers)

**Week 1:**
- Nearly entire faction (1000+ NPCs) has heard rumor
- Some details fuzzy at distance (accuracy decay - enhancement)
- "There's a ruby somewhere in the capital city"
- Merchants travel from 100+ miles away

**Result: GLOBAL MARKET**
- High-value item attracts distant buyers
- Information travels far and fast
- Price competition emerges (multiple buyers)
- Thomas can charge premium (scarcity + high demand)

**Comparison:**
- Wheat: 20 NPCs know after 3 months (local)
- Ruby: 300 NPCs know after 3 days (global)
- Information spread speed: 45x faster for high-value items

---

## **Appendix C: Market Behavior Examples**

### **C.1: Typical Market Day (Town Market)**

**6:00 AM - Market Opens (Empty)**
- Market square empty except for permanent fixtures
- Early NPCs begin arriving

**8:00 AM - Sellers Arrive**
- 20 farmers walk to market carrying wheat, vegetables
  - **Visible:** Farmers traveling from farms, goods in carts
- 5 craftsmen arrive with tools, goods
  - **Visible:** Craftsmen carrying products
- 3 merchants arrive with diverse inventory
  - **Visible:** Merchants with large packs/carts

**9:00 AM - Stall Setup**
- Farmers find spots, place goods on ground/tables
  - **Visible:** Wheat piles appearing at stalls
- Craftsmen display tools on tables
  - **Visible:** Tools arranged neatly
- Merchants organize diverse goods
  - **Visible:** Multiple item types visible
- Sellers stand at stalls, some call out
  - Speech bubbles: "Fresh wheat!" "Tools for sale!"

**10:00 AM - Buyers Start Browsing**
- 30-40 NPCs enter market area
  - **Visible:** NPCs streaming in from various directions
- Buyers walk between stalls
  - **Visible:** Movement patterns, stopping to look
- Some approach sellers, initiate conversations
  - **Visible:** Face-to-face interactions, speech bubbles

**NOON - Peak Activity**
- 80-100 NPCs present (sellers + buyers)
  - **Visible:** Crowded market, bustling activity
- Multiple trades happening simultaneously
  - **Visible:** Exchange animations at 5-10 stalls
- Sellers with popular goods (wheat) have lines
  - **Visible:** 2-3 buyers waiting per popular stall
- Some stalls sold out, sellers packing up early
  - **Visible:** Empty stalls, sellers leaving

**2:00 PM - Activity Declining**
- Many sellers sold out, departing
  - **Visible:** NPCs leaving with empty carts
- Fewer buyers (most got what they needed)
- 40-50 NPCs remain

**5:00 PM - Market Closes**
- Last sellers pack up
- Unsold goods carried back home
  - **Visible:** Sellers leaving with remaining inventory
- Market square empties
- Next market: Tomorrow morning

---

### **C.2: Transaction Examples**

**SUCCESS: Simple Purchase**

**Setup:**
- John (buyer) needs 10 wheat
- Marcus (seller) has 50 wheat at stall
- Baseline price: 3 coins per 10 wheat

**Sequence:**
1. John approaches Marcus's stall
   - **Visible:** John walking to Marcus
2. John and Marcus face each other
3. John: "I'd like to buy wheat"
   - Speech bubble appears
4. Marcus: "I have plenty. 10 wheat for 3 coins"
   - Speech bubble appears
5. John checks:
   - Can afford? John has 20 coins ✅
   - Need urgency? Moderate (wants to bake bread)
   - Price acceptable? 3 coins = baseline ✅
6. John: "Deal"
   - Speech bubble appears
7. **Exchange animation:**
   - John extends hand with 3 coins
   - Marcus extends hand with wheat
   - Simultaneous swap
8. **Inventory updates (visible):**
   - John: +10 wheat, -3 coins
   - Marcus: -10 wheat, +3 coins
   - Marcus's stall: Wheat pile shrinks
9. **Knowledge updates:**
   - John: `supplier_knowledge["wheat"]["Marcus"] reliability += 10` (now 80)
   - Marcus: Remembers John as customer
10. John: "Thank you"
11. Marcus: "Come again!"
12. John walks away
    - **Visible:** John leaving with wheat visible

**Trade successful, both satisfied**

---

**FAILURE: Can't Afford**

**Setup:**
- Sarah (buyer) needs 1 tool
- Elena (seller) has tools at workshop
- Tool price: 15 coins
- Sarah has: 8 coins

**Sequence:**
1. Sarah approaches Elena's stall
2. Sarah: "I'd like to buy a tool"
3. Elena: "15 coins"
4. Sarah checks:
   - Can afford? 8 < 15 ❌
5. Sarah: "I only have 8 coins"
   - Speech bubble appears
6. Elena: "Sorry, I need 15"
   - Speech bubble appears
7. Sarah: "I understand" (disappointed)
8. Sarah walks away
   - **Visible:** Sarah leaving empty-handed, head down
9. Sarah's options:
   - Work to earn more coins (continue current profession)
   - Find cheaper tool seller (unlikely, baseline price standard)
   - Return later when has 15 coins
   - Switch profession (if cannot afford critical professional requirement)

**Trade failed, Sarah must find currency**

---

**FAILURE: Out of Stock**

**Setup:**
- Thomas (buyer) needs wheat
- Marcus (seller) usually has wheat, but sold out today

**Sequence:**
1. Thomas goes to Marcus's barn (knows Marcus from past trades)
   - **Visible:** Thomas traveling
2. Thomas arrives, looks for wheat pile
   - Wheat pile: EMPTY
3. Thomas: "Do you have any wheat?"
4. Marcus: "Sorry, bad harvest this season. Sold out"
5. Thomas disappointed
6. **Reliability update:**
   - Thomas: `supplier_knowledge["wheat"]["Marcus"] reliability -= 30`
   - Was 70, now 40
7. Thomas walks away
   - **Visible:** Thomas leaving frustrated
8. Thomas's options:
   - Try again tomorrow (reliability still > 20, worth one more attempt)
   - Ask around for other wheat suppliers
   - Go to market to browse

**Trade failed due to supply issue**

---

**FAILURE: Price Too High**

**Setup:**
- Anna (buyer) wants luxury item (fancy cloth)
- Merchant David has it at market
- David's price: 50 coins (2× baseline, Ambitious personality markup)
- Anna has 60 coins but thinks price unfair

**Sequence:**
1. Anna approaches David's stall
2. Anna: "How much for the cloth?"
3. David: "50 coins" (Ambitious, wants high profit)
4. Anna checks:
   - Can afford? 60 > 50 ✅
   - Need urgency? LOW (luxury want, not necessity)
   - Price acceptable? 50 vs baseline 25 = 2× markup ❌
5. Anna (Rational personality): "That's too expensive"
6. David: "That's my price, quality cloth"
7. Anna: "No thanks"
8. Anna walks away
   - **Visible:** Anna leaving without purchase
9. Anna's options:
   - Browse other stalls (maybe cheaper seller)
   - Return later if desperate
   - Go without (it's a luxury, not critical)

**Trade failed due to price disagreement**

**David's situation:**
- If no one buys at 50 coins after a few hours
- David (Ambitious but also Rational): "Maybe I should lower to 40"
- Eventually finds buyer willing to pay premium
- OR lowers price to move inventory

---

## **Appendix D: Economic Pattern Examples**

### **D.1: Local Specialization Pattern**

**Year 1-5: Initial Settlement**

**Village A - "Greenfield":**
- Location: Fertile river valley
- Starting NPCs: 100 (random professions)
- 10 become farmers (good land attracts them)
- Farmers produce wheat efficiently (high yields)

**Village B - "Ironpeak":**
- Location: Near mountains and forest
- Starting NPCs: 100
- 8 become miners (ore deposits visible)
- 5 become woodcutters (abundant trees)
- Resources extracted efficiently

**Year 5: Specialization Emerges**

**Village A:**
- 20 farmers now (others saw farming profitable)
- Wheat production: 2000 units/year
- Local consumption: 500 units/year
- Surplus: 1500 units
- Wheat price in Village A: 2 coins per 10 (abundant, cheap)
- **Problem:** Village A needs tools (few craftsmen, no ore)
- Tool scarcity in Village A → Tool price: 25 coins (expensive)

**Village B:**
- 15 miners + 10 woodcutters
- Ore production: 1000 units/year
- Wood production: 1500 units/year
- 8 craftsmen (materials abundant, easy to craft)
- Tool production: 80 tools/year
- Tool price in Village B: 12 coins (abundant materials, cheap)
- **Problem:** Village B needs food (few farmers, rocky land)
- Food scarcity → Food price: 8 coins per 10 (expensive)

**Year 6: Merchant Emerges**

**NPC: Thomas (Ambitious + Rational)**
- Lives in Village A
- Observes: "Wheat is 2 coins here, but I bet it's expensive in Ironpeak"
- Observes: "Tools are 25 coins here, but cheaper where they're made"
- **Plan:** Buy wheat cheap in Village A, sell in Village B. Buy tools cheap in Village B, sell in Village A.

**Thomas's First Trade Route:**
1. Buy 100 wheat in Village A (cost: 20 coins)
2. Travel to Village B (1 day journey)
3. Sell wheat in Village B (price: 6 coins per 10, revenue: 60 coins)
4. **Profit on wheat:** 40 coins
5. Buy 2 tools in Village B (cost: 24 coins)
6. Travel back to Village A
7. Sell tools in Village A (price: 25 coins each, revenue: 50 coins)
8. **Profit on tools:** 26 coins
9. **Total profit:** 66 coins from one trip

**Year 7-10: Trade Route Establishes**

**Thomas (now Merchant Profession):**
- Makes trip weekly
- Brings wheat to Village B, tools to Village A
- Becomes known: "Thomas the trader"
- 50+ NPCs in each village know him as reliable supplier

**Economic Effects:**
- Village A gets tools (farmers can work)
- Village B gets food (workers don't starve)
- Prices equalize somewhat:
  - Wheat in Village B: 6 → 5 coins (Thomas's supply)
  - Tools in Village A: 25 → 20 coins (Thomas's supply)
- Thomas becomes wealthy (200+ coins saved)

**Year 10: More Merchants Emerge**

- Anna (Ambitious) sees Thomas's success
- Anna imitates: Starts trade route
- Competition: 2 merchants now
- Prices equalize further
- Trade route becomes established economic link

**Year 15: Regional Economy**

- 5 merchants regularly traveling between villages
- Villages specialized but interdependent
- Village A: Agricultural center
- Village B: Industrial center
- Both thrive through trade

**Pattern:** Geographic advantages → Specialization → Trade emerges → Regional integration

---

### **D.2: Merchant Class Emergence**

**Year 1: Everyone is Equal**
- 1000 NPCs, random professions
- No merchants yet (profession doesn't exist formally)
- Everyone produces/consumes basics

**Year 3: First Opportunist**

**NPC: John (Ambitious 60, Rational 70, Social 50)**
- Currently: Farmer
- Observation: "I produce 150 wheat, only need 50. Surplus: 100."
- Observation: "Craftsmen produce tools, I need 1 tool."
- Thought: "If I sell my surplus wheat, I can buy a tool AND have coins left"

**John's First Trade:**
1. Brings 100 wheat to market
2. Sells for 30 coins (baseline 3 per 10)
3. Buys 1 tool for 15 coins
4. **Profit:** 15 coins remaining
5. John realizes: "Trading is profitable!"

**Year 4: John Shifts Strategy**

- John continues farming BUT focuses on surplus
- Produces extra wheat specifically to trade
- Starts buying diverse goods at market (when cheap)
- Stockpiles in barn: Wheat, wood, occasional tool

**Year 5: John Becomes Known**

- 20 NPCs have John in `supplier_knowledge` for various goods
- John's barn has diverse inventory:
  - 200 wheat
  - 50 wood
  - 10 tools (bought cheap, selling at markup)
  - 5 weapons (rare, acquired from traveling NPC)
- John spends more time at market than farm
- **Occupation transition:** Farmer → Merchant (emergent, not assigned)

**Year 6: Full-Time Merchant**

- John stops farming entirely
- Buys from producers, sells to consumers
- Profit margin: 20-30% markup
- Makes 5-10 trades per week
- Wealth: 500 coins (rich tier)

**Year 7: Competition Emerges**

**NPC: Sarah (Ambitious 70, Rational 65, Deceitful 30)**
- Observes John's success: "He's rich from trading!"
- Sarah (currently Craftsman) tries trading
- Sells crafted goods, buys raw materials to resell
- Becomes second merchant

**Year 10: Merchant Class Established**

- 8 NPCs now primarily merchants
- All Ambitious + Rational personalities
- Some honest (fair prices), some deceitful (markup)
- Merchants know each other (competitors but also information sources)
- Control 30% of all trades
- Average wealth: 800 coins (vs 100 for farmers)

**Year 15: Merchant Specialization**

- **Luxury Merchant:** Deals only in high-value items (gems, masterwork weapons)
- **Food Merchant:** Bulk wheat/food trade between regions
- **Tool Merchant:** Connects craftsmen with farmers/soldiers
- **General Merchant:** Diverse goods, "one-stop shop"

**Year 20: Merchant Political Power**

- Wealthiest merchants (3000+ coins) gain influence
- Form merchant faction/guild
- Begin influencing faction policies (enhancement: economic policy)
- Some merchants become Tier 3 NPCs (major players)

**Pattern:** Opportunity recognized → Profit-seeking behavior → Specialization → Class emergence → Power concentration

---

### **D.3: Boom-Bust Cycle**

**BOOM PHASE**

**Year 1: Tool Shortage**
- Situation: 5 craftsmen, 60 farmers
- Tool demand: 60 (1 per farmer)
- Tool supply: 20/year (craftsmen can't keep up)
- **Scarcity:** Demand/Supply = 60/20 = 3.0 (SEVERE shortage)
- Tool price: 15 coins baseline → 40 coins (scarcity premium)
- Farmers desperate: "I need a tool to work!"

**Year 2: Craftsmen Profit**
- Craftsmen earning 40 coins per tool (vs 15 baseline)
- Craftsmen wealth increasing rapidly
- Craftsmen occupation satisfaction: +40 (making good money)
- **Observation spreads:** "Craftsmen are getting rich!"

**Year 3: Rush to Crafting**
- 10 NPCs see opportunity, switch to craftsman
  - Ambitious NPCs (want wealth)
  - Rational NPCs (calculated it's profitable)
- Total craftsmen: 5 → 15
- Tool production: 20/year → 60/year

**EQUILIBRIUM APPROACHED**

**Year 4: Supply Catches Up**
- Tool demand: 60
- Tool supply: 60
- **Scarcity:** 60/60 = 1.0 (BALANCED)
- Tool price: 40 → 18 coins (normalizing toward baseline)
- Farmers: "Finally, tools are available!"
- Craftsmen: "Prices dropping, but still profitable"

**BUST PHASE**

**Year 5: Oversupply Begins**
- More NPCs became craftsmen (momentum from Year 3 decisions)
- Total craftsmen: 15 → 22
- Tool production: 60 → 88/year
- Tool demand: 60 (unchanged, farmers only need 1 tool)
- **Scarcity:** 60/88 = 0.68 (SURPLUS)
- Tool price: 18 → 12 coins (below baseline)

**Year 6: Bust Deepens**
- Craftsmen competing for customers
- Many craftsmen: "I can't sell my tools!"
- Craftsmen wealth declining
- Craftsmen occupation satisfaction: -30 (not making money)
- Some craftsmen have tools in storage, unsold

**Year 7: Correction Begins**
- 8 craftsmen switch professions (cannot sustain)
  - Some → Farmer (always need food)
  - Some → Soldier (if war)
  - Some → Merchant (try different trade)
- Total craftsmen: 22 → 14
- Tool production: 88 → 56/year

**RETURN TO BOOM**

**Year 8: Shortage Re-emerges**
- Tool demand: 60
- Tool supply: 56
- **Scarcity:** 60/56 = 1.07 (slight shortage)
- Tool price: 12 → 16 coins (rising)
- Craftsmen: "Business picking up again"

**Year 9: Cycle Repeats**
- Prices rising attracts new craftsmen
- Boom phase begins again

**LONG-TERM PATTERN:**

```
Year 1-3:  BOOM (shortage, high prices)
Year 4:    EQUILIBRIUM (balanced)
Year 5-7:  BUST (oversupply, low prices)
Year 8:    EQUILIBRIUM (balanced)
Year 9+:   BOOM (shortage, cycle repeats)

Cycle length: ~6-8 years
Amplitude: Decreases over time (smaller swings)
Eventually: Settles near equilibrium with minor oscillations
```

**Why Cycle Exists:**
- Information lag: NPCs don't know how many others are switching
- Production lag: Takes time to train as craftsman, produce tools
- Momentum: Decisions made in Year 3 affect Years 4-6
- No central planning: Decentralized decisions create overshooting

**Why Cycle Dampens:**
- NPCs learn patterns (memory, enhancement)
- Barriers to entry limit switching
- Some NPCs become stable (Content personality)
- Market matures, stabilizes

---

### **D.4: Trade Hub Emergence**

**Year 1-5: Three Equal Towns**

**Town A, B, C:**
- Each: 500 NPCs
- Each: Small local market (20 stalls)
- Each: Self-sufficient (farms, craftsmen, basic goods)
- Trade between towns: Minimal (distance, no infrastructure)

**Year 6: Geographic Advantage**

**Town B - "Crossroads":**
- Location: Central, between Town A and Town C
- New development: Road built (faction project)
- Travel time: A→B = 1 day, B→C = 1 day, A→C = 3 days

**Merchant calculus:**
- Merchant from Town A wants to reach Town C
- Direct: 3 days travel
- Via Town B: 2 days total, can trade at B's market
- **Decision:** Stop at Town B market, sell some goods, buy new goods, continue

**Year 7: Traffic Increases**

- 5 merchants regularly pass through Town B
- They sell excess inventory at B's market
- They buy new goods to resell in destination
- Town B market gains variety:
  - Goods from Town A (agricultural)
  - Goods from Town C (industrial)
  - Local Town B goods

**Year 8: Information Hub**

- Gossip spreads: "Town B's market has everything!"
- Social NPCs from A and C travel to B specifically for market
- Town B's market grows: 20 → 40 stalls
- More merchants attracted (good customer base)

**Year 10: Positive Feedback Loop**

**Loop:**
1. More merchants → More goods variety
2. More variety → More customers travel to B
3. More customers → More profitable for merchants
4. More profitable → More merchants attracted
5. Return to step 1 (cycle)

**Town B's Market:**
- 100+ stalls
- Daily market now major event
- Attracts NPCs from 50+ miles
- Luxury goods appear (high-value items drawn to large market)
- Gossip spreads far: "Town B is the trade capital"

**Year 15: Dominance Established**

**Town B:**
- Population: 500 → 1200 (NPCs moving there for opportunity)
- Market: 200+ stalls, daily crowds of 300-400
- Merchant quarter established (20+ full-time merchants)
- Wealth concentration: Town B's average wealth 2× other towns
- Political power: Town B's faction gains influence (wealth = power)

**Towns A and C:**
- Markets shrink: 20 → 12 stalls (merchants prefer Town B)
- Local goods only, less variety
- Some NPCs migrate to Town B (especially Ambitious)
- Become supplier towns for Town B (agricultural/industrial base)

**Year 20: Regional Capital**

- Town B: Undisputed trade hub
- Controls regional economy
- Monthly fair draws 1000+ NPCs
- Rare items only appear at Town B market
- Faction headquarters may relocate there (power follows wealth)

**Pattern:** Geographic advantage → Traffic concentration → Positive feedback → Dominance → Regional restructuring

---

### **D.5: Economic Stratification Over Time**

**Year 1: Equality**

**All 1000 NPCs:**
- Start with ~50 coins each
- Random professions assigned
- No wealth inequality yet

**Year 5: Early Divergence**

**Emerging Rich (5% of NPCs, 50 NPCs):**
- Merchants (early adopters who started trading)
- Successful craftsmen (high-demand goods)
- Lucky farmers (inherited good land)
- **Wealth:** 200-500 coins
- **Income:** 20-30 coins/week

**Middle Class (70%, 700 NPCs):**
- Working farmers, craftsmen, soldiers
- Steady income from labor
- **Wealth:** 50-150 coins
- **Income:** 5-10 coins/week

**Poor (25%, 250 NPCs):**
- Struggling farmers (bad land)
- Unemployed (switched professions, between jobs)
- **Wealth:** 10-50 coins
- **Income:** 2-5 coins/week

**Year 10: Stratification Deepens**

**Rich (3%, 30 NPCs):**
- **Who:** Successful merchants, master craftsmen, landowners
- **Wealth:** 1000-3000 coins
- **Income:** Passive (rents, trade profits) + active labor
- **Behavior:**
  - Buy luxury goods (status display)
  - Invest in businesses (fund other merchants)
  - Political influence emerging (Tier 3 NPCs)
- **Personality:** Mostly Ambitious + Rational

**Upper Middle (12%, 120 NPCs):**
- **Who:** Prosperous farmers, skilled craftsmen, merchants
- **Wealth:** 300-1000 coins
- **Income:** 15-25 coins/week
- **Behavior:**
  - Comfortable living
  - Can afford occasional luxuries
  - Savings buffer for emergencies

**Middle Class (60%, 600 NPCs):**
- **Who:** Working farmers, craftsmen, soldiers, servants
- **Wealth:** 50-300 coins
- **Income:** 5-15 coins/week
- **Behavior:**
  - Meet basic needs
  - Little savings
  - Vulnerable to shocks (bad harvest, war)

**Poor (20%, 200 NPCs):**
- **Who:** Struggling workers, bad land, low skills
- **Wealth:** 10-50 coins
- **Income:** 2-5 coins/week
- **Behavior:**
  - Barely surviving
  - May skip meals
  - One crisis from destitution

**Destitute (5%, 50 NPCs):**
- **Who:** Bandits (desperation), beggars, unemployed
- **Wealth:** 0-10 coins
- **Income:** Sporadic (theft, charity)
- **Behavior:**
  - Starvation risk
  - Crime for survival
  - May die if no support

**Year 20: Entrenched Classes**

**Very Rich (1%, 10 NPCs):**
- **Wealth:** 5000-10000+ coins
- **Income:** Primarily passive (owns businesses, land, trade routes)
- **Tier:** Mostly Tier 3 (major players)
- **Power:** Control factions, influence policy
- **Dynasties:** Children inherit wealth, perpetuate class

**Rich (4%, 40 NPCs):**
- **Wealth:** 2000-5000 coins
- **Income:** Mix of passive + active
- **Tier:** Tier 2/3
- **Power:** Local influence, guild leaders

**Upper Middle (10%, 100 NPCs):**
- **Wealth:** 500-2000 coins
- **Tier:** Mostly Tier 2
- **Aspiration:** Some may reach Rich through luck/skill

**Middle Class (50%, 500 NPCs):**
- **Wealth:** 100-500 coins
- **Stable:** Routine, predictable life
- **Limited mobility:** Hard to move up without opportunity

**Lower Class (25%, 250 NPCs):**
- **Wealth:** 20-100 coins
- **Vulnerable:** Shocks push toward poverty

**Poor (8%, 80 NPCs):**
- **Wealth:** 5-20 coins
- **Desperate:** May become bandits, beggars

**Destitute (2%, 20 NPCs):**
- **Wealth:** 0-5 coins
- **Survival:** Crime, charity, or death

**Factors Creating Stratification:**

**Positive Feedback (Rich get Richer):**
- Wealth → Invest in business → More wealth
- Wealth → Buy land → Rent income → More wealth
- Wealth → Children inherit advantage

**Negative Feedback (Poor Stay Poor):**
- No capital → Cannot start business
- Bad land → Low yields → Low income
- No savings → Crisis = catastrophe
- Children inherit poverty

**Personality Selection:**
- Ambitious NPCs more likely to become rich (seek opportunity)
- Content NPCs stay middle class (satisfied with stability)
- Cautious NPCs avoid risks (miss opportunities)

**Random Luck:**
- Right place/right time (found rare gem)
- Wrong place/wrong time (war destroyed farm)
- Inheritance (parent was rich merchant)

**Social Mobility:**
- **Upward:** Possible but rare (5% move up a class per generation)
- **Downward:** More common (10% move down due to shocks)
- **Barriers:** Capital requirements, education/skills, social networks

**Pattern:** Initial randomness → Opportunity exploitation → Wealth concentration → Feedback loops → Class stratification → Generational persistence

---

## **Appendix E: Integration Examples**

### **E.1: Need-Driven Trade Decisions**

**Scenario: Peasant John (Tier 1 NPC)**

**Current State:**
- Need Level: SECURITY (has food, wants stable life)
- Occupation: Farmer
- Current Productivity: 0% (lacks tools)
- Currency: 20 coins
- Goal: "Acquire tools to farm efficiently"

**Trade Decision Process:**

1. **Need Assessment:**
   - SURVIVAL: Met ✅ (has food stored)
   - SECURITY: Threatened ❌ (cannot farm without tools = no future income)

2. **Goal Generation (AI Systems - Core, Section 2.6.3):**
   - Need level: SECURITY
   - Profession: Farmer
   - Missing requirement: Tools (AI Systems - Core, Section 2.5.3)
   - **Generated Goal:** "Buy tools to restore productivity"

3. **Resource Search:**
   - Check knowledge: Does John know who sells tools?
   - Yes: Marcus sells tools (reliability 75)
   - Decision: Go to Marcus

4. **Trade Evaluation:**
   - Arrive at Marcus's workshop
   - Marcus: "Tools cost 15 coins"
   - **Affordability:** 20 coins > 15 coins ✅
   - **Need Urgency:** HIGH (critical for profession)
   - **Price Evaluation:**
     - Baseline: 15 coins
     - John's assessment: "Without tools, I cannot farm. This is worth ANY price I can afford."
   - **Decision:** BUY (even though 75% of total wealth)

5. **Post-Trade:**
   - John's currency: 20 → 5 coins (now poor)
   - John's tools: 0 → 1 ✅
   - John's productivity: 0% → 100% ✅
   - John's goal: ACHIEVED
   - **New goal generated:** "Produce surplus wheat to rebuild savings"

6. **Emotional/Satisfaction:**
   - SECURITY need: Progressing (can work again)
   - Mood: +20 (crisis averted)
   - Occupation satisfaction: -10 → +30 (can function again)

**Alternative: If John Couldn't Afford (had 10 coins):**
1. Cannot buy tools
2. SECURITY need: FAILING
3. Occupation satisfaction: -50 (cannot work)
4. New goals considered:
   - "Borrow coins from friend" (if has Tier 2 relationship with Trust > 50)
   - "Sell other possessions to get 15 coins"
   - "Switch to profession that doesn't need tools" (forager, laborer)
   - "Become bandit" (if Desperate + Low Loyalty, AI Doc 2.5.3)

---

### **E.2: Professional Requirements Economic Chain**

**Scenario: Tool Production Chain Creates Economic Flow**

**PHASE 1: Raw Material Extraction**

**Miner Thomas (Tier 1):**
- Occupation: Miner
- Need: SECURITY (steady income)
- Activity: Extracts 50 iron ore/week
- Personal use: 0 (miners don't use ore)
- Surplus: 50 ore/week
- **Economic motivation:** "I produce ore to sell for currency"

**Woodcutter Elena (Tier 1):**
- Occupation: Woodcutter
- Need: SECURITY
- Activity: Extracts 80 wood/week
- Personal use: 10 wood (home repairs)
- Surplus: 70 wood/week
- **Economic motivation:** "I produce wood to sell"

**PHASE 2: Crafting Demand**

**Craftsman Marcus (Tier 1):**
- Occupation: Craftsman
- Need: SECURITY
- **Professional requirement:** Needs wood + ore to craft (AI Systems - Core, Section 3.3)
- Activity: Crafts tools
- Input per tool: 2 wood + 1 ore
- Can craft: 10 tools/week (if has materials)
- Personal use: 1 tool (for himself)
- Surplus: 9 tools/week

**Marcus's Material Need:**
- Weekly need: 20 wood + 10 ore
- **Problem:** Marcus doesn't produce wood/ore
- **Solution:** MUST trade for materials

**PHASE 3: Derived Demand (Marcus Needs Materials)**

**Marcus's Trade Behavior:**
1. Needs wood: Checks supplier knowledge → Knows Elena
2. Goes to Elena's location
3. Buys 20 wood for 4 coins
4. Needs ore: Checks supplier knowledge → Knows Thomas
5. Goes to Thomas's location
6. Buys 10 ore for 8 coins
7. **Total spent:** 12 coins on materials

**Economic Effect:**
- Thomas earns 8 coins/week (selling ore)
- Elena earns 4 coins/week (selling wood)
- Both have stable income (SECURITY need met)

**PHASE 4: End-User Demand (Farmers Need Tools)**

**Farmer John (Tier 1):**
- Occupation: Farmer
- **Professional requirement:** Needs 1 tool to farm (AI Systems - Core, Section 3.3)
- Current tools: 0 (old tool broke)
- Productivity without tool: 0%
- **Crisis:** Cannot farm, no income

**John's Trade Behavior:**
1. Needs tool urgently (SECURITY threatened)
2. Checks supplier knowledge → Knows Marcus
3. Goes to Marcus's workshop
4. Buys 1 tool for 15 coins
5. **Can now farm:** Productivity 0% → 100%

**Economic Effect:**
- Marcus earns 15 coins/tool
- 9 tools sold/week = 135 coins revenue
- Material cost: 12 coins
- **Marcus's profit:** 123 coins/week (very profitable)

**PHASE 5: Complete Economic Chain**

```
Thomas (Miner) → Ore → Marcus (Craftsman) → Tools → John (Farmer) → Food → Everyone
Elena (Wood) ↗                                                             ↓
                                                                   (Currency flows back)
```

**Currency Flow:**
1. John sells wheat → Earns 30 coins
2. John buys tool from Marcus → Marcus earns 15 coins
3. Marcus buys materials from Thomas/Elena → They earn 12 coins total
4. Thomas/Elena buy food from farmers → Currency returns

**Interdependence:**
- Farmers need craftsmen (for tools)
- Craftsmen need miners/woodcutters (for materials)
- Miners/woodcutters need farmers (for food)
- **Everyone needs everyone → Trade network forms naturally**

**If Chain Breaks:**

**Scenario: All Miners Die (War, Disaster)**
1. No ore production
2. Marcus cannot craft tools (missing materials)
3. Farmers' tools break over time, no replacements
4. Farming productivity drops
5. Food shortage
6. Economic crisis
7. **Recovery:** NPCs switch to miner (high demand, high prices)

---

### **E.3: Personality-Driven Economic Behavior**

**Scenario: Five NPCs Need Wheat - Different Approaches**

**All 5 NPCs:**
- Need: Wheat (10 units)
- Market: Town market has 3 wheat sellers
  - Marcus: 10 wheat for 3 coins (baseline)
  - Anna: 10 wheat for 2.5 coins (Content, lower price)
  - David: 10 wheat for 4 coins (Ambitious, higher price)

---

**NPC 1: John (Ambitious 60, Rational 70)**

**Behavior:**
1. Arrives at market
2. Doesn't buy from first seller (Marcus)
3. Browses all stalls (systematic)
4. Compares prices:
   - Marcus: 3 coins
   - Anna: 2.5 coins ✅ (best price)
   - David: 4 coins
5. Calculates: "Anna's price saves me 0.5 coins"
6. Goes to Anna, buys at 2.5 coins
7. **Personality effect:** Rational → Optimizes, Ambitious → Seeks best deal

---

**NPC 2: Sarah (Cautious 60, Content 50)**

**Behavior:**
1. Arrives at market, nervous (Cautious)
2. Approaches first seller (Marcus) immediately
3. Marcus: "3 coins"
4. Sarah: "That sounds fair" (avoids negotiation)
5. Buys immediately (doesn't browse others)
6. **Personality effect:** Cautious → Avoids uncertainty, accepts first reasonable offer

---

**NPC 3: Thomas (Social 70, Kind 60)**

**Behavior:**
1. Arrives at market
2. Sees Marcus, recognizes him (acquaintance)
3. Thomas: "Hey Marcus! How's the family?" (Social)
4. Chats for 2 minutes (relationship building)
5. Marcus: "3 coins for wheat"
6. Thomas: "Deal!" (supports friend, Kind)
7. Buys from Marcus despite not best price
8. **Personality effect:** Social → Values relationships, Kind → Supports friends over profit

---

**NPC 4: Elena (Deceitful 50, Ambitious 60)**

**Behavior:**
1. Arrives at market
2. Browses, finds Anna (2.5 coins, best price)
3. Elena: "I only have 2 coins" (LIE - actually has 10 coins)
4. Anna (Kind personality): "Okay, 2 coins is fine" (helps poor person)
5. Elena buys at 2 coins (saved extra 0.5 coins by lying)
6. **Personality effect:** Deceitful → Manipulates, Ambitious → Maximizes personal gain

**Long-term consequence:**
- If Anna discovers the lie (finds out Elena had more money):
  - Anna's Trust in Elena: -50
  - Relationship damaged
  - Anna won't trade with Elena in future
  - Word may spread (if Anna is Social)

---

**NPC 5: Marcus2 (Traditional 60, Honest 70)**

**Behavior:**
1. Arrives at market
2. Goes to Marcus (same name, coincidence)
3. Marcus seller: "3 coins"
4. Marcus2: "That's the fair price" (knows baseline)
5. Buys at 3 coins without haggling
6. **Personality effect:** Honest → Pays fair price, Traditional → Respects established norms

---

**Comparison Summary:**

| NPC | Personality | Price Paid | Reason |
|-----|------------|------------|--------|
| John | Ambitious/Rational | 2.5 coins | Optimized, found best deal |
| Sarah | Cautious/Content | 3 coins | Accepted first offer, avoided uncertainty |
| Thomas | Social/Kind | 3 coins | Bought from friend, values relationship |
| Elena | Deceitful/Ambitious | 2 coins | Lied to get discount |
| Marcus2 | Traditional/Honest | 3 coins | Paid fair baseline price |

**Economic Effects:**

**For Sellers:**
- Anna: Got 2 sales (best price attracts Rational shoppers)
- Marcus: Got 2 sales (Social/Traditional loyalty)
- David: Got 0 sales (price too high)
- **Lesson:** Pricing affects customer base, but relationships matter

**For System:**
- Same need (wheat), diverse behaviors
- Personality visible in economic choices
- Reputation builds (Thomas loyal to Marcus, Elena damages trust)
- Market dynamics emerge (David may lower price if no sales)

---

## **Appendix F: Quick Reference Tables**

### **F.1: Resource Baseline Prices**

| Resource (10 units unless noted) | Baseline Price | Production Time | Producers |
|----------------------------------|---------------|-----------------|-----------|
| Food (Wild) | 4 coins | Instant (foraging) | Anyone |
| Food (Crops/Wheat) | 3 coins | Annual cycle | Farmers |
| Wood | 2 coins | 1-2 hours | Woodcutters |
| Stone | 3 coins | 2-3 hours | Miners |
| Iron Ore | 8 coins | 3-4 hours | Miners |
| Precious Ore | 50+ coins | Rare finds | Miners |
| Tool (1 unit) | 15 coins | 1 week | Craftsmen |
| Weapon (1 unit) | 25 coins | 2 weeks | Craftsmen |
| Basic Goods (1 unit) | 5 coins | 3-5 days | Craftsmen |
| Building Materials (1 unit) | 30 coins | 2 weeks | Craftsmen |
| Luxury Good | 50-500 coins | Varies | Craftsmen/Merchants |

---

### **F.2: Wealth Tiers**

| Tier | Currency Range | % of Population | Economic Status |
|------|---------------|-----------------|-----------------|
| Destitute | 0-10 | 2-5% | Starvation risk, crime |
| Poor | 10-50 | 8-20% | Barely surviving |
| Lower Class | 50-100 | 20-25% | Vulnerable to shocks |
| Middle Class | 100-500 | 50-60% | Stable, routine life |
| Upper Middle | 500-2000 | 10-12% | Comfortable, some luxuries |
| Wealthy | 2000-5000 | 3-4% | Significant surplus |
| Rich | 5000-10000 | 1-2% | Land ownership, influence |
| Very Rich | 10000+ | <1% | Faction power, dynasties |

---

### **F.3: Market Types**

| Market Type | NPCs | Frequency | Stalls | Coverage Radius | Goods |
|-------------|------|-----------|--------|-----------------|-------|
| Village | 100-500 | Daily | 10-20 | 5 miles | Basics only |
| Town | 500-2000 | Daily + Weekly Fair | 50-100 | 20 miles | Basics + some luxuries |
| City | 2000-10000 | Daily + Monthly Fair | 100-200+ | Civilization-wide | Everything |
| Crossroads | Varies | Sporadic | 20-50 | Trade routes | Traveling goods |

---

### **F.4: Acquaintance Limits by Tier**

| Tier | Max Acquaintances | Supplier Knowledge Scope | Relationship Tracking |
|------|------------------|--------------------------|----------------------|
| Tier 1 (90%) | 5-10 | Limited (5-10 resources) | None (faction only) |
| Tier 2 (9%) | 20-50 | Moderate (10-20 resources) | Yes (20 relationships) |
| Tier 3 (1%) | 50-100 | Extensive (20+ resources) | Yes (50-100 relationships) |

---

### **F.5: Information Spread Types**

| Good Type | Spread Method | Trigger | Range | Speed | Example |
|-----------|--------------|---------|-------|-------|---------|
| Low-Value | Asked directly | None | 10-15 NPCs | Slow (weeks) | Wheat, wood, stone |
| High-Value | Gossip cascade | Value > 100 coins | 100-300+ NPCs | Fast (days) | Ruby, masterwork weapon |

---

### **F.6: Reliability Score Meanings**

| Score | Interpretation | Player Visible Behavior |
|-------|---------------|------------------------|
| 100 | Always has stock | NPC goes directly every time |
| 70-99 | Very reliable | NPC prefers this supplier |
| 50-69 | Moderately reliable | NPC uses but may try others |
| 20-49 | Questionable | NPC wary, asks around first |
| <20 | Unreliable | Entry removed, NPC forgets |

---

### **F.7: Personality Economic Behaviors**

| Personality | Trade Behavior | Market Behavior | Occupation Preference |
|------------|---------------|----------------|---------------------|
| Ambitious | Seeks high-value, travels far | Stays long, high prices | Merchant, profitable roles |
| Cautious | Local suppliers, first offer | Leaves if slow, low prices | Stable (farmer, craftsman) |
| Rational | Calculates value, optimizes | Observes supply/demand | Analyzes economics |
| Social | Large network, relationship trades | Chats, attracts customers | Merchant, people-facing |
| Honest | Fair prices, keeps promises | Transparent, builds trust | Any, reputation matters |
| Deceitful | Manipulates, overcharges | Short-term profit | Merchant (if not caught) |
| Content | Accepts "good enough" | Doesn't browse much | Farmer, simple work |
| Kind | May trade at loss for friends | Helps others | Service roles |

---

