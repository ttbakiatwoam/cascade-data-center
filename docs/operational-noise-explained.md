---
layout: page
title: Operational Noise Explained
permalink: /operational-noise/
---

# Operational Noise: Understanding the proposed M-2 standards

> **Status: November 3, 2026.** This is a plain-language explanation of the proposed M-2 ordinance, **not current City of Cascade law**. It does not replace an acoustical study or the City Attorney's review. The limits below are **proposed**, and the source is [§165.11(G)(4) of the November 3 working draft]({{ '/draft-ordinance/' | relative_url }}#4-operational-noise).[^1]

The proposal creates **two separate checks** on noise from any M-2 industrial use. One is made at its property boundary. The other protects existing homes and other sensitive places. **Both the A-weighted and C-weighted limits must be met** at each applicable location.

## The proposed limits, at a glance

| Where sound is evaluated | 7:00 a.m.–10:00 p.m. | 10:00 p.m.–7:00 a.m. |
| --- | --- | --- |
| **Any M-2 property boundary** | **65 dBA and 75 dBC** | **65 dBA and 75 dBC** |
| **Inside a dwelling or other sensitive-receptor structure, doors and windows closed** | **55 dBA and 65 dBC** | **50 dBA and 60 dBC** |

The property-boundary limit does not change at night. The different nighttime limits apply **inside occupied sensitive structures**, not automatically at every industrial boundary.

The sensitive-receptor list includes an **existing dwelling, school, licensed child-care facility, hospital, nursing facility, place of worship, public library, or comparable occupied sensitive use**. The measurement would be made in the **nearest normally occupied room on the source-facing side**, initially at the closest qualifying occupied structure. The microphone would be **within five feet of the interior surface of the nearest exterior wall**, normally **at least 1.5 feet away from reflective surfaces**, about four to five feet above the floor. **All doors and windows must be closed**. An acoustician would also check other qualifying structures where sound might be greater because of terrain or equipment direction. Indoor entry requires consent or other lawful authority.[^6][^7]

**Important change in protection:** This replaces the original exterior-wall/outdoor-use-area measurement. A closed building generally reduces outside sound, so **the same 50 dBA nighttime limit is considerably less protective when measured indoors**. WHO guidance uses **30 dBA Leq indoors at night for bedrooms** as a sleep-related benchmark. That is guidance, not Iowa law. The draft deliberately preserves its earlier numbers for committee discussion, and they **need independent acoustical review before adoption**.[^8] Outdoor patios and yards are no longer checked under this separate sensitive-receptor limit, though the M-2 property-line limit remains.

## 1. What do dBA and dBC mean?

- **dBA (A-weighted):** A filter that roughly follows human hearing sensitivity and strongly discounts many low-frequency sounds. It is common in community-noise assessment.[^2]
- **dBC (C-weighted):** A flatter filter that retains substantially more low-frequency sound energy. It can help identify bass-heavy machinery that an A-weighted result may understate.[^2]

These are **different measurements of the same sound**, not two types of equipment. **C-weighting does not measure building or ground vibration directly.** A separate vibration method would be needed for that.

**Example:** If a machine contributes **63 dBA and 79 dBC at the M-2 property line**, it satisfies the proposed dBA limit but **fails the 75 dBC limit**. Both must pass.

### What about a distinct hum or whine?

Proposed **§4(c)** lowers the **A-weighted** limit by **5 dB** when there is a prominent recurring tone, whine, screech, or hum. The text does not apply that deduction to the C-weighted limit.

| Location / time | Regular proposed dBA limit | With qualifying tonal sound |
| --- | ---: | ---: |
| M-2 property line | 65 dBA | **60 dBA** |
| Sensitive receptor, daytime | 55 dBA | **50 dBA** |
| Sensitive receptor, nighttime | 50 dBA | **45 dBA** |

Whether a tone qualifies should be established through a documented professional method, not simply personal impression.

## 2. What does “hourly average” mean?

Proposed **§4(d)** defines the one-hour average as **Leq,1h**, the energy-equivalent continuous sound level. It is **not** an ordinary arithmetic average of decibel readings. Louder events count disproportionately because decibels are logarithmic.[^3]

**Illustrative example:** If a facility alone produced **80 dBA for one minute** and no sound for the remaining 59 minutes, its one-hour Leq would be about **62.2 dBA**. That is below the proposed 65 dBA property-line limit, even though the brief event was louder. The example ignores existing background sound, tonal penalties, other rules, and other operating periods.

**Important:** This section does **not create a separate maximum instantaneous level (Lmax)**. Other rules, including generator-testing hours and applicable nuisance law, may still matter. The revised §4(b) expressly applies **Leq,1h** to the indoor sensitive-receptor limits.

## 3. What if the neighborhood is already noisy?

The draft regulates noise **“attributable to the use”**, not every sound a meter hears. Traffic, other industrial operations, wind, and birds may contribute to the total. The qualified professional must record background conditions and use a documented method to estimate the facility's contribution. ANSI/ASA S12.9 Part 3 includes methods for correction for background sound.[^4]

**Illustrative calculation, not a Cascade measurement:**

| Sound contribution | Hypothetical level |
| --- | ---: |
| Background without the facility | 60 dBA |
| Facility by itself | 63 dBA |
| **Both together** | **about 64.8 dBA** |

These levels are combined **logarithmically**, not by adding 60 and 63. Conversely, if a properly comparable total measurement is **67 dBA** and background is **60 dBA**, the facility contribution would be roughly **66 dBA**, rather than 7 dBA. That would exceed a 65 dBA source-attributable limit under those assumptions.[^3]

A roughly **60 dB informal reading** was discussed in earlier local research, but its weighting, measurement duration, location, instrument quality, and operating conditions were not established. It is **not a certified 60 dBA baseline** for Cascade.[^5]

## 4. Does a parcel between the industry and a house change anything?

It can matter for **setbacks or adjacency rules**, but **not the existence of the sensitive-receptor noise check**.

Think of the locations in order:

**M-2 facility → industrial property boundary → intervening parcel → occupied room inside the existing home (doors/windows closed).**

The facility must satisfy the property-line rule where applicable. It also must satisfy the sensitive-receptor rule **inside the home**, even without a shared property boundary. The home's actual location, building attenuation, and acoustical exposure must be established by mapping and professional assessment. Indoor testing requires consent or lawful access; when access is unavailable, professionally modeled levels should be clearly identified as estimates rather than verified measurements. [See the preliminary site-distance research]({{ '/site-distances/' | relative_url }}).

That distinction matters in Cascade because an intervening parcel has been discussed for the proposed site. The presence of a parcel between properties **does not prove compliance**, and it does **not by itself establish the shortest distance** from equipment to a home.

## 5. What happens with generators, existing businesses, and major facilities?

- **All M-2 uses:** The proposed operational limits are drafted as district-wide performance requirements, not special restrictions on data centers alone. Proposed §165.11(G)(2) separately addresses lawful preexisting uses and nonconforming situations; it does **not** establish that every older business must retrofit immediately.
- **Generators:** Under proposed §165.11(G)(6), routine elevated-noise generator testing is generally limited to **8 a.m.–6 p.m., Monday–Friday**, with listed emergency, safety, regulatory, and authorized exceptions. These hours are **additional to**, not a replacement for, the noise provisions.
- **Major Industrial Facilities:** Proposed §165.11(G)(5) calls for preconstruction baseline work, a full-operating-condition model, post-startup verification, and testing at least every three years or after certain material changes. This is an extra study requirement triggered by the draft's neutral impact thresholds.

The facility's loudest reasonably anticipated conditions matter, including hot-weather cooling, multiple operating units, and appropriate generator scenarios. A single quiet-day reading is not a full compliance demonstration.

## 6. Questions to resolve before adoption

The existing draft already calls for a qualified acoustical professional, a calibrated **Type 1 or Type 2** meter, A/C frequency weighting, weather and background documentation, and an ANSI/ASA S12.9-based method. That is useful groundwork. The remaining decisions should be made explicit:

1. **Reassess the indoor limits.** The 55/50 dBA residential numbers were written for outdoor measurement. Decide whether to lower them for occupied indoor rooms and whether an outdoor living-area standard should remain.
2. **Confirm microphone placement.** Evaluate the draft's 1.5-to-5-foot wall distance, room selection, window clearance, and special low-frequency test positions with an acoustician.
3. **Background correction?** Identify the applicable standard, acceptable measurement conditions, and treatment of uncertainty when source and background levels are close.
4. **Intermittent peaks and tones?** Decide whether a separate event maximum, tonal test, or correction is needed.
5. **Multiple industries?** Explain how individual responsibility is assigned when several nearby businesses contribute sound.
6. **Existing operations?** Confirm how any adopted amendment would interact with nonconforming uses, equipment replacement, and the City's authority to enforce it.

**A useful committee test:** If a meter reads **67 dBA** at a property line while the matching preexisting background is **60 dBA**, can two qualified engineers follow the ordinance and arrive at the same compliance decision?

The objective is a rule that protects residents **and** gives every M-2 business a measurable, predictable way to comply.

---

## Sources and related research

[^1]: Cascade Data Center research project, [*Draft M-2 Heavy Industrial District Performance Standards*, November 3, 2026](https://github.com/ttbakiatwoam/cascade-data-center/blob/master/proposals/DRAFT-ORDINANCE-M2-DATA-CENTER-PERFORMANCE-STANDARDS-2026-11-03.md), proposed §165.11(G)(2), (4)–(6). This is draft local policy, not adopted City law.
[^2]: U.S. Occupational Safety and Health Administration, [*Technical Manual*, Section III, Chapter 5, “Loudness and Weighting Networks”](https://www.osha.gov/otm/section-3-health-hazards/chapter-5). OSHA's workplace rules are **not** the proposed community limits.
[^3]: Federal Highway Administration, [*Noise Measurement Handbook*](https://www.fhwa.dot.gov/Environment/noise/measurement/handbook.cfm), definitions of equivalent continuous sound level and formulas for combined noise.
[^4]: Acoustical Society of America / ANSI, [*ASA/ANSI S12.9-2013/Part 3 (R2023): Short-term Measurements with an Observer Present*](https://webstore.ansi.org/standards/asa/asaansis122013partr2023-2504997), scope and background-correction procedures. The exact method to use should be adopted clearly and reviewed by an acoustician.
[^5]: [*LEED and Neighborhood Noise*]({{ '/leed-noise/' | relative_url }}) and [the source-based noise research](https://github.com/ttbakiatwoam/cascade-data-center/blob/master/dataset/impacts/08_NOISE_AND_ACOUSTICS.md), which distinguish informal reported ambient sound from a professional baseline.
[^6]: International Organization for Standardization, *ISO 1996-2:2017*, <https://www.iso.org/standard/59766.html>, environmental sound assessment with indoor-placement guidance. The five-foot rule is proposed Cascade language, not an ISO requirement.
[^7]: Acoustical Society of America / ANSI, *S12.72-2015 (R2025)*, <https://webstore.ansi.org/standards/asa/asaansis12722015r2025>, and *S12.9-2016/Part 7 (R2025)*, <https://webstore.ansi.org/standards/asa/asaansis122016partr2025>, indoor ambient and low-frequency sound measurement methods.
[^8]: World Health Organization, *Guidelines for Community Noise* (1999), <https://www.who.int/publications-detail-redirect/a68672>, indoor nighttime bedroom reference (30 dBA Leq); nonbinding guidance.

[Return to the current draft ordinance]({{ '/draft-ordinance/' | relative_url }}) · [Browse the Research Library]({{ '/research-library/' | relative_url }})
