---
layout: default
title: Resource Systems
parent: Core Systems
grand_parent: Economic Systems
nav_order: 2
---

**Related Documents:**
- AI Systems - Core (main AI behavior systems)
- AI Systems - Enhancements (future AI features)
- Economic Systems - Enhancements (future economic features)
- [Future] Resource Encyclopedia (detailed resource specs, interactions, visuals)


# **PART 2: RESOURCE SYSTEMS**

## **2.1 Resource Categories**

### **PRIMARY RESOURCES (Extracted from Environment)**

**Renewable Resources:**

| Resource | Source Location | Extraction Method | Regeneration |
|----------|----------------|-------------------|--------------||
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
|----------|----------------|---------|-----------------||
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