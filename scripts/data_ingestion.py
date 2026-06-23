import pandas as pd
import os

data_folder = "data/raw"

print("=" * 60)
print("MUTUAL FUND DATA INGESTION")
print("=" * 60)

for file in os.listdir(data_folder):

    if file.endswith(".csv"):

        file_path = os.path.join(data_folder, file)

        print("\n" + "=" * 60)
        print("FILE:", file)
        print("=" * 60)

        df = pd.read_csv(file_path)

        print("Shape:", df.shape)
        print("Columns:", len(df.columns))
        print("Missing Values:")
        print(df.isnull().sum())

        print("\nFirst 5 Rows:")
        print(df.head())