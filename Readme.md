# FDA FAERS Pharmacovigilance Analysis — Colorectal & Appendiceal Cancer

Analysis of real-world adverse event data from the **FDA Adverse Event Reporting System (FAERS)** focused on colorectal and appendiceal cancer patients, their chemotherapy regimens, and comorbidity-related drug exposures. Built on the full 2024 FAERS dataset (Q1–Q4) using SQL, Python, and Jupyter notebooks.

---

## Background & Motivation

Colorectal and appendiceal cancers share core chemotherapy regimens — primarily fluorouracil-based combinations (FOLFOX, FOLFIRI, FOLFIRINOX) and, in peritoneal disease, HIPEC protocols using oxaliplatin or mitomycin C. Despite extensive clinical trial data on efficacy, real-world adverse event profiles in spontaneous reporting databases like FAERS offer a complementary signal — capturing drug combinations, indication patterns, and outcomes at population scale.

This project applies pharmacovigilance methods to characterize the adverse event burden in this patient population, with analytical angles spanning chemotherapy toxicity, disproportionality signal detection, patient population characterization, serious outcomes, and indication-first rare cancer profiling.

> **Note:** FAERS data represents *reported associations*, not confirmed causal relationships. All findings should be interpreted in the context of spontaneous reporting limitations including indication bias, reporting lag, and duplicate submissions.

---

## Key Findings

- **13,000+ fluorouracil drug records** identified across 2024 FAERS, requiring normalization of **33 distinct drug name variants** — illustrating the data quality challenges inherent to spontaneous reporting databases.

- **Diarrhoea and neutropenia** were the most consistently reported adverse events across all fluorouracil-containing regimens, with diarrhoea accounting for 555 reports in the PS/SS-filtered population — consistent with the known toxicity profile.

- **Cardiotoxicity (ROR=15.0) and polyneuropathy (ROR=32.3)** were identified as statistically significant disproportionality signals via Reporting Odds Ratio analysis — cardiotoxicity being a clinically important and often underappreciated fluorouracil risk.

- **Outcome distributions differed significantly across regimens** (χ²=118.1, df=9, p<0.0001). Monotherapy patients showed 32% more deaths than expected — likely reflecting patient selection (frail/end-stage patients ineligible for combination regimens) rather than drug toxicity.

- **Colorectal cancer was the dominant reported indication** for fluorouracil (5,617 PS/SS reports). Off-label use ranked 2nd among all reported reactions (424 reports), representing a pharmacovigilance signal worth further investigation.

- **Appendiceal cancer generated only ~339 FAERS reports** across the full 2024 dataset — confirming the rarity of these diagnoses even at national reporting scale and highlighting the limits of spontaneous reporting for orphan oncology indications.

- **Mitomycin C had only 4 reports** in the appendiceal population despite being a primary HIPEC agent — likely reflecting underreporting of intraperitoneal chemotherapy administered in surgical rather than outpatient settings.

---

## Analytical Approach

This project uses two complementary frameworks:

**Drug-first (Module 1):** Begin with a specific drug (fluorouracil), build a clean analysis population through name normalization and role code filtering, then characterize reactions, demographics, outcomes, and statistical signals for that population.

**Indication-first (Module 3):** Begin with a specific cancer population (appendiceal cancer), identify all primaryids matching curated MedDRA indication terms, then ask what drugs were reported and what adverse events occurred. Appropriate for rare cancer populations where the disease — not a single drug — is the analytical anchor.

---

## Notebooks

**Schema Overview**

| Notebook | Description |
|---|---|
| [explore_faers_schema.ipynb](notebooks/explore_faers_schema.ipynb) | Schema overview, table validation, row counts, and data quality checks across all 7 FAERS tables |

**Module 1 — Fluorouracil** ✓ Complete

| Notebook | Focus | Key Output |
|---|---|---|
| [01_5fu_explore.ipynb](notebooks/module_1_fluorouracil/01_5fu_explore.ipynb) | Drug name normalization, role code filtering, route and reporter type analysis | 5,617-report `fluorouracil_analysis` table; 33 name variants consolidated |
| [02_5fu_reactions.ipynb](notebooks/module_1_fluorouracil/02_5fu_reactions.ipynb) | Top adverse reactions; regimen-stratified symptom heatmap | Diarrhoea, neutropenia, nausea dominate; FOLFOX drives neuropathy signal |
| [03_5fu_population.ipynb](notebooks/module_1_fluorouracil/03_5fu_population.ipynb) | Age, sex, country, indication profile | Median age 60–69; male predominance; colorectal cancer dominant indication |
| [04_5fu_outcomes.ipynb](notebooks/module_1_fluorouracil/04_5fu_outcomes.ipynb) | Serious outcomes by regimen (DE/HO/LT/OT) | Hospitalization most common; FOLFIRINOX highest death proportion |
| [05_5fu_statistics.ipynb](notebooks/module_1_fluorouracil/05_5fu_statistics.ipynb) | ROR disproportionality analysis; chi-square outcome comparison | Cardiotoxicity ROR=15.0, polyneuropathy ROR=32.3; p<0.0001 across regimens |

**Module 2 — Colorectal Cancer HIPEC Agents** *(in progress)*

| Notebook | Description |
|---|---|
| *(planned)* | Oxaliplatin and mitomycin C adverse event profiling within peritoneal malignancy subgroup |

**Module 3 — Appendiceal Cancer** *(in progress)*

| Notebook | Focus |
|---|---|
| [01_appendiceal_explore.ipynb](notebooks/module_3_appendiceal/01_appendiceal_explore.ipynb) | Indication term discovery, manual curation, `appendiceal_reports` table construction, drug landscape |
| [02_appendiceal_reactions.ipynb](notebooks/module_3_appendiceal/02_appendiceal_reactions.ipynb) | Top adverse reactions in appendiceal cancer population *(planned)* |
| [03_appendiceal_population.ipynb](notebooks/module_3_appendiceal/03_appendiceal_population.ipynb) | Patient demographics *(planned)* |
| [04_appendiceal_outcomes.ipynb](notebooks/module_3_appendiceal/04_appendiceal_outcomes.ipynb) | Serious outcomes by top drug *(planned)* |

**Module 4 — Metformin**

| Notebook | Description |
|---|---|
| [Metformin_explore.ipynb](notebooks/module_4_metformin/Metformin_explore.ipynb) | Metformin adverse event analysis across formulations and combination therapies |

---

## Project Structure

```
FDA_FAERS/
│
├── notebooks/
│   ├── explore_faers_schema.ipynb
│   ├── module_1_fluorouracil/
│   │   ├── 01_5fu_explore.ipynb
│   │   ├── 02_5fu_reactions.ipynb
│   │   ├── 03_5fu_population.ipynb
│   │   ├── 04_5fu_outcomes.ipynb
│   │   ├── 05_5fu_statistics.ipynb
│   │   └── 06_5fu_ml.ipynb
│   ├── module_2_colorectal_hipec/
│   │   └── colorectal_hipec_explore.ipynb
│   ├── module_3_appendiceal/
│   │   ├── 01_appendiceal_explore.ipynb
│   │   ├── 02_appendiceal_reactions.ipynb
│   │   ├── 03_appendiceal_population.ipynb
│   │   └── 04_appendiceal_outcomes.ipynb
│   └── module_4_metformin/
│       └── Metformin_explore.ipynb
│
├── database/
│   └── faers.db                    # SQLite database (excluded from version control)
│
├── data/
│   ├── Dataset ASCII Downloads/    # Raw FAERS quarterly zip files (Q1–Q4 2024)
│   └── Dataset ASCII Extracts/     # Extracted quarterly .txt files
│
├── python/
│   ├── build_database.py           # Builds SQLite DB from raw FAERS files
│   ├── export_db_samples.py        # Exports sample CSVs for each table
│   └── inspect_data.py             # Data inspection utilities
│
├── outputs/
│   └── db_sample_review/           # Sample CSVs for schema review
│
├── sql/
│   └── schema_inspection.sql       # Schema inspection queries
│
└── README.md
```

> `faers.db` is excluded from version control due to file size. To reproduce: download FAERS 2024 quarterly ASCII files from the [FDA FAERS website](https://www.fda.gov/drugs/fda-adverse-event-reporting-system-faers) and run `python/build_database.py`.

---

## Tech Stack

Python · SQL · SQLite · pandas · NumPy · SciPy · matplotlib · Jupyter · Git

---

## Planned Extensions

- Complete Module 3 appendiceal reactions, population, and outcomes notebooks
- Module 2 HIPEC agent profiling (oxaliplatin, mitomycin C) in peritoneal malignancy subgroup
- Combined fluoropyrimidine analysis including capecitabine (oral 5-FU prodrug)
- Logistic regression modeling of serious outcomes (death, hospitalization, life-threatening)
