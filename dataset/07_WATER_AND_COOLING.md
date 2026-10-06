# Water and Cooling

> Project-specific water use cannot be inferred from the generic phrase “data center.” Cooling architecture, heat-rejection method, climate, electrical load, server utilization, water source, and operating assumptions materially change water demand.
>
> Last reviewed: 2026-10-06

## Core distinction: closed loop is not one single design

A closed internal coolant loop recirculates fluid through servers, cold plates, immersion systems, CDUs, chillers, or heat exchangers. That describes the **internal loop**, but it does not by itself prove that the entire facility consumes zero water.

External heat rejection can be:

- fully dry / air-cooled;
- evaporative;
- adiabatic or hybrid;
- connected to a cooling tower;
- connected to another heat sink.

Therefore, the useful Cascade questions are not merely “Is it closed loop?” but:

1. What carries heat away from the computing equipment?
2. How is that heat finally rejected outdoors?
3. Is any water evaporated during normal or peak-weather operation?
4. What is annual makeup-water use?
5. Is potable municipal water used?
6. What is peak-day use during hot weather?
7. What coolant is used and how is it contained?
8. What is discharged to sewer/stormwater, if anything?
9. What happens during drought or equipment failure?

## Simple Mining claims

Simple Mining's public water article states that its Iowa fleet uses closed-loop systems and claims very low water use, including a figure of approximately 300 gallons per year per 10 MW and no evaporative cooling in its systems. The company also discusses propylene-glycol coolant.

Those are **company statements about its operations**, not an independent engineering determination for Cascade. A Cascade approval process should request sealed design documents, actual WUE/makeup-water estimates, peak-day demand, source-water information, metering, leak detection, and independent review.

## October 1 Cascade forum update

At the October 1, 2026 forum, Simple Mining described the Cascade concept as **closed-loop hydrocooling with an air-cooled condenser / dry heat-rejection system**. The company said municipal water would **not** be used for routine cooling and that the cooling-loop fluid would be brought to the site. Expected municipal use was described mainly as domestic building use (restrooms/sinks) plus possible limited humidification.

The company also expressed willingness to accept an enforceable water-use cap. It discussed a glycol-based coolant and described the coolant used at its Manchester facility as biodegradable/corn-based, but no final Cascade product selection, SDS, coolant inventory, sealed mechanical drawing, or gallons/day/year estimate was provided.

These are company representations. They materially narrow the proposed architecture but do not eliminate the need for final engineering and metering.

See [`28_SIMPLE_MINING_COMMUNITY_FORUM_2026-10-01.md`](28_SIMPLE_MINING_COMMUNITY_FORUM_2026-10-01.md).

## October 1 Cascade forum update

At the October 1, 2026 community forum, Simple Mining described the current Cascade concept as **closed-loop hydrocooling with an air-cooled condenser / dry heat-rejection system**. The company represented that Cascade municipal water would **not** be used for normal cooling heat rejection; expected municipal use was described as ordinary building/domestic use and potentially limited winter humidification. The presenter also said the initial coolant charge would be brought to the site rather than filled from the municipal water system and expressed willingness to accept an enforceable monthly/project water-use cap.

Those statements materially narrow the earlier design uncertainty, but they remain **company representations based on a preliminary design**. The forum did not supply final mechanical drawings, quantified average/peak/annual municipal water demand, the final coolant product/SDS, leak-containment design, or independently reviewed performance data.

The raw forum source is a YouTube automated-caption transcript and is not human-verified. See [`28_SIMPLE_MINING_COMMUNITY_FORUM_2026-10-01.md`](28_SIMPLE_MINING_COMMUNITY_FORUM_2026-10-01.md).

## Industry evidence: water use varies dramatically

A 2025 peer-reviewed Lawrence Berkeley National Laboratory review found workload-level data-center water use can vary by more than four orders of magnitude. Important variables include server efficiency, utilization, cooling system, climate, grid water use, inactive equipment, and hardware-refresh cycle. This is strong evidence against applying one generic “gallons per data center” number to every project.

## Zero-water / dry-cooling examples

Microsoft announced a next-generation data-center cooling design using chip-level closed-loop cooling that it says consumes zero water for cooling during operation, aside from non-cooling administrative uses. This demonstrates technical feasibility for some modern designs; it is not evidence that Simple Mining's Cascade design uses Microsoft's architecture.

Supermicro markets closed-loop dry-cooler systems for data-center liquid cooling. Its materials describe dry heat rejection at multi-megawatt scale.

Chart Industries describes large closed-loop air-cooled heat exchangers/dry coolers as a method of dramatically reducing water compared with evaporative systems.

ThermoKey and EVAPCO publish dry-cooler and hybrid/adiabatic product information that illustrates the distinction between fully dry cooling and designs that add water under high-temperature conditions.

## Important terminology lesson

EVAPCO's technical material is particularly useful because it shows that a product can be called a **closed-circuit cooler** while still evaporating water on the outside of the closed process-fluid coil. Thus “closed circuit” and “zero water consumption” are not synonyms.

## Cascade policy implications

A defensible local standard should be based on measurable performance rather than a brand or marketing term. Potential requirements include:

- engineering narrative and diagram from IT load to outdoor heat rejection;
- expected annual, monthly, peak-day, and emergency water demand;
- water source and whether potable water is used;
- cooling-water and process-water metering;
- independent water-capacity/hydrology review;
- leak detection and chemical/coolant containment;
- drought curtailment plan;
- wastewater/blowdown disclosure;
- maximum project-wide annual water use;
- renewed review before a cooling-system change or expansion.

## What remains unknown for Cascade

The October 1 forum represented a dry/air-cooled heat-rejection design and municipal water limited mainly to domestic uses, but the following still lack final documented values:

- annual gallons/year;
- maximum gallons/day;
- peak hot-weather demand;
- final sealed mechanical design;
- exact municipal-water demand;
- wastewater volume;
- final coolant product and inventory;
- drought-response plan and enforceable water cap.

These are appropriately treated as open questions, not assumptions.

## Sources

### Company / project-specific context

- Simple Mining — Data Center Water Usage: https://www.simplemining.io/insights/post/data-center-water-usage
- Simple Mining — Data Center Cooling: https://www.simplemining.io/insights/post/data-center-cooling
- City of Cascade — June 22, 2026 Council Minutes (records closed-loop representation): https://www.cityofcascade.org/vimages/shared/vnews/stories/6959ce08641c7/June%2022%202026%20Council%20Minutes.pdf
- October 1 forum summary and transcript provenance: [`28_SIMPLE_MINING_COMMUNITY_FORUM_2026-10-01.md`](28_SIMPLE_MINING_COMMUNITY_FORUM_2026-10-01.md)

### Independent / academic

- Lawrence Berkeley National Laboratory — Water Use in Data Center Workloads: https://eta.lbl.gov/publications/water-use-data-center-workloads
- DOI — Resource Conservation & Recycling paper: https://doi.org/10.1016/j.resconrec.2025.108310

### Technology examples

- Microsoft — Sustainable by Design: next-generation datacenters consume zero water for cooling: https://www.microsoft.com/en-us/microsoft-cloud/blog/2024/12/09/sustainable-by-design-next-generation-datacenters-consume-zero-water-for-cooling/
- Microsoft — Inside Microsoft's two-decade push to cut water intensity while scaling for growth: https://blogs.microsoft.com/blog/2026/06/24/inside-microsofts-two-decade-push-to-cut-water-intensity-while-scaling-for-growth/
- Supermicro — Liquid Cooling Solutions: https://www.supermicro.com/en/solutions/liquid-cooling
- Supermicro — Dry Cooler datasheet: https://www.supermicro.com/datasheet/datasheet_Dry_Cooler.pdf
- Chart Industries — Powering Data Centers / cooling solutions: https://files.chartindustries.com/powering_data_centers.pdf
- EVAPCO — EAW-DD Double Stack Dry Cooler: https://www.evapco.com/products/closed-circuit-coolers-air-cooled/eaw-dd-double-stack-dry-cooler
- EVAPCO — EAW-FD Flat Dry Cooler: https://www.evapco.com/products/closed-circuit-coolers-air-cooled/eaw-fd-flat-dry-cooler
- EVAPCO — Evaporative Closed Circuit Coolers: Know Your Options: https://www.evapco.com/sites/evapco.com/files/2017-08/Evaporative-Closed-Circuit-Coolers-Options-4-2013.pdf
- ThermoKey — Data Centre cooling solutions: https://www.thermokey.com/wp-content/uploads/2023/04/Brochure_Data-Center-cooling-Solution_Digital-Ver_03.24.pdf
- ThermoKey — AFS Air Fresh System: https://www.thermokey.com/en/accessories/air-fresh-system/
- Google — water stewardship and cooling tradeoffs: https://blog.google/company-news/outreach-and-initiatives/sustainability/new-water-stewardship-commitments/

### Iowa policy comparators

- Linn County approved data-center ordinance: https://www.linncountyiowa.gov/DocumentCenter/View/27695/PA26-0001-Ordinance-PDF
- Jones County data-center ordinance: https://www.linncountyiowa.gov/DocumentCenter/View/27656/Jones-County-Data-Center-Ordinance
- Norwalk Project West: https://norwalkiaswdevelopment.com/datacenter
