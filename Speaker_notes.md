# Speaker notes: The Ledger of Record

## Slide 1

I’m presenting as Apple TV+’s Digital Transformation Consultant. My question is simple: can blockchain-based smart contracts help Apple TV+ pay royalties accurately as it grows? I treat the technology as plumbing, not hype. It gives legal and rights teams a record they can trust. The real risk isn’t whether it works technically. It’s whether the law and the organisation are ready for it.

I’ll start with the problem, then explain the technology in plain terms, then weigh the benefits and limits. After that I’ll look at the people involved, how it fits Apple’s strategy, and what I’d recommend.

## Slide 2

Apple TV+ is growing. It clears music rights for its shows and negotiates talent deals across the same territories, and in 2024 it hired a licensing executive to take its originals to other platforms (9to5Mac, 2024). Every new platform and territory adds more parties and more rights windows, and Legal, Rights Ops and Finance still reconcile most of this by hand. So the question is how Apple TV+ keeps payments accurate and trusted as it grows, instead of paying for disputes afterwards.

The music industry shows what can go wrong, so I use it as an example. The Mechanical Licensing Collective is holding over $424 million in streaming royalties that were collected but never matched to the people owed them (Billboard, 2023). Sharp (2023) argues this is what manual matching looks like when there are too many rights holders and territories. Of course, that is a music figure, not Apple TV+’s own loss. What carries over is the pattern: manual matching breaks down as the number of parties grows.

Disputes also take a long time to settle. The Copyright Royalty Board set a streaming rate in 2018, it was appealed within months, and it wasn’t final until August 2023 (U.S. Copyright Royalty Board, 2023). A private dispute across several countries has no referee like that.

Someone might say this is a music problem, not a film and TV one. But Apple TV+ clears music rights and talent deals in the same territories, so the same structure applies, and it grows with the licensing plan. So before any pilot, Apple TV+ should measure its own dispute rate and reconciliation cost. Then any benefit we claim later can be checked against a real baseline.

## Slide 3

I’ll keep the technology simple. A blockchain has three ideas. First, blocks. Each record sits in a block linked to the one before it, so if someone changes an old record, the chain breaks and everyone can see it. Second, shared copies. Talent, rights holders and Apple TV+ each hold a copy, so nobody has to simply trust one administrator. Third, the smart contract. The licensing rules are written as code, so when a rights window opens the royalty calculation and payment can start without someone checking by hand.

You might ask why this isn’t just a better rights database. The problem with a normal database is that everyone has to trust whoever runs it, and in a multi-party deal that is often one of the counterparties. A shared ledger lets each party check the record for themselves. Zhao and O’Mahony (2018) built a working prototype for music rights, so we know it can be done. García et al. (2023) say research has moved on from “does it work?” to the legal and business questions, which is where this briefing sits. But a shared ledger is only useful if the other parties actually join it. So its value depends on talent and rights holders taking part, which is as much a relationship job as a technical one.

For a definition, I’ll use Iansiti and Lakhani (2017): an open, distributed ledger that records transactions between two parties in a way that can be verified and can’t be changed, and that can be programmed to trigger transactions automatically. They call it a foundational technology, like the internet, which changes things slowly rather than overnight. That fits here. Apple TV+ isn’t replacing its business. It is changing how a record is shared.

## Slide 4

The key point is that the contract doesn’t wait for someone to enforce it. The trigger sits inside the ledger. When a rights window opens in a territory, the calculation and payment can start right then. At the moment, the EU, APAC and US windows open on different dates, and each one needs someone to confirm it and someone to pay it.

Williamson’s (1979) transaction cost economics helps explain why that matters. His idea is that firms organise a deal so that contracting costs stay low, including the cost of monitoring and enforcing it. Checking that a window has opened is a monitoring cost. So automating the trigger changes how the deal is governed, not just how fast it runs. But the theory cuts both ways. Writing terms as code, auditing the code and running the platform are costs too. So the ledger only pays off where the monitoring it saves is worth more than that. That points to territories with frequent, standard payments, and away from rare, heavily negotiated deals. In practice, Apple TV+ can count the saving as fewer manual confirmation steps per territory.

There is one limit. Williamson can show the ledger may be a cheaper way to govern a deal. He can’t tell us whether a court in every country would accept an automatic payment as legally binding. That legal gap is what the next slides deal with.

## Slide 5

Here are the benefits and the limits side by side. The benefits are fewer errors and disputes, because automatic triggers take away discretion over when and how royalties are paid; one record that everyone can audit; and faster payment that scales, because a new territory just adds a trigger. The limits are legal enforceability, cost and integration, and skills and coding risk.

Jensen and Meckling’s (1976) agency theory explains the first benefit. Agency costs appear when someone hands decisions to another party whose interests may differ. Taking discretion out of the payment calculation reduces that cost, and the $424 million on slide two is really an example of it. But the theory only goes so far. Removing discretion helps with routine payments. Many royalty disputes come from unclear terms, and code can’t fix unclear terms.

The biggest limit is legal, not technical. A payment can execute correctly and still not be legally binding if someone disputes the underlying terms (Werbach and Cornell, 2017; Levy, 2017). Turning contract terms into code also creates a smaller new risk, because whoever translates them can make a mistake. That is why slide eleven has a specific control for it.

On cost and skills, Deloitte’s 2019 Global Blockchain Survey found that 28% of executives cite uncertain return on investment and 28% cite a lack of in-house skills (I took these figures from secondary coverage). They matter for Apple TV+ too. The ledger has to connect to the contract and finance systems already in use, or it just becomes a fourth record. And someone has to translate legal terms into code, which is where lawyers and developers can talk past each other. So each limit needs an answer, and the later slides give one: sign-off for the coding risk, a phased rollout for enforceability, and a one-territory pilot to test integration.

Finally, timing. Gartner’s 2024 Hype Cycle for Web3 and Blockchain put most blockchain technologies past the peak and sliding into the Trough of Disillusionment, with smart contracts just entering it. For Apple TV+ that means a staged pilot, not a big launch. Gartner may not publish another blockchain cycle, and its 2025 emerging-technologies cycle covers tokenisation and smart contracts under programmable money, as part of Autonomous Business. The technology works, but the legal and business setting is still maturing, so the case rests on narrow, well-defined payment rules, not on blockchain in general.

## Slide 6

Right now, three teams each keep their own version of the same royalty information. Legal holds the contract terms, Rights Ops tracks territories and windows, and Finance holds the payments. They only check against each other from time to time. A shared ledger doesn’t just make that check faster. It removes most of the need for it.

The work itself changes, not only the speed. Legal stops reviewing after the event and starts checking terms as they are written into the system. Rights Ops stops chasing people to confirm a window has opened and watches the ledger triggers instead. Finance stops sorting out disputed claims and audits a record that is already reconciled. That is a real change in skills, so the worries on the next slide aren’t just resistance to change.

On structure and culture, I’d form one small team with a single named owner in place of three separate reconciliations. Culturally, people have to trust a record they didn’t create themselves, and that takes training and shared accountability.

I also used Porter’s (1985) value chain to see where the ledger bites. In technology development, royalty rules become tested code that Legal and engineers sign off together. In inbound logistics, which for a streamer means receiving content and talent rights, windows and payment terms come from one shared record instead of being re-confirmed by hand in each territory. Porter’s point is that the benefit is spread across activities, which is why one named owner matters. Without one, each function improves its own step and the ledger becomes a fourth record. So this is really an organisational design choice, not only a technology choice.

## Slide 7

I focus on legal and rights teams. They aren’t against change by habit. They are the people who would have to answer to a regulator or a court if something went wrong, so their concerns are professional ones.

They have three. The first is regulation: which country’s law applies to a cross-border smart-contract payment dispute, and an unchangeable ledger can clash with GDPR rights to correct or delete personal data (European Parliament and Council, 2016; Finck, 2018). The second is enforceability. Correct execution doesn’t guarantee a binding payment, and Werbach and Cornell (2017) and Levy (2017) both argue that smart contracts don’t replace contract law. The third is integration. The ledger has to work with the contract and finance systems already in use, or it recreates the three-way reconciliation problem.

Underneath all three is the same gap: there is little settled case law on smart-contract royalties. Legal teams are being asked to approve something the law hasn’t caught up with.

So my answer is about sequencing, not reassurance. Start in territories where digital-contract rules are clearer, keep personal data off the ledger, pilot in one territory with Legal in the design team, and keep a standing legal review as territories are added. The written contract stays the master and the ledger just carries it out. That follows from Werbach and Cornell: the ledger can only run a contract the law already recognises. So Legal should be a design authority, not a late reviewer, and its approval is the real gate for each new territory.

## Slide 8

My answer is yes, legal and rights teams can be brought along, but only if three things happen. Legal helps shape the design, a one-territory pilot proves the value, and people are trained before go-live.

I used Davis’s (1989) technology acceptance model, which says people adopt a tool if it seems useful and easy to use. The ledger will seem useful if it answers the worries from slide seven: a record they can show a regulator, the written contract kept as master, and no extra version of the truth. It will seem hard to use if it brings unfamiliar tools, coding and awkward system links, and easy if it plugs into current systems, needs no coding from users, and gives a simple read-only view. One more point. These teams carry personal accountability, so trust in the output matters as much as ease of use. That’s why I focus on their ability to stop a payment.

For change, I used three of Kotter’s (1996) eight steps, in order. Step two, build a guiding coalition: Legal, Rights Ops and Finance sit in the design team under one named owner. Step six, create short-term wins: pilot in one territory and share the results. Step eight, anchor the change in the culture: make the quarterly review permanent. Kotter assumes there is a sponsor who can drive change, and the named owner is that person. Both models describe attitudes, though. Neither tells us whether the law will accept the ledger.

The main barrier is fear of answering for a wrongly coded payment, so I’d use dual sign-off, a manual override and a dispute freeze. And I’d train Legal, Rights Ops and Finance before the pilot on how the record works, how to read a smart-contract term, and when to freeze a payment.

## Slide 9

The idea on this slide is simple. Every verified payment is a small deposit of trust with talent, and that trust is tied to how quickly Apple TV+ can license. If rights holders see payments that are accurate, on time and traceable, they have less reason to hesitate over the next deal.

This ties to Apple’s strategy. Apple TV+ has committed to expanding third-party licensing, with an executive hired in 2024 (9to5Mac, 2024). As partners and territories grow, it needs a system that scales without disputes growing at the same rate. That makes the ledger more a condition of the strategy than a bonus. There are two links. On talent retention, originals draw people into the wider Services ecosystem, and creators who can verify every payment have less reason to take their next project elsewhere. On agility, if partners already trust the record, adding a platform or a territory means adding a trigger, not starting a new reconciliation.

I’d call this a resource-based argument rather than a technology one. Accurate payments build a track record that rivals can’t simply buy. But it cuts both ways. One visible error damages trust faster than many correct payments build it. So the sign-off controls on slide eleven protect the strategy as well as the money. And the link can be tested: do dispute numbers fall, and can new territories and partners be added faster?

One assumption needs checking. The ledger is only a differentiator while competitors don’t have one. Whether the advantage lasts is the next slide.

## Slide 10

Being early is a real advantage, but staying ahead is a different claim, and I don’t think the evidence supports it without qualification.

DiMaggio and Powell’s (1983) institutional isomorphism says organisations in the same field become more alike over time, through pressure from regulators, copying under uncertainty, and professional norms. Copying could happen if a rival simply follows Apple TV+. Regulators could also push for more transparent royalty reporting, as the Copyright Royalty Board cycle on slide two suggests. Since the technology is easy to copy, only the organisation and the relationships can be a lasting source of advantage.

There is a fair counterargument. Talent already on Apple’s ledger has a payment history and little reason to leave just because a rival adopts something similar. So the technology advantage may fade while the relationship advantage lasts longer. That is my claim: the advantage is built on relationships and builds up over time. It is not built on technology. Trust is also lopsided. Talent will judge Apple TV+ on its worst payment, not its average one, so the advantage is only as strong as the error controls on slide eleven. So I treat the ledger as the foundation of a relationship strategy, not the advantage itself, and I’d review this every year.

Using Barney’s (1991) VRIO test: is it valuable? Yes, mainly because it means fewer disputes. Is it rare? Yes, for now. My searches found no major video streamer running a rights ledger, only music efforts such as Spotify’s 2017 purchase of Mediachain and vendor platforms like Tech Mahindra’s bCRMS. That isn’t proof that none exist. Is it hard to imitate? The code is easy to copy. The payment history isn’t. Is Apple TV+ organised to capture it? Not yet. A named owner and team are proposed on slide six, but dual sign-off and a standing legal review still need to be set up, so this is the weakest test today. Barney assumes a stable resource, but here the record of payments grows with use, so the advantage depends on starting early and running without visible errors. My verdict: the advantage is temporary until the organisation and the trust are built.

## Slide 11

There are three risks, each with its own cause and its own fix, but they affect each other.

The first is data privacy. Ledger entries can hold sensitive commercial data or personal data, and some laws let people correct or delete their data, which clashes with a ledger that can’t be changed (European Parliament and Council, 2016; Finck, 2018). The fix is in the design: keep personal data off the ledger and record only a verification hash.

The second is cross-border regulation. There is no settled international standard for enforcing smart-contract royalties. The fix is the phased rollout from slide seven, starting where digital-contract law is clearer. This is the risk Apple TV+ can’t fully control, which is why the order of rollout matters.

The third is smart-contract error, and I think it’s the most serious. It connects to the coding gap on slide five. A wrong term in the code keeps paying the wrong party until someone notices. So I’d require legal and technical sign-off before go-live, plus a manual override and a dispute freeze. The risks interact. An error is harder to fix on a ledger that can’t be changed, and fixing it may involve personal data. So the controls work as a set: personal data kept off the ledger, sign-off, and a freeze, each covering a gap in the others. The practical test is whether Apple TV+ can find and stop a wrong payment before it reaches talent, and the pilot can rehearse that before go-live.

## Slide 12

I have three recommendations, and each one turns a theory from earlier into something someone owns.

First, set up a standing governance review. Transaction cost economics tells us to keep checking that the system still lowers contracting costs as new territories and rights types are added. Second, require dual sign-off before go-live. Agency theory warns that translating terms into code creates a new risk, and two sign-offs control it. Third, invest in relationships, not just technology. Institutional isomorphism says competitors will copy the technology, so the first-mover edge is temporary by design. What lasts is trust built through visible payment history and clear timelines. None of these costs much compared with the technology, and they are where management effort changes the outcome.

## Slide 13

Slide two started with a $424 million problem and a choice: fix royalty accuracy properly, or keep paying for disputes. My answer is yes, fix it, but only if the ledger is treated as a legal and organisational commitment, not a technical fix left to run on its own.

That depends on three things. For enforceability, a phased rollout by jurisdiction, as on slide seven. For coding risk, dual sign-off, as on slide eleven. And for competitive advantage, we have to accept that it is relationship-based and time-limited, as on slide ten, because competitors will be pushed to follow.

Against the three questions I set at the start: on feasibility, the mechanism cuts real monitoring and agency costs but adds a coding risk. On people and processes, the concerns of legal and rights teams are legitimate, and they need governance, not reassurance. On lasting advantage, the edge is accumulated trust and payment history, which Apple TV+ has to keep building. So the conclusion is conditional, not enthusiastic.

In practice, I’d do three things. Measure the current dispute rate and reconciliation cost. Pick one territory with clearer digital-contract rules and run the pilot with Legal in the design team. Then judge it on fewer disputes, faster payments and legal sign-off, not just technical success, before moving to the next territory. I should also be clear about the limits. The evidence on competitors is thin, the Deloitte figures cover many industries, and the music example is an analogy. That is why I recommend a governed pilot with clear tests, not a guaranteed return.

