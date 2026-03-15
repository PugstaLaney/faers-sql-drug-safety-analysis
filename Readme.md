# FAERS SQL Drug Safety Analysis

This project builds a relational database from the **FDA Adverse Event Reporting System (FAERS)** quarterly datasets and performs exploratory pharmacovigilance analysis using **SQL, Python, and Jupyter notebooks**.

The workflow demonstrates a data science pipeline for working with large public health datasets containing **millions of adverse event reports**.

---

# Project Goals

This project was built to practice:

- SQL-based analysis on large relational datasets
- Data engineering with Python and SQLite
- Exploratory pharmacovigilance analysis
- Statistical signal detection methods used in drug safety monitoring

---

# Data Pipeline Overview

The analysis pipeline follows these steps:

1. **Download FAERS quarterly ASCII datasets**

2. **Parse and ingest files using Python**

3. **Build a consolidated SQLite database**

4. **Perform feature engineering using SQL**

5. **Analyze drug safety signals using Python and Jupyter notebooks**

The final dataset contains **millions of report–drug pairs** derived from the FAERS reporting system.

---

# Pharmacovigilance Analysis

The project implements a **Reporting Odds Ratio (ROR)** analysis to detect potential safety signals.

The Reporting Odds Ratio is a common method used in pharmacovigilance systems such as:

- FAERS
- EudraVigilance
- WHO VigiBase

ROR compares the odds of a serious adverse event for a specific drug against the background reporting rate for all other drugs.

Contingency table structure:

|                | Serious | Non-Serious |
|---------------|--------|-------------|
| Drug          | a      | b           |
| Other drugs   | c      | d           |

ROR is calculated as:
# FAERS SQL Drug Safety Analysis

This project builds a relational database from the **FDA Adverse Event Reporting System (FAERS)** quarterly datasets and performs exploratory pharmacovigilance analysis using **SQL, Python, and Jupyter notebooks**.

The workflow demonstrates a data science pipeline for working with large public health datasets containing **millions of adverse event reports**.

---

# Project Goals

This project was built to practice:

- SQL-based analysis on large relational datasets
- Data engineering with Python and SQLite
- Exploratory pharmacovigilance analysis
- Statistical signal detection methods used in drug safety monitoring

---

# Data Pipeline Overview

The analysis pipeline follows these steps:

1. **Download FAERS quarterly ASCII datasets**

2. **Parse and ingest files using Python**

3. **Build a consolidated SQLite database**

4. **Perform feature engineering using SQL**

5. **Analyze drug safety signals using Python and Jupyter notebooks**

The final dataset contains **millions of report–drug pairs** derived from the FAERS reporting system.

---

# Pharmacovigilance Analysis

The project implements a **Reporting Odds Ratio (ROR)** analysis to detect potential safety signals.

The Reporting Odds Ratio is a common method used in pharmacovigilance systems such as:

- FAERS
- EudraVigilance
- WHO VigiBase

ROR compares the odds of a serious adverse event for a specific drug against the background reporting rate for all other drugs.

Contingency table structure:

|                | Serious | Non-Serious |
|---------------|--------|-------------|
| Drug          | a      | b           |
| Other drugs   | c      | d           |

ROR is calculated as:
ROR = (a * d) / (b * c)
Values greater than 1 may indicate a potential safety signal.

Note: FAERS is a spontaneous reporting system. Signals identified here do **not imply causation** and require further investigation.

---

# Project Structure
faers-sql-drug-safety-analysis
│
├── scripts
│ ├── build_database.py
│ ├── build_severity_database.py
│ └── export_db_samples.py
│
├── sql
│ ├── schema_inspection.sql
│ ├── basic_counts.sql
│ ├── first_analysis.sql
│ └── build_faers_severity_dataset_table.sql
│
├── notebooks
│ ├── explore_faers_schema.ipynb
│ └── faers_severity_analysis.ipynb
│
├── database
│ └── faers.db
│
└── .gitignore

Large datasets, generated database files, and output artifacts are excluded from version control.

---

# Technologies Used

- Python
- SQLite
- SQL
- Pandas
- Jupyter Notebook
- Git / GitHub

---

# Dataset

FAERS data is provided by the **U.S. Food and Drug Administration (FDA)**.

Source:

https://www.fda.gov/drugs/fda-adverse-event-reporting-system-faers

---

# Future Improvements

Potential extensions to this project include:

- Confidence intervals for Reporting Odds Ratios
- Filtering analyses to **Primary Suspect drugs**
- Reaction-level signal detection
- Visualization of adverse event networks
- Machine learning models predicting serious outcomes
