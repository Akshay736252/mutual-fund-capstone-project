import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 60)
print("Cleaning NAV History Dataset")
print("=" * 60)

# 1. Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# 2. Sort by AMFI code and date
df = df.sort_values(by=["amfi_code", "date"])

# 3. Remove duplicate rows
df = df.drop_duplicates()

# 4. Forward fill missing NAV values
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# 5. Validate NAV > 0
invalid_nav = df[df["nav"] <= 0]

print(f"Invalid NAV records: {len(invalid_nav)}")

# 6. Save cleaned dataset
output_path = "data/processed/02_nav_history_cleaned.csv"
df.to_csv(output_path, index=False)

print("\nCleaning Completed Successfully")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Saved to: {output_path}")