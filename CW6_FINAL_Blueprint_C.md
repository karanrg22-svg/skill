# CW6 — FINAL BLUEPRINT (FRAMING C): "ONE DISNEY PLATFORM — UNIFY, RESHAPE, RETIRE"
**The single working document for C. It follows the brief's recommended structure (Sections 1–5, Slides 1–12) and supersedes the slide specs in `CW6_Blueprint_C_Detailed.md` (keep that file as a reference library). Do not mix material from A, B or D.**
Module: Digital Business and Emerging Technologies (BSc Applied Management, BPP) · Role: Digital Transformation Consultant presenting to the Disney+ leadership team · Deliverables: slide deck + speaker notes (converted to Word) + ≤10-minute Teams video.

> **AI rule.** The brief allows AI only to review a draft or correct language; you must declare it and keep every prompt. This file tells you *what to argue, prove and show*, with **"Answer in your own words" prompts** per slide. **You** write the slide text, notes, figures and numbers. A viva may test any concept, theory, example or source — C uses engineering and governance concepts, so write only what you can explain.
> `[V]` = verify in the primary source (delete the claim if you can't). `[IC]` = insert in-class Disney+ material (the brief allows it).

**What changed from the earlier C file:** (1) **One hero visual per slide** — the first spec put up to three figures on a slide (slide 4) and two tables on slide 6. (2) Slide 5 shows the **top five** failure modes only; the full eight go in the appendix. (3) The decision-rights matrix is cut to three decisions (full matrix in Appendix A2). (4) Every brief bullet is traced to a slide. (5) A production workflow, quality gates and rehearsal plan are added. (6) **C-specific safeguards:** Disney's internal technology isn't public, so the blueprint tells you how to argue from public evidence and label every assumption; and the persona on slide 1 must be labelled *illustrative*.

---

## 1. BRIEF COMPLIANCE MAP

### 1.1 Rules you must not break (tick before every export)
| Rule (from brief) | Done? |
|---|---|
| Assignment Cover Sheet completed and included as page 1 (programme, module, **SRN**, title, date, AI declaration, word count) | ☐ |
| **SRN only** — no name/email anywhere (slides, notes, file name, file properties, Teams display name, video) | ☐ |
| Submission 1: deck + speaker notes **converted to Word**; Submission 2: **Teams** video ≤ 10:00; via the online submission points | ☐ |
| ~10–12 slides + **up to 3 appendix slides** (information only, not presented) | ☐ |
| Reference list (alphabetical, **Harvard**) at the end of the pack — not presented orally | ☐ |
| Word limit **≤ 3,500** (plan ≈ 2,300; hard cap 3,000); state true count on cover sheet (excl. contents, bibliography, appendices) | ☐ |
| AI use (if any) declared; prompts/responses retained and attached | ☐ |
| Submitted **before** the deadline (late = not marked) | ☐ |
| Tutor email sent: *"Does the 3,500-word limit apply to slide text + notes combined, excluding references and appendices?"* | ☐ |

### 1.2 Brief structure → your slides → marks → time
| Brief section | Brief slides | Your slides | Criterion | Weight | Speak time |
|---|---|---|---|---|---|
| **1. Introduction & Context** | 1–2 | S1, S2 | AC1 (problem) + AS1 | part of 30% | 1:10 |
| **2. Technology Analysis** | 3–5 | S3, S4, S5 | **AC1** | 30% | 2:15 |
| **3. Organisational & Stakeholder Impacts** | 6–7 | S6, S7 | **AC2** | 30% | 2:35 |
| **4. Strategic Evaluation & Recommendations** | 8–10 | S8, S9, S10 | **AC3** | 30% | 2:50 |
| **5. Conclusion & References** | 11 or 12 | S11, S12 | AC3/AS2 | – | 0:25 |
| Academic skills (presentation, notes, referencing) | – | all | **AS1 + AS2** | 10% | – |
Total speaking time ≈ **9:15** (limit 10:00; never exceed).

### 1.3 Brief bullet traceability
| Brief guideline bullet | Slide |
|---|---|
| AC1: briefly introduce the **problem** and why it concerns Disney+ | S1–S2 |
| AC1: briefly introduce **your chosen technology** | S3 |
| AC1: explain **how the technology could address the problem** | S3 |
| AC1: analyse **benefits and risks** | S4 (benefits), S5 (risks/limits) |
| AC1: support with **academic and industry sources** | S2–S5 |
| AC2: identify **one** stakeholder group and summarise concerns | S7 |
| AC2: address the concerns; explain how they can be managed | S7 |
| AC2: discuss **barriers or resistance** | S7 |
| AC2: **change management** and **digital confidence** across teams | S7 |
| AC2 headline: effect on Disney+ **structure, culture, processes** and key stakeholders | S6 (structure, culture, processes) + S7 (stakeholder) |
| AC3: supports **long-term strategic goals** (agility, innovation, retention) | S8 |
| AC3: **sustain advantage** through continuous improvement and innovation | S8 |
| AC3: **ethical and risk** considerations and mitigation | S9 |
| AC3: **three** clear, evidence-based recommendations | S10 |
| Presentation: logical structure; professional; correct spelling/grammar | all |
| Presentation: concise text, clear data, relevant visuals; tables/figures labelled with Harvard citation | all |
| Presentation: speaker notes expand key points (not full scripts) | all |
| Referencing: independent research with accurate Harvard citations | all + S12 |

---

## 2. THE ARGUMENT (lock before opening PowerPoint)
| Element | Locked choice |
|---|---|
| **Technology (one)** | **A unified cloud data-and-operations platform**: shared identity-and-billing spine + lakehouse data foundation with data-mesh (domain-owned) governance + observability/SRE tooling, migrated incrementally (strangler-fig) |
| **Problem** | Disney+, Hulu and ESPN (plus regional variants) risk running as parallel technology stacks and teams — duplicated systems, inconsistent customer/content data, uneven reliability, compliance managed region by region — slowing launches and bundling and raising cost-to-serve. The brief names it: "managing people, processes and technology across a global streaming platform" and "integrating its services with Hulu and ESPN in selected markets" |
| **Stakeholder (one)** | **Operations and compliance teams** (platform reliability/SRE, content operations, customer support, regional compliance) — the group the brief says focuses on "platform reliability, data protection, regulatory compliance, and supporting employees across international markets" |
| **Thesis (S1–S2 and S11)** | Unification is **an organisational redesign enabled by technology, not an IT migration**; it creates **sustained** advantage only if architecture, team structure, decision rights and culture change **together** ("organisations ship their org chart") |
| **Spine** | **UNIFY** (R1) → **RESHAPE** (R2) → **RETIRE & REINVEST** (R3) |
| **Three recommendations** | **R1** Unify: one account, one data truth, migrated by market waves · **R2** Reshape: platform/product team topology, decision rights, SRE, fair-process people transition · **R3** Retire and reinvest: sunset legacy stacks on schedule and ring-fence verified savings |
| **Thread phrases** | "platform before personalisation" · "reliability is a feature" · "the org chart is the architecture" |

**Five critical moves to land (these separate 70s from 80s):**
1. **Unify the spine, differentiate the experience** — "unify everything" is the wrong answer (operating-model diagnosis).
2. **Benefits are measurable but conditional**: availability arithmetic, delivery metrics, and a payback that depends on savings you must size.
3. **Architecture and organisation are mutually dependent** (Conway) — the loop must be shown in both directions.
4. **Treat dissent as signal**: give operations and compliance teams *voice*, *veto where law requires*, and *fair process*.
5. **Platform parity is likely** — the advantage is the capacity to recombine across brands (options, scope), and it erodes if teams revert to silos.

---

## 3. THE FINAL DECK — SLIDE-BY-SLIDE
Rule for every slide: **one hero visual + ≤3 supporting elements + ≤65 on-slide words** (counts the stack indicator and metric chip), an **action title**, a **so-what for Disney+**, and a source line under every figure/table. A small **stack-layer indicator** (Experience · Data · Identity & Billing · Infrastructure & Operations — highlight the layer discussed) and a **"Metric of the slide" chip** (≤6 words) appear on S2–S10.
Format: **Brief tag · Message · Hero visual · Supporting · Cite · Answer in your own words · Notes core/depth · Time/words · Pitfall.**

---

### SECTION 1 — INTRODUCTION & CONTEXT (Slides 1–2)

#### S1 — One customer, three apps
- **Brief tag:** Section 1 (state purpose & structure) · **Time:** 0:25 · **On-slide:** ≈35 · **Notes:** ≈70
- **Message:** the customer experiences our organisation chart.
- **Hero visual:** a three-panel **persona journey strip** (one family: sign up → pay → log in → find something to watch → get help) across Disney+, Hulu and ESPN, with friction markers. **Label prominently: "Illustrative persona — product details to be verified." `[V]`** Do not assert specific app behaviours as fact.
- **Supporting:** title "One Disney platform: unify, reshape, retire"; one-sentence thesis; footer **SRN** · module · date.
- **Answer in your own words:** (1) What friction would one family face, and which are only plausible rather than verified? (2) What is my thesis in one sentence? (3) What are the three decisions I will ask for?
- **Notes core:** persona friction; why it matters commercially; thesis (organisational redesign enabled by a platform); route.
- **Notes depth:** disclose the persona is illustrative; tie to the brief's Hulu/ESPN integration.
- **Pitfall:** presenting the persona as fact; a name on the slide.

#### S2 — Diagnosis: which operating model?
- **Brief tag:** Section 1 · **Time:** 0:45 · **On-slide:** ≈60 · **Notes:** ≈140
- **Message:** Disney is straddling operating models; unify the spine, differentiate the experience.
- **Hero visual (Fig 1 — operating-model 2×2, Ross, Weill and Robertson, 2006):** x = business-process standardisation, y = business-process integration; quadrants **Diversification · Coordination · Replication · Unification**. Plot "Disney+/Hulu/ESPN today (author's assessment)" in Diversification→Coordination, and "Target": **Coordination-to-Unification for identity, billing and data; Diversification retained for brand/content experience**. Caption "Figure 1: … (Source: Author, adapted from Ross, Weill and Robertson, 2006)". Label "author's assessment from public information `[IC]`".
- **Supporting:** three cited facts — (a) the brief's own challenge statements and Hulu/ESPN integration `[IC]`; (b) product consolidation moves (e.g., ESPN direct-to-consumer launch; Hulu folded into the Disney+ app) `[V]`; (c) reliability risk at peak events `[V]`. One problem statement: "Parallel stacks and regional silos slow launches, fragment data and make reliability and compliance costly."
- **Cite:** Ross, Weill and Robertson (2006); Tornatzky and Fleischer (1990) (TOE, optional); Disney 10-K and announcements `[V]`.
- **Answer in your own words:** What does each operating model imply for technology? Why *selective* unification? What can I say about Disney's real estate from public sources, and what must I label as an assumption?
- **Notes core:** the four models; why unify the spine only; why brand experience stays differentiated.
- **Notes depth:** TOE lens (technology: legacy/cloud readiness; organisation: structure/skills; environment: regulation, competitors); how I know — public statements, brief, `[IC]`; discovery would validate.
- **Pitfall:** pretending to know internal architecture.

---

### SECTION 2 — TECHNOLOGY ANALYSIS (Slides 3–5) → **AC1, 30%**

#### S3 — The technology and how it addresses the problem
- **Time:** 0:45 · **On-slide:** ≈55 · **Notes:** ≈140
- **Message:** four layers — unify the spine, federate the data, engineer reliability.
- **Hero visual (Fig 2 — platform stack):** bottom → top: **Infrastructure & Operations** (cloud, observability, SLOs/error budgets, incident management) · **Identity & Billing spine** (one account, entitlements, payments across brands) · **Data foundation** (lakehouse + data-mesh domains: content metadata, customer, playback, finance; data contracts; policy-as-code for residency) · **Experience layer** (Disney+, Hulu, ESPN — differentiated). A side arrow shows the **strangler-fig migration** around legacy. Caption "Figure 2: … (Source: Author, adapted from Armbrust et al., 2021; Dehghani, 2022; Ross, Weill and Robertson, 2006)".
- **Supporting:** three problem→capability rows — parallel stacks → shared spine · inconsistent data → governed data products · uneven reliability → SLO-driven operations; one-line option appraisal: "Chosen over status quo/middleware, an off-the-shelf customer data platform alone, and a big-bang re-platform (Appendix A1)."
- **Cite:** Armbrust et al. (2021) (vendor-authored — flag); Dehghani (2022) (practitioner — flag); Beyer et al. (2016).
- **Answer in your own words:** What does each layer do in one sentence? Why the spine first? What stays separate? Why not a ready-made customer data platform?
- **Notes core:** layer purposes; spine first; what stays differentiated.
- **Notes depth:** lakehouse vs warehouse vs lake; data-mesh principles and maturity warning; SLI/SLO/error-budget definitions; option criteria (fit, risk, time-to-value, org impact).
- **Pitfall:** vendor-brand soup; "cloud is good".

#### S4 — Benefits (measurable, conditional)
- **Time:** 0:50 · **On-slide:** ≈55 · **Notes:** ≈150
- **Message:** reliability, speed and cost are measurable; strategic value depends on organisational change.
- **Hero visual (Fig 3 — allowed downtime per month):** columns for availability targets using a 30.44-day month (43,834 minutes): **99.9% → 43.8 min; 99.95% → 21.9 min; 99.99% → 4.4 min**. Note: apply to "playback-start success", not generic uptime. Caption "Figure 3: Availability targets and allowed downtime (Source: Author's calculation)".
- **Supporting:** (a) a **delivery-performance strip** — deployment frequency · lead time for changes · change failure rate · time to restore (DORA; Forsgren, Humble and Kim, 2018; benchmark bands `[V]`; "association, not causation"); (b) a **payback line**: payback (months) = 100 ÷ s, where s = monthly run-cost saving as % of migration cost (s = 2% → 50; 3% → 33.3; 4% → 25; 5% → 20) — "depends on s, to be sized in discovery; excludes agility benefits"; (c) tags mapping to DeLone and McLean (2003): system quality, information quality, service quality, net benefits.
- **Cite:** Forsgren et al. (2018); DORA report `[V]`; Beyer et al. (2016); DeLone and McLean (2003); McAfee and Brynjolfsson (2012); Redman (2016) `[V]` (use cautiously).
- **Answer in your own words:** How do I compute allowed downtime? Why is "100% availability" the wrong target? What savings share s would make this worthwhile, and how will discovery size it? Which benefits aren't in the payback?
- **Notes core:** nines arithmetic; delivery metrics; payback logic.
- **Notes depth:** error budgets; peak-event load; involuntary churn from payment failures as a *plausible* benefit (quantify only with verified data `[V]`); data-quality cost claims are extrapolations (avoid the "1-10-100 rule"); vendor benchmarks flagged.
- **Pitfall:** invented dollar savings; treating survey associations as causal.

#### S5 — Limitations and failure modes
- **Time:** 0:40 · **On-slide:** ≈55 · **Notes:** ≈125
- **Message:** the biggest risks are migration, adoption and concentration — manage them as failure modes.
- **Hero visual (Fig 4 — failure-mode analysis, top five, RPN before → after, horizontal bars; scores are the author's judgement, S/O/D 1–10, RPN = S × O × D):**
  | Failure mode | S × O × D | RPN | After |
  |---|---|---|---|
  | Peak-event outage during cutover | 9 × 5 × 5 | 225 | 81 |
  | Data-mesh domain non-adoption/quality drift | 6 × 6 × 5 | 180 | 54 |
  | Talent attrition/ops fear | 7 × 6 × 4 | 168 | 63 |
  | Vendor lock-in/concentration | 7 × 4 × 6 | 168 | 84 |
  | Regional compliance breach (residency) | 8 × 4 × 5 | 160 | 48 |
  Caption "Figure 4: Failure-mode analysis (Source: Author's assessment, method after IEC 60812 `[V]`)". *(Full eight in Appendix A3, including security target 150→60, migration data loss 144→36, cloud cost overrun 144→54.)*
- **Supporting:** three short limit tags — data mesh is immature · a platform is not a strategy · legacy coupling; verdict "Viable if cutovers avoid tentpole events and parity gates hold."
- **Cite:** IEC 60812 `[V]`; Dehghani (2022); NIST CSF 2.0 (2024).
- **Answer in your own words:** Why did I score the top failure mode as I did? What does "detectability" mean in a migration? What is RPN's weakness (ordinal numbers multiplied) and how do I handle it?
- **Notes core:** top three modes; why FMEA; mitigations.
- **Notes depth:** score rationale; limits of RPN; replace scores with internal incident data in discovery.
- **Pitfall:** unexplained scores; hiding RPN's weakness.

---

### SECTION 3 — ORGANISATIONAL & STAKEHOLDER IMPACTS (Slides 6–7) → **AC2, 30%**

#### S6 — Organisation: architecture and structure shape each other
- **Time:** 1:10 · **On-slide:** ≈60 · **Notes:** ≈215
- **Message:** architecture and organisation are mutually dependent; change both or neither works.
- **Hero visual (Fig 5 — Conway diagram, two panels):** **Today (illustrative):** team boundaries by brand/region → duplicated services, with dashed hand-off/ticket arrows. **Target (Team Topologies):** stream-aligned teams per brand/experience · a **platform team** (identity, billing, data, observability) · **enabling teams** (SRE, data governance, security) · a **complicated-subsystem team** (e.g., playback pipeline). An **inverse-Conway** arrow: "design teams to get the architecture you want". **Mutual-influence labels:** architecture → structure (shared identity forces a platform team) and structure → architecture (regional teams reproduce regional silos). Caption "Figure 5: … (Source: Author, adapted from Conway, 1968; Skelton and Pais, 2019)".
- **Supporting (three short items):** **Decision rights** (Weill and Ross, 2004), three decisions only — data standards (platform team *decides*; brand teams *input*) · regional data residency (regional compliance **veto**) · release/rollback (platform + SRE *decide*); **Culture** (Westrum, 2004): bureaucratic ticket hand-offs → generative shared responsibility, blameless post-mortems; **Processes**: continuous delivery with automated checks; incident management; policy-as-code replaces committee approvals; follow-the-sun support.
- **Cite:** Conway (1968); Skelton and Pais (2019); Weill and Ross (2004); Westrum (2004); Weick and Sutcliffe (2007); Meyer (2014) with McSweeney (2002) (optional culture-across-markets critique).
- **Answer in your own words:** How does architecture change structure, and how does structure change architecture? Which decisions need a veto and why? What does a "generative" culture look like on an incident call? Which processes change?
- **Notes core:** one loop each direction; decision rights; culture shift.
- **Notes depth:** high-reliability principles (preoccupation with failure; deference to expertise); national-culture generalisations are contested (McSweeney); Conway is observational — used as a design heuristic and tested via delivery metrics; full decision-rights matrix in Appendix A2.
- **Pitfall:** org-chart boxes without interdependence; copying a framework with no Disney application.

#### S7 — The one stakeholder group: operations and compliance teams
- **Time:** 1:25 · **On-slide:** ≈65 · **Notes:** ≈260
- **Message:** the people who run the platform decide whether unification succeeds; give them voice, fair process and capability.
- **Hero visual (Table 1 — concern → response → metric, 5 rows, ≤8 words per cell):**
  1. "Central platform ignores local law" → regional compliance veto + policy-as-code → % policies automated; audit findings
  2. "We'll be blamed when it breaks" / on-call load → blameless post-mortems; error budgets; toil caps → pages per engineer per shift; MTTR
  3. "Consolidation means job cuts" → **fair process** (explain, engage, clarify expectations) + redeployment → attrition; fairness pulse
  4. "Don't break what works" → parallel run; rehearsed rollback; no cutovers at tentpole events → change failure rate
  5. "New tools and skills" → DigComp-aligned reskilling; platform-engineering career ladder → tier completion; skill coverage
- **Supporting (three short strips):** **Why this group** — on the critical path of every migration wave; holds run-time accountability and regulatory knowledge; high exit cost to Disney (Hirschman, 1970; Weill and Ross, 2004). **Change message** — five beliefs: *discrepancy* (why change), *appropriateness* (why this), *efficacy* (we can), *principal support* (leaders back it), *personal valence* (what's in it for me) (Armenakis and Harris, 2002); **voice channels**: platform council with ops/compliance seats; objection log with response SLA; anonymous pulse. **Digital-confidence ladder** (DigComp 2.1, Carretero, Vuorikari and Punie, 2017) — *Foundations → Practitioner → Platform-fluent*, with communities of practice (Wenger, 1998) and controlled **game days** (Basiri et al., 2016); metrics: tier completion, confidence pulse, game-day recovery time.
- **Barriers (one line, evidence-tagged):** attachment to local autonomy · fear of job loss · tool overload · regional legal variance · legacy coupling (Oreg, 2003 for dispositional resistance factors).
- **Cite:** Hirschman (1970); Oreg (2003); Colquitt (2001); Armenakis and Harris (2002); Carretero et al. (2017); Wenger (1998); Basiri et al. (2016).
- **Answer in your own words:** Why operations and compliance rather than another group? Which concern is hardest and why? What does "fair process" mean concretely here? How will I measure digital confidence?
- **Notes core:** why this group; five concerns with responses; message beliefs; ladder.
- **Notes depth:** Oreg's critique (individual vs situational causes); Hirschman — dissent as voice, attrition as exit; works-council/union consultation in some markets `[V]`; how to avoid "change theatre".
- **Pitfall:** a training slide with no evidence; developing a second stakeholder group.

---

### SECTION 4 — STRATEGIC EVALUATION & RECOMMENDATIONS (Slides 8–10) → **AC3, 30%**

#### S8 — Sustained competitive advantage
- **Time:** 0:55 · **On-slide:** ≈55 · **Notes:** ≈170
- **Message:** the platform becomes advantage as digital options and economies of scope — if the organisation can exploit them.
- **Hero visual (Fig 6 — options chain):** capabilities (modular services, shared identity, data products) → **digital options** (launch a bundle; enter a market; test pricing; add a sports tier; integrate a partner) → **agility** (time-to-launch KPI marked here) → competitive action → performance. Caption "Figure 6: … (Source: Author, adapted from Sambamurthy, Bharadwaj and Grover, 2003)".
- **Supporting:** a **shared vs differentiated** two-column mini-list (Panzar and Willig, 1981): *Shared* — identity, billing, data foundation, observability, compliance engine · *Differentiated* — brand experience, content, curation, marketing; a **goals→KPI line** — agility → time-to-launch · innovation → experiments/quarter on shared data · retention → fewer billing/login friction events `[V]`; an **improvement/ambidexterity line** — reliability (exploit) via platform/SRE and experimentation (explore) via stream-aligned teams (O'Reilly and Tushman, 2004); monthly SLO/error-budget review; quarterly architecture review.
- **Cite:** Sambamurthy et al. (2003); Panzar and Willig (1981); O'Reilly and Tushman (2004).
- **Answer in your own words:** Why isn't "being on the cloud" an advantage? What is shared and what must stay differentiated? What would make teams revert to silos? Which option would you exercise first?
- **Notes core:** options logic; shared vs differentiated; improvement cadence.
- **Notes depth:** counter-argument — rivals also use cloud; rebuttal — advantage is the *coupling of platform with a multi-brand portfolio and the organisation's ability to recombine*; concede platform parity is likely and that advantage erodes if silos return; limits of the options and scope theories.
- **Pitfall:** claiming "cloud = advantage".

#### S9 — Ethics, social, risk implications and horizons
- **Time:** 0:50 · **On-slide:** ≈55 · **Notes:** ≈150
- **Message:** responsible consolidation means fairness to staff, regional sovereignty, security and sustainability — then plan across horizons.
- **Hero visual (Table 2, 4 rows; issue → mitigation → KPI/owner):**
  1. **Workforce fairness** → fair-process commitments; redeployment/reskilling budget; no surprise cuts → fairness pulse; attrition (CHRO)
  2. **Data sovereignty and transfers** → residency by design; regional keys; transfer assessments (GDPR Ch. V; India DPDP `[V]`) → audit findings (Chief Compliance Officer)
  3. **Concentration and cyber risk** → zero-trust; segmentation; NIST CSF 2.0 mapping; exit plan → incidents; recovery tests (CISO)
  4. **Cloud environmental footprint** → carbon-aware workload placement; track software carbon intensity `[V]` → intensity per user-hour (CTO)
- **Supporting:** a **Three Horizons strip** (Baghai, Coley and White, 1999) — *H1 (0–12m)* stabilise and unify the spine · *H2 (12–30m)* exploit options (bundles, new markets) · *H3 (30m+)* emergent (AI-assisted operations; new formats on unified data); a **decision-trigger line**: deeper Hulu/ESPN integration timetable `[V]` → accelerate identity wave · major outage or regulatory change → pause cutovers and re-baseline · proven AI-ops maturity → pilot · major sports-rights expansion → capacity programme; one line admitting a trade-off ("protecting people slows decommissioning").
- **Cite:** Colquitt (2001); NIST (2024) *CSF 2.0*; GDPR Ch. V; India DPDP Act 2023 `[V]`; Baghai et al. (1999).
- **Answer in your own words:** Which issue is the most likely to derail execution and why? What are my triggers to accelerate or pause? What does fairness cost, and why accept it?
- **Notes core:** workforce fairness first; sovereignty; horizons and triggers.
- **Notes depth:** voluntary frameworks have limits; sustainability trade-off (migration emissions vs efficiency gains); ethics as execution risk-management.
- **Pitfall:** an ethics checklist with no owner or trigger.

#### S10 — Three recommendations
- **Time:** 1:05 · **On-slide:** ≈70 · **Notes:** ≈195
- **Message:** Unify → Reshape → Retire; sequenced by market waves and gates.
- **Hero visual (Table 3 + mini wave strip):**
  | # | Recommendation | Owner | Evidence | KPI / gate |
  |---|---|---|---|---|
  | R1 UNIFY | **Identity-billing spine + data foundation**, migrated by market **waves** (strangler-fig), SLOs from day one (M1–24) | CTO (accountable) + Chief Data Officer | Ross et al. (2006); Armbrust et al. (2021); Beyer et al. (2016) | SLO attainment; MTTR; **single-customer-view match rate**; time-to-launch; **parity gate per wave**, rollback rule |
  | R2 RESHAPE | **Platform/stream-aligned teams, decision rights (regional compliance veto), SRE, fair-process transition, reskilling** (M1–18, then standing) | COO (accountable) + CHRO + Chief Compliance Officer | Conway (1968); Skelton and Pais (2019); Westrum (2004); Colquitt (2001) | DORA four; Westrum score; fairness pulse; attrition; tier completion; **M9 gate** |
  | R3 RETIRE | **Sunset legacy systems after parity gate; ring-fence a fixed share of verified savings** for resilience, experimentation and people (M12–30) | CFO + CTO | Sambamurthy et al. (2003); O'Reilly and Tushman (2004) | Legacy decommissioned vs plan; cost-to-serve; % savings reinvested |
  Under it: a **wave strip** — W0 foundations (H1) · W1 first market pair (H2) · W2 regulated markets (H3) · W3 growth markets (H4) · W4 remaining/partners (H5), with ◆ gates and decommission windows (full 30-month swimlane in Appendix A3). Caption "Figure 7: 30-month wave plan (Source: Author)".
- **Define precisely (notes/A3):** **parity & stability gate per wave** — ≥30 days at/above SLO in parallel run · zero Sev-1 data loss · rollback rehearsed · regional compliance sign-off; **rollback rule** — a migration-attributable Sev-1 reverts within the agreed recovery time; **freeze windows** around tentpole events `[V]`; **single-customer-view match rate** = accounts resolved across brands at an agreed confidence; **cost-to-serve** definition agreed in discovery; **savings rule** — a share of *verified* savings (split set by the platform council).
- **Cost shape (notes):** three buckets — platform and cloud; people and transition; assurance and dual-running; ranges validated in discovery; **no invented figures**; if a wave fails the gate: keep the spine and governance (no-regret), narrow scope, rerun.
- **Answer in your own words:** Why this order? What do I want approved now? What triggers a rollback or a pause? Why a ring-fenced savings rule?
- **Pitfall:** recommendations that could apply to any company; no gate; no owner.

---

### SECTION 5 — CONCLUSION & REFERENCES (Slides 11–12)

#### S11 — Conclusion and key insights
- **Time:** 0:25 · **On-slide:** ≈45 · **Notes:** ≈80
- **Hero visual:** three insights — (1) unify the spine, differentiate the experience; (2) the org chart is the architecture; (3) advantage is exploiting options, not owning cloud.
- **Decision ask:** approve discovery and Wave 0; stand up the platform council with operations/compliance seats; confirm the savings-reinvestment rule; reconvene at M6.
- **Answer in your own words:** What are my three insights? What decision do I want today?
- **Pitfall:** new information; weak close.

#### S12 — References (not presented). Full alphabetical Harvard list (two columns, 9–10pt); continuation slide acceptable.

#### Appendix (max 3; information only — never hide core analysis here)
- **A1:** technology option appraisal (status quo/middleware; off-the-shelf CDP; big-bang re-platform; spine + federated data) + glossary (lakehouse, data mesh, SLI/SLO, error budget, strangler-fig, policy-as-code).
- **A2:** full decision-rights matrix + DigComp mapping + regional compliance table `[V]`.
- **A3:** detailed 30-month wave swimlane (build → parallel run → cutover → decommission), full eight-row FMEA with scoring rationale, KPI definitions.
- *AI-use evidence (prompts/responses)* as the cover sheet requires.

---

## 4. TIMING AND WORD BUDGET (final)
| Slide | Brief section | Speak | Spoken words | On-slide cap | Notes cap | Actual on-slide | Actual notes |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 0:25 | 60 | 35 | 70 | | |
| 2 | 1 | 0:45 | 105 | 60 | 140 | | |
| 3 | 2 | 0:45 | 105 | 55 | 140 | | |
| 4 | 2 | 0:50 | 115 | 55 | 150 | | |
| 5 | 2 | 0:40 | 95 | 55 | 125 | | |
| 6 | 3 | 1:10 | 165 | 60 | 215 | | |
| 7 | 3 | 1:25 | 200 | 65 | 260 | | |
| 8 | 4 | 0:55 | 130 | 55 | 170 | | |
| 9 | 4 | 0:50 | 115 | 55 | 150 | | |
| 10 | 4 | 1:05 | 150 | 70 | 195 | | |
| 11 | 5 | 0:25 | 60 | 45 | 80 | | |
| **Total** | | **9:15** | **≈1,300** | **≈610** | **≈1,695** | | |
- Counted words ≈ **2,300**; hard cap **3,000**; don't pad to 3,500. Notes ≈ 75% core + 25% depth; bullets, not scripts.
- If long in rehearsal: trim S2 and S3 first, never S6–S10.
- **Run sheet (cumulative):** S1 0:00 · S2 0:25 · S3 1:10 · S4 1:55 · S5 2:45 · S6 3:25 · S7 4:35 · S8 6:00 · S9 6:55 · S10 7:45 · S11 8:50 · end 9:15.

---

## 5. EVIDENCE PLAN
### 5.1 Core reading list (read properly; defend in a viva)
| Priority | Source | Used for |
|---|---|---|
| 1 | The Walt Disney Company — latest 10-K, earnings releases and product announcements `[V]` | S1–S2 context; what is public vs assumed |
| 2 | Ross, Weill and Robertson (2006) *Enterprise architecture as strategy* (core chapters) | S2 operating model; S3 appraisal |
| 3 | Armbrust et al. (2021) CIDR; Dehghani (2022) (skim principles) | S3 architecture (flag vendor/practitioner status) |
| 4 | Beyer et al. (2016) SRE chapters on SLOs, error budgets, toil; Forsgren, Humble and Kim (2018) + a DORA report `[V]` | S3–S4 reliability and delivery metrics |
| 5 | Conway (1968); Skelton and Pais (2019) | S6 structure |
| 6 | Weill and Ross (2004); Westrum (2004) | S6 decision rights and culture |
| 7 | Hirschman (1970); Oreg (2003); Colquitt (2001) | S7 stakeholder and fair process |
| 8 | Armenakis and Harris (2002); Carretero et al. (2017); Wenger (1998); Basiri et al. (2016) | S7 change message and digital confidence |
| 9 | Sambamurthy et al. (2003); Panzar and Willig (1981); O'Reilly and Tushman (2004) | S8 advantage |
| 10 | NIST (2024) CSF 2.0; GDPR Ch. V; India DPDP Act 2023 `[V]`; Baghai et al. (1999) | S9 risk, sovereignty, horizons |
Supporting: Tornatzky and Fleischer (1990); DeLone and McLean (2003); McAfee and Brynjolfsson (2012); Redman (2016) `[V]`; Weick and Sutcliffe (2007); Meyer (2014); McSweeney (2002); IEC 60812 `[V]`; Fowler (2004) `[V URL/date]`; Green Software Foundation SCI `[V]`. (Full bibliographic details are in `CW6_Blueprint_C_Detailed.md` §12.)

### 5.2 Verification rules
- Open each `[V]` item and confirm number, date and exact wording; if you can't verify, **delete the claim**. **Highest-risk items for C:** Disney's 2025–26 product consolidation and any outage history; DORA benchmark bands and year; who authored what (vendor-authored sources must be flagged); transfer-law specifics by market; "tentpole event" freeze windows.
- Label every assumption ("author's assessment", "illustrative persona", "payback depends on s").
- Flag source strength in notes (peer-reviewed / practitioner / vendor / regulator / company).
- Paraphrase; page numbers for any quote; two-way citation check.

---

## 6. PRODUCTION WORKFLOW
| Phase | Do | Definition of done |
|---|---|---|
| **0 Setup** | Confirm deadline and word-count method with tutor; start cover sheet; file naming (SRN only); BPP Harvard guide open | Admin checklist (§1.1) started |
| **1 Evidence** | Read core sources (§5.1); gather `[IC]` notes; verify every `[V]`; build the **reference list first** | Reference list complete; claim table (claim, source, strength, critique) filled |
| **2 Figures** | Build Fig 3 (nines), Fig 4 (FMEA bars), Fig 7 wave strip; then Fig 1, 2, 5, 6; captions + sources | Readable at 14pt; assumptions labelled |
| **3 Draft slides 6–10** | Write slide text and notes *in your own words* | ≤65 words; each has a so-what |
| **4 Draft slides 2–5, then 1 and 11** | Same method | Golden thread consistent |
| **5 Notes** | Bullets: core + depth; check caps | No full scripts |
| **6 Self-mark** | §8 checklist harshly; ask a peer/tutor with an IT or operations background to check the architecture explanation | No ★ below 2 |
| **7 Language review (permitted AI use)** | If used, only to proof/review; keep prompts; declare | Declaration + evidence complete |
| **8 Word conversion test** | Export to Word with notes (BPP guide); check slides, figures, notes, references; remove metadata | Passes |
| **9 Rehearse** | Three timed run-throughs; target 9:15–9:45; talk map not script | Two consecutive runs on time |
| **10 Record** | Teams; display name = SRN; Do Not Disturb; check audio and screen legibility | Playback verified |
| **11 Submit early** | Upload both ≥24h before deadline; keep receipts | Receipts saved |

---

## 7. NOTES METHOD AND DELIVERY
**Each slide's notes (bullets, own words):** 1) headline; 2) evidence (author/year); 3) so-what for Disney+; 4) depth (caveat/calculation/counter-argument/source critique); 5) bridge to next slide.
**Style:** UK English; precise and calm; define every technical term first time (lakehouse, data mesh, SLO, error budget, strangler-fig); signposts ("The evidence here is practitioner-based, so…", "The limitation of RPN is…"); avoid vendor names and hype.
**Video:** share screen; point at diagrams; one-second pause at transitions; never read slides; finish 9:15–9:45; talk map = slide → three prompts → transition sentence.

---

## 8. FINAL QUALITY GATES
### 8.1 80+ band checklist (0–2; every ★ must be 2)
| Criterion | Check | Score |
|---|---|---|
| AC1 ★ | One technology; Disney-specific problem; persona labelled illustrative | |
| AC1 ★ | Mechanism clear (layers, mesh, SLO, strangler-fig) and justified by the operating-model diagnosis | |
| AC1 | Benefits honest: nines arithmetic; DORA flagged as association; payback depends on s | |
| AC1 ★ | Limitations genuine (failure modes); RPN's weakness acknowledged | |
| AC1 | ≥2 academic + ≥2 industry/standards sources; vendor sources flagged | |
| AC2 ★ | Exactly one stakeholder group (operations and compliance); concerns specific and managed | |
| AC2 ★ | **Structure, culture and processes explicit (S6)**; two-way influence shown | |
| AC2 | Barriers evidenced; change message + fair process + voice channels; digital-confidence ladder with metrics | |
| AC3 ★ | Advantage conditional (options, scope, ambidexterity); platform-parity counter addressed | |
| AC3 ★ | Ethics/risk integrated (fairness, sovereignty, concentration); owners + KPIs; horizons and triggers | |
| AC3 ★ | **Exactly three** recs; owner, KPI, wave gates, rollback rule, savings rule, fallback | |
| AS1 | ≤65 words/slide; one hero visual; stack indicator + metric chip; figures labelled/sourced; notes expand | |
| AS1 | UK spelling/grammar clean; video 9:15–9:45, not read | |
| AS2 ★ | Two-way citation check; Harvard consistent; no unsourced numbers | |
| Admin ★ | Cover sheet; SRN only; AI declaration + prompts; word count; both uploads early | |

### 8.2 Harsh-marker pre-mortem (one sentence each)
1. What is original here? (selective unification via operating-model choice; org-chart-as-architecture; savings ring-fenced for people and resilience)
2. Where did I say what the evidence cannot show? (Disney internals are not public; vendor sources; DORA association; RPN)
3. Which numbers are assumptions, and are they labelled?
4. Did I develop **one** stakeholder group, and did S6 cover structure, culture and processes?
5. Exactly three recommendations, each with owner, KPI, gate and fallback?
6. Is every source real, read and cited both ways; are vendor/practitioner sources flagged?
7. Can I explain the architecture in plain language and finish under 10 minutes?

### 8.3 Viva prep (know these cold)
Lakehouse vs warehouse vs data lake · What is data mesh; what are its limits? · SLI, SLO, error budget; why 99.95% not 100%? · Show how you computed allowed downtime · The strangler-fig pattern and why not big-bang · Conway's Law and the inverse Conway manoeuvre · Team Topologies' four team types · Ross et al.'s four operating models; where is Disney, where should it be? · TOE and DeLone and McLean in your argument · DORA metrics and their limits · Why operations and compliance rather than creative teams or customers? · Hirschman's exit, voice and loyalty here · What is fair process and how do you measure it? · Armenakis and Harris's five beliefs with an example each · DigComp and a game day · How do you manage regional compliance on a global platform? · What if a wave fails the parity gate? · How do you avoid cutovers at major events? · Where is the advantage if rivals also use cloud? · Economies of scope — what is shared? · Which failure modes score highest and why is RPN imperfect? · How does the payback frontier work and what would invalidate it? · What would make you accelerate or pause?

---

## 9. WHAT TO SEND ME NEXT (permitted help)
1. **In-class Disney+ notes**, **deadline**, your tutor's **word-count answer**, and whether your module guide lists **LO4/LO5**.
2. A **draft** (even partial): I can review it against the rubric and §8 (the brief permits AI review of a draft), or build the **skeleton .pptx** with figure shells in C's design (paper/forest/coral), or the **spreadsheet** for the nines table, payback frontier, FMEA and wave plan.
