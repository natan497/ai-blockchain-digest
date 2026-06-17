# AI & Blockchain Digest — Session Instructions

## News freshness (strictly enforced)
- Only include stories published within the **last 24 hours** (yesterday and today’s date)
- Every web search query must include the exact current date AND the day before
  - Example: `"June 18 2026" OR "June 17 2026" AI news`
- Reject any story older than 48 hours — do not use it even if no fresher story exists on that topic
- If a platform returns no fresh stories, note that and move on — never pad with older content

## News sourcing — search ALL platforms before writing
Run **at least 8 separate web searches** per run, covering these sources:

**AI / tech:**
- TechCrunch AI
- The Verge tech news
- VentureBeat AI
- Hacker News front page (`news.ycombinator.com`) — look for Show HN and trending posts
- artificialintelligence-news.com
- buildfastwithai.com
- Bloomberg AI / Reuters technology
- Google News AI topic

**Blockchain / crypto:**
- CoinDesk (coindesk.com)
- The Block (theblock.co)
- CryptoNews (cryptonews.com)
- Decrypt (decrypt.co)
- Bloomberg Crypto
- Cointelegraph
- Yahoo Finance Crypto

Always search for **"breaking news"** and **"today"** variants. Cross-reference: if a story appears on 3+ sources it is likely top news.

## Story selection criteria
- 4–5 stories per section (AI and Blockchain)
- Must be within 24 hours of the post date
- Prioritise: breaking exclusives, major product launches, regulatory moves, significant protocol upgrades
- Developer / tech-professional angle required: explain the “so what” for builders in every summary
- Avoid: pure price speculation, token price recaps, obvious hype without technical substance

## Post cadence
- Published **daily**
- Intro blockquote: “Daily roundup of the most important developments in AI and blockchain for developers and tech professionals.”
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

**Story focus rule:** Pick the **1–2 most impactful stories** of the day across both sections and write ALL platform drafts about those stories only. Do not summarise the full digest across platforms — depth on the top story beats breadth across all stories.

Append this section after the footer. Use exactly these `###` headings:

### LinkedIn
Focus on the 1–2 top stories. Professional tone. 150–200 words. Explain the developer/business implication clearly. End with 3–5 hashtags.

### Twitter/X
Focus on the single most breaking story. Max 280 characters. Strong hook. Include a call-to-action ("Full digest →"). 2–3 hashtags.

### Bluesky
Focus on the single most breaking story. Max 300 characters. Slightly more casual than Twitter. 2–3 hashtags.

### Medium
Teaser intro paragraph (80–100 words) focused on the top story. Designed to pull readers into the full post. No hashtags.

### Contra
Freelancer / builder angle (100–150 words) focused on the top story. Frame the news as a concrete opportunity for independent developers — what can they build or offer as a direct result of this specific story?

### Background Image Prompt
A detailed prompt for Midjourney / DALL-E / Stable Diffusion that **visually represents the actual top news story** — not generic tech imagery. Describe the real-world event, entities, or concept from the story in visual terms. Include: style, mood, dominant colours, specific subject matter tied to the story, aspect ratio (16:9, 1200x400 hero banner). No text overlay.

## Deployment
- **Never push directly to `master`**
- Create a PR for every new post
- PR title: `AI & Blockchain Digest — Month DD, YYYY`
- Merging to `master` triggers automatic GitHub Pages deploy
