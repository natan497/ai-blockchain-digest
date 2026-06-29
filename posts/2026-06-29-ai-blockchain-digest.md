# AI & Blockchain Digest — June 29, 2026

> Daily roundup of the most important developments in AI and blockchain for developers and tech professionals.

---

## Artificial Intelligence

### Prompt Injection Is Now Targeting Your Entire AI Stack, Not Just Your Chatbot

A VentureBeat investigation published June 28 documents how prompt injection has evolved from toy exploits into systematic multi-vector attacks targeting the complete enterprise AI pipeline: multi-agent systems, RAG retrieval pipelines, and model routers simultaneously. Attackers embed malicious instructions inside documents, database records, or web pages that agents retrieve, causing the agent to exfiltrate data or redirect tool calls — all within a workflow that looks completely normal from the outside. For developers shipping agentic applications to production, every retrieval source is now an attack surface, and input sanitization at each retrieval boundary is no longer an optional hardening step.

### Coinbase Halves Its AI Spend by Switching to Chinese Open-Weight Models

Coinbase CEO Brian Armstrong posted on X Saturday that Coinbase has cut its AI infrastructure bill by nearly 50% without reducing token usage — by rerouting engineers through an internal LLM gateway that defaults to Zhipu AI's GLM 5.2 and Moonshot AI's Kimi K2.7 Code rather than Anthropic or OpenAI. Armstrong outlined five specific cost levers: cheaper default model selection, a 12x cache hit rate improvement, request batching, explicit context management, and routing governance. This is the highest-profile corporate endorsement of Chinese open-weight models as production defaults to date, and it arrives as Lindy CEO Flo Crivello simultaneously moved 100% of his company's traffic off Anthropic's Claude to DeepSeek, citing millions in annual savings — a convergence that puts direct pricing pressure on Western frontier labs.

### CEO-Bench: AI Agents Can't Run a Business, and a Rule-Based Heuristic Beats Them

Princeton researchers released CEO-Bench, a benchmark where AI agents manage a fictional subscription-software company (NovaMind) for 500 simulated days, beginning with zero customers and $1M in cash and graded on final cash position. Most frontier models go bankrupt, and a simple rule-based heuristic with no AI beats nearly all of them; only Claude Opus 4.8 and GPT-5.5 finish above the $1M starting balance, and neither consistently turns a profit. For developers building long-horizon autonomous agents, CEO-Bench exposes a specific and underappreciated gap: current LLMs handle individual tasks well but fail at sustained strategic decision-making under compounding uncertainty — exactly the condition real agentic workflows operate in.

### Alibaba's HappyHorse 1.1 Climbs to #2 in Global AI Video Rankings

Alibaba Cloud's HappyHorse 1.1 has reached No. 2 on every major AI video generation benchmark, as OpenAI discontinued Sora after it proved financially unsustainable and ByteDance shelved the international rollout of Seedance 2.0 following Hollywood copyright complaints. The model ships with full API access on Alibaba Cloud Model Studio, enterprise SLAs, regional compliance certifications across Europe (with new French and German data centers), and a 40% launch discount. For developers building video generation into production apps, HappyHorse 1.1 is currently the only competitive enterprise-grade video API with global availability, aggressive pricing, and an active commercial roadmap — worth running benchmark evals against.

---

## Blockchain

### Binance Exits the EU Tonight as MiCA Takes Full Effect at Midnight

Binance withdrew its MiCA license application in Greece on June 24 — reportedly because the Greek regulator was preparing to reject it over co-founder Changpeng Zhao's failure to clear the "fit and proper" ownership test — leaving millions of EU users in France, Italy, Poland, and Spain facing a July 1 service cutoff. From midnight tonight, Binance halts new spot orders, deposits, sign-ups, and all Earn/staking products for EU residents; every existing VASP license across the bloc simultaneously expires, and only exchanges holding full MiCA CASP authorization can legally onboard new EU users. Coinbase, Kraken, and Bitstamp have all positioned to capture Binance's displaced customer base — this is the largest exchange-to-exchange customer migration event European crypto has seen since MiFID II reshaped traditional finance.

### SBI Holdings Acquires Bitbank for $289M and Launches Japan's First Bank-Backed Yen Stablecoin the Same Day

Japan's SBI Holdings signed a full acquisition agreement for crypto exchange Bitbank at 46.7 billion yen (~$289M), combining it with its existing SBI VC Trade unit to create Japan's largest regulated crypto operator — 2.92 million accounts and $6.8 billion in assets under custody, ahead of bitFlyer and Coincheck by trading volume. On the same day, SBI launched JPYSC, Japan's first trust bank-backed yen stablecoin, signaling a move toward a vertically integrated exchange-to-stablecoin stack under a single regulated entity. With Japan potentially reclassifying digital assets under the Financial Instruments and Exchange Act as early as FY2027, the acquisition positions SBI to operate under stricter compliance frameworks that favor large, well-capitalized incumbents over independent platforms.

### Securitize Targets $400M Raise and Public Debut as RWA Tokenization Market Hits $31.38B

BlackRock-backed tokenization platform Securitize expects to raise $400 million ahead of a public market debut, while the broader real-world asset tokenization market reached $31.38 billion in distributed AUM as of June 28, according to RWA.xyz. Securitize has already tokenized BlackRock's BUIDL fund on Ethereum and multiple institutional products, and a public listing would mark the most significant IPO yet from the tokenization sector — giving institutional investors a public vehicle for exposure to what has become the dominant growth story in on-chain finance. For developers building on RWA infrastructure, a Securitize liquidity event is likely to accelerate enterprise API adoption and set compliance-grade architecture patterns that the rest of the sector will reference.

### Ethereum Foundation Cuts 54 Jobs and 40% of Budget, Restructures Into Five Clusters

The Ethereum Foundation announced on June 23 that it eliminated 54 positions (roughly 20% of its ~270-person workforce) and cut its operating budget by 40%, reorganizing the remaining organization around five domain-focused clusters: protocol, access, user, community, and institutional. The restructuring follows nine senior departures since January 2026 — including former co-executive directors Tomasz Stańczak and Hsiao-Wei Wang — and arrived one day after former EF researchers launched Ethlabs, an independent protocol lab now operating outside the foundation's direct payroll. For developers building on Ethereum, the practical question is whether Ethlabs and the five-cluster structure actually accelerate protocol iteration, or whether the dispersal of research capacity creates coordination friction at exactly the moment Ethereum faces real competition from rival L1s.

---

## Sources

- [VentureBeat: Prompt injection exploiting enterprise AI's biggest design flaws — June 28, 2026](https://venturebeat.com/security/prompt-injection-is-exploiting-enterprise-ais-biggest-design-flaws-by-targeting-agents-rag-pipelines-and-model-routers)
- [The Decoder: Coinbase joins the rush to Chinese AI models — June 28, 2026](https://the-decoder.com/coinbase-joins-the-rush-to-chinese-ai-models-as-western-labs-face-a-pricing-stress-test/)
- [TechTimes: Coinbase cuts AI spend 50% on Chinese models — June 28, 2026](https://www.techtimes.com/articles/319248/20260628/coinbase-cuts-ai-spend-50-chinese-models-legal-risk-its-ceo-didnt-lead.htm)
- [arXiv: CEO-Bench: Can Agents Play the Long Game? — June 2026](https://arxiv.org/abs/2606.18543)
- [VentureBeat: Alibaba's AI video model rises to No. 2 in global rankings](https://venturebeat.com/technology/alibabas-ai-video-model-rises-to-no-2-in-global-rankings-as-openais-sora-and-bytedances-seedance-fall-away)
- [CoinDesk: Binance tells EU users it will no longer provide services — June 26, 2026](https://www.coindesk.com/policy/2026/06/26/binance-tells-eu-users-it-will-no-longer-provide-services-after-failing-to-secure-mica-license)
- [CoinDesk: New MiCA regime in Europe — Crypto Week Ahead, June 29, 2026](https://www.coindesk.com/markets/2026/06/29/new-mica-regime-in-europe-u-s-jobs-report-for-june-crypto-week-ahead)
- [CoinDesk: Why SBI paid $289M for an unprofitable crypto exchange — June 28, 2026](https://www.coindesk.com/business/2026/06/28/sbi-s-usd289-million-bitbank-deal-is-symptomatic-of-japan-s-crypto-consolidation-architect-partners)
- [CoinDesk: Securitize expects to raise $400M as tokenization firm nears public debut — June 26, 2026](https://www.coindesk.com/business/2026/06/26/securitize-expects-to-raise-usd400-million-as-tokenization-firm-nears-public-debut)
- [CoinDesk: Ethereum Foundation cuts 20% of staff amid leadership exodus — June 23, 2026](https://www.coindesk.com/tech/2026/06/23/ethereum-foundation-cuts-20-of-staff-amid-leadership-exodus)

---

*Generated on 2026-06-29. Next digest: 2026-06-30.*

---

## Social Media Drafts

### LinkedIn

Coinbase just cut its AI infrastructure bill in half. Not by reducing access, not by restricting engineers — by switching the default models.

CEO Brian Armstrong posted on Saturday that Coinbase now routes through an internal LLM gateway defaulting to Zhipu AI's GLM 5.2 and Moonshot AI's Kimi K2.7 Code. Token usage is growing. The bill shrank by nearly 50%. He outlined five levers: cheaper defaults, aggressive caching (they hit a 12x cache hit rate), batching, context management, and routing governance.

I think this matters more than the Lindy story from a few days ago — and that story was already significant. Lindy is a 25-person startup. Coinbase has thousands of engineers, is a publicly traded company, and its CEO chose to make this public on a weekend. That's not a cost-cutting move you hide.

The framing I keep coming back to: this isn't about Chinese models being better than Claude or GPT-5.6. It's about the moment when the delta between frontier and good-enough got small enough that "good enough" won on economics. And once a company of Coinbase's visibility says that publicly, the negotiating leverage in the room shifts.

The technical piece that's actually interesting: the internal LLM gateway + routing layer. That's the infrastructure investment that made this possible. That's what other engineering orgs should be looking at.

https://the-decoder.com/coinbase-joins-the-rush-to-chinese-ai-models-as-western-labs-face-a-pricing-stress-test/

#AI #LLM #AICosts #EnterpriseAI #Developers

### Twitter/X

Coinbase halved its AI bill by switching to Chinese open-weight models (GLM 5.2, Kimi K2.7 Code) as the default — no usage cuts, token usage still growing. CEO posted the 5-step playbook publicly on Saturday.

https://the-decoder.com/coinbase-joins-the-rush-to-chinese-ai-models-as-western-labs-face-a-pricing-stress-test/

#AI #LLM #OpenWeightModels

### Bluesky

Coinbase halved its AI infrastructure bill by switching to Chinese open-weight defaults (GLM 5.2, Kimi K2.7 Code). CEO posted the full playbook on X Saturday. Token usage still growing.

https://the-decoder.com/coinbase-joins-the-rush-to-chinese-ai-models-as-western-labs-face-a-pricing-stress-test/

#AI #LLM #EnterpriseAI

### Medium

# Coinbase Just Told the AI Industry Something It Didn't Want to Hear

*When a major public company's CEO benchmarks Chinese open-weight models against Anthropic on a Saturday morning, the pricing game changes*

I saw the post on Saturday. Brian Armstrong, CEO of Coinbase, on X, describing in some detail how his company had cut its AI infrastructure bill nearly in half. Not by telling engineers to use AI less. Not by adding friction. By switching the default models.

GLM 5.2. Kimi K2.7 Code. Two Chinese open-weight models I hadn't spent much time benchmarking against anything in production until reading that post.

I'm a developer. I've built on Anthropic's API. I've watched the pricing move over the past 18 months in ways that are — I'll be honest — not consistently predictable. And I've had the same general assumption most people have: frontier models from the big Western labs are meaningfully better than alternatives, so you pay for them, you absorb the cost, and you build around it.

Coinbase's announcement doesn't break that assumption exactly. But it complicates it.

---

The thing that struck me first wasn't the models they switched to. It was the routing infrastructure. Armstrong described an internal LLM gateway that their engineers route all requests through. The gateway decides, based on task type and cost, which model to use. That's the real investment — not the model selection, but the abstraction layer that makes the model selection flexible.

I've seen teams build this. It's not trivial. But it's also not exotic. The fact that Coinbase built it and used it to halve their AI spend while growing token usage — that's a concrete proof point that's hard to argue with.

What Lindy did a few days earlier (moved 100% off Claude to DeepSeek to save millions) got attention because it was visceral. 25-person startup, existential cost pressure, founder talking publicly. I get why it traveled. But Coinbase is different. Publicly traded. Thousands of engineers. CEO posting about five specific cost-control levers on a weekend, which is not how you casually mention a footnote.

That's a company saying: we tested this, we thought about it, we're comfortable standing behind it publicly.

---

I might be wrong about what this signals. There's a version where Coinbase's engineering team has unusually good taste in open-weight model evaluation, and most teams trying to replicate this find the quality gap bites them in unexpected places. That's possible. GLM 5.2 is strong on coding tasks; it's less clear how it performs on the long-tail of things enterprise engineering teams actually ask models to do.

There's also a version where this is, at least partly, a negotiating move. Anthropic's pricing is the number Armstrong is clearly unhappy with. A public statement from your biggest corporate customers that they're switching to your competitors' models is not a coincidence.

But I don't think it's only that. The cache hit rate improvement — 12x — is real operational work. You don't get there without having instrumented your actual request patterns. That's an engineering investment, not a press release.

---

The five levers Armstrong listed are worth thinking about as a checklist: cheaper default model, caching strategy, request batching, explicit context management, routing governance. Four of those five have nothing to do with which lab makes the model. They're infrastructure patterns.

And that's actually what I keep coming back to. The model you're using is the most legible part of your AI cost structure. It's the number that shows up in the bill with a clear label. But for most teams running at any meaningful scale, the bigger levers are in the infrastructure surrounding the model — how requests get routed, how aggressively you cache, how much context you're actually including per call.

Coinbase built the infrastructure first. Then the model switch was almost incidental.

I don't know if GLM 5.2 is right for what I'm building. But I'm going to run the evals this week. And I'm going to look more carefully at the gateway layer we're using, because that's apparently where the real conversation is happening.

https://the-decoder.com/coinbase-joins-the-rush-to-chinese-ai-models-as-western-labs-face-a-pricing-stress-test/

### Contra

Coinbase halving its AI bill in public is a useful signal: the opportunity right now isn't switching models, it's building the infrastructure layer that makes model-switching possible. Three concrete angles for independent developers: (1) LLM gateway architecture consulting — most teams don't have one and have no idea what their actual model routing looks like; (2) caching strategy audits — Coinbase got a 12x cache hit rate improvement, which is an embarrassingly large gain for a company with real engineering talent; (3) open-weight model evaluation services — enterprise teams are suddenly very interested in running systematic evals against GLM 5.2 and Kimi K2.7 Code but don't have the tooling or the time. The window is now, before this becomes commoditized knowledge.

https://the-decoder.com/coinbase-joins-the-rush-to-chinese-ai-models-as-western-labs-face-a-pricing-stress-test/

### Background Image Prompt

A dramatic, editorial-style digital artwork for a Medium blog header (1500×1000px, no text overlay). The scene: a split composition — on the left, a sleek American corporate headquarters tower at night (representing Coinbase/US AI labs), illuminated in cold blue-white, with dollar signs subtly visible in the windows; on the right, a stream of glowing data packets flows away from the tower toward a different server infrastructure on the right side, represented by abstract server racks glowing in warm amber and red, with Chinese architectural motifs subtly woven into the rack design. Between the two, a translucent LLM gateway node pulses at center — a routing junction where the data stream splits and redirects. Dominant colors: deep navy and cold white on the left, warm amber and deep red on the right, with bright cyan for the data stream. Mood: analytical, slightly unsettling, economically significant. Art style: hyperrealistic digital illustration with cinematic lighting and a slight corporate-thriller aesthetic.
