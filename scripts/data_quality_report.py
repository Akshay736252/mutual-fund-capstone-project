import pandas as pd
import os

data_folder = "data/raw"

print("=" * 70)
print("MUTUAL FUND DATA QUALITY REPORT")
print("=" * 70)

for file in os.listdir(data_folder):

    if file.endswith(".csv"):

        file_path = os.path.join(data_folder, file)

        df = pd.read_csv(file_path)

        print("\n" + "=" * 70)
        print(f"FILE: {file}")
        print("=" * 70)

        rows, cols = df.shape

        missing_values = df.isnull().sum().sum()

        duplicate_rows = df.duplicated().sum()

        print(f"Rows: {rows}")
        print(f"Columns: {cols}")
        print(f"Total Missing Values: {missing_values}")
        print(f"Duplicate Rows: {duplicate_rows}")