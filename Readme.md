# Fluorouracil and Metformin FAERS Safety Analysis

This project analyzes adverse event reports associated with **Fluorouracil (5-FU)** and **Metformin** using data from the **FDA Adverse Event Reporting System (FAERS)**.

The current goal is to explore how different **Fluorouracil drug combinations** and **Metformin drug combinations** appear in adverse event reports and examine their associated safety outcomes using **SQL, Python, and Jupyter notebooks**.

The project demonstrates how large pharmacovigilance datasets can be filtered, cleaned, and analyzed to investigate potential safety signals. This is a learning project for complex SQL queries and python EDA. More advanced statistical analysis and ML are planned.

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

This project focuses specifically on **Fluorouracil-containing therapies, and Metforming-containing therapies**.

The workflow isolates reports containing drug labels with:

FLUOROURACIL
METFORMIN


These labels include:

- Fluorouracil monotherapy
- Fluorouracil combination regimens
- Multi-drug chemotherapy protocols

Examples found in the dataset include:


FLUOROURACIL
FLUOROURACIL\LEUCOVORIN
FLUOROURACIL\OXALIPLATIN
FLUOROURACIL\IRINOTECAN
FLUOROURACIL\IRINOTECAN\LEUCOVORIN\OXALIPLATIN

METFORMIN
METFORMIN HYDROCHLORIDE
METFORMIN\SITAGLIPTIN
METFORMIN HYDROCHLORIDE\VILDAGLIPTIN
METFORMIN HYDROCHLORIDE\SITAGLIPTIN PHOSPHATE
EMPAGLIFLOZIN\METFORMIN HYDROCHLORIDE
METFORMIN PAMOATE
CANAGLIFLOZIN\METFORMIN HYDROCHLORIDE
DAPAGLIFLOZIN PROPANEDIOL\METFORMIN HYDROCHLORIDE



The analysis integrates adverse reaction data with filtered Fluorouracil/Metform report groups by joining REAC and DRUG tables on report identifiers. Aggregated SQL queries were used to compute symptom frequencies for each drug combination, alongside quarterly report trends. Results were visualized using bar charts and normalized heatmaps to compare symptom distributions across regimens.

---

# Data Processing Steps

The analysis pipeline includes:

1. Build a relational SQLite database from FAERS quarterly datasets  
2. Filter reports containing Fluorouracil drug labels  
3. Identify common drug combinations  
4. Remove extremely rare labels  
5. Downsample large groups to balance the dataset  

Balanced sampling ensures that regression and comparative analyses are not dominated by the most common label (Fluorouracil monotherapy).

---

# Downsampling Strategy - Still in progress----

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
fluorouracil-faers-analysis
│
├── notebooks
│ ├── explore_faers_schema.ipynb
│ └── fluorouracil_analysis.ipynb
│
├── database
│ └── faers.db
│
├── scripts
│ └── build_database.py
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

Potential extensions to the analysis include:

- Reaction-level signal detection
- Reporting Odds Ratio (ROR) calculations
- Visualization of adverse event networks
- Clustering of toxicity profiles across chemotherapy regimens
- Predictive modeling of serious outcomes