import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("=" * 60)
print("Cleaning Scheme Performance Dataset")
print("=" * 60)

# Remove duplicate rows
df = df.drop_duplicates()

# Return columns to validate
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct"
]

# Convert return columns to numeric
for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Convert expense ratio to numeric
df["expense_ratio_pct"] = pd.to_numeric(
    df["expense_ratio_pct"],
    errors="coerce"
)

# Check for invalid expense ratio
invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print(f"Invalid Expense Ratio Records : {len(invalid_expense)}")

# Check for missing values after conversion
print(f"Missing Values After Cleaning : {df.isnull().sum().sum()}")

# Save cleaned dataset
output_path = "data/processed/07_scheme_performance_cleaned.csv"

df.to_csv(output_path, index=False)

print("\nCleaning Completed Successfully")
print(f"Rows    : {len(df)}")
print(f"Columns : {len(df.columns)}")
print(f"Saved to: {output_path}")