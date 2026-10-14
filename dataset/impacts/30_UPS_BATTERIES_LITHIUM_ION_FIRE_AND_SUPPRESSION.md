# UPS Batteries, Lithium-Ion Fires, and Data-Center Fire Protection

> Independent technical research for Cascade, Iowa. Last reviewed: 2026-10-13.
>
> **Evidence status:** General standards, fire-service research, survey data, and manufacturer cost models. This is **not** a confirmed equipment inventory or fire-protection design for Simple Mining's proposed Cascade site. The applicable edition of any code must be determined by the authority having jurisdiction (AHJ).

## Executive findings

1. **Battery chemistry is unconfirmed for Cascade.** The October 1, 2026 forum record does not specify UPS capacity, lead-acid versus lithium-ion, rack-level backup batteries, battery-energy-storage systems (BESS), or an approved fire-protection package. About 15 proposed **diesel backup generators** are a separate technology from batteries. See [October 1 forum record](../updates/28_SIMPLE_MINING_COMMUNITY_FORUM_2026-10-01.md).
2. **Valve-regulated lead-acid (VRLA) has a long history in UPS use and usually costs less to buy.** It is not established that lead-acid is always cheaper to **maintain and replace over the long term**. Longer lithium-ion service life may reduce replacements, footprint, cooling, and lifetime cost. Outcomes depend on duty cycle, operating temperatures, warranty, installation, finance, fire controls, and disposal.
3. **Lithium-ion uptake is substantial.** Uptime Institute's 2024 supplier survey found 63% of responding suppliers reported *increasing adoption* of lithium-ion for centralized UPS, and 52% for in-rack distributed UPS. **These are not market-share percentages.** A separate 2024 industry survey reported VRLA at 37% of respondents' centralized UPS installations and lithium-manganese-oxide at 26%; this survey is vendor-sponsored and not representative of every facility.
4. **Fire protection and emergency response depend on installed equipment and capacity.** Stationary ESS fire safety falls under applicable fire/building/electrical codes and may draw on NFPA 855, NFPA 75, NFPA 13, and relevant UL standards. These standards are not automatically Cascade ordinance text merely because this repository cites them.
5. **Lithium-ion can fail through thermal runaway.** An overheated cell can release flammable and toxic gases, propagate to other cells, reignite, and in poorly controlled conditions create deflagration hazards. Battery chemistry, cells, BMS, spacing, containment, ventilation, detection, cooling, and response planning matter.
6. **Private ownership and tenant contracts do not cancel fire-code requirements.** A tenant may own an in-rack UPS while the site operator owns central UPS and generators. The respective responsibilities cannot be inferred for Cascade until the intended arrangement, lease, inventory, and fire plan are disclosed.

## Three different systems often conflated

| System | Purpose | Common location and responsibility | Project status |
| --- | --- | --- | --- |
| Facility UPS (centralized) | Bridges short outages, stabilizes power, may carry loads while generator starts | Dedicated room/equipment area; typically coordinated by operator/owner | Not specified for Cascade |
| Distributed/rack UPS | Protects individual servers or racks | In-row/in-rack systems; owner may be customer or operator, subject to contract and site rules | Not specified for Cascade |
| Standalone BESS | Stores energy for extended backup, load shifting, grid services, or another purpose | Separate cabinets, room, or enclosure; may require different engineering and fire controls | Not established for Cascade |
| Diesel standby generators | Produce electricity using fuel when needed | Site-level backup equipment | Approximately 15 proposed by company, subject to final engineering |

The presence of diesel generators does **not** prove any particular UPS design or lithium-ion battery quantity.

## VRLA versus lithium-ion

| Consideration | VRLA / lead-acid | Lithium-ion |
| --- | --- | --- |
| Purchase price | Frequently lower | Frequently higher upfront |
| Typical UPS service life | Often about 3-6 years in practice, varies by conditions | Can exceed 10 years in specified UPS applications, varies by chemistry and conditions |
| Replacement and planned maintenance | More frequent replacements can increase labor, downtime, and lifetime cost | Often fewer replacements and less routine maintenance, but requires a suitable battery-management system |
| Weight / space | Generally heavier and bulkier for similar duty | Generally smaller and lighter |
| Safety issues | Lead toxicity, sulfuric acid, hydrogen venting/charging, electrical faults and thermal runaway possible in batteries | Cell thermal runaway, flammable off-gas, propagation, deflagration potential, electrical faults |
| End of life | Mature lead-acid recycling stream; recycling and lead handling still require controls | Recycling and disposal depend on chemistry and available services |
| Ownership | Operator or tenant depending on UPS architecture | Operator or tenant depending on UPS architecture |

These are broad industry comparisons, not Cascade equipment specifications. Schneider Electric's 2026 single-phase UPS analysis models a 53% **lower** 10-year total cost of ownership for lithium-ion despite higher initial cost. That is an equipment vendor's model, **not** an independent price quotation or a universal outcome. Argonne National Laboratory also reports scenarios in which lithium-ion UPS ownership cost is lower over ten years. The correct statement is **lead-acid is usually cheaper upfront; lifetime cost is scenario-dependent and may favor lithium-ion**.

**Supporting research:**

- Uptime Institute, *Global Data Center Survey 2024: Supplier View* (adoption trends, not market share): https://datacenter.uptimeinstitute.com/rs/711-RIA-145/images/2024.GlobalDataCenterSurvey.VendorResults.pdf
- ZincFive, *2024 Data Center Energy Storage Industry Insights* (vendor-sponsored survey; treat sampling cautiously): https://zincfive.com/industry-insights-report/data-center-energy-storage-2024/
- Schneider Electric, *UPS Total Cost of Ownership*, 2026 (vendor scenario): https://blog.se.com/datacenter/2026/04/02/what-every-it-professional-should-know-about-ups-total-cost/
- Schneider Electric, UPS TCO calculation tool and white paper references: https://www.se.com/ww/en/work/solutions/data-centers-and-networks/trade-off-tools/single-phase-li-ion-vs-vrla-ups-tco-calculator/
- Schneider Electric, *Life Expectancy of APC Lithium Ion Batteries*, updated 2025: https://www.se.com/us/en/faqs/FAQ000265882/
- Argonne National Laboratory, energy storage / UPS technology cost comparisons (2018): https://publications.anl.gov/anlpubs/2018/05/138665.pdf
- Uptime Institute, *Lithium Ion Batteries for the Data Center*: https://journal.uptimeinstitute.com/lithium-ion-batteries-in-the-data-center/

## What occurs in a lithium-ion battery failure?

A cell can enter **thermal runaway**, leading to accelerating temperature and possible heating of nearby cells. Failure may include smoke, toxic or flammable vent gases, ignition, heat, and delayed reignition. An enclosed room or cabinet may accumulate gases that can deflagrate if ignited. These are scenario-specific hazards, not evidence that every installation will experience a fire.

**Recorded large-scale example:** Fire Safety Research Institute (FSRI) documented a 2019 incident at a 2.16 MWh Arizona ESS in which a clean-agent system discharged, but combustible/toxic gas accumulated and a deflagration seriously injured four firefighters. The incident is a useful caution about gas monitoring, ventilation, explosion protection, crew training, and not assuming extinguishment equals safety. It is **not a frequency estimate for data centers**.

- FSRI incident findings: https://fsri.org/research-update/report-four-firefighters-injured-lithium-ion-battery-energy-storage-system
- FSRI firefighter-training resource: https://training.fsri.org/course/104/fire-service-considerations-with-lithium-ion-battery-energy-storage-systems
- U.S. Fire Administration, lithium-ion hazards and response strategies: https://www.usfa.fema.gov/a-z/lithium-ion-batteries/risks-and-response-strategies/

## How data centers detect and suppress fires

Protection is generally **layered**. Which measures are needed depends on building and fire code, equipment chemistry/capacity, occupancy, site arrangement, engineer of record, and the AHJ.

### Detection and prevention

- Smoke detection, often including early-warning or aspirating detection in equipment spaces.
- Battery-management systems (BMS), temperature/voltage monitoring, alarms, fault isolation, and power shutoffs.
- Battery off-gas detection or combustible-gas monitoring where required by evaluated hazards and codes.
- Segregation of batteries/electrical equipment, approved enclosures and spacing, fire-rated barriers, and appropriate ventilation/explosion protection.
- Commissioned emergency disconnects, incident plans, inspections, training, and maintenance.

### Suppression and control

- **Automatic sprinklers:** Protect the building and limit fire spread. Pre-action sprinklers can reduce inadvertent water discharge around IT hardware. The actual system design must meet applicable standards.
- **Clean-agent / inert-gas systems:** Often installed to protect electronic equipment, sometimes alongside sprinklers. They can be appropriate for certain equipment-room fires but should **not be assumed to stop an internal lithium-ion thermal-runaway sequence or remove a gas-explosion hazard**.
- **Water mist:** An engineered option in some installations where approved. It must be evaluated for the specific hazard.
- **Battery-specific systems and measures:** Water-based cooling, propagation barriers, detection, ventilation/explosion controls, compartmentation, and separation may be needed according to test evidence and approved design. The objective may be containment and protection of exposures rather than instantly extinguishing every failed cell.

ASHRAE's 2023 Data Centers handbook describes sprinkler/pre-action, gaseous suppression, and combinations of the two, with approval by local code authorities.

- ASHRAE, *Data Centers and Telecommunication Facilities*, fire-protection section: https://handbook.ashrae.org/Handbooks/A23/IP/A23_Ch20/a23_ch20_ip.aspx
- NFPA 75 (2024), IT equipment fire protection: https://www.nfpa.org/codes-and-standards/nfpa-standard-development/75
- NFPA 13, sprinkler system installation: https://www.nfpa.org/codes-and-standards/nfpa-standard-development-process/13

## Fire department response

**This is operational context, not a tactical instruction for a local firefighter.** Incident command must follow training, the actual equipment emergency response guides, measured conditions, and local procedures. Plans typically consider:

1. Determine whether the incident concerns ordinary IT equipment, VRLA UPS, lithium-ion UPS, or large ESS.
2. Obtain a site battery inventory, chemistry, capacity, floor plan, emergency contacts, disconnect locations, and manufacturer's emergency response guide.
3. Establish exclusion areas and use appropriate firefighter PPE/SCBA; assess toxic and flammable off-gases.
4. Monitor temperature and atmosphere remotely where possible. Gas accumulations can pose explosion risks even when visible flames are absent.
5. Coordinate utility isolation, system shutdown, ventilation decisions, containment/cooling, and protection of adjacent areas with trained personnel.
6. Plan for prolonged monitoring, potential reignition, hazardous runoff, and safe cleanup/disposal.

The USFA and FSRI research underscore that thermal runaway can require substantial cooling, gas monitoring, and careful re-entry. **Never assume a discharged clean-agent system has neutralized a damaged lithium-ion battery.**

## NFPA/UL standards and their limits

- **NFPA 855**: Installation of stationary energy storage systems; 2026 edition exists, but local adoption/version and system applicability must be checked. It addresses hazards according to technology, size, location, and installation.
- **NFPA 75**: Fire protection of IT equipment and equipment areas. The 2024 edition directs lithium-ion storage matters to NFPA 855, avoiding the assumption that general server-room rules replace ESS-specific analysis.
- **NFPA 13 / 2001 / 750**: Sprinkler, clean-agent, and water-mist systems respectively, as relevant.
- **UL 9540**: Product/system standard for applicable ESS equipment. **UL 9540A** is a **test method** that evaluates thermal runaway propagation and fire/explosion behavior; it is not a blanket declaration that a site is risk-free, nor should it be casually described as a product certification.
- Fire and electrical codes and AHJ interpretation determine site requirements. Whether all these standards apply to a particular small UPS, rack unit, or large ESS requires a design-specific review.

Sources:
- NFPA 855 standard scope: https://www.nfpa.org/codes-and-standards/nfpa-standard-development-process/855
- NFPA 75 2024 edition description: https://www.nfpa.org/product/nfpa-75-standard/p0075code/nfpa-75-standard-for-the-fire-protection-of-information-technology-equipment-2024/7524
- UL Solutions, UL 9540A/NFPA 855 technical explanation: https://www.ul.com/thecodeauthority/knowledge/understanding-UL-9540A-NFPA-855
- UL Solutions, ESS installation FAQ: https://www.ul.com/resources/installation-codes-and-requirements-energy-storage-systems-ess-faqs

## Private property, tenants, and accountability

Zoning is mainly concerned with land use and measurable external effects. It is **not** a general power to select a private data center's lawful customers or the workloads on their computers. But a private industrial building remains subject to applicable zoning, building, fire, electrical, environmental, and hazardous-material regulations. A tenant-installed UPS is not inherently exempt from fire inspection or operator site rules. Lease terms allocate private obligations; they do not erase public-law obligations.

Central UPS chemistry is often an operator/facility-design choice. In-rack UPS equipment **may** be a tenant choice when the service agreement permits it. There is no evidence confirming either arrangement for Cascade. Likewise, the October 1 forum did not establish who will own UPS components or whether rack rentals will permit tenant-owned batteries.

See [Cascade zoning/local authority](../policy/04_CASCADE_ZONING_AND_LOCAL_AUTHORITY.md) and [workload type background](../technology/03_DATA_CENTER_WORKLOAD_TYPES.md).

## Why comparing a cellphone battery to a data-center battery is not valid

Both can use lithium-ion chemistry and share generic cell-failure mechanisms. That **does not show equal failure probability**. Cell chemistry, engineering, manufacturing, duty cycle, protection, temperature, age, environment, and quality affect risk. A centralized data-center battery installation can contain much more stored energy and has different fire spread, gas accumulation, isolation, and emergency response issues.

**No credible matched dataset was found here supporting a claim that a cellphone battery is equally likely to ignite as a data-center battery installation.** Do not use this comparison as a statistic.

## Site-specific Cascade evidence needed

- Final UPS architecture, **battery chemistry for each system**, quantities, kWh/MWh, locations, and ownership.
- Whether an independent stationary BESS is planned at all; separate it from rack UPS.
- Battery/vendor/model specifications, safety data sheets, UL listings and applicable UL 9540A test results when required.
- Fire and building code editions selected by the AHJ, fire-protection plans, fire suppression and detection system diagrams.
- Off-gas detection, HVAC/ventilation, rated fire compartments, disconnect and explosion-hazard evaluation where relevant.
- Water supply and suppression-water runoff plans as applicable.
- Local fire/EMS pre-incident response, specialized training, emergency contacts, and developer funding for project-driven needs.
- Tenant installation restrictions, inspection rights, emergency notification, and assignment of continuing responsibilities.
- Final approved design and a change-control procedure if battery chemistry, energy capacity, or tenant rack equipment materially changes.

## Evidence labels

- **Verified external primary sources:** NFPA, USFA, FSRI, ASHRAE, UL Solutions, Argonne, Uptime Institute.
- **Vendor model, not a universal outcome:** Schneider Electric lifecycle-cost analysis.
- **Vendor-sponsored survey:** ZincFive 2024 sample results.
- **Company representation:** October 1 forum statements about generators and fire protection.
- **Not established for Cascade:** any lithium-ion/lead-acid installation, quantity, tenancy arrangement, suppression package, or battery fire risk.
