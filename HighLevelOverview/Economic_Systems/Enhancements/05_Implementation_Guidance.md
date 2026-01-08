---
layout: default
title: Implementation Guidance
parent: Enhancements
grand_parent: Economic Systems
nav_order: 5
---

**Related Documents:**
- Economic Systems - Core (MVP) (foundational systems)
- AI Systems - Core (AI behavior integration)
- AI Systems - Enhancements (future AI features)
- [Future] Resource Encyclopedia (detailed resource specs)


# **PART 5: IMPLEMENTATION GUIDANCE**

## **5.1 When to Implement Each Enhancement**

**Decision Framework:**

**Implement Enhancement IF:**
1. Core systems stable (no major bugs)
2. Performance acceptable (60 FPS with 10k NPCs)
3. Economic patterns as expected (emergent balance)
4. Team has bandwidth (not blocking other work)
5. Enhancement adds significant value (playtesting feedback)

**Prioritization:**

**TIER 1 (Implement First):**
1. **Dynamic Pricing** - Enables market-responsive production
2. **Negotiation** - Adds interaction depth
3. **Resource Spoilage** - Creates urgency
4. **Market-Responsive Production** - Makes economy dynamic

**Order:** Dynamic Pricing → Negotiation → Spoilage → Market-Responsive

**TIER 2 (Implement Second):**
- Based on playtesting feedback
- Choose enhancements that address player pain points
- Skip if not adding value

**TIER 3 (Implement Last, Optional):**
- Only if core gameplay focuses on that system
- Most can be skipped without loss

---

## **5.2 Testing Requirements**

**Per Enhancement Testing:**

**Dynamic Pricing:**
- Test: Price oscillations stabilize over time
- Test: Boom-bust cycles emerge but dampen
- Test: Local price variations make sense
- Test: No infinite price spirals

**Negotiation:**
- Test: Personality differences visible in negotiation
- Test: Relationship effects function correctly
- Test: Negotiations resolve (don't loop forever)
- Test: Performance acceptable (not too slow)

**Resource Spoilage:**
- Test: Spoilage creates urgency (NPCs sell before spoiling)
- Test: Seasonal price variations emerge
- Test: Tool degradation creates steady demand
- Test: No exploit (infinite fresh food tricks)

**Market-Responsive Production:**
- Test: NPCs switch crops based on prices
- Test: Supply adjusts to demand over time
- Test: Market finds equilibrium (eventually)
- Test: No degenerate strategies (all-wheat then all-vegetable flip-flopping)

---

## **5.3 Integration Challenges**

**Common Integration Issues:**

**Dynamic Pricing + Market-Responsive Production:**
- **Issue:** Positive feedback loops (price rises → more production → oversupply → crash)
- **Solution:** Damping factors, switching costs, personality variation

**Negotiation + Relationship System:**
- **Issue:** Too many relationship updates (performance)
- **Solution:** Only significant trades affect relationships (>10 coins)

**Resource Spoilage + Storage:**
- **Issue:** NPCs lose all food to spoilage (frustrating)
- **Solution:** AI prioritizes selling perishables first

**Barter + Currency:**
- **Issue:** Which system to use when?
- **Solution:** Currency preferred, barter fallback when currency scarce

---

# **APPENDICES**

## **Appendix A: Market-Responsive Production Examples**

### **A.1: Vegetable Boom-Bust Cycle**

[Full detailed example with year-by-year progression, price changes, NPC decisions, and market equilibration]

### **A.2: Tool Market Equilibration**

[Example of craftsmen responding to tool shortage, oversupply correction, finding balance]

### **A.3: Cascading Production Shifts**

[Example of how wheat shortage affects food prices, which affects vegetable prices, creating cascade]

---

## **Appendix B: Dynamic Pricing Examples**

### **B.1: Famine Price Spike**

[Detailed example of bad harvest causing food shortage, price spike, economic crisis, recovery]

### **B.2: Regional Price Differences**

[Example of Village A vs Village B price differences creating merchant arbitrage opportunity]

### **B.3: Price Equilibration Over Time**

[Example showing how prices oscillate and eventually stabilize near equilibrium]

---

## **Appendix C: Negotiation Examples**

### **C.1: Honest vs Honest (Quick Agreement)**

[Two honest NPCs negotiate, reach fair price quickly, both satisfied]

### **C.2: Ambitious vs Rational (Calculated Haggling)**

[Ambitious seller wants profit, Rational buyer calculates fair price, negotiation process]

### **C.3: Deceitful Manipulation**

[Deceitful seller tries to overcharge, different buyer reactions based on personality]

### **C.4: High-Trust Relationship (Flexible Terms)**

[Two NPCs with high Trust negotiate, flexible payment, relationship strengthens]

---

## **Appendix D: Barter Examples**

### **D.1: Successful Barter (Mutual Benefit)**

[Farmer and Craftsman trade wheat for tool, both value what they get more than what they give]

### **D.2: Failed Barter (Unequal Value)**

[Attempted barter fails because valuations don't align, no mutual benefit]

### **D.3: Multi-Item Barter**

[Complex barter involving 3+ items, NPCs negotiate bundle deals]

### **D.4: Barter Chain**

[NPC trades through intermediaries to eventually get what they need]

---

## **Appendix E: Advanced Systems Examples**

### **E.1: Emergent Currency**

[Full example of how Kingdom A gold vs Kingdom B silver creates exchange rates, money changers]

### **E.2: Advanced Information Spread**

[Example of rumor spreading, false information, espionage, information trading]

### **E.3: Employment System**

[Example of employer hiring laborers, wage negotiation, labor strike]

---

**END OF DOCUMENT**

---

## **Document Revision History**

| Version | Date | Changes |
|---------|------|---------|  
| 1.0 | 2025-01-XX | Initial enhancements document created |

---

**Implementation Priority:** Focus on Core systems first (see Economic Systems - Core document). Only implement enhancements after Core is stable and proven.