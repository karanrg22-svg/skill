# 400IT Networking Coursework: Report Plan and Checklist

Group B range: 192.70.20.0/24. This is a planning outline only. Write the report text yourself (the brief's AI policy does not allow AI to compose it).

## Report plan (~2000 words, +/- 10%)

**Intro (~100 words)**
- Who SWG is, the three sites (Skipton HQ, Wroclaw, Greenwich), and what you built: VLSM, VLANs, OSPF, DNS/HTTP in Packet Tracer.

**A. Addressing (~400 words)**
- Method: start from 192.70.20.0/24, size subnets by host count, allocate largest first. Sales 30 hosts -> /27, IT 17 -> /27 (a /28 gives only 14 usable), HR 8 -> /28. Repeat per site = 9 subnets. 0th subnet used.
- Efficiency and scalability: spare addresses per subnet (Sales 0, IT 13, HR 6), /30 for serial links, unused space left for growth, what you would do if a department grew.
- Include one summary table of all nine subnets and their gateways.

**B. Topology (~350 words)**
- Hub-and-spoke vs triangle: pick what you actually build and justify it.
- Efficiency and resilience: OSPF reroutes if a link fails (use your route costs: 65 direct, 129 via another router). Say what a link failure does in your design.
- Router-on-a-stick with subinterfaces Gi0/0.10, .20, .30 and why VLANs are used.

**C. Security (~350 words)**
- Only describe what you configured: enable secret, console and VTY passwords, VLAN segmentation (HR separated from Sales and IT).
- If you add service password-encryption, banner, SSH or port security, say so. If not, say so honestly and describe as future improvement.
- Head office to branch: be honest the lab has no VPN/ACLs; explain what a real deployment would add (IPsec VPN, ACLs).

**D. Network testing (~450 words)**
- Discuss 2-3 ping/tracert results; explain what each hop shows.
- Troubleshooting as symptom -> cause -> fix, using your real problems (missing Skipton-Greenwich serial link, Skipton Se0/1/1 down, device names not matching, any failed ping).
- Screenshots: show ip ospf neighbor, show ip route, website at www.coventrylab.ac.uk.

**E. Reliability and resilience (~250 words)**
- Tie A-D together: dynamic routing (no manual route changes), VLANs limit broadcast domains, addressing leaves room to grow, security + topology keep the business running.

**Conclusion + references (~100 words + refs)**
- Academic sources only (textbooks / journal articles) for OSPF, VLSM, VLANs.
- State any AI use and what it was used for (required by the brief).

## What is left to do

### 1. Task 6 report (40 marks)
- [ ] Write the 2000-word report (A-E above) with screenshots.
- [ ] Fix the Task 1 plan in your draft (IT=.32/27, HR=.64/28) so it matches the final nine-subnet plan.

### 2. Topology (Task 2, 5 marks)
- [ ] Add the Skipton-Greenwich serial link (e.g. 192.70.20.245/30 Skipton, 192.70.20.246/30 Greenwich); re-run show ip ospf neighbor.
- [ ] Rename devices to match the worksheet (PC01-08, Laptop02/04, PC68-73, Laptop77-79, PC98-106, DNS Server, HTTP Server).
- [ ] Check the wireless router / access point at Wroclaw.

### 3. Lab Scenario Worksheet (.docx is blank)
- [ ] Student ID at the top.
- [ ] Task 1: three subnet tables + 10-mark workings box.
- [ ] Task 2: host tables for all sites with real ipconfig /all output (IP, mask, gateway, MAC). Remove guessed (*) addresses.
- [ ] Task 3: all six serial IPs (remove "Verify..." placeholders, fix duplicate Router1 Se0/1/1), Gig interface table, router names/passwords table, OSPF details.
- [ ] Task 4: ping and tracert screenshots (12 marks).
- [ ] Task 5: DNS/HTTP details and webpage screenshot.
- [ ] Router names: worksheet says Router0/1/2 ("0, 2, 3" looks like a typo); yours are Skipton/Wroclaw/Greenwich. Ask your tutor or rename.
- [ ] Task 4 rows differ slightly between brief and worksheet (PC20 vs PC69, PC02 vs Laptop02); follow the worksheet.

### 4. Device_Configuration.txt
- [ ] Paste full show running-config for all 3 routers and 3 switches (currently truncated: no interfaces, OSPF block, enable secret, console/VTY class0, VLAN names, access ports).
- [ ] Recapture show ip route after adding the third link (Skipton table is missing .224/28 and serial networks).
- [ ] show vlan brief for the Wroclaw and Greenwich switches (only Skipton shown so far).
- [ ] copy run start on every device before saving the .pkt.

### 5. Security additions (for section C)
- [ ] service password-encryption, login banner, login on VTY; optionally SSH and switchport port-security.

### 6. Submission (4 files or score = 0)
- [ ] ID_Report.docx
- [ ] ID_topology.pkt
- [ ] ID_Device_Configuration.txt
- [ ] ID_Lab_Scenario_Paper.docx
- [ ] Reference any AI tools used and for what purpose.
