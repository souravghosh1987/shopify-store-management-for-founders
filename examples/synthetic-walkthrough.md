# Synthetic walkthrough: product-page consistency

All names, row keys, dates, quantities and amounts below are invented for training. They are not a real store, customer, product or Shopify identifier. No screenshots or brand examples are used.

## Input to give your AI

Use `product-page-parity`. Audit this supplied data only. Do not connect to a store or make changes. Return the worksheet, distinguish confirmed discrepancies from missing evidence, and prepare a handoff if needed.

Merchant-approved product sheet, sample revision A:
- Draft row key: DEMO-CUP-01 (not a Shopify ID).
- Product: Example Ceramic Cup, 300 ml.
- Pack: one cup.
- Care: hand wash.
- Approved color choices: blue and cream.
- No evidence supplied for microwave use.

Sample catalog export, revision B:
- Title: Example Ceramic Cup, 300 ml.
- Pack: one cup.
- Description: dishwasher safe; microwave safe.
- Selected default color: blue.
- Default image reference: DEMO-BLUE-IMAGE.

Sample rendered-page observation supplied by the merchant:
- Title: Example Ceramic Cup, 350 ml.
- Care text: dishwasher safe.
- Initial visible image: cream cup.
- After choosing blue: blue cup appears.
- Browser/device and live route not supplied.

## Expected useful findings

- Title capacity conflicts with approved 300 ml evidence.
- Dishwasher claim conflicts with approved hand-wash instruction.
- Microwave claim has no supplied substantiation; quarantine it.
- Initial image conflicts with the supplied default color; successful selection afterward does not clear the initial-load issue.
- Do not claim to have independently viewed the page or diagnosed its code.
- No verified Shopify ID, browser/device, actual route or current live snapshot is available. A real write cannot be safely targeted from this fixture.
- Preserve the supported one-cup pack and both color choices.

## Example handoff excerpt

Status: proposed, not applied. Target: DEMO-CUP-01, synthetic row only. Proposed wording changes: 350 ml → 300 ml; dishwasher safe → hand wash; remove unsubstantiated microwave claim pending evidence. Ask the merchant/operator to identify the real object and affected text bindings, capture current state and approve the revision before execution. Investigate the initial image separately rather than blindly replacing catalog media.

## Second exercise: incomplete offer economics

Synthetic order Net Sales ex tax is 40 units of currency. Product cost is 14; fulfillment is 3; shipping subsidy is 4; payment fees are 1. Assume these are the complete supplied cost-of-delivery components for this exercise only. CM2/Gross Profit is 18 (45% of Net Sales). Ad spend and operating expenses are missing, so Contribution Profit, Net Profit and MER cannot be established. Do not assume that this cost coverage is complete for a real merchant.

Ask `offer-governance` to explain the missing evidence before reviewing a discount. Do not activate a promotion or apply these invented numbers to a store.
