# AI & Blockchain Digest — July 01, 2026

> Daily roundup of the most important developments in AI and blockchain for developers and tech professionals.

---

## Artificial Intelligence

### EU Council Finalizes AI Act Simplification — High-Risk Deadlines Extended to 2027–2028
On June 29, the EU Council gave its final green light to the AI Act simplification package, completing a legislative journey that began earlier in 2026. The most significant changes for developers are hard timeline extensions: standalone high-risk AI systems now have until December 2, 2027 to comply, and AI embedded in regulated products has until August 2, 2028. A new prohibition on non-consensual AI-generated intimate imagery goes live in December 2026 — any platform generating or editing images of real people needs to review its compliance posture within months, not years.

### GitHub Copilot Closes First Token-Billing Cycle — Some Developers Report 10–50x Cost Spikes
June 30 marked the end of Copilot's first complete 30-day usage-based billing period, and the community reaction has been loud: reports of $29/month plans reaching $750, and $50 subscriptions climbing to $3,000. Code completions remain unlimited across paid plans, but agentic tasks — multi-step coding sessions, automated PR reviews, CI-integrated agents — are where token consumption explodes. Any team with Copilot agents wired into pipelines should pull their June 30 billing statement before assuming old subscription economics still apply.

### Gemini 3.5 Pro Misses Committed June GA Deadline, Slips to Mid-July
Sundar Pichai publicly promised at Google I/O in May that Gemini 3.5 Pro would reach general availability "next month" — June came and went without a public launch, leaving the model in limited Vertex AI enterprise preview. Token efficiency issues have been flagged in long-context coding and reasoning tasks, with a mid-to-late July internal target now circulating but no public commitment. The missed deadline compounds credibility concerns at a moment when four senior Google DeepMind researchers departed for Anthropic — teams evaluating Gemini 3.5 Pro for production workloads should not plan capacity around a June delivery.

### RAISE US Launches With $500M+ to Retrain Workers Displaced by AI
A new nonprofit, RAISE US, launched on June 30 with over $500 million committed toward a $1 billion fundraising target, backed by OpenAI, Anthropic, Microsoft, Amazon, IBM, Bank of America, and the Rockefeller Foundation. Founded by former US Commerce Secretary Gina Raimondo and former Indiana Governor Eric Holcomb, the organization will fund retraining, apprenticeships, and career navigation programs starting in Arkansas, Connecticut, Maryland, and Utah. For developers, this signals a turning point: the largest AI labs are now explicitly co-funding labor displacement mitigation at scale, treating workforce disruption as a shared liability rather than a secondary concern.

---

## Blockchain

### Europe's Unlicensed Crypto Firms Face 'Wipeout' as MiCA Hard Deadline Falls
As of July 1, only about 230 of 1,200+ registered virtual asset service providers in the EU have converted to full MiCA CASP authorization — a conversion rate of roughly 17% — leaving the remaining 80%+ legally unable to continue offering crypto services. Five EU member states have zero licensed CASPs; Germany leads with 56, followed by the Netherlands with 26 and France with 21. Developers integrating EU-facing crypto infrastructure need to immediately verify that counterparties hold valid CASP authorization — platforms without licenses cannot solicit new clients or continue regular services after today.

### MiCA Deadline Could Force 10 Million EU Crypto Users to Find New Platforms
CoinDesk reporting from June 29 estimates that approximately 10 million EU crypto users are currently on non-MiCA-compliant platforms and face sudden disruption if those platforms fail to complete an orderly wind-down. Some unlicensed platforms are attempting asset transfers to licensed CASPs, but coordination is incomplete and many users may encounter service restrictions without advance notice. For product teams building wallet apps, portfolio trackers, or DeFi frontends serving European users, surfacing MiCA compliance status for connected exchanges and liquidity sources is now an urgent feature requirement.

### Dubai Positions as Crypto Destination as MiCA Pushes EU Exodus
CoinDesk reported June 30 that Dubai's VARA is seeing a surge of inbound interest from crypto firms reassessing their EU footprint in the face of MiCA compliance costs, with several EU-based exchanges in active discussions about establishing Dubai subsidiaries as their primary regulatory home. Binance — which withdrew its Greek MiCA application on June 24 and is winding down EU operations — is among the larger firms factoring in alternative jurisdictions. For protocol developers and infrastructure builders, tracking which jurisdictions capture the displaced firm base matters for where compliant liquidity and the next cycle of exchange infrastructure will be built.

### White House Convenes Law Enforcement to Build Support for Crypto's Clarity Act
The White House held a June 29 meeting with law enforcement organizations — including the National Sheriffs Association — to address objections to the Clarity Act's developer-protection provisions. The contested clause protects software developers who don't control deployed tools from money-transmitter classification, a critical safeguard for DeFi builders, while law enforcement argues it creates loopholes for mixers and tumblers; White House crypto advisor Patrick Witt called it "the most pro-law enforcement crypto bill ever considered by Congress." With the Senate heading into a two-week recess, the next 14 days will determine whether US DeFi developers get statutory legal clarity or remain in the gray zone.

### OKX Europe Chief: 80% of Crypto Exchanges Won't Survive MiCA
Erald Ghoos, CEO of OKX Europe, told The Block that he expects 80% of crypto market participants to exit the EU — attributing the attrition not just to MiCA but to the compounding weight of the full EU regulatory stack, including the additional Payment Institution or Electronic Money Institution licenses required for stablecoin offerings. He noted that several firms had approached OKX asking to be acquired purely because they cannot afford the certification process. OKX holds a valid CASP license and is actively recruiting Binance's EU user base, signaling that the post-MiCA market will consolidate quickly around a handful of well-capitalized survivors.

---

## Sources

- [EU Council gives final green light to simplify and streamline AI rules (June 29, 2026)](https://www.consilium.europa.eu/en/press/press-releases/2026/06/29/artificial-intelligence-council-gives-final-green-light-to-simplify-and-streamline-rules/)
- [GitHub Copilot is moving to usage-based billing](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)
- [Gemini 3.5 Pro slips to July and four senior Google researchers just left for Anthropic](https://blog.getbind.co/gemini-3-5-pro-slips-to-july-and-four-senior-google-researchers-just-left-for-anthropic/)
- [RAISE US launches with $500M+ secured for AI workforce programs](https://www.edtechinnovationhub.com/news/raise-us-launches-with-500-million-plus-secured-for-ai-workforce-programs)
- [Europe's unlicensed crypto firms face 'wipeout' as MiCA transition deadline nears (CoinDesk, June 29)](https://www.coindesk.com/policy/2026/06/29/europe-s-unlicensed-crypto-firms-face-wipeout-as-final-regulatory-deadline-falls)
- [MiCA July 1 deadline could leave 10 million crypto users searching for a new platform in the EU (CoinDesk, June 29)](https://www.coindesk.com/business/2026/06/29/mica-july-1-deadline-could-leave-10-million-crypto-users-searching-for-a-new-platform-in-the-eu)
- [Dubai set for crypto firm influx as MiCA deadline pushes companies to reassess Europe (CoinDesk, June 30)](https://www.coindesk.com/policy/2026/06/30/dubai-set-for-crypto-firm-influx-as-mica-deadline-pushes-companies-to-reassess-europe)
- [White House to speak with law enforcement groups to push crypto's Clarity Act (CoinDesk, June 29)](https://www.coindesk.com/policy/2026/06/29/white-house-to-speak-with-law-enforcement-groups-to-push-crypto-s-clarity-act)
- [OKX Europe chief says 80% of crypto exchanges won't survive MiCA as deadline nears (The Block)](https://www.theblock.co/post/405777/okx-europe-chief-mica-deadline-nears)

---

*Generated on 2026-07-01. Next digest: 2026-07-02.*

---

## Social Media Drafts

### LinkedIn

This morning, GitHub Copilot's first token-billing cycle closed. The posts started appearing around noon — developers opening their statements to find $750 where $29 used to be, $3,000 where $50 was. I've been watching the thread carefully because I'm in the same boat.

Here's what I can't shake: most of us had no idea what we were actually consuming. I found a Copilot integration I'd installed months ago and completely forgotten about — it had been running on every PR, calling a reasoning model variant I didn't know was activated. The flat subscription made the cost invisible, so I never had a reason to look.

Usage-based pricing changes that. Not because it's cheaper or more expensive in isolation, but because visibility changes behavior. You notice the agentic tasks running in CI. You see the long-running refactor sessions for what they actually cost in compute. You audit things you'd let run on autopilot.

For developers with Copilot wired into pipelines or automated code review: check your June 30 statement before the next cycle starts.

https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/

#GitHubCopilot #AITools #DeveloperTools #SoftwareEngineering #AIBilling

### Twitter/X

80%+ of EU crypto firms lose operating rights tonight. MiCA hard deadline: July 1. Only 230 of 1,200+ VASPs got licensed. Binance already out. 10M users need new platforms.

https://www.coindesk.com/policy/2026/06/29/europe-s-unlicensed-crypto-firms-face-wipeout-as-final-regulatory-deadline-falls

#MiCA #Crypto #CryptoRegulation

### Bluesky

GitHub Copilot's first usage-based bill just hit. Developers are reporting 10–50x cost spikes — $29/month becoming $750. Agentic tasks and forgotten CI integrations are the culprit. Check your June 30 statement.

https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/

#GitHubCopilot #DevTools #AIBilling

### Medium

# The GitHub Copilot bill landed. I can't look away from the number.

*When AI coding help gets priced per token, you find out what you were actually buying.*

I checked my GitHub billing dashboard this morning knowing it wouldn't be great. June 30 was the end of the first complete 30-day cycle under Copilot's new usage-based pricing. I had a rough sense of how much I'd been using it. I was wrong.

Not catastrophically. But wrong enough to sit with the number for longer than I'd expected.

The horror stories had been circulating all month. $29 plans hitting $750. A $50 monthly subscription becoming $3,000. I'd been reading the threads with that specific kind of detachment you have when you're pretty sure the problem doesn't apply to you. Then I looked at my own statement.

Mine wasn't that bad. But the moment I saw it, I noticed something: I couldn't actually account for all of it.

---

There's a Copilot integration I installed in November and basically forgot about. It hooks into every pull request and runs a review agent. I thought it was a lightweight check — maybe a few completions. Turns out the underlying model calls a reasoning variant for certain file types. I didn't know that. I'd never looked. The cost was invisible under the old flat subscription, so I never had a reason to.

That's the thing that's been sitting with me all day. The old pricing model didn't just make Copilot affordable — it made it opaque. You kicked off an agent to refactor a module, it spun up a chain of calls, and the meter ran in the background while you did something else. You weren't consuming AI assistance. You were receiving it passively, in amounts you had no way to track.

The new pricing forces you to see what you were actually doing.

I'm honestly not sure how I feel about that. The people complaining loudest about 10x bills are — maybe — the ones who were most dramatically underserved by the old model. Not because they got ripped off, but because flat pricing rewards heavy usage and punishes light usage, and somewhere in there, GitHub was making a bet about average consumption that turned out to be off for a vocal subset of power users.

But there's another reading. Maybe the developers seeing the biggest spikes were the ones building the most ambitious agentic workflows. The ones actually getting real leverage out of the tool. And now, with a cost attached to every call, there's a chilling effect. You don't kick off the long-running review because it feels wasteful. You second-guess the automated refactor. The sum of all that caution might cost more in productivity than the extra billing would have in dollars.

I genuinely don't know which camp I'm in. I'm still working through my statement.

---

What I do know: every developer in my circle who uses Copilot is now paying close attention to their usage. That's genuinely new. For two years we all just ran it and treated the subscription as a rounding error, like a gym membership you justify by going twice a month.

The bill made the tool real in a way it wasn't before. Not more useful, necessarily. Just visible. You see the sessions, the agents, the reasoning calls, the hidden integrations you installed and forgot about. It's clarifying in an uncomfortable way — like finding out what the snacks at the free lunch were actually worth.

Whether the new pricing is "fair" is almost beside the point. One AI credit is $0.01. That's not predatory in isolation. The question is whether the workflows people built under the assumption of unlimited flat access still make economic sense when every call costs something. For some teams, probably yes. For others — especially those with Copilot agents wired into CI pipelines or automated code review — June 30 was a wake-up call.

The next 30-day cycle starts now. This time, I'm watching.

https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/

### Contra

GitHub Copilot's first usage-based billing cycle just closed and the numbers are startling — some developers are seeing 10–50x cost increases over their old flat subscriptions. If you're freelancing and billing clients for AI-assisted development, this changes the math immediately.

The opportunity: clients who relied on in-house Copilot setups are suddenly doing cost audits. That creates demand for developers who know how to build efficient agentic workflows — ones that accomplish the same output with fewer token calls. If you understand which Copilot tasks are worth the compute cost and which aren't, you have something concrete to sell right now.

The practical move: map your own token consumption before quoting on any AI-assisted project. Then offer clients a Copilot usage audit as a paid standalone engagement. June 30 opened a window where every engineering manager is asking "what are we actually spending on AI?" — that question is a door.

https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/

### Background Image Prompt

Cinematic horizontal editorial image (1500×1000px, no text overlay). A developer sits at a dark-mode workstation at night, face lit by monitor glow, staring at a terminal window showing a GitHub billing dashboard with a prominently displayed cost meter in soft red-orange showing an unexpectedly high figure. Late-night home office setting, blue-hour city lights visible through a floor-to-ceiling window behind. On screen: lines of code interleaved with billing metrics and AI credit usage charts climbing steeply upward. Dominant palette: deep navy, charcoal, and muted silver with a single red-orange accent on the cost readout. Shallow depth of field — mechanical keyboard sharp in the foreground, background office scene softly blurred. Mood: quiet shock and reckoning, the stillness of discovering something unexpected. Art style: cinematic editorial photography aesthetic, high contrast, modern tech environment, no UI chrome or logos visible.
