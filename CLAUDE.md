# AI & Blockchain Digest — Session Instructions

## News freshness (strictly enforced)
- Only include stories published within the **last 24 hours** (yesterday and today's date)
- Every web search query must include the exact current date AND the day before
  - Example: `"June 18 2026" OR "June 17 2026" AI news`
- Reject any story older than 48 hours — do not use it even if no fresher story exists on that topic
- If a platform returns no fresh stories, note that and move on — never pad with older content

## News sourcing — use deep-research skill

**Always invoke the `/deep-research` skill** as the first step of every run. Do not skip this in favour of raw web searches — deep-research fetches actual article content, runs adversarial cross-verification, and returns cited findings that are far more reliable than search-snippet summaries.

Pass a focused research question as the args, for example:
> "What are the most significant AI and blockchain news stories published on [today's date] or [yesterday's date], relevant to software developers and tech professionals? Cover sources including TechCrunch, The Verge, VentureBeat, Hacker News, buildfastwithai.com, CoinDesk, The Block, Cointelegraph, Decrypt, and Bloomberg. For each story confirm the publication date and that it is within the last 24 hours."

The skill will fan out parallel searches, fetch source articles, adversarially verify claims across sources, and return a cited synthesis. Use that output as the factual basis for writing the digest — do not add stories from memory or older searches.

**Sources to cover (instruct deep-research to check all of these):**

*AI / tech:* TechCrunch AI, The Verge, VentureBeat AI, Hacker News (`news.ycombinator.com`), artificialintelligence-news.com, buildfastwithai.com, Bloomberg AI / Reuters technology, Google News AI topic

*Blockchain / crypto:* CoinDesk, The Block, CryptoNews, Decrypt, Bloomberg Crypto, Cointelegraph, Yahoo Finance Crypto

**After deep-research completes:** if any section has fewer than 4 confirmed fresh stories, run 1–2 targeted follow-up WebSearch queries to fill the gap. Always search for "breaking news" and "today" variants. Cross-reference: if a story appears on 3+ sources it is likely top news.

## Story selection criteria
- 4–5 stories per section (AI and Blockchain)
- Must be within 24 hours of the post date
- Prioritise: breaking exclusives, major product launches, regulatory moves, significant protocol upgrades
- Developer / tech-professional angle required: explain the "so what" for builders in every summary
- Avoid: pure price speculation, token price recaps, obvious hype without technical substance

## Post cadence
- Published **daily**
- Intro blockquote: "Daily roundup of the most important developments in AI and blockchain for developers and tech professionals."
- Footer: `*Generated on YYYY-MM-DD. Next digest: YYYY-MM-DD.*` — next date is always **tomorrow**
- Filename: `posts/YYYY-MM-DD-ai-blockchain-digest.md`

## Required post structure (in order)
1. `# AI & Blockchain Digest — Month DD, YYYY`
2. Blockquote intro
3. `---`
4. `## Artificial Intelligence` (4–5 stories, each with `### Story Title` + 3-sentence summary)
5. `---`
6. `## Blockchain` (4–5 stories, same format)
7. `---`
8. `## Sources` (bulleted markdown links)
9. `---`
10. `*Generated on YYYY-MM-DD. Next digest: YYYY-MM-DD.*`
11. `---`
12. `## Social Media Drafts` (see format below)

## Social Media Drafts section

**Humanization requirement (all platforms):** Every draft must read as if written by a real person with a genuine point of view. Avoid:
- Formulaic openers ("In a significant development…", "Today marks…", "It is worth noting…")
- Three-part structures that feel like an essay outline
- Generic "developer takeaway" or "key implication" labels
- Overly polished, risk-free language — a real person has opinions and uses contractions

**Story focus rule:** Pick the **1–2 most impactful stories** of the day and write ALL platform drafts about those stories only. Do not summarise all stories across platforms.

**Links in social drafts — always use the real source news URL, not the GitHub Pages digest link.**
Each draft must link to the **actual news article** being referenced (e.g., the TechCrunch URL, CoinDesk article URL, etc.). Do NOT link to `natan497.github.io`. This drives readers directly to the primary source.

Use exactly these `###` headings:

### LinkedIn
Professional but personal tone — write as a developer sharing something they found genuinely interesting, not as a brand account. 150–200 words focused on the top 1–2 stories. No bullet lists, no bold "key takeaway" lines, no three-part essay structure. End with the **real source URL** of the article on its own line, then 3–5 hashtags. **Do NOT add "Full digest ↓" or any placeholder link text.**

### Twitter/X
Single most breaking story. Max 280 characters (excluding URL — Twitter auto-shortens to 23 chars). Strong hook. End with the **real source URL** of the article on its own line, then 2–3 hashtags. **Do NOT add "Full digest → [link]" or any placeholder text.**

### Bluesky
Single most breaking story. Max 300 characters. Slightly casual. End with the **real source URL**. 2–3 hashtags.

### Medium
Full blog post — must be a **3-minute read (~700–900 words)**. Medium flags AI-generated content; this draft MUST read as authentic human writing or it will be filtered.

**Voice — the non-negotiables:**
- Write in **first person** with genuine perspective: real opinions, honest admissions, actual curiosity
- Open with a **specific moment or observation**, not background context. Never open with "If you work in AI…" or "There are a handful of papers that…" or "There's a version of this story that writes itself"
- Argue **one specific angle** — possibly counterintuitive — not a comprehensive summary of the news
- Include honest uncertainty: "I might be wrong," "I genuinely don't know," "I'm not sure what to make of this"
- Sound like a developer who found this genuinely interesting, not a journalist summarising a briefing

**Sentence rhythm (burstiness is essential):**
- Mix very short sentences and fragments with longer ones unpredictably — AI writes in uniform medium-length sentences, humans don't
- Start sentences with "But," "And," "So" where natural — humans do, AI avoids it
- Use sentence fragments. Occasionally. They read as human.
- Avoid triplet structures: "X, Y, and Z" or "not X, but Y — it's Z" appear constantly in AI output

**Banned phrases and patterns (AI detector red flags):**
- "Here's what I keep coming back to" — overused AI tell
- "What's interesting about X isn't Y — it's Z" — classic AI scaffolding
- "That's not a career. That's a thesis." — parallel one-two punch sentences
- "Different X, different Y, same Z" — triplet contrast structure
- "The gap between X and Y" — abstract framing AI loves
- "X has navigated that problem before" — polished analytical wrap-up
- Any sentence that could be a subheading in disguise

**Structure — break the AI explainer template:**
- Maximum **2 `##` section headers** in the whole piece — use `---` as a break instead
- Do NOT use the intro → context → analysis → "what developers should watch" → conclusion pattern
- No bullet-point lists inside the body. No bold "key takeaway" bullets. No "Developer angle:" labels anywhere
- The ending should be **understated**, not punchy — humans trail off, AI lands cleanly

**Technical:**
- **Title**: argument-forward, not neutral — something the writer actually believes (use `# Title`)
- **Subtitle**: one-sentence hook (use `*Subtitle*`)
- End with the real source URL, no label

### Contra
Freelancer/builder angle. 100–150 words focused on the top story. Frame as concrete opportunities for independent developers. End with the real source URL.

### Background Image Prompt
A prompt formatted specifically for **ChatGPT image generation (DALL-E)** to produce a **Medium blog header image** (horizontal, 1500×1000px, no text overlay). The prompt must visually represent the **actual top news story** — reference the real event, entities, and concept specifically. Include art style, mood, dominant colours, and subject matter tied directly to the story.

## Social Media Drafts formatting rule
**Do NOT place `---` horizontal rules between the `###` platform sections** (LinkedIn, Twitter/X, Bluesky, Medium, Contra, Background Image Prompt). The `###` headings are sufficient separators. Adding `---` causes the divider to be copied along with the draft text when using the Copy button. Exception: `---` section breaks *inside* the Medium body are fine.

## Deployment
- **Never push directly to `master`**
- Create a PR for every new post
- PR title: `AI & Blockchain Digest — Month DD, YYYY`
- Merging to `master` triggers automatic GitHub Pages deploy
