---
layout: default
title: Market Systems
parent: Core Systems
grand_parent: Economic Systems
nav_order: 5
---

**Related Documents:**
- AI Systems - Core (main AI behavior systems)
- AI Systems - Enhancements (future AI features)
- Economic Systems - Enhancements (future economic features)
- [Future] Resource Encyclopedia (detailed resource specs, interactions, visuals)


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