# =============================================================================
# FAERS Database Builder
#
# This script compiles FDA FAERS ASCII quarterly datasets into a single
# SQLite database for analysis.
#
# FAERS releases adverse event reports in separate quarterly ASCII files.
# Each quarter contains tables such as DEMO, DRUG, REAC, OUTC, INDI, etc.
#
# This script:
# 1. Iterates through the quarterly dataset folders (Q1–Q4)
# 2. Loads each ASCII table using pandas
# 3. Adds a column identifying the source quarter
# 4. Appends the data into unified SQL tables
#
# Result:
# A SQLite database containing consolidated FAERS tables that can be
# queried using SQL or accessed through Python for analysis.
# 
# Note: Datatype converted to string due to memory overload.
# =============================================================================

from pathlib import Path
import pandas as pd
import sqlite3

project_root = Path(__file__).resolve().parents[1]
extracts_root = project_root / "data" / "Dataset ASCII Extracts"
db_path = project_root / "database" / "faers.db"

quarter_dirs = [
    extracts_root / "ASCII Q1",
    extracts_root / "ASCII Q2",
    extracts_root / "ASCII Q3",
    extracts_root / "ASCII Q4",
]

conn = sqlite3.connect(db_path)

for quarter_dir in quarter_dirs:
    quarter_name = quarter_dir.name.replace("ASCII ", "").strip()

    print(f"\nProcessing folder: {quarter_dir}")

    txt_files = sorted(quarter_dir.glob("*.txt"))

    for file_path in txt_files:
        table_name = file_path.stem[:4].lower()   # DEMO -> demo, DRUG -> drug

        print(f"  Loading {file_path.name} into table '{table_name}'")

        df = pd.read_csv(
            file_path,
            delimiter="$",
            encoding="latin1",
            dtype=str,
            low_memory=False)

        df["source_quarter"] = quarter_name

        df.to_sql(
            table_name,
            conn,
            if_exists="append",
            index=False
        )

conn.close()

print("\nDatabase build complete.")


# ### Build was successful based on terminal output.

# #Processing folder: C:\Users\palla\OneDrive\Documents\Coding Projects\FDA_FAERS\data\Dataset ASCII Extracts\ASCII Q1
#   Loading DEMO24Q1.txt into table 'demo'
#   Loading DRUG24Q1.txt into table 'drug'
#   Loading INDI24Q1.txt into table 'indi'
#   Loading OUTC24Q1.txt into table 'outc'
#   Loading REAC24Q1.txt into table 'reac'
#   Loading RPSR24Q1.txt into table 'rpsr'
#   Loading THER24Q1.txt into table 'ther'

# Processing folder: C:\Users\palla\OneDrive\Documents\Coding Projects\FDA_FAERS\data\Dataset ASCII Extracts\ASCII Q2
#   Loading DEMO24Q2.txt into table 'demo'
#   Loading DRUG24Q2.txt into table 'drug'
#   Loading INDI24Q2.txt into table 'indi'
#   Loading OUTC24Q2.txt into table 'outc'
#   Loading REAC24Q2.txt into table 'reac'
#   Loading RPSR24Q2.txt into table 'rpsr'
#   Loading THER24Q2.txt into table 'ther'

# Processing folder: C:\Users\palla\OneDrive\Documents\Coding Projects\FDA_FAERS\data\Dataset ASCII Extracts\ASCII Q3
#   Loading DEMO24Q3.txt into table 'demo'
#   Loading DRUG24Q3.txt into table 'drug'
#   Loading INDI24Q3.txt into table 'indi'
#   Loading OUTC24Q3.txt into table 'outc'
#   Loading REAC24Q3.txt into table 'reac'
#   Loading RPSR24Q3.txt into table 'rpsr'
#   Loading THER24Q3.txt into table 'ther'

# Processing folder: C:\Users\palla\OneDrive\Documents\Coding Projects\FDA_FAERS\data\Dataset ASCII Extracts\ASCII Q4
#   Loading DEMO24Q4.txt into table 'demo'
#   Loading DRUG24Q4.txt into table 'drug'
#   Loading INDI24Q4.txt into table 'indi'
#   Loading OUTC24Q4.txt into table 'outc'
#   Loading REAC24Q4.txt into table 'reac'
#   Loading RPSR24Q4.txt into table 'rpsr'
#   Loading THER24Q4.txt into table 'ther'

# Database build complete.
# PS C:\Users\palla\OneDrive\Documents\Coding Projects> 