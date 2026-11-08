from html import escape
from pathlib import Path
import collections
import json
import re
import random

root = Path(__file__).resolve().parent
e = escape

def exchange_art():
    # Editorial illustration: two circles, one per partner, overlapping on a multiplication sign.
    serif = "'Source Serif 4', Georgia, serif"
    sans = "'Source Sans 3', Arial, sans-serif"
    return f'''<svg viewBox="0 0 920 560" preserveAspectRatio="xMidYMid slice" role="img" aria-labelledby="art-title">
<title id="art-title">Illustration of two overlapping circles, one labelled brand A and one labelled brand B, meeting at a large multiplication sign. A line underneath asks what each side brought.</title>
<path d="M0 0h920v560H0z" fill="#172C2A"/>
<g opacity=".18" stroke="#DBE9E1" stroke-width="1">{''.join(f'<path d="M{x} 0v560"/>' for x in range(40, 920, 40))}</g>
<circle cx="370" cy="270" r="190" fill="#075950" opacity=".92"/>
<circle cx="550" cy="270" r="190" fill="#C97B60" opacity=".85" style="mix-blend-mode:screen"/>
<path d="M460 105a190 190 0 0 1 0 330a190 190 0 0 1 0-330z" fill="#DBE9E1"/>
<path d="M432 242l56 56M488 242l-56 56" stroke="#172C2A" stroke-width="14" stroke-linecap="round"/>
<text x="290" y="276" text-anchor="middle" font-family="{sans}" font-size="20" font-weight="700" letter-spacing="3" fill="#F7F3EA">BRAND A</text>
<text x="630" y="276" text-anchor="middle" font-family="{sans}" font-size="20" font-weight="700" letter-spacing="3" fill="#172C2A">BRAND B</text>
<text x="460" y="508" text-anchor="middle" font-family="{serif}" font-size="26" font-style="italic" fill="#F7F3EA">What did each side bring?</text>
<text x="460" y="52" text-anchor="middle" font-family="{sans}" font-size="14" letter-spacing="3" fill="#DBE9E1">EDITION 01 / FAME FIRST</text>
</svg>'''

LEVELS = ['Modelled effect', 'Sales trend', 'Survey', 'Reach only', 'Archival']
LEVEL_NOTES = {
    'Modelled effect': 'A model estimates the effect against a baseline.',
    'Sales trend': 'Sales, sign-ups or revenue moved, but other causes are not separated out.',
    'Survey': 'People who saw it said something changed.',
    'Reach only': 'The number counts attention, not what either partner gained.',
    'Archival': 'The record shows the partnership happened, not what it earned.',
}
# In this archive the "mechanism" is the exchange: what each side traded.
MECHANISMS = [
    ('Licence', 'One side lends a story or character the other could not create.'),
    ('Talent for scale', 'A designer or artist brings taste, and a big brand brings reach.'),
    ('Product for product', 'Two products combine into something neither could sell alone.'),
    ('Content for reach', 'One side makes something worth watching, and the other gets it seen.'),
    ('Platform for audience', 'A platform lends its users, and a partner brings a reason to show up.'),
    ('Money for association', 'One side pays to stand next to something people already love.'),
]
ROLES = ['Co-branded product', 'Designer collaboration', 'Licence', 'Content partnership', 'Platform integration', 'Sponsorship and placement']
# Every case is sorted by the type of partnership.
ROLE_DEFAULTS = {'roles': ROLES, 'role_label': 'Type', 'role_aria': 'Type of partnership', 'source_label': 'The partners'}
ERAS = ['1950s to 1980s', '1990s and 2000s', '2010s', '2020s']


def era(year):
    if year < 1990:
        return ERAS[0]
    if year < 2010:
        return ERAS[1]
    if year < 2020:
        return ERAS[2]
    return ERAS[3]


def strength_of(level):
    return len(LEVELS) - LEVELS.index(level)


def meter(level):
    strength = strength_of(level)
    bars = ''.join(f'<i class="{"on" if n < strength else ""}"></i>' for n in range(len(LEVELS)))
    return (f'<span class="meter s{strength}" role="img" aria-label="Evidence strength {strength} of {len(LEVELS)}: {e(level)}">'
            f'<span class="bars" aria-hidden="true">{bars}</span><span class="meter-label" aria-hidden="true">{e(level)}</span></span>')


def slug(text):
    return text.lower().replace(' ', '-')


def campaign_image(c, placement, prefix=''):
    image = c.get('image')
    if not image:
        return ''
    fit = ' image-contain' if image.get('contain') else ''
    return (f'<span class="{placement}{fit}"><img src="{e(prefix + image["src"])}" '
            f'alt="{e(image["alt"])}" width="{image["width"]}" height="{image["height"]}" '
            'loading="lazy" decoding="async"></span>')


def proof_tile(c):
    # Used where a case has no licensed image: a type tile that names how the effect was proved,
    # or, in a data edition, how the data was used and where it came from.
    if c.get('data_role'):
        cls, label = f'r-{slug(c["data_role"])}', f'{c["data_role"]} / {c["data_source"]}'
    else:
        cls, label = f'm-{slug(c["mechanism"])}', c.get('method') or c['evidence_level']
    return (f'<span class="case-thumbnail proof-tile {cls}" aria-hidden="true">'
            f'<span class="tile-year">{c["year"]}</span><span class="tile-method">{e(label)}</span></span>')


def render_cards(campaigns, notes, test_heading, prefix='', source_label='The partners'):
    # Partnership Turning Points uses a six-part case: the situation, the exchange, the turning point,
    # what the evidence shows, what to take into a deal, and sources and media.
    cards = []
    for i, c in enumerate(campaigns, 1):
        creative = c['creative']
        image = c.get('image')
        outcome_label, outcome_url = c['impact_source']
        announce_label, announce_url = c['announcement']
        legacy = c['stat_type'] == 'legacy'
        stat_tag = '<p class="stat-tag small">Legacy fact, not a result</p>' if legacy else ''
        deal = f'<p class="deal-tag"><span class="small">Deal value</span> {e(c["deal_value"])}</p>' if c.get('deal_value') else ''
        credit = f'\n<p class="case-credit small">{e(c["credit"])}</p>' if c.get('credit') else ''
        if creative.get('url'):
            creative_link = f'<a href="{e(creative["url"])}">{e(creative["label"])}</a>'
        else:
            creative_link = f'<p class="no-copy">{e(creative["label"])}</p>'
        image_credit = f'\n<p class="image-credit">Image: <a href="{e(image["source"])}">{e(image["credit"])}</a></p>' if image else ''
        thumbnail = campaign_image(c, 'case-thumbnail', prefix) or proof_tile(c)
        brought = ''.join(f'<li><strong>{e(name)}</strong> {e(what)}</li>' for name, what in c['brought'])
        extra = ''.join(f'<li><a href="{e(url)}">{e(label)}</a></li>' for label, url in c['links'])
        cards.append(f'''<details id="{e(c['id'])}" class="case" data-mechanism="{e(c['mechanism'])}" data-evidence="{e(c['evidence_level'])}" data-era="{e(era(c['year']))}" data-role="{e(c['data_role'])}">
<summary>
<span class="case-number small">{i:02d}</span>
{thumbnail}
<span class="case-heading"><span class="case-brand small">{e(c['brand'])} / {c['year']} / {e(c['mechanism'])}</span><span class="case-title">{e(c['title'])}</span><span class="case-hook">{e(c['hook'])}</span><span class="case-data"><strong>{e(c['data_role'])}</strong> · {e(c['stage'])}</span></span>
<span class="metric-cell{' legacy' if legacy else ''}"><span class="row-metric">{e(c['metric'])}</span><span class="row-label small">{e(c["metric_label"])}{' · legacy fact' if legacy else ''}</span>{meter(c['evidence_level'])}</span>
<span class="toggle" aria-hidden="true"></span>
</summary>
<div class="case-inner">
<div>
<p class="case-meta">{e(c['place'])} / {e(c['sector'])}</p>{credit}
<h3>The situation</h3><p>{e(c['situation'])}</p>
<h3>The exchange</h3><p>{e(c['exchange'])}</p>
<ul class="brought">{brought}</ul>
<h3>The turning point</h3><p>{e(c['turning_point'])}</p>
<div class="memory take"><h3>My take</h3><p>{e(c['take'])}</p></div>
<div class="creative-record">
<h3>{e(creative.get('heading', 'Media'))} <span>{e(creative['medium'])}</span></h3>
{creative_link}{image_credit}
</div>
</div>
<aside class="proof" aria-label="Evidence">
<h3>{'Headline fact' if legacy else 'Outcome'} <span>{e(c['stage'])}</span></h3>
<p class="proof-value">{e(c['metric'])}</p>
{stat_tag}
<p class="proof-metric">{e(c['measure'])}</p>{deal}
<div class="proof-strength"><span class="small">Evidence strength</span>{meter(c['evidence_level'])}<p>{e(notes[c['evidence_level']])}</p></div>
<p class="impact-citation"><span class="small">Outcome source</span> <a href="{e(outcome_url)}">{e(outcome_label)}</a></p>
</aside>
</div>
<details class="full-case">
<summary><span>Read the full case</span><span class="toggle" aria-hidden="true"></span></summary>
<div class="full-inner">
<div>
<h3>What the evidence shows</h3><p>{e(c['evidence'])}</p>
<h3>What to take into a deal</h3><p>{e(c['lesson'])}</p>
</div>
<div>
<h3>Sources</h3>
<ul class="sources"><li><span class="small">Announcement</span> <a href="{e(announce_url)}">{e(announce_label)}</a></li><li><span class="small">Outcome</span> <a href="{e(outcome_url)}">{e(outcome_label)}</a></li>{extra}</ul>
</div>
</div>
</details>
</details>''')
    return cards


def render_ladder(campaigns, notes, compare=None):
    ladder = []
    for level in LEVELS:
        group = [c for c in campaigns if c['evidence_level'] == level]
        links = ', '.join(f'<a href="#{e(c["id"])}">{e(c["brand"])}</a>' for c in group)
        if compare is None:
            ladder.append(f'''<li class="s{strength_of(level)}"><span class="ladder-name">{meter(level)}</span>
<span class="ladder-count"><b>{len(group)}</b><span class="ladder-bar" style="--n:{len(group)}" aria-hidden="true"></span></span>
<span class="ladder-cases"><span class="ladder-note">{e(notes[level])}</span> {links}</span></li>''')
        else:
            before = sum(1 for c in compare['campaigns'] if c['evidence_level'] == level)
            ladder.append(f'''<li class="s{strength_of(level)} compare-row"><span class="ladder-name">{meter(level)}</span>
<span class="ladder-pair"><span class="pair-row now"><b>{len(group)}</b><span class="ladder-bar" style="--n:{len(group)}" aria-hidden="true"></span><span class="sr">in this edition</span></span><span class="pair-row then"><b>{before}</b><span class="ladder-bar" style="--n:{before}" aria-hidden="true"></span><span class="sr">in {e(compare['label'])}</span></span></span>
<span class="ladder-cases"><span class="ladder-note">{e(notes[level])}</span> {links or '<span class="none">None in this edition</span>'}</span></li>''')
    return ladder


def render_role_grid(campaigns, all_roles=ROLES, role_aria='How data was used'):
    roles = [r for r in all_roles if any(c.get('data_role') == r for c in campaigns)]
    if not roles:
        return ''
    levels = [l for l in LEVELS if any(c['evidence_level'] == l for c in campaigns)]
    cells = ['<span class="rg-corner" aria-hidden="true"></span>'] + [f'<span class="rg-head">{e(l)}</span>' for l in levels]
    brands = [c['brand'] for c in campaigns]
    def chip_label(c):
        # Name the year too when a brand appears more than once, so two IBM chips can be told apart.
        return f'{c["brand"]} {c["year"]}' if brands.count(c['brand']) > 1 else c['brand']
    for r in roles:
        cells.append(f'<span class="rg-role">{e(r)}</span>')
        for l in levels:
            group = [c for c in campaigns if c.get('data_role') == r and c['evidence_level'] == l]
            chips_html = ''.join(f'<a class="rg-chip s{strength_of(l)}" href="#{e(c["id"])}">{e(chip_label(c))}</a>' for c in group)
            cells.append(f'<span class="rg-cell{" empty" if not group else ""}" data-level="{e(l)}">{chips_html}</span>')
    return (f'<div class="role-grid" style="--cols:{len(levels)}" role="group" aria-label="Cases by {e(role_aria.lower())} and by evidence strength">'
            + ''.join(cells) + '</div>')


def series_modelled(edition):
    parts = []
    for other in EDITIONS:
        data = root / other['data']
        if not data.exists():
            continue
        n = sum(1 for c in json.loads(data.read_text(encoding='utf-8')) if c['evidence_level'] == 'Modelled effect')
        parts.append((f'{n} here' if n else 'none here') if other is edition else (f'{n} in Edition {other["number"]}' if n else f'none in Edition {other["number"]}'))
    return ', '.join(parts[:-1]) + ' and ' + parts[-1] if len(parts) > 1 else (parts[0] if parts else '')


def present_mechanisms(campaigns, mechanisms=None):
    # An edition can name its own mechanisms (Edition 05 sorts failures by the mistake behind them).
    return [(m, note) for m, note in (mechanisms or MECHANISMS) if any(c['mechanism'] == m for c in campaigns)]


def render_mechanisms(campaigns, mechanisms=None):
    cols = []
    for name, note in present_mechanisms(campaigns, mechanisms):
        items = ''.join(f'<li><a href="#{e(c["id"])}">{e(c["brand"])} <span>{c["year"]}</span></a></li>'
                        for c in sorted(campaigns, key=lambda c: c['year']) if c['mechanism'] == name)
        cols.append(f'<div class="mech"><h3><button class="mech-pick" type="button" data-value="{e(name)}">{e(name)}</button></h3><p>{e(note)}</p><ul>{items}</ul></div>')
    return cols


def render_timeline(campaigns):
    first, last = min(c['year'] for c in campaigns), max(c['year'] for c in campaigns)
    span = last - first
    decades = [y for y in range((first // 10 + 1) * 10, last + 1, 10)]
    ticks = ''.join(f'<span class="tick" style="--x:{(y - first) / span * 100:.2f}%">{y}</span>' for y in decades)
    dots, stacks = [], {}
    for c in sorted(campaigns, key=lambda c: c['year']):
        stack = stacks.get(c['year'], 0)
        stacks[c['year']] = stack + 1
        dots.append(f'<a class="dot s{strength_of(c["evidence_level"])}" href="#{e(c["id"])}" data-id="{e(c["id"])}" style="--x:{(c["year"] - first) / span * 100:.2f}%;--y:{stack}" title="{e(c["brand"])}, {c["year"]}. {e(c["evidence_level"])}"><span class="sr">{e(c["brand"])}, {c["year"]}</span></a>')
    return f'<div class="timeline" role="group" aria-label="Partnerships by year, {first} to {last}">{"".join(dots)}<div class="axis" aria-hidden="true">{ticks}</div></div>'


def chips(group, values):
    out = [f'<button class="filter" type="button" data-group="{group}" data-value="All" aria-pressed="true">All</button>']
    out += [f'<button class="filter" type="button" data-group="{group}" data-value="{e(v)}" aria-pressed="false">{e(v)}</button>' for v in values]
    return ''.join(out)


def render_filters(campaigns, all_roles=ROLES, role_label='Data use', role_aria='How data was used', mechanisms=None, mech_label='Mechanism'):
    mech_names = [m for m, _ in present_mechanisms(campaigns, mechanisms)]
    levels = [l for l in LEVELS if any(c['evidence_level'] == l for c in campaigns)]
    eras = [x for x in ERAS if any(era(c['year']) == x for c in campaigns)]
    roles = [r for r in all_roles if any(c.get('data_role') == r for c in campaigns)]
    role_row = f'<div class="filter-row" role="group" aria-label="{e(role_aria)}"><span class="small">{e(role_label)}</span>{chips("role", roles)}</div>' if roles else ''
    return role_row + (f'<div class="filter-row" role="group" aria-label="{e(mech_label)}"><span class="small">{e(mech_label)}</span>{chips("mechanism", mech_names)}</div>'
            f'<div class="filter-row" role="group" aria-label="Evidence strength"><span class="small">Evidence</span>{chips("evidence", levels)}</div>'
            f'<div class="filter-row" role="group" aria-label="Era"><span class="small">Era</span>{chips("era", eras)}</div>')


def render_screenings(campaigns, screening, prefix=''):
    screenings = []
    for case_id, note, drawn in screening:
        c = next(entry for entry in campaigns if entry['id'] == case_id)
        creative = c['creative']
        url = creative.get('screening_url', creative['url'])
        video = url.partition('https://www.youtube.com/watch?v=')[2]
        player = ''
        if video:
            player = f'<button class="play-film small" type="button" data-video="{e(video)}" data-title="{e(c["title"])}" hidden>Play here</button>'
        frame = campaign_image(c, 'film-frame', prefix) or f'<span class="film-frame drawn {drawn}" aria-hidden="true"></span>'
        screenings.append(f'''<article class="screening">
{frame}
<div class="film-body">
<div class="film-heading"><p class="small">{e(c['brand'])} / {c['year']}</p><h3>{e(c['title'])}</h3></div>
<p>{e(note)}</p>
<div class="film-actions">
{player}<a href="{e(url)}">{'Watch on YouTube' if video else 'Watch at HAT'}</a>
<a href="#{case_id}">Read the case</a>
</div>
</div>
</article>''')
    return screenings


def relative_dir(from_output, to_output):
    import posixpath
    here = posixpath.dirname(from_output) or '.'
    there = posixpath.dirname(to_output) or '.'
    rel = posixpath.relpath(there, here)
    return '' if rel == '.' else rel + '/'


def render_edition_nav(edition):
    links = []
    for other in EDITIONS:
        if not (root / other['data']).exists():
            continue
        label = f'<span class="sr">Edition </span>{other["number"]}'
        if edition is not None and other is edition:
            links.append(f'<a href="#top" aria-current="page" title="Edition {other["number"]}{", " + other["name"] if other.get("name") else ""}">{label}</a>')
        else:
            href = relative_dir(edition['output'] if edition else INDEX_OUTPUT, other['output']) or './'
            links.append(f'<a href="{href}" title="Edition {other["number"]}{", " + other["name"] if other.get("name") else ""}">{label}</a>')
    here = edition['output'] if edition else INDEX_OUTPUT
    if not INDEX_READY:
        pass
    elif edition:
        links.append(f'<a class="index-link" href="{relative_dir(here, INDEX_OUTPUT)}" title="The Index: the whole series in one place">Index</a>')
    else:
        links.append('<a class="index-link" href="#top" aria-current="page" title="The Index: the whole series in one place">Index</a>')
    return f'<span class="edition-nav"><span class="edition-nav-label" aria-hidden="true">Editions</span>{"".join(links)}</span>'


def write_forwarding_page(edition):
    alias = edition.get('alias')
    if not alias:
        return None
    target = relative_dir(alias, edition['output']) or './'
    page = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Brand Turning Points | Edition {edition["number"]}{", " + edition["name"] if edition.get("name") else ""}</title>
<link rel="canonical" href="{target}">
<meta http-equiv="refresh" content="0; url={target}">
<meta name="robots" content="noindex">
</head>
<body>
<p><a href="{target}">Open Brand Turning Points, Edition {edition["number"]}</a></p>
<script>location.replace({json.dumps(target)} + location.hash);</script>
</body>
</html>
'''
    out = root.parent / alias
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding='utf-8')
    return out


def build(edition):
    campaigns = json.loads((root / edition['data']).read_text(encoding='utf-8'))
    notes = dict(LEVEL_NOTES, **edition.get('level_notes', {}))
    prefix = edition.get('asset_prefix', '')
    compare = None
    if edition.get('compare'):
        compare = {'label': edition['compare']['label'],
                   'campaigns': json.loads((root / edition['compare']['data']).read_text(encoding='utf-8'))}
    template = (root / edition['template']).read_text(encoding='utf-8')
    css = (root / 'site.css').read_text(encoding='utf-8')
    js = (root / 'site.js').read_text(encoding='utf-8')
    r = dict(ROLE_DEFAULTS, **edition.get('roles', {}))
    modelled = sum(1 for c in campaigns if c['evidence_level'] == 'Modelled effect')
    compare_modelled = sum(1 for c in (compare or {}).get('campaigns', []) if c['evidence_level'] == 'Modelled effect')
    output = (template.replace('@@CSS@@\n', css)
              .replace('@@JS@@\n', js)
              .replace('@@ART@@', edition['art']() if edition.get('art') else '')
              .replace('@@CASES@@', '\n'.join(render_cards(campaigns, notes, edition['test_heading'], prefix, r['source_label'])))
              .replace('@@SCREENINGS@@', '\n'.join(render_screenings(campaigns, edition['screening'], prefix)))
              .replace('@@LADDER@@', '\n'.join(render_ladder(campaigns, notes, compare)))
              .replace('@@MECHANISMS@@', '\n'.join(render_mechanisms(campaigns, edition.get('mechanisms'))))
              .replace('@@TIMELINE@@', render_timeline(campaigns))
              .replace('@@FILTERS@@', render_filters(campaigns, r['roles'], r['role_label'], r['role_aria'], edition.get('mechanisms'), edition.get('mechanism_label', 'Mechanism')))
              .replace('@@MODELLED@@', str(modelled))
              .replace('@@COMPARE_MODELLED@@', str(compare_modelled))
              .replace('@@EDITION_NAV@@', render_edition_nav(edition))
              .replace('@@ROLE_GRID@@', render_role_grid(campaigns, r['roles'], r['role_aria']))
              .replace('@@SERIES_MODELLED@@', series_modelled(edition))
              .replace('@@ASSET_PREFIX@@', prefix)
              .replace('@@COUNT@@', str(len(campaigns)))
              .replace('@@FIRST_YEAR@@', str(min(c['year'] for c in campaigns)))
              .replace('@@LAST_YEAR@@', str(max(c['year'] for c in campaigns))))
    out = root.parent / edition['output']
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(output, encoding='utf-8')
    return out


# The series convention: number every edition with two digits and give it three things.
#   src/campaigns-NN.json      the cases
#   src/page-template-NN.html  the page copy
#   edition-NN/index.html      the published page (Edition 01 also sits on the home page)
# Add an entry below and run `python3 src/build.py`. The editions switcher in the menu updates itself.


# The Index joins the series once enough editions exist. Until then the menu shows editions only.
INDEX_OUTPUT = 'the-index/index.html'
INDEX_READY = False

# The series convention: number every edition with two digits and give it three things.
#   src/campaigns-NN.json      the cases
#   src/page-template-NN.html  the page copy
#   edition-NN/index.html      the published page (Edition 01 also sits on the home page)
EDITIONS = [
    {
        'number': '01',
        'name': 'Fame first',
        'data': 'campaigns-01.json',
        'template': 'page-template-01.html',
        'output': 'index.html',
        'alias': 'edition-01/index.html',
        'art': exchange_art,
        'test_heading': 'How the outcome was recorded',
        'mechanism_label': 'Exchange',
        'screening': (
            ('red-bull-gopro', 'GoPro tells the Stratos story from the cameras on Felix Baumgartner’s suit.', 'space'),
            ('lego-star-wars', 'LEGO looks back on 25 years of the licence it nearly turned down.', 'bricks'),
            ('bmw-films-the-hire', 'Wong Kar-wai’s film for the series, with Clive Owen as the Driver.', 'road'),
            ('taco-bell-doritos-locos', 'Taco Bell’s own telling of how two brands became one shell.', 'shell'),
        ),
    },
]

if __name__ == '__main__':
    import sys
    wanted = sys.argv[1:]
    for edition in EDITIONS:
        if wanted and edition['output'] not in wanted:
            continue
        if not (root / edition['data']).exists():
            continue
        print('Built', build(edition).relative_to(root.parent))
        forwarding = write_forwarding_page(edition)
        if forwarding:
            print('Built', forwarding.relative_to(root.parent), '(forwards to', edition['output'] + ')')
