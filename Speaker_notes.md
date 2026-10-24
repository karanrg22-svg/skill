# Speaker notes: The Ledger of Record

## Slide 1

This briefing is presented from the perspective of Apple TV+’s Digital Transformation Consultant. The central question is whether blockchain-based smart contracts can help Apple TV+ pay royalties accurately as it grows. The technology is treated as infrastructure, not hype: it gives legal and rights teams a record they can trust. The real risk is not whether it works technically, but whether the law and the organisation are ready for it.

The briefing begins with the problem, then explains the technology in plain terms and weighs the benefits and limits. It then covers the people involved, the fit with Apple’s strategy, and the recommendations.

## Slide 2

Apple TV+ is growing. It clears music rights for its shows and negotiates talent deals across the same territories, and in 2024 it hired a licensing executive to take its originals to other platforms (9to5Mac, 2024). Every new platform and territory adds more parties and more rights windows, and Legal, Rights Ops and Finance still reconcile most of this by hand. The question is how Apple TV+ keeps payments accurate and trusted as it grows, instead of paying for disputes afterwards.

The music industry shows what can go wrong, so it is used here as an example. The Mechanical Licensing Collective is holding over $424 million in streaming royalties that were collected but never matched to the people owed them (Billboard, 2023). Sharp (2023) argues this is what manual matching looks like when there are too many rights holders and territories. That is a music figure, not Apple TV+’s own loss. What carries over is the pattern: manual matching breaks down as the number of parties grows.

Disputes also take a long time to settle. The Copyright Royalty Board set a streaming rate in 2018, it was appealed within months, and it was not final until August 2023 (U.S. Copyright Royalty Board, 2023). A private dispute across several countries has no referee like that.

It could be argued that this is a music problem, not a film and TV one. But Apple TV+ clears music rights and talent deals in the same territories, so the same structure applies, and it grows with the licensing plan. Before any pilot, therefore, Apple TV+ should measure its own dispute rate and reconciliation cost, so that any benefit claimed later can be checked against a real baseline.

## Slide 3

A blockchain has three ideas. First, blocks. Each record sits in a block linked to the one before it, so if an old record is changed, the chain breaks and everyone can see it. Second, shared copies. Talent, rights holders and Apple TV+ each hold a copy, so nobody has to simply trust one administrator. Third, the smart contract. The licensing rules are written as code, so when a rights window opens the royalty calculation and payment can start without anyone checking by hand.

A fair question is why this is not simply a better rights database. The problem with a normal database is that everyone has to trust whoever runs it, and in a multi-party deal that is often one of the counterparties. A shared ledger lets each party check the record for themselves. Zhao and O’Mahony (2018) built a working prototype for music rights, so the approach is known to be workable. García et al. (2023) say research has moved on from whether it works to the legal and business questions, which is where this briefing sits. But a shared ledger is only useful if the other parties actually join it. Its value depends on talent and rights holders taking part, which is as much a relationship job as a technical one.

For a definition, Iansiti and Lakhani (2017) describe an open, distributed ledger that records transactions between two parties in a way that can be verified and cannot be changed, and that can be programmed to trigger transactions automatically. They call it a foundational technology, like the internet, which changes things slowly rather than overnight. That fits here. Apple TV+ is not replacing its business. It is changing how a record is shared.

## Slide 4

The key point is that the contract does not wait for someone to enforce it. The trigger sits inside the ledger. When a rights window opens in a territory, the calculation and payment can start right then. At the moment, the EU, APAC and US windows open on different dates, and each one needs someone to confirm it and someone to pay it.

Williamson’s (1979) transaction cost economics helps explain why that matters. The idea is that firms organise a deal so that contracting costs stay low, including the cost of monitoring and enforcing it. Checking that a window has opened is a monitoring cost, so automating the trigger changes how the deal is governed, not just how fast it runs. But the theory cuts both ways. Writing terms as code, auditing the code and running the platform are costs too, so the ledger only pays off where the monitoring it saves is worth more than that. That points to territories with frequent, standard payments, and away from rare, heavily negotiated deals. In practice, Apple TV+ can count the saving as fewer manual confirmation steps per territory.

There is one limit. Williamson can show the ledger may be a cheaper way to govern a deal, but not whether a court in every country would accept an automatic payment as legally binding. That legal gap is what the next slides deal with.

## Slide 5

The slide sets the benefits and the limits side by side. The benefits are fewer errors and disputes, because automatic triggers take away discretion over when and how royalties are paid; one record that everyone can audit; and faster payment that scales, because a new territory just adds a trigger. The limits are legal enforceability, cost and integration, and skills and coding risk.

Jensen and Meckling’s (1976) agency theory explains the first benefit. Agency costs appear when someone hands decisions to another party whose interests may differ. Taking discretion out of the payment calculation reduces that cost, and the $424 million on slide two is really an example of it. But the theory only goes so far. Removing discretion helps with routine payments, yet many royalty disputes come from unclear terms, and code cannot fix unclear terms.

The biggest limit is legal, not technical. A payment can execute correctly and still not be legally binding if someone disputes the underlying terms (Werbach and Cornell, 2017; Levy, 2017). Turning contract terms into code also creates a smaller new risk, because whoever translates them can make a mistake. That is why slide eleven has a specific control for it.

On cost and skills, Deloitte’s 2019 Global Blockchain Survey found that 28% of executives cite uncertain return on investment and 28% cite a lack of in-house skills (figures taken from secondary coverage). These matter for Apple TV+ too. The ledger has to connect to the contract and finance systems already in use, or it becomes a fourth record. And someone has to translate legal terms into code, which is where lawyers and developers can talk past each other. Each limit therefore needs an answer, and the later slides give one: sign-off for the coding risk, a phased rollout for enforceability, and a one-territory pilot to test integration.

Finally, timing. Gartner’s 2024 Hype Cycle for Web3 and Blockchain put most blockchain technologies past the peak and sliding into the Trough of Disillusionment, with smart contracts just entering it. For Apple TV+ that means a staged pilot, not a big launch. Gartner may not publish another blockchain cycle, and its 2025 emerging-technologies cycle covers tokenisation and smart contracts under programmable money, as part of Autonomous Business. The technology works, but the legal and business setting is still maturing, so the case rests on narrow, well-defined payment rules, not on blockchain in general.

## Slide 6

Right now, three teams each keep their own version of the same royalty information. Legal holds the contract terms, Rights Ops tracks territories and windows, and Finance holds the payments. They only check against each other from time to time. A shared ledger does not just make that check faster. It removes most of the need for it.

The work itself changes, not only the speed. Legal stops reviewing after the event and starts checking terms as they are written into the system. Rights Ops stops chasing people to confirm a window has opened and watches the ledger triggers instead. Finance stops sorting out disputed claims and audits a record that is already reconciled. That is a real change in skills, so the concerns on the next slide are not just resistance to change.

On structure and culture, the proposal is one small team with a single named owner in place of three separate reconciliations. Culturally, people have to trust a record they did not create themselves, and that takes training and shared accountability.

Porter’s (1985) value chain shows where the ledger has its effect. In technology development, royalty rules become tested code that Legal and engineers sign off together. In inbound logistics, which for a streamer means receiving content and talent rights, windows and payment terms come from one shared record instead of being re-confirmed by hand in each territory. Porter’s point is that the benefit is spread across activities, which is why one named owner matters. Without one, each function improves its own step and the ledger becomes a fourth record. This makes it an organisational design choice, not only a technology choice.

## Slide 7

The focus is legal and rights teams. They are not against change by habit. They are the people who would have to answer to a regulator or a court if something went wrong, so their concerns are professional ones.

There are three. The first is regulation: which country’s law applies to a cross-border smart-contract payment dispute, and an unchangeable ledger can clash with GDPR rights to correct or delete personal data (European Parliament and Council, 2016; Finck, 2018). The second is enforceability. Correct execution does not guarantee a binding payment, and Werbach and Cornell (2017) and Levy (2017) both argue that smart contracts do not replace contract law. The third is integration. The ledger has to work with the contract and finance systems already in use, or it recreates the three-way reconciliation problem.

Underneath all three is the same gap: there is little settled case law on smart-contract royalties. Legal teams are being asked to approve something the law has not caught up with.

The response is about sequencing, not reassurance. Start in territories where digital-contract rules are clearer, keep personal data off the ledger, pilot in one territory with Legal in the design team, and keep a standing legal review as territories are added. The written contract stays the master and the ledger just carries it out. This follows from Werbach and Cornell: the ledger can only run a contract the law already recognises. Legal should therefore be a design authority, not a late reviewer, and its approval is the real gate for each new territory.

## Slide 8

The answer is yes, legal and rights teams can be brought along, but only if three things happen. Legal helps shape the design, a one-territory pilot proves the value, and people are trained before go-live.

Davis’s (1989) technology acceptance model says people adopt a tool if it seems useful and easy to use. The ledger will seem useful if it answers the concerns from slide seven: a record that can be shown to a regulator, the written contract kept as master, and no extra version of the truth. It will seem hard to use if it brings unfamiliar tools, coding and awkward system links, and easy if it plugs into current systems, needs no coding from users, and gives a simple read-only view. One more point is that these teams carry personal accountability, so trust in the output matters as much as ease of use. That is why the barrier box focuses on the ability to stop a payment.

For change, three of Kotter’s (1996) eight steps are used, in order. Step two, build a guiding coalition: Legal, Rights Ops and Finance sit in the design team under one named owner. Step six, create short-term wins: pilot in one territory and share the results. Step eight, anchor the change in the culture: make the quarterly review permanent. Kotter assumes there is a sponsor who can drive change, and the named owner is that person. Both models describe attitudes, though. Neither shows whether the law will accept the ledger.

The main barrier is fear of answering for a wrongly coded payment, so the plan uses dual sign-off, a manual override and a dispute freeze. Legal, Rights Ops and Finance staff should also be trained before the pilot on how the record works, how to read a smart-contract term, and when to freeze a payment.

## Slide 9

The idea on this slide is simple. Every verified payment is a small deposit of trust with talent, and that trust is tied to how quickly Apple TV+ can license. If rights holders see payments that are accurate, on time and traceable, they have less reason to hesitate over the next deal.

This ties to Apple’s strategy. Apple TV+ has committed to expanding third-party licensing, with an executive hired in 2024 (9to5Mac, 2024). As partners and territories grow, it needs a system that scales without disputes growing at the same rate. That makes the ledger more a condition of the strategy than a bonus. There are two links. On talent retention, originals draw people into the wider Services ecosystem, and creators who can verify every payment have less reason to take their next project elsewhere. On agility, if partners already trust the record, adding a platform or a territory means adding a trigger, not starting a new reconciliation.

This is a resource-based argument rather than a technology one. Accurate payments build a track record that rivals cannot simply buy. But it cuts both ways. One visible error damages trust faster than many correct payments build it, so the sign-off controls on slide eleven protect the strategy as well as the money. The link can also be tested: do dispute numbers fall, and can new territories and partners be added faster?

One assumption needs checking. The ledger is only a differentiator while competitors do not have one. Whether the advantage lasts is the subject of the next slide.

## Slide 10

Being early is a real advantage, but staying ahead is a different claim, and the evidence does not support it without qualification.

DiMaggio and Powell’s (1983) institutional isomorphism says organisations in the same field become more alike over time, through pressure from regulators, copying under uncertainty, and professional norms. Copying could happen if a rival simply follows Apple TV+. Regulators could also push for more transparent royalty reporting, as the Copyright Royalty Board cycle on slide two suggests. Since the technology is easy to copy, only the organisation and the relationships can be a lasting source of advantage.

There is a fair counterargument. Talent already on Apple’s ledger has a payment history and little reason to leave just because a rival adopts something similar. The technology advantage may therefore fade while the relationship advantage lasts longer. That is the claim made here: the advantage is built on relationships and builds up over time. It is not built on technology. Trust is also lopsided. Talent will judge Apple TV+ on its worst payment, not its average one, so the advantage is only as strong as the error controls on slide eleven. The ledger is therefore treated as the foundation of a relationship strategy, not the advantage itself, and the position should be reviewed every year.

Using Barney’s (1991) VRIO test: is it valuable? Yes, mainly because it means fewer disputes. Is it rare? Yes, for now. Searches found no major video streamer running a rights ledger, only music efforts such as Spotify’s 2017 purchase of Mediachain and vendor platforms like Tech Mahindra’s bCRMS. That is not proof that none exist. Is it hard to imitate? The code is easy to copy. The payment history is not. Is Apple TV+ organised to capture it? Not yet. A named owner and team are proposed on slide six, but dual sign-off and a standing legal review still need to be set up, so this is the weakest test today. Barney assumes a stable resource, but here the record of payments grows with use, so the advantage depends on starting early and running without visible errors. The verdict is that the advantage is temporary until the organisation and the trust are built.

## Slide 11

There are three risks, each with its own cause and its own fix, but they affect each other.

The first is data privacy. Ledger entries can hold sensitive commercial data or personal data, and some laws let people correct or delete their data, which clashes with a ledger that cannot be changed (European Parliament and Council, 2016; Finck, 2018). The fix is in the design: keep personal data off the ledger and record only a verification hash.

The second is cross-border regulation. There is no settled international standard for enforcing smart-contract royalties. The fix is the phased rollout from slide seven, starting where digital-contract law is clearer. This is the risk Apple TV+ cannot fully control, which is why the order of rollout matters.

The third is smart-contract error, and it is the most serious. It connects to the coding gap on slide five. A wrong term in the code keeps paying the wrong party until someone notices, so legal and technical sign-off should be required before go-live, together with a manual override and a dispute freeze. The risks interact. An error is harder to fix on a ledger that cannot be changed, and fixing it may involve personal data. The controls therefore work as a set: personal data kept off the ledger, sign-off, and a freeze, each covering a gap in the others. The practical test is whether Apple TV+ can find and stop a wrong payment before it reaches talent, and the pilot can rehearse that before go-live.

## Slide 12

There are three recommendations, and each one turns a theory from earlier into something with an owner.

First, set up a standing governance review. Transaction cost economics says to keep checking that the system still lowers contracting costs as new territories and rights types are added. Second, require dual sign-off before go-live. Agency theory warns that translating terms into code creates a new risk, and two sign-offs control it. Third, invest in relationships, not just technology. Institutional isomorphism says competitors will copy the technology, so the first-mover edge is temporary by design. What lasts is trust built through visible payment history and clear timelines. None of these costs much compared with the technology, and they are where management effort changes the outcome.

## Slide 13

Slide two started with a $424 million problem and a choice: fix royalty accuracy properly, or keep paying for disputes. The answer is yes, fix it, but only if the ledger is treated as a legal and organisational commitment, not a technical fix left to run on its own.

That depends on three things. For enforceability, a phased rollout by jurisdiction, as on slide seven. For coding risk, dual sign-off, as on slide eleven. And for competitive advantage, it has to be accepted that the advantage is relationship-based and time-limited, as on slide ten, because competitors will be pushed to follow.

Against the three questions set at the start: on feasibility, the mechanism cuts real monitoring and agency costs but adds a coding risk. On people and processes, the concerns of legal and rights teams are legitimate, and they need governance, not reassurance. On lasting advantage, the edge is accumulated trust and payment history, which Apple TV+ has to keep building. The conclusion is therefore conditional, not enthusiastic.

In practice, three steps follow. First, measure the current dispute rate and reconciliation cost. Second, pick one territory with clearer digital-contract rules and run the pilot with Legal in the design team. Third, judge it on fewer disputes, faster payments and legal sign-off, not just technical success, before moving to the next territory. The limits of the analysis should also be clear. The evidence on competitors is thin, the Deloitte figures cover many industries, and the music example is an analogy. That is why a governed pilot with clear tests is recommended, not a guaranteed return.

