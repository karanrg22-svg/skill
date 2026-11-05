# FreshGo operations improvement blueprint

Fixing peak-time delivery delays and inventory availability

Basis: FreshGo facts come only from the company brief. Market and competitor evidence is taken from published sources. Anything not in the brief is labelled as an assumption.

## 1. Strategy at a glance

| Item | Decision |
|---|---|
| Problem A | Delivery delays at peak demand |
| Problem B | Inventory availability and stock inaccuracy |
| Central argument | Both are symptoms of one chain. Weak forecasting leads to poor capacity and labour matching, which causes stock-outs and late delivery, and each failure makes the other worse |
| Benchmark | Ocado, used for one capability and one limit |
| Analytical tools | Input-transformation-output (ITO) view, the 4Vs (volume, variety, variability, visibility), the five performance objectives, capacity and demand management |
| Evidence rule | FreshGo evidence comes from the brief only. Market and competitor evidence is real and sourced. Assumptions are labelled |

## 2. Plan structure

| Section | Purpose |
|---|---|
| Introduction | Market context and the logic of the plan |
| Problem A: peak delivery delays | Define, explain impact, analyse |
| Problem B: inventory availability | Define, explain impact, analyse |
| How the problems compound, and external pressure | Show the loop and the strategic cost |
| Root causes | Trace symptoms back to ranked causes |
| Gap table | FreshGo practice versus better practice, with trade-offs |
| Benchmark and recommendations | Ocado comparison, sequenced actions, stress test |
| Conclusion | Which cause matters most and what to do first |

## 3. Section blueprints

### Introduction

Job: frame the problem and the logic of the plan, with no filler.

| Move | Content | Source |
|---|---|---|
| 1 | UK online grocery is growing and contested. Use one or two real figures | ONS internet sales data (2025); Worldpanel by Numerator market share (2025) |
| 2 | FreshGo's stated strategy promises fast, reliable, customer-focused delivery | FreshGo brief |
| 3 | The plan analyses peak delivery delays and inventory availability, then diagnoses root causes | Operations management framework |

Avoid: company history, a definition of operations management, and "this plan will..." padding.

### Problem A: peak delivery delays

| Step | What to cover | Source |
|---|---|---|
| 1. Problem | One precise sentence: delays at weekends, holidays and promotions, with pressure on the distribution centres, drivers and route planning | Brief |
| 2. Why (preview only) | Demand spikes against a capacity that does not flex. Detail is left to the root-cause section | Operations framework |
| 3. Impact | Reliability and satisfaction fall, and repeat purchases fall (brief). Overtime pushes cost up. This contradicts the stated "reliable" strategy. Link service quality to loyalty and profit through the service-profit chain | Brief; service-profit chain |
| 4. Analysis | ITO: inputs (orders, drivers, route-planning systems), transformation (pick, pack, dispatch, route), output (late deliveries). Show where the transformation saturates. 4Vs: variability dominates. Volume is high, which would normally allow standardisation. Say which Vs matter less. Performance objectives: dependability and speed are hit first, cost second, quality (fresh goods) third. Rank them | Operations framework |
| Service-quality angle | Late delivery is a gap between what the customer expects and what is delivered (SERVQUAL gap model) | Service-quality model |

Key point: call peak delay a symptom, and say why in one clause. That sets up the root-cause section.

### Problem B: inventory availability

| Step | What to cover | Source |
|---|---|---|
| 1. Problem | Items unavailable after order, caused by stock inaccuracy, poor visibility and weak replenishment | Brief |
| 3. Impact | More cancellations and lower customer confidence (brief). Refund and waste cost | Brief |
| 4. Analysis | ITO: inaccurate stock data in, picking on a false basis, then substitutions and cancellations out. 4Vs: visibility is the key V, because the online catalogue shows stock the warehouse may not hold. Variety (fresh and ambient SKUs) adds difficulty. Performance objectives: quality (order accuracy), dependability, cost | Operations framework |
| Inventory record accuracy | Record inaccuracy is common and drives lost sales and poor availability | Retail inventory-accuracy research |
| Product type | Perishable, variable-demand goods need a responsive supply chain, not an efficient one | Supply-chain fit model (functional versus innovative products) |

### How the problems compound, and external pressure

| Move | Content | Source |
|---|---|---|
| Compounding | A stock-out causes substitutions or re-picks, which add peak load and worsen delays. Delay then raises order changes and cancellations. Present it as a loop | Reasoning from the brief |
| External pressure | Fast-growing competitors raise customer expectations. Ocado sales up 15.8% to a record 2.2% share (12 weeks to 30 November 2025) | Worldpanel by Numerator (2025), via Retail Gazette; verify against the primary release |
| Strategic link | The operation undermines its own strategy | Brief |

### Root causes

Work backwards from symptom to cause and show the "why?" chain.

| Cause (ranked) | Argument | Source |
|---|---|---|
| 1. Weak forecasting | The brief says forecasts rely on historical data and omit real-time information. Error carries into both capacity and stock, so it is the strongest candidate for primary root cause. A bullwhip-style amplification argument applies if it can be justified | Brief; bullwhip effect; forecasting practice |
| 2. Capacity-demand mismatch | A level-capacity posture fails in peaks. Contrast level, chase and demand-management strategies, and say which fits FreshGo and why (for example, a hybrid) | Capacity management; service-capacity matching |
| 3. Workforce planning | Fixed rostering gives idle labour in troughs and overtime in peaks (brief). Flexible options (annualised hours, cross-training, temporary labour) have costs in training, quality and morale | Capacity management |
| 4. Utilisation and bottlenecks | Manual picking and poor layout create a constraint. As utilisation nears 100%, waiting time rises sharply | Theory of constraints; queueing (Little's law); factory physics |

Required checks:

- Rank and justify. Say which cause is the root and which are contributory.
- Counter-view. Promotions may create some of the peaks, so part of the demand is self-inflicted.
- Limits. The brief gives no utilisation or forecast-error figures, so the diagnosis is inferential. Say so in one sentence.

### Gap table

| Practice | FreshGo (from brief) | Gap | Better practice | Trade-off |
|---|---|---|---|---|
| Forecasting | Historical sales | No real-time signals | Add weather, promotion and event data | Data cost, complexity |
| Capacity | Fixed hub capacity | Peak overload | Surge or flexible capacity | Idle capacity in troughs |
| Workforce | Static staffing | Overtime and idle labour | Flexible contracts | Training, quality |
| Demand management | Not mentioned | Peaks unshaped | Slot pricing, promotion timing | Customer reaction |
| Inventory visibility | Poor | Stock inaccuracy | Cycle counts, real-time tracking | System cost |

Keep every row tied to a cause in the root-cause analysis.

### Benchmark and recommendations

| Element | Content | Source |
|---|---|---|
| Benchmark | One Ocado capability, such as automated fulfilment or high order accuracy, with the figure checked in the annual report (the search suggested 99% of items delivered as ordered, which must be verified). Then the limit: it is capital-intensive, and 2026 reporting says North American partners are closing some customer fulfilment centres, so FreshGo should not copy it wholesale | Ocado Retail Annual Report 2025; RTE (2026), verify |
| Recommendations | 1) Improve forecasting and inventory accuracy first (cheap, fixes both problems). 2) Add flexible labour and slot-based demand management. 3) Evaluate automation only if volume justifies it. For each, give the benefit, the cost or risk, and the order | Supply chain and logistics practice |
| Stress test | What if demand grows a further 30%, or forecasting gains are smaller than expected? | Reasoning from the brief |

### Conclusion

Give a judgement: which root cause matters most, which action comes first and why. Add no new evidence and do not restate everything.

## 4. Test of the plan

| Test | How the blueprint meets it |
|---|---|
| Problems interact and compound | Compounding section, with the loop |
| Links to strategy and external pressure | Strategy contradiction, plus the Ocado pressure |
| Models used to reach conclusions, not just described | Each model is followed by "so FreshGo...", with ranked Vs and objectives |
| Management decisions affect capacity and utilisation | Root-cause section |
| Contradictions between intentions and outcomes | "Reliable" strategy against peak failure |
| Evidence from the case | Every FreshGo claim traces to the brief |
| Sources | Every external figure has a named source |

## 5. Pitfalls to avoid

- Definitions with no application, or models named but not used.
- Retelling the brief.
- Invented FreshGo numbers.
- Recommendations without cost, risk or sequence.
- Unsourced claims.

## 6. Sources to confirm

Check every figure against the original before relying on it.

- FreshGo company brief.
- Ocado Retail (2025) Annual Report 2025: https://sustainability.ocadoretail.com/wp-content/uploads/2025/09/OCADO-ANNUAL-REPORT_2025.pdf
- Office for National Statistics (2025) Internet sales by retail sector, Great Britain: https://www.ons.gov.uk/businessindustryandtrade/retailindustry/adhocs/3027internetretailsalesbysectoruptojuly2025greatbritain
- Worldpanel by Numerator (2025) UK grocery market share. Replace the secondary news page with the primary release.
- RTE (2026) reporting on Ocado partner fulfilment centre closures. Verify.
- Background references for the frameworks used: operations management textbook (ITO, 4Vs, performance objectives, capacity strategies); supply-chain strategy and logistics texts; bullwhip effect, theory of constraints and queueing literature; service-profit chain and SERVQUAL service-quality models; retail inventory-accuracy research.
