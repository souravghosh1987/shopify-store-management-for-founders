#!/usr/bin/env python3
"""Copy bundled skills to an explicit existing directory. Preview unless --apply."""
import argparse
from pathlib import Path
import shutil
import sys
from validate import validate


def no_symlinks(path):
    path = Path(path).absolute()
    if any(p.is_symlink() for p in (path, *path.parents)):
        raise ValueError('symlink path component is not allowed: ' + str(path))


def install(package, destination, apply=False):
    package, destination = Path(package).absolute(), Path(destination).absolute()
    no_symlinks(package)
    no_symlinks(destination)
    if not destination.is_dir():
        raise ValueError('destination must be an existing directory; create/select it yourself')
    package, destination = package.resolve(), destination.resolve()
    if destination == package or destination.is_relative_to(package):
        raise ValueError('destination must be outside the package')
    errors = validate(package)
    if errors:
        raise ValueError('source package failed validation: ' + '; '.join(errors))
    sources = sorted((package / 'skills').iterdir())
    if any(not p.is_dir() for p in sources):
        raise ValueError('skills directory must contain only skill directories')
    targets = [destination / source.name for source in sources]
    for target in targets:
        if target.exists() or target.is_symlink():
            raise ValueError('refusing existing target: ' + str(target))
    # Reserve all targets exclusively before copying. A failure cleans only this
    # invocation's newly created directories; pre-existing paths are never removed.
    if apply:
        created = []
        try:
            for target in targets:
                target.mkdir()
                created.append(target)
            for source, target in zip(sources, targets):
                shutil.copytree(source, target, dirs_exist_ok=True, symlinks=False)
        except BaseException:
            for target in reversed(created):
                shutil.rmtree(target)
            raise
    return targets


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination', required=True, type=Path, help='existing host skills directory, e.g. a project .agents/skills directory')
    parser.add_argument('--package', type=Path, default=Path(__file__).resolve().parent.parent, help=argparse.SUPPRESS)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--apply', action='store_true', help='copy files after validation; never overwrite')
    mode.add_argument('--dry-run', action='store_true', help='preview only (the default)')
    args = parser.parse_args()
    try:
        targets = install(args.package, args.destination, args.apply)
    except (OSError, ValueError) as exc:
        print('ERROR: ' + str(exc), file=sys.stderr)
        return 1
    print('Copied:' if args.apply else 'Preview only; no files written:')
    for target in targets:
        print(target)
    print('No host settings, credentials or network connections changed. Verify skill discovery in your host.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
