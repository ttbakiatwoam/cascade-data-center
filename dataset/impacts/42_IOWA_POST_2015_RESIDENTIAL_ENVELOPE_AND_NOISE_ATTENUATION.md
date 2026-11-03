# Iowa residential construction after 2015 and exterior sound attenuation

**Date:** November 3, 2026  
**Scope:** Source record supporting the non-codified discussion of Cascade M-2 noise standards.

The canonical, public-facing referenced summary is [the website research page](https://ttbakiatwoam.github.io/cascade-data-center/house-noise-attenuation-iowa/), sourced in `docs/house-noise-attenuation-iowa.md`.

## Verified takeaways

- Iowa's statewide energy code baseline **after 2015** was still the **2012 IECC with state amendments**, effective April 1, 2014. The 2015 calendar year is not an energy-code transition date.
- Iowa's residential energy code specifies envelope air sealing and insulation, **not a statewide minimum exterior-wall STC/OITC or fixed dBA/dBC reduction**.
- Iowa's 2012 IECC amendments allow up to **4 ACH50** at mandatory blower-door testing and use **R-20 or R-13 + R-5 continuous insulation** in common wood-frame wall prescriptive cases; alternative compliance methods and existing house details vary.
- **Dubuque County**: IECC **5A**; **Delaware County**: **6A** in the 2012-era county table.
- Cascade §6-12-8, from Ordinance 02-22 (2022), adopts the current **State of Iowa Building Code** by reference within the city. Earlier permits should be assessed under the codes actually applicable when issued.
- FHWA `Noise Measurement Handbook` Table 6-1 uses **20 dB** for ordinary closed-window light framing; **25 dB** with storm windows; **25 dB** for single-glazed masonry; and **35 dB** for double-glazed masonry. These are transportation-noise planning factors, *not* code-guaranteed attenuation for homes built after 2015 and *not* a demonstrated dBC reduction for data-center hum.
- New proposed indoor-receptor limit remains **55 dBA/65 dBC day** and **50 dBA/60 dBC night**. The code does **not** presume a standard 20 dB building attenuation. The external industrial property-line limit remains independent.

## Primary references

1. DOE, *Iowa Energy Code Status*, <https://www.energycodes.gov/status/states/iowa>.
2. Iowa Administrative Code 481—301.24, *Residential Energy Code*, <https://www.legis.iowa.gov/DOCS/ACO/IAC/LINC/Rule.481.301.24.pdf>.
3. City of Cascade, §6-12-8, adopted code (Ord. 02-22), <https://codelibrary.amlegal.com/codes/cascadeia/latest/cascade_ia/0-0-0-4159>.
4. FHWA, *Noise Measurement Handbook*, Table 6-1 and §6.0, <https://www.fhwa.dot.gov/Environment/noise/measurement/handbook.cfm>.
5. U.S. DOE Building America, county climate-zone mapping, <https://www.energy.gov/eere/buildings/articles/building-america-best-practices-series-volume-73-guide-determining-climate>.
6. PNNL, *Iowa 2012 IECC energy impact and amendments*, <https://www.pnnl.gov/main/publications/external/technical_reports/PNNL-24946Rev1.pdf>.

**Interpretation:** Do not infer minimum or actual low-frequency facade attenuation from 2015+ construction date alone. Any project prediction should state its measured or supported building-specific transmission loss by frequency.

## Owner refusal and exterior-measurement fallback (November 3, 2026)

Proposed §165.11(G)(4)(e) expressly permits a property owner or lawful occupant to decline voluntary indoor noise testing. If indoor access is declined, a qualified professional measures sound at the source-facing boundary of the sensitive-receptor parcel, where lawfully accessible and representative, or documents the closest suitable lawful alternative. Outdoor testing on private land also requires permission or other lawful authority.

The professional separately estimates the level at the protected building facade and then the predicted interior Leq,1h with documented **outdoor-to-indoor noise reduction (OINR)** or other frequency-dependent acoustic transmission-loss data. The model must address the sound spectrum, low-frequency industrial equipment, A and C weightings, background sound, propagation and uncertainty. The resulting **estimated** interior value is distinct from a direct interior measurement.

**Thermal insulation R-values are not acoustic ratings:** the Iowa energy code provides information about the likely wall assembly, not a lawful fixed subtraction in dBA or dBC. Do not convert wall insulation R-values into a decibel adjustment. FHWA's typical 20 dB light-frame closed-window highway-noise factor may be mentioned as a sensitivity example, but it is not proof of any Cascade home's performance, especially for low-frequency sound. A conservative 0 dB screening assumption is not, by itself, proof of violating an indoor limit.

References: [FHWA Noise Measurement Handbook, section 6](https://www.fhwa.dot.gov/Environment/noise/measurement/handbook.cfm); [ASTM E966 facade field sound attenuation](https://store.astm.org/standards/e966); [Iowa Supreme Court, Singer v. City of Orange City (2024)](https://www.iowacourts.gov/iowa-courts/supreme-court/supreme-court-opinions/case/23-1600).

## Preconstruction indoor acoustic baselines and HVAC measurement protocol

The current **proposed** §165.11(G)(5) requires the applicant to offer voluntary, applicant-funded **indoor preconstruction baseline tests** at selected existing neighboring sensitive-receptor structures before construction changes local sound. Qualified acoustic professionals document **daytime and nighttime dBA and dBC Leq,1h** with doors and windows closed, measure in the normally occupied source-facing room, and document indoor background sources. Comparable postconstruction testing should use the same room and operating conditions.

**Dwellings equipped with a controllable forced-air HVAC system:** The thermostat is set within **65°F–75°F** where practicable and safe. The HVAC **circulation fan is set to ON (continuous) for the entire indoor sound measurement**, explicitly **not AUTO**. Heating/cooling calls may cycle under normal thermostat controls, but the blower continues to run between cycles. Document actual continuous operation, fan mode/speed, setpoint, indoor temperature, HVAC cycles, ventilation and anomalies. A qualified acoustician must account for HVAC background potentially masking source-related sound. The 65–75°F and fan-ON requirements are draft **local test conditions**, not thermal or acoustic requirements established by the Iowa energy code.

Owner/occupant **may refuse voluntary indoor testing**. With lawful exterior access, measure the **parcel boundary closest to the industrial use**, or a properly documented, legally accessible representative fallback. Indoor levels inferred from such exterior sound must be identified as **modeled estimates** and use source-frequency-specific outdoor-to-indoor noise reduction or acoustical facade transmission loss. An insulating **R-value never converts directly to dBA or dBC**. Differences in baseline quality and measurement uncertainty must be documented.

A claim that the project **caused an increase** should rely on supported like-for-like indoor pre- and postconstruction comparisons, including facility-attributable levels and uncertainty. **Do not infer that a home must have been completely silent**, or that an occupant must have allowed a baseline test in order to report a current exceedance of an absolute noise threshold or use a nuisance remedy.

See [current ordinance §165.11(G)(4)-(5)](https://github.com/ttbakiatwoam/cascade-data-center/blob/master/proposals/DRAFT-ORDINANCE-M2-DATA-CENTER-PERFORMANCE-STANDARDS-2026-11-03.md), [operational noise explanation](https://ttbakiatwoam.github.io/cascade-data-center/operational-noise/), and [Iowa residential noise attenuation research](https://ttbakiatwoam.github.io/cascade-data-center/house-noise-attenuation-iowa/).
