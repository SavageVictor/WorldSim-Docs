---
layout: default
title: Production Systems
parent: Core Systems
grand_parent: Economic Systems
nav_order: 3
---

**Related Documents:**
- AI Systems - Core (main AI behavior systems)
- AI Systems - Enhancements (future AI features)
- Economic Systems - Enhancements (future economic features)
- [Future] Resource Encyclopedia (detailed resource specs, interactions, visuals)


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