# Add the workflows to your AI setup

## Choose a route

| Your setup | Route | What this does not establish |
| --- | --- | --- |
| Host supporting Agent Plugins v1.0.0 | Add this package root using the host's documented plugin import method | Not every host implements this portable format |
| Host supporting Agent Skills folders | Copy the desired immediate folders from `skills/` into that host's documented skills directory | Does not install Shopify connectivity or grant scopes |
| Chat with file uploads but no skill loader | Attach the desired `SKILL.md`, its worksheet and your authorized input; ask the AI to follow them | Manual instructions, not a persistent plugin install |
| Chat without uploads | Paste the selected skill text and a small sanitized input, then use its worksheet headings | No local filesystem or live-store access implied |

Use your host's current documentation to select its skill destination. For a project-scoped host that recognizes `.agents/skills`, create that directory in your own project first. Do not assume all chat apps recognize it. Do not overwrite an existing skill with the same name.

## Optional offline installer

Requires Python 3.10 or later. Run from the downloaded package root. Replace the example destination with your actual existing skills directory. The first command previews the eight target folders and writes nothing:

```bash
python3 scripts/install.py --destination /path/to/your/project/.agents/skills
```

After reviewing the paths, explicitly apply the copy:

```bash
python3 scripts/install.py --destination /path/to/your/project/.agents/skills --apply
```

The destination must already exist. The installer refuses collisions and symlink paths. It does not install packages, modify host settings, authenticate or access the network. Run the host's own refresh/reload procedure if needed, then ask it to identify the loaded skill and its worksheet.

If you only need one workflow, manually copy that entire skill folder, including `assets/`, into the documented destination. Copying only SKILL.md loses the worksheet.

## Verify use before connecting a store

Ask: “Use product-page-parity with the synthetic walkthrough. Return a coverage matrix, unsupported claims and next action. Do not connect to Shopify or change anything.”

Check the output against the walkthrough's expected findings. A model following instructions is not proof that a native plugin loader discovered the package. Record your actual host and version if you test native loading.

## Updating and removing

Before updating, compare the release and back up any edits you made to your installed skill folders. The installer deliberately does not overwrite existing folders. Reconcile manually or install into a new empty test destination, then replace only the old package's folders after checking your changes.

To remove, delete only the eight installed folders listed in README.md from the destination you selected. Removing these files does not revoke a Shopify integration: revoke that separately in the integration/Shopify admin using official guidance. Do not delete a shared skills directory or another package's files.

## Connect Shopify separately

Use [Shopify Build with AI](https://www.shopify.com/build-with-ai) to choose the official route for your actual host. Consumer integrations and local CLI authorization are different. Review [platforms and CLI](docs/platforms-and-cli.md) before setup. Never paste tokens into a chat or public issue.
