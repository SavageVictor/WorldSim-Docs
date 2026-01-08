---
layout: default
title: Currency & Value
parent: Core Systems
grand_parent: Economic Systems
nav_order: 6
---

**Related Documents:**
- AI Systems - Core (main AI behavior systems)
- AI Systems - Enhancements (future AI features)
- Economic Systems - Enhancements (future economic features)
- [Future] Resource Encyclopedia (detailed resource specs, interactions, visuals)


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
|-------------|---------------|------------------|
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