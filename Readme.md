# FDA FAERS Pharmacovigilance Analysis — Colorectal & Appendiceal Cancer

Analysis of real-world adverse event data from the **FDA Adverse Event Reporting System (FAERS)** focused on colorectal and appendiceal cancer patients, their chemotherapy regimens, and comorbidity-related drug exposures. Built on the full 2024 FAERS dataset (Q1–Q4) using SQL, Python, and Jupyter notebooks.

---

## Background & Motivation

Colorectal and appendiceal cancers share core chemotherapy regimens — primarily fluorouracil-based combinations (FOLFOX, FOLFIRI, FOLFIRINOX) and, in peritoneal disease, HIPEC protocols using oxaliplatin or mitomycin C. Despite extensive clinical trial data on efficacy, real-world adverse event profiles in spontaneous reporting databases like FAERS offer a complementary signal — capturing drug combinations, indication patterns, and outcomes at population scale.

This project applies pharmacovigilance methods to characterize the adverse event burden in this patient population, with analytical angles spanning chemotherapy toxicity, off-label prescribing, serious outcomes, and comorbidity drug exposures.

> **Note:** FAERS data represents *reported associations*, not confirmed causal relationships. All findings should be interpreted in the context of spontaneous reporting limitations.

---

## Key Findings

- **13,000+ fluorouracil drug records** were identified across 2024 FAERS, requiring normalization of **33 distinct drug name variants** before analysis — illustrating the data quality challenges inherent to spontaneous reporting databases.

- **Diarrhoea and neutropenia** were the most consistently reported adverse events across all fluorouracil-containing regimens (monotherapy and combinations), with diarrhoea accounting for 806 total reports — consistent with the known toxicity profile and validating the signal detection approach.

- **"Off-label use" ranked 2nd** among all reported events for fluorouracil (698 reports), representing a clinically meaningful pharmacovigilance signal worth further investigation.

- **Fluorouracil carried the highest hospitalization burden** among all chemotherapy drugs analyzed in the cancer population — 590 hospitalization outcomes vs. 127 deaths — more than bevacizumab, capecitabine, or irinotecan.

- **Appendiceal cancer-specific indications** (mucinous adenocarcinoma of appendix, pseudomyxoma peritonei) generated fewer than 12 adverse event reports each across the entire 2024 dataset — confirming the rarity of these diagnoses even at national reporting scale, and highlighting the limits of FAERS for orphan oncology indications.

- **Neuropathy peripheral** appeared prominently in both fluorouracil and oxaliplatin reports — expected given their combined use in FOLFOX, and a relevant finding for HIPEC protocols that also employ oxaliplatin.

---

## Analysis Angles

**1. Colorectal & Appendiceal Cancer Population**

Reports filtered using cancer-related MedDRA indication terms from the `indi` table, including:
- Colon cancer / Colorectal cancer (all stages and metastatic variants)
- Malignant peritoneal neoplasm / Metastases to peritoneum
- Pseudomyxoma peritonei / Mucinous adenocarcinoma of appendix

Within this population: top drugs by report volume, adverse reaction frequencies, serious outcome distributions, and per-drug toxicity comparisons across FOLFOX, FOLFIRI, and targeted therapies (bevacizumab, cetuximab, panitumumab).

**2. Fluorouracil-Containing Regimens**

Drug name normalization applied to consolidate 33+ brand, generic, and combination variants. Adverse reaction profiles compared across:
- Fluorouracil monotherapy
- FOLFOX (Fluorouracil + Leucovorin + Oxaliplatin)
- FOLFIRI (Fluorouracil + Irinotecan + Leucovorin)
- FOLFIRINOX (Fluorouracil + Irinotecan + Leucovorin + Oxaliplatin)

**3. Metformin as a Comorbidity Drug**

Diabetes is a common comorbidity in colorectal cancer patients. Metformin name variants identified and grouped; adverse reaction profiles compared across formulations and combinations (monotherapy, Metformin/Sitagliptin, Empagliflozin/Metformin) to characterize safety signals in this overlapping population.

**4. HIPEC Agents (Planned)**

Oxaliplatin and mitomycin C are the primary agents used in hyperthermic intraperitoneal chemotherapy (HIPEC) for peritoneal disease from appendiceal and colorectal primaries. Adverse event profiling for these agents within the peritoneal malignancy indication subgroup is planned.

---

## Data Processing Pipeline

1. Build a relational SQLite database from FAERS 2024 quarterly ASCII datasets (Q1–Q4)
2. Validate schema: row counts, column types, join integrity across all 7 tables
3. Filter cancer indication reports using the `indi` table and MedDRA terminology
4. Identify fluorouracil records using LIKE pattern matching; enumerate name variants
5. Normalize drug names — map brand names, salt variants, and combination strings to standard labels
6. Join `drug`, `reac`, `indi`, `outc`, and `demo` tables on `primaryid`
7. Aggregate reaction and outcome frequencies; remove noise indication terms
8. Apply downsampling for balanced cross-drug comparisons in modeling workflows

---

## Notebooks

**Schema Overview**

| Notebook | Description |
|---|---|
| [explore_faers_schema.ipynb](notebooks/explore_faers_schema.ipynb) | Schema overview, table validation, row counts, and data quality checks across all 7 FAERS tables |

**Module 1 — Fluorouracil**

| Notebook | Description |
|---|---|
| [01_5fu_explore.ipynb](notebooks/module_1_fluorouracil/01_5fu_explore.ipynb) | Drug name discovery, normalization of 33 variants, data quality checks, PS/SS role filtering, analysis-ready dataset construction |
| [02_5fu_reactions.ipynb](notebooks/module_1_fluorouracil/02_5fu_reactions.ipynb) | Adverse reaction frequency profile and cross-regimen heatmap comparison (FOLFOX, FOLFIRI, FOLFIRINOX) |
| [03_5fu_population.ipynb](notebooks/module_1_fluorouracil/03_5fu_population.ipynb) | Patient population characterization — treatment indications and demographics *(in progress)* |
| [04_5fu_outcomes.ipynb](notebooks/module_1_fluorouracil/04_5fu_outcomes.ipynb) | Serious outcome distributions — death, hospitalization, life-threatening events by regimen *(in progress)* |
| [05_5fu_statistics.ipynb](notebooks/module_1_fluorouracil/05_5fu_statistics.ipynb) | Reporting Odds Ratio (ROR) signal detection and outcome rate comparisons *(in progress)* |
| [06_5fu_ml.ipynb](notebooks/module_1_fluorouracil/06_5fu_ml.ipynb) | Predictive modeling of serious outcomes *(in progress)* |

**Module 2 — Colorectal Cancer HIPEC Agents**

| Notebook | Description |
|---|---|
| *(in progress)* | Oxaliplatin and mitomycin C adverse event profiling within peritoneal malignancy subgroup |

**Module 3 — Appendiceal Cancer**

| Notebook | Description |
|---|---|
| [01_appendiceal_indication.ipynb](notebooks/module_3_appendiceal/appendiceal_indication.ipynb) | Cancer indication filtering; top drugs, reactions, and outcomes in the colorectal/appendiceal population |

**Module 4 — Metformin**

| Notebook | Description |
|---|---|
| [01_metformin_explore.ipynb](notebooks/module_4_metformin/Metformin_explore.ipynb) | Metformin adverse event analysis across formulations and combination therapies |

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
│   ├── module_3_appendiceal/
│   │   └── appendiceal_indication.ipynb
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

Python · SQL · SQLite · pandas · matplotlib · seaborn · Jupyter

---

## Planned Extensions

- Reporting Odds Ratio (ROR) calculations for formal disproportionality signal detection
- Demographic stratification — age, sex, and reporter country within cancer subpopulations
- Dechallenge/rechallenge signal analysis
- HIPEC agent profiling (oxaliplatin, mitomycin C) in peritoneal malignancy subgroup
- Logistic regression modeling of serious outcomes (death, hospitalization, life-threatening)
