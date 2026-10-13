---
layout: default
title: Demo II
nav_order: 3
has_children: true
permalink: /demo-ii
---

# Demo II

Design output for the second milestone: meeting transcripts, decisions taken, and the concrete next steps derived from them.

This section is **working material**, not the frozen specification. Once a topic here is settled it should be folded into [Documentation](../High_Level_Overview/index.md) (AI Systems / Economic Systems / Visual Design) and the corresponding transcript entry should be marked as superseded.

---

## Contents

| Section | What it holds |
|---------|---------------|
| [Transcripts](./Transcripts/index.md) | Lightly cleaned recordings of WorldSim design meetings, with original and translated text |
| [Next Steps](./Next_Steps.md) | Decisions, workstreams, open questions and risks extracted from the meetings |

---

## Current meeting log

| Date | Meeting | Topics |
|------|---------|--------|
| 2026-10-13 | [WorldSim design meeting — 13 Oct 2026](./Transcripts/2026-10-13-WorldSim-Design-Meeting.md) | Economy model, two-tier pricing, starting capital, agent goals, city planning, resources, families |

---

## How this section is maintained

1. Record the meeting, transcribe it offline, and lightly clean it.
2. Store the transcript under **Transcripts** with front matter (`parent: Transcripts`, `grand_parent: Demo II`, sequential `nav_order`).
3. Extract **Decisions**, **Next Steps** and **Open Questions** into [Next Steps](./Next_Steps.md).
4. When an item is implemented, promote it into the main [Documentation](../High_Level_Overview/index.md) and link back to the transcript as the rationale.
