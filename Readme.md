FAERS SQL Drug Safety Analysis

This project builds a relational database from the FDA FAERS (FDA Adverse Event Reporting System) quarterly ASCII datasets and performs exploratory drug safety analysis using SQL and Python.

The workflow demonstrates a basic data pipeline for large public datasets:

Download FAERS quarterly ASCII datasets

Parse and ingest the files using Python

Build a consolidated SQLite database

Inspect the schema and relationships

Perform exploratory analysis using SQL and Jupyter notebooks

The goal of this project is to practice SQL-based data analysis on a real-world dataset containing millions of adverse event reports.
```
Project Structure
faers-sql-drug-safety-analysis
│
├── python
│   ├── build_database.py
│   ├── export_db_samples.py
│   └── inspect_data.py
│
├── sql
│   ├── schema_inspection.sql
│   ├── basic_counts.sql
│   └── first_analysis.sql
│
├── notebooks
│   └── explore_faers_schema.ipynb
│
└── .gitignore
```
Large datasets, generated database files, and outputs are excluded from version control.