# FAERS Pharmacovigilance Analysis — Colorectal Cancer, Fluorouracil, and Metformin

This project analyzes adverse event reports from the **FDA Adverse Event Reporting System (FAERS)** with a focus on **colorectal and appendiceal cancer patients**, **Fluorouracil (5-FU)-containing chemotherapy regimens**, and **Metformin-containing therapies**.

The current goal is to explore how drug indication filtering, drug combination analysis, and adverse reaction profiling can be combined to investigate safety signals in oncology and diabetes pharmacovigilance using **SQL, Python, and Jupyter notebooks**.

The project demonstrates how large public health datasets can be filtered, cleaned, and analyzed to investigate potential safety signals. This is a learning project for complex SQL queries and Python EDA. More advanced statistical analysis and ML are planned.

---

# Project Goals

This project was built to practice:

- Working with large public health datasets
- SQL analysis on relational medical data
- Data cleaning and normalization of drug labels
- Exploratory pharmacovigilance analysis
- Class balancing techniques for modeling
- Data visualization with Python

---

# Dataset

The data comes from the **FDA Adverse Event Reporting System (FAERS)**.

FAERS is a spontaneous reporting system containing millions of adverse event reports submitted by:

- Healthcare professionals
- Pharmaceutical companies
- Patients and caregivers

Source:

https://www.fda.gov/drugs/fda-adverse-event-reporting-system-faers

**Important note**

FAERS data contains **reported associations**, not confirmed causal relationships.

---

# Analysis Focus

This project covers three areas of analysis:

**1. Colorectal and Appendiceal Cancer Population**

Reports are isolated using the FAERS `indi` table, filtering by cancer-related MedDRA indication terms including:

- Colon cancer / Colorectal cancer (all stages)
- Colon cancer metastatic / Colorectal cancer metastatic
- Malignant peritoneal neoplasm / Metastases to peritoneum
- Pseudomyxoma peritonei
- Mucinous adenocarcinoma of appendix

Within this population, the top drugs, adverse reactions, and serious outcomes are analyzed across core chemotherapy regimens (FOLFOX, FOLFIRI, CAPOX) and targeted therapies (Bevacizumab, Cetuximab, Panitumumab).

**2. Fluorouracil-Containing Therapies**

The workflow isolates reports containing Fluorouracil drug labels including:

- Fluorouracil monotherapy
- Fluorouracil combination regimens (FOLFOX, FOLFIRI, FOLFIRINOX)

Drug name normalization is applied to consolidate brand and generic name variants before analysis.

**3. Metformin-Containing Therapies**

Metformin name variants are identified and grouped. Adverse reaction profiles are compared across formulations and combinations including Metformin monotherapy, Metformin/Sitagliptin, Metformin/Vildagliptin, and Empagliflozin/Metformin.

Results across all analyses are visualized using bar charts and normalized heatmaps to compare symptom distributions across drug groups.

---

# Data Processing Steps

The analysis pipeline includes:

1. Build a relational SQLite database from FAERS 2024 quarterly datasets (Q1–Q4)
2. Explore schema and validate table row counts and column types
3. Filter reports by drug name using keyword search (LIKE pattern matching)
4. Filter reports by cancer indication using the `indi` table and MedDRA terms
5. Normalize drug names — map brand names and salt variants to a single standard name
6. Join drug, reaction, indication, and outcome tables on `primaryid`
7. Aggregate reaction and outcome frequencies using GROUP BY and window functions
8. Remove noise indication terms (peritonitis, appendicitis, peritoneal dialysis)
9. Downsample large drug groups to balance the dataset for future ML modeling

Balanced sampling ensures that regression and comparative analyses are not dominated by the most common drug label.

---

# Downsampling Strategy for future ML - Still in progress----

FAERS reporting is highly imbalanced.

Example distribution:


FLUOROURACIL: thousands of reports
Combination therapies: tens to hundreds of reports


To allow fair comparisons between drug mixtures, the dataset is **downsampled** so each drug group contains the same number of reports.

Groups with fewer than **55 reports** are removed.

Remaining groups are randomly sampled to **55 reports per drug label**.

This produces a balanced dataset suitable for exploratory modeling.

---

# Example Analyses

Possible analyses performed on the dataset include:

- Comparison of adverse reaction profiles across drug combinations
- Frequency analysis of reported toxicities
- Serious outcome rates across chemotherapy regimens
- Logistic regression modeling of severe adverse events

These analyses demonstrate how pharmacovigilance datasets can be used to investigate drug safety signals.

---

# Project Structure

```
FDA_FAERS
│
├── notebooks
│   ├── explore_faers_schema.ipynb        # Schema overview and table validation
│   ├── appendiceal_indication.ipynb      # Cancer indication filtering and drug/reaction analysis
│   ├── 5_FU_explore.ipynb                # Fluorouracil adverse event EDA
│   ├── 5_FU_ML.ipynb                     # Fluorouracil ML modeling (in progress)
│   └── Metformin_explore.ipynb           # Metformin adverse event EDA
│
├── database
│   └── faers.db                          # SQLite database (excluded from version control)
│
├── data
│   ├── Dataset ASCII Downloads/          # Raw FAERS quarterly zip files (Q1-Q4 2024)
│   └── Dataset ASCII Extracts/           # Extracted quarterly txt files
│
├── python
│   ├── build_database.py                 # Builds SQLite database from raw FAERS files
│   ├── export_db_samples.py              # Exports sample CSVs for each table
│   └── inspect_data.py                   # Data inspection utilities
│
├── outputs
│   └── db_sample_review/                 # Sample CSVs for each table
│
├── sql
│   └── schema_inspection.sql             # SQL schema inspection queries
│
└── README.md
```

Large database files are excluded from version control.

---

# Technologies Used

- Python
- SQL
- SQLite
- Pandas
- Matplotlib
- Jupyter Notebook
- Git / GitHub

---

# Future Work

Planned extensions to the analysis include:

- Reporting Odds Ratio (ROR) calculations for formal signal detection
- Demographic analysis — age, sex, and country breakdowns within cancer population
- Dechallenge/rechallenge analysis for causal signal strength
- Quarterly trend analysis using LAG window functions
- Seaborn visualizations for drug-reaction heatmaps
- Clustering of toxicity profiles across chemotherapy regimens
- Logistic regression modeling of serious outcomes (DE, HO, LT)
- Class balancing and predictive modeling in 5_FU_ML.ipynb