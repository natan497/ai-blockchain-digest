# AI & Blockchain Digest — June 24, 2026

> Daily roundup of the most important developments in AI and blockchain for developers and tech professionals.

---

## Artificial Intelligence

### Noam Shazeer Leaves Google DeepMind for OpenAI

Noam Shazeer — co-author of the landmark 2017 paper "Attention Is All You Need" that introduced the Transformer architecture underpinning every major AI model today — has announced he is leaving Google DeepMind to join OpenAI. The move follows a pattern of high-profile talent migration toward OpenAI through 2026; Shazeer previously departed Google in 2021 to co-found Character.AI, which Google subsequently reacquired for approximately $2.7 billion in 2024 before he moved to DeepMind. His expertise centers on architectural efficiency and large-scale training — the exact problems that determine frontier model cost-per-token.

**Developer angle:** When the person who co-invented the Transformer switches employers, it is a directional signal about where next-generation architecture work will happen. Watch OpenAI's model architecture announcements over the next 6–12 months closely — efficiency gains that change the cost curve for frontier inference tend to emerge from this kind of foundational hire.

---

### OpenAI Launches Daybreak Cybersecurity Program

OpenAI announced Daybreak, a cybersecurity-focused initiative combining GPT-5.5 models with Codex security capabilities, positioned as OpenAI's answer to Anthropic's Project Glasswing. The program gives security teams AI-powered code analysis, automated vulnerability detection, and threat-modeling tooling at enterprise scale. The timing is deliberate: Glasswing's first-month report catalogued over 23,000 vulnerabilities across 1,000+ open-source projects, and OpenAI is moving to match that capability with its own security-adjacent customer base.

**Developer angle:** Two competing AI-powered vulnerability-scanning programs from the two largest frontier labs means the bar for automated security tooling is rising fast. If you're not yet integrating AI into your security pipeline, these programs represent both a real capability uplift and a benchmark that security reviewers will increasingly expect teams to meet.

---

### Colorado Consumer AI Act: Six Days Until Compliance Deadline

The Colorado Consumer Protections for Artificial Intelligence Act — the first US state-level comprehensive AI regulation — takes effect June 30, 2026. It applies to deployers and developers of high-risk AI systems in employment, healthcare, financial services, education, housing, and legal services. Covered entities must have a documented risk management program, conduct annual impact assessments, and display specific user-facing disclosure language; penalties reach $20,000 per violation.

**Developer angle:** If your AI product touches any of the six covered sectors and serves Colorado users, you have six days. The minimum viable compliance checklist: (1) a written risk management policy, (2) a defined impact assessment process, and (3) disclosure language in your user-facing interface. This obligation falls on both the AI builder and any downstream deployer using your API — check your terms of service.

---

### Sakana AI Packages Collective Intelligence as a Single API

Sakana AI announced a commercial API that wraps its collective intelligence approach — coordinating swarms of small, specialized models rather than relying on a single large frontier model — into a single endpoint targeting enterprise buyers. The product directly addresses the single-vendor reliability risk exposed when the US government's export-control directive forced Anthropic to take Fable 5 offline globally from June 12–18. Sakana's architecture routes queries across multiple smaller models and aggregates responses, providing both redundancy and domain-specialized performance.

**Developer angle:** The Fable 5 outage gave enterprises a concrete cost estimate for single-vendor model dependency. Sakana's multi-model ensemble API is one of the first commercial products explicitly designed around that risk — if your production pipelines cannot absorb another multi-day model blackout, this architecture pattern is worth evaluating now.

---

### Apple Foundation Models Going Open Source This Summer

Apple confirmed that its on-device Apple Foundation Models framework will go open source later this summer, alongside free Private Cloud Compute access for developers with fewer than two million first-time App Store downloads. The framework is also gaining image input support and a unified server-side integration layer that allows developers to call third-party models — including Claude and Gemini — through the same Swift API. The open-source release would make Apple's on-device inference infrastructure broadly available for research and developer use.

**Developer angle:** A unified Swift API that abstracts over on-device and cloud models — including third-party — means your application code stops caring whether inference is running locally or remotely. The open-source release further lowers the bar for privacy-preserving AI features in iOS and macOS apps; start evaluating the framework for use cases where user data cannot leave the device.

---

## Blockchain

### Cardano Launches Leios Testnet: 1,000+ TPS in Sight

Cardano launched the Musashi Dojo public testnet on June 23 — the opening stage of the Ouroboros Leios scaling program targeting a throughput increase from roughly 10 TPS today to over 1,000 TPS on mainnet. The Leios codebase has exceeded 705,000 lines of code, and the testnet runs through five structured stages — Earth, Water, Fire, Wind, and Void — covering protocol validation, parameter tuning, real-world performance, and adversarial stress scenarios. Input Output is targeting a mainnet hard fork as early as November 2026.

**Developer angle:** A 100x throughput increase would open Cardano to use cases — high-frequency DeFi, micropayment channels, on-chain gaming — that are effectively foreclosed at 10 TPS. If you've been watching Cardano from the sidelines, now is the right time to run a validator node on Musashi Dojo and stress-test your contracts against the new architecture well ahead of the November mainnet target.

---

### Berachain Activates Fusaka Hard Fork on Mainnet

Berachain activated the Fusaka hard fork on June 24, implementing the combined Fulu and Osaka EL/CL specification changes across its execution and consensus layers. The upgrade ends compatibility with Bera-Geth, moving the network fully onto its native stack. Fusaka also restructures proof-of-liquidity (PoL) mechanics around sWBERA with fixed WBERA emissions and ERA-style emission streams, reshaping incentive models for liquidity providers across the ecosystem.

**Developer angle:** The end of Bera-Geth compatibility requires immediate action for any team running contracts or infrastructure on Berachain — tooling built against the Geth RPC spec may silently break. Review the Fusaka migration notes today, validate all contract interactions against the new EL spec, and confirm your monitoring and alerting tooling is compatible with the updated stack before assuming backward compatibility.

---

### CBDC Ban Heads to President's Desk After 358–32 House Vote

Following the US Senate's 85–5 vote on June 22, the US House voted 358–32 to pass the 21st Century Road to Housing Act, sending a bill to the President's desk that includes a provision barring the Federal Reserve from issuing or developing a central bank digital currency through 2030. The near-unanimous bipartisan margins in both chambers signal strong congressional consensus. The ban explicitly exempts dollar-denominated stablecoins that are open, permissionless, and private; after 2030, the Fed would need explicit congressional authorization to proceed with any CBDC.

**Developer angle:** With both chambers having passed the CBDC ban by lopsided margins, the US payment infrastructure trajectory for at least four years is unambiguous: permissionless private stablecoins, not government-issued digital dollars. Developers building cross-border payment rails, DeFi settlement layers, or regulated fintech products can now design confidently around this framework without waiting for a policy reversal.

---

### Chainlink Project Pangea: 47 Banks Settle FX Trades On-Chain

Chainlink announced Project Pangea, a partnership with 47 South Korean and European banks to use stablecoins for near-real-time settlement of multimillion-dollar FX trades between the two regions — replacing a settlement process that currently takes one to two business days with on-chain finality measured in minutes. The project uses Chainlink's Cross-Chain Interoperability Protocol (CCIP) to bridge the banks' private institutional ledgers to public stablecoin infrastructure, avoiding the need to move banks onto a single shared ledger.

**Developer angle:** Project Pangea is one of the largest real-world deployments of blockchain-based FX settlement to date. For developers building on CCIP or designing cross-border payment protocols, the architectural pattern — bridging private institutional ledgers to public stablecoin rails without requiring a common ledger — is a repeatable reference design worth studying closely as this use case scales.

---

### Permissionless IV Opens in Brooklyn

Permissionless IV, DeFi's flagship developer conference, opened today in Industry City, Brooklyn, running through June 26. The agenda reflects a maturing ecosystem: keynote sessions cover real-world asset tokenization infrastructure, institutional DeFi, and cross-chain composability rather than the retail speculation themes that dominated earlier editions. The event arrives one day after the US House passed the CBDC ban and the same week as the Cardano Leios testnet launch — making it one of the more consequential Permissionless gatherings in terms of concurrent protocol milestones.

**Developer angle:** If you can't attend in person, the sessions on post-CBDC regulatory landscape, multi-chain liquidity routing, and RWA tokenization infrastructure are worth following remotely — decisions made at conferences like this routinely shape which protocol standards become industry defaults over the following year.

---

## Sources

- [AI News Today June 23 2026 — Build Fast With AI](https://www.buildfastwithai.com/blogs/ai-news-today-june-23-2026)
- [LLM AI News June 2026 — llm-stats.com](https://llm-stats.com/ai-news)
- [June 2026 AI Launch Wave — WaveSpeed Blog](https://wavespeed.ai/blog/posts/june-2026-ai-launch-wave/)
- [June 2026 AI Releases — ThursdAI](https://thursdai.news/releases/2026-06)
- [Apple Platforms State of the Union AI Updates — MacRumors](https://www.macrumors.com/2026/06/09/apple-outlines-major-ai-and-developer-tool-updates/)
- [Colorado Consumer AI Act — Latham & Watkins Regulatory Tracker](https://www.lw.com/en/us-crypto-policy-tracker/regulatory-developments)
- [Cardano Leios Testnet Launch — Edgen](https://www.edgen.tech/news/post/cardano-launches-leios-testnet-as-ada-sinks-to-5-year-low-of-0148)
- [Cardano Leios Testnet 60x Throughput — Blockonomi](https://blockonomi.com/crypto-update-cardano-launches-leios-testnet-with-60x-throughput-as-eth-holds-1656-and-pepeto-tops-10-3m/)
- [Cardano Leios Proposal Passes — CoinGape](https://coingape.com/cardano-news-leios-proposal-passes-ahead-of-june-testnet-launch/)
- [Bitcoin News Digest June 23 2026 — Substack](https://bitcoinnewsdigest.substack.com/p/bitcoin-news-digest-june-23-2026)
- [Berachain Fusaka Mainnet — CoinMarketCap](https://coinmarketcap.com/cmc-ai/berachain/latest-updates/)
- [US Crypto Policy Tracker — Latham & Watkins](https://www.lw.com/en/us-crypto-policy-tracker/regulatory-developments)
- [Crypto Today CBDC Ban — Cointelegraph](https://cointelegraph.com/news/what-happened-in-crypto-today)
- [Chainlink Project Pangea — CoinDesk](https://www.coindesk.com/latest-crypto-news)
- [Permissionless IV — Blockspot Events](https://blockspot.io/events/)

---

*Generated on 2026-06-24. Next digest: 2026-06-25.*

---

## Social Media Drafts

*Top stories: Noam Shazeer joins OpenAI + Cardano Leios testnet launch*

---

### LinkedIn

Noam Shazeer — one of the eight people who co-wrote "Attention Is All You Need" in 2017 — just left Google DeepMind for OpenAI.

Every LLM powering your product right now is built on that paper's architecture. GPT, Claude, Gemini, LLaMA — same engine, different wrapping. And one of the people who designed that engine just changed employers.

His previous departure from Google in 2021 led to Character.AI, which became one of the fastest-growing consumer AI products in history. The reason it scaled wasn't just that it was good — it was that Shazeer built it to be efficient under real production load. Google bought the tech for ~$2.7B. The architectural thinking from that work filtered across the whole industry.

Now he's at OpenAI, which is under real cost pressure to make frontier-class inference cheaper. That's exactly the kind of problem he's solved before.

I'm not predicting anything dramatic. But I've started paying closer attention to OpenAI's model releases now. When the person who co-designed the foundation changes teams, the next thing they build tends to matter.

Also today: Cardano's Leios testnet went live, targeting 1,000+ TPS from a current 10 TPS. If you build on Cardano, now's a good time to start testing.

https://www.buildfastwithai.com/blogs/ai-news-today-june-23-2026

#AI #OpenAI #Transformers #Blockchain #Developers

---

### Twitter/X

Noam Shazeer — co-author of "Attention Is All You Need," the paper that gave us the Transformer — just left Google DeepMind for OpenAI. When the person who invented the architecture moves, it's worth paying attention.

https://www.buildfastwithai.com/blogs/ai-news-today-june-23-2026

#AI #OpenAI #Transformers

---

### Bluesky

Noam Shazeer, co-inventor of the Transformer architecture, is leaving Google DeepMind for OpenAI. Every LLM you use descends from his 2017 paper. Hard to overstate how much this kind of move tends to matter.

https://www.buildfastwithai.com/blogs/ai-news-today-june-23-2026

#AI #OpenAI #ML

---

### Medium

# Attention Really Is All You Need — Including at OpenAI

*Noam Shazeer has changed employers three times since 2021. Each time, something important shifted. Today he joined OpenAI.*

There's a version of this story that writes itself. "Transformer co-inventor joins OpenAI." You read the headline, you nod, you close the tab. I almost did.

Then I thought about what it actually means that the person who co-wrote the paper underlying every model any of us use has now left Google three separate times — and chosen each time to go somewhere he thought mattered more. That's not a career. That's a thesis about where the real work is.

I've spent the last few years building on top of GPT, Claude, and Gemini. I have opinions about which one to reach for and when. What I rarely think about is that they all share the same skeletal architecture — the same multi-headed attention, the same positional encoding, the same basic design that eight people described in a 2017 paper. Different bodies, different fine-tuning, same engine under the hood.

One of those eight people just walked into OpenAI's building.

---

I don't think this is primarily a talent story. Every frontier lab has brilliant people. What's interesting about Shazeer isn't that he's smart — it's the specific shape of what he tends to build, and why.

When he left Google the first time in 2021, he built Character.AI. The interesting thing wasn't that it became popular (it grew faster than almost any consumer AI product before or since). The interesting thing was *why* it was efficient. Running conversational inference at Character's scale — millions of simultaneous short-turn sessions — meant slowness killed the product directly. There was no room for bloated architecture. The work Shazeer did there quietly influenced how the whole industry started thinking about inference efficiency. Google bought the tech for around $2.7 billion. He stayed at DeepMind for a while. Now he's at OpenAI.

OpenAI is dealing with a version of the same problem at a different order of magnitude. GPT-5 is genuinely impressive. It's also expensive. The gap between "technically capable" and "economically viable for most enterprise workloads" is exactly where the competitive battle will be fought over the next few years — not on benchmarks, but on cost per useful output. Shazeer has navigated that problem before. He almost certainly has a view on how to navigate it again.

---

Here's what I keep coming back to: architectural shifts in AI don't announce themselves. The Transformer didn't displace recurrent networks overnight. It appeared, it was good, and then over two or three years it was everywhere. Looking back, there were people at the time who understood what was happening. Most people didn't notice until it was obvious.

I'm not predicting the Transformer era is ending. It might not be, or not anytime soon. But I've learned to pay attention when someone with Shazeer's specific track record moves. His previous moves have been directional in ways that only became clear after the fact.

The practical version of this, for anyone building production systems on top of frontier models, is less dramatic than it sounds: don't treat your current model integration as a permanent dependency. Build the abstraction layer now. Maintain the optionality. The cost and performance ratios that make your architecture work today may look quite different in eighteen months — and the reason might trace back to a Wednesday job announcement in June 2026.

https://www.buildfastwithai.com/blogs/ai-news-today-june-23-2026

---

### Contra

Noam Shazeer — Transformer co-inventor — just joined OpenAI. Most people will read that headline and move on. Independent developers paying attention have a window here.

Enterprise teams with multi-year AI contracts are already nervous. They've built cost models around current performance-per-dollar assumptions. A major architectural shift from OpenAI — which is exactly what Shazeer was hired to help build — could invalidate those assumptions faster than their roadmap accounts for.

That nervousness is a concrete, billable problem. A model migration readiness assessment — mapping how tightly a company's production pipelines depend on specific model behaviors, context windows, and fine-tuning — is an engagement in the $4k–$8k range that almost every enterprise AI team needs but hasn't prioritized yet. The news gives you the conversation opener. The analysis is the actual work.

The shift hasn't landed yet. The window to help companies prepare is now, before it does.

https://www.buildfastwithai.com/blogs/ai-news-today-june-23-2026

---

### Background Image Prompt

A dramatic horizontal cinematic composition (1500×1000px, no text overlay) depicting the symbolic transfer of a foundational architectural idea. Center: a precise geometric rendering of the Transformer architecture — multi-headed attention heads as luminous crystalline polyhedra, encoder-decoder blocks as interconnected floating monoliths, attention arrows as streams of white light — suspended in deep black space. On the left, a fading cool blue-white light source (suggesting Google's design language) gradually losing brightness. On the right, a rising warm white-green luminescence (suggesting OpenAI's aesthetic) growing stronger. The architecture diagram is caught mid-flight, trailing arcs of light from left to right like a comet. Background: a dark cosmic void with faint neural-network constellations connecting distant stars. Foreground: dissolving fragments of mathematical notation — softmax equations, attention matrices — drifting from the left light source toward the right, shifting in color as they cross. Art style: high-concept science fiction editorial illustration, precise geometry, cinematic chiaroscuro lighting. Dominant palette: deep navy, electric cyan, and off-white with a single thin gold accent line tracing the trajectory of the transfer. Mood: historical significance, momentum, architectural inevitability. No people, no faces, no text, no logos.
