# Official Shopify integrations and the CLI

Documentation checked 12 November 2026. These are documented capabilities, not a claim that this package was tested inside every product. Availability and actions depend on current rollout, user permissions, data access and the selected integration.

## Three separate layers

1. **Your AI host** reads instructions and provides tools.
2. **Shopify's official integration or CLI** supplies authorized store access.
3. **This package** supplies the operating workflow, worksheets and handoff discipline.

Installing layer three does not create layer two. A successful connection also does not authorize every action.

## Chat integrations

The [official capability overview](https://help.shopify.com/en/manual/ai-powered-tools/connecting-ai-tools) distinguishes these surfaces:

| Surface | Documented emphasis |
| --- | --- |
| ChatGPT and Claude | Store creation, storefront work, existing-store management and Collective sourcing |
| Gemini and Grok / Grok Bot | Store creation, storefront work and existing-store management |
| Muse | Preview creation, connecting an existing store or signup/linking a new one |
| Perplexity and Microsoft Copilot | Preview creation and existing-store management; Copilot has product-specific host contexts |

Consult the individual integration page before assuming an action exists. Canvas design is still labelled coming soon in that overview. Do not promise uniform feature parity or a fixed skill count.

[ChatGPT's documentation](https://help.shopify.com/en/manual/ai-powered-tools/connecting-ai-tools/shopify-plugin-for-chatgpt) includes product, collection, inventory, order, customer, discount and analytics tasks and unpublished-theme edits. It contains conflicting publishing guidance: its considerations prohibit publishing, while its detailed theme section/action table describes confirmation-based publishing. Check the actual connected tool and current guidance; use Shopify admin when the integration cannot reliably complete an approved action. This package does not publish themes.

[Authorization guidance](https://help.shopify.com/en/manual/ai-powered-tools/connecting-ai-tools/authorizing-access) documents one consumer store connection at a time and a supported switch flow. Start a fresh conversation after switching and reconfirm the target. Access is limited by both the approved data scope and the user's permissions. Increasing access requires consent; decreasing approved scope requires uninstalling the integration. Review the provider's privacy terms because authorized data leaves Shopify.

## Developer and agent tools

[Build with AI](https://www.shopify.com/build-with-ai) supplies maintained official toolkit installation routes for Claude Code, Codex, Antigravity, Cursor, Hermes, OpenClaw, Pi and VS Code. Use the instructions shown there for the actual host; do not substitute a consumer connector or assume an MCP-only setup is required. Those official installation commands install Shopify's toolkit, not this workflow package.

The [CLI connector](https://help.shopify.com/en/manual/ai-powered-tools/shopify-cli-connector) is intended for local developer tools on a machine you control. It authorizes API access and is not a chat interface. An operator can pair it with these workflows for reproducible reads and separately approved execution.

## Where CLI complements chat

| Need | CLI advantage | Cost or tradeoff |
| --- | --- | --- |
| Repeatable data investigation | Explicit store, query inputs, output files and version selection | Validate queries and protect exported private data |
| Larger operational handoff | Reusable operation files and per-item receipts | Pagination, throttling and partial failures need deliberate handling |
| Theme specialist work | Theme Check, targeted files, development/unpublished previews | Uploads are remote writes; preserve merchant changes and test visuals |
| Several stores over time | Explicit target parameters and isolated job folders | Remembered context can still target the wrong store; no blind batch operations |

CLI is not inherently safer and does not bypass user permissions or business approval. A chat integration may be the simpler route for a founder's occasional lookup. Exports can be adequate for an offline audit.

## Operator connection procedure

1. Inspect the installed CLI version and help. Use the project's supported version and current official documentation; do not silently upgrade a shared environment.
2. Confirm the exact store and requested operation. Follow [store auth](https://shopify.dev/docs/api/shopify-cli/store/store-auth): store and scopes are required, and online authentication may need renewal. Explain consent rather than promising a fixed setup time.
3. Start with a minimal authorized read. [Store execute](https://shopify.dev/docs/api/shopify-cli/store/store-execute) uses stored authentication and disables mutations unless explicitly enabled. Do not add the mutation flag to a read-only investigation.
4. Keep tokens out of prompts, logs and source control. Do not use verbose logs when they might expose sensitive data.
5. For any later write, hand off a reviewed revision, explicit target, fresh-state check and verification plan to the authorized execution owner. Check uncertain outcomes before retrying.

Theme access is separate: [Theme CLI](https://shopify.dev/docs/storefronts/themes/tools/cli) documents supported authentication methods and permissions. [Theme dev](https://shopify.dev/docs/api/shopify-cli/theme/theme-dev) uploads a theme; it is not local-only. [Theme push](https://shopify.dev/docs/api/shopify-cli/theme/theme-push) can replace remote files, and publishing needs separate approval. Theme Check cannot prove merchant-editability or correct mobile/desktop behavior.
