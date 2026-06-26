# AI & Blockchain Digest — June 25, 2026

> Daily roundup of the most important developments in AI and blockchain for developers and tech professionals.

---

## Artificial Intelligence

### OpenAI and Broadcom Unveil Jalapeño — OpenAI's First Custom AI Inference Chip

OpenAI and Broadcom announced Jalapeño, a custom-built LLM inference chip that went from blank-sheet design to manufacturing tape-out in just nine months — a development pace described as potentially the fastest ASIC cycle ever achieved in high-performance computing. Engineering samples are already running GPT-5.3-Codex-Spark workloads in the lab at production target frequency and power, with initial deployment planned by end of 2026 targeting gigawatt-scale data centers alongside Microsoft and other partners. OpenAI used its own AI models to accelerate the design process itself, which is either a proof-of-concept for AI-assisted hardware engineering or the start of a recursive loop depending on how seriously you take the company's internal timelines.

**Developer angle:** OpenAI has been renting Nvidia's GPUs to run inference on your behalf; Jalapeño is their first step toward owning that layer. If it delivers on its claimed performance-per-watt advantage over current SOTA, inference costs will eventually compress — watch API pricing tiers over the next 12 months as Jalapeño ramps into production.

---

### Anthropic Accuses Alibaba of "Largest Known Distillation Attack" on Claude

Anthropic has formally accused Alibaba-affiliated entities of running the largest known distillation attack on its Claude models, involving 28.8 million interactions through nearly 25,000 fraudulent accounts between April 22 and June 5, 2026. The campaign used adversarial distillation — systematically prompting Claude to harvest its reasoning patterns at scale — and exceeded a February incident involving DeepSeek, MiniMax, and Moonshot AI that generated over 16 million exchanges via approximately 24,000 fake accounts. Anthropic has detailed the breach to White House officials and U.S. senators via a letter obtained by CNBC, calling for tighter regulatory safeguards around AI model access.

**Developer angle:** This attack exploited the API directly rather than model weights — the fraudulent accounts looked like legitimate enterprise traffic in aggregate. For developers building on commercial LLM APIs, the secondary effect matters most: Anthropic will tighten access controls, which means more verification overhead, stricter rate limits, and potentially longer API approval queues for everyone.

---

### White House Signs AI Innovation and Security Executive Order

President Trump signed an executive order titled "Promoting Advanced Artificial Intelligence Innovation and Security," formalizing the federal government's approach to AI development after a cancelled May ceremony over concerns the text could undermine U.S. competitive advantage over China. The order directs federal agencies to invest in cybersecurity defenses using AI, establishes voluntary model-testing frameworks for advanced AI systems before public release, and promotes public-private partnerships for frontier model development. The signing follows a period of significant AI security activity: Anthropic's Claude Mythos Preview had demonstrated the ability to autonomously identify thousands of severe vulnerabilities, which contributed to the urgency around a federal framework.

**Developer angle:** The voluntary testing framework is the provision to watch — it sets expectations for how frontier labs pre-screen models before deployment, which eventually shapes compliance expectations in regulated sectors. If your AI product touches federal agencies or any sector with federal oversight, the compliance playbook is starting to take shape.

---

### Qualcomm Acquires Modular for ~$3.9B, Eyes Tenstorrent at Up to $10B

Qualcomm confirmed its acquisition of Modular, an AI platform company building ML compiler infrastructure, for approximately $3.9 billion, while Bloomberg separately reports Qualcomm is in early-stage talks to acquire AI chip startup Tenstorrent at a valuation of $8–$10 billion. Tenstorrent, led by legendary chip architect Jim Keller (formerly Apple, Tesla), builds RISC-V-based AI accelerators targeting Nvidia's dominance in inference — the acquisition would give Qualcomm both the software stack via Modular and the custom silicon to compete at the data center level. Qualcomm revealed its data center ambitions at its June 24 Investor Day, framing the combined strategy as a $14 billion bet on cracking Nvidia's AI compute monopoly with an open-architecture alternative.

**Developer angle:** Qualcomm's push into AI inference silicon is one of the most credible competitive threats to the Nvidia/CUDA ecosystem in years. RISC-V-based AI chips combined with Modular's open ML compiler stack could create a viable alternative inference path — particularly appealing for teams who want to avoid long-term lock-in to a single vendor's proprietary toolchain.

---

## Blockchain

### Catholic Leaders Oppose CLARITY Act's DeFi Developer Exemption, Threatening Senate Passage

Nearly 100 Catholic bishops and church leaders sent letters to Senate Majority Leader John Thune and Minority Leader Chuck Schumer opposing Section 604 of the Digital Asset Market Clarity (CLARITY) Act, arguing the provision creates exploitable loopholes for human trafficking, organized crime, and sanctions evasion. Section 604 would exempt non-custodial blockchain software developers — meaning people who build self-custody wallets, DeFi protocols, and open-source infrastructure — from AML compliance and money-transmitter regulations that apply to financial intermediaries. The industry counters that Section 604 simply ensures software developers aren't held liable as banks for what users do with their tools; the Digital Chamber called the Catholic coalition's framing a mischaracterization of what "non-custodial" means in practice.

**Developer angle:** If Section 604 survives intact, it's a meaningful legal clarification for builders of open-source DeFi tools — you're not a money transmitter for writing software. If it's stripped from the bill, non-custodial infrastructure developers face significant compliance ambiguity. The CLARITY Act is four steps from passage before August recess; this fight determines which legal landscape you're building into.

---

### Cambrian Raises $6M Seed to Build Verifiable Blockchain Oracle Network for AI Agents

Cambrian, an a16z CSX-backed startup, raised a $6 million seed round co-led by Franklin Templeton and Polychain Capital to expand its blockchain data API into a cryptographically verifiable oracle network. The company currently provides real-time and historical on-chain data feeds, and the new funding drives expansion into verifiable data attestations — output that can be provably checked on-chain rather than trusted on reputation alone. The product is designed specifically for institutions and AI agents that need reliable, auditable blockchain data to make capital allocation decisions autonomously.

**Developer angle:** Trustworthy data feeds are the bottleneck for serious AI agent deployments in DeFi — most oracle solutions were designed for humans double-checking numbers, not for agents acting on them programmatically. Cambrian's verifiable oracle approach fills a real gap if you're building autonomous agents that interact with smart contracts without human-in-the-loop confirmation.

---

### Ethereum Leads All Major Blockchains in User Retention at 26.2% in Q1 2026

A study published this week found Ethereum posted a 26.2% wallet retention rate for users active in Q1 2025 who remained active through Q1 2026, leading all major blockchains on a percentage basis — translating to approximately 682,000 retained wallets out of 2.6 million qualifying. BNB Chain (1.49M retained wallets) and Solana (1.39M) retain more users in absolute numbers, while Ethereum leads in developer activity with 31,869 active developers — nearly double Solana's 17,708 — and over 50% of Ethereum developers now work primarily on Layer 2 networks. The Ethereum developer ecosystem has also crossed 1 million contributors total, marking a significant milestone for the ecosystem's depth.

**Developer angle:** Ethereum's retention advantage matters for applications where user lifetime value compounds over time — sticky users mean better cohort economics. The L2 developer majority confirms where the real Ethereum activity is happening: if you're still debating whether to ship on mainnet versus Base or Arbitrum, the answer has clearly shifted toward L2 for most use cases.

---

### EU MiCA Enforcement Cliff: Existing Crypto Licenses Expire July 1

Starting July 1, 2026 — five days from now — all VASP licenses issued under pre-MiCA EU regulatory frameworks expire and become invalid, requiring any firm providing crypto asset services in the EU to hold a full MiCA CASP (Crypto Asset Service Provider) authorization. The transition marks the final milestone of MiCA's full implementation, creating the world's most comprehensive operational crypto regulatory framework, but stringent requirements have already led to significant market disruption as underprepared firms face the compliance cliff. The July 1 deadline is hard — there is no grace period extension for entities that failed to complete CASP authorization in time.

**Developer angle:** Any application that touches custody, staking, exchange functions, or crypto asset management for EU users needs to be running on MiCA CASP-licensed infrastructure partners by July 1 or it operates in regulatory breach. If you haven't checked whether your infrastructure layer (wallet provider, exchange integrations, staking contracts) is CASP-authorized, do it this weekend.

---

## Sources

- [OpenAI unveils its first custom chip, built by Broadcom — TechCrunch](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/)
- [OpenAI and Broadcom reveal Jalapeño, first AI chip in partnership — CNBC](https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html)
- [OpenAI unveils first custom AI inference chip Jalapeño with Broadcom — VentureBeat](https://venturebeat.com/infrastructure/openai-unveils-first-custom-ai-inference-chip-jalapeno-with-broadcom-and-its-development-was-sped-up-with-openais-own-models)
- [OpenAI and Broadcom Unveil LLM-Optimized Intelligence Processor — Broadcom Inc.](https://investors.broadcom.com/news-releases/news-release-details/openai-and-broadcom-unveil-llm-optimized-intelligence-processor)
- [Anthropic accuses Alibaba of campaign to 'brazenly' and 'illicitly' extract AI capabilities — CNBC](https://www.cnbc.com/2026/06/24/anthropic-alibaba-distillation-campaign.html)
- [Anthropic accuses Alibaba of 'largest known distillation attack' on Claude — Nikkei Asia](https://asia.nikkei.com/business/technology/artificial-intelligence/anthropic-accuses-alibaba-of-largest-known-distillation-attack-on-claude)
- [Alibaba ran largest known AI theft campaign against Claude, Anthropic tells Senate — TechTimes](https://www.techtimes.com/articles/319105/20260625/alibaba-ran-largest-known-ai-theft-campaign-against-claude-anthropic-tells-senate.htm)
- [Promoting Advanced Artificial Intelligence Innovation and Security — The White House](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/)
- [Qualcomm inks deal for AI startup Modular to bolster software stack — CNBC](https://www.cnbc.com/2026/06/24/qualcomm-ai-chip-modular-software.html)
- [Qualcomm in Talks to Acquire AI Chip Startup Tenstorrent for Up to $10 Billion — Reuters/Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/qualcomm-talks-acquire-ai-chip-230401789.html)
- [Crypto's Clarity Act Has a New Enemy: Catholic Leaders — Decrypt](https://decrypt.co/371923/crypto-clarity-act-new-enemy-catholic-leaders)
- [Nearly 100 Catholic leaders oppose Clarity Act over weakened safeguards — The Block](https://www.theblock.co/amp/post/405868/clarity-act-new-opposition-catholic-leaders-weakened-safeguards-against-illicit-finance)
- [a16z CSX-backed Cambrian raises $6M seed to build blockchain data oracle network — The Block](https://www.theblock.co/post/406028/a16z-csx-backed-cambrian-seed-round-blockchain-data-oracle-network)
- [Ethereum leads blockchain user retention at 26% in Q1 2026 — CryptoBriefing](https://cryptobriefing.com/ethereum-leads-blockchain-user-retention-q1-2026/)
- [2026 Digital Assets Regulatory Update — Cleary Gottlieb](https://www.clearygottlieb.com/news-and-insights/publication-listing/2026-digital-assets-regulatory-update-a-landmark-2025-but-more-developments-on-the-horizon)

---

*Generated on 2026-06-25. Next digest: 2026-06-26.*

---

## Social Media Drafts

*Top stories: OpenAI/Broadcom Jalapeño chip + Anthropic accuses Alibaba of largest known distillation attack on Claude*

---

### LinkedIn

Nine months. That's how long it took OpenAI and Broadcom to go from a blank sheet to a working inference chip.

I've shipped enough software projects to know that nine months to tape-out on a custom ASIC isn't just fast — it's unusually fast. And they used their own models to accelerate the design process, which is either a compelling proof-of-concept for AI-assisted hardware engineering or the beginning of something weirder, depending on how literally you take the roadmap slides.

What actually matters for developers: OpenAI has been renting Nvidia's GPUs to run inference at scale. Jalapeño is their first step toward owning that layer. If the performance-per-watt claims hold up in production — and engineering samples are already running GPT-5.3 in the lab — the cost of inference at scale comes down. Not tomorrow. But the direction is clear.

The same day, Anthropic revealed that Alibaba ran 28.8 million conversations through 25,000 fake accounts to extract Claude's reasoning patterns. The attack looked like legitimate enterprise traffic from the outside. Both stories point at the same thing: the inference layer is now infrastructure worth fighting over.

https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/

#AI #OpenAI #Semiconductors #LLM #Developers

### Twitter/X

Anthropic says Alibaba ran 25,000 fake accounts, scraped 28.8M Claude conversations, and took the results to train competing models. Called it the largest distillation attack they've ever seen. Wrote to the White House about it.

Your LLM API is infrastructure worth attacking now.

https://www.cnbc.com/2026/06/24/anthropic-alibaba-distillation-campaign.html

#AI #Security #LLM

### Bluesky

OpenAI + Broadcom shipped Jalapeño — a custom LLM inference chip — in 9 months flat. Samples running GPT-5.3 in the lab now. If perf-per-watt claims hold, inference costs will eventually drop. That's the Nvidia dependency story getting complicated.

https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/

#AI #OpenAI #Chips

### Medium

# 28.8 Million Conversations

*Alibaba allegedly drained nearly 29 million Claude exchanges through fake accounts. The attack worked because it looked completely normal.*

Read the number slowly: 28.8 million. That's how many conversations Anthropic says Alibaba-affiliated entities had with Claude between April 22 and June 5 of this year, through nearly 25,000 fraudulent accounts.

My first instinct was skepticism. "Chinese company stole our AI" has a convenient political valence right now, and AI companies have every incentive to frame competitive threats as theft. But Anthropic sent this to the White House. To the Senate. They named a prior incident in February — DeepSeek, MiniMax, Moonshot, 24,000 accounts, 16 million conversations — that we can corroborate independently. The February incident happened. So I'm taking this one seriously.

When I do, the question I can't stop returning to is: what did they actually take?

---

Distillation attacks don't steal model weights. The underlying Claude model stays on Anthropic's servers. What adversarial distillation does is collect (prompt, response) pairs at scale — enough of them, systematically enough, that you can train a smaller model to approximate the original's behavior. You're not cracking the vault. You're standing at the slot in the door, asking questions until you've reconstructed most of what's inside.

This works because LLMs are genuinely effective at producing training signal for other models. Every response is a labeled example. Run enough of them in coordinated patterns, cluster by reasoning structure, and the resulting dataset encodes a real fraction of the model's capabilities. The distilled model has a ceiling — there's a fidelity loss — but if the goal is closing a capability gap cheaply and quickly, this is a rational approach.

Anthropic's terms of service prohibit it. Their rate limits and account verification apparently weren't enough to catch 25,000 coordinated accounts operating for seven weeks.

I build on LLM APIs. I've shipped production applications on Claude and GPT-4 and Gemini. Reading this, I went back and thought about my assumptions around rate limiting. I'd always treated rate limits as a floor — a minimum bar for abuse detection. What I hadn't thought hard enough about is that a patient adversary doesn't need to move fast. They need to move at whatever rate the limits allow, across enough accounts to accumulate volume. 25,000 accounts each operating at a legitimate-looking pace is just a lot of API traffic that looks like enterprise usage in aggregate.

That's the part that genuinely unsettles me. Not the sophistication. The unremarkability of it.

---

The proposed fix — regulatory action, which is what Anthropic is pushing for — isn't wrong exactly. But it will lag. And in the meantime, behavioral fingerprinting is the more interesting technical direction: detecting the semantic patterns of systematic capability extraction versus normal production use. Legitimate enterprise usage is messy. It's domain-specific. It asks off-topic questions and stops mid-conversation. Distillation sampling is structured and has coverage goals. It probably has a different shape in the logs.

Whether that shape is distinguishable reliably at scale, I genuinely don't know. It might not be.

The practical effect for most developers building on commercial APIs is less dramatic than the headlines suggest. You're not the target. But the secondary impact is real: when Anthropic tightens access controls — and they will — the friction goes up for everyone. More identity verification. Stricter rate limits. Longer approval queues. You absorb that collateral because the infrastructure you depend on got weaponized.

There's a third thing worth sitting with. Alibaba's Qwen models have been improving faster than most people expected. We now have documented evidence that at least one Chinese AI lab was systematically extracting capabilities from frontier Western models at scale. The capability gap between top labs and everyone else is real. And it's being closed, at least partly, through this kind of attack. What that means for the competitive landscape in six months, I'm not sure.

Seven weeks. 28.8 million conversations. Someone planned this carefully, coordinated 25,000 accounts, and executed it without triggering detection for nearly two months. That's a lot of investment to pour into something that produces no weights, no code, no direct product. Which tells you something about how much those responses are apparently worth.

https://www.cnbc.com/2026/06/24/anthropic-alibaba-distillation-campaign.html

### Contra

OpenAI's Jalapeño chip announcement opens a concrete window for independent developers.

Right now, inference cost is the reason a lot of AI product ideas don't close economically. The use cases exist. The user demand exists. The math just doesn't work at current pricing. When OpenAI owns its own inference silicon — with claimed performance-per-watt improvements over Nvidia — those economics shift. Probably not this quarter. But the direction is set.

Watch what gets unlocked on Jalapeño first. New inference capabilities tend to get dogfooded internally and then opened to developers at better price points than what's currently possible. Applications that are too expensive to run in production today become viable next. That's historically where new products get built before the rest of the market catches up.

Separate angle: Qualcomm's Tenstorrent acquisition talks point toward open RISC-V inference infrastructure. If that materializes, there's a consulting market for teams wanting to move off Nvidia lock-in.

https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/

### Background Image Prompt

A dramatic horizontal cinematic composition (1500×1000px, no text overlay) visualizing a large-scale data extraction attack on an AI model. Center: a luminous, architectural neural network node — dense, crystalline, electric blue-white — representing a frontier AI model. Radiating outward from this node: 25,000 thin luminous threads, each barely visible individually but collectively forming a glowing web, being pulled toward a dark vortex at the left edge of the frame. The threads carry faint fragments of conversation symbols — abstract text glyphs and reasoning-pattern geometries — dissolving as they're drawn toward the void. The central node pulses with steady blue light while the threads glow amber-red under tension. Background: deep navy space with faint surveillance-grid lines suggesting algorithmic monitoring. Art style: high-detail science fiction digital painting, cinematic chiaroscuro, dramatic tension between the bright center and the consuming darkness at the edge. Dominant colors: deep navy, electric blue, amber, red-gold. Mood: quiet alarm, industrial-scale extraction, something valuable being methodically drained. No characters, no faces, no readable text, no logos, no UI elements.
