---
layout: default
title: Visual Design Rant
parent: Visual Design
grand_parent: Documentation
nav_order: 1
---

Overall visual design thoughts and considerations

Our visual design should allow ease of scaling of objects on different zoom levels, allow destruction/cretion of environment by user, should allow for clear destinction and uniqness of characters/npcs. And obviously should be pleasant for eyes. Overall feel direction is to have more high fantasy vibrant pixel art style.

All of the solutions below use prerendered 3d graphics to 2d sprites for characters, and some for environments

Biggest question right now is what camera setup and angle to use. isometric side view looks very promising because of good possibility to showcase our characters and their details, wich aligns well with the philosophy of the project.

![a8873d45-5f11-43ab-967c-5662143a0c30.webp](./Images/a8873d45-5f11-43ab-967c-5662143a0c30.webp)

![diablo_example_1.gif](./Images/diablo_example_1.gif)

![diablo_example_2.gif](./Images/diablo_example_2.gif)

With this approach there's not resoved issue for this type of world simulation game is how to better handle zooming of the camera. One of the possible solutions that is the easiest t come up with is at some point is to just change camera angle and use absolutely different low res assets and make it like a strategic top down view.

Then to pure top down.

It is simpler to implement, it's easier to work with in terms of scale
