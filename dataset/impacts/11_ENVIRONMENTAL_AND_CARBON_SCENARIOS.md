# Environmental and Carbon Scenarios

> **Important:** the calculations in this file are illustrative research scenarios, not forecasts for the proposed Cascade project. Where earlier scratch-work assumptions cannot be fully reconstructed, the result is preserved as historical context but explicitly marked non-authoritative.
>
> Last reviewed: 2026-09-10

## Environmental categories considered

The project has compared industrial-compute development and agricultural land use across more than carbon alone:

- operational electricity/fuel use;
- lifecycle electricity-generation emissions;
- construction materials;
- agricultural machinery fuel;
- fertilizer-related emissions;
- agricultural-soil nitrous oxide;
- crop drying;
- erosion and nutrient runoff;
- site stormwater and drainage;
- cooling-water demand;
- land conversion/restoration;
- decommissioning and waste.

The core methodological conclusion is that an environmental comparison must define a scenario and a boundary. A claim such as “a data center emits more than a farm” or “a farm is worse than a data center” is incomplete without identifying what emissions, energy sources, acreage, period, cooling design, crop practices, and lifecycle stages are included.

## Prior 100 MW / 10-year electricity scenario

A prior project exercise intentionally assumed a hypothetical data center drawing **100 MW continuously for 10 years** and powered by nuclear generation. This was an illustrative scenario selected to test scale, not a statement about Simple Mining's Cascade design or power source.

Energy calculation:

```text
100 MW × 1,000 kW/MW × 8,760 hours/year × 10 years
= 8,760,000,000 kWh
= 8.76 TWh
```

NREL's life-cycle assessment work shows nuclear and renewable generation have much lower lifecycle greenhouse-gas emissions per kWh than fossil generation. Using an illustrative nuclear lifecycle factor around 12 g CO2e/kWh produces approximately:

```text
8.76 billion kWh × 12 g CO2e/kWh
= 105.12 billion g CO2e
= approximately 105,120 metric tonnes CO2e
```

This number describes the **assumed electricity-generation lifecycle factor applied to the hypothetical energy demand**. It is not direct on-site data-center emissions, does not include every possible facility/construction lifecycle component, and must not be attributed to Cascade.

## Prior 100-acre agricultural comparison

Earlier research also developed rough 10-year estimates for a hypothetical 100-acre row-crop operation, including machinery fuel, fertilizer-production energy, agricultural-soil nitrous oxide, and crop drying. The prior scratch analysis produced order-of-magnitude results in the hundreds rather than tens of thousands of tonnes CO2e.

However, the complete original assumption table—crop rotation, nitrogen application rate, field operations, yield, drying requirement, fuel usage, and emission-factor version—was not preserved cleanly enough to make those totals reproducible from this dataset. Therefore the earlier numeric farm totals should **not** be cited as a finished result.

A future version should reconstruct the calculation transparently from:

1. Iowa State field-operation fuel requirements;
2. EIA fuel carbon factors;
3. EPA agricultural-soil/N2O methodology;
4. documented fertilizer-production factors;
5. crop-specific drying assumptions;
6. crop rotation/yield/fertilizer assumptions.

## Agricultural greenhouse-gas context

EPA identifies agricultural soils and fertilizer-related nitrous oxide as important agricultural greenhouse-gas sources. Iowa DNR's statewide greenhouse-gas inventory likewise shows agriculture as a major share of Iowa emissions, with agricultural soils a substantial contributor.

This is statewide context only; it is not an estimate of emissions from the Cascade Industrial Park parcel or any specific nearby farm.

## Stormwater and land conversion

Industrial development typically increases impervious surface and changes drainage patterns. A meaningful data-center environmental review should therefore include pre/post-development runoff, detention/retention, downstream capacity, erosion control, spill containment, and restoration/decommissioning.

Agricultural land has different impacts, including soil erosion and nutrient runoff. Iowa's Nutrient Reduction Strategy and STRIPS research provide evidence for those impacts and for mitigation strategies.

## Direct vs. indirect emissions

For a data center, it is useful to separate:

- **Scope-like direct site emissions:** primarily backup generators, onsite fuel combustion, refrigerants, construction, and maintenance sources;
- **electricity-related emissions:** determined strongly by generation mix and contractual/grid accounting;
- **embodied/lifecycle emissions:** servers, electrical equipment, concrete/steel, generation assets, and replacement cycles.

A nuclear-, wind-, hydro-, gas-, or coal-supplied 100 MW load can have radically different lifecycle carbon intensity even though the computing facility consumes the same number of kWh.

## Sources

- NREL — Life Cycle Greenhouse Gas Emissions from Electricity Generation: https://www.nrel.gov/docs/fy13osti/57187.pdf
- NREL — LCA Harmonization Project: https://www.nrel.gov/analysis/life-cycle-assessment.html
- U.S. EIA — Carbon Dioxide Emissions Coefficients by Fuel: https://www.eia.gov/environment/emissions/co2_vol_mass.php
- U.S. EPA — Agriculture Sector Emissions: https://www.epa.gov/ghgemissions/agriculture-sector-emissions
- U.S. EPA — Nitrous Oxide Emissions: https://www.epa.gov/ghgemissions/nitrous-oxide-emissions
- Iowa DNR — Greenhouse Gases: https://www.iowadnr.gov/environmental-protection/air-quality/greenhouse-gases
- Iowa State Extension — Fuel Required for Field Operations: https://shop.iastate.edu/extension/farm-environment/farm-and-business-management/land-and-equipment/pm709.html
- Iowa State STRIPS: https://strips.nrem.iastate.edu/
- Iowa Nutrient Reduction Strategy: https://nrstracking.cals.iastate.edu/iowa-nutrient-reduction-strategy
