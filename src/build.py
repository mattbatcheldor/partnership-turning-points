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


def contract_art():
    # Editorial illustration: a partnership agreement, signed by two parties and stamped with its measured return.
    serif = "'Source Serif 4', Georgia, serif"
    sans = "'Source Sans 3', Arial, sans-serif"
    lines = ''.join(f'<rect x="280" y="{190 + i * 22}" width="{360 - (i % 4) * 40}" height="7" fill="#DBE9E1"/>' for i in range(8))
    return f'''<svg viewBox="0 0 920 560" preserveAspectRatio="xMidYMid slice" role="img" aria-labelledby="art-title">
<title id="art-title">Illustration of a partnership agreement signed by two parties, with a large stamp across it reading 14.5 to 1, the measured return.</title>
<defs><filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#000" flood-opacity=".4"/></filter></defs>
<path d="M0 0h920v560H0z" fill="#172C2A"/>
<g transform="translate(46 20) scale(.9)"><g transform="rotate(-2 460 280)" filter="url(#sh)">
<rect x="240" y="50" width="440" height="470" fill="#F7F3EA"/>
<text x="280" y="104" font-family="{sans}" font-size="13" letter-spacing="3" fill="#075950">EDITION 02 / PROOF FIRST</text>
<text x="280" y="152" font-family="{serif}" font-size="34" fill="#172C2A">Partnership agreement</text>
{lines}
<line x1="280" y1="430" x2="440" y2="430" stroke="#172C2A" stroke-width="1.5"/>
<line x1="480" y1="430" x2="640" y2="430" stroke="#172C2A" stroke-width="1.5"/>
<path d="M290 420c18-26 30 10 46-6s22-22 34 2" fill="none" stroke="#075950" stroke-width="2.5"/>
<path d="M492 422c12-20 28-6 40-14s20 4 36-10" fill="none" stroke="#C97B60" stroke-width="2.5"/>
<text x="280" y="452" font-family="{sans}" font-size="12" letter-spacing="2" fill="#53584d">PARTNER A</text>
<text x="480" y="452" font-family="{sans}" font-size="12" letter-spacing="2" fill="#53584d">PARTNER B</text>
<g transform="rotate(-12 470 300)" opacity=".93">
<rect x="330" y="240" width="280" height="118" rx="10" fill="none" stroke="#075950" stroke-width="7"/>
<text x="470" y="312" text-anchor="middle" font-family="{serif}" font-size="56" font-weight="600" fill="#075950">14.5 : 1</text>
<text x="470" y="342" text-anchor="middle" font-family="{sans}" font-size="13" font-weight="700" letter-spacing="3" fill="#075950">MEASURED RETURN</text>
</g>
</g></g>
</svg>'''


def price_art():
    # Editorial illustration: a large price tag with a deal value filled in and the result line left blank.
    serif = "'Source Serif 4', Georgia, serif"
    sans = "'Source Sans 3', Arial, sans-serif"
    return f'''<svg viewBox="0 0 920 560" preserveAspectRatio="xMidYMid slice" role="img" aria-labelledby="art-title">
<title id="art-title">Illustration of a large price tag on a string. The deal value is filled in as twenty billion dollars, and the line for the result is left blank.</title>
<defs><filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#000" flood-opacity=".4"/></filter></defs>
<path d="M0 0h920v560H0z" fill="#172C2A"/>
<path d="M150 40c80 40 140 70 196 118" fill="none" stroke="#DBE9E1" stroke-width="3" stroke-dasharray="2 7"/>
<g transform="translate(40 18) scale(.92)"><g transform="rotate(-8 470 300)" filter="url(#sh)">
<path d="M300 150h400a18 18 0 0 1 18 18v264a18 18 0 0 1-18 18h-400l-110-150z" fill="#C97B60"/>
<circle cx="262" cy="300" r="16" fill="#172C2A"/>
<text x="330" y="208" font-family="{sans}" font-size="14" letter-spacing="3" fill="#172C2A">EDITION 03 / MONEY FIRST</text>
<text x="330" y="246" font-family="{sans}" font-size="15" font-weight="700" letter-spacing="2" fill="#F7F3EA">DEAL VALUE</text>
<text x="330" y="312" font-family="{serif}" font-size="54" font-weight="600" fill="#F7F3EA">$20,000,000,000</text>
<text x="330" y="378" font-family="{sans}" font-size="15" font-weight="700" letter-spacing="2" fill="#172C2A">RESULT</text>
<line x1="420" y1="380" x2="680" y2="380" stroke="#172C2A" stroke-width="2" stroke-dasharray="6 6"/>
<text x="330" y="418" font-family="{serif}" font-size="18" font-style="italic" fill="#172C2A">Not disclosed.</text>
</g></g>
</svg>'''


def record_art():
    # Editorial illustration: a record half out of its sleeve, side A for the brand and side B for the culture it partnered with.
    serif = "'Source Serif 4', Georgia, serif"
    sans = "'Source Sans 3', Arial, sans-serif"
    grooves = ''.join(f'<circle cx="680" cy="280" r="{r}" fill="none" stroke="#2b3a38" stroke-width="1.2"/>' for r in range(70, 200, 9))
    return f'''<svg viewBox="0 0 920 560" preserveAspectRatio="xMidYMid slice" role="img" aria-labelledby="art-title">
<title id="art-title">Illustration of a vinyl record sliding out of its sleeve. The label reads side A, the brand, and side B, the culture.</title>
<defs><filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#000" flood-opacity=".45"/></filter></defs>
<path d="M0 0h920v560H0z" fill="#172C2A"/>
<g filter="url(#sh)">
<circle cx="680" cy="280" r="205" fill="#0d1615"/>
{grooves}
<circle cx="680" cy="280" r="78" fill="#C97B60"/>
<circle cx="680" cy="280" r="6" fill="#0d1615"/>
<text x="680" y="270" text-anchor="middle" font-family="{sans}" font-size="12" font-weight="700" letter-spacing="1.5" fill="#172C2A">A · THE BRAND</text>
<text x="680" y="300" text-anchor="middle" font-family="{sans}" font-size="12" font-weight="700" letter-spacing="1.5" fill="#172C2A">B · THE CULTURE</text>
</g>
<g filter="url(#sh)">
<rect x="150" y="70" width="420" height="420" fill="#DBE9E1"/>
<rect x="150" y="70" width="420" height="420" fill="none" stroke="#F7F3EA" stroke-width="2" opacity=".6"/>
<text x="190" y="128" font-family="{sans}" font-size="14" letter-spacing="3" fill="#075950">EDITION 04</text>
<text x="190" y="214" font-family="{serif}" font-size="64" fill="#172C2A">Culture</text>
<text x="190" y="284" font-family="{serif}" font-size="64" font-style="italic" fill="#172C2A">first.</text>
<text x="190" y="446" font-family="{sans}" font-size="13" letter-spacing="2" fill="#075950">MUSIC · SPORT · ART · FASHION</text>
</g>
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
    ('Purpose for preference', 'A brand gives a cause money or a stage, and the cause gives people a reason to choose the brand.'),
    ('Network for network', 'Peers or rivals join up to offer customers something none could alone.'),
    ('Money for distribution', 'One side pays to be where customers start: the default, the shelf or the screen.'),
    ('Capital for capability', 'One side invests money or infrastructure, and the other brings a capability it could not build.'),
    ('Credibility for reach', 'A cultural figure lends authenticity, and a brand takes it to a mass audience.'),
]
ROLES = ['Co-branded product', 'Designer collaboration', 'Licence', 'Content partnership', 'Platform integration', 'Sponsorship and placement', 'Cause partnership', 'Alliance', 'Endorsement', 'Investment partnership', 'Artist collaboration']
# Every case is sorted by the type of partnership.
ROLE_DEFAULTS = {'roles': ROLES, 'role_label': 'Type', 'role_aria': 'Type of partnership', 'source_label': 'The partners'}
ERAS = ['1950s to 1980s', '1990s and 2000s', '2010s', '2020s']


def torn_art():
    # Editorial illustration: a partnership agreement torn in two, stamped as terminated.
    serif = "'Source Serif 4', Georgia, serif"
    sans = "'Source Sans 3', Arial, sans-serif"
    pts = [(450 + (12 if i % 2 else -10), 60 + i * 25) for i in range(21)]
    down = ' '.join(f'L{x} {y}' for x, y in pts)
    up = ' '.join(f'L{x} {y}' for x, y in reversed(pts))
    lines_l = ''.join(f'<rect x="220" y="{230 + i * 22}" width="{190 - (i % 3) * 30}" height="7" fill="#DBE9E1"/>' for i in range(6))
    lines_r = ''.join(f'<rect x="490" y="{230 + i * 22}" width="{170 - (i % 3) * 30}" height="7" fill="#DBE9E1"/>' for i in range(6))
    return f'''<svg viewBox="0 0 920 560" preserveAspectRatio="xMidYMid slice" role="img" aria-labelledby="art-title">
<title id="art-title">Illustration of a partnership agreement torn in two, with the halves pulling apart. A stamp across the tear reads terminated.</title>
<defs><filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#000" flood-opacity=".4"/></filter></defs>
<path d="M0 0h920v560H0z" fill="#172C2A"/>
<g transform="translate(60 30) scale(.86)">
<g transform="rotate(-5 320 300) translate(-26 8)" filter="url(#sh)">
<path d="M180 60 {down} L180 560Z" fill="#F7F3EA"/>
<text x="216" y="112" font-family="{sans}" font-size="13" letter-spacing="3" fill="#075950">EDITION 05 / FAILURE FIRST</text>
<text x="216" y="166" font-family="{serif}" font-size="34" fill="#172C2A">Partnership agr</text>
{lines_l}
<line x1="220" y1="440" x2="380" y2="440" stroke="#172C2A" stroke-width="1.5"/>
<text x="220" y="462" font-family="{sans}" font-size="12" letter-spacing="2" fill="#53584d">PARTNER A</text>
</g>
<g transform="rotate(4 600 300) translate(24 -6)" filter="url(#sh)">
<path d="M720 60 L720 560 {up}Z" fill="#F7F3EA"/>
<text x="466" y="166" font-family="{serif}" font-size="34" fill="#172C2A">eement</text>
{lines_r}
<line x1="500" y1="440" x2="660" y2="440" stroke="#172C2A" stroke-width="1.5"/>
<text x="500" y="462" font-family="{sans}" font-size="12" letter-spacing="2" fill="#53584d">PARTNER B</text>
</g>
<g transform="rotate(-10 460 300)" opacity=".94">
<rect x="290" y="258" width="340" height="88" rx="10" fill="none" stroke="#C97B60" stroke-width="7"/>
<text x="460" y="317" text-anchor="middle" font-family="{sans}" font-size="40" font-weight="700" letter-spacing="6" fill="#C97B60">TERMINATED</text>
</g>
</g>
</svg>'''


def screen_art():
    # Editorial illustration: a phone mid-livestream, with a brand pinned in the chat and hearts rising.
    serif = "'Source Serif 4', Georgia, serif"
    sans = "'Source Sans 3', Arial, sans-serif"
    hearts = ''.join(f'<path transform="translate({x} {y}) scale({s})" d="M0 6C0 2 3 0 6 0s6 3 6 6c0 6-12 12-12 12S-12 12-12 6c0-3 3-6 6-6s6 2 6 6z" fill="{c}" opacity="{o}"/>' for x, y, s, c, o in [(640, 380, 1.4, '#C97B60', 1), (668, 320, 1.1, '#DBE9E1', .85), (630, 262, .9, '#C97B60', .7), (676, 210, .8, '#DBE9E1', .55), (644, 160, .6, '#C97B60', .4)])
    return f'''<svg viewBox="0 0 920 560" preserveAspectRatio="xMidYMid slice" role="img" aria-labelledby="art-title">
<title id="art-title">Illustration of a phone showing a live stream. A live badge sits at the top, a brand message is pinned in the chat, and hearts float up the side of the screen.</title>
<defs><filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#000" flood-opacity=".45"/></filter></defs>
<path d="M0 0h920v560H0z" fill="#172C2A"/>
<g opacity=".16" fill="#DBE9E1">{''.join(f'<circle cx="{x}" cy="{y}" r="2"/>' for x in range(40, 920, 40) for y in range(40, 560, 40))}</g>
<g transform="rotate(-6 460 280)" filter="url(#sh)">
<rect x="330" y="36" width="260" height="488" rx="34" fill="#0d1615"/>
<rect x="344" y="52" width="232" height="456" rx="22" fill="#075950"/>
<rect x="420" y="62" width="80" height="14" rx="7" fill="#0d1615"/>
<rect x="362" y="96" width="62" height="26" rx="4" fill="#C97B60"/>
<text x="393" y="114" text-anchor="middle" font-family="{sans}" font-size="13" font-weight="700" letter-spacing="2" fill="#F7F3EA">LIVE</text>
<text x="436" y="114" font-family="{sans}" font-size="13" fill="#DBE9E1">2.4m watching</text>
<text x="368" y="210" font-family="{sans}" font-size="13" letter-spacing="3" fill="#DBE9E1">EDITION 06</text>
<text x="368" y="262" font-family="{serif}" font-size="46" fill="#F7F3EA">Platform</text>
<text x="368" y="312" font-family="{serif}" font-size="46" font-style="italic" fill="#F7F3EA">first.</text>
<rect x="362" y="400" width="196" height="54" rx="10" fill="#F7F3EA"/>
<text x="376" y="422" font-family="{sans}" font-size="11" font-weight="700" letter-spacing="1.5" fill="#075950">PINNED · PARTNER</text>
<text x="376" y="442" font-family="{sans}" font-size="13" fill="#172C2A">Use my code at checkout</text>
<rect x="362" y="466" width="196" height="26" rx="13" fill="none" stroke="#DBE9E1" stroke-width="1.5"/>
<text x="378" y="484" font-family="{sans}" font-size="12" fill="#DBE9E1">Say something…</text>
</g>
{hearts}
</svg>'''

def edge_art():
    # Editorial illustration: a large faded circle for the centre of the market, with ten bright points on its edge.
    import math
    serif = "'Source Serif 4', Georgia, serif"
    sans = "'Source Sans 3', Arial, sans-serif"
    cx, cy, r = 470, 290, 200
    colours = ['#C97B60', '#DBE9E1', '#ffcf5a', '#F7F3EA', '#C97B60', '#DBE9E1', '#ffcf5a', '#F7F3EA', '#C97B60', '#DBE9E1']
    dots = ''.join(f'<circle cx="{cx + r * math.cos(math.radians(i * 36 - 90)):.1f}" cy="{cy + r * math.sin(math.radians(i * 36 - 90)):.1f}" r="15" fill="{colours[i]}"/>' for i in range(10))
    return f'''<svg viewBox="0 0 920 560" preserveAspectRatio="xMidYMid slice" role="img" aria-labelledby="art-title">
<title id="art-title">Illustration of a large faded circle standing for the centre of the market, with ten bright points spaced around its edge and the number 100 in the middle.</title>
<path d="M0 0h920v560H0z" fill="#172C2A"/>
<circle cx="{cx}" cy="{cy}" r="{r}" fill="#075950" opacity=".35"/>
<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#DBE9E1" stroke-width="2" stroke-dasharray="3 9"/>
<circle cx="{cx}" cy="{cy}" r="{r - 70}" fill="none" stroke="#DBE9E1" stroke-width="1" opacity=".3"/>
{dots}
<text x="{cx}" y="{cy - 46}" text-anchor="middle" font-family="{sans}" font-size="13" letter-spacing="3" fill="#DBE9E1">EDITION 07 / EDGE FIRST</text>
<text x="{cx}" y="{cy + 40}" text-anchor="middle" font-family="{serif}" font-size="104" fill="#F7F3EA">100</text>
<text x="{cx}" y="{cy + 76}" text-anchor="middle" font-family="{serif}" font-size="20" font-style="italic" fill="#DBE9E1">Ten from the edge.</text>
</svg>'''

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
        title = creative.get('screening_title', c['title'])
        url = creative.get('screening_url', creative['url'])
        video = url.partition('https://www.youtube.com/watch?v=')[2]
        player = ''
        if video:
            player = f'<button class="play-film small" type="button" data-video="{e(video)}" data-title="{e(title)}" hidden>Play here</button>'
        frame = campaign_image(c, 'film-frame', prefix) or f'<span class="film-frame drawn {drawn}" aria-hidden="true"></span>'
        screenings.append(f'''<article class="screening">
{frame}
<div class="film-body">
<div class="film-heading"><p class="small">{e(c['brand'])} / {c['year']}</p><h3>{e(title)}</h3></div>
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
<title>Partnership Turning Points | Edition {edition["number"]}{", " + edition["name"] if edition.get("name") else ""}</title>
<link rel="canonical" href="{target}">
<meta http-equiv="refresh" content="0; url={target}">
<meta name="robots" content="noindex">
</head>
<body>
<p><a href="{target}">Open Partnership Turning Points, Edition {edition["number"]}</a></p>
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


# The Index joins the series once all the editions exist. It reads every case file and is built after them.
INDEX_OUTPUT = 'the-index/index.html'
INDEX_READY = True

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
            ('lego-star-wars', 'LEGO’s 25th anniversary short shows what the licence made possible.', 'bricks'),
            ('bmw-films-the-hire', 'Wong Kar-wai’s film for the series, with Clive Owen as the Driver.', 'road'),
            ('taco-bell-doritos-locos', 'Taco Bell’s own telling of how two brands became one shell.', 'shell'),
        ),
    },
    {
        'number': '02',
        'name': 'Proof first',
        'data': 'campaigns-02.json',
        'template': 'page-template-02.html',
        'output': 'edition-02/index.html',
        'asset_prefix': '../',
        'art': contract_art,
        'test_heading': 'How the outcome was measured',
        'mechanism_label': 'Exchange',
        'level_notes': {
            'Modelled effect': 'A model or a comparison with markets that didn’t take part estimates the effect against a baseline.',
            'Sales trend': 'Sales, donations or outcomes moved, but other causes are not separated out.',
            'Survey': 'Tracking or research showed people’s views or interest changed.',
        },
        'screening': (
            ('heineken-champions-league', 'Heineken turns watching a Champions League match into a chance to share the sofa with a football legend.', 'sofa'),
            ('mcdonalds-london-2012', 'Leo Burnett’s campaign film puts the spectators, volunteers and families of London 2012 centre stage.', 'torch'),
            ('tourism-ireland-game-of-thrones', 'Discover Ireland shows how scenes from the series became a tapestry that fans could see in person.', 'tapestry'),
            ('gillette-movember', 'In a later Gillette UK film for Movember, Aaron Ramsdale and Ian Wright talk about having a mate to lean on.', 'mo'),
        ),
    },
    {
        'number': '03',
        'name': 'Money first',
        'data': 'campaigns-03.json',
        'template': 'page-template-03.html',
        'output': 'edition-03/index.html',
        'asset_prefix': '../',
        'art': price_art,
        'test_heading': 'How the outcome was recorded',
        'mechanism_label': 'Exchange',
        'level_notes': {
            'Sales trend': 'Sales, revenue or company value moved, but other causes are not separated out.',
            'Archival': 'The record shows the price and the terms, not what the money achieved.',
        },
        'screening': (
            ('nike-michael-jordan', 'Jordan Brand’s own history of the first shoe. Notice how much of the story is about the people who wore it.', 'court'),
            ('emirates-arsenal', 'Arsenal’s film for the renewal. A sponsor that has stayed this long is its own kind of evidence.', 'stadium'),
            ('oracle-red-bull-racing', 'Oracle’s launch film for the car carrying its name. Watch how the sponsor presents itself as a technology partner.', 'car'),
            ('amazon-nfl', 'Prime Video’s opening film for its first season. The price bought a new kind of football broadcast.', 'field'),
        ),
    },
    {
        'number': '04',
        'name': 'Culture first',
        'data': 'campaigns-04.json',
        'template': 'page-template-04.html',
        'output': 'edition-04/index.html',
        'asset_prefix': '../',
        'art': record_art,
        'test_heading': 'How the outcome was recorded',
        'mechanism_label': 'Exchange',
        'level_notes': {
            'Sales trend': 'Sales, share or donations moved, but other causes are not separated out.',
            'Archival': 'The record shows the partnership and how long it lasted, not what it earned.',
        },
        'screening': (
            ('run-dmc-adidas', 'The song that started it, from Run-DMC’s own channel. Listen for the brand name in the chorus.', 'vinyl'),
            ('absolut-warhol', 'Absolut tells the story from Warhol’s first painting in 1985 to today.', 'bottle'),
            ('adidas-stella-mccartney', 'A campaign film from the partnership’s second decade. Notice whose name comes first.', 'gym'),
            ('coca-cola-olympics', 'Coca-Cola’s archivists on ninety years of the Olympic partnership.', 'rings'),
        ),
    },
    {
        'number': '05', 'name': 'Failure first', 'data': 'campaigns-05.json', 'template': 'page-template-05.html',
        'output': 'edition-05/index.html', 'asset_prefix': '../', 'art': torn_art, 'test_heading': 'How the damage was recorded',
        'mechanism_label': 'Exchange',
        'level_notes': {
            'Modelled effect': 'Economists compared the sponsors’ share prices with the market and their rivals.',
            'Sales trend': 'Revenue or share price moved, but other causes are not separated out.',
            'Reach only': 'The record shows how many people it reached, not what it cost or earned.',
            'Archival': 'The record shows how the partnership ended, not what it cost.',
        },
        'screening': (
            ('pepsi-madonna', 'The advert Pepsi pulled in 1989, from Pepsi’s own channel. It finally ran again in 2023.', 'candle'),
            ('apple-u2-songs-of-innocence', 'Apple’s 2014 launch event, from Apple’s channel. U2 appear near the end, just before the album landed in every library.', 'stage'),
            ('lego-shell', 'Not a partner’s film, but the one that ended a partnership, from Greenpeace’s channel.', 'brick'),
        ),
    },
    {
        'number': '06', 'name': 'Platform first', 'data': 'campaigns-06.json', 'template': 'page-template-06.html',
        'output': 'edition-06/index.html', 'asset_prefix': '../', 'art': screen_art, 'test_heading': 'How the outcome was recorded',
        'mechanism_label': 'Exchange',
        'level_notes': {
            'Sales trend': 'Sales, downloads or revenue moved, but other causes are not separated out.',
            'Reach only': 'Views or streams show attention, not what it did for the brand.',
            'Archival': 'The record shows the partnership happened, not what it earned.',
        },
        'screening': (
            ('nike-casey-neistat', 'The film Neistat made instead of the advert, from his own channel. Count how often the product appears.', 'globe'),
            ('fortnite-avengers', 'Epic’s trailer for the Thanos mode, from Fortnite’s channel. The film is advertised by being played.', 'gauntlet'),
            ('lil-nas-x-roblox', 'The whole concert, from Lil Nas X’s channel. Notice the audience is never shown, because it was inside the game.', 'concert'),
            ('ocean-spray-nathan-apodaca', 'Ocean Spray’s thank you, from its own channel. The brand arrives after the culture, not before.', 'truck'),
        ),
    },
    {
        'number': '07', 'name': 'Edge first', 'data': 'campaigns-07.json', 'template': 'page-template-07.html',
        'output': 'edition-07/index.html', 'asset_prefix': '../', 'art': edge_art, 'test_heading': 'How the outcome was recorded',
        'mechanism_label': 'Exchange',
        'level_notes': {
            'Modelled effect': 'Economists compared households by how close they were to the service.',
            'Sales trend': 'Sales or donations moved, but other causes are not separated out.',
            'Reach only': 'Views show attention, not what it did for the brand.',
            'Archival': 'The record shows the partnership happened, not what it earned.',
        },
        'screening': (
            ('coke-studio-pakistan', 'The song that went round the world, from Coke Studio Pakistan’s channel. Notice how little of it is about the drink.', 'mic'),
            ('innocent-age-uk', 'innocent on its Big Knit, from its own channel. Watch who does the work.', 'hat'),
            ('liquid-death-tony-hawk', 'Liquid Death’s film, from its own channel. A small brand making fun of how big brands do celebrity deals.', 'deck'),
            ('corona-parley', 'Corona and Parley on their island promise, from Corona’s channel.', 'wave'),
        ),
    },
]

# The Index: one page that reads the whole series, built from the same case files as the editions.
REGIONS = [
    ('UK and Ireland', ('United Kingdom', 'England', 'Northern Ireland', 'Scotland', 'London', 'Manchester', 'Birmingham')),
    ('North America', ('United States', 'New York', 'Vermont', 'Idaho', 'Miami')),
    ('Europe', ('Europe', 'Paris', 'Barcelona', 'Amsterdam', 'Netherlands', 'Zurich', 'Champions League')),
    ('Asia', ('Japan', 'Tokyo', 'China', 'South Korea', 'Taiwan', 'Pakistan')),
    ('Latin America', ('Brazil', 'Mexico')),
    ('Africa', ('Kenya',)),
]
INDUSTRIES = [
    ('Sport', ('sport', 'football', 'basketball', 'golf', 'cycling', 'swimming', 'rugby', 'olympic', 'skateboarding', 'formula', 'fitness', 'sportswear')),
    ('Music', ('music', 'hip-hop', 'rock', 'pop', 'k-pop', 'festivals')),
    ('Fashion', ('fashion', 'sportswear', 'footwear', 'luxury', 'watches', 'beauty', 'streetwear', 'clothing')),
    ('Food and drink', ('food', 'drinks', 'coffee', 'beer', 'spirits', 'ice cream', 'chocolate', 'juice', 'smoothies', 'cereal', 'water', 'snacks', 'supermarkets')),
    ('Technology', ('technology', 'smartphones', 'mobile', 'payments', 'streaming', 'artificial intelligence', 'software', 'cloud', 'search', 'networks', 'money', 'cryptocurrency', 'cameras', 'ride-hailing')),
    ('Gaming', ('gaming',)),
    ('Media', ('film', 'television', 'publishing', 'youtube', 'tiktok', 'broadcasting', 'podcasts', 'entertainment', 'animation')),
    ('Art', ('art', 'toys', 'character licensing')),
    ('Retail', ('retail', 'diy', 'furniture')),
    ('Travel', ('airlines', 'car rental', 'tourism')),
    ('Causes', ('charity', 'conservation', 'health')),
    ('Energy', ('oil',)),
]
EVIDENCE_COLOURS = {'Modelled effect': '#557400', 'Sales trend': '#7c9a1e', 'Survey': '#a5c31c', 'Reach only': '#d3d1c5', 'Archival': '#a8aa9d'}
LESSONS = [
    ('Back what’s already there.',
     'The partnerships people loved most often began before the contract. The partner already wore, drank or played the product, so nobody had to pretend.',
     [('04', 'run-dmc-adidas'), ('04', 'ben-jerrys-phish'), ('04', 'swatch-keith-haring'), ('06', 'dunkin-charli-damelio'), ('06', 'ocean-spray-nathan-apodaca')]),
    ('Bring something the other side can’t make.',
     'Talent for scale is the second most common exchange, in {talent} of the {total} cases. The strongest pair a capability with a reach that neither side could build alone.',
     [('01', 'hm-karl-lagerfeld'), ('01', 'lego-star-wars'), ('03', 'disney-pixar'), ('04', 'louis-vuitton-murakami'), ('07', 'm-pesa')]),
    ('Sponsorship can be proved, and it can break.',
     'Money for association is the most common exchange, in {money} cases. It holds {money_mod} of the {modelled} modelled effects, and nine of the fifteen failures in Edition 05. Paying to stand next to someone is the easiest deal to measure and the hardest to undo.',
     [('02', 'o2-the-o2'), ('02', 'heineken-champions-league'), ('04', 'coca-cola-olympics'), ('05', 'hertz-oj-simpson'), ('05', 'tiger-woods-sponsors')]),
    ('A price is not a result.',
     '{deals} cases carry a deal value, flagged so it isn’t read as an outcome. The biggest sums, from Google’s payments to Apple to Microsoft’s bet on OpenAI, came with the least public evidence of what they bought.',
     [('03', 'google-apple'), ('03', 'microsoft-openai'), ('03', 'spotify-joe-rogan'), ('05', 'ftx-sports'), ('06', 'ninja-mixer')]),
    ('Go where the audience already is.',
     'From Big Brother to Roblox, the partnerships that reached people met them somewhere they already spent their time. The ones that tried to move an audience, like Mixer, struggled.',
     [('02', 'bt-cellnet-big-brother'), ('01', 'fortnite-travis-scott'), ('06', 'pokemon-go-mcdonalds-japan'), ('06', 'lil-nas-x-roblox'), ('07', 'mcdonalds-bts')]),
    ('Decide how it ends before you start.',
     'The deals that ended in court or in a warehouse rarely agreed in advance how decisions were made, or what would happen if a partner fell. Fred Perry shows the other way: it let the partner’s family decide.',
     [('05', 'mastercard-fifa'), ('05', 'yeezy-gap'), ('05', 'adidas-kanye-west'), ('06', 'mrbeast-burger'), ('04', 'fred-perry-amy-winehouse')]),
]
PARTY_GROUPS = {'Apple Music': 'Apple', 'McDonald’s Japan': 'McDonald’s'}
PARTY_SKIP = {'his sponsors', 'sport', 'its first creators'}
PARTY_NOTES = {
    'Apple': 'A running sensor with Nike, a search deal worth billions, two U2 releases and an open letter from Taylor Swift. Partner, payer and the one being told what to do.',
    'Nike': 'Jordan and Ronaldo, a sensor with Apple, Virgil Abloh’s Ten and a filmmaker who spent the budget. Nike keeps backing people over products.',
    'McDonald’s': 'An Olympic sponsor, a Pokémon gym and two famous orders. The menu became the partnership.',
    'Coca-Cola': 'Nearly a century at the Olympics, its own mistake revived by Netflix, and Pakistan’s biggest music show.',
    'Adidas': 'The fans who signed Run-DMC, twenty years with Stella McCartney, and the cost of Yeezy.',
    'Pepsi': 'Michael Jackson set the price of fame. Madonna showed what it could cost.',
    'U2': 'The same partners ten years apart. People chose the U2 iPod and resented the free album.',
    'Michael Jordan': 'A brand built with Nike, and an advert people remember better than its sales.',
    'Mastercard': 'A measured Rugby World Cup, and a football World Cup lost to a rival.',
    'FIFA': 'One sponsorship, two card companies and a court case. Visa kept it, Mastercard was paid to go.',
    'Heineken': 'A Bond film placement, and a Champions League deal with a published return.',
    'Louis Vuitton': 'Murakami’s colours in 2003 and Supreme’s logo in 2017. A house that keeps letting outsiders in.',
    'Spotify': 'A playlist in an Uber, a stadium name and a podcast host.',
    'LEGO': 'Star Wars helped save it. Shell became a partner it had to end.',
    'Uniqlo': 'Jil Sander’s minimalism and KAWS’ crowds. Designer names at a mass price.',
    'Fortnite': 'Travis Scott’s concert and Thanos’ gauntlet. A game that became a stage.',
    'Gucci': 'The North Face in shops, a garden in Roblox.',
    'Ben & Jerry’s': 'A Vermont band’s flavour, and a Dutch chocolate maker’s rules.',
}
NUMBER_WORDS = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 100: 'A hundred'}


def region_of(place):
    head = place.split(',')[0]
    if head.strip().lower().startswith(('global', 'online')) and 'United States' not in place:
        return 'Global'
    hits = [(place.find(k), name) for name, keys in REGIONS for k in keys if k in place]
    return min(hits)[1] if hits else 'Global'


def industries_of(sector):
    s = sector.lower()
    words = set(re.findall(r"[a-z\-]+", s))
    return [name for name, keys in INDUSTRIES if any((k in s) if ' ' in k else (k in words) for k in keys)] or ['Other']


def decade_of(year):
    return f'{year // 10 * 10}s'


def load_series():
    series = []
    for edition in EDITIONS:
        if not (root / edition['data']).exists():
            continue
        campaigns = json.loads((root / edition['data']).read_text(encoding='utf-8'))
        template = (root / edition['template']).read_text(encoding='utf-8')
        finding = re.search(r'<h2 id="finding-title">(.*?)</h2>', template)
        series.append({'edition': edition, 'campaigns': campaigns, 'finding': finding.group(1) if finding else ''})
    return series


def case_href(edition, case_id):
    return f'{relative_dir(INDEX_OUTPUT, edition["output"]) or "./"}#{case_id}'


def build_index():
    series = load_series()
    by_number = {s['edition']['number']: s for s in series}
    everything = [(s['edition'], c) for s in series for c in s['campaigns']]
    total = len(everything)
    modelled = sum(1 for _, c in everything if c['evidence_level'] == 'Modelled effect')
    years = [c['year'] for _, c in everything]
    regions = collections.Counter(region_of(c['place']) for _, c in everything)
    decades = collections.Counter(decade_of(c['year']) for _, c in everything)
    levels = collections.Counter(c['evidence_level'] for _, c in everything)
    mechs = collections.Counter(c['mechanism'] for _, c in everything)
    roles = collections.Counter(c['data_role'] for _, c in everything)
    inds = collections.Counter(i for _, c in everything for i in industries_of(c['sector']))
    deals = sum(1 for _, c in everything if c.get('deal_value'))
    money_mod = sum(1 for _, c in everything if c['mechanism'] == 'Money for association' and c['evidence_level'] == 'Modelled effect')
    e02_mod = sum(1 for c in by_number['02']['campaigns'] if c['evidence_level'] == 'Modelled effect') if '02' in by_number else 0

    cards = []
    for s in series:
        ed, cs = s['edition'], s['campaigns']
        n_mod = sum(1 for c in cs if c['evidence_level'] == 'Modelled effect')
        href = relative_dir(INDEX_OUTPUT, ed['output']) or './'
        cards.append(f'<a class="ed-card" href="{href}"><span class="ed-num">{ed["number"]}</span><span class="ed-name">{e(ed["name"])}</span>'
                     f'<span class="ed-finding">{e(s["finding"])}</span><span class="ed-meta small">{len(cs)} cases · {min(c["year"] for c in cs)} to {max(c["year"] for c in cs)} · {n_mod or "no"} modelled</span></a>')

    rows = []
    for s in series:
        ed, cs = s['edition'], s['campaigns']
        segs = []
        for level in LEVELS:
            n = sum(1 for c in cs if c['evidence_level'] == level)
            if n:
                dark = level in ('Modelled effect', 'Sales trend')
                segs.append(f'<span class="ev-seg{" dark" if dark else ""}" style="--n:{n};background:{EVIDENCE_COLOURS[level]}" title="{e(level)}: {n}">{n}<span class="sr"> {e(level)}</span></span>')
        rows.append(f'<div class="ev-row"><span class="ev-label"><a href="{relative_dir(INDEX_OUTPUT, ed["output"]) or "./"}">Edition {ed["number"]}</a> <span>{e(ed["name"])}</span></span><span class="ev-bar">{"".join(segs)}</span></div>')
    legend = ''.join(f'<span><i style="background:{EVIDENCE_COLOURS[l]}"></i>{e(l)} <b>{levels[l]}</b></span>' for l in LEVELS)

    lessons = []
    for i, (title, text, refs) in enumerate(LESSONS, 1):
        chip_html = []
        for num, cid in refs:
            s = by_number[num]
            c = next(c for c in s['campaigns'] if c['id'] == cid)
            chip_html.append(f'<a class="lesson-chip" href="{case_href(s["edition"], cid)}"><span class="small">{num}</span> {e(c["brand"])}</a>')
        text = text.format(total=total, talent=mechs['Talent for scale'], money=mechs['Money for association'],
                           money_mod=money_mod, modelled=modelled, deals=NUMBER_WORDS.get(deals, str(deals)) if deals <= 10 else deals)
        lessons.append(f'<article class="lesson"><p class="lesson-num small">{i:02d}</p><h3>{e(title)}</h3><p>{e(text)}</p><div class="lesson-chips">{"".join(chip_html)}</div></article>')

    groups = collections.defaultdict(list)
    for ed, c in everything:
        for party in c['brand'].split(' × '):
            party = PARTY_GROUPS.get(party.strip(), party.strip())
            if party not in PARTY_SKIP:
                groups[party].append((ed, c))
    recurring = sorted(((p, v) for p, v in groups.items() if len({ed['number'] for ed, _ in v}) > 1),
                       key=lambda pv: (-len({ed['number'] for ed, _ in pv[1]}), -len(pv[1]), pv[0]))
    missing = [p for p, _ in recurring if p not in PARTY_NOTES]
    assert not missing, f'Add a note for these partners: {missing}'
    partners = []
    for p, v in recurring:
        items = ''.join(f'<li><a href="{case_href(ed, c["id"])}"><span class="small">Edition {ed["number"]}</span> {e(c["brand"])} <span class="yr">{c["year"]}</span></a></li>'
                        for ed, c in sorted(v, key=lambda x: x[1]['year']))
        partners.append(f'<article class="brand-row"><div><h3>{e(p)}</h3><p>{e(PARTY_NOTES[p])}</p></div><ol>{items}</ol></article>')

    region_order = [r for r, _ in REGIONS] + ['Global']
    filt = {
        'edition': ('Edition', [s['edition']['number'] for s in series]),
        'role': ('Type', [r for r in ROLES if roles[r]]),
        'industry': ('Industry', [i for i, _ in INDUSTRIES if inds[i]] + (['Other'] if inds['Other'] else [])),
        'region': ('Where', [r for r in region_order if regions[r]]),
        'evidence': ('Evidence', [l for l in LEVELS if levels[l]]),
    }
    filters = ''.join(f'<div class="filter-row" role="group" aria-label="{label}"><span class="small">{label}</span>{chips(g, vals)}</div>' for g, (label, vals) in filt.items())
    lines = []
    for ed, c in sorted(everything, key=lambda x: (x[1]['year'], x[1]['brand'])):
        thumbnail = campaign_image(c, 'ix-thumbnail', '../')
        video_url = c['creative'].get('url')
        watch = (f'<a class="ix-watch" href="{e(video_url)}" aria-label="Watch video for {e(c["brand"])}">Watch <span aria-hidden="true">↗</span></a>'
                 if video_url else '')
        lines.append(f'<li class="ix-case" data-edition="{ed["number"]}" data-role="{e(c["data_role"])}" data-industry="{e("|".join(industries_of(c["sector"])))}" data-region="{e(region_of(c["place"]))}" data-evidence="{e(c["evidence_level"])}">'
                     f'<a class="ix-case-link" href="{case_href(ed, c["id"])}"><span class="ix-visual">{thumbnail}<span class="ix-year">{c["year"]}</span></span><span class="ix-main"><span class="ix-brand small">{e(c["brand"])} · {e(c["mechanism"])}</span>'
                     f'<span class="ix-title">{e(c["title"])}</span><span class="ix-place">{e(c["place"])} · {e(c["data_role"])}</span></span>'
                     f'<span class="ix-side"><span class="ix-ed">Edition {ed["number"]}, {e(ed["name"])}</span>{meter(c["evidence_level"])}</span></a>{watch}</li>')

    share = lambda n: f'{round(n / total * 100)}%'
    uk, na = regions['UK and Ireland'], regions['North America']
    recent = sum(n for d, n in decades.items() if int(d[:4]) >= 2010)
    early = sum(n for d, n in decades.items() if int(d[:4]) < 1990)
    early_text = f'Only {NUMBER_WORDS.get(early, early).lower()} {"comes" if early == 1 else "come"} from before 1990'
    gaps = [
        ('Where the deals were made', f'{uk} cases, {share(uk)}, started in the UK or Ireland, {na}, {share(na)}, in North America and {regions["Global"]} were global from the start. '
                                     f'Europe has {regions["Europe"]}, Asia {regions["Asia"]}, Latin America {regions["Latin America"]} and Africa {regions["Africa"]}.'),
        ('When', f'{recent} of the {total} cases, {share(recent)}, date from 2010 or later. {early_text}, because older deals rarely left a public record of what each side gained.'),
        ('What the proof looks like', f'{modelled} of {total} cases have a modelled effect, and {e02_mod} of those are in Edition 02. {levels["Sales trend"]} show a sales trend, {levels["Archival"]} are archival only, and survey evidence is the rarest, with {levels["Survey"]}.'),
        ('Whose side the evidence is on', 'Most outcome figures describe one partner, usually the bigger brand. Few cases show what both sides gained, and the smaller partner’s result is the hardest to find.'),
    ]
    gap_html = ''.join(f'<div><h3>{e(t)}</h3><p>{e(x)}</p></div>' for t, x in gaps)
    reads = ', '.join(f'<a href="{relative_dir(INDEX_OUTPUT, s["edition"]["output"]) or "./"}">Edition {s["edition"]["number"]}, {e(s["edition"]["name"])}</a>' for s in series)

    template = (root / 'page-template-index.html').read_text(encoding='utf-8')
    css = (root / 'site.css').read_text(encoding='utf-8')
    output = (template.replace('@@CSS@@\n', css)
              .replace('@@EDITION_NAV@@', render_edition_nav(None))
              .replace('@@EDITION_COUNT@@', str(len(series)))
              .replace('@@EDITION_WORD@@', NUMBER_WORDS.get(len(series), str(len(series))))
              .replace('@@TOTAL_WORD@@', NUMBER_WORDS.get(total, str(total)))
              .replace('@@TOTAL@@', str(total))
              .replace('@@MODELLED@@', str(modelled))
              .replace('@@E02_MODELLED_WORD@@', NUMBER_WORDS.get(e02_mod, str(e02_mod)))
              .replace('@@DEALS@@', str(deals))
              .replace('@@FIRST_YEAR@@', str(min(years)))
              .replace('@@LAST_YEAR@@', str(max(years)))
              .replace('@@EDITION_CARDS@@', '\n'.join(cards))
              .replace('@@EVIDENCE_ROWS@@', '\n'.join(rows))
              .replace('@@EVIDENCE_LEGEND@@', legend)
              .replace('@@LESSONS@@', '\n'.join(lessons))
              .replace('@@PARTNER_COUNT@@', str(len(recurring)))
              .replace('@@PARTNERS@@', '\n'.join(partners))
              .replace('@@FILTERS@@', filters)
              .replace('@@CASES@@', '\n'.join(lines))
              .replace('@@GAPS@@', gap_html)
              .replace('@@READS@@', reads))
    assert '@@' not in output, re.findall(r'@@\w+@@', output)
    out = root.parent / INDEX_OUTPUT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(output, encoding='utf-8')
    return out

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
    if not wanted or INDEX_OUTPUT in wanted:
        print('Built', build_index().relative_to(root.parent))
