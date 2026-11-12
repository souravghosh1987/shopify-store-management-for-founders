#!/usr/bin/env python3
"""Offline structural checks; not a security audit or a full YAML/schema engine."""
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

EXPECTED_SKILLS = {
    'store-operating-baseline', 'merchandising-governance', 'product-page-parity',
    'media-library-discipline', 'offer-governance', 'store-reporting-rhythm',
    'controlled-change-handoff', 'founder-operating-sops',
}
MANIFEST_FIELDS = {'$schema', 'name', 'version', 'description', 'author', 'homepage',
                   'repository', 'license', 'keywords', 'extensions'}
SCHEMA = 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'
NAME = re.compile(r'^(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]{0,62}[a-z0-9])?$')
SKILL_NAME = re.compile(r'^(?!.*--)[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$')


def plain_frontmatter(text):
    """Parse this package's intentionally simple scalar frontmatter subset."""
    lines = text.splitlines()
    if not lines or lines[0] != '---':
        raise ValueError('missing opening frontmatter delimiter')
    try:
        end = lines.index('---', 1)
    except ValueError:
        raise ValueError('missing closing frontmatter delimiter') from None
    fields = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        match = re.fullmatch(r'([a-z][a-z-]*):\s*(.+)', line)
        if not match:
            raise ValueError('use one-line scalar frontmatter values')
        key, value = match.groups()
        if key in fields:
            raise ValueError('duplicate frontmatter key: ' + key)
        if value.startswith('"'):
            value = json.loads(value)
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1].replace("''", "'")
        elif value in {'|', '>', '|-', '>-'}:
            raise ValueError('use one-line scalar frontmatter values')
        fields[key] = value
    return fields


def validate(root):
    root = Path(root).absolute()
    errors = []
    if root.is_symlink() or any(p.is_symlink() for p in root.parents):
        return ['package path must not contain symlinks']
    if not root.is_dir():
        return ['package root does not exist']
    files = []
    for p in root.rglob('*'):
        if p.is_symlink():
            errors.append(f'symlink forbidden: {p.relative_to(root)}')
        elif p.is_file():
            files.append(p)
    for required in ('plugin.json', 'README.md', 'CHANGELOG.md', 'LICENSE'):
        if not (root / required).is_file():
            errors.append('missing required file: ' + required)
    try:
        manifest = json.loads((root / 'plugin.json').read_text(encoding='utf-8'))
        if not isinstance(manifest, dict):
            raise ValueError('manifest must be an object')
        if set(manifest) - MANIFEST_FIELDS:
            errors.append('unknown manifest fields: ' + ', '.join(sorted(set(manifest) - MANIFEST_FIELDS)))
        if manifest.get('$schema') != SCHEMA:
            errors.append('incorrect manifest schema identifier')
        if not isinstance(manifest.get('name'), str) or not NAME.fullmatch(manifest['name']):
            errors.append('invalid manifest name')
        for key in ('version', 'description', 'homepage', 'repository', 'license'):
            if key in manifest and not isinstance(manifest[key], str):
                errors.append(f'manifest {key} must be a string')
        if 'author' in manifest:
            author = manifest['author']
            if not isinstance(author, dict) or set(author) - {'name', 'email', 'url'} or any(not isinstance(v, str) for v in author.values()):
                errors.append('invalid manifest author')
        if 'keywords' in manifest and (not isinstance(manifest['keywords'], list) or any(not isinstance(x, str) for x in manifest['keywords'])):
            errors.append('manifest keywords must be strings')
        if 'extensions' in manifest and (not isinstance(manifest['extensions'], dict) or any(not isinstance(v, dict) for v in manifest['extensions'].values())):
            errors.append('manifest extensions must contain objects')
    except (OSError, ValueError, TypeError) as exc:
        errors.append('cannot read manifest: ' + str(exc))
    skill_root = root / 'skills'
    names = {p.name for p in skill_root.iterdir() if p.is_dir()} if skill_root.is_dir() else set()
    if names != EXPECTED_SKILLS:
        errors.append(f'skill set mismatch: missing={sorted(EXPECTED_SKILLS - names)}, extra={sorted(names - EXPECTED_SKILLS)}')
    for name in sorted(names):
        path = skill_root / name / 'SKILL.md'
        try:
            text = path.read_text(encoding='utf-8')
            fields = plain_frontmatter(text)
            if fields.get('name') != name or not SKILL_NAME.fullmatch(name):
                errors.append(f'{name}: invalid or mismatched skill name')
            description = fields.get('description')
            if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
                errors.append(f'{name}: invalid description')
            if len(text.splitlines()) >= 500:
                errors.append(f'{name}: package policy requires fewer than 500 lines')
        except (OSError, ValueError, TypeError) as exc:
            errors.append(f'{name}: {exc}')
    # Inline links only: intentionally not an HTTP availability or anchor checker.
    for path in files:
        if path.suffix.lower() != '.md':
            continue
        text = path.read_text(encoding='utf-8')
        for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text):
            target = target.strip().strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            dest = (path.parent / unquote(parsed.path)).resolve()
            if not dest.is_relative_to(root.resolve()):
                errors.append(f'{path.relative_to(root)}: link escapes package: {target}')
            elif not dest.exists():
                errors.append(f'{path.relative_to(root)}: missing link target: {target}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('package', nargs='?', type=Path, default=Path(__file__).resolve().parent.parent)
    args = parser.parse_args()
    errors = validate(args.package)
    for error in errors:
        print('FAIL: ' + error, file=sys.stderr)
    if errors:
        return 1
    print('PASS: manifest, eight skill headers, required documents, containment and local link targets')
    print('Not checked: remote links, anchors, host discovery, model behavior or privacy clearance.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
