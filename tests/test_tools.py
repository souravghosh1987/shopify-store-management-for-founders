"""Offline regression tests using only temporary synthetic fixtures."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from install import install
from validate import EXPECTED_SKILLS, SCHEMA, validate

class ToolsTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.package = self.root / 'package'
        self.package.mkdir()
        (self.package / 'plugin.json').write_text(json.dumps({'$schema': SCHEMA, 'name': 'test-package'}))
        for name in ('README.md', 'CHANGELOG.md', 'LICENSE'):
            (self.package / name).write_text('Synthetic fixture\n')
        for name in EXPECTED_SKILLS:
            skill = self.package / 'skills' / name
            skill.mkdir(parents=True)
            (skill / 'SKILL.md').write_text(f'---\nname: {name}\ndescription: Synthetic test skill.\n---\n# Task\nPerform a synthetic review.\n')
        self.destination = self.root / 'destination'
        self.destination.mkdir()
    def tearDown(self):
        self.temp.cleanup()
    def test_valid_package(self):
        self.assertEqual(validate(self.package), [])
    def test_preview_writes_nothing(self):
        self.assertEqual(len(install(self.package, self.destination)), 8)
        self.assertEqual(list(self.destination.iterdir()), [])
    def test_apply_copies_all_skill_bytes(self):
        install(self.package, self.destination, True)
        for name in EXPECTED_SKILLS:
            self.assertEqual((self.destination/name/'SKILL.md').read_bytes(), (self.package/'skills'/name/'SKILL.md').read_bytes())
    def test_collision_preserves_existing_and_copies_nothing(self):
        target = self.destination / sorted(EXPECTED_SKILLS)[-1]
        target.mkdir()
        marker = target / 'merchant.txt'
        marker.write_text('preserve me')
        with self.assertRaisesRegex(ValueError, 'existing target'):
            install(self.package, self.destination, True)
        self.assertEqual(marker.read_text(), 'preserve me')
        self.assertEqual(list(self.destination.iterdir()), [target])
    def test_even_empty_target_is_rejected(self):
        (self.destination / sorted(EXPECTED_SKILLS)[0]).mkdir()
        with self.assertRaisesRegex(ValueError, 'existing target'):
            install(self.package, self.destination, True)
    def test_destination_must_exist(self):
        with self.assertRaisesRegex(ValueError, 'existing directory'):
            install(self.package, self.root / 'missing', True)
        self.assertFalse((self.root / 'missing').exists())
    def test_inside_package_destination_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'outside the package'):
            install(self.package, self.package / 'skills', True)
    def test_source_symlink_rejected(self):
        outside = self.root / 'outside.txt'
        outside.write_text('synthetic private material')
        (self.package / 'leak.txt').symlink_to(outside)
        with self.assertRaisesRegex(ValueError, 'symlink forbidden'):
            install(self.package, self.destination, True)
        self.assertEqual(list(self.destination.iterdir()), [])
    def test_symlink_destination_ancestor_rejected(self):
        alias = self.root / 'alias'
        alias.symlink_to(self.destination, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'symlink path component'):
            install(self.package, alias, True)
    def test_dangling_target_symlink_rejected(self):
        (self.destination / sorted(EXPECTED_SKILLS)[0]).symlink_to(self.root / 'missing')
        with self.assertRaisesRegex(ValueError, 'existing target'):
            install(self.package, self.destination, True)
    def test_copy_failure_rolls_back_only_new_directories(self):
        marker = self.destination / 'unrelated.txt'
        marker.write_text('preserve me')
        with patch('install.shutil.copytree', side_effect=OSError('synthetic failure')):
            with self.assertRaises(OSError):
                install(self.package, self.destination, True)
        self.assertEqual(list(self.destination.iterdir()), [marker])
        self.assertEqual(marker.read_text(), 'preserve me')
    def test_unknown_manifest_field_fails(self):
        p = self.package / 'plugin.json'
        data = json.loads(p.read_text()); data['commands'] = []
        p.write_text(json.dumps(data))
        self.assertTrue(any('unknown manifest fields' in e for e in validate(self.package)))
    def test_invalid_skill_name_and_missing_skill_fail(self):
        p = self.package / 'skills' / 'offer-governance' / 'SKILL.md'
        p.write_text('---\nname: wrong-name\ndescription: Example.\n---\n')
        self.assertTrue(any('mismatched skill name' in e for e in validate(self.package)))
        p.unlink()
        self.assertTrue(any('offer-governance:' in e for e in validate(self.package)))
    def test_escaping_and_missing_links_fail(self):
        (self.package / 'README.md').write_text('[outside](../private.md)\n[missing](missing.md)\n')
        errors = validate(self.package)
        self.assertTrue(any('escapes package' in e for e in errors))
        self.assertTrue(any('missing link target' in e for e in errors))
    def test_scalar_manifest_fails_cleanly(self):
        (self.package / 'plugin.json').write_text('[]')
        self.assertTrue(any('manifest must be an object' in e for e in validate(self.package)))
    def test_duplicate_frontmatter_key_fails(self):
        p = self.package / 'skills' / 'offer-governance' / 'SKILL.md'
        p.write_text('---\nname: offer-governance\nname: offer-governance\ndescription: Example.\n---\n')
        self.assertTrue(any('duplicate frontmatter key' in e for e in validate(self.package)))

if __name__ == '__main__':
    unittest.main()
