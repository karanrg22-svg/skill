# CW6 — FRAMING C: "ONE DISNEY PLATFORM — UNIFY, RESHAPE, RETIRE" — DETAILED 80+ BLUEPRINT
Companion to `CW6_Disney_Blueprint.md` (admin rules/brief facts). **Independent of** `CW6_Blueprint_A_Detailed.md` and `CW6_Blueprint_B_Detailed.md`: do not mix material between A, B and C.
**Blueprint only.** It specifies what to argue, prove and show. Final wording, diagrams and numbers must be yours (brief: AI only to review a draft/correct language; keep prompts; declare on cover sheet; viva possible).
**Flags:** `[V]` = verify in the primary source before use. `[IC]` = insert in-class Disney+ material (send it to me). Facts from memory may be out of date (today is Nov 2026); Disney's product/organisation changes quickly.

---

## 0. LOCKED DECISIONS
| Decision | Locked choice |
|---|---|
| Technology (AC1: *one*) | **A unified cloud data-and-operations platform**: a shared identity-and-billing spine + lakehouse data foundation with data-mesh (domain-owned) governance + observability/SRE tooling, migrated incrementally ("strangler-fig") |
| Problem (AC1) | **An integration and operating-complexity problem**: Disney+, Hulu and ESPN (plus regional variants) risk running as parallel technology stacks and teams — duplicated systems, inconsistent customer/content data, uneven reliability, and compliance managed region-by-region — slowing launches, bundling and decisions, and raising cost-to-serve |
| Stakeholder (AC2: *one*) | **Operations and compliance teams** (platform reliability/SRE, content operations, customer support, regional compliance) — the group the brief names as focused on "platform reliability, data protection, regulatory compliance and supporting employees across international markets" |
| Thesis | Unification is **an organisational redesign enabled by technology, not an IT migration**: the platform only creates **sustained** advantage if architecture, team structure, decision rights and culture are changed *together*, because "organisations ship their org chart" (Conway) |
| Spine | **UNIFY** (R1: one account, one data truth) → **RESHAPE** (R2: operating model, decision rights, people) → **RETIRE** (R3: decommission legacy and reinvest savings) |
| Length | 12 slides (11 content + references) + 3 appendix; video ≈ 9:15 (≤ 9:45) |

---

## 1. DIFFERENCE MATRIX vs A AND B
| Dimension | A | B | **C (this file)** |
|---|---|---|---|
| Core problem | Churn + creative/data misalignment | Family trust & regulatory exposure | **Integration & operating complexity across brands/markets** |
| Technology | ML recommender + editorial layer | PETs (federated/on-device, DP) | **Unified cloud data platform (identity-billing spine, lakehouse, data mesh, SRE/observability)** |
| Stakeholder | Creative teams | Parents/guardians | **Operations & compliance teams** |
| Thesis type | Resource-based/capability | Differentiation via verified trust | **Socio-technical redesign: architecture = organisation** |
| Adoption/relevance lens (AC1) | Porter forces; Davenport & Ronanki | Cavoukian PbD; privacy paradox | **TOE framework (Tornatzky & Fleischer); DeLone & McLean; Ross–Weill–Robertson operating models** |
| Org-impact theory | Leavitt; Schein | Galbraith Star; Cameron & Quinn | **Conway's Law + Team Topologies; Weill & Ross decision rights; Westrum culture typology** |
| Stakeholder theory | Mendelow; Mitchell | Freeman; Clarkson; Arnstein | **Hirschman exit–voice–loyalty; decision-rights input/veto; Oreg on resistance** |
| Change & digital confidence | Kotter(critique), ADKAR, Edmondson | Beer & Nohria, Bandura, TAM | **Armenakis & Harris change message; Colquitt procedural justice; DigComp 2.1; communities of practice; chaos "game days"** |
| Advantage theory | VRIN; dynamic capabilities | Porter 1985; Keller; Blue Ocean | **Digital options & agility; economies of scope; ambidexterity; three horizons** |
| Ethics/risk lens | Floridi principles; heat map | Contextual integrity; UNCRC; scenarios | **Fair process (workforce), data sovereignty, concentration/cyber risk (NIST CSF 2.0), cloud sustainability; FMEA with RPN** |
| Foresight tool | Sense–Seize–Transform | Scenario 2×2 | **Three Horizons + decision-trigger signposts** |
| Quantification | Churn→lifetime revenue | Regulatory-exposure ladder | **"Nines" downtime arithmetic; DORA benchmarks; payback frontier (% of cost saved per month)** |
| Hero visuals | Flywheel, heat map, Leavitt diamond | Data-flow comparison, exposure ladder, strategy canvas | **Estate map, operating-model 2×2, platform stack, Conway diagram, FMEA bars, wave swimlane** |
| KPIs | Churn Δ, discovery breadth | Trust Index, minimisation ratio | **DORA four, SLO attainment, MTTR, single-customer-view match rate, time-to-launch, legacy decommissioned, cost-to-serve** |
| Roadmap | 8 quarters by workstream | 18 months, monthly | **30 months, swimlanes by market wave (Build → Parallel run → Cutover → Decommission)** |
| Slide-1 style | Answer first | Hook question (SCQA) | **"One customer, three apps" persona journey; diagnosis follows** |
| Slide split (AC2) | S6 org+stakeholder / S7 change | S6 stakeholder / S7 org+change | **S6 org (mutual influence) / S7 stakeholder+barriers+change** |
| Recurring device | Golden-thread phrases | "Parent's view" strip | **"Stack layer" indicator + one "Metric of the slide" chip** |
| Palette | Navy/teal/gold | Charcoal/plum/amber | **Paper off-white + forest green + coral, engineering-grid aesthetic** |
| Academic references | – | no overlap with A | **No overlap with A or B** (only unavoidable law/standard overlap, e.g., GDPR) |
| Viva focus | Strategy/org | Privacy tech/law/trust | **Architecture, reliability engineering, governance, migration** |

---

## 2. 80+ DESCRIPTOR CHECKLIST

### AC1 — Select and Analyse a Relevant Technology (30%)
| 80+ phrase | Slide | On-slide proof | Notes proof | Harsh-marker test |
|---|---|---|---|---|
| "outstanding depth" | 2–5 | Fig 2 operating-model 2×2; Fig 3 platform stack; Fig 4 nines/DORA; FMEA | architecture terms defined at defensible level (lakehouse, data mesh, SLO) | Can the student explain *why each layer exists*? |
| "originality in evaluating the technology" | 2–5 | Reframe: it's an **operating-model** choice (Ross et al.), not "move to cloud" | why platform before personalisation | Is the angle different from "cloud migration benefits"? |
| "integrates multiple high-quality sources" | 2–5 | Academic (Ross; Weill; Armbrust; Sambamurthy) + industry (DORA/Accelerate) + company (Disney 10-K) | triangulation, conflicts (vendor claims vs peer review) | Are vendor sources flagged as such? |
| "exceptional critical insight and synthesis" | 4–5 | Benefits tied to DeLone & McLean dimensions with caveats; payback frontier shows dependence on unknown savings | data-mesh immaturity; "cloud ≠ strategy" | Does the student say when the investment *wouldn't* pay? |
| Problem & why of concern | 1–2 | Persona journey; operating-model diagnosis | brief's "managing people, processes and technology across a global platform" | Disney-specific? |
| Technology introduced; addresses problem | 3 | Fig 3 + problem→capability map | TOE framing | Mechanism, not buzzwords? |
| Benefits & risks | 4–5 | Fig 4; FMEA | scoring rationale | Balanced? |

### AC2 — Assess Organisational and Stakeholder Impacts (30%)
| 80+ phrase | Slide | Proof | Notes proof | Test |
|---|---|---|---|---|
| "outstanding critical evaluation of organisational and stakeholder impacts" | 6–7 | Fig 5 Conway diagram; decision-rights matrix; Westrum shift | worked example of two-way influence | Structure, culture, processes all explicit? |
| "innovative, evidence-based insights into managing change and digital confidence" | 7 | Armenakis five-belief message; fair-process consolidation; DigComp ladder; game days | evidence per element | Digital confidence concrete? |
| "exceptional synthesis of theory and practice" | 6–7 | Each theory → named Disney action | examples | Theory applied? |
| ONE stakeholder group; concerns; management | 7 | Ops & compliance; concerns→responses→metric | Hirschman logic | Only one group? |
| Barriers/resistance | 7 | 5 barriers w/ evidence | Oreg dispositions | Evidence-based? |
| Change management & digital confidence | 7 | Change message + ladder + metrics | measures | Measurable? |

### AC3 — Evaluate Strategic Implications and Make Recommendations (30%)
| 80+ phrase | Slide | Proof | Notes proof | Test |
|---|---|---|---|---|
| "integrates strategic theory, ethics, and innovation" | 8–9 | digital-options chain; ambidexterity; fair process & sovereignty tied to strategy | link sentences | One argument, not three? |
| "original, feasible, grounded in deep critical reasoning" | 10 | wave plan, parity gate, rollback, savings reinvestment rule | why-not alternatives | Feasible given tentpole-event risk? |
| "exceptional strategic foresight" | 9 | Three Horizons + decision triggers | signposts | Forward-looking & testable? |
| Supports agility/innovation/retention | 8 | goal→mechanism→KPI | — | Evidenced? |
| Sustain via continuous improvement | 8 | SLO/error-budget loop; quarterly architecture review; DORA trend | cadence | Concrete? |
| Ethics/risk + mitigation | 9 | table + FMEA residuals | NIST, fair process | Owner + KPI? |
| Exactly **three** recs | 10 | Table 4 | evidence per rec | Exactly 3? |

### AS1 / AS2
| 80+ phrase | Proof |
|---|---|
| "exceptional professionalism and creativity" | original technical diagrams in one visual language; stack-layer indicator |
| "cohesive" | UNIFY–RESHAPE–RETIRE tag from S3 onward; metric chip per slide |
| "visually outstanding" | ≤65 words/slide; one hero visual |
| "academically rigorous" | critique tag per theory; vendor-source flags |
| "well-crafted notes that expand" | core + depth bullets |
| AS2 "precise, full, appropriate" | two-way citation check; sourced figures |

---

## 3. SPINE AND SIGNPOSTING
**S1 Persona → S2 Diagnosis → S3 Platform → S4 Benefits → S5 Limits → S6 Organisation (two-way) → S7 Ops & compliance teams, barriers, change → S8 Advantage → S9 Ethics, risk & horizons → S10 Decisions → S11 Ask**
Tags: **UNIFY** (S3–S5, R1) · **RESHAPE** (S6–S7, R2) · **RETIRE** (S8–S10, R3).
Three phrases: **"platform before personalisation"**, **"reliability is a feature"**, **"the org chart is the architecture"**.
Transition formula: *Operating problem → mechanism → metric → "which depends on people, so…"*.
**Recurring devices (counted in words):** (i) a four-layer **stack indicator** at right (Experience · Data · Identity & Billing · Infrastructure & Operations) highlighting the layer discussed; (ii) a **"Metric of the slide"** chip at top-right (one KPI, ≤6 words).

---

## 4. CLAIM–EVIDENCE–CRITIQUE (CEC) LEDGER
Strength: A = peer-reviewed/regulatory; B = official/company/primary practitioner standard; C = vendor/consultancy/self-reported.
| # | Claim | Slide | Evidence | Strength | Critique to state | Counter-view / rebuttal |
|---|---|---|---|---|---|---|
| 1 | Disney+ operates alongside Hulu/ESPN; integration in selected markets (brief) | 1–2 | Brief; Disney reports `[V]`; `[IC]` | B | Company framing | Use brief as anchor |
| 2 | Disney Streaming technology lineage (BAMTech acquisition) and 2025–26 product consolidation (ESPN DTC; Hulu in Disney+ app) | 2 | Disney announcements `[V]` | B | Dates/details change | Verify before citing; omit if unverifiable |
| 3 | Launch-period reliability incidents (Nov 2019) show operational risk | 2, 4 | Press/Disney statements `[V]` | C | Journalistic | Use sparingly as illustration |
| 4 | Technology adoption depends on technology, organisation, environment contexts | 2–3 | Tornatzky & Fleischer (1990) | A | Broad, descriptive | Structure the analysis only |
| 5 | Operating-model choice (diversification/coordination/replication/unification) drives IT/process standardisation | 2 | Ross, Weill & Robertson (2006) | A/B | Practitioner-oriented, case-based | Use as diagnostic lens |
| 6 | IS success dimensions: system, information, service quality, use, satisfaction, net benefits | 4 | DeLone & McLean (2003) | A | Needs context-specific measures | Map to KPIs |
| 7 | Lakehouse unifies warehouse & lake architectures | 3 | Armbrust et al. (2021) | A | Vendor-authored (Databricks team) → flag | Treat as architecture description, not proof of ROI |
| 8 | Data mesh: domain ownership, data-as-product, federated governance | 3, 7 | Dehghani (2022) | B | Practitioner book; limited empirical evidence | Pilot; require data contracts |
| 9 | Poor data quality is costly | 4 | Redman (2016) `[V]`; Gartner estimates `[V]` | C | Extrapolated/cited widely; avoid "1-10-100 rule" folklore | Quote cautiously; measure internally |
| 10 | Big-data/analytics capability and decision quality | 4 | McAfee & Brynjolfsson (2012) | A | Pre-cloud-lakehouse era | Principle persists |
| 11 | Delivery performance (deploy frequency, lead time, change failure rate, time to restore) correlates with organisational performance | 4, 7, 8 | Forsgren, Humble & Kim (2018); DORA reports `[V]` | A/B | Survey-based; correlation | Use as measurement frame |
| 12 | Reliability engineering practice: SLOs, error budgets, toil | 3–4, 7 | Beyer et al. (2016) | B | Google context | Adapt scale |
| 13 | Availability arithmetic ("nines") | 4 | Own calculation | – | Simplified: ignores partial degradation | Use playback-start success SLO |
| 14 | Conway's Law: system structure mirrors communication structure | 6 | Conway (1968); Skelton & Pais (2019) | A/B | Observational | Use "inverse Conway" as design lever |
| 15 | Decision rights determine IT governance effectiveness | 6 | Weill & Ross (2004) | A/B | Large-firm survey | Apply to data standards |
| 16 | Culture typology predicts information flow and safety | 6 | Westrum (2004); Forsgren et al. (2018) | A | Measurement by survey | Use Westrum survey pulse |
| 17 | Resistance patterns/dispositions | 7 | Oreg (2003) | A | Individual-level | Use with Hirschman |
| 18 | Exit, voice, loyalty as responses to decline/discontent | 7 | Hirschman (1970) | A | Not tech-specific | Design voice channels |
| 19 | Change message beliefs: discrepancy, appropriateness, efficacy, principal support, personal valence | 7 | Armenakis & Harris (2002) | A | Conceptual | Use as message checklist |
| 20 | Procedural/interactional justice in change | 7, 9 | Colquitt (2001) | A | Scale-development paper | Apply as design principles |
| 21 | Digital competence areas | 7 | Carretero, Vuorikari & Punie (2017) | B | Citizen-focused framework | Adapt to professional roles |
| 22 | Communities of practice build shared knowledge | 7 | Wenger (1998) | A | Conceptual | Support, don't over-engineer |
| 23 | Chaos engineering builds confidence in resilience | 7 | Basiri et al. (2016) | A/B | Netflix-originated | Use "game days" in controlled form |
| 24 | Digital options create agility | 8 | Sambamurthy, Bharadwaj & Grover (2003) | A | Conceptual; survey | Pair with KPI time-to-launch |
| 25 | Economies of scope: shared costs across products | 8 | Panzar & Willig (1981) | A | Cost-theory; requires actual shared inputs | Show what is shared vs differentiated |
| 26 | Ambidexterity: exploit + explore | 8 | O'Reilly & Tushman (2004) | A | Case-based | Structural separation via platform/product teams |
| 27 | Three Horizons growth model | 9 | Baghai, Coley & White (1999) | B | Consultancy framework | Use for sequencing only |
| 28 | Cybersecurity risk management | 9 | NIST *Cybersecurity Framework 2.0* (2024) | B | Voluntary framework | Map controls |
| 29 | Cross-border data-transfer rules | 9 | GDPR Ch. V; India DPDP Act 2023 `[V]` | A | Evolving | Regional compliance owners |
| 30 | High-reliability organisation principles | 6–7 | Weick & Sutcliffe (2007) | A | Different industries | Translate to streaming ops |
**Rule:** no claim without a row; no `[V]` unresolved at submission.

---

## 5. SLIDE-BY-SLIDE DETAILED SPEC
Format: **Key message · Layout · Inventory · Figure spec · Notes core/depth · Critical move · Q&A shield · Timing · Trap.** (Every slide has the stack indicator + metric chip.)

### S1 — One customer, three apps (0:00–0:25)
- **Key message:** the customer experiences our organisation chart.
- **Layout:** left title; right a three-panel **persona journey strip** (one family: sign-up → billing → login → find content → get help) across Disney+, Hulu, ESPN, with friction markers. Mark clearly "**Illustrative persona — product details to be verified**" `[V]`.
- **Inventory:** title "One Disney platform: unify, reshape, retire"; one-sentence ask; SRN · module · date.
- **Notes core:** (1) the persona friction; (2) why it matters commercially; (3) thesis: this is an organisational redesign enabled by a platform; (4) route.
- **Notes depth:** disclose persona is illustrative; link to brief's integration with Hulu/ESPN.
- **Metric chip:** "Time to launch a new bundle".
- **Trap:** presenting the persona as fact; name on slide.

### S2 — Diagnosis: operating model (0:25–1:10)
- **Key message:** Disney is straddling operating models; the choice determines what technology is needed.
- **Layout:** Fig 2 (operating-model 2×2) centre; left 3 cited facts; bottom problem statement.
- **Fig 2 spec (Ross, Weill & Robertson, 2006):** x = business-process **standardisation** (low→high); y = business-process **integration** (low→high). Quadrants: **Diversification** (low/low), **Coordination** (low std/high integration), **Replication** (high std/low integration), **Unification** (high/high). Plot "Disney+/Hulu/ESPN today (author's assessment)" in Diversification→Coordination and "Target" in **Coordination-to-Unification for identity, billing and data; Diversification retained for brand/content experience** (nuance: not everything unifies). Caption "Figure 2: … (Source: Author, adapted from Ross, Weill and Robertson, 2006)".
- **Facts:** (a) brief: managing people, processes and technology across a global platform; integrating Hulu and ESPN in selected markets (brief; `[IC]`); (b) product consolidation moves `[V]`; (c) reliability/complexity risks during peak events `[V]`.
- **Problem statement:** "Parallel stacks and regional silos slow launches, fragment data and make reliability and compliance costly."
- **Notes core:** what each operating model implies; why Disney needs *selective* unification; why brand experience stays differentiated.
- **Notes depth:** TOE lens (technology: legacy/ cloud readiness; organisation: structure/skills; environment: regulation, competitors); evidence limits for Disney's internal estate.
- **Critical move:** show that "unify everything" is wrong — unify the *spine*, differentiate the *experience*.
- **Q&A shield:** "Where's your evidence on Disney's current state?" → public statements, brief, in-class material; discovery would validate.
- **Metric chip:** "Standardised spine vs differentiated experience".
- **Trap:** pretending to know internal architecture.

### S3 — The technology: the platform (1:10–1:55)
- **Key message:** four layers; unify the spine, federate the data, engineer reliability.
- **Layout:** Fig 3 platform stack (60%); right 3 problem→capability rows.
- **Fig 3 spec (layers, bottom→top):** (1) **Infrastructure & Operations:** cloud infrastructure, observability, SLOs/error budgets, incident management; (2) **Identity & Billing spine:** one account, entitlements, payments across brands; (3) **Data foundation:** lakehouse + **data-mesh domains** (content metadata, customer, playback, finance) with data contracts, policy-as-code for residency; (4) **Experience layer:** Disney+, Hulu, ESPN apps (differentiated). Right-hand side: **migration approach** — strangler-fig around legacy. Caption "Figure 3: … (Source: Author, adapted from Armbrust et al., 2021; Dehghani, 2022; Ross, Weill and Robertson, 2006)".
- **Mapping rows:** parallel stacks → shared spine · inconsistent data → governed data products · uneven reliability → SLO-driven operations.
- **Notes core:** each layer's purpose in a sentence; why spine first; what stays separate.
- **Notes depth:** lakehouse vs warehouse vs lake; data-mesh principles and maturity warning; SRE concepts (SLI/SLO/error budget); option appraisal (A1): (a) status quo + integration middleware, (b) off-the-shelf CDP only, (c) full re-platform ("big-bang"), (d) **chosen: spine + federated data via strangler-fig**.
- **Critical move:** one-line appraisal with criteria: strategic fit, risk, time-to-value, org-impact.
- **Q&A shield:** "Why not a ready-made customer data platform?" → covers marketing data, not identity/billing/reliability/governance; may be a component.
- **Metric chip:** "SLO attainment".
- **Trap:** vendor-brand soup; "cloud good".

### S4 — Benefits (1:55–2:45)
- **Key message:** reliability, speed and cost are measurable; strategic value depends on organisational change.
- **Layout:** left Fig 4a "Nines" table/bar; centre Fig 4b DORA benchmark; right payback frontier mini-chart.
- **Fig 4a spec:** allowed downtime per month (30.44-day month = 43,834 min): **99.9% → 43.8 min; 99.95% → 21.9 min; 99.99% → 4.4 min**. Caption "Figure 4a: Availability targets and allowed downtime (Source: Author's calculation)". Note: apply to "playback start success", not generic uptime.
- **Fig 4b spec:** four DORA metrics; show elite vs low performer bands as published `[V]` (Forsgren et al., 2018; DORA report year `[V]`). Flag: survey-based association, not causation.
- **Payback frontier (mini):** payback (months) = 100 ÷ s, where s = monthly run-cost saving as % of migration cost: s = 2% → 50; 3% → 33.3; 4% → 25; 5% → 20. Message: "the case depends on s — to be sized in discovery." Caption "Figure 4c: Payback frontier (Source: Author's calculation; illustrative)".
- **DeLone & McLean mapping (tags):** system quality (reliability), information quality (single customer view), service quality (support), use/satisfaction (internal and customer), net benefits (cost-to-serve, time-to-launch).
- **Notes core:** each benefit's mechanism; what's measured.
- **Notes depth:** why "nines" are about error budgets; peak-event load; involuntary churn from payment failures as plausible benefit `[V]` (quantify only with verified data); benefits **not** counted (agility) in payback; data-quality cost claims (Redman; Gartner) are extrapolations.
- **Critical move:** refuse to over-claim; show payback sensitivity and what s must be.
- **Q&A shield:** "Where do the numbers come from?" → arithmetic + published benchmarks; Disney's own inputs come from discovery.
- **Metric chip:** "Change failure rate / MTTR".
- **Trap:** invented dollar savings.

### S5 — Limitations and failure modes (2:45–3:25)
- **Key message:** the platform's biggest risks are migration, concentration and adoption — manage them as failure modes.
- **Layout:** Fig 5 (FMEA horizontal bars: RPN before→after) left; right 3 limitations.
- **Fig 5 spec (FMEA; S, O, D scored 1–10; RPN = S×O×D; author's judgement, defend in notes):**
  | Failure mode | S | O | D | RPN | Mitigation | RPN after |
  |---|---|---|---|---|---|---|
  | Peak-event outage during cutover | 9 | 5 | 5 | 225 | freeze windows around tentpole events; load tests; game days | 81 (9×3×3) |
  | Data-mesh domain non-adoption/quality drift | 6 | 6 | 5 | 180 | data-product owners; contracts; quality SLOs | 54 |
  | Talent attrition/ops fear | 7 | 6 | 4 | 168 | fair process; reskilling | 63 |
  | Vendor lock-in/concentration | 7 | 4 | 6 | 168 | open formats; exit plan | 84 |
  | Regional compliance breach (residency) | 8 | 4 | 5 | 160 | policy-as-code; regional keys | 48 |
  | Single-platform security target | 10 | 3 | 5 | 150 | zero-trust; NIST CSF 2.0 | 60 |
  | Migration data corruption/loss | 9 | 4 | 4 | 144 | parallel run; checksums; rollback | 36 |
  | Cloud cost overrun | 6 | 6 | 4 | 144 | FinOps; unit-cost budgets | 54 |
  Caption "Figure 5: Failure-mode analysis (Source: Author's assessment, method after IEC 60812 `[V]`)".
- **Limitations text:** data mesh immature; platform ≠ strategy; legacy coupling.
- **Notes core:** top three modes; why FMEA (detectability matters in migration).
- **Notes depth:** score rationale; limits of RPN (ordinal multiplication) — acknowledge; verdict: "viable if cutovers avoid tentpole events and parity gates hold".
- **Critical move:** acknowledge RPN's methodological weakness yet use for ranking and track residuals.
- **Q&A shield:** "Who scored this?" → author's judgement; replace with internal incident data in discovery.
- **Metric chip:** "Residual RPN".
- **Trap:** unexplained scores.

### S6 — Organisation: architecture and structure shape each other (4:35 → S6 = 3:25–4:35)
- **Key message:** architecture and organisation are mutually dependent; change both or neither works.
- **Layout:** left Fig 6 Conway diagram; right "decision-rights matrix" + culture shift.
- **Fig 6 spec (two panels):**
  - *Today (illustrative):* team boundaries by brand/region → duplicated services (Conway) with dashed arrows showing hand-offs and tickets.
  - *Target:* **Team Topologies** — stream-aligned teams (per brand/experience) · **platform team** (identity/billing/data/observability) · enabling teams (SRE, data governance, security) · complicated-subsystem team (e.g., playback/streaming pipeline). Show **inverse-Conway** arrow: "design teams to get the architecture you want". Mutual-influence arrows with examples: *Architecture → structure* (shared identity forces a platform team); *Structure → architecture* (regional teams reproduce regional silos).
  Caption "Figure 6: … (Source: Author, adapted from Conway, 1968; Skelton and Pais, 2019)".
- **Decision-rights matrix (Weill & Ross, 2004), compact:** decisions (data standards; identity/billing rules; regional residency; release/rollback; vendor selection) × roles (Input / Decide / Veto). Example: regional compliance **veto** on residency rules; platform team **decides** standards; brand teams **input**.
- **Culture (Westrum, 2004):** shift from *bureaucratic* (ticket hand-offs) toward *generative* (shared responsibility; blameless post-mortems); measurable via survey and DORA.
- **Processes:** release (continuous delivery with automated checks), incident management, change approval (from committee to automated policy), follow-the-sun support.
- **Notes core:** one loop each direction; decision rights; culture shift.
- **Notes depth:** Meyer (2014) cultural-communication differences across markets, with McSweeney (2002) critique of national-culture generalisations; High-reliability principles (Weick & Sutcliffe, 2007): preoccupation with failure, deference to expertise.
- **Critical move:** treat the org chart as a design variable; one group (ops & compliance) is examined deeply in S7.
- **Q&A shield:** "Isn't Conway's Law just anecdote?" → observational; used as design heuristic and tested via DORA metrics.
- **Metric chip:** "Lead time for changes".
- **Trap:** org-chart boxes with no explanation of interdependence.

### S7 — Operations & compliance teams: concerns, barriers, change (4:35–6:00)
- **Key message:** the people who run the platform decide whether unification succeeds; give them voice, fair process and capability.
- **Layout:** left Table 2 (concern → response → metric); centre Fig 7 change/confidence ladder; right barrier tags.
- **Justification line:** on the critical path of every migration wave; hold run-time accountability and regulatory knowledge; high exit cost to Disney (Hirschman, 1970; Weill & Ross, 2004).
- **Table 2 (5 rows):**
  1. *"Central platform ignores local law"* → **regional compliance veto + policy-as-code** → % policies automated; audit findings.
  2. *"We'll be blamed when it breaks / on-call burden"* → blameless post-mortems; error budgets; toil caps → pages per engineer per shift; MTTR.
  3. *"Consolidation means job cuts"* → **fair process** (explain, engage, clarify expectations; Colquitt, 2001); redeployment guarantees → attrition; fairness pulse.
  4. *"Don't break what works"* → parallel run + rollback tested; cutover outside tentpole events → change failure rate.
  5. *"New tools and skills"* → DigComp-aligned reskilling; platform-engineering career ladder → certification/skill coverage.
- **Barriers (with evidence tag):** attachment to local autonomy · fear of job loss · tool overload · regional legal variance · legacy coupling. Oreg (2003) dispositional resistance factors considered (routine-seeking, emotional reaction, short-term focus, cognitive rigidity).
- **Change message (Armenakis & Harris, 2002):** five beliefs — *discrepancy* (why change), *appropriateness* (why this solution), *efficacy* (we can), *principal support* (leaders back it), *personal valence* (what's in it for me).
- **Fig 7 spec — confidence ladder:** DigComp 2.1 areas mapped to three tiers: **Foundations** (information & data literacy, safety) → **Practitioner** (collaboration, problem solving, content/ automation) → **Platform fluent** (design & govern data products; SRE). Rituals: **communities of practice** (Wenger), **game days** (controlled chaos engineering, Basiri et al., 2016) to practise failure safely. Metrics: tier completion; confidence pulse; game-day recovery time. Caption "Figure 7: … (Source: Author, adapted from Carretero, Vuorikari and Punie, 2017)".
- **Voice design (Hirschman):** formal channels — platform council with ops/compliance seats, objection log with response SLA, anonymous pulse; exit risk monitored via attrition.
- **Notes core:** why this group; five concerns with responses; message beliefs; ladder.
- **Notes depth:** Oreg critique (individual vs situational causes); compare against Hirschman — resistance as voice; how to avoid "change theatre"; union/works-council consultation in some markets `[V]`.
- **Critical move:** treat dissent as signal and design channels; make fairness measurable.
- **Q&A shield:** "Why not data analysts or customers?" → AC2 asks one; ops/compliance are named in the brief and are on every critical path.
- **Metric chip:** "Attrition & fairness pulse".
- **Trap:** training slide with no evidence.

### S8 — Sustained competitive advantage (6:00–6:55)
- **Key message:** the platform converts into advantage as digital options and economies of scope — if the organisation can exploit them.
- **Layout:** left Fig 8 chain; right "shared vs differentiated" table; bottom goals strip.
- **Fig 8 spec (Sambamurthy et al., 2003):** capabilities (modular services, shared identity, data products) → **digital options** (launch a bundle; enter a market; test pricing; add sports tier; new partner integration) → **agility** (entrepreneurial & operational) → competitive action → performance. Show **time-to-launch** KPI at the agility node. Caption "Figure 8: … (Source: Author, adapted from Sambamurthy, Bharadwaj and Grover, 2003)".
- **Table "Shared vs differentiated" (Panzar & Willig, 1981):** *Shared:* identity, billing, data foundation, observability, compliance engine · *Differentiated:* brand experience, content, curation, marketing.
- **Ambidexterity (O'Reilly & Tushman, 2004):** reliability (exploit) via platform/SRE; experimentation (explore) via stream-aligned teams; separated structurally, integrated by leadership.
- **Goals strip:** agility → time-to-launch · innovation → experiments/quarter on shared data · retention → fewer billing/login friction events `[V]`.
- **Continuous improvement:** SLO/error-budget review monthly; architecture review quarterly; DORA trend tracked; platform roadmap treated as product backlog.
- **Notes core:** option logic; what's shared; how improvement is institutionalised.
- **Notes depth:** counter-argument — rivals also run on cloud, so no advantage; rebuttal — advantage is **coupling of platform with multi-brand/IP portfolio and the organisation's ability to recombine**, not cloud use; admit that platform parity is likely, and that advantage erodes if teams revert to silos.
- **Critical move:** advantage is conditional on exploitation capability.
- **Q&A shield:** "Is this just cost-cutting?" → cost is a by-product; the strategic value is optionality and speed.
- **Metric chip:** "Time to launch".
- **Trap:** claiming "cloud = advantage".

### S9 — Ethics, social, risk and horizons (6:55–7:45)
- **Key message:** responsible consolidation means fairness to staff, regional sovereignty, security and sustainability — then plan across horizons.
- **Layout:** left Table 3; right Three-Horizons strip with signposts.
- **Table 3 (issue → mitigation → KPI/owner):**
  1. *Workforce fairness* (consolidation, automation) → fair-process commitments; redeployment/reskilling budget; no surprise cuts → fairness pulse; attrition (CHRO).
  2. *Data sovereignty & cross-border transfers* → residency by design; regional keys; transfer assessments (GDPR Ch. V; DPDP `[V]`) → audit findings (Compliance).
  3. *Concentration & cyber risk* (single platform) → zero-trust; segmentation; NIST CSF 2.0 mapping; exit plan → incidents; recovery tests (CISO).
  4. *Environmental footprint of cloud* → carbon-aware workload placement; track SCI (Green Software Foundation) `[V]` → intensity per user-hour (CTO).
  5. *Equity of support across markets* (follow-the-sun, languages) → service-level parity targets → support SLA by market (COO).
- **Three Horizons (Baghai et al., 1999):** **H1 (0–12m)** stabilise & unify spine; **H2 (12–30m)** exploit options (bundles, new markets); **H3 (30m+)** emergent: AIOps, AI-assisted operations, new formats on unified data.
- **Decision-trigger signposts:** e.g., (i) deeper Hulu/ESPN integration timetable `[V]` → accelerate identity wave; (ii) major outage or regulatory change → pause cutovers & re-baseline; (iii) AIOps maturity proof → pilot anomaly detection; (iv) major sports-rights expansion → capacity programme.
- **Notes core:** workforce fairness first; sovereignty; horizons and triggers.
- **Notes depth:** limits of voluntary frameworks; sustainability trade-off (migration emissions vs efficiency gains); linking ethics to strategy (trust of regulators/staff reduces execution risk).
- **Critical move:** ethics as execution risk-management with costs admitted (slower decommissioning to protect people).
- **Q&A shield:** "Is the workforce piece ethics or PR?" → fair process measured by pulse and attrition; commitments binding.
- **Metric chip:** "Fairness pulse".
- **Trap:** ethics checklist with no owner.

### S10 — Three recommendations (7:45–8:50)
- **Key message:** Unify → Reshape → Retire; sequenced by waves and gates.
- **Layout:** Table 4 top; Fig 9 wave swimlane bottom.
- **Table 4:** see §6.
- **Notes core:** why this order; what is approved now; parity gate; rollback.
- **Notes depth:** cost-shape buckets (platform & cloud; people & transition; assurance & dual-running), ranges validated in discovery (no invented figures); why not "big-bang"; why savings ring-fenced.
- **Metric chip:** "Legacy decommissioned".
- **Trap:** generic recommendations.

### S11 — Conclusion (8:50–9:15)
- Three insights: (1) unify the spine, differentiate the experience; (2) the org chart is the architecture; (3) advantage is exploiting options, not owning cloud. **Decision requested:** approve discovery & Wave 0; stand up the platform council with ops/compliance seats; confirm the savings-reinvestment rule; reconvene at M6. No new information.

### S12 — References (not presented). **Appendix:** A1 option appraisal + glossary (lakehouse, data mesh, SLI/SLO, error budget, strangler-fig, policy-as-code) · A2 decision-rights matrix (full) + DigComp mapping + compliance-by-market table `[V]` · A3 detailed wave plan, KPI definitions, FMEA scoring rationale. *Separate:* AI-use evidence per cover sheet.

---

## 6. RECOMMENDATION CARDS

### R1 — UNIFY: one account, one data truth (M1–24)
- **What:** build the identity-and-billing spine and data foundation; migrate by **market waves** using the strangler-fig pattern; data-mesh domains with contracts; observability and SLOs from day one.
- **Owner:** CTO (accountable); Chief Data Officer (data domains).
- **Evidence:** Ross, Weill & Robertson (2006); Armbrust et al. (2021); Dehghani (2022); Beyer et al. (2016); Fowler (2004) `[V]`.
- **KPIs:** SLO attainment (playback-start success; target set in discovery, e.g., 99.95% `[V]` benchmark); MTTR; **single-customer-view match rate** (accounts resolved across brands at agreed confidence); data-quality score per domain; time-to-launch a new bundle (weeks).
- **Gate per wave (parity & stability):** ≥ 30 days at/above SLO in parallel run · zero Sev-1 data-loss · rollback rehearsed · compliance sign-off by regional owner. **Rollback rule:** Sev-1 attributable to migration → revert within agreed RTO.
- **Risks:** tentpole-event outage → cutover freeze windows; lock-in → open formats.
- **Why not alternative:** a CDP alone doesn't fix identity/billing/reliability; big-bang concentrates risk.

### R2 — RESHAPE: operating model, decision rights, people (M1–18, then standing)
- **What:** move to platform/stream-aligned team topology; adopt decision-rights matrix (regional compliance **veto** on residency); SRE with SLOs/error budgets; blameless post-mortems; **fair-process consolidation**; DigComp-aligned reskilling; communities of practice; game days.
- **Owner:** COO (accountable) + CHRO; Chief Compliance Officer for decision rights.
- **Evidence:** Conway (1968); Skelton & Pais (2019); Weill & Ross (2004); Westrum (2004); Colquitt (2001); Armenakis & Harris (2002); Carretero et al. (2017).
- **KPIs:** DORA four (deployment frequency, lead time, change failure rate, time to restore); Westrum survey score; pages per engineer per shift; fairness pulse; attrition among ops/compliance; skill-tier completion.
- **Gate:** at M9 — Westrum score and change-failure rate improving versus baseline; fairness pulse ≥ agreed threshold, else pause consolidation steps.
- **Risks:** attrition/knowledge loss → retention & redeployment; change fatigue → align with wave calendar.
- **Why not alternative:** shipping the platform into the old structure reproduces silos (Conway).

### R3 — RETIRE & REINVEST: decommission legacy, recycle savings (M12–30)
- **What:** enforce **sunset dates** per legacy system after parity gate; track run-cost; **ring-fence a fixed share of verified savings** (proposal: split across resilience, experimentation and people development; split agreed by the platform council) so consolidation funds capability, not only budget cuts; quarterly architecture review; platform scorecard.
- **Owner:** CFO (savings rule) + CTO (decommissioning).
- **Evidence:** Sambamurthy et al. (2003); O'Reilly & Tushman (2004); Panzar & Willig (1981); Forsgren et al. (2018) for scorecard metrics.
- **KPIs:** legacy systems decommissioned vs plan; cost-to-serve per subscriber (definition agreed in discovery); % of verified savings reinvested; experiments launched on shared data; time-to-launch.
- **Gate:** no decommission without parity gate and 30-day dual-run exit criteria.
- **Risks:** zombie systems persist (political) → sunset governance by council; savings diverted → CFO-owned rule.
- **Why not alternative:** without retirement, Disney pays for two worlds and the advantage never materialises.

---

## 7. ROADMAP (Fig 9) — 30 months, swimlanes by market wave
Legend: **B** build · **P** parallel run · **C** cutover · **D** decommission · ◆ gate. Half-year columns (H1 = M1–6 … H5 = M25–30). Freeze windows around tentpole events are overlaid in coral.
| Lane | H1 (M1–6) | H2 (M7–12) | H3 (M13–18) | H4 (M19–24) | H5 (M25–30) |
|---|---|---|---|---|---|
| **Wave 0 — Foundations** (spine, data domains, observability, council) | B B B B B ◆ | P | | | |
| **Wave 1 — First market pair** (e.g., one home market + one regulated market) | | B B P P C ◆ | D | | |
| **Wave 2 — Further regulated markets** | | | B B P P C ◆ | D | |
| **Wave 3 — Major growth markets** | | | | B B P P C ◆ | D |
| **Wave 4 — Remaining markets & partner integrations** | | | | | B P C ◆ D |
| **R2 People & operating model** (topology, decision rights, reskilling, game days) | ██ | ██ | ██ | ░ | ░ |
| **R3 Savings rule & sunset governance** | ░ | ░ | ██ | ██ | ██ |
Gate criteria in A3. Build in PowerPoint shapes/Excel; caption "Figure 9: 30-month wave plan (Source: Author)"; ≥14pt labels; export at 2×; alt-text; shade freeze windows (e.g., around major sports events/premieres `[V]`).

---

## 8. VIVA / Q&A BANK (answer in 2–3 sentences)
1. What is a lakehouse and how does it differ from a warehouse/data lake?
2. What is data mesh and what does "data as a product" mean? What are its limits?
3. Explain SLI, SLO and error budget. Why 99.95% not 100%?
4. Show how you computed allowed downtime.
5. What is the strangler-fig pattern, and why not big-bang?
6. What is Conway's Law and what is the inverse Conway manoeuvre?
7. What are Team Topologies' four team types?
8. Explain Ross et al.'s four operating models; where is Disney today and where should it be?
9. How do TOE and DeLone & McLean shape your argument?
10. What are the DORA metrics, and what are their limitations?
11. Why operations & compliance teams, and not creative or customers?
12. Explain Hirschman's exit, voice and loyalty in this context.
13. What is fair process and how do you measure it?
14. What are Armenakis & Harris's five beliefs? Give an example for each.
15. How would you build digital confidence (DigComp) and what's a game day?
16. How do you manage regional compliance on a global platform?
17. What happens if the pilot wave fails the parity gate?
18. How would you avoid cutovers during major events?
19. Is platform parity possible with rivals — where's the advantage?
20. What is an economy of scope and where does it apply here?
21. Which risks have the highest RPN and why is RPN imperfect?
22. How does your payback frontier work and what would invalidate it?
23. What does NIST CSF 2.0 add? Which controls matter most for a single platform?
24. How would you decide to accelerate or pause (decision triggers)?

---

## 9. VIDEO RUN SHEET (Teams; display name = SRN)
| Time | Slide | Prompts (not script) | Show |
|---|---|---|---|
| 0:00 | 1 | persona friction; thesis; route | journey strip |
| 0:25 | 2 | operating models; unify spine, differentiate experience | Fig 2 |
| 1:10 | 3 | four layers; why spine first; option appraisal line | Fig 3 |
| 1:55 | 4 | nines; DORA; payback depends on s | Fig 4a–c |
| 2:45 | 5 | top failure modes; RPN before→after | Fig 5 |
| 3:25 | 6 | Conway two-way; decision rights; culture | Fig 6 |
| 4:35 | 7 | ops & compliance; fair process; message; ladder | Table 2, Fig 7 |
| 6:00 | 8 | options; shared vs differentiated; conditional advantage | Fig 8 |
| 6:55 | 9 | fairness, sovereignty, cyber, horizons | Table 3 |
| 7:45 | 10 | three recs; waves; gate; savings rule | Table 4, Fig 9 |
| 8:50 | 11 | three insights; ask | conclusion |
| 9:15 | – | stop; ≤9:45 | – |

---

## 10. WORD AND TIME BUDGET (C's own)
~140 wpm; target 9:15 (≤9:45).
| Slide | AC | Speak | Spoken words | On-slide cap | Notes cap | Actual on-slide | Actual notes |
|---|---|---|---|---|---|---|---|
| 1 | Intro | 0:25 | 60 | 35 | 70 | | |
| 2 | AC1 | 0:45 | 105 | 60 | 140 | | |
| 3 | AC1 | 0:45 | 105 | 55 | 140 | | |
| 4 | AC1 | 0:50 | 115 | 55 | 150 | | |
| 5 | AC1 | 0:40 | 95 | 55 | 125 | | |
| 6 | AC2 | 1:10 | 165 | 60 | 215 | | |
| 7 | AC2 | 1:25 | 200 | 65 | 260 | | |
| 8 | AC3 | 0:55 | 130 | 55 | 170 | | |
| 9 | AC3 | 0:50 | 115 | 55 | 150 | | |
| 10 | AC3 | 1:05 | 150 | 70 | 195 | | |
| 11 | – | 0:25 | 60 | 45 | 80 | | |
| **Total** | | **9:15** | **~1,300** | **610** | **1,695** | | |
- Counted words ≈ **2,300** (slide text + notes); hard cap **3,000**; state true count on cover sheet (excl. contents, references, appendices). Do not pad to 3,500.
- Notes ≈ 75% core / 25% depth (calculations, caveats, counters, source critique). Bullets, not scripts.
- Weight check: AC1 (S1–S5) 3:25 ≈ 37%; AC2 (S6–S7) 2:35 ≈ 28%; AC3 (S8–S10) 2:50 ≈ 31%; close 0:25. If over, trim S2–S3 first.

---

## 11. DESIGN SYSTEM (C)
- 16:9; paper off-white (#F7F4EC) background; text ink (#14213D-ish dark); primary **forest green** (#1F5F4A); accent **coral** (#E4572E); neutral greys. Engineering-grid motif, thin rules, mono-spaced figure labels (e.g., Consolas) for technical diagrams; body in one sans (Segoe UI/Aptos).
- Titles 28pt, claim-style; body ≥18pt; labels ≥14pt; source lines 10–12pt; references 9–10pt; ≤65 words/slide excluding labels.
- Persistent **stack indicator** (right edge) and **metric chip** (top-right).
- Every figure/table: number + title + "(Source: …)"; alt-text; contrast ≥ 4.5:1; no colour-only meaning (use hatch/labels).
- Avoid vendor logos; avoid screenshots of internal-looking systems; no Disney logos/stills.
- After Word export: confirm notes present; remove personal metadata.

---

## 12. REFERENCE STARTER LIST (real sources; verify every detail; no overlap with A or B)
*Academic / books / standards*
- Armbrust, M. et al. (2021) 'Lakehouse: a new generation of open platforms that unify data warehousing and advanced analytics', *Proceedings of CIDR 2021*.
- Armenakis, A.A. and Harris, S.G. (2002) 'Crafting a change message to create transformational readiness', *Journal of Organizational Change Management*, 15(2), pp. 169–183.
- Baghai, M., Coley, S. and White, D. (1999) *The alchemy of growth*. London: Orion Business.
- Basiri, A. et al. (2016) 'Chaos engineering', *IEEE Software*, 33(3), pp. 35–41.
- Beyer, B., Jones, C., Petoff, J. and Murphy, N.R. (eds.) (2016) *Site reliability engineering: how Google runs production systems*. Sebastopol: O'Reilly.
- Carretero, S., Vuorikari, R. and Punie, Y. (2017) *DigComp 2.1: the digital competence framework for citizens*. Luxembourg: Publications Office of the European Union.
- Colquitt, J.A. (2001) 'On the dimensionality of organizational justice: a construct validation of a measure', *Journal of Applied Psychology*, 86(3), pp. 386–400.
- Conway, M.E. (1968) 'How do committees invent?', *Datamation*, 14(4), pp. 28–31.
- DeLone, W.H. and McLean, E.R. (2003) 'The DeLone and McLean model of information systems success: a ten-year update', *Journal of Management Information Systems*, 19(4), pp. 9–30.
- Dehghani, Z. (2022) *Data mesh: delivering data-driven value at scale*. Sebastopol: O'Reilly.
- Forsgren, N., Humble, J. and Kim, G. (2018) *Accelerate: the science of lean software and DevOps*. Portland, OR: IT Revolution Press.
- Hirschman, A.O. (1970) *Exit, voice, and loyalty*. Cambridge, MA: Harvard University Press.
- McAfee, A. and Brynjolfsson, E. (2012) 'Big data: the management revolution', *Harvard Business Review*, 90(10), pp. 60–68.
- McSweeney, B. (2002) 'Hofstede's model of national cultural differences and their consequences: a triumph of faith — a failure of analysis', *Human Relations*, 55(1), pp. 89–118.
- Meyer, E. (2014) *The culture map*. New York: PublicAffairs.
- O'Reilly, C.A. and Tushman, M.L. (2004) 'The ambidextrous organization', *Harvard Business Review*, 82(4), pp. 74–81.
- Oreg, S. (2003) 'Resistance to change: developing an individual differences measure', *Journal of Applied Psychology*, 88(4), pp. 680–693.
- Panzar, J.C. and Willig, R.D. (1981) 'Economies of scope', *American Economic Review*, 71(2), pp. 268–272.
- Redman, T.C. (2016) 'Bad data costs the U.S. $3 trillion per year', *Harvard Business Review*, 22 September `[V]`.
- Ross, J.W., Weill, P. and Robertson, D.C. (2006) *Enterprise architecture as strategy*. Boston: Harvard Business School Press.
- Sambamurthy, V., Bharadwaj, A. and Grover, V. (2003) 'Shaping agility through digital options', *MIS Quarterly*, 27(2), pp. 237–263.
- Skelton, M. and Pais, M. (2019) *Team topologies*. Portland, OR: IT Revolution Press.
- Tornatzky, L.G. and Fleischer, M. (1990) *The processes of technological innovation*. Lexington, MA: Lexington Books.
- Weick, K.E. and Sutcliffe, K.M. (2007) *Managing the unexpected*. 2nd edn. San Francisco: Jossey-Bass.
- Weill, P. and Ross, J.W. (2004) *IT governance*. Boston: Harvard Business School Press.
- Wenger, E. (1998) *Communities of practice*. Cambridge: Cambridge University Press.
- Westrum, R. (2004) 'A typology of organisational cultures', *Quality and Safety in Health Care*, 13(suppl 2), pp. ii22–ii27.
- Fowler, M. (2004) 'StranglerFigApplication'. Available at: martinfowler.com `[V URL/date]`.
- IEC 60812 (failure modes and effects analysis) `[V edition]`.
*Regulatory / company / industry (fetch latest)*
- NIST (2024) *Cybersecurity Framework 2.0*.
- GDPR Chapter V (international transfers); India *Digital Personal Data Protection Act 2023* `[V]`.
- The Walt Disney Company (latest) *Annual Report/Form 10-K* and earnings releases (segments, DTC, ESPN, integration announcements) `[V]`.
- Google Cloud / DORA (latest) *Accelerate State of DevOps Report* `[V]`.
- Green Software Foundation, *Software Carbon Intensity (SCI) specification* `[V]`.
- Gartner data-quality cost estimate `[V; flag as consultancy]`.

---

## 13. SELF-MARKING GRID (0–2; ★ must be 2)
| Criterion | Check | Score |
|---|---|---|
| AC1 ★ | One technology (platform); problem Disney-specific; persona labelled illustrative | |
| AC1 ★ | Mechanism clear (layers, mesh, SLO, strangler-fig) and justified by operating-model diagnosis | |
| AC1 | Benefits honest: nines arithmetic, DORA benchmarks flagged as associations, payback depends on s | |
| AC1 ★ | Limitations genuine (FMEA); RPN weakness acknowledged | |
| AC1 | ≥2 academic + ≥2 industry/standards; vendor sources flagged | |
| AC2 ★ | Exactly one stakeholder group (ops & compliance); concerns specific and managed | |
| AC2 ★ | Structure, culture, processes explicit; two-way (Conway) shown | |
| AC2 | Barriers evidenced; change message + fair process + DigComp ladder | |
| AC2 | Digital confidence with measures (tier completion, game-day recovery, confidence pulse) | |
| AC3 ★ | Advantage conditional (options, scope, ambidexterity); platform-parity counter addressed | |
| AC3 ★ | Ethics/risk integrated; workforce fairness and sovereignty owners + KPIs; Three Horizons + triggers | |
| AC3 ★ | Exactly three recs; owner, KPI, wave gates, rollback rule, savings rule | |
| AS1 | ≤65 words/slide; stack indicator + metric chip; figures labelled/sourced | |
| AS1 | Notes expand; UK spelling; video 9:15–9:45, not read | |
| AS2 ★ | Two-way citation check; Harvard consistent; no unsourced stats | |
| Admin ★ | Cover sheet complete; SRN only; AI use declared; prompts retained; word count stated; uploads early | |

---

## 14. WHAT I STILL NEED FROM YOU
1. **[IC] in-class Disney+ material** (folds into S2, S6, S7).
2. **Deadline** and the tutor's answer on word-count method.
3. Whether your module guide lists LO4/LO5.
4. Next build step: (a) skeleton .pptx with figure shells in C's design system, (b) spreadsheet for nines, payback frontier, FMEA and the wave plan, or (c) a review of your own draft against §2 and §13.
