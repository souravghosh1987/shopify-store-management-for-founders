# Validation and compatibility

## Run offline checks

From the package root, with Python 3.10 or later:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests
```

The validator checks this package's manifest/frontmatter/layout, required files and local Markdown links. Unit tests exercise installer and validator failure paths. These checks do not prove AI reasoning quality, host discovery, store access or merchant approval.

## Compatibility contract

- Portable target: Agent Plugins v1.0.0, with Agent Skills in immediate `skills/` children.
- No custom MCP configuration or universal slash commands.
- Each skill is independently copyable with its worksheet.
- Host-specific loading must be verified in the chosen host. Manual chat use is supported as instructions, not advertised as native installation.
- Python utilities use the standard library and do not connect to Shopify.

## Behavioral acceptance

Use the synthetic walkthrough and check that the AI identifies supported discrepancies, quarantines unsupported claims, preserves correct fields, distinguishes observation from diagnosis and refuses to invent missing IDs. Also test a store switch, an approval followed by changed source values, a partial/uncertain execution receipt and missing costs. The correct behavior is useful bounded analysis plus a clear next step, not false completion.

## Release review

Independent reviewers should inspect every release file for privacy/proprietary leakage and evaluate a realistic workflow from raw inputs. Scan filenames and text, then inspect the clean public Git history. Record the exact reviewed version and rerun affected gates after edits. No live-store acceptance is implied by these offline procedures.
