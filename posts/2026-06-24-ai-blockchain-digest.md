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

The co-inventor of the Transformer just changed employers — and it matters for developers.

Noam Shazeer, co-author of the 2017 paper "Attention Is All You Need" that introduced the Transformer architecture underlying every major AI model today, has announced he is leaving Google DeepMind to join OpenAI.

This isn't routine talent news. Shazeer's previous departure from Google in 2021 led directly to Character.AI, one of the fastest-growing consumer AI products in history — acquired by Google for ~$2.7B before he moved to DeepMind. His work sits at the specific intersection of architectural efficiency and large-scale training that determines frontier model cost-per-token.

For developers: watch OpenAI's architectural announcements over the next 6–12 months more carefully than usual. When the person who helped build the foundation of modern AI changes employers, the next thing they build tends to reshape the industry.

Meanwhile, Cardano's Leios testnet just launched — targeting 1,000+ TPS from today's 10 TPS. If you've been waiting for Cardano to support high-throughput DeFi, the testnet is live now.

https://www.buildfastwithai.com/blogs/ai-news-today-june-23-2026

#AI #MachineLearning #OpenAI #Transformers #Blockchain #DeveloperTools

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

# The Transformer's Co-Inventor Just Changed Teams — Here's Why It Matters for Developers

*Noam Shazeer leaving Google DeepMind for OpenAI is more than a talent headline. It's a signal about where the next architectural frontier will be built.*

## A Name Worth Knowing

If you work in AI — whether you build models, deploy them, or simply depend on them — there are a handful of papers that shaped the world you operate in. "Attention Is All You Need," published in 2017 by Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, and Polosukhin, is the most consequential of them.

That paper introduced the Transformer architecture. Every significant language model in production today — GPT-4, Claude, Gemini, LLaMA, Mistral — is a direct architectural descendant of the design it described. The Transformer is to modern AI what the microprocessor was to personal computing: the architectural invention that made everything else possible at scale.

Noam Shazeer is one of the paper's co-authors. On June 24, 2026, he announced he is leaving Google DeepMind to join OpenAI.

## Why This Move Is Different

The AI industry generates a constant stream of executive moves and talent reshuffles. Most of them are noise. Shazeer's move is different for a specific reason: he is not a builder who happened to study architecture. He is an architect who has repeatedly demonstrated the ability to build systems that redefine what is commercially possible.

After leaving Google in 2021, Shazeer co-founded Character.AI, which became one of the fastest-growing consumer AI products in history before Google reacquired the technology for approximately $2.7 billion in 2024. The architecture decisions he made at Character.AI — particularly around inference efficiency and conversational state management — directly influenced how the entire industry approaches real-time language model deployment. After the acquisition, he joined Google DeepMind. Now he is moving again.

His expertise sits at a specific intersection: making frontier-class models architecturally efficient without sacrificing capability, at the scale that matters commercially. That is precisely the problem every major lab is trying to solve right now.

## What OpenAI Likely Gets

OpenAI is at an interesting inflection point in mid-2026. GPT-5 and its successors have demonstrated that scale still produces capability gains, but the cost curves are becoming harder to justify for mid-tier enterprise buyers. The company's recent moves — reduced API pricing, the mid-tier GPT-5.5 Mini launch, the Daybreak cybersecurity program — all point toward an organization trying to make frontier-class AI economically accessible, not just technically impressive.

Shazeer's work on architectural efficiency maps directly onto that priority. If he can find a path to frontier-class performance at meaningfully lower computational cost — the way Transformers made attention-based architectures tractable in 2017 where prior approaches had failed — it would change OpenAI's competitive position at every pricing tier simultaneously.

## What Developers Should Watch

For developers making technology choices over the next 12–18 months, this move is a directional signal worth factoring into your roadmap.

**Model architecture is not static.** The Transformer has been dominant for nearly a decade, but architectural research has continued. Shazeer's presence at OpenAI raises the probability of a non-incremental architectural shift in future models — one that could dramatically change the performance-per-dollar calculus and disrupt the assumptions built into your current integration choices.

**OpenAI's efficiency trajectory deserves closer attention.** If the next generation of OpenAI models shows significant efficiency gains — lower inference cost, higher throughput, reduced latency at equivalent capability — this hire is likely a contributing reason.

**The talent concentration matters.** OpenAI now has, by most measures, the densest concentration of foundational AI architecture talent in the industry. When the people who invented the tools gather to build the next tools, the output tends to be significant.

## The Practical Implication

You don't need to act on this today. The architectural work starting now will take 12–18 months to appear in production models. But the time to understand your switching costs — how tightly your production systems are coupled to specific model behaviors, context window assumptions, or fine-tuning investments — is before the architectural shift lands, not after.

The Transformer's co-inventor just signed on to build whatever comes next. Worth watching closely.

https://www.buildfastwithai.com/blogs/ai-news-today-june-23-2026

---

### Contra

Noam Shazeer moving from Google DeepMind to OpenAI is the kind of talent signal that creates concrete consulting opportunities for independent developers.

Here's the logic: when the co-inventor of the Transformer changes employers, enterprises with multi-year AI vendor contracts start getting nervous about whether their assumptions still hold. Cost models built around current performance-per-dollar ratios may not survive a next-generation architectural shift. Most enterprise AI teams know this is a risk but haven't done the analysis.

That's a billable problem you can solve right now.

A model migration readiness assessment — examining how tightly a company's production systems depend on specific model behaviors, context window sizes, and fine-tuning investments — is a $4,000–$8,000 engagement that almost every enterprise AI team needs and hasn't prioritized. The Shazeer news is the conversation opener. The analysis is the work.

The architectural shift hasn't happened yet. The window to help companies prepare is open now.

https://www.buildfastwithai.com/blogs/ai-news-today-june-23-2026

---

### Background Image Prompt

A dramatic horizontal cinematic composition (1500×1000px, no text overlay) depicting the symbolic transfer of a foundational architectural idea. Center: a precise geometric rendering of the Transformer architecture — multi-headed attention heads as luminous crystalline polyhedra, encoder-decoder blocks as interconnected floating monoliths, attention arrows as streams of white light — suspended in deep black space. On the left, a fading cool blue-white light source (suggesting Google's design language) gradually losing brightness. On the right, a rising warm white-green luminescence (suggesting OpenAI's aesthetic) growing stronger. The architecture diagram is caught mid-flight, trailing arcs of light from left to right like a comet. Background: a dark cosmic void with faint neural-network constellations connecting distant stars. Foreground: dissolving fragments of mathematical notation — softmax equations, attention matrices — drifting from the left light source toward the right, shifting in color as they cross. Art style: high-concept science fiction editorial illustration, precise geometry, cinematic chiaroscuro lighting. Dominant palette: deep navy, electric cyan, and off-white with a single thin gold accent line tracing the trajectory of the transfer. Mood: historical significance, momentum, architectural inevitability. No people, no faces, no text, no logos.
