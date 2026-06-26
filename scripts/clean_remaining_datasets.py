import pandas as pd
import os

# Remaining datasets to clean
datasets = {
    "01_fund_master.csv": "01_fund_master_cleaned.csv",
    "03_aum_by_fund_house.csv": "03_aum_by_fund_house_cleaned.csv",
    "04_monthly_sip_inflows.csv": "04_monthly_sip_inflows_cleaned.csv",
    "05_category_inflows.csv": "05_category_inflows_cleaned.csv",
    "06_industry_folio_count.csv": "06_industry_folio_count_cleaned.csv",
    "09_portfolio_holdings.csv": "09_portfolio_holdings_cleaned.csv",
    "10_benchmark_indices.csv": "10_benchmark_indices_cleaned.csv"
}

raw_path = "data/raw"
processed_path = "data/processed"

os.makedirs(processed_path, exist_ok=True)

print("=" * 70)
print("CLEANING REMAINING DATASETS")
print("=" * 70)

for input_file, output_file in datasets.items():

    file_path = os.path.join(raw_path, input_file)

    df = pd.read_csv(file_path)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove leading/trailing spaces from text columns
    object_columns = df.select_dtypes(include="object").columns

    for col in object_columns:
        df[col] = df[col].str.strip()

    # Save cleaned dataset
    output_path = os.path.join(processed_path, output_file)

    df.to_csv(output_path, index=False)

    print(f"✔ {input_file}")
    print(f"   Rows    : {len(df)}")
    print(f"   Columns : {len(df.columns)}")
    print("-" * 70)

print("\nAll remaining datasets cleaned successfully.")