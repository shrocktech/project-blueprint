---
name: sitemap
description: Set up, extend or audit automatic XML sitemap generation for a public website, so every indexable page appears without a manual edit, and verify it on the deployed site.
---

# Sitemap

Work from the application root. Its `standards/offering.md` search visibility rules decide which pages are public and indexable. Use this skill for a new public site, when a page type or route group is added, before a public release, and for a requested audit.

## Generate it from the site

A sitemap is generated output, never a hand-edited file or a committed crawler snapshot.

1. Find what the stack already provides and prefer it over custom code: the CMS or framework's built-in sitemap or its maintained official integration. WordPress core serves `/wp-sitemap.xml`, and an active SEO plugin may replace it; keep one source, not two. Static site generators and web frameworks usually offer a sitemap convention, integration or package. Confirm the current method under `standards/packages.md` current product references.
2. Where nothing suitable exists, add a small generator that derives URLs from the same source that produces the pages: the route table, content collection or database query. Run it at build time for a static site, or serve it dynamically for a database-driven site.
3. When an issue adds a page type or route group, include it in the generator in that same issue.

## What belongs in it

- Only canonical, indexable, public URLs that return 200, as absolute HTTPS URLs on the production host.
- Exclude redirects, error pages, `noindex` pages, anything behind a login, admin areas, internal search and filter variations, previews and duplicates.
- Set `lastmod` only from a real content modification date, and omit it otherwise. Omit `priority` and `changefreq`; Google ignores both.
- Use UTF-8 with escaped values. Split into several files under a sitemap index before 50,000 URLs or 50 MB uncompressed.
- Serve it at the site root and reference it from `robots.txt` with a `Sitemap:` line giving the absolute URL.
- Development and preview hosts stay out of search, and their URLs never appear in the production sitemap.

Follow Google's current [sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap) and the [sitemap protocol](https://www.sitemaps.org/protocol.html) where they differ from this summary.

## Prove it

- Add a test to the project's suite that lists the public indexable routes or content and fails when one is missing from the sitemap, or when the sitemap lists a URL that is not public, indexable and successful. Show that a new synthetic page appears without editing the sitemap.
- After each public release, follow the sitemap URL in the live `robots.txt`. Verify valid XML and the expected URL count across all sitemap files, following the index when present. Fetch a representative listed URL from each page type, including any new or changed type, and confirm HTTP 200 and a matching canonical URL.
- Submit the sitemap in Search Console when access is available, or give the owner the exact steps. Submission is a hint, not a guarantee of indexing.
- Record the generator, sitemap URL and test command in `AGENTS.md` or linked private docs, and report any page type not yet covered.
