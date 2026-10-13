---
layout: default
title: Next Steps
parent: Demo II
nav_order: 2
permalink: /demo-ii/next-steps
---

# Next Steps

Derived from [WorldSim design meeting — 13 Oct 2026](./Transcripts/2026-10-13-WorldSim-Design-Meeting.md).

Scope: what was **decided**, what to **build next**, what is **still open**, and which existing documents need to change as a result. This is a working checklist, not a specification — specs stay in [Documentation](../High_Level_Overview/index.md).

---

## 1. Decisions taken

| # | Decision | Note |
|---|----------|------|
| D1 | Economy core is a **centralised supply-and-demand system** that counts population, demand and stock, and refreshes periodically | No hidden "grey cardinal" agent secretly steering the economy |
| D2 | **Trading is decentralised.** No single market where everyone buys and sells | Rejected as "far too simplified" |
| D3 | **Sellers sell from their workplace** and derive price from input costs (blacksmith: iron + wood → product price) | |
| D4 | **Two-tier pricing**: a city market price projected from total production and demand, plus a per-seller local price | Market sets the trend/ceiling; the local seller sets the actual price |
| D5 | **Travel cost is part of price.** Distance walked to buy inputs is added to the seller's cost basis | Worked example: flour 10 + 2 travel = 12 cost → sell at 13 |
| D6 | **Markets exist on several levels** — nearest market within an NPC's reach, then city level | Only one city is simulated for now |
| D7 | **Barter is out of scope for now** | Explicitly not wanted yet |
| D8 | **Sellers buy their own inputs** (the baker buys flour) rather than having flour delivered | Simplest option; flagged as unverified |
| D9 | Start the simulation with a **limited capital pool** and observe behaviour | Rules for distributing it are *not* settled (see O2) |
| D10 | **City planning is centralised**, driven by demand, implemented as **state orders from the Town Hall** | Builders get their reason-to-build from Town Hall orders; no landlords |
| D11 | A **tax system** is required so the Town Hall has income | Prerequisite for a healthy economy |
| D12 | A **planner role** (possibly its own profession) walks the city and places flags marking buildable / building sites | Builders then construct at those sites |
| D13 | **World generation is frozen** until it is finished and chunked | Exploration comes after, not now |
| D14 | Resources are assumed **provided within the local city** for now | Depletion-driven conflict is a long-term idea, not current scope |
| D15 | **Reputation is postponed** | Considered hard to get right and not yet understood |
| D16 | **Social interactions are in progress** — purpose is satisfying social needs, with potential transition into relationships | |
| D17 | Today's housing model (up to 4 unrelated NPCs per house) stays **provisional** | Whether agents build their own houses is undecided (see O3) |

---

## 2. Workstreams

Ordered by dependency. W1–W2 are the critical path for Demo II; W3–W5 can run in parallel.

### W1 — Supply-and-demand core  `[blocking]`

- Periodic refresh loop: population → demand → stock → prices.
- Multi-level market resolution (nearest reachable → city level).
- NPC awareness of goods and prices, so trade decisions are informed.
- Owns: D1, D6.

### W2 — Two-tier pricing prototype  `[blocking]`

- City price model projected from total production and demand (trend / ceiling only).
- Local seller price model: input cost + travel cost + margin.
- Baker worked example as the acceptance scenario:
  - buy flour at 10, travel 2 → cost 12 → sell 13 with 1 silver margin, capped by city price;
  - near a cheap source: cost 8, city price 12 → sell 11–12, following the market.
- Must resolve **input sourcing** — does the baker buy, or is flour delivered (D8 / O1)?
- Owns: D2, D3, D4, D5, D8.

### W3 — City planning and construction

- City-planning algorithm research (published/known approaches, plus historical city layout evidence).
- Planner profession: flag placement + placement-legality checks.
- Town Hall order pipeline feeding builders.
- Tax system so the Town Hall has income.
- **Performance constraint:** this is expected to be expensive and **must not run often** — treat it as a low-frequency batch job, not a per-frame system.
- Owns: D10, D11, D12.

### W4 — Resource and item lifecycle

- Resource-awareness sensor review (recently adjusted).
- Item/tool return or wear loop so goods keep circulating.
- Recycling as the long-simulation answer to resource exhaustion.
- Explicitly **do not** touch world generation here (D13).
- Owns: D14.

### W5 — Society, families and goals

- Multi-layer goal tiers (daily → personal → city goal pool → agent ambitions).
- Skills that level up, driving self-improvement and **profession change**.
- Children, education/learning, and profession-change systems as a unit.
- Families, names/surnames, housing decisions, social interactions.
- Owns: D16, D17; feeds D15 (reputation) later.

---

## 3. Immediate action items

Carried over verbatim from the meeting, grouped and sequenced:

### Research

- [ ] Research how historical markets were organised — number, levels, central vs. local
- [ ] Research city-planning algorithms
- [ ] Decide starting-capital rules and run an experiment with a limited pool

### Design

- [ ] Design the supply-and-demand system with periodic updates
- [ ] Prototype two-tier pricing (city market price + local seller price, travel cost included)
- [ ] Design planner role, Town-Hall orders and taxes
- [ ] Decide on families, house building and social interactions

### Process

- [ ] Review the shared base/documents after the meeting

---

## 4. Open questions

| # | Question | Blocks |
|---|----------|--------|
| O1 | Did bakers buy flour, or was it delivered? Simplest option chosen for now, needs validation | W2 |
| O2 | Starting capital: one limited pool, per-person limit, or split equally? How do children draw from it? | W1 / capital experiment |
| O3 | Should agents build their own houses, or does the current 4-per-house model stay? | W5 |
| O4 | Which professions get a family unit? Peasant households yes; "a cowboy, say, that's not needed" | W5 |
| O5 | How is reputation modelled properly, and when does it come off the postponed list? | W5 |
| O6 | Does resource depletion eventually drive conflict/revolution, or is that permanently out of scope? | W4 |
| O7 | When is world generation "finished" enough to unfreeze and start exploration? | W4 |

---

## 5. Risks

| Risk | Source | Mitigation |
|------|--------|-----------|
| **City-planning cost** | Legality/placement checks already hurt performance in an earlier implementation; improved but still a risk | Low-frequency execution only; the meeting explicitly warned this will be expensive |
| **Resource exhaustion in long simulations** | Long runs need resources not to run out permanently | Recycling, item return/wear loops; local-city provisioning in the meantime |
| **Over-simplification** | The single-market model was rejected as too simple | Keep trading decentralised (D2/D3) despite added complexity |
| **Voice/transcript quality** | Unseparated speakers, background noise, `[unintelligible]` passages | Treat attribution as unreliable; confirm decisions with participants before they become spec |
| **Scope creep into macro-politics** | Depletion → war/revolution ideas surfaced, then were set aside | Hold at local-city scope (D14) |

---

## 6. Impact on existing documentation

Changes to fold into [Documentation](../High_Level_Overview/index.md) once implemented:

| Existing doc | Change |
|--------------|--------|
| [Market Systems](../High_Level_Overview/Economic_Systems/Core/05_Market_Systems.md) | Currently describes markets as **physical designated locations** (village/town/city square, weekly fairs). Needs reconciling with D2/D3 — decentralised workplace selling plus multi-level reachability. |
| [Currency & Value](../High_Level_Overview/Economic_Systems/Core/06_Currency_Value.md) | Add the two-tier pricing model (city trend price + local seller price) and travel cost as a price component. |
| [Occupation System](../High_Level_Overview/AI_Systems/Core/06_Occupations.md) | Its supply/demand section overlaps W1; profession change should now emerge from skills + ambition (W5) rather than being placeholder-only. |
| [Needs & Goals](../High_Level_Overview/AI_Systems/Core/07_Needs_Goals.md) | Add the multi-layer goal tiers: daily desires → personal goals → city goal pool → agent life goals and achievements. |
| [Trade & Commerce](../High_Level_Overview/Economic_Systems/Core/04_Trade_Commerce.md) | Align trade networks with workplace-based selling and travel-cost pricing. |
| [Resource Systems](../High_Level_Overview/Economic_Systems/Core/02_Resource_Systems.md) | Add the recycling / item-return loop intended for long simulations. |
| [Reputation & Gossip](../High_Level_Overview/AI_Systems/Core/10_Reputation_Gossip.md) | Mark as postponed (D15) — the design exists but is not yet trusted. |
| [Relationships](../High_Level_Overview/AI_Systems/Core/04_Relationships.md) | Link families and social-interaction needs to the in-progress social system (D16). |
| [Implementation Plan](../High_Level_Overview/Economic_Systems/Core/08_Implementation_Plan.md) | Reconcile its phase list with the workstreams above. |

---

## 7. Suggested next-meeting agenda

1. Resolve **O1** (input sourcing) — cheap to settle, unblocks W2.
2. Resolve **O2** (starting capital distribution) — unblocks the capital experiment.
3. Report on the two research items (historical markets, city-planning algorithms).
4. Decide **O3** (house building) so W5 can be scoped.
5. Agree the acceptance scenario for the two-tier pricing prototype.
6. Confirm the city-planning frequency budget before any implementation starts.

---

*Source: [WorldSim design meeting — 13 Oct 2026](./Transcripts/2026-10-13-WorldSim-Design-Meeting.md)*
