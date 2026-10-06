# Repository layout

The October 6, 2026 reorganization groups research by subject and separates preserved files, transcriptions, and project-generated policy drafts. It changes navigation and file placement, not research findings or draft ordinance requirements.

| Folder | Responsibility |
| --- | --- |
| `dataset/project/` | Project scope, chronology, site evidence, and open questions |
| `dataset/impacts/` | Physical, environmental, economic, and community impacts |
| `dataset/policy/` | Authority, public process, policy analysis, and comparators |
| `dataset/technology/` | Workloads, AI, and cryptocurrency context |
| `dataset/evidence/` | Source validation and consolidated citations |
| `dataset/community/` | Question-bank documentation and original CSV |
| `dataset/updates/` | Dated public-record updates and forum summaries |
| `dataset/cascade-zoning/` | Transcribed code and ordinance records, with draft labels preserved |
| `dataset/comparator-ordinances/` | Records of external ordinances and working drafts |
| `proposals/` | This project's draft ordinance text |
| `sources/` | Preserved source/working files and their hash manifest |
| `scripts/` | Manual tools and local validation |
| `docs/` | Research scope and repository navigation |

The original 01–29 identifiers and filenames are retained. The central [research index](../dataset/00_INDEX.md) and [zoning index](../dataset/cascade-zoning/00_INDEX.md) retain their paths. Existing research and ordinance text is preserved except for repository path updates; source binaries, raw captions, and the 76-question CSV retain their exact bytes.

## File move map

Old file URLs using a branch name do not redirect automatically after a GitHub rename. Use this map to update bookmarks; links pinned to earlier commits remain historical references.

| Previous repository path | Current file |
| --- | --- |
| `dataset/01_PROJECT_OVERVIEW_AND_TIMELINE.md` | [`dataset/project/01_PROJECT_OVERVIEW_AND_TIMELINE.md`](../dataset/project/01_PROJECT_OVERVIEW_AND_TIMELINE.md) |
| `dataset/02_SIMPLE_MINING_AND_PROJECT_SCOPE.md` | [`dataset/project/02_SIMPLE_MINING_AND_PROJECT_SCOPE.md`](../dataset/project/02_SIMPLE_MINING_AND_PROJECT_SCOPE.md) |
| `dataset/03_DATA_CENTER_WORKLOAD_TYPES.md` | [`dataset/technology/03_DATA_CENTER_WORKLOAD_TYPES.md`](../dataset/technology/03_DATA_CENTER_WORKLOAD_TYPES.md) |
| `dataset/04_CASCADE_ZONING_AND_LOCAL_AUTHORITY.md` | [`dataset/policy/04_CASCADE_ZONING_AND_LOCAL_AUTHORITY.md`](../dataset/policy/04_CASCADE_ZONING_AND_LOCAL_AUTHORITY.md) |
| `dataset/05_PROJECT_MODEL_ACCOUNTABILITY_ORDINANCE.md` | [`dataset/policy/05_PROJECT_MODEL_ACCOUNTABILITY_ORDINANCE.md`](../dataset/policy/05_PROJECT_MODEL_ACCOUNTABILITY_ORDINANCE.md) |
| `dataset/06_IOWA_DATA_CENTER_POLICY_COMPARATORS.md` | [`dataset/policy/06_IOWA_DATA_CENTER_POLICY_COMPARATORS.md`](../dataset/policy/06_IOWA_DATA_CENTER_POLICY_COMPARATORS.md) |
| `dataset/07_WATER_AND_COOLING.md` | [`dataset/impacts/07_WATER_AND_COOLING.md`](../dataset/impacts/07_WATER_AND_COOLING.md) |
| `dataset/08_NOISE_AND_ACOUSTICS.md` | [`dataset/impacts/08_NOISE_AND_ACOUSTICS.md`](../dataset/impacts/08_NOISE_AND_ACOUSTICS.md) |
| `dataset/09_ELECTRICITY_GRID_AND_BACKUP_POWER.md` | [`dataset/impacts/09_ELECTRICITY_GRID_AND_BACKUP_POWER.md`](../dataset/impacts/09_ELECTRICITY_GRID_AND_BACKUP_POWER.md) |
| `dataset/10_AGRICULTURE_GREENHOUSES_AND_LAND_USE.md` | [`dataset/impacts/10_AGRICULTURE_GREENHOUSES_AND_LAND_USE.md`](../dataset/impacts/10_AGRICULTURE_GREENHOUSES_AND_LAND_USE.md) |
| `dataset/11_ENVIRONMENTAL_AND_CARBON_SCENARIOS.md` | [`dataset/impacts/11_ENVIRONMENTAL_AND_CARBON_SCENARIOS.md`](../dataset/impacts/11_ENVIRONMENTAL_AND_CARBON_SCENARIOS.md) |
| `dataset/12_JOBS_TAXES_AND_COMMUNITY_BENEFITS.md` | [`dataset/impacts/12_JOBS_TAXES_AND_COMMUNITY_BENEFITS.md`](../dataset/impacts/12_JOBS_TAXES_AND_COMMUNITY_BENEFITS.md) |
| `dataset/13_INFRASTRUCTURE_TRAFFIC_AND_EMERGENCY_RESPONSE.md` | [`dataset/impacts/13_INFRASTRUCTURE_TRAFFIC_AND_EMERGENCY_RESPONSE.md`](../dataset/impacts/13_INFRASTRUCTURE_TRAFFIC_AND_EMERGENCY_RESPONSE.md) |
| `dataset/14_ADVISORY_COMMITTEE_AND_OPEN_MEETINGS.md` | [`dataset/policy/14_ADVISORY_COMMITTEE_AND_OPEN_MEETINGS.md`](../dataset/policy/14_ADVISORY_COMMITTEE_AND_OPEN_MEETINGS.md) |
| `dataset/15_MORATORIUM_AND_DEVELOPMENT_PROCESS.md` | [`dataset/policy/15_MORATORIUM_AND_DEVELOPMENT_PROCESS.md`](../dataset/policy/15_MORATORIUM_AND_DEVELOPMENT_PROCESS.md) |
| `dataset/16_MONITORING_ENFORCEMENT_AND_DECOMMISSIONING.md` | [`dataset/impacts/16_MONITORING_ENFORCEMENT_AND_DECOMMISSIONING.md`](../dataset/impacts/16_MONITORING_ENFORCEMENT_AND_DECOMMISSIONING.md) |
| `dataset/17_PERMITS_AND_REVIEW_TIMING.md` | [`dataset/policy/17_PERMITS_AND_REVIEW_TIMING.md`](../dataset/policy/17_PERMITS_AND_REVIEW_TIMING.md) |
| `dataset/18_MEDIA_CLAIMS_AND_SOURCE_VALIDATION.md` | [`dataset/evidence/18_MEDIA_CLAIMS_AND_SOURCE_VALIDATION.md`](../dataset/evidence/18_MEDIA_CLAIMS_AND_SOURCE_VALIDATION.md) |
| `dataset/19_EXTERNAL_POLICY_AND_TECHNOLOGY_COMPARATORS.md` | [`dataset/policy/19_EXTERNAL_POLICY_AND_TECHNOLOGY_COMPARATORS.md`](../dataset/policy/19_EXTERNAL_POLICY_AND_TECHNOLOGY_COMPARATORS.md) |
| `dataset/20_COMMUNITY_FORUM_QUESTION_BANK.md` | [`dataset/community/20_COMMUNITY_FORUM_QUESTION_BANK.md`](../dataset/community/20_COMMUNITY_FORUM_QUESTION_BANK.md) |
| `dataset/21_OPEN_QUESTIONS_AND_EVIDENCE_GAPS.md` | [`dataset/project/21_OPEN_QUESTIONS_AND_EVIDENCE_GAPS.md`](../dataset/project/21_OPEN_QUESTIONS_AND_EVIDENCE_GAPS.md) |
| `dataset/22_SOURCE_INDEX.md` | [`dataset/evidence/22_SOURCE_INDEX.md`](../dataset/evidence/22_SOURCE_INDEX.md) |
| `dataset/23_CASCADE_MUNICIPAL_WATER_BASELINE.md` | [`dataset/impacts/23_CASCADE_MUNICIPAL_WATER_BASELINE.md`](../dataset/impacts/23_CASCADE_MUNICIPAL_WATER_BASELINE.md) |
| `dataset/24_ARTIFICIAL_INTELLIGENCE_BENEFITS_AND_ACCOMPLISHMENTS.md` | [`dataset/technology/24_ARTIFICIAL_INTELLIGENCE_BENEFITS_AND_ACCOMPLISHMENTS.md`](../dataset/technology/24_ARTIFICIAL_INTELLIGENCE_BENEFITS_AND_ACCOMPLISHMENTS.md) |
| `dataset/25_ARTIFICIAL_INTELLIGENCE_DEVELOPMENT_AND_MODERN_USE_TIMELINE.md` | [`dataset/technology/25_ARTIFICIAL_INTELLIGENCE_DEVELOPMENT_AND_MODERN_USE_TIMELINE.md`](../dataset/technology/25_ARTIFICIAL_INTELLIGENCE_DEVELOPMENT_AND_MODERN_USE_TIMELINE.md) |
| `dataset/26_CRYPTOCURRENCY_BENEFITS_RISKS_AND_ECONOMIC_IMPACT.md` | [`dataset/technology/26_CRYPTOCURRENCY_BENEFITS_RISKS_AND_ECONOMIC_IMPACT.md`](../dataset/technology/26_CRYPTOCURRENCY_BENEFITS_RISKS_AND_ECONOMIC_IMPACT.md) |
| `dataset/27_WEEKLY_PUBLIC_RECORD_UPDATE_2026-09-11_TO_2026-09-18.md` | [`dataset/updates/27_WEEKLY_PUBLIC_RECORD_UPDATE_2026-09-11_TO_2026-09-18.md`](../dataset/updates/27_WEEKLY_PUBLIC_RECORD_UPDATE_2026-09-11_TO_2026-09-18.md) |
| `dataset/28_SIMPLE_MINING_COMMUNITY_FORUM_2026-10-01.md` | [`dataset/updates/28_SIMPLE_MINING_COMMUNITY_FORUM_2026-10-01.md`](../dataset/updates/28_SIMPLE_MINING_COMMUNITY_FORUM_2026-10-01.md) |
| `dataset/29_SIMPLE_MINING_SITE_PARCEL_AND_ZONING.md` | [`dataset/project/29_SIMPLE_MINING_SITE_PARCEL_AND_ZONING.md`](../dataset/project/29_SIMPLE_MINING_SITE_PARCEL_AND_ZONING.md) |
| `dataset/cascade-zoning/ordinances/Cascade_Zoning_Ordinance_OCR.docx` | [`sources/cascade-zoning/Cascade_Zoning_Ordinance_OCR.docx`](../sources/cascade-zoning/Cascade_Zoning_Ordinance_OCR.docx) |
| `dataset/cascade-zoning/ordinances/DRAFT-ORDINANCE-M2-DATA-CENTER-PERFORMANCE-STANDARDS-2026-10-06.md` | [`proposals/DRAFT-ORDINANCE-M2-DATA-CENTER-PERFORMANCE-STANDARDS-2026-10-06.md`](../proposals/DRAFT-ORDINANCE-M2-DATA-CENTER-PERFORMANCE-STANDARDS-2026-10-06.md) |
| `dataset/cascade-zoning/ordinances/Entire zoning code-1.pdf` | [`sources/cascade-zoning/Entire zoning code-1.pdf`](../sources/cascade-zoning/Entire%20zoning%20code-1.pdf) |
| `dataset/cascade-zoning/ordinances/ORDINANCE #02-22 CLEAN VERSION Building Permits CH 6-12.docx` | [`sources/cascade-zoning/ORDINANCE #02-22 CLEAN VERSION Building Permits CH 6-12.docx`](../sources/cascade-zoning/ORDINANCE%20%2302-22%20CLEAN%20VERSION%20Building%20Permits%20CH%206-12.docx) |
| `dataset/cascade-zoning/ordinances/ORDINANCE #03-23 CEDC Lots on 1st AVe E M2 to C1.docx` | [`sources/cascade-zoning/ORDINANCE #03-23 CEDC Lots on 1st AVe E M2 to C1.docx`](../sources/cascade-zoning/ORDINANCE%20%2303-23%20CEDC%20Lots%20on%201st%20AVe%20E%20M2%20to%20C1.docx) |
| `dataset/cascade-zoning/ordinances/ORDINANCE #04-21 zoning amend permitted uses r-3.docx` | [`sources/cascade-zoning/ORDINANCE #04-21 zoning amend permitted uses r-3.docx`](../sources/cascade-zoning/ORDINANCE%20%2304-21%20zoning%20amend%20permitted%20uses%20r-3.docx) |
| `dataset/cascade-zoning/ordinances/ORDINANCE #05-21 R-1 minimum lot area.docx` | [`sources/cascade-zoning/ORDINANCE #05-21 R-1 minimum lot area.docx`](../sources/cascade-zoning/ORDINANCE%20%2305-21%20R-1%20minimum%20lot%20area.docx) |
| `dataset/cascade-zoning/ordinances/ORDINANCE #05-22 zoning amend permitted uses C1, C2, M1, M2 Exercise and Fitness Businesses.docx` | [`sources/cascade-zoning/ORDINANCE #05-22 zoning amend permitted uses C1, C2, M1, M2 Exercise and Fitness Businesses.docx`](../sources/cascade-zoning/ORDINANCE%20%2305-22%20zoning%20amend%20permitted%20uses%20C1%2C%20C2%2C%20M1%2C%20M2%20Exercise%20and%20Fitness%20Businesses.docx) |
| `dataset/cascade-zoning/ordinances/ORDINANCE #06-23 zoning amend permitted Setbacks R3 Single Family with zero interior setbacks.docx` | [`sources/cascade-zoning/ORDINANCE #06-23 zoning amend permitted Setbacks R3 Single Family with zero interior setbacks.docx`](../sources/cascade-zoning/ORDINANCE%20%2306-23%20zoning%20amend%20permitted%20Setbacks%20R3%20Single%20Family%20with%20zero%20interior%20setbacks.docx) |
| `dataset/cascade-zoning/ordinances/ORDINANCE #18-24 Front Setbacks R1 R2 for Porches.docx` | [`sources/cascade-zoning/ORDINANCE #18-24 Front Setbacks R1 R2 for Porches.docx`](../sources/cascade-zoning/ORDINANCE%20%2318-24%20Front%20Setbacks%20R1%20R2%20for%20Porches.docx) |
| `dataset/cascade-zoning/ordinances/ORDINANCE #19-24 Fence Heights 8ft in C and M Districts.docx` | [`sources/cascade-zoning/ORDINANCE #19-24 Fence Heights 8ft in C and M Districts.docx`](../sources/cascade-zoning/ORDINANCE%20%2319-24%20Fence%20Heights%208ft%20in%20C%20and%20M%20Districts.docx) |
| `dataset/source-materials/2026-10-01_simple-mining-community-forum_youtube-auto-captions.en.vtt` | [`sources/community-forums/2026-10-01_simple-mining-community-forum_youtube-auto-captions.en.vtt`](../sources/community-forums/2026-10-01_simple-mining-community-forum_youtube-auto-captions.en.vtt) |
| `questions.csv` | [`dataset/community/questions.csv`](../dataset/community/questions.csv) |
| `submit-questions.sh` | [`scripts/submit-questions.sh`](../scripts/submit-questions.sh) |

The detailed purpose, areas of focus, policy principles, research standards, and project stance previously on the root README are preserved in [research scope](research-scope.md). The README now provides the navigation entry point.
