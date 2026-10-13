---
layout: default
title: Home
nav_order: 1
description: "WorldSim documentation - Complex world simulation with emergent AI and dynamic economies"
permalink: /
---

# WorldSim Documentation

{: .fs-9 }

A complex world simulation featuring emergent AI behavior, dynamic economies, and rich factional politics.
{: .fs-6 .fw-300 }

[Get Started](#-quick-start){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[View on GitHub](https://github.com/SavageVictor/WorldSim-Docs){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## 📚 Documentation Structure

### AI Systems

The AI systems define how NPCs think, feel, and interact with each other and the world.

**Core Systems (MVP):**
- [Executive Summary](./High_Level_Overview/AI_Systems/Core/01_Executive_Summary.md) - Philosophy & priorities
- [NPC Tiering](./High_Level_Overview/AI_Systems/Core/02_NPC_Tiering.md) - 90/9/1 distribution
- [Personality System](./High_Level_Overview/AI_Systems/Core/03_Personality.md) - 7 traits driving behavior
- [Relationships](./High_Level_Overview/AI_Systems/Core/04_Relationships.md) - Multi-dimensional bonds
- [Factions](./High_Level_Overview/AI_Systems/Core/05_Factions.md) - Group dynamics
- [Occupations](./High_Level_Overview/AI_Systems/Core/06_Occupations.md) - Dynamic careers
- [Needs & Goals](./High_Level_Overview/AI_Systems/Core/07_Needs_Goals.md) - Maslow hierarchy
- [More...](./High_Level_Overview/AI_Systems)

**Enhancements (Post-MVP):**
- [Promotion System](./High_Level_Overview/AI_Systems/Enhancements/02_Promotion_System.md) - Tier advancement
- [Future Systems](./High_Level_Overview/AI_Systems/Enhancements/03_Future_Systems.md) - Religion, combat, etc.
- [More...](./High_Level_Overview/AI_Systems)

### Economic Systems

The economic systems create realistic trade, production, and resource flow dynamics.

**Core Systems (MVP):**
- [Core Philosophy](./High_Level_Overview/Economic_Systems/Core/01_Core_Philosophy.md) - Observable, physical, emergent
- [Resource Systems](./High_Level_Overview/Economic_Systems/Core/02_Resource_Systems.md) - Categories & inventory
- [Production](./High_Level_Overview/Economic_Systems/Core/03_Production_Systems.md) - Extraction & crafting
- [Trade & Commerce](./High_Level_Overview/Economic_Systems/Core/04_Trade_Commerce.md) - Networks & discovery
- [Markets](./High_Level_Overview/Economic_Systems/Core/05_Market_Systems.md) - Physical locations
- [More...](./High_Level_Overview/Economic_Systems)

**Enhancements (Post-MVP):**
- [Tier 1](./High_Level_Overview/Economic_Systems/Enhancements/02_Tier1_Enhancements.md) - Dynamic pricing, negotiation
- [Tier 2](./High_Level_Overview/Economic_Systems/Enhancements/03_Tier2_Enhancements.md) - Barter, reputation
- [More...](./High_Level_Overview/Economic_Systems)

### Visual Design

- [**Visual Design**](./High_Level_Overview/Visual_Design/Visual_Design_Rant.md) - Art style and camera perspective

### Demo II

- [**Demo II**](./Demo_II/index.md) - Design meeting transcripts and the next steps derived from them
- [**Next Steps**](./Demo_II/Next_Steps.md) - Decisions, workstreams, open questions and risks

---

## 🎯 Quick Start

### For Developers

1. Start with [AI Systems - Core](./High_Level_Overview/AI_Systems) to understand foundational behavior systems
2. Review [Economic Systems - Core](./High_Level_Overview/Economic_Systems) for economic integration
3. See enhancement documents for post-MVP features

### For Designers

1. Read the **Design Rationale** sections ([AI](./High_Level_Overview/AI_Systems/Core/13_Design_Rationale.md) | [Economy](./High_Level_Overview/Economic_Systems/Core/01_Core_Philosophy.md))
2. Review **Emergence Pattern Examples** in appendices
3. Check **Success Metrics** to understand goals

### For Game Masters / Players

1. Explore **Personality Behavior Examples** ([link](./High_Level_Overview/AI_Systems/Core/14_Appendices.md)) to understand NPC types
2. Study **Faction Dynamics** ([link](./High_Level_Overview/AI_Systems/Core/05_Factions.md)) to grasp political systems
3. Learn **Occupation Emergence** ([link](./High_Level_Overview/AI_Systems/Core/06_Occupations.md)) to see career paths

---

## 🔑 Key Concepts

### Emergence Over Scripting

Stories emerge from system interactions rather than pre-written narratives. No two playthroughs are identical.

### Observable Economy

Every resource has physical presence. Players can trace wheat from field → barn → market → baker.

### Tiered Complexity

- **90% Tier 1 NPCs**: Simplified simulation (the masses)
- **9% Tier 2 NPCs**: Notable figures with individual relationships
- **1% Tier 3 NPCs**: Major players shaping civilization

### Personality Drives All

7 personality traits (Courage, Loyalty, Ambition, Kind/Cruel, Honest/Deceitful, Rational/Emotional, Traditional/Progressive) determine every decision.

---

## 📊 System Overview

```
┌─────────────────────────────────────────────────────────┐
│                    10,000 NPCs                          │
├─────────────────────────────────────────────────────────┤
│  Personality (7 traits) → Behavior                      │
│  Relationships (faction + individual) → Social Dynamics │
│  Needs (Maslow hierarchy) → Goals                       │
│  Occupations (dynamic) → Economy                        │
│  Memory (events) → Learning                             │
│  Reputation (gossip) → Social Pressure                  │
├─────────────────────────────────────────────────────────┤
│  Individual Decisions → Emergent Civilization           │
└─────────────────────────────────────────────────────────┘
```

---

## 🎨 Design Philosophy

### Three Pillars

1. **Observable**: Players can see and understand cause-and-effect chains
2. **Physical**: Resources exist as actual items, NPCs must travel and carry
3. **Emergent**: Economy, politics, and stories arise from individual NPC decisions

### Core Goals

- ✅ Believable NPCs with distinct personalities
- ✅ Emergent narratives players want to share
- ✅ Scalable to 10,000 NPCs at 60 FPS
- ✅ Deep systems where needed, abstraction where appropriate

---

## 📈 Implementation Status

| System                | Status      | Priority        |
|:--------------------- |:-----------:|:--------------- |
| AI Core               | ✅ Ready     | Must Have (MVP) |
| Economic Core         | ✅ Ready     | Must Have (MVP) |
| AI Enhancements       | 📋 Designed | Post-MVP        |
| Economic Enhancements | 📋 Designed | Post-MVP        |

---

## 💡 Example Emergence Patterns

### Micro (Individual)

- Peasant John kills 7 enemies → Becomes War Hero (Tier 2)
- Merchant Sarah accumulates wealth → Rich Merchant → Political influence

### Meso (Factional)

- House Varlen vs House Marcus rivalry → Civil war
- Merchant guild monopolizes trade → Economic power → Political pressure

### Macro (Civilization)

- Too many soldiers recruited → Farms abandoned → Famine → Banditry → Collapse
- Wise king opens granaries → Crisis averted → Golden age

---

## 🛠️ Technical Details

- **Target Population**: 10,000 NPCs
- **Performance Target**: 60 FPS
- **Technology**: DOTS (Data-Oriented Technology Stack) for Tier 1 batch processing
- **Relationship Tracking**: Tier 2/3 only (200k tracked relationships vs 100M potential)

---

*Last Updated: 2025-01-XX*  
*Status: Ready for Implementation*
