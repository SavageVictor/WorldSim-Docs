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
[View on GitHub](https://github.com/YOUR-USERNAME/YOUR-REPO){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## 📚 Documentation Structure

### AI Systems

The AI systems define how NPCs think, feel, and interact with each other and the world.

- [**AI Systems - Core (MVP)**](./HighLevelOverview/AI_Systems_Core)  
  Foundational AI behavior systems ready for implementation

- [**AI Systems - Enhancements (Future)**](./HighLevelOverview/AI_Systems_Enhancements)  
  Post-MVP features and polish

### Economic Systems

The economic systems create realistic trade, production, and resource flow dynamics.

- [**Economic Systems - Core (MVP)**](./HighLevelOverview/Economic_Systems_Core)  
  Observable, physical, emergent economy

- [**Economic Systems - Enhancements (Future)**](./HighLevelOverview/Economic_Systems_Enhancements)  
  Advanced economic features

### Visual Design

- [**Visual Design**](./HighLevelOverview/Visual Design/Visual Design Rant)  
  Art style and camera perspective

---

## 🎯 Quick Start

### For Developers

1. Start with [AI Systems - Core](./HighLevelOverview/AI_Systems_Core) to understand the foundational behavior systems
2. Review [Economic Systems - Core](./HighLevelOverview/Economic_Systems_Core) for economic integration
3. See enhancement documents for post-MVP features

### For Designers

1. Read the **Design Rationale** sections in core documents
2. Review **Emergence Pattern Examples** in appendices
3. Check **Success Metrics** to understand goals



### For Game Masters / Players

1. Explore **Personality Behavior Examples** to understand NPC types
2. Study **Faction Dynamics** to grasp political systems
3. Learn **Occupation Emergence** to see career paths

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
