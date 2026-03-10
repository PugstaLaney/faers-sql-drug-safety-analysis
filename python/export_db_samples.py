from pathlib import Path
import sqlite3
import pandas as pd

# -------------------------------------------------------
# Export small CSV samples from each SQL table for review
# -------------------------------------------------------

# Project directories
project_root = Path(__file__).resolve().parents[1]
db_path = project_root / "database" / "faers.db"
output_dir = project_root / "outputs" / "db_sample_review"

# Create output folder if it doesn't exist
output_dir.mkdir(exist_ok=True)

# Connect to database
conn = sqlite3.connect(db_path)

# Find all tables in the database
tables_query = """
SELECT name
FROM sqlite_master
WHERE type='table'
ORDER BY name;
"""

tables = pd.read_sql_query(tables_query, conn)["name"].tolist()

print("Tables found:")
for t in tables:
    print(" -", t)

# Export sample rows from each table
for table in tables:

    print(f"\nExporting sample from: {table}")

    query = f"""
    SELECT *
    FROM {table}
    LIMIT 100;
    """

    df = pd.read_sql_query(query, conn)

    output_file = output_dir / f"{table}_sample.csv"
    df.to_csv(output_file, index=False)

    print(f"Saved to: {output_file}")

conn.close()

print("\nSample export complete.")