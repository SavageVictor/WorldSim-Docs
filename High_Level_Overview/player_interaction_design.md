---
layout: default
title: Player Interaction Design
parent: Documentation
nav_order: 2
---

# Player Interaction Design

## Overview

This document outlines the player interaction systems for the civilization simulation game, focusing on how players influence the world through NPC relationships and emergent consequences rather than direct control.

---

## Core Philosophy

### Player Role
- Players operate a "dollhouse/sandbox" - creative freedom to shape the world
- NPCs maintain autonomy - they can reject player suggestions based on personality
- Influence works through **external pressure** and **indirect manipulation**
- Drama emerges from NPCs surprising players with their autonomous decisions

### Design Principles
- **Observable consequences**: All player actions have visible, traceable effects
- **Personality-driven responses**: NPCs evaluate player actions through trait filters
- **Emergent rather than scripted**: Systems interact to create dramatic events naturally
- **Failure as content**: NPC deaths, betrayals, and policy failures generate compelling stories

---

## Player Character System

### "Your Characters" Concept

Players sponsor NPCs who, if successfully developed, grant the player special abilities:

**Example**: 
- Nurture an NPC into becoming a powerful geomancer
- That geomancer grants player the ability to terraform landscape
- The geomancer remains an autonomous NPC with their own goals and personality

### Key Characteristics

**Sponsored NPCs**:
- Player-selected NPCs who receive special attention and resources
- Can occupy political positions, develop special skills, or build dynasties
- Retain full personality and decision-making autonomy
- May reject player suggestions if they conflict with traits or current goals

**Attention Limits**:
- Arbitrary cap on number of actively sponsored NPCs (suggested: 5-10)
- Reflects realistic player bandwidth for tracking individual stories
- Forces meaningful choices about which NPCs to invest in

---

## Sleeper Stats Architecture

### Performance Optimization

All NPCs have hidden potential that activates only when player interacts with them:

```
All NPCs (10,000):
├─ Basic tier (9,000)
│  ├─ Active: 7 personality traits, basic needs, occupation
│  └─ Sleeper: Hidden potential scores (magic affinity, leadership, etc.)
│
├─ Medium tier (900) 
│  ├─ Active: Relationships, reputation, skills
│  └─ Sleeper: Detailed ambitions, political leanings, trauma responses
│
└─ Complex tier (100)
   ├─ Active: Full behavior trees, memory system, faction dynamics
   └─ Sleeper: Legacy potential, dynasty mechanics, unique abilities
```

### Awakening Mechanics

**Trigger**: First player interaction (revelation, patronage, gift)
- Sleeper stats activate → NPC gains appropriate depth
- Performance impact acceptable (only awakening NPCs player cares about)
- Creates natural player investment in awakened NPCs

---

## Player Abilities & Tools

### Material Gifts

**What players can create**:
- **Weapons**: Sword, armor, siege equipment
- **Resources**: Gold, food supplies, rare materials  
- **Tools**: Farming equipment, books, artisan tools
- **Luxuries**: Fine clothes, jewelry, art

**NPC Responses** (personality-driven):
- **Ambitious + poor** NPC gets sword → "This is my chance for glory!" → Becomes mercenary/bandit
- **Honest + traditional** NPC gets gold → Donates to temple/community
- **Cruel + deceitful** NPC gets weapons → Immediately uses for violence/robbery
- **Kind + rational** NPC gets farming tools → Shares with community, improves yields

**Cascading Effects**:
- Give weapons to peasants → Some become bandits → Trade disrupted → Food scarcity → More desperation
- Give gold to merchant → Expand business → Employ NPCs → Economic boom OR monopolize market → Inequality

### Communication Tools

**Letters** (to literate NPCs):
- Direct communication of ideas
- Spread based on personality compatibility
- Examples:
  - "The nobles don't deserve their wealth" → Revolutionary sentiment
  - "Our kingdom is divinely chosen" → Nationalist fervor
  - "Magic users are dangerous" → Persecution of mages

**Rumors** (through sponsored NPCs):
- Less direct than letters
- Spreads through social networks
- Creates uncertainty and speculation

**Goal Suggestions**:
- Integrated into GOAP (Goal-Oriented Action Planning) architecture
- NPCs evaluate suggestions through personality filters
- Competing with existing NPC goals and priorities

### Power Unlocks (from Advanced NPCs)

Powers emerge from successfully nurturing NPCs:

| NPC Achievement | Player Power Gained | Requirements |
|----------------|-------------------|--------------|
| Geomancer | Terrain manipulation | Complex tier + Earth magic mastery |
| Spymaster | Information networks | Complex tier + High Deceitful + Intelligence network |
| Champion | Direct combat influence | Complex tier + Legendary combat skill |
| Architect | Building/city planning | Complex tier + Major construction achievements |
| Merchant Prince | Economic manipulation | Complex tier + Massive wealth generation |

**Discovery Model**: **Hybrid approach**
- Players can sense general categories ("This person has martial potential")
- Specific development paths remain mysterious
- Enough information for meaningful choices, enough mystery for surprises

---

## Goal Influence System

### GOAP Integration

Player suggestions integrate into NPC's multilayer Goal-Oriented Action Planning:

```
Player Suggestion: "You should study earth magic"
├─ NPC Evaluation (GOAP layer)
│  ├─ Personality compatibility check
│  │  ├─ Traditional: -50% weight (magic is newfangled)
│  │  ├─ Rational: +30% weight (logical long-term investment)
│  │  └─ Ambitious: +60% weight (path to power)
│  ├─ Current goal conflicts
│  │  └─ "Feed family" priority 10 vs "Study magic" priority 2
│  └─ Environmental feasibility
│     ├─ Magic school accessible? (Yes/No)
│     ├─ Can afford tuition? (Resources check)
│     └─ Social acceptability? (Cultural factors)
└─ Outcome: Added to goal pool at calculated priority
```

### Revelation Mechanics

**Basic concept**: 
- Small divine nudges that NPCs evaluate through their personality
- Not mind control - suggestions that may be accepted or rejected
- More effective with NPCs who have high loyalty or compatible traits

**Alignment filtering**:
- Traditional NPC + progressive revelation → Likely ignored
- Ambitious NPC + power-seeking revelation → Likely accepted  
- Rational NPC + illogical revelation → Questioned or rejected

---

## Political Influence

### Scope

Players **influence but don't micromanage** kingdom politics:
- Can push agendas through sponsored NPCs in positions of power
- NPCs maintain autonomy in how they execute (or ignore) suggestions
- Everything can happen - player plans frequently derailed by emergent events

### Influence Paths

**Direct positions**:
- Sponsor NPCs into roles: advisors, generals, guild masters, religious leaders
- Give them suggestions through revelations/letters
- They filter through personality and circumstances
- May refuse, modify, or execute suggestions in unexpected ways

**Interpersonal webs**:
- Multiple sponsored NPCs interact and conflict
- Their relationships create emergent political dynamics
- Player must manage competing loyalties and personalities

**Environmental manipulation**:
- Create economic incentives/pressures
- Arrange marriages between sponsored NPCs
- Fund rival factions to create threats
- Provide resources that shift power balances

### Failure States

**What happens when things go wrong**:
- Sponsored NPC killed → Power vacuum, new challenges
- NPC changes priorities → Family over career, peace over war
- NPCs develop rivalries → One kills the other, network collapses
- Betrayal → NPC turns against player interests

**Design approach**: Make failures compelling story moments, not just setbacks

---

## Emergent Drama Systems

### Simple Foundations

Drama emerges from basic systems interacting, not scripted events:

```
Core Loop:
NPCs have needs → Make decisions based on personality → 
Actions create consequences → Consequences affect other NPCs → 
Emergent patterns
```

### Key Emergent Patterns

**Inequality**:
- Track resource ownership naturally
- Ambitious + Rational NPCs accumulate wealth
- Kind + Emotional NPCs share resources
- Disparity grows organically
- Poor NPCs get desperate → theft, banditry, migration

**Violence cycles**:
- Cruel NPCs + weapons + opportunity = attacks
- Victims' friends seek revenge  
- Escalation through personality-driven retaliation
- No complex "violence system" - just traits + tools

**Resource crises**:
- Food production < consumption = famine
- NPCs starve (Basic tier first)
- Survivors become desperate → more conflict
- Simple population tracking reveals the scale

**Faction conflicts**:
- Factions compete for resources
- Sponsored NPCs influence faction decisions
- Small conflicts escalate if unresolved
- Just needs: faction relationships + resource competition

### Player's Role in Drama

**What players provide**:
- Resources (weapons to warriors, gold to merchants)
- Ideas (letters spreading revolutionary thoughts)
- Catalysts (assassinating key figures, creating scarcity)
- Opportunities (sponsoring ambitious NPCs into power)

**What emerges**:
- Wars from sponsored warlord + weapons + ambition
- Inequality from sponsored merchant + gold + greed
- Stability from sponsored farmer + tools + kindness
- Unexpected betrayals, alliances, and consequences

---

## Save System

### Character & World Separation

**Separate save pools**:
- **Character pool**: Export/import interesting sponsored NPCs
- **World pool**: Save/load world states

**Benefits**:
- Mix and match NPCs across different worlds
- Preserve particularly successful/interesting characters
- Experiment with different world configurations
- Meta-level emergent possibilities

---

## MVP Scope

### Core Systems (Minimum Viable)

**Player can**:
1. Select NPCs to sponsor (5-10 active limit)
2. Give items to NPCs (unlocked based on advanced NPCs)
3. Send letters/suggest goals (NPCs evaluate through personality)
4. Use powers from advanced sponsored NPCs (terraforming, information, etc.)

**Player observes**:
- Sponsored NPCs' actions and outcomes
- Kingdom-level stats (population, wealth, conflicts)
- Emergent events arising from simulation
- Consequences cascading through NPC networks

### Starting Condition

**Player begins with**:
- One pre-saved NPC character
- Provides basic functionality/powers
- Serves as tutorial for sponsorship mechanics
- Foundation for building initial power base

### Out of Scope (Enhancement Phase)

- Multiplayer political PvP
- Complex scripted event systems  
- Detailed revolution mechanics
- Advanced dynasty/legacy systems
- Comprehensive UI for political visualization

---

## Design Tensions & Solutions

### Pokemon Problem

**Concern**: NPCs feel like collectibles rather than people

**Solutions**:
- Embrace dollhouse/sandbox framing (player has creative freedom)
- Organic discovery (no UI showing "This NPC could become X")
- Unclear requirements (can't perfectly optimize development paths)
- Meaningful relationships (powers come with ongoing NPC ties and complications)
- Autonomous rejection (NPCs can refuse patronage if suspicious/independent)

### Agency vs Control

**Tension**: Players want influence but NPCs need autonomy

**Balance**:
- Players provide opportunities and resources
- NPCs decide how to use them based on personality
- Rejection mechanics preserve NPC agency
- Emergent consequences create unpredictability
- Failure states generate compelling stories

### Performance vs Depth

**Solution**: Tiered + sleeper stats
- Most NPCs stay simple until player interacts
- Awakening selected NPCs adds depth only where needed
- Player attention limits naturally cap active complex NPCs
- Acceptable performance impact for engaged gameplay

---

## Future Considerations

### Potential Expansions

**Multi-kingdom networks**:
- Sponsor NPCs across multiple kingdoms
- Complex international political webs
- Extremely fragile, endlessly dramatic

**Dynasty mechanics**:
- Multi-generational sponsored bloodlines
- Children inherit traits + loyalty modifiers
- Long-term political machines

**Advanced communication**:
- Prophecies through sponsored religious NPCs
- Mass propaganda systems
- Cultural manipulation at scale

### Open Questions

1. Should revelation/suggestion have resource costs or cooldowns?
2. How transparent should NPC potential be to players?
3. What happens when player loses all sponsored NPCs in positions of power?
4. How do we make complex emergent politics visible and engaging in UI?

---

## Key Takeaways

**Player experience focus**:
- Creative sandbox with autonomous NPCs
- Influence through relationships and resources
- Drama from emergent consequences, not scripts
- Success = interesting stories, not perfect optimization

**Technical approach**:
- Simple systems that interact to create complexity
- Performance-friendly through tiered awakening
- GOAP integration for personality-driven goal evaluation
- Observable, traceable cause-and-effect chains

**Design philosophy**:
- NPCs as people, not puppets
- Failure as compelling content
- Emergent over scripted
- Player shapes conditions, NPCs create stories
