# Partnership Turning Points

An independent editorial project by Matthew Batcheldor. One hundred case studies about the alliances that changed what companies could do, where they could go and whom they could reach.

## The archive

- Editions 01 to 06. Fifteen cases each.
- Edition 07. A final ten cases.
- The Index. A searchable view of all 100 cases, with filters for partnership type, industry, geography and strength of evidence.

A companion to [Brand Turning Points](https://mattbatcheldor.github.io/brand-turning-points/the-index/). Follow its edition structure, editorial navigation, case cards and visible sourcing. Each edition opens with a finding and a note on scope, then presents the cases, selected original media and evidence.

## Proposed design direction

| Element | Treatment |
| --- | --- |
| Palette | Warm paper #F7F3EA, ink #172C2A, deep teal #075950 for links and actions, soft sage #DBE9E1 for panels and muted clay #C97B60 for decorative accents |
| Type | Source Serif 4 for the masthead and headlines, Source Sans 3 for reading and navigation, with Georgia and system sans fallbacks |
| Reading layout | 18px body text, generous line spacing, a measure of about 68 characters, and one-column case cards on mobile |
| Family resemblance | Keep the numbered editions, editorial masthead, archive index and evidence labels. Give this project its own colour and typography. |

## Case study structure

1. **The situation.** What was difficult for either organisation to do alone?
2. **The exchange.** What did each partner contribute and what did each stand to gain?
3. **The turning point.** What launched, changed or ended?
4. **What the evidence shows.** Give dated outcomes, identify who reported them and flag undisclosed terms or unclear attribution.
5. **What to take into a deal.** Offer one specific lesson or question for a partnership team.
6. **Sources and media.** Link the announcement and outcome evidence separately. Credit images and identify whether video is original footage or a later account.

Write in British English. Include deals that stalled or failed alongside successes, and distinguish a signed agreement from a launched partnership and a measured result.

## Build and preview

The site is built from the files in `src/`, using the same engine as Brand Turning Points.

- `src/campaigns-NN.json` holds each edition's cases, `src/page-template-NN.html` its page copy, and `src/site.css` and `src/site.js` the shared design and behaviour.
- Edition settings, including the screening-room films, live in `EDITIONS` in `src/build.py`.
- Run `python3 src/build.py` to rebuild every page, then commit the source and the output together.
- Edition 01 is the home page (`index.html`), and `edition-01/` forwards to it.
- The Index (`the-index/`) is built from every edition's case file, using `src/page-template-index.html`. Its lessons and partner notes live in `LESSONS` and `PARTY_NOTES` in `src/build.py`, and the build stops if a partner who appears in two editions has no note.

`main` is the only source of truth, and GitHub Pages publishes from it. Start new work from the latest `main`, and never force-push to it.
