# Common mistakes and remedies

| Symptom or mistake | Check | Remedy |
| --- | --- | --- |
| “Installed the plugin, but no Shopify tools” | Did you install this workflow package or Shopify's official integration? | Install/connect the official integration separately when needed; use exports meanwhile |
| Skill not discovered | Host's actual skill directory, folder name, SKILL.md and reload behavior | Use the documented destination; copy the whole skill folder, then test a synthetic prompt |
| Installer refuses an existing folder | Is this a prior version or another owner's skill? | Compare and back up; never blindly overwrite or delete the shared destination |
| Authentication expired | Current CLI help, session and required scopes | Merchant reauthorizes via official flow; never paste a token into chat |
| Permission denied | Requested action, granted data scope and account role | Explain missing access; don't escalate permissions or infer every API error is a scope issue |
| Wrong store after switching | Actual tool response/store identity and conversation context | Stop, start a fresh conversation where required and reconfirm; do not reuse old approval |
| Timeout after a write | Current saved state and any returned job ID | Check outcome before retry; reconcile per-item partial results |
| “Draft” interpreted as harmless | Does it create a product, upload media or stage a theme remotely? | Treat it as a remote mutation requiring approval |
| Product image passes after clicking but fails on load | Default media, selected variant and initial rendered frame | Test fresh load and transitions separately; don't infer all devices from one browser |
| Reports disagree | Period, timezone, currency, tax/refund/discount definitions | Align definitions before comparing; keep unresolved discrepancies visible |
| Revenue called profit or MER | Complete costs and relevant ad spend present? | Calculate only supported metrics; show the missing inputs |
| Too many landing-page sections | Existing native content coverage and information needs | Reuse suitable native sections; no mandatory section count |
| Merchant edits disappeared | Was current state re-read immediately before action? | Stop affected changes, reconcile revisions and use an approved recovery plan |
| Unverified product claim sounds persuasive | Exact evidence and applicable variant | Quarantine the claim; ask for the missing source instead of inventing support |
| Public issue contains a store export | Data exposure and destination | Don't upload it; create a small synthetic reproduction with no customer data |

These are diagnosis steps, not permission to repair live systems. Return the exact unresolved error and a useful next step when access or evidence is insufficient.
