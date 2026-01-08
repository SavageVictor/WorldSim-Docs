---
layout: default
title: Core Philosophy
parent: Core Systems
grand_parent: Economic Systems
nav_order: 1
---

**Related Documents:**
- AI Systems - Core (main AI behavior systems)
- AI Systems - Enhancements (future AI features)
- Economic Systems - Enhancements (future economic features)
- [Future] Resource Encyclopedia (detailed resource specs, interactions, visuals)


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