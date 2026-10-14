# Noise and Acoustics

> This file distinguishes health guidance, acoustic engineering principles, and enforceable Iowa comparator standards. None of the external standards cited here automatically applies to the Cascade proposal unless adopted or incorporated into an approval.
>
> Last reviewed: 2026-10-13

## Why data-center noise requires more than one dB number

Potential continuous sources can include:

- cooling fans and dry coolers;
- container or server fans;
- pumps;
- transformers and substations;
- generators during tests or outages;
- air-handling equipment;
- tonal or low-frequency mechanical/electrical components.

A useful acoustic review should identify source locations, source sound-power/sound-pressure data, barriers/buildings, terrain, ground conditions, weather assumptions, receptor locations, operating modes, tonal characteristics, and nighttime conditions.

## dBA and dBC

A-weighted levels (dBA) approximate human hearing sensitivity and are widely used for community-noise regulation. C-weighted levels (dBC) retain more low-frequency energy. Linn County's ordinance uses both dBA and dBC limits, making it a particularly relevant Iowa example for facilities with persistent low-frequency mechanical sound.

## Tonal noise

A steady tonal component can be more noticeable or annoying than broadband sound at the same overall level. Jones County's data-center ordinance reduces its permissible sound limit by 5 dB when a steady pure tone is present. This is an example of regulating the acoustic character of a facility, not merely average volume.

## Distance and propagation

Federal Highway Administration acoustic guidance explains the basic free-field relationship that a point source decreases approximately 6 dB per doubling of distance, while an ideal line source decreases approximately 3 dB per doubling. Real industrial-site predictions require more than this rule of thumb: barriers, source geometry, ground, terrain, atmosphere, multiple sources, reflections, and frequency content all matter.

Accordingly, a simple distance calculation is useful for screening but should not replace an engineered site model.

## Iowa comparator standards

### Linn County

The 2026 Linn County data-center ordinance includes hourly-average limits measured at adjacent occupied structures:

- residential: 55 dBA and 65 dBC;
- nonresidential: 65 dBA and 75 dBC.

The ordinance also provides for acoustic evaluation before/after development and periodic reevaluation after buildout. Certain elevated-noise maintenance/testing activities are generally limited to specified daytime hours unless approved.

### Jones County

The 2025 Jones County ordinance includes:

- 60 dB daytime;
- 50 dB nighttime;
- a 5 dB reduction for steady pure tones;
- applicant-funded third-party noise profiling.

These are comparator policies, not current Cascade limits.

## WHO guidance

The World Health Organization's environmental and night-noise publications provide health-based guidance for environmental noise and sleep. They are not Iowa zoning law. They are useful as background when evaluating persistent nighttime noise and the distinction between regulatory compliance and health-protective planning.

## Everyday-sound comparisons

Consumer-device or household sound levels can help readers understand the decibel scale, but such comparisons should not be used as substitutes for a facility acoustic study. For example, ResMed publishes approximately 27 dBA sound-pressure level for an AirSense 11 configuration under its specified test standard. A single appliance measured near the device is acoustically different from multiple outdoor industrial sources operating continuously.

## LEED certification: indoor acoustics versus exterior neighborhood sound

Simple Mining's October 1 **LEED design goal** is not an earned certificate or a binding residential noise limit. See the [updated USGBC credit and local ambient analysis](34_LEED_CERTIFICATION_ACOUSTICS_AND_EXTERIOR_NOISE.md) and [website guide](../../docs/leed-and-noise.md).

**Distinct credit types and history:**
- **LEED v4.1 BD+C Data Centers:** optional **indoor** Acoustic Performance credit, not an outdoor community sound limit.
- **LEED v5 BD+C New Construction:** optional Sound Environment design and measurement pathway. It is not automatically an enforceable cap at nearby homes.
- **Exterior Noise Control Pilot Credit 57:** optional pilot. The **original 2011 text** used **5 dBA below pre-project ambient Ldn and no more than 60 dBA** at the nearest property line/right of way. The **June 4, 2015 revision** instead specifies **45 dBA Leq(8h)** for project sound at boundaries adjacent to residential buildings, with **Lmax no greater than existing ambient and no greater than 60 dBA**. At other boundaries it uses **60 dBA Ldn/CNEL**. Emergency generator noise is excluded from its numeric requirement, with an operating/testing plan still required. **Neither version is a condition of ordinary LEED certification**, and availability/eligibility for Cascade remains unverified.

Earlier claims that Pilot 57 had **no 45 dBA provision** were incorrect because they relied on the older PDF. The revised credit language and 2015 change history appear in [LEEDuser's reproduction of the USGBC credit text](https://leeduser.buildinggreen.com/credit/Pilot-Credits/EQpc57). [Archived original USGBC PDF](https://s3.amazonaws.com/legacy.usgbc.org/usgbc/docs/Archive/General/Docs10404.pdf).

**Existing Cascade noise:** In the **October 1 public forum** at roughly **1:24:26**, a neighbor says she hears work at a nearby building when opening her doors. The YouTube automatic captions do **not confirm the business name**. One informal personal measurement reportedly found **roughly 60 dB** near the area, but without meter weighting, location, dates, sample period or calibration, it is **not an established 60 dBA Ldn/Leq baseline**. A [2026 federal labor posting](https://seasonaljobs.dol.gov/jobs/H-400-25364-516568) shows **Cascade Lumber Company** planned truss production involving staple guns, hammers and nailing on a shift ending **1 a.m.** It does not prove 24-hour uninterrupted use of all machinery.

Hearing one facility across the industrial park **does not mean every business between it and a home can be heard**, nor that residents cease to have grounds for noise complaints. Sound travels unevenly and different sources can add nighttime noise, tonal components or peak events. It does show **industrial noise already exists**, which is relevant to pre-construction baselines, source attribution, cumulative impacts and neutral, district-wide noise controls.

**Engineering and policy response:** Obtain calibrated multi-day **day/night receptor measurements**, with **dBA/dBC, Ldn, Leq, Lmax, narrowband tonal analysis**, the time of night and existing industrial contributors clearly documented. Model the **incremental new facility sound** and **total combined sound** at actual nearby homes under several operations scenarios. Adopt neutral standards applicable to similarly situated **M-2 businesses**, independently of LEED.

## Cooling equipment may cycle or change speed: continuous workload is not fixed noise

**Acoustical distinction:** Data centers produce heat continuously while computing, but **individual cooling components do not necessarily run at a fixed speed or duty cycle**. Refrigerant compressors (where installed) can stage, modulate, or stop when other cooling methods suffice; outdoor dry-cooler/air-cooled-condenser fans can stage or use variable-speed drives, and fans, pumps and transformers may still operate while compressors are off. Neither continuous operation of the facility nor a changing control sequence establishes a constant external sound level.

- [ENERGY STAR](https://www.energystar.gov/products/data_center_equipment/5-simple-ways-avoid-energy-waste-your-data-center/replace-standard-fans-variable-speed-fans) documents data-center computer-room conditioning fan-speed control to track changing heat loads.
- [ENERGY STAR's sensors and controls guidance](https://www.energystar.gov/products/data_center_equipment/16-more-ways-cut-energy-waste-data-center/use-sensors-and-controls) explains modulation of cooling capacity and airflow based on sensor readings near servers.
- [DOE, Cooling Water Efficiency Opportunities for Federal Data Centers](https://www.energy.gov/cmei/femp/cooling-water-efficiency-opportunities-federal-data-centers) explains that data centers require cooling day and night, but airside/waterside economizers can reduce or replace compressor-intensive refrigeration under suitable outdoor conditions.
- [ASHRAE, AI Data Center Energy Performance Framework](https://www.ashrae.org/technical-resources/topics-and-initiatives/ai-data-center/energy-and-thermal-efficiency) specifically describes **dry coolers** rejecting heat without mechanical chiller compressors when ambient conditions permit and variable fan controls tied to thermal load.
- [Seresco NG Series Dry Coolers operation manual (January 2022)](https://dehumidifiedairservices.com/wp-content/uploads/2023/05/Seresco-NG-Series-Dry-Coolers-OMM-Jan-2022.pdf) documents dry-cooler fan speeds between 0 and 100% using EC controls and switching/staging strategies as fluid temperature changes. **This is a technology example, not a confirmed Simple Mining supplier or design**.

**Cascade-specific caution:** The October 1 proposal called its concept **closed-loop hydrocooling with dry/air-cooled heat rejection**. A dry cooler typically rejects heat through a finned heat exchanger and fans. It is not automatically the same device as a house's **refrigerant compressor**. Whether this project includes conventional compressors at all, how pumps/fans are controlled, when units stop or run slowly, and how much sound occurs at receptors cannot be established without the final mechanical schedule.

**Noise may be variable but still present.** Lower cooling demand and cooler ambient conditions can allow equipment to slow, stage off, or operate differently. Yet a 24/7 heat source may require fans/pumps to operate **even at night**, and other sources such as electrical transformers may persist regardless of cooling. Variable-speed and cycling fans may also change tonal frequencies or create noticeable on/off events. We cannot assume cooling equipment always turns off at a thermostat setpoint, **nor assume that a constant, equal-amplitude hum is guaranteed**.

**For an independent Cascade acoustic model and enforceable neutral M-2 limits:** show **minimum / typical / maximum fan speeds** with day, night, summer heat, cooler-weather and full-IT-load cases; clearly identify compressor versus dry cooler, pump and transformer contributions; model on/off transitions, multiple units running together, prominent tones, dBA and dBC, receptor distances and ambient backgrounds; verify with post-construction time-series measurements. Compliance must hold in realistic **worst-case operating conditions**, not just the quietest duty cycle.

## October 1 Cascade forum update

Simple Mining's October 1 presentation added preliminary project-specific noise representations. The presenter discussed roughly **50 dB** in describing hydro-cooling noise/property-line conditions and repeatedly said the company wanted a clear, enforceable property-line limit. During Q&A, the company acknowledged that hotter-weather cooling can be louder and stated that **50 dB was not a guaranteed constant level 24/7**. A limit around **65 dB at the property line** was discussed as an example the company believed it could meet.

The company also said backup generators would be enclosed and subject to the same overall compliance framework. However, no final acoustic model, low-frequency/tonal analysis, hot-day full-load model, generator-test model, or independent acceptance study was presented. When specifically asked about propagation modeling, the response indicated such modeling could be performed rather than demonstrating that it already existed.

Accordingly, the forum changes the evidence status from “no project-specific representation” to **company representation/preliminary**, not to independently verified acoustic performance.

See [`../updates/28_SIMPLE_MINING_COMMUNITY_FORUM_2026-10-01.md`](../updates/28_SIMPLE_MINING_COMMUNITY_FORUM_2026-10-01.md).

## Recommended project-specific evidence

Before final approval, a robust Cascade record could include:

1. baseline ambient measurements at representative property/receptor locations;
2. engineered pre-construction acoustic model at full buildout;
3. separate dBA and low-frequency/tonal analysis;
4. daytime and nighttime operating scenarios;
5. normal operation, maximum cooling, generator testing, and emergency operation;
6. post-construction independent verification;
7. recurring compliance tests;
8. complaint-triggered testing;
9. enforceable mitigation if limits are exceeded.

Potential mitigation includes source selection, fan-speed controls, equipment orientation, enclosures, silencers, barriers/berms, setbacks, building shielding, and operating restrictions for nonessential testing.

## Open Cascade evidence gap

No project-specific **final** acoustic study or full-buildout property-line/residential prediction has been located. The October 1 forum supplied company noise estimates and willingness to accept an enforceable limit, but those statements should not be treated as a substitute for modeling and measurement.


## New research: low-frequency sound, infrasound, and bird predation

**dBC versus vibration.** A C-weighted sound-pressure level (dBC) retains more low-frequency acoustic energy than dBA, but does not specify the spectral frequencies, measure physical ground/building vibration, or demonstrate a medical outcome. Evaluate sound spectra and measured vibration separately where required.

**Human health evidence.** Baliatsas et al. (2016) systematically reviewed seven observational studies. Their findings included associations between low-frequency noise and annoyance, sleep problems, concentration difficulty, and headaches, but **very limited evidence concerning chronic medical diseases**. This is neither proof that a small hum causes disease nor proof that every intensity is harmless. A blinded 2023 crossover study of 37 noise-sensitive but otherwise healthy adults found **no measured adverse effects from 72 hours of inaudible simulated wind-turbine infrasound** versus sham. In the same study, **audible traffic noise** worsened sleep. These sound exposures are not equivalent to a proposed data center; an audible tonal mechanical hum cannot be assumed harmless based on inaudible wind-turbine infrasound.

**Avoid an unsupported health claim:** Research does **not** establish that only people with a diagnosed underlying condition or a preexisting sleep disorder can experience sleep disturbance from industrial sound. Vulnerability varies, and sleep disturbance is a health-relevant outcome even without established chronic disease.

**Wildlife evidence and an important limitation.** Francis, Ortega, and Cruz (2009), studying **natural-gas compressor sites in New Mexico**, observed **lower nesting bird-species richness** in noisy habitats but **higher reproductive success for certain birds** associated with predator-prey changes and reduced nest predation. This is not a study of data centers. It did **not** demonstrate that data centers chase off cats or foxes, bring back insects, or restore wildlife habitat in Cascade. Effects differ by species and habitat.

Original research:

- Baliatsas et al. (2016), *Health effects from low-frequency noise and infrasound*: https://pubmed.ncbi.nlm.nih.gov/26994804/
- Marshall et al. (2023), *The Health Effects of 72 Hours of Simulated Wind Turbine Infrasound*: https://pmc.ncbi.nlm.nih.gov/articles/PMC10032045/
- Francis et al. (2009), *Noise Pollution Changes Avian Communities and Species Interactions*: https://pubmed.ncbi.nlm.nih.gov/19631542/
- WHO, *Protecting people from harmful exposure to environmental noise*: https://www.who.int/europe/health-topics/noise/protecting-people-from-harmful-exposure-to-environmental-noise

For proposed enforceable standards and the uncertainty relevant to **this** site, see the [public objections evidence review](../evidence/31_PUBLIC_OBJECTIONS_EVIDENCE_REVIEW.md). These references are comparative studies, not measured Cascade impacts.

## Navy aircraft carriers, submarines and duration of sound exposure

**New comparison reviewed October 13, 2026:** [Expanded research on naval shipboard noise, hearing risk, sleep and long-duration exposure](33_NAVAL_SHIPBOARD_NOISE_SLEEP_AND_LONG_DURATION_EXPOSURE.md). These are **occupational/maritime comparators**, not measurements at the proposed Cascade data center.

**Carrier personal exposure:** A 2019 U.S. Navy study measured 59 sailors during a 2014 five-day underway period. **93% exceeded the study's 24-hour 80 dBA occupational noise threshold** and **61% exceeded 70 dBA off-duty**, a benchmark for **auditory recovery**. These results do not mean 93% had diagnosed hearing loss, and the auditory-recovery comparison is **not a residential nighttime limit**. In a separate 2019 carrier-berthing study, **72% of 60 noise measurements** across eight sleeping locations exceeded 70 dBA; that percentage refers to **measurements**, not sailors.

**Cumulative hearing effects:** A 2007 retrospective study of hearing records for **nearly 268,000 enlisted sailors (1979–2004)** found an estimated **13-percentage-point greater probability of hearing reduction** in a model of half a 30-year career aboard surface warships compared with service ashore. This is stronger long-term occupational **hearing** evidence, not a direct test of quiet low-frequency sound.

**Measured noise and sleep:** A 2016 Royal Norwegian Navy study directly paired **83 sleep periods among 68 sailors** with sleep-time cabin noise measurements. Higher equivalent levels and more noise events were associated with more sleep movement; more events were associated with worse sleep efficiency. The study sampled different surface vessel types, **not just submarines**. A larger U.S. Navy berthing study (1,269 sailors) associated **combined habitability complaints** including noise, light and temperature with poorer perceived sleep and mood, but did not isolate noise as the cause.

**Submariners and sleep:** A **2024 U.S. Navy 30-day study** of **58 submariners** found **77.8%** met criteria for poor subjective sleep quality underway, yet **68.8%** already reported poor quality ashore; the researchers did **not** isolate machinery noise. A **2015 French 70-day patrol** study of **19 submariners** found **no significant deterioration in objectively measured sleep between days 21 and 51** under an organized schedule and controlled environment. Neither finding establishes the lifelong health effects of low-level mechanical hum.

**How to use this evidence:** A **72-hour** inaudible-infrasound experiment cannot settle years-long exposure, but multi-month military deployment alone does not isolate noise without appropriate measurements and controls. The defensible Cascade response is an independent **day-and-night residential acoustic model**, considering **dBA, dBC, tonal peaks, spectral content, noise events, and background conditions**, with post-build verification. Keep **hearing conservation limits** distinct from **community sleep guidance**. Apply impact-based rules to **all similarly situated M-2 industries**, not only data centers.

Selected primary studies:
- Schaal et al. (2019), 24-hour carrier exposures: https://pubmed.ncbi.nlm.nih.gov/30855086/
- Schaal et al. (2019), aircraft carrier berthing levels: https://pubmed.ncbi.nlm.nih.gov/31260521/
- Rovig et al. (2004), carrier flight deck versus engineering and administrative hearing results: https://pubmed.ncbi.nlm.nih.gov/15281670/
- Trost and Shaw (2007), 1979–2004 Navy service and hearing records: https://pubmed.ncbi.nlm.nih.gov/17484318/
- Sunde et al. (2016), Norwegian Navy noise dosimetry and actigraphic sleep: https://pubmed.ncbi.nlm.nih.gov/26960785/
- Matsangas and Shattuck (2021), U.S. Navy berthing habitability: https://pubmed.ncbi.nlm.nih.gov/32109155/
- Chabal et al. (2024), U.S. submarine 30-day sleep study: https://pubmed.ncbi.nlm.nih.gov/38820921/
- Trousselard et al. (2015), French submarine 70-day patrol: https://pubmed.ncbi.nlm.nih.gov/26016656/
- Marshall et al. (2023), 72-hour inaudible infrasound controlled study: https://pmc.ncbi.nlm.nih.gov/articles/PMC10032045/

## Sources

### Iowa comparators

- Linn County approved data-center ordinance: https://www.linncountyiowa.gov/DocumentCenter/View/27695/PA26-0001-Ordinance-PDF
- Jones County data-center ordinance: https://www.linncountyiowa.gov/DocumentCenter/View/27656/Jones-County-Data-Center-Ordinance

### Health guidance

- WHO — Environmental Noise Guidelines for the European Region: https://www.who.int/europe/publications/i/item/9789289053563
- WHO — Night Noise Guidelines for Europe: https://www.who.int/europe/publications/i/item/9789289041737
- WHO — Noise fact sheet: https://www.who.int/europe/news-room/fact-sheets/item/noise
- WHO — Night Noise Guidelines PDF: https://iris.who.int/bitstream/handle/10665/326486/9789289041737-eng.pdf

### Acoustic principles

- FHWA — Three-Part Approach / Sound Propagation: https://www.fhwa.dot.gov/Environment/noise/regulations_and_guidance/analysis_and_abatement_guidance/polguide01.cfm
- FHWA — Acoustical Considerations: https://www.fhwa.dot.gov/Environment/noise/noise_barriers/design_construction/design/design03.cfm
- FHWA — Noise Measurement Handbook: https://www.fhwa.dot.gov/ENVIRonment/noise/measurement/handbook.cfm
- FHWA — Traffic Noise Model and Tools: https://www.fhwa.dot.gov/Environment/noise/traffic_noise_model/
- Noise Pollution Clearinghouse — Household noise levels: https://www.nonoise.org/library/household/
- CDC — What Causes Noise-Induced Hearing Loss: https://www.cdc.gov/hearing-loss/causes/
- ResMed — AirSense 11 User Guide / declared sound values: https://document.resmed.com/documents/products/machine/airsense-11/user-guide/398291_airsense-11_user-guide_amer_multi.pdf

## Preliminary site distances, October 13, 2026

The September 25 preliminary concept and an October 13 county-parcel screenshot indicate a separate **400.50-foot** parcel between the Simple Mining east lot line and residential lot lines. After allowing for the visible roofline setback and the proposed structures' own setback inside the Simple Mining parcel, a project-generated screening estimate is **~610 ft cooling yard**, **~640 ft electrical yard**, **~670 ft main building**, and **~1,020 ft substation** to a nearby visible roofline. These are **not surveyed measurements**. The approximate building location can shift with final design, and the equipment edges are partly obscured by annotation labels.

These distances improve receptor selection for a future acoustic study but **cannot predict sound exposure** by themselves. See [the fully documented scale and plan assumptions](../project/35_PRELIMINARY_FACILITY_TO_HOME_DISTANCES_2026-10-13.md) and [the public illustrated page](../../docs/site-distances.md).
