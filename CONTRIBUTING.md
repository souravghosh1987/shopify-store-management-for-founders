# Contributing

Keep changes small and explain the user problem. Use only official documentation and synthetic fixtures; never submit client work, customer information, proprietary frameworks, scraped brand research or credentials.

Every workflow needs clear triggers, inputs, useful output, missing-data handling and a boundary between analysis and execution. Avoid duplicated long guides inside every skill. Keep worksheets inside their skill so copying a skill preserves its dependencies.

Run package validation and unit tests. For a behavioral change, try the synthetic walkthrough and at least one missing-data or conflicting-source case. Record observed output, host/version and limitations; never claim all-host compatibility from a filesystem test.

Before a release, review the entire exported tree and Git history for sensitive content. Use a clean history containing only the public package; never push an internal workspace's history. Recheck current upstream schemas and platform guidance. Release notes should distinguish offline tests, model walkthroughs and actual host/store tests.
