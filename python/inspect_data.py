from pathlib import Path
import pandas as pd

project_root = Path(__file__).resolve().parents[1]
data_dir = project_root / "data" / "Dataset ASCII Extracts" / "ASCII"

# Only keep .txt files
txt_files = sorted(data_dir.glob("*.txt"))

print("TXT files found:")
for f in txt_files:
    print(" -", f.name)

# Load each txt file and preview the first 3 rows
for file_path in txt_files:
    print(f"\n{'=' * 60}")
    print(f"Loading: {file_path.name}")

    df = pd.read_csv(
        file_path,
        delimiter="$",
        encoding="latin1",
        nrows=3,
        low_memory=False
    )

    print("\nColumns:")
    print(list(df.columns))

    print("\nPreview:")
    print(df.head())