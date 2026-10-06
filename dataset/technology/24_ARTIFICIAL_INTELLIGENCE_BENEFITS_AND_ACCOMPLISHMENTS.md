# Artificial Intelligence: Documented Benefits and Accomplishments

> Research context for the Cascade Data Center project. This file documents benefits that artificial-intelligence systems have **already demonstrated** in research, medicine, science, accessibility, forecasting, cultural preservation, and work. It does not assume that the proposed Cascade facility will run AI workloads or produce any particular benefit.
>
> Last reviewed: 2026-09-10

## Why this belongs in the dataset

Data-center debates often focus appropriately on local impacts: electricity, water, noise, land use, infrastructure, public incentives, and emergency response. Those impacts should be measured and regulated. But compute infrastructure also supports technologies whose benefits can occur far beyond the community that hosts the physical equipment.

A complete cost-benefit discussion therefore needs two ideas at the same time:

1. **AI has already produced measurable scientific, medical, accessibility, forecasting, and productivity benefits.**
2. **Those broader benefits do not erase localized costs or justify weak local protections.**

The relevant policy question is not whether AI is universally good or bad. It is how communities can permit lawful computing infrastructure while making its local physical costs measurable, bounded, and appropriately allocated.

---

# 1. Medicine and biomedical research

## AI-guided antibiotic discovery: halicin

A 2020 *Cell* study used a deep-learning model to search chemical space for antibacterial compounds. The work identified halicin as a structurally unusual antibiotic candidate with broad antibacterial activity and demonstrated activity in animal models.

**What this establishes:** machine learning can identify promising antibiotic candidates that conventional similarity-based screening might overlook.

**Primary research:**
- Stokes et al., *Cell* (2020), “A Deep Learning Approach to Antibiotic Discovery”  
  https://pubmed.ncbi.nlm.nih.gov/32084340/  
  https://doi.org/10.1016/j.cell.2020.01.021

## AI-guided antibiotic discovery: abaucin

A 2023 *Nature Chemical Biology* study screened approximately 7,500 molecules against multidrug-resistant *Acinetobacter baumannii*, trained a neural network on those results, and used it to identify structurally distinct candidates. The researchers discovered **abaucin**, a narrow-spectrum antibacterial compound that controlled *A. baumannii* infection in a mouse wound model.

**What this establishes:** AI-assisted drug discovery has generated experimentally validated lead compounds against difficult pathogens.

**Primary research:**
- Liu et al., *Nature Chemical Biology* (2023), “Deep learning-guided discovery of an antibiotic targeting Acinetobacter baumannii”  
  https://www.nature.com/articles/s41589-023-01349-8  
  https://doi.org/10.1038/s41589-023-01349-8

## Protein structure prediction: AlphaFold 2

AlphaFold 2 demonstrated protein-structure prediction with accuracy competitive with experimental structures in many cases, transforming a long-standing scientific challenge into a practical computational tool.

**Primary research:**
- Jumper et al., *Nature* (2021), “Highly accurate protein structure prediction with AlphaFold”  
  https://www.nature.com/articles/s41586-021-03819-2  
  https://doi.org/10.1038/s41586-021-03819-2

## Biomolecular interactions: AlphaFold 3

AlphaFold 3 expanded structure prediction beyond proteins to complexes containing proteins, nucleic acids, small molecules, ions, and modified residues, with substantial accuracy improvements over specialized tools in multiple interaction categories.

**Primary research:**
- Abramson et al., *Nature* (2024), “Accurate structure prediction of biomolecular interactions with AlphaFold 3”  
  https://www.nature.com/articles/s41586-024-07487-w  
  https://doi.org/10.1038/s41586-024-07487-w

## Mammography screening

The randomized MASAI trial compared AI-supported mammography screening with standard double reading. In its 2023 safety analysis of roughly 80,000 women, AI-supported screening detected 244 cancers versus 203 in the control group while reducing screen-reading workload by **44.3%**. False-positive rates were 1.5% in both groups.

This is stronger and more precise evidence than a blanket statement such as “AI diagnoses patients 10% better than doctors.” Performance varies by medical task, disease, population, system, and workflow.

**Primary research:**
- Lång et al., *The Lancet Oncology* (2023), randomized MASAI trial  
  https://pubmed.ncbi.nlm.nih.gov/37541274/  
  https://doi.org/10.1016/S1470-2045(23)00298-X

## AI is already present in regulated medical devices

The U.S. Food and Drug Administration maintains a public list of AI-enabled medical devices authorized for marketing in the United States. The list includes products across radiology, cardiovascular medicine, neurology, pathology, gastroenterology, and other specialties and is updated as devices complete applicable premarket review.

**Primary / official:**
- FDA — Artificial Intelligence-Enabled Medical Devices  
  https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-enabled-medical-devices

---

# 2. Mobility, disability, and accessibility

## Brain–spine interface after spinal-cord injury

A 2023 *Nature* study demonstrated a brain–spine interface that decoded movement intentions from brain activity and used them to control spinal-cord stimulation. The digital bridge enabled a participant with spinal-cord injury to stand and walk naturally, including over more complex terrain.

This should be described accurately as neurotechnology with AI/decode-control components—not as a general cure for paralysis.

**Primary research:**
- Lorach et al., *Nature* (2023), “Walking naturally after spinal cord injury using a brain–spine interface”  
  https://www.nature.com/articles/s41586-023-06094-5  
  https://doi.org/10.1038/s41586-023-06094-5

## Visual assistance for blind and low-vision users

AI does not literally restore biological sight in most accessibility applications, but it can convert visual information into usable audio or haptic information. Microsoft’s Seeing AI, for example, describes text, currency, colors, people, products, and scenes through a phone camera. Peer-reviewed research is also demonstrating AI-powered wearable systems that improve navigation and post-navigation tasks for participants with visual impairment.

**Primary / original sources:**
- Microsoft Seeing AI  
  https://www.microsoft.com/en-us/garage/wall-of-fame/seeing-ai/
- Tang et al., *Nature Machine Intelligence* (2025), “Human-centred design and fabrication of a wearable multimodal visual assistance system”  
  https://www.nature.com/articles/s42256-025-01018-6  
  https://doi.org/10.1038/s42256-025-01018-6

---

# 3. Weather and disaster-relevant forecasting

## GraphCast

GraphCast uses graph neural networks for global medium-range weather forecasting. The peer-reviewed *Science* paper reported 10-day forecasts for hundreds of atmospheric variables at 0.25-degree resolution in under one minute and significant outperformance of the leading operational deterministic system on about **90% of 1,380 verification targets** evaluated. The work also demonstrated prediction capability relevant to tropical cyclones, atmospheric rivers, and extreme temperatures.

**Primary research:**
- Lam et al., *Science* (2023), “Learning skillful medium-range global weather forecasting”  
  https://pubmed.ncbi.nlm.nih.gov/37962497/  
  https://doi.org/10.1126/science.adi2336
- Google DeepMind publication page  
  https://deepmind.google/research/publications/22598/

---

# 4. Materials and energy research

## GNoME materials discovery

A 2023 *Nature* paper reported that graph-network models used for materials exploration identified **2.2 million** crystal structures stable relative to previous datasets; **381,000** entries were on the updated convex hull as newly discovered stable materials. Hundreds had independent experimental confirmation.

Potential applications include batteries, photovoltaics, electronics, and other materials-intensive technologies. A predicted stable structure is not automatically a manufacturable commercial material, so the result should not be described as hundreds of thousands of new commercial products.

**Primary research:**
- Merchant et al., *Nature* (2023), “Scaling deep learning for materials discovery”  
  https://www.nature.com/articles/s41586-023-06735-9  
  https://doi.org/10.1038/s41586-023-06735-9

## Fusion plasma control

A 2022 *Nature* study demonstrated deep-reinforcement-learning control of magnetic coils on the TCV tokamak, successfully producing and controlling multiple plasma configurations.

**What this establishes:** AI has been experimentally applied to a difficult real-time physical-control problem relevant to fusion research.

**Primary research:**
- Degrave et al., *Nature* (2022), “Magnetic control of tokamak plasmas through deep reinforcement learning”  
  https://www.nature.com/articles/s41586-021-04301-9  
  https://doi.org/10.1038/s41586-021-04301-9

---

# 5. History, language, and cultural preservation

## Ancient Greek inscriptions: Ithaca

Ithaca is a deep neural network developed to help restore and attribute damaged ancient Greek inscriptions. In the 2022 *Nature* study, the model alone reached 62% restoration accuracy; historians using the system improved from 25% to 72% restoration accuracy. The system also attributed geographic origin with 71% accuracy and narrowed chronological estimates.

This is the appropriate evidence behind claims that AI is helping historians reconstruct ancient texts. It should **not** be described as an AI analysis of the Rosetta Stone unless a source specifically demonstrates that application.

**Primary research:**
- Assael et al., *Nature* (2022), “Restoring and attributing ancient texts using deep neural networks”  
  https://www.nature.com/articles/s41586-022-04448-z  
  https://doi.org/10.1038/s41586-022-04448-z

## Akkadian cuneiform translation

A 2023 *PNAS Nexus* study demonstrated neural machine translation directly from Akkadian cuneiform Unicode glyphs and from transliteration into English. The authors frame the system as a human-in-the-loop aid for scholars working with the many cuneiform texts that remain difficult to translate at scale.

This is strong evidence for AI assisting the study of Mesopotamian cuneiform. Because the model translates **Akkadian**, it should not be generalized into a claim that AI has translated all Sumerian tablets.

**Primary research:**
- Gutherz et al., *PNAS Nexus* (2023), “Translating Akkadian to English with neural machine translation”  
  https://academic.oup.com/pnasnexus/article/2/5/pgad096/7147349  
  https://doi.org/10.1093/pnasnexus/pgad096

---

# 6. Productivity and diffusion of expertise

A large field study of **5,179 customer-support agents** found that access to a generative-AI assistant increased productivity, measured as issues resolved per hour, by **14% on average**. The gain was **34% for novice and lower-skilled workers**, with minimal effects for experienced/high-skilled workers. The study also found improvements in customer sentiment and employee retention.

This is useful evidence for the “democratization of expertise” discussion: in this setting, the largest gains accrued to workers who began with less experience rather than to the strongest performers.

**Primary research / working paper, later published in QJE:**
- Brynjolfsson, Li & Raymond, NBER Working Paper 31161, “Generative AI at Work”  
  https://www.nber.org/papers/w31161  
  https://doi.org/10.3386/w31161

---

# 7. Frontier mathematics: important, current, and not yet settled

On September 8, 2026, OpenAI published an AI-generated analytical proof and Lean formalization that it says resolves the Navier–Stokes Millennium Prize Problem by demonstrating finite-time singularity for a specified construction.

This is a major AI-research milestone **if the proof survives independent mathematical scrutiny**, but as of September 10, 2026 it is too early to write “AI solved a Millennium Prize Problem” as an accepted fact. The Clay Mathematics Institute’s rules require a proposed solution to appear in a qualifying outlet, remain published for at least two years, and achieve general acceptance in the global mathematics community before CMI will consider it for the prize.

**Primary / original sources:**
- OpenAI — “On the Navier–Stokes Millennium Prize Problem” (2026-09-08)  
  https://openai.com/index/navier-stokes-solution/
- Clay Mathematics Institute — Rules for the Millennium Prize Problems  
  https://www.claymath.org/millennium-problems/rules/

**Independent contemporaneous reporting:**
- *Nature* — “OpenAI claims huge maths breakthrough on a famed ‘Millennium Problem’” (2026-09-08)  
  https://www.nature.com/articles/d41586-026-02842-5

**Evidence status:** proposed solution; independent validation and CMI prize eligibility are not established as of 2026-09-10.

---

# 8. What the evidence supports — and what it does not

The sources above support the proposition that AI has already:

- accelerated discovery of antibiotic candidates;
- materially advanced protein and biomolecular structure prediction;
- improved or streamlined particular medical-screening workflows;
- enabled practical accessibility tools for blind and low-vision users;
- contributed to neurotechnology that restored walking capability for a participant with spinal-cord injury;
- improved medium-range weather forecasting;
- expanded computational discovery of candidate stable materials;
- controlled difficult experimental fusion-plasma configurations;
- assisted restoration, attribution, and translation of ancient texts;
- increased worker productivity in a large real-world deployment; and
- generated a formally encoded proposed solution to a major open mathematics problem that is now subject to external validation.

The same evidence does **not** establish that every AI system is beneficial, that every deployment is accurate or safe, that AI should replace expert judgment, or that communities hosting compute infrastructure should absorb unlimited local externalities.

---

# 9. Relevance to Cascade

None of these examples proves that the proposed Cascade project will perform AI research, host an AI model, discover medicines, forecast weather, or produce any other specific public benefit. The project’s actual workload mix must be evaluated from project-specific evidence.

These examples matter for a different reason: they demonstrate that the electricity, networking, cooling, and computing infrastructure discussed in data-center debates can support outcomes with broad societal value. A sound local policy can recognize that value while still requiring enforceable limits on water, noise, power-system impacts, infrastructure costs, emergency response, and decommissioning.

That is the core distinction of this repository: **support useful computing infrastructure while regulating the physical impacts that actually reach the host community.**
