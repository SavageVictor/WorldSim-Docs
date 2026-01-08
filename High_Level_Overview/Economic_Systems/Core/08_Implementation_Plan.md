---
layout: default
title: Implementation Plan
parent: Core Systems
grand_parent: Economic Systems
nav_order: 8
---

**Related Documents:**
- AI Systems - Core (main AI behavior systems)
- AI Systems - Enhancements (future AI features)
- Economic Systems - Enhancements (future economic features)
- [Future] Resource Encyclopedia (detailed resource specs, interactions, visuals)


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