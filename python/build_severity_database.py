from pathlib import Path
import sqlite3

# ---------------------------------------------
# Run SQL script to build FAERS severity dataset
# ---------------------------------------------

# Project root
project_root = Path(__file__).resolve().parents[1]

# Paths
db_path = project_root / "database" / "faers.db"
sql_file_path = project_root / "sql" / "build_faers_severity_dataset_table.sql"

# Connect to database
conn = sqlite3.connect(db_path)

# Read SQL file
with open(sql_file_path, "r", encoding="utf-8") as file:
    sql_script = file.read()

# Execute SQL script
conn.executescript(sql_script)

# Save changes and close connection
conn.commit()
conn.close()

print("faers_severity_dataset table created successfully.")