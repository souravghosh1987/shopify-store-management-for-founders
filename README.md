# Shopify Store Management for Founders

Eight practical AI workflows for a founder who wants a clearer, more consistent Shopify store: audit the evidence, decide what matters, prepare bounded changes, and hand over work that can be checked.

Use this **alongside [Shopify's official AI tools](https://www.shopify.com/build-with-ai)**. It is an independent workflow package, not a Shopify app, official connector, autonomous store manager or promise of revenue. Version 1.0.0 prepares analyses and change handoffs; it does not execute store writes.

## Start here

1. **Try without a store connection:** give your AI [the synthetic walkthrough](examples/synthetic-walkthrough.md) and the `product-page-parity` skill. Ask it to produce the coverage matrix. No credentials or real customer data needed.
2. **Add the skills:** follow [INSTALL.md](INSTALL.md) for a compatible skills host, manual project installation, or plain chat use. Installing these instructions does not connect Shopify.
3. **Connect only if needed:** choose an official integration using [the platform and CLI guide](docs/platforms-and-cli.md). Review provider privacy and permissions before sharing store data.
4. **First real request:** “Use store-operating-baseline. Help me review this store's product information using these authorized exports. Start read-only, identify missing evidence, and recommend the first three actions.”

## Pick the workflow

| Ask your AI to use | Useful when | You receive |
| --- | --- | --- |
| `store-operating-baseline` | Starting or switching a store review | Access/source inventory and priorities |
| `merchandising-governance` | Titles, handles and collections disagree | Before/after catalog proposal and dependencies |
| `product-page-parity` | Product details or claims need checking | Evidence/coverage matrix and limited corrections |
| `media-library-discipline` | Default or variant images look wrong | Asset/binding plan, rights and coverage gaps |
| `offer-governance` | Considering a discount or shipping offer | Economics-aware decision brief |
| `store-reporting-rhythm` | Reviewing a period of performance | Defined metrics, exceptions and next actions |
| `controlled-change-handoff` | Someone must execute a store edit | Revision, exact scope, drift/rollback checks and receipt requirements |
| `founder-operating-sops` | Maintaining or handing over store work | Short operating procedure with owners and stop conditions |

Each skill has a worksheet inside its own folder. Skill names are invocation hints, not guaranteed slash commands. Ask your host to show which skills it actually loaded.

## What makes the package practical

- Start from exports or synthetic inputs before granting access.
- Install only the skills you need manually, or all eight with the optional offline installer.
- Preserve human decisions and merchant edits through explicit change records.
- Separate source checks, saved-state checks and visual checks.
- Use included worksheets and a worked example rather than inventing a process each time.
- Keep platform claims dated and link to the maintained official source.

## Boundaries

No MCP server, OAuth app, token store, store-writing script, scheduler or telemetry is bundled. The installer only copies files after `--apply`; the validator only reads package files. AI instructions are not a security boundary: host permissions, provider controls and merchant authorization still govern access. See [SECURITY.md](SECURITY.md).

This is not a theme-design library. It contains no client artifacts, brand research, scraped examples or storefront code. For actual theme/API implementation, use the official Shopify toolkit and a separately authorized operator.

## Documentation

- [Installation and removal](INSTALL.md)
- [Official integrations and CLI tradeoffs](docs/platforms-and-cli.md)
- [Common mistakes and remedies](docs/troubleshooting.md)
- [Synthetic walkthrough](examples/synthetic-walkthrough.md)
- [Validation and compatibility](docs/validation.md)
- [Sources](docs/sources.md)
- [Changelog](CHANGELOG.md)

## Contributing

Use synthetic examples and official sources only. Describe the observed problem, expected output and tested host/version. Do not post credentials, customer information, private exports or store screenshots in public issues. See [CONTRIBUTING.md](CONTRIBUTING.md). Licensed under [MIT](LICENSE).
