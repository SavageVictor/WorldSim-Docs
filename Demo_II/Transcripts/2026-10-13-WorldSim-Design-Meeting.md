---
layout: default
title: Design Meeting — 13 Oct 2026
parent: Transcripts
grand_parent: Demo II
nav_order: 1
permalink: /demo-ii/transcripts/2026-10-13-worldsim-design-meeting
---

# WorldSim design meeting — 13 Oct 2026

Oct 13, 2026 · @Zadroticus

A 27:40 recording of a WorldSim design discussion covering the economy, agent goals, city planning, resources and families.

The transcript was machine-generated (Whisper small, run offline) and then lightly cleaned. Speech is mostly Ukrainian with switches into Russian and Polish, the audio has background noise, and speakers were not separated, so expect errors. Passages that could not be recovered are marked \[нерозбірливо\] / \[unintelligible\]; filler and noise fragments were dropped.

## Discussion points

The team leaned toward a centrally computed supply-and-demand system with decentralised, local trading, plus a town-hall-driven construction pipeline; most other topics were left as ideas for later.

### 1. Economy model (00:17–05:00)

- Framed as planned economy vs. free market; no hidden "grey cardinal" agent should secretly control the economy.
- Agreed the core should be a centralised supply-and-demand system: it counts people, what they want and what exists, and refreshes periodically so NPCs have knowledge of goods and prices.
- Markets should exist on several levels: the nearest market an NPC can reach, then a city-level market. Only one city is simulated for now.
- In a growing city, NPCs should not have to walk from one end to the other to trade.
- Research needed: how historical markets actually worked and how many there were (central markets plus smaller ones).
- Barter (e.g. peasants trading grain) is possible but explicitly not wanted right now.

### 2. Decentralised selling and two-tier pricing (05:00–10:10)

- Rejected a single place where everyone sells and buys as too simplified.
- Producers sell from their workplace: the blacksmith sells from his smithy and derives prices from input costs (iron, wood).
- Food is bought often and should be easy to reach; tools are bought rarely, so there can be fewer smiths. Bakeries were not in every house but there can be several.
- Two-tier pricing: a city market price projected from total production and demand, plus a local price per seller.
- Worked example: a baker walks a quarter of the city to buy flour for 10 silver, travel costs 1 silver each way, so his cost is 12. Market bread price is 8, but he sells at 13 (1 silver margin), capped by what the market tolerates. A baker near a cheap flour source might produce at 8 and sell at 11–12, following the market.
- Open question: did bakers buy flour or was it delivered to them? Simplest option for now: they buy it.

### 3. Starting capital (10:17–11:52)

- Start with a limited capital pool and observe what the simulation does with it.
- Capital possibly limited per person; new agents could draw from the pool or split it equally. Not settled.
- Noted as a possible research article topic; one participant is willing to do the research rather than write.

### 4. Children, learning and profession change (11:56–12:10)

- Raised as next systems to design: children, education/learning, and changing professions. No decisions.

### 5. Multi-layer goals (12:56–15:00)

- Current layer: local desires driving daily decisions.
- Planned next tier: goals set for people in general, chosen less often.
- Highest tier: city-level goals forming a goal pool; each agent gets access to part of it and builds its own goals and achievements (e.g. a farmer aiming at another profession).
- Agents should receive longer-term life goals.

### 6. Skills, ambition and growth (15:35–16:53)

- Agents should grow and change: skills that level up, so some work better than others.
- Goal-directed self-improvement in a chosen direction.
- Profession change should emerge from this. Until it exists, an agent's initial abilities and skills decide its profession.

### 7. City planning and construction (17:09–20:20)

- City planning should be a central system that accounts for demand, possibly via state orders.
- Idea: a planner role (possibly its own profession) walks around and places flags marking where to build; existing builders then build at construction sites.
- Needs a good city-planning algorithm (research the topic). Warning: this will be expensive and should not run often.
- Placement-legality checks already hurt performance in an earlier implementation; they were improved but remain a risk.
- Orders come centrally from the town hall, which gives builders a reason to build. No landlords for now.
- A tax system is needed so the town hall has income for a healthy economy.

### 8. Resources (21:04–24:06)

- Resource awareness: an agent sensor for resources was adjusted recently.
- Leave world generation alone until it is finished; once the world is large and chunked, add exploration.
- Long simulations need resources not to run out permanently; recycling could be added later.
- Tools and items should wear out or be returned so they keep circulating.
- Long-term idea: depletion (e.g. exhausted mines) could trigger conflict or revolution; for now resources are provided within the local city.

### 9. Housing, families and social life (24:23–26:50)

- Currently up to four agents can live in one house, but they are not related.
- Open question: should agents build their own houses?
- Families: e.g. a peasant household would be a family; other professions not necessarily. Names/surnames needed.
- Social interactions are wanted to satisfy social needs, with possible relationships later; work on this has started.
- Reputation is postponed: hard to do right and not yet well understood.

### Action items

- [ ] Research how historical markets were organised (number, levels, central vs. local)
- [ ] Design the supply-and-demand system with periodic updates
- [ ] Prototype two-tier pricing (city market price + local seller price, travel cost included)
- [ ] Decide starting-capital rules and run an experiment with a limited pool
- [ ] Research city-planning algorithms; design planner role, town-hall orders and taxes
- [ ] Decide on families, house building and social interactions
- [ ] Review the shared base/documents after the meeting (mentioned at 27:10)

## Transcript — original

**\[00:17\]** …економіка \[нерозбірливо\]. Це… плановане, центральне управління… Все те, що в нас буде \[нерозбірливо\].

**\[00:42\]** Ми хочемо вільний ринок? …що у нас планова економіка… Хочем брати ринок, які можуть бути… з регулюванням зверху.

**\[01:05\]** Ми не можемо собі дозволити \[нерозбірливо\] активного агента, а не гравця… Ми не можемо собі дозволити, щоб був якийсь чорний кардинал, сірий кардинал, котрий буде керувати економікою \[нерозбірливо\].

**\[01:45\]** Я погоджуюсь з тим, що це має бути централізована система. Тоді треба зробити систему попиту і пропозиції, де ця система буде дивитися, скільки у нас людей, скільки вони чого хочуть, дивитися, скільки всього є, і раз в якийсь час оновлювати — щоб у неписів була свідомість \[про товари\].

**\[02:19\]** *(польською)* To jest bardzo proste… Trzeba, żeby to było lokalne.

**\[02:27\]** На різних рівнях, на різних масштабах: щоб був маркет найближчий, в доступності для неписа, потім маркет на рівні міста… Для якихось \[нерозбірливо\] — маркет на рівні \[нерозбірливо\].

**\[02:50\]** …Ми робимо одне місто. Але нам все одно треба… Якщо в нас розростається місто — щоб у нас непис не йшов з одного боку міста в протилежний.

**\[03:21\]** Як це працювало? Треба перевірити, як це працювало. По-хорошому, треба було б перевірити, як це працювало в реальності, скільки там було цих маркетів. Були точно маркет-центри і були точно якісь ще. Наприклад, у нас є селяни, які вирощують зерно, — можуть прийти до них як бартер і взяти в них зерно в обмін на щось інше.

**\[04:15\]** …економічно. Але ми можемо, звичайно, зробити простіше — просто централізовано, де туди приходять, чуваки туди складають речі, а потім приходять інші і забирають.

**\[04:39\]** Всі, хто може, приходять продавати речі; можна навіть систему обміну — обмін речей на речі. Це теоретично можливо, але я б точно цього не хотів додавати зараз.

**\[05:15\]** Я не хочу, щоб було просто якесь одне місце, куди всі приходять, продають речі і купляють. Дуже вже спрощено. Ми можемо зробити, щоб вони не приходили в одне місце. Коваль, наприклад, — в тому місці, де він працює, звідти він і продає свої речі. Він знає, наприклад, ціну на залізо, ціну на дерево, і звідти він може зробити ціну на \[свій товар\].

**\[06:11\]** Плюс \[нерозбірливо\]… це буде вже більше на рівні міста… Важливо, але не кожен день потрібно.

**\[06:33\]** Теоретично все залежить від того, як ми \[нерозбірливо\]… Щоб їжу, яка їм треба, вони часто купляли, а якщо там якісь інструменти — то вони в принципі могли піти і пошукати, бо їх має бути менше.

**\[07:04\]** Так. Ну, наприклад, та сама пекарня — з того, що я пам'ятаю, в містах була не в кожного дома. — Ні, це правда. — …І їх може бути більше, ніж одна.

**\[07:23\]** Теоретично ми можемо зробити двошарову систему: в тебе є ринкова ціна, котра проєктується загальним продакшеном і загальним запитом у місті, і локальна ціна. Тому що, наприклад, пекарю треба купити пшеницю… чи борошно. Далі цікаво: чи приносили їм борошно, чи вони купляли борошно?

**\[08:05\]** Як ми хочемо це зробити… Простіше, щоб вони купляли. І тоді, мені здається, якщо зробити, щоб вони купляли: нашому пекарю треба піти з пункту A в пункт B — пройти чверть міста і купити там борошно за 10 срібняків. І прибавляємо дистанцію. Повертається, готує — і, наприклад, дистанція — це був один срібняк: туди, назад — два. Купити борошно обійшлося йому 12.

**\[09:07\]** Загальна ринкова ціна хліба, наприклад, може бути вісім, тому що десь є надлишок, але оскільки для нього купити \[борошно\] було 12, то він продає, наприклад, за 13 і маржу собі в один срібняк залишає — тому що ринок каже, що хліб не може бути зараз занадто дорогим.

**\[09:29\]** Або якщо він, наприклад, достатньо близько до великого джерела пшениці чи борошна і може купити його дешевше, ніж ринкова ціна, — він може виробити собі хліб, наприклад, за 8 срібняків, а ринкова ціна хліба 12, то він може продати за якісь 11, або за 12, і сам орієнтуватися на ринок. Ринок орієнтує загальний тренд — що це не може бути забагато.

**\[10:17\]** *(польською)* …Proponuję potem dawać z początku jakiś limitowany pul kapitału.

**\[10:35\]** Я б почав з обмеженого капіталу і подивився, що станеться в нашій економічній симуляції, після чого написав би по цьому наукову дисертацію… — Це звучить справді як гарна тема для якоїсь статті. — …Не писати, але я готовий проводити дослідження.

**\[11:17\]** \[нерозбірливо\] …був лімітований для однієї особи… Тому діти \[нерозбірливо\], а просто з'являлися в пулі. Чи, може, всім разом розділялися порівну… Ну, то потім я хочу перевірити.

**\[11:56\]** Далі — система дітей і система навчання… система зміни професій.

**\[12:56\]** Ми теоретично можемо це зробити. Багатошаровість \[цілей\]… Ми хотіли це зробити, якщо я правильно пам'ятаю, так: зараз у нас є система, що в тебе є твої локальні бажання — це в тебе активно кожен день, ти приймаєш рішення, базуючись на своїх цілях. І наступний тір мав бути ставленням таких цілей для людей в цілому — яка дозволяє тобі вибрати ціль. Вона б оновлювалась рідше. І якась ще вища, котра ставила б загальні цілі і робила пул цілей для міста. У міста є повний пул цілей, і ти як людина в місті отримуєш доступ до цих цілей, і на основі цього отримуєш свій пул цілей, з якого ти розбудовуєш свої цілі, досягнення.

**\[14:27\]** Типу ти хочеш стати \[нерозбірливо\]. Зараз ти фермер. Твоя ціль — \[нерозбірливо\]. Пул цих цілей у тебе обмежений… Ми хотіли, щоб у них могли з'являтися якісь амбіції… що агенти мають отримувати якісь цілі життя.

**\[15:35\]** Ну, вони треба в скіли давати… Я б про це взагалі — багато творчості, амбіції і ріст агентів, щоб вони змінювалися і розвивалися.

**\[16:10\]** Ми все ж можемо зробити скіли, які можуть якось прокачуватися, щоб хтось працював краще, хтось гірше… але ось таку якусь ціль, спрямовану на покращення себе в якомусь напрямку, щоб чогось досягти. — Я просто думаю, що якраз зміна професії і мала виходити з цього. — Так, ну, тоді поки немає зміни професій, в тебе є твої початкові уміння, навики, і з них ми будуємо, хто є хто.

**\[17:09\]** Планування міста. Планування міста має бути централізована система. Скоріше за все, цього разу вона має враховувати попит \[нерозбірливо\]… Чи хочемо ми це робити реалістично… поки я можу це зробити на системі держзамовлень.

**\[17:41\]** Я хочу, щоб у людини було ходіння і розставити прапорці: що тут можна будувати і що тут будується. У нас уже є білдери, вони ставлять у construction center. \[нерозбірливо\] Він ходить і ставить, де можна будувати; білдери вже приходять і будують. Ну, можна це відокремити в іншу професію. Якщо ти бачив симуляцію, то в нас так уже частково відбувається.

**\[18:25\]** Просто треба якісь алгоритми придумати гарні — city planning, алгоритми city planning… Пошукати. І увага, одразу попереджаю: це буде дорога система. — Так, вона не має часто запускатися.

**\[18:59\]** \[нерозбірливо\] …котра була написана під моїм керівництвом… І через те, що вона дуже багато чого перевіряла — перевірка, чи легальна \[позиція\]… Оскільки ми будуємо \[нерозбірливо\], нам потрібно проходити такі перевірки. Це достатньо вдаряло по перформансу. Я це покращив, але… воно може вдарити по перформансу.

**\[19:42\]** Ну, всі ці білдери, то ми зараз плануємо… Це має бути централізовано: Town Hall робить замовлення. Скоріше за все, тоді якраз білдери отримують причину, чому — тому я хочу, щоб це робив Town Hall. Тому що наразі ми робимо без різних лендлордів, ми просто робимо цей \[Town Hall\]. Тоді треба ще зробити систему податків для здорової економіки, щоб у \[міста\] з'являлися гроші.

**\[20:29\]** *(жарти про реальну економіку і політику)* Ладно, тепер повертаємось до нашої гри і виходимо з політики.

**\[21:04\]** Що ще у нас такого потрібно? …Вичерпність ресурсів і усвідомленість ресурсів. Наразі у нас є агенти… Я, здається, підкрутив цей сенсор, щоб він перевіряв \[нерозбірливо\]. Генерацію світу нормально — я б її не чіпав, нехай поки не закінчена. Потім, коли вже буде повноцінний світ, він буде великий, буде нормально чанками працювати, — тоді можна вже морочитися з експлорацією.

**\[21:56\]** …Вичерпність ресурсів. Але знову ж таки, для довгих симуляцій тобі треба, щоб… вони не закінчувались. — А, ти про майбутнє… — Ідеї: потім добавляємо ресайклінг. Теоретично ми можемо не ламати інструменти. Симуляція колись прийде до того, що в домі сортуватимуть сміття.

**\[22:43\]** Ми додамо \[нерозбірливо\]… Це як у відео про D&D-партію, що заходить у магазин і купляє Health Potion… «5 золота, 50 срібла» — бо ми задовбалися втрачати людей у цих данжах. Тому, наприклад, інструменти — це ваші повернуті \[речі\]…

**\[23:28\]** …вичерпаних ресурсів. Тобто так чи інакше ресурс \[закінчиться\]. Тому що тоді буде війна. Революція. Твій президент каже: у нас закінчились шахти… а \[опозиція каже\], що ми продовжимо копати золото. Потім приходить до влади — а він не може копати…

**\[23:59\]** *(англійською)* But within the framework of the local city, the resource has been provided.

**\[24:23\]** \[нерозбірливо\] Зараз четверо людей може жити в одному домі, але вони не related. Чи ми наразі так \[залишаємо\], чи ми хотіли б, щоб вони будували \[свої доми\]?

**\[25:00\]** Ну, так. У селянина вони мають бути фамілі. Вони можуть бути родиною… У селянина — так. А в ковбоя, наприклад, ну, це не потрібно. Друга половина — це якісь \[нерозбірливо\].

**\[25:35\]** Але імена, фамілії… там треба ще соціальні інтеракції, ми ж хочемо, щоб вони якось спілкувалися. — *(польською)* No, trzeba. — Але під це я вже почав трохи щось робити, не має бути сильної проблеми. Сенс у цих спілкуваннях — це буде якесь задоволення соціальних потреб, з потенційним переходом в \[стосунки\]. Але без якихось \[нерозбірливо\].

**\[26:23\]** Тепер, може, поки без репутації і всякого — досить складно, і не до кінця розуміємо, як це правильно зробити. …Сім'ями задаються якісь зв'язки. В принципі, соціальні \[зв'язки\] на рівні \[нерозбірливо\].

**\[27:02\]** Мені треба потроху виходити, тому, швидше за все, пара буде скоро. — Добре. — *(польською)* Ja mam bazę… a jeszcze podkładasz jakieś dokumenty? — Зібрати. Я потім ще на нього подивлюсь, думаю, ми над ним ще попрацюємо. — Зараз роботи… — Добре. Удачі, я полетів.

## Transcript — English translation

**\[00:17\]** …the economy \[unintelligible\]. This is… a planned one, central management… Everything we'll have \[unintelligible\].

**\[00:42\]** Do we want a free market? …that we have a planned economy… We'd take a market, whatever kinds there can be… with regulation from above.

**\[01:05\]** We can't afford \[unintelligible\] an active agent rather than a player… We can't afford some kind of hidden power, a grey cardinal, who'll be running the economy \[unintelligible\].

**\[01:45\]** I agree it should be a centralised system. Then we need a supply-and-demand system, where the system looks at how many people we have, how much of what they want, looks at how much of everything there is, and updates every so often — so the NPCs have awareness \[of goods\].

**\[02:19\]** *(in Polish)* That's very simple… It needs to be local.

**\[02:27\]** On different levels, different scales: so there's a nearest market within an NPC's reach, then a market at city level… For some \[unintelligible\] — a market at \[unintelligible\] level.

**\[02:50\]** …We're making one city. But we still need… If our city grows, the NPC shouldn't have to walk from one side of the city to the opposite one.

**\[03:21\]** How did it work? We need to check how it worked. Ideally we'd check how it worked in reality, how many of these markets there were. There were definitely central markets and definitely some others. For example, we have peasants who grow grain — people could come to them for barter and take grain in exchange for something else.

**\[04:15\]** …economically. But of course we can make it simpler — just centralised, where guys come and drop off their goods, and then others come and pick them up.

**\[04:39\]** Everyone who can comes to sell things; we could even have an exchange system — goods for goods. That's theoretically possible, but I definitely wouldn't want to add it now.

**\[05:15\]** I don't want there to be just one place where everyone comes, sells their stuff and buys. That's far too simplified. We can make it so they don't all come to one place. The blacksmith, for example — he sells his goods from the place where he works. He knows, say, the price of iron, the price of wood, and from that he can set the price of \[his product\].

**\[06:11\]** Plus \[unintelligible\]… that would be more at city level… Important, but not needed every day.

**\[06:33\]** In theory it all depends on how we \[unintelligible\]… Food they need, they should buy often; but tools — they could in principle go and look for them, because there should be fewer \[toolmakers\].

**\[07:04\]** Yes. Take the bakery — from what I remember, in cities not every house had one. — No, that's true. — …And there can be more than one.

**\[07:23\]** In theory we can make a two-tier system: you have a market price, projected from overall production and overall demand in the city, and a local price. Because, for example, the baker needs to buy wheat… or flour. Then it's interesting: was flour brought to them, or did they buy it?

**\[08:05\]** How we want to do it… Simpler if they buy it. And then, I think, if we make them buy it: our baker has to go from point A to point B — cross a quarter of the city and buy flour there for 10 silver. And we add distance. He comes back, bakes — and say the distance cost one silver: there and back, two. Buying flour cost him 12.

**\[09:07\]** The general market price of bread might be, say, eight, because there's a surplus somewhere, but since buying \[flour\] cost him 12, he sells for, say, 13 and keeps a one-silver margin — because the market says bread can't be too expensive right now.

**\[09:29\]** Or if he's close enough to a big source of wheat or flour and can buy it cheaper than the market price — he can make bread for, say, 8 silver, while the market price of bread is 12, so he can sell for 11, or 12, orienting himself on the market. The market sets the general trend — that it can't be too much.

**\[10:17\]** *(in Polish)* …I'd suggest giving some limited pool of capital at the start.

**\[10:35\]** I'd start with limited capital and see what happens in our economic simulation, and then write a doctoral thesis about it… — That honestly sounds like a good topic for an article. — …Not write it, but I'm ready to do the research.

**\[11:17\]** \[unintelligible\] …was limited per person… So children \[unintelligible\], they'd just appear in the pool. Or maybe it gets split equally among everyone… Well, that's what I want to test later.

**\[11:56\]** Next — a children system and a learning system… a profession-change system.

**\[12:56\]** In theory we can do it. Multiple layers \[of goals\]… If I remember right, we wanted it like this: right now we have a system where you have your local desires — that's active for you every day, you make decisions based on your goals. The next tier was supposed to set goals like these for people in general — something that lets you choose a goal. It would update less often. And then an even higher one that sets overall goals and builds a goal pool for the city. The city has a full goal pool, and you as a person in the city get access to those goals, and based on that you get your own goal pool, from which you build up your goals and achievements.

**\[14:27\]** Like, you want to become \[unintelligible\]. Right now you're a farmer. Your goal is \[unintelligible\]. Your pool of these goals is limited… We wanted them to be able to develop ambitions… that agents should get some life goals.

**\[15:35\]** Well, they need to feed into skills… I'm all for that — lots of creativity, ambition and agent growth, so they change and develop.

**\[16:10\]** We can still make skills that level up somehow, so some work better and some worse… but a goal like this, aimed at improving yourself in some direction, to achieve something. — I just think profession change was supposed to come out of exactly that. — Right, so until there's profession change, you have your starting abilities and skills, and from those we decide who's who.

**\[17:09\]** City planning. City planning should be a centralised system. Most likely this time it should take demand into account \[unintelligible\]… Whether we want to do it realistically… for now I can do it on a state-orders system.

**\[17:41\]** I want a person to walk around and place flags: what can be built here and what's being built here. We already have builders; they place things at the construction center. \[unintelligible\] He walks around and marks where building is allowed; the builders then come and build. We could split this into a separate profession. If you've seen the simulation, it already partly works like that.

**\[18:25\]** We just need to come up with some good algorithms — city planning, city-planning algorithms… Look them up. And heads-up, I'm warning you right away: this will be an expensive system. — Yes, it shouldn't run often.

**\[18:59\]** \[unintelligible\] …which was written under my supervision… And because it checked a lot of things — checking whether a \[placement\] is legal… Since we're building \[unintelligible\], we have to pass those checks. That hit performance quite a bit. I improved it, but… it can hit performance.

**\[19:42\]** Well, all these builders, we're now planning… It should be centralised: the Town Hall places the orders. Most likely that's exactly what gives builders their reason — that's why I want the Town Hall to do it. Because for now we're doing it without landlords of any kind, we're just doing this \[Town Hall\]. Then we also need a tax system for a healthy economy, so the \[city\] has money coming in.

**\[20:29\]** *(jokes about the real-world economy and politics)* OK, now back to our game and out of politics.

**\[21:04\]** What else do we need? …Resource depletion and resource awareness. Right now we have agents… I think I tweaked that sensor so it checks \[unintelligible\]. World generation is fine — I wouldn't touch it, let it stay unfinished for now. Later, once it's a full world, it'll be big and work properly in chunks — then we can bother with exploration.

**\[21:56\]** …Resource depletion. But again, for long simulations you need them to… not run out. — Ah, you mean the future… — Ideas: later we add recycling. In theory we could make tools not break. At some point the simulation will get to people sorting their trash at home.

**\[22:43\]** We'll add \[unintelligible\]… It's like that video about a D&D party walking into a shop and buying a Health Potion… "5 gold, 50 silver" — because we got fed up with losing people in those dungeons. So, for example, tools are your returned \[items\]…

**\[23:28\]** …depleted resources. So one way or another the resource \[will run out\]. Because then there'll be war. Revolution. Your president says: our mines have run out… and \[the opposition says\] we'll keep digging gold. Then he comes to power — and he can't dig…

**\[23:59\]** *(in English)* But within the framework of the local city, the resource has been provided.

**\[24:23\]** \[unintelligible\] Right now four people can live in one house, but they're not related. Do we keep it like that for now, or do we want them to build \[their own houses\]?

**\[25:00\]** Well, yes. For a peasant they should be a family. They can be a family… For a peasant, yes. But for a cowboy, say, that's not needed. The other half is some \[unintelligible\].

**\[25:35\]** But names, surnames… we also need social interactions — we want them to talk to each other somehow. — *(in Polish)* Yes, we need that. — I've already started a bit of work on that; it shouldn't be a big problem. The point of these interactions is satisfying social needs, with a potential transition into \[relationships\]. But without any \[unintelligible\].

**\[26:23\]** Maybe no reputation and such for now — it's quite complex, and we don't fully understand how to do it properly. …Families define some connections. Basically, social \[ties\] at the level of \[unintelligible\].

**\[27:02\]** I need to head out soon; most likely class starts soon. — OK. — *(in Polish)* I have the base… are you also adding some documents? — Gather it. I'll take another look at it later; I think we'll keep working on it. — Work now… — OK. Good luck, I'm off.
