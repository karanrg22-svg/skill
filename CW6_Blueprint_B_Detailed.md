# CW6 — FRAMING B: "EARN IT, SHOW IT, KEEP IT — FAMILY TRUST AS THE PRODUCT" — DETAILED 80+ BLUEPRINT
Companion to `CW6_Disney_Blueprint.md` (admin rules, brief facts) and **independent of** `CW6_Blueprint_A_Detailed.md`. Do not mix material between A and B: they are built to be different in every analytical respect (see §1).
**Blueprint only.** It specifies what to argue, prove and show. The final wording, diagrams and numbers must be yours (brief: AI only to review a draft/correct language; keep prompts; declare on cover sheet; viva possible).
**Flags:** `[V]` = verify against the primary source before use. `[IC]` = insert in-class Disney+ material (send it to me). Any figure I give from memory may be out of date (today is Nov 2026).

---

## 0. LOCKED DECISIONS
| Decision | Locked choice |
|---|---|
| Technology (AC1: *one*) | **Privacy-enhancing technologies (PETs) for personalisation**: on-device inference + federated learning + differential privacy, so recommendations are produced **without centralising raw viewing data**, starting with kids' and family profiles |
| Problem (AC1) | **A trust and regulatory-exposure problem**: Disney+ needs data to personalise and monetise (ad tier, global expansion), but its core customers are families, regulators are tightening on children's data, consent-based privacy is failing in practice, and regional compliance is fragmented |
| Stakeholder (AC2: *one*) | **Parents and guardians** (customers who are also the legal consent-givers for children) |
| Thesis | In a market of near-identical catalogues and recommender algorithms, **verifiable family trust** is a defensible differentiator; it must be achieved by **architecture over policy**, proven through **independent verification**, and sustained as a **moving baseline** |
| Spine | **Earn it** (architecture) → **Show it** (verification & transparency) → **Keep it** (operating model & renewal) |
| Recommendations (AC3: *three*) | R1 Privacy-by-Architecture Standard with PET pilot on kids/family profiles (Earn) · R2 Family Trust Layer: Data Passport, parent panel, independent audit, published scorecard (Show) · R3 Trust & Privacy Engineering operating model with aligned rewards and capability (Keep) |
| Length | 12 slides (11 content + references) + 3 appendix; video 9:15–9:45 |

---

## 1. DIFFERENCE MATRIX vs FRAMING A (proof of non-overlap)
| Dimension | A (flywheel) | **B (this file)** |
|---|---|---|
| Core problem | Churn + creative/data misalignment | Trust, children's-data exposure, consent failure, regional compliance fragmentation |
| Technology | ML recommender + editorial layer | **PETs: on-device/federated learning, differential privacy** |
| Stakeholder | Creative teams | **Parents/guardians (customers)** |
| Thesis type | Resource-based/capability argument | **Differentiation via trust + verification** |
| Stakeholder theory | Mendelow, Mitchell et al. | **Freeman (1984), Clarkson (1995)** |
| Org-impact theory | Leavitt diamond | **Galbraith Star Model** |
| Culture theory | Schein | **Cameron & Quinn Competing Values Framework** |
| Change theory | Kotter (critiqued) + ADKAR + Edmondson | **Beer & Nohria Theory E/O + Bandura self-efficacy + TAM + Arnstein participation ladder** |
| Advantage theory | VRIN + dynamic capabilities | **Porter (1985) differentiation + Keller brand equity + Blue Ocean ERRC/strategy canvas** |
| Ethics lens | Floridi principles | **Nissenbaum contextual integrity + UNCRC General Comment 25 + privacy-washing critique** |
| Foresight tool | Sense–Seize–Transform | **Scenario planning 2×2 (Schoemaker)** |
| Quantification | Illustrative churn/lifetime-value model | **Regulatory-exposure ladder + breach-cost benchmarks + privacy–utility frontier** |
| Hero visuals | Flywheel, heat map, Leavitt diamond | **Data-flow comparison, exposure ladder, strategy canvas, Star model, scenario matrix** |
| KPIs | Churn Δ, discovery breadth, cross-franchise adoption | **Trust Index, data-minimisation ratio, on-device share, privacy–utility gap, DSAR time, audit findings** |
| Roadmap | 8 quarters, pilot-then-scale | **18 months, monthly grid; phases Assure → Architect → Assert** |
| Slide-1 style | Answer-first | **Hook question first; answer by S2 (SCQA)** |
| Recurring device | Golden-thread phrases | **"Parent's view" strip on every slide** |
| Palette | Navy/teal/gold | **Charcoal/plum/amber** |
| Reference overlap | – | **No overlapping academic sources** (only unavoidable statute/regulator overlap) |
| Viva focus | Strategy/organisation | **Privacy technology, law, trust measurement** |
Unavoidable common ground: the brief's structure, the one-tech/one-group/three-recs rules, and shared law (UK/EU GDPR, ICO Children's Code).

---

## 2. 80+ DESCRIPTOR CHECKLIST (every phrase → proof)

### AC1 — Select and Analyse a Relevant Technology (30%)
| 80+ phrase | Slide | On-slide proof | Notes proof | Harsh-marker test |
|---|---|---|---|---|
| "outstanding depth" | 3–5 | Fig 2 data-flow comparison; Fig 3 exposure ladder; Fig 4 frontier | how federated learning/DP work at a level you can defend; device constraints | Could someone with no PET knowledge follow *and* a specialist not wince? |
| "originality in evaluating the technology" | 2–5 | Reframe: privacy as architecture not policy; privacy–utility trade-off made explicit | privacy paradox implication | Is the angle different from "AI + ethics"? |
| "integrates multiple high-quality sources" | 2–5 | Academic (McMahan; Dwork & Roth; Acquisti) + regulatory (ICO, GDPR) + industry (Pew, Cisco, IBM) | triangulation; conflicts (privacy paradox vs concern surveys) | Do surveys and behavioural studies disagree, and is it said? |
| "exceptional critical insight and synthesis" | 4–5 | Benefits flagged as avoided-loss/option value (not revenue); limits table | self-reported survey critique | Does it say what PETs *cannot* do? |
| Problem & why of concern | 2 | SCQA structure; Fig 1 | brief's ops/compliance vs data/marketing tension | Disney-specific? |
| Technology introduced; addresses problem | 3 | Fig 2 + 3 mapping rows | mechanism | Mechanism shown? |
| Benefits & risks | 4–5 | Fig 3; Table 1; Fig 4 | scoring | Balanced? |

### AC2 — Assess Organisational and Stakeholder Impacts (30%)
| 80+ phrase | Slide | Proof | Notes proof | Test |
|---|---|---|---|---|
| "outstanding critical evaluation of organisational and stakeholder impacts" | 6–7 | Table 2 (parents); Fig 6 Star model | alignment/misalignment propositions | Impacts on structure, culture and processes all explicit? |
| "innovative, evidence-based insights into managing change and digital confidence" | 6–7 | Parent panel at Arnstein "partnership"; Theory E/O hybrid; Bandura-based confidence design; TAM for controls adoption | evidence per element | Is digital confidence addressed for both staff *and* parents? |
| "exceptional synthesis of theory and practice" | 6–7 | Each theory → named Disney action | worked example | Theory applied or decorative? |
| ONE stakeholder group; concerns; management | 6 | Parents/guardians; justify via Freeman/Clarkson + legal consent role | evidence of concerns [V] | Only one group developed? |
| Barriers/resistance | 7 | Ad-revenue pressure, analytics reliance, device fragmentation, accuracy fear, regional variance | owners of resistance | Evidence? |
| Change management & digital confidence | 7 | Fig 6 + confidence strip | metrics | Measurable? |

### AC3 — Evaluate Strategic Implications and Make Recommendations (30%)
| 80+ phrase | Slide | Proof | Notes proof | Test |
|---|---|---|---|---|
| "integrates strategic theory, ethics, and innovation" | 8–9 | Strategy canvas + ERRC; ethics tensions tied to differentiation; innovation = household co-viewing recommendations & published trust scorecard | link sentences | Are ethics inside the strategy argument? |
| "original, feasible, grounded in deep critical reasoning" | 10 | Gate + kill-switch + fallback hybrid; sequencing | why-not alternatives | Feasible given smart-TV fragmentation? |
| "exceptional strategic foresight" | 9 | Fig 8 scenario matrix + no-regret moves | scenario logic | Robust across scenarios? |
| Supports agility/innovation/retention | 8 | goal→mechanism→KPI | — | Each evidenced? |
| Sustain through continuous improvement | 8 | Privacy maturity model + audit cadence + "moving baseline" | cadence | Concrete? |
| Ethics/risk + mitigation | 9 | Table 3 + residual risk | UNCRC/Nissenbaum | Owner + KPI? |
| Exactly **three** recs, evidence-based | 10 | Table 4 | evidence per rec | Exactly 3? |

### AS1 / AS2
| 80+ phrase | Proof |
|---|---|
| "exceptional professionalism and creativity" | Original diagrams; "Parent's view" strip; consistent visual system |
| "cohesive" | Earn–Show–Keep spine as a progress marker on S3–S11 |
| "visually outstanding" | ≤65 words/slide; one hero visual |
| "academically rigorous" | critique tag per theory |
| "well-crafted notes that expand" | core + depth bullets |
| AS2 "precise, full, appropriate" | two-way citation audit; sourced figures |

---

## 3. SPINE AND SIGNPOSTING
**S1 Hook → S2 SCQA → S3 Mechanism → S4 Benefits → S5 Limits → S6 Parents → S7 Organisation & change → S8 Advantage → S9 Ethics & futures → S10 Decisions → S11 Ask**
Spine labels: **EARN** (S3–S5, R1) · **SHOW** (S6, S9, R2) · **KEEP** (S7–S8, R3).
Three phrases to repeat: **"architecture over policy"**, **"verify, don't promise"**, **"trust is a moving baseline"**.
Transition formula: *Question → evidence → "so what for a parent" → next question.*
**Recurring device:** "Parent's view" strip (one line at the bottom of each slide, ≤14 words) translating the slide into what a parent would notice. Counts toward on-slide words.

---

## 4. CLAIM–EVIDENCE–CRITIQUE (CEC) LEDGER
Strength: A = peer-reviewed/regulatory primary; B = official report/regulator decision; C = survey/industry/self-reported.
| # | Claim | Slide | Evidence | Strength | Critique to state | Counter-view / rebuttal |
|---|---|---|---|---|---|---|
| 1 | Consumers report high concern about company data use | 2 | Pew Research Center (2019) `[V]`; Cisco Data Privacy Benchmark `[V]` | C | Self-reported; US-heavy; industry survey | Behavioural evidence (#2) qualifies it |
| 2 | Stated concern ≠ behaviour (privacy paradox); consent fatigue | 2, 6 | Kokolakis (2017); Acquisti et al. (2015) | A | Paradox contested | So rely on architecture, not consent |
| 3 | Privacy-by-design principles (proactive, embedded, default) | 3 | Cavoukian (2011) | B | Principles, not tests | Make testable via KPIs |
| 4 | Federated learning keeps raw data on device | 3 | McMahan et al. (2017); Kairouz et al. (2021) | A | Gradients can leak; not a full defence | Combine with differential privacy |
| 5 | Differential privacy bounds individual disclosure with a utility cost | 3, 5 | Dwork & Roth (2014) | A | ε trade-off; hard for non-specialists | Set tolerance in pilot |
| 6 | Children's data attracts stricter rules/enforcement | 2, 9 | ICO Age-appropriate design code; UK/EU GDPR (consent age rules); COPPA; UNCRC GC25 (2021) `[V]` | A/B | Jurisdictions differ | Design to strictest standard |
| 7 | Enforcement precedents on children's/user data | 2–4 | ICO v TikTok (2023, £12.7m) `[V]`; Irish DPC v Instagram (2022, €405m) `[V]`; DPC v Meta (2023, €1.2bn) `[V]`; FTC action involving Disney (COPPA) `[V]` | B | Different facts/jurisdictions | Use as ladder of magnitude, not prediction |
| 8 | Theoretical GDPR exposure: up to 4% global turnover | 4 | GDPR Art. 83; Disney FY24 revenue ≈ $91.4bn `[V]` → ≈ $3.7bn theoretical ceiling | A/B | Ceiling, not expected fine | State clearly |
| 9 | Average breach cost | 4 | IBM *Cost of a Data Breach* (2024) `[V]` | C | Vendor report, global average | Benchmark only |
| 10 | Trust has components: ability, benevolence, integrity | 4, 6 | Mayer et al. (1995) | A | Developed for interpersonal/organisational trust | Adapt carefully for brands |
| 11 | Trust as brand equity asset | 4, 8 | Keller (1993) | A | Brand-equity ≠ privacy trust | Use as mechanism |
| 12 | Information privacy concern and procedural fairness shape trust | 6 | Culnan & Armstrong (1999) | A | Pre-streaming era | Principle persists |
| 13 | Privacy as contextual integrity (appropriate flows) | 6, 9 | Nissenbaum (2004) | A | Hard to operationalise | Use flows in Data Passport |
| 14 | Marketing data practices and consumer privacy | 7 | Martin & Murphy (2017) | A | Review | Informs marketing process change |
| 15 | Stakeholder legitimacy & primary stakeholders | 6 | Freeman (1984); Clarkson (1995) | A | Normative vs instrumental debate | Parents are primary on both views |
| 16 | Participation ladder | 6 | Arnstein (1969) | A | Civic context, power-transfer assumption | Aim for "partnership" on controls, "consultation" on business model |
| 17 | Star model alignment | 7 | Galbraith (2002) | B | Descriptive | Used to find misalignments |
| 18 | Culture types and shifts | 7 | Cameron & Quinn (2011) | A | Survey-based, simplification | Use as diagnostic, not label |
| 19 | Change needs both economic (E) and organisational (O) levers | 7 | Beer & Nohria (2000) | A | Prescriptive | Hybrid with phases |
| 20 | Self-efficacy builds via mastery, vicarious, persuasion | 7 | Bandura (1977) | A | Individual-level | Design training around sources |
| 21 | Perceived usefulness/ease predicts adoption of controls | 6 | Davis (1989) | A | Pre-mobile era | Test controls with parent panel |
| 22 | Differentiation strategy; brand-based advantage | 8 | Porter (1985); Kim & Mauborgne (2005) | A/B | Imitable | Sustain through verification & heritage |
| 23 | Scenario planning for uncertainty | 9 | Schoemaker (1995) | A | Subjective | Test recommendations across all four |
| 24 | Surveillance-capitalism critique | 9 | Zuboff (2019) | A (book) | Polemical | Use as contrast, flag as contested |
| 25 | Children's digital rights | 9 | Livingstone & Third (2017); UN CRC GC25 `[V]` | A | Rights framing vs parental authority | Balance best-interests with teen autonomy |
**Rule:** no claim without a row; no `[V]` unresolved at submission.

---

## 5. SLIDE-BY-SLIDE DETAILED SPEC
Format: **Key message · Layout · Inventory · Figure spec · Notes core / depth · Critical move · Q&A shield · Timing · Trap.**
(Every slide ends with the "Parent's view" strip.)

### S1 — Hook and question (0:00–0:30)
- **Key message:** frame the decision as a question about family trust.
- **Layout:** full-bleed title left; right a single visual: a device icon with a small lock boundary (no logos).
- **Inventory:** title "Earn it, show it, keep it: making family trust Disney+'s product"; hook line (one enforcement case/stat `[V]`); the question: *"Should a family's viewing data ever leave the living-room device?"*; SRN · module · date.
- **Notes core:** (1) hook case; (2) the question; (3) one-sentence preview of the answer; (4) route: Earn → Show → Keep.
- **Notes depth:** why hook for a leadership audience; verify the case facts.
- **Parent's view:** "Is my child's viewing private?"
- **Trap:** sensational tone; unverified case; name on slide.

### S2 — Situation–Complication–Answer (0:30–1:05)
- **Key message:** Disney+'s family promise is being squeezed by data needs, regulators and consumer scepticism; privacy-by-architecture is the answer.
- **Layout:** three horizontal bands (S / C / A) + Fig 1 at right.
- **Inventory:**
  - **S:** family brand; global expansion; ad tier and personalisation need data `[V]` Disney report; Hulu/ESPN integration.
  - **C:** (i) regulators target children's data (ICO code; COPPA; GDPR) (ii) consumers worried but click through (privacy paradox) (iii) internal views differ: ops/compliance vs data/marketing (brief; `[IC]`).
  - **A:** PET-based personalisation, proven and verified.
- **Fig 1 spec:** "The trust gap" two-bar comparison: share of consumers concerned about company data use (Pew 2019 `[V]`) vs share of organisations that say customers would not buy without data protection (Cisco `[V]`); caption "Figure 1: … (Source: Pew Research Center, 2019; Cisco, 20XX)". Caveat in notes: different populations; illustrative juxtaposition.
- **Notes core:** why family trust is Disney's asset; why regulators matter; why consent alone fails; the answer.
- **Notes depth:** privacy paradox evidence (Kokolakis 2017; Acquisti et al. 2015); age-of-consent differences; why the brief's creative/data/compliance views make this an organisational problem too.
- **Critical move:** show that *policy and consent can't fix this*, setting up architecture.
- **Q&A shield:** "Is this just compliance?" → no: compliance is the floor; trust is the product.
- **Parent's view:** "Disney is the brand I let my kids use unsupervised."
- **Trap:** a legal essay.

### S3 — The technology: privacy-by-architecture (1:05–1:55)
- **Key message:** PETs let Disney+ personalise without moving raw family viewing data.
- **Layout:** Fig 2 across 65% width; right 3 mapping rows.
- **Fig 2 spec (two panels, same viewer scenario):**
  - **Panel A "Centralised today (typical):"** device → raw viewing events → cloud warehouse → model → recommendations (arrows thick; label "raw data leaves device").
  - **Panel B "Privacy-by-architecture":** device runs a local model; sends **encrypted/noised model updates** (federated learning + differential privacy) → server aggregates → improved global model → back to devices; label "raw data stays on device"; show a **verification box** (independent audit) on the aggregation step. Caption "Figure 2: … (Source: Author, adapted from McMahan et al., 2017; Dwork and Roth, 2014)".
- **Mapping rows:** children's data exposure → minimised by design · regional compliance fragmentation → one strict standard everywhere · consent fatigue → protection that doesn't depend on a click.
- **Notes core:** 3-step mechanism; why start with kids' profiles; how it differs from "consent and policy" and from "data clean rooms".
- **Notes depth:** federated vs on-device inference; ε (privacy budget) in one sentence; device mix (smart TVs, mobiles, consoles, web); household vs profile level; option appraisal (A1): (a) policy+consent platform, (b) clean rooms/tokenisation, (c) PETs; criteria: regulatory risk reduction, trust signal, utility, feasibility, maturity.
- **Critical move:** one-line option appraisal; Cavoukian principle "embedded into design".
- **Q&A shield:** "Is federated learning proven for video recommendation?" → used at scale in keyboards/mobile; video is less mature → hence pilot (Kairouz et al., 2021 `[V]`).
- **Parent's view:** "My child's viewing habits stay on our device."
- **Trap:** deep-dive maths; Silicon Valley jargon without definition.

### S4 — Benefits (1:55–2:35)
- **Key message:** the benefits are avoided loss, trust and simplification; honest about what is measurable.
- **Layout:** Fig 3 left (55%); right three benefit cards with evidence.
- **Fig 3 spec — "Regulatory exposure ladder" (horizontal bars, log-style annotation):** TikTok ICO £12.7m (2023) · Instagram DPC €405m (2022) · Meta DPC €1.2bn (2023) · **Disney theoretical GDPR ceiling ≈ $3.7bn** (4% × ≈ $91.4bn `[V]`). Footnote: currencies not converted/dates differ; ceiling ≠ expectation. Caption "Figure 3: Illustrative regulatory exposure (Source: ICO, 2023; DPC, 2022, 2023; Disney, 20XX; author's calculation)".
- **Benefit cards:** (1) **Lower regulatory & breach exposure** (IBM average breach cost `[V]` as benchmark) · (2) **Trust as brand equity** with families (Keller 1993; Mayer et al. 1995) · (3) **Operational simplification:** one strictest-standard design across markets; fewer data-subject requests to service.
- **Notes core:** each benefit's mechanism; "what must be true".
- **Notes depth:** why not claim revenue uplift (no robust evidence of willingness-to-pay for privacy in streaming; test in pilot); breach-cost benchmark limits; avoided-loss logic and option value.
- **Critical move:** *refuse to over-claim*; promise measurement via Trust Index and family-segment retention in the pilot.
- **Q&A shield:** "Where's the ROI?" → risk-adjusted: exposure avoided + retention in family segment (measured), not guaranteed uplift.
- **Parent's view:** "Fewer places my family's data can go wrong."
- **Trap:** inventing revenue gains.

### S5 — Limitations (1:55→ 2:35 ends; S5 = 2:35–3:20)
- **Key message:** PETs trade accuracy and simplicity for privacy; they are not a complete defence.
- **Layout:** Fig 4 left; Table 1 right (5 rows); verdict band.
- **Fig 4 spec — conceptual "privacy–utility frontier":** x = privacy strength (e.g., decreasing ε), y = recommendation utility; curve falling; mark "centralised baseline", "PET sweet spot (to be found in pilot)", "over-noised". **Label "Conceptual illustration, not empirical data".** Caption "Figure 4: … (Source: Author, adapted from Dwork and Roth, 2014)".
- **Table 1 (limitation → implication):** accuracy loss (ε) → test tolerance · device heterogeneity & compute limits (smart TVs) → phased client support · residual attacks (membership inference/model inversion; Kairouz et al.) → combine with DP + audit · ad measurement/attribution harder → contextual advertising on family profiles · immaturity for video recommendation → pilot gating.
- **Verdict:** "Viable for kids/family profiles first; hybrid for adult profiles."
- **Notes core:** top three limits; why the frontier matters.
- **Notes depth:** score rationale; why PETs still need legal compliance; engineering talent scarcity.
- **Critical move:** insist trust claims remain **verified, not asserted**.
- **Q&A shield:** "What accuracy loss will you accept?" → tolerance set by pilot; fallback hybrid.
- **Parent's view:** "Recommendations may be slightly less spot-on. Worth it?"
- **Trap:** hiding the accuracy cost.

### S6 — The one stakeholder: parents and guardians (3:20–4:30)
- **Key message:** parents hold the consent, the wallet and the veto; their concerns must be addressed with real participation.
- **Layout:** left Table 2; right Fig 5 (Arnstein ladder, adapted).
- **Justification line:** primary stakeholder with legitimacy (legal consent role), power (subscription/profile control) and urgency (child safety) (Freeman, 1984; Clarkson, 1995).
- **Table 2 (concern → evidence → response → metric), 5 rows max:**
  1. *What is collected about my child and who sees it?* → **Family Data Passport** (plain-language flows; Nissenbaum 2004) → % parents reviewing in 60 days.
  2. *Ads and profiling aimed at children* → no behavioural targeting on kids' profiles; contextual only `[V]` current Disney policy → zero-targeting audit.
  3. *Manipulative engagement (autoplay, nudges)* → kids defaults: autoplay off, session summaries → parent-reported satisfaction.
  4. *Controls are confusing / consent fatigue* → safe defaults, two-click controls tested with parent panel (Davis 1989; Acquisti et al. 2015) → control-adoption rate.
  5. *Will privacy make recommendations worse?* → utility-parity commitment tested in pilot → privacy–utility gap.
- **Fig 5 spec:** adapt Arnstein rungs (Informing → Consultation → Placation → Partnership). Show Disney+ today (estimate: informing/consultation) vs target (partnership on controls & scorecard; consultation on business model). Caption "Figure 5: … (Source: Author, adapted from Arnstein, 1969)".
- **Notes core:** why this group; how each response is concrete; panel mechanics (recruited across markets/age bands, rotating, published responses).
- **Notes depth:** Mayer et al. trust dimensions mapped to responses (ability = security/architecture; benevolence = defaults for children; integrity = audit & disclosure); digital confidence for parents (Ofcom parental-confidence data `[V]`; TAM); limits of Arnstein in commercial setting; mention internal groups only as owners.
- **Critical move:** treat the privacy paradox as a design constraint; participation with explicit boundaries.
- **Q&A shield:** "Why not creative teams or marketing?" → AC2 needs one; parents are the binding constraint on trust and the legal gatekeeper; internal teams appear in S7.
- **Parent's view:** "I can see and change what's used, in two clicks."
- **Trap:** developing four stakeholder groups.

### S7 — Organisation, barriers and change (4:30–5:55)
- **Key message:** trust-by-architecture changes strategy, structure, processes, rewards and people — and culture decides whether it sticks.
- **Layout:** Fig 6 Star model (centre, 55%); right: barrier tags + change strip; bottom-left small CVF shift.
- **Fig 6 spec (five points, each "from → to"):**
  - **Strategy:** trust as differentiator, not cost → family-trust KPIs in strategy.
  - **Structure:** compliance as regional gatekeepers → **Trust & Privacy Engineering guild** (privacy engineers + embedded privacy champions in product, marketing, creative ops); dual reporting (product/legal).
  - **Processes:** privacy review at end → **privacy-by-design gates** in the release pipeline; automated DSAR handling; vendor/ad-tech due diligence; single strictest-standard policy.
  - **Rewards:** growth/ad-revenue KPIs → balanced OKRs including trust metrics; marketing KPIs adjusted for kids' profiles.
  - **People:** generalist analytics → privacy engineers, data-protection champions, training.
  - Centre: **Culture (Cameron & Quinn)** — shift from control (compliance-as-policing) + adhocracy (creative) toward **collaborate + create** with trust as shared value. Arrows show **mutual influence**: e.g., *Rewards ↔ Culture* (ad-revenue targets can drive workarounds/shadow data collection), *Processes ↔ Structure*, *Technology constraint → Processes* (on-device limits force marketing analytics redesign).
  Caption "Figure 6: … (Source: Author, adapted from Galbraith, 2002; Cameron and Quinn, 2011)".
- **Barrier tags (with owner of resistance):** ad-revenue pressure (ads/finance) · reliance on centralised analytics (marketing/data science) · device fragmentation & complexity (engineering) · fear of accuracy loss (product) · regional regulatory variance (compliance).
- **Change strip:** **Theory E + O hybrid** (Beer & Nohria, 2000): E = clear financial case on exposure + family retention; O = capability and culture build, phased; **pre-mortem** (Klein, 2007) before pilot; **digital confidence for staff** designed around Bandura's sources — mastery (hands-on PET labs), vicarious (peer demos), persuasion (leader messaging), emotional state (safe-to-fail sandbox); metrics: lab completion, confidence pulse, % releases passing privacy gates first time.
- **Notes core:** walk each Star point once; show two mutual-influence loops; name where resistance comes from.
- **Notes depth:** Star model as alignment test (misalignment predicts failure); CVF diagnostic limits; why E-only (cost-cutting) or O-only (culture) fails (Beer and Nohria); how to defuse ad-revenue resistance (contextual ad products; kids' profiles already low-targeting `[V]`).
- **Critical move:** show misalignment between *Rewards* and *Strategy* as the likeliest failure point.
- **Q&A shield:** "Where is the biggest barrier?" → rewards/ad-revenue incentives, not technology.
- **Parent's view:** "Staff are trained and accountable — not just a policy page."
- **Trap:** listing all five Star points as a textbook definition.

### S8 — Sustained competitive advantage (5:55–6:50)
- **Key message:** trust differentiates only if verified, family-specific and renewed; it is a moving baseline.
- **Layout:** Fig 7 strategy canvas (60%); right ERRC grid (compact) + goals strip.
- **Fig 7 spec — strategy canvas:** x-axis factors: catalogue breadth · franchise appeal · price · personalisation accuracy · **family-safety controls** · **data transparency** · **privacy architecture** · **independent verification**. Lines: Netflix, Amazon Prime Video, Apple TV+, Max, Disney+ today, **Disney+ target**. Scores 1–5 **labelled "author's assessment based on public feature comparison `[V]`"**; evidence compiled in A2. Caption "Figure 7: … (Source: Author, adapted from Kim and Mauborgne, 2005)".
- **ERRC grid:** Eliminate: behavioural profiling of children; dark-pattern consent · Reduce: central raw-data retention; duplicated regional compliance · Raise: transparency, parent control, share of on-device processing, audit independence · Create: Family Data Passport; published trust scorecard; household co-viewing recommendations (privacy-preserving).
- **Goals strip:** agility → modular PET pipeline & quarterly privacy reviews · innovation → new household-level discovery features · retention → family-segment loyalty (Trust Index linked).
- **Theory:** Porter (1985) differentiation; Keller (1993): "safe for families" brand association as asset.
- **Notes core:** why differentiation here; how verification prevents "privacy-washing"; how to renew (maturity model: Ad hoc → Defined → Measured → Optimised; annual external audit; horizon scan of rules).
- **Notes depth:** counter-argument — rivals can adopt PETs and consumers trade privacy for convenience (Kokolakis, 2017); rebuttal — parents of children are a distinct, higher-stakes segment, heritage + verification are harder to copy than code, and trust becomes a *hygiene factor* if the regulatory floor rises → hence keep exceeding it.
- **Critical move:** concede trust may become table stakes; argue advantage lies in *staying ahead* and *proving it*.
- **Q&A shield:** "Do families really switch for privacy?" → evidence is mixed; we treat it as retention/protection first, differentiator second; pilot tests it.
- **Parent's view:** "Disney+ shows its proof; others just promise."
- **Trap:** unsupported canvas scores.

### S9 — Ethics, social implications and futures (6:50–7:45)
- **Key message:** the ethical stakes are tensions to manage; strategy must hold across plausible futures.
- **Layout:** left Table 3 (ethics tensions); right Fig 8 scenario 2×2.
- **Table 3 (tension → mitigation → KPI/owner), 5 rows:**
  1. *Children's best interests vs commercial interest* (UNCRC GC25; ICO code) → best-interests assessment in design gate → audit pass.
  2. *Inclusion vs privacy:* noise can reduce discovery of niche/minority-language content → coverage/diversity guardrail → diversity-of-exposure index.
  3. *Parental control vs teen autonomy* (Livingstone & Third, 2017) → age-tiered controls; teen-visible transparency → satisfaction by age band.
  4. *Privacy-washing:* claims outrun reality → independent audit; publish scorecard incl. failures → critical findings = 0.
  5. *Environmental/social cost of on-device compute* → efficiency targets; measure energy `[V]`.
  Frame with Nissenbaum (2004): data flows must match context norms; contrast with Zuboff (2019) surveillance model.
- **Fig 8 spec:** axes — Regulatory stringency (loose → strict) × Consumer privacy salience (low → high). Scenarios: **Compliance baseline** (strict/low) · **Trust premium** (strict/high) · **Wild frontier** (loose/low) · **Consumer-led trust** (loose/high). Under each: what the recommendations deliver; show **no-regret moves** valid in all four (data minimisation, audit, parent controls). Caption "Figure 8: … (Source: Author, adapted from Schoemaker, 1995)".
- **Notes core:** two sharpest tensions (inclusion; privacy-washing); why scenarios; which moves are no-regret.
- **Notes depth:** regulatory pointers with limits (GDPR consent ages, COPPA <13, UK GDPR 13; AI Act mostly outside recommenders `[V]`); residual-risk table link to A3.
- **Critical move:** ethics as design constraint with *costs admitted* (accuracy, engagement).
- **Q&A shield:** "Is this ethics theatre?" → independent audit and published failures are the counter.
- **Parent's view:** "Rules for teens differ from rules for toddlers."
- **Trap:** ethics checklist.

### S10 — Three recommendations (7:45–8:45)
- **Key message:** Earn, Show, Keep — sequenced, gated, accountable.
- **Layout:** Table 4 top; Fig 9 monthly Gantt bottom.
- **Table 4:** see §6 (summary row per rec: action · owner · evidence · KPI · gate).
- **Notes core:** why this order; what is approved now; fallback.
- **Notes depth:** cost shape (three buckets: platform/engineering; assurance/legal/audit; people/training) with ranges validated M1–3; no invented figures; dependencies; why not "buy a consent platform only".
- **Parent's view:** "First changes land on kids' profiles within the year."
- **Trap:** recommendations that could apply to any company.

### S11 — Conclusion (8:45–9:15)
- Three insights: (1) trust must be architected, not asserted; (2) it is won through participation and verification; (3) it is a moving baseline, kept through incentives and capability. **Decision requested:** approve R1 pilot funding; appoint an accountable executive owner for trust; reconvene at M4. No new information.

### S12 — References (not presented)
### APPENDIX (information only; do not hide core analysis here)
- **A1:** PET primer (one-page glossary: federated learning, differential privacy, ε, on-device inference, membership inference) + option appraisal scoring table.
- **A2:** Regulatory matrix by market (UK, EU, US, selected others `[V]`) + competitor evidence table behind Fig 7 + KPI definitions.
- **A3:** Detailed 18-month roadmap + Trust Scorecard template + full risk register (§7).
- *Separate:* AI-use evidence (prompts/responses) as the cover sheet requires.

---

## 6. RECOMMENDATION CARDS

### R1 — EARN: Privacy-by-Architecture Standard and PET pilot (M1–10, scale M10–18)
- **What:** adopt a company-wide standard (data minimisation, on-device by default for kids' and family profiles, strictest-law-applies); pilot on-device/federated personalisation for **kids' profiles** in two contrasting regimes (e.g., one UK/EU, one US/COPPA); hybrid fallback (pseudonymised, short retention, DP) for adult profiles.
- **Owner:** CTO (accountable), Chief Privacy Officer (assurance).
- **Evidence:** McMahan et al. (2017); Kairouz et al. (2021); Dwork & Roth (2014); Cavoukian (2011); ICO code `[V]`.
- **KPIs:** on-device share of kids'-profile recommendation impressions; data-minimisation ratio (personal data fields leaving device per active profile vs baseline); **privacy–utility gap** (relative difference in a pre-registered engagement metric, PET vs centralised control; tolerance set in M1–3).
- **Gate (M10):** gap within tolerance · zero critical audit findings · no unresolved regulatory finding · device coverage ≥ agreed threshold → go/no-go. **Kill-switch:** critical finding on kids' profiles pauses rollout. **Fallback:** hybrid approach.
- **Risks:** device fragmentation → phased client support; accuracy loss → ε tuning, hybrid; talent scarcity → partnerships.
- **Why not alternative:** consent-and-policy tooling alone leaves raw children's data centralised.

### R2 — SHOW: Family Trust Layer (M6–18)
- **What:** (a) **Family Data Passport** (plain-language, per-profile flows); (b) **Parent Advisory Panel** at Arnstein "partnership" on controls/scorecard (recruited across markets & age bands; published responses); (c) **independent audit** annually + **published Trust Scorecard** including failures; (d) safe defaults for kids.
- **Owner:** Chief Product Officer + Chief Marketing Officer (shared), CPO for audit.
- **Evidence:** Nissenbaum (2004); Arnstein (1969); Mayer et al. (1995); Culnan & Armstrong (1999); Davis (1989).
- **KPIs:** **Trust Index** (quarterly parent survey; mean of ability, benevolence, integrity items, 1–7); Passport review rate in 60 days; control-adoption rate; panel recommendations adopted or answered with rationale (%); critical audit findings = 0.
- **Gate:** Trust Index above baseline by M12 *and* no scorecard-publication reversal.
- **Risks:** privacy-washing perception → publish failures; low parent adoption → usability testing; legal caution → pre-agreed disclosure rules.
- **Why not alternative:** a privacy notice update is consent theatre (Acquisti et al., 2015).

### R3 — KEEP: Trust & Privacy Engineering operating model (M1–18, then standing)
- **What:** guild structure with privacy champions embedded in product, marketing and creative ops; privacy-by-design release gates; balanced OKRs (trust metrics for product/marketing); 3-tier capability programme (Aware / Practitioner / Fluent) built on Bandura's sources; annual maturity assessment.
- **Owner:** CHRO + Chief Privacy Officer + Head of Product Engineering.
- **Evidence:** Galbraith (2002); Cameron & Quinn (2011); Beer & Nohria (2000); Bandura (1977); Martin & Murphy (2017).
- **KPIs:** % releases passing privacy gate first time; DSAR fulfilment time; confidence pulse by tier; maturity score; share of OKRs with trust metrics.
- **Risks:** rewards misaligned with ad revenue → exec sponsorship + contextual ad roadmap; change fatigue → sequence with pilot waves.
- **Why not alternative:** a central compliance team without incentive change reproduces the control-vs-growth conflict.

---

## 7. ROADMAP (Fig 9) — monthly grid, 18 months
Phases: **Assure (M1–4)** → **Architect (M3–10)** → **Assert (M9–18)**. ◆ = gate.
| Workstream | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 | M11 | M12 | M13 | M14 | M15 | M16 | M17 | M18 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Data audit, DPIA, baseline Trust Index | █ | █ | █ | █ | | | | | | | | | | | | | | |
| Strictest-standard policy & tolerance setting | █ | █ | █ | | | | | | | | | | | | | | | |
| PET pipeline & device clients (R1) | | | █ | █ | █ | █ | █ | █ | █ | | | | | | | | | |
| Kids'-profile pilot, 2 regimes (R1) | | | | | | █ | █ | █ | █ | █ | | | | | | | | |
| ◆ Gate 1: scale go/no-go | | | | | | | | | | ◆ | | | | | | | | |
| Scale to family/adult profiles (hybrid fallback) | | | | | | | | | | | █ | █ | █ | █ | █ | █ | █ | █ |
| Parent Advisory Panel set-up & cycles (R2) | | | | | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ |
| Family Data Passport build & launch (R2) | | | | | | | █ | █ | █ | █ | █ | ◆ | | | | | | |
| Independent audit + first Trust Scorecard (R2) | | | | | | | | | | | █ | █ | █ | ◆ | | | | |
| Guild, release gates, OKR redesign (R3) | █ | █ | █ | █ | █ | █ | | | | | | | | | | | | |
| Capability programme (3 tiers) (R3) | | | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ | █ |
| Maturity assessment & horizon-scan review | | | | | | | | | | | | ◆ | | | | | | ◆ |
Build spec: PowerPoint shapes/Excel stacked bar; colour by Earn (plum) / Show (amber) / Keep (charcoal); caption "Figure 9: 18-month roadmap (Source: Author)"; ≥14pt labels; export at 2× resolution; alt-text; gate criteria in notes/A3. M4 check-in (decision to leadership in S11).

### Risk register (for A3; summarise as a tag on S5/S9)
| ID | Risk | L | I | Mitigation | Residual |
|---|---|---|---|---|---|
| 1 | Privacy–utility degradation hurts engagement | 3 | 4 | Tolerance in pilot; hybrid fallback | L2/I3 |
| 2 | Ad-revenue/incentive resistance | 4 | 4 | Contextual ad roadmap; OKR redesign; exec sponsor | L3/I3 |
| 3 | Device fragmentation/engineering complexity | 4 | 3 | Phased client support; partnerships | L3/I3 |
| 4 | Privacy-washing perception | 3 | 5 | Independent audit; publish failures | L2/I4 |
| 5 | Residual attacks (inversion/re-identification) | 2 | 5 | DP + secure aggregation + red-teaming | L2/I4 |
| 6 | Regulatory divergence across markets | 4 | 3 | Strictest standard; regional champions | L3/I3 |
| 7 | Low parent adoption of controls / consent fatigue | 4 | 2 | Safe defaults; usability tests | L2/I2 |

---

## 8. VIVA / Q&A BANK (answer in 2–3 sentences)
1. Explain federated learning and differential privacy simply. What is ε?
2. Why PETs rather than strong policy and consent?
3. Can federated learning be attacked? (membership inference, model inversion) How do you mitigate?
4. Will it run on smart TVs, consoles, mobiles? What if not?
5. What accuracy loss is acceptable and who decides?
6. Why start with kids' profiles?
7. What is the privacy paradox and how does it shape the design?
8. Why parents rather than creative teams or marketing?
9. What does Arnstein's ladder add? What are its limits here?
10. Why the Star model over other models? What does misalignment look like?
11. How does the Competing Values Framework apply, and is it too simplistic?
12. What is Theory E vs Theory O and why hybrid?
13. How do you build digital confidence (Bandura) for engineers and for parents?
14. How would you measure trust? Why Mayer et al.? Limitations?
15. How could you stop privacy-washing?
16. How does the ad tier interact with your strategy and revenue?
17. Would rivals copy this? Is trust only table stakes?
18. What does GDPR say about children's consent and automated profiling? What is the age threshold in the UK/EU/US? `[V]`
19. Which numbers are theoretical vs expected (exposure ladder)?
20. What would make you recommend against scaling at the gate?
21. What are the scenarios, and which recommendations survive all four?
22. What are the environmental and inclusion costs?

---

## 9. VIDEO RUN SHEET (Teams; display name = SRN)
| Time | Slide | Prompts (not script) | Show |
|---|---|---|---|
| 0:00 | 1 | hook; question; route | title |
| 0:30 | 2 | S–C–A in 35s | Fig 1 |
| 1:05 | 3 | mechanism; why kids first; option appraisal line | Fig 2 |
| 1:55 | 4 | three benefits; ceiling vs expectation; honest about ROI | Fig 3 |
| 2:35 | 5 | accuracy cost; residual attacks; verdict | Fig 4, Table 1 |
| 3:20 | 6 | why parents; five concerns→responses; partnership | Table 2, Fig 5 |
| 4:30 | 7 | Star model; misalignment; barriers; E/O; confidence | Fig 6 |
| 5:55 | 8 | canvas; ERRC; concede table stakes; stay ahead | Fig 7 |
| 6:50 | 9 | ethics tensions; scenarios; no-regret moves | Table 3, Fig 8 |
| 7:45 | 10 | Earn–Show–Keep; gate; approve now | Table 4, Fig 9 |
| 8:45 | 11 | three insights; ask | conclusion |
| 9:15 | – | stop; ≤9:45 | – |
Delivery: calm, evidence-led, parent-centred; pause after each "Parent's view"; trim S2/S3 first if over.

---

## 10. WORD AND TIME BUDGET (B's own)
Speaking rate ~140 wpm; target video 9:15–9:45.
| Slide | AC | Speak | Spoken words | On-slide cap | Notes cap | Actual on-slide | Actual notes |
|---|---|---|---|---|---|---|---|
| 1 | Hook | 0:30 | 70 | 30 | 80 | | |
| 2 | AC1 | 0:35 | 80 | 55 | 110 | | |
| 3 | AC1 | 0:50 | 115 | 50 | 150 | | |
| 4 | AC1 | 0:40 | 95 | 50 | 125 | | |
| 5 | AC1 | 0:45 | 105 | 55 | 140 | | |
| 6 | AC2 | 1:10 | 165 | 65 | 215 | | |
| 7 | AC2 | 1:25 | 200 | 60 | 260 | | |
| 8 | AC3 | 0:55 | 130 | 55 | 170 | | |
| 9 | AC3 | 0:55 | 130 | 60 | 170 | | |
| 10 | AC3 | 1:00 | 140 | 65 | 185 | | |
| 11 | – | 0:30 | 70 | 50 | 90 | | |
| **Total** | | **9:15** | **~1,300** | **595** | **1,695** | | |
- Counted words ≈ **2,290** (slide text + notes); hard cap **3,000**; state true count on cover sheet (excl. contents, references, appendices). Do not pad to 3,500.
- Notes: ~75% core talking points, ~25% depth (caveats, calculations, counter-arguments, source critique). Bullets, not scripts.
- Weight check: AC1 (S1–S5) 3:20 ≈ 36%; AC2 (S6–S7) 2:35 ≈ 28%; AC3 (S8–S10) 2:50 ≈ 31%; close 0:30. If long, trim S2–S3 first.

---

## 11. DESIGN SYSTEM (B)
- 16:9, one master. Palette: **charcoal (#2B2B33) + plum (#6B2D5C) + amber (#F2A33A)** + off-white; red/green only for risk. No Disney logos/stills.
- Type: one humanist sans (e.g., Segoe UI/Aptos); titles 28–30pt; body ≥18pt; figure labels ≥14pt; sources 10–12pt; references 9–10pt.
- Titles as full-sentence claims (≤2 lines). ≤65 words/slide excluding figure labels.
- **Spine tracker** at top-right (EARN · SHOW · KEEP) with current stage highlighted; **Parent's view** strip at the bottom (italic, amber rule).
- Every figure/table: number + title + "(Source: …)"; alt-text; contrast ≥ 4.5:1; no colour-only meaning.
- After Word export: check notes appear; remove personal metadata (File → Inspect Document).

---

## 12. REFERENCE STARTER LIST (real sources; verify every detail; no overlap with A's academic list)
*Academic / books*
- Acquisti, A., Brandimarte, L. and Loewenstein, G. (2015) 'Privacy and human behavior in the age of information', *Science*, 347(6221), pp. 509–514.
- Arnstein, S.R. (1969) 'A ladder of citizen participation', *Journal of the American Institute of Planners*, 35(4), pp. 216–224.
- Bandura, A. (1977) 'Self-efficacy: toward a unifying theory of behavioral change', *Psychological Review*, 84(2), pp. 191–215.
- Beer, M. and Nohria, N. (2000) 'Cracking the code of change', *Harvard Business Review*, 78(3), pp. 133–141.
- Cameron, K.S. and Quinn, R.E. (2011) *Diagnosing and changing organizational culture*. 3rd edn. San Francisco: Jossey-Bass.
- Cavoukian, A. (2011) *Privacy by design: the 7 foundational principles*. Toronto: Information and Privacy Commissioner of Ontario.
- Clarkson, M.B.E. (1995) 'A stakeholder framework for analyzing and evaluating corporate social performance', *Academy of Management Review*, 20(1), pp. 92–117.
- Culnan, M.J. and Armstrong, P.K. (1999) 'Information privacy concerns, procedural fairness, and impersonal trust', *Organization Science*, 10(1), pp. 104–115.
- Davis, F.D. (1989) 'Perceived usefulness, perceived ease of use, and acceptance of information technology', *MIS Quarterly*, 13(3), pp. 319–340.
- Dwork, C. and Roth, A. (2014) 'The algorithmic foundations of differential privacy', *Foundations and Trends in Theoretical Computer Science*, 9(3–4), pp. 211–407.
- Freeman, R.E. (1984) *Strategic management: a stakeholder approach*. Boston: Pitman.
- Galbraith, J.R. (2002) *Designing organizations: an executive guide to strategy, structure, and process*. San Francisco: Jossey-Bass.
- Kairouz, P. et al. (2021) 'Advances and open problems in federated learning', *Foundations and Trends in Machine Learning*, 14(1–2), pp. 1–210.
- Keller, K.L. (1993) 'Conceptualizing, measuring, and managing customer-based brand equity', *Journal of Marketing*, 57(1), pp. 1–22.
- Kim, W.C. and Mauborgne, R. (2005) *Blue ocean strategy*. Boston: Harvard Business School Press.
- Klein, G. (2007) 'Performing a project premortem', *Harvard Business Review*, 85(9), pp. 18–19.
- Kokolakis, S. (2017) 'Privacy attitudes and privacy behaviour: a review of current research on the privacy paradox phenomenon', *Computers & Security*, 64, pp. 122–134.
- Livingstone, S. and Third, A. (2017) 'Children and young people's rights in the digital age: an emerging agenda', *New Media & Society*, 19(5), pp. 657–670.
- Martin, K.D. and Murphy, P.E. (2017) 'The role of data privacy in marketing', *Journal of the Academy of Marketing Science*, 45(2), pp. 135–155.
- Mayer, R.C., Davis, J.H. and Schoorman, F.D. (1995) 'An integrative model of organizational trust', *Academy of Management Review*, 20(3), pp. 709–734.
- McMahan, H.B. et al. (2017) 'Communication-efficient learning of deep networks from decentralized data', *Proceedings of the 20th International Conference on Artificial Intelligence and Statistics (AISTATS)*, PMLR 54, pp. 1273–1282.
- Nissenbaum, H. (2004) 'Privacy as contextual integrity', *Washington Law Review*, 79(1), pp. 119–158.
- Porter, M.E. (1985) *Competitive advantage: creating and sustaining superior performance*. New York: Free Press.
- Schoemaker, P.J.H. (1995) 'Scenario planning: a tool for strategic thinking', *Sloan Management Review*, 36(2), pp. 25–40.
- Zuboff, S. (2019) *The age of surveillance capitalism*. London: Profile Books.

*Regulatory / company / industry (fetch latest, cite exact documents)*
- Information Commissioner's Office (ICO) *Age-appropriate design code* (Children's code).
- UK GDPR / EU GDPR (Arts. 8, 83 and relevant provisions); US *Children's Online Privacy Protection Act* (COPPA) and FTC rule.
- UN Committee on the Rights of the Child (2021) *General comment No. 25 on children's rights in relation to the digital environment*.
- ICO (2023) monetary penalty notice, TikTok; Irish Data Protection Commission (2022) Instagram decision; DPC (2023) Meta decision `[V]`.
- Federal Trade Commission — action/settlement involving The Walt Disney Company (COPPA) `[V]`.
- The Walt Disney Company (latest) *Annual Report/Form 10-K*; Disney+ privacy and kids' profile policy pages `[V]`.
- Pew Research Center (2019) *Americans and privacy: concerned, confused and feeling lack of control over their personal information* `[V]`.
- Cisco (latest) *Data Privacy Benchmark Study* `[V]`; IBM (2024) *Cost of a Data Breach Report* `[V]`; Ofcom (latest) *Children and parents: media use and attitudes* `[V]`.

---

## 13. SELF-MARKING GRID (score 0–2; ★ must be 2)
| Criterion | Check | Score |
|---|---|---|
| AC1 ★ | One technology (PETs); problem is Disney-specific, not generic privacy | |
| AC1 ★ | Mechanism explained correctly (FL, DP, on-device) and tied to problem | |
| AC1 | Benefits framed honestly (avoided loss/option value), exposure ladder labelled "theoretical ceiling" | |
| AC1 ★ | Limitations real (accuracy, devices, residual attacks) | |
| AC1 | ≥2 academic + ≥2 regulatory/industry sources integrated; conflicts noted | |
| AC2 ★ | Exactly one stakeholder group (parents); concerns specific and managed | |
| AC2 ★ | Structure, culture, processes all explicit; mutual influence shown | |
| AC2 | Barriers tied to owners; E/O hybrid and confidence design evidenced | |
| AC2 | Digital confidence for staff **and** parents | |
| AC3 ★ | Advantage argued conditionally (verification, moving baseline), table-stakes counter acknowledged | |
| AC3 ★ | Ethics integrated into strategy with costs admitted; scenarios used | |
| AC3 ★ | Exactly three recs; owner, KPI, timing, gate, kill-switch, fallback | |
| AS1 | ≤65 words/slide; spine tracker + Parent's view; figures labelled/sourced | |
| AS1 | Notes expand; UK spelling; video 9:15–9:45, not read | |
| AS2 ★ | Two-way citation check; Harvard consistent; no unsourced stats | |
| Admin ★ | Cover sheet complete; SRN only; AI use declared, prompts retained; word count stated; both uploads early | |

---

## 14. WHAT I STILL NEED FROM YOU
1. **[IC] in-class Disney+ material** (folds into S2, S6, S7).
2. **Deadline**, and your tutor's answer on how words are counted for slides.
3. Whether your module guide lists LO4/LO5.
4. Next build step: (a) skeleton .pptx with figure shells in B's design system, (b) spreadsheet for the exposure ladder and 18-month Gantt, or (c) review of your own draft against §2 and §13.
