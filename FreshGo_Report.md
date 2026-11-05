# FreshGo: why peak deliveries run late and items go missing

## 1. Introduction

UK online grocery is large and contested: food retailers took about £1.5bn in online sales in July 2025 alone (ONS, 2025), and Ocado grew 15.8% to a record 2.2% share in the 12 weeks to 30 November 2025 (Worldpanel by Numerator, 2025). FreshGo promises fast, reliable, customer-focused delivery, but peak-time delays and unavailable items undermine that promise. This report analyses both problems, shows they share root causes, and recommends what to fix first.

## 2. Problem A: peak delivery delays

**The problem.** Deliveries slip at weekends, holidays and promotions, when distribution centres, drivers and route planning are all under pressure.

**Impact.** Reliability, satisfaction and repeat purchases fall (brief), and overtime raises cost. This contradicts the "reliable" promise. In the service-profit chain, service drives loyalty and profit, so delays hit revenue, not just reputation.

**Where it breaks.** Inputs are orders, drivers and route-planning systems; transformation is pick, pack, dispatch and route; output is late delivery. Assumption: dispatch and driver capacity saturate first. Lateness is the gap between what customers expect and what they get, so it erodes trust each time it happens.

**Operation type.** Variability dominates because demand swings sharply; volume is high, which normally allows standardisation, while variety and visibility matter less here. Dependability and speed suffer first, cost second, quality third. So FreshGo must manage variability, not just volume. Peak delay is a symptom, not the cause.

## 3. Problem B: inventory availability

**The problem.** Items become unavailable after ordering, caused by stock inaccuracy, poor visibility and weak replenishment.

**Impact.** Cancellations rise and confidence falls (brief). Refunds and waste add cost, and each cancellation breaks the customer promise a second time.

**Where it breaks.** Inaccurate stock data goes in, picking proceeds on a false basis, and substitutions and cancellations come out. Visibility is the key V: the catalogue shows stock the warehouse may not hold. Fresh and ambient variety adds difficulty.

**Operation type.** Order accuracy (quality) suffers first, then dependability, then cost. Stock-record inaccuracy is common and drives lost sales (DeHoratius and Raman, 2008); perishable, variable-demand goods need a responsive supply chain (Fisher, 1997).

## 4. How the problems compound

A stock-out forces substitutions or re-picks, adding peak workload and worsening delays. Delay raises order changes and cancellations, feeding back into stock errors, so the loop tightens exactly when demand is highest. Rivals raise expectations: Ocado's growth (above) shows what customers can now get elsewhere. FreshGo's operation works against its own strategy.

## 5. Root causes

Both problems trace to the same causes, ranked below.

1. **Weak forecasting (primary).** The brief says forecasts use historical data and omit real-time information. Forecast error flows into both capacity and stock and amplifies along the chain (the bullwhip effect; Lee et al., 1997), so it is the strongest root candidate.
2. **Capacity does not match demand.** Level capacity fails in peaks. Chase capacity is costly with fixed hubs; demand shaping is cheap but slow. A hybrid suits FreshGo: a level base, surge capacity for known peaks, and slots and promotion timing.
3. **Workforce planning.** Fixed rostering gives idle labour in troughs and overtime in peaks (brief). Flexible options (annualised hours, cross-training, temporary labour) cost training, quality and morale.
4. **Utilisation and bottlenecks.** Manual picking and layout (assumed) create a constraint, and management decisions on capacity and rostering set utilisation. As it nears 100%, waiting time rises sharply (queueing theory), so a small surge causes a large delay.

**Judgement.** Forecasting is the root; the others turn forecast error into failure, so fixing them alone treats symptoms. Counter-view: promotions may create some peaks. The brief gives no utilisation or forecast-error figures, so this diagnosis is inferred.

## 6. Gap table

| Practice | FreshGo (brief) | Gap | Better practice | Trade-off |
|---|---|---|---|---|
| Forecasting | Historical sales | No real-time signals | Weather, promotion, event data | Data cost |
| Capacity | Fixed hub capacity | Peak overload | Surge capacity | Idle troughs |
| Workforce | Static staffing | Overtime, idle labour | Flexible contracts | Training, quality |
| Demand management | Not mentioned | Peaks unshaped | Slot pricing, promotion timing | Customer reaction |
| Inventory visibility | Poor | Stock inaccuracy | Cycle counts, real-time tracking | System cost |

## 7. Ocado benchmark and recommendations

**Benchmark.** Ocado Retail reports 99% of items delivered as promised from automated centres (Ocado Retail, 2025). The limit is capital intensity: Kroger is closing three Ocado-built centres in the US (Ocado Group, 2025). FreshGo should not copy it wholesale.

1. **Improve forecasting and stock accuracy first** (real-time signals, cycle counts). It fixes both problems cheaply; the risk is data cost and uncertain gains.
2. **Add flexible labour and slot-based demand management.** It matches capacity to demand; the risks are training and customer reaction. Second, as it needs better forecasts.
3. **Evaluate automation only if volume justifies it.** It gains accuracy and speed but needs heavy capital. Last.

**Stress test.** If demand grows 30% or forecasting gains disappoint, action 3 moves earlier and action 2 widens.

## 8. Conclusion

Weak forecasting matters most because it drives both capacity and stock errors. Improve forecasting and stock accuracy first: it is cheapest and fixes both problems. Track peak on-time delivery, item availability, substitution rate and overtime hours; if they do not improve within two peak periods (an assumption), move to the later actions.
