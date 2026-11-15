"""Check generated navigation and local assets before publishing (standard library only)."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import hashlib
import json

ROOT = Path(__file__).resolve().parent.parent

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.refs = set(), []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        field = 'href' if tag in ('a', 'link') else 'src' if tag in ('img', 'script') else None
        if field and attrs.get(field):
            self.refs.append((tag, attrs[field]))


def main():
    errors, images, cases = [], set(), []
    pages = {p.resolve(): Page(p.read_text()) for p in ROOT.rglob('*.html') if 'src' not in p.relative_to(ROOT).parts}
    for page, parsed in pages.items():
        for tag, url in parsed.refs:
            parts = urlsplit(url)
            if parts.scheme or parts.netloc:
                continue
            target = (ROOT / unquote(parts.path.lstrip('/'))) if parts.path.startswith('/') else (page.parent / unquote(parts.path)).resolve()
            if target.is_dir():
                target /= 'index.html'
            if not target.is_file():
                errors.append(f'{page.relative_to(ROOT)}: missing {url}')
            elif parts.fragment and target in pages and unquote(parts.fragment) not in pages[target].ids:
                errors.append(f'{page.relative_to(ROOT)}: missing anchor {url}')
            if tag == 'img':
                images.add(target)
    for path in sorted((ROOT / 'src').glob('campaigns-*.json')):
        entries = json.loads(path.read_text())
        expected = 10 if path.stem.endswith('07') else 15
        if len(entries) != expected:
            errors.append(f'{path.name}: expected {expected} cases, got {len(entries)}')
        for case in entries:
            cases.append(case['id'])
            image = case.get('image')
            if not image or not image.get('alt'):
                errors.append(f'{case["id"]}: missing thumbnail or description')
            elif not (ROOT / urlsplit(image['src']).path).is_file():
                errors.append(f'{case["id"]}: missing thumbnail file')
            for field in ('impact_source', 'announcement'):
                if case.get(field) and urlsplit(case[field][1]).scheme not in ('http', 'https'):
                    errors.append(f'{case["id"]}: invalid {field} URL')
    if len(cases) != 100 or len(set(cases)) != 100:
        errors.append('Expected 100 uniquely identified cases')
    # Every generated case thumbnail must carry the current file fingerprint.
    for page, parsed in pages.items():
        for tag, url in parsed.refs:
            if tag == 'img' and '?v=' in url:
                parts = urlsplit(url)
                target = (page.parent / parts.path).resolve()
                if target.is_file():
                    expected = hashlib.sha256(target.read_bytes()).hexdigest()[:12]
                    if parts.query != 'v=' + expected:
                        errors.append(f'{page.relative_to(ROOT)}: stale thumbnail fingerprint {url}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(pages)} pages, 100 cases, {len(images)} local images; all internal links, anchors and thumbnail fingerprints valid.')

if __name__ == '__main__':
    main()
