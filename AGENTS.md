# Package maintenance

Keep the portable core in plugin.json and skills/. This package provides operating instructions, not a Shopify connection or an authorization mechanism. Do not introduce secrets, telemetry, automatic installations or store mutations into scripts.

Use only official platform documentation and clearly labelled synthetic examples. Never add customer records, private workspaces, client examples, screenshots, proprietary playbooks or scraped brand research. Review every release file and its Git history before public publication.

Run python3 scripts/validate.py and python3 -m unittest discover -s tests before release. Check every skill's trigger, required inputs, stop conditions and usable output. Recheck official capability links and date the comparison. Describe actual test coverage; do not imply a live-store or host integration test happened when only offline checks ran.
