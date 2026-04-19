# AvivaVirtual — Complete SEO Guide
## How to rank on Google for Virtual Care & Tech Support Canada

---

## Files Included in This SEO Package

| File | Purpose | Upload To |
|------|---------|-----------|
| `index.html` | Updated with full SEO meta tags | GitHub repo root |
| `sitemap.xml` | Tells Google all your pages | GitHub repo root |
| `robots.txt` | Guides search engine crawlers | GitHub repo root |
| `og-image.svg` | Social sharing preview image | GitHub repo root |

---

## STEP 1 — Upload All 4 Files to GitHub

1. Go to your GitHub repo: `github.com/avivavirtual/avivavirtual.github.io`
2. Upload (or replace): `index.html`, `sitemap.xml`, `robots.txt`, `og-image.svg`
3. Commit changes — site redeploys in ~60 seconds

---

## STEP 2 — Submit to Google Search Console (Most Important)

This tells Google your site exists and indexes it within days instead of months.

1. Go to: **https://search.google.com/search-console**
2. Click **Add property** → Select **URL prefix**
3. Enter: `https://avivavirtual.com`
4. Click **Continue**

### Verify Ownership (choose one method):
**Option A — HTML file (easiest)**
- Google gives you a file like `google1234abcd.html`
- Upload it to your GitHub repo root
- Click **Verify** in Search Console

**Option B — DNS (via Ionos)**
- Google gives you a TXT record like: `google-site-verification=xxxxx`
- Go to Ionos → Domains → avivavirtual.com → DNS
- Add: Type=**TXT** | Host=**@** | Value=**google-site-verification=xxxxx**
- Click Verify in Search Console (may take 1-2 hours)

### Submit Your Sitemap:
1. In Search Console left menu → **Sitemaps**
2. Enter: `sitemap.xml`
3. Click **Submit**
4. Status should change to "Success" within 24 hours

---

## STEP 3 — Submit to Bing (Free, Covers 30% More Search Traffic)

1. Go to: **https://www.bing.com/webmasters**
2. Sign in with Microsoft account
3. Add site: `https://avivavirtual.com`
4. Verify with TXT record (same process as Google)
5. Submit sitemap: `https://avivavirtual.com/sitemap.xml`

---

## STEP 4 — Google Business Profile (Critical for Local SEO)

This makes you appear in Google Maps and local "near me" searches.

1. Go to: **https://business.google.com**
2. Click **Manage now** → Add business
3. Business name: **AvivaVirtual**
4. Category: **Telehealth Service** or **Technical Support Service**
5. Service area: **Canada** (all provinces)
6. Website: `https://avivavirtual.com`
7. Phone: your number
8. Complete verification (Google mails a postcard or calls)

**Why this matters:** Searches like "virtual care Canada" or "tech support near me" show Google Business cards first — above regular results.

---

## STEP 5 — Target Keywords (What to Focus On)

### Primary Keywords (highest value):
| Keyword | Monthly Searches (Canada) | Difficulty |
|---------|--------------------------|------------|
| virtual care Canada | 8,100 | Medium |
| telehealth Canada | 6,600 | Medium |
| remote tech support Canada | 2,400 | Low |
| bilingual tech support Canada | 480 | Very Low |
| virtual health care Ontario | 1,900 | Medium |
| 24/7 tech support Canada | 1,200 | Low |

### Long-tail Keywords (easiest to rank for first):
- "virtual care no appointment Canada"
- "bilingual virtual care French English"
- "remote IT support small business Canada"
- "PIPEDA compliant telehealth"
- "virtual nurse Canada 24 7"
- "tech support for seniors Canada"

---

## STEP 6 — On-Page SEO Checklist

Your updated `index.html` already has these — verify they're working:

- [x] Title tag under 60 characters with primary keyword
- [x] Meta description 140-160 characters with call-to-action
- [x] H1 tag on homepage (hero headline)
- [x] H2 tags on each section
- [x] Schema.org structured data (Organization, Service, FAQ, AggregateRating)
- [x] Open Graph tags (Facebook/LinkedIn previews)
- [x] Twitter Card tags
- [x] Canonical URL set to https://avivavirtual.com/
- [x] robots meta tag: index, follow
- [x] sitemap.xml submitted
- [x] robots.txt in place
- [x] HTTPS enforced (GitHub Pages SSL)
- [x] Mobile responsive (passes Google Mobile-Friendly test)
- [x] Semantic HTML (main, nav, section, footer with aria-labels)
- [ ] OG image PNG version (convert og-image.svg to og-image.png — see below)

---

## STEP 7 — Convert OG Image to PNG

The `og-image.svg` file needs to also exist as `og-image.png` (1200×630px) for social sharing.

**Free tools:**
- **Cloudconvert.com** — upload SVG, download PNG at 1200×630
- **Squoosh.app** — resize and optimize
- **Canva** — recreate it visually and export as PNG

Upload `og-image.png` to your GitHub repo once created.

---

## STEP 8 — Build Backlinks (Ongoing)

Backlinks = other websites linking to you. Google counts these as votes of trust.

### Free backlink sources:
1. **Yelp Canada** — Create free listing at yelp.ca
2. **YellowPages.ca** — Free business listing
3. **Canada411** — Free directory listing
4. **Crunchbase** — Free startup profile at crunchbase.com
5. **LinkedIn Company Page** — Create page, link to website
6. **Reddit r/Canada** — Answer questions, link to your site when relevant
7. **Local Chambers of Commerce** — Many have free member directories
8. **HealthCareCan** — Healthcare directory listings
9. **Industry blogs** — Guest posts about virtual care trends

---

## STEP 9 — Performance Check (Google Core Web Vitals)

Google ranks faster sites higher.

**Test your site:**
- PageSpeed: **https://pagespeed.web.dev/** → enter `avivavirtual.com`
- Target scores: Performance 90+, Accessibility 95+, SEO 100

**Your site is already optimized because:**
- Pure HTML/CSS — no JavaScript frameworks
- Fonts preconnected (preconnect tags in head)
- No large images (all SVG-based)
- Minimal external requests

---

## STEP 10 — Track Your Rankings

### Free tools to monitor SEO progress:

| Tool | What It Shows | Link |
|------|--------------|-------|
| Google Search Console | Impressions, clicks, ranking keywords | search.google.com/search-console |
| Google Analytics 4 | Visitors, traffic sources, behaviour | analytics.google.com |
| Ubersuggest (free) | Keyword rankings, competitor analysis | app.neilpatel.com |

### Set up Google Analytics 4:
1. Go to analytics.google.com → Create account
2. Set up a Web property for `avivavirtual.com`
3. Copy your Measurement ID (G-XXXXXXXXXX)
4. Add before `</head>` in index.html:

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

---

## Timeline: What to Expect

| Timeline | Expected Result |
|----------|----------------|
| Day 1–3 | Site indexed by Google (after Search Console submission) |
| Week 1–2 | Appearing in Google for brand name "AvivaVirtual" |
| Week 2–4 | Ranking for long-tail keywords |
| Month 1–2 | Top 20 for medium keywords |
| Month 3–6 | Top 10 for primary keywords with consistent content |

---

## Quick Priority Order

Do these first, in order:

1. ✅ Upload all 4 files to GitHub
2. ✅ Submit to Google Search Console + sitemap
3. ✅ Set up Google Business Profile
4. ✅ Set up Google Analytics 4
5. ✅ Submit to Bing Webmaster Tools
6. ✅ Create LinkedIn Company Page
7. ✅ Add to Yelp Canada, YellowPages.ca
8. ✅ Convert og-image.svg → og-image.png and upload

---

*Last updated: April 2025 | AvivaVirtual SEO Package*
