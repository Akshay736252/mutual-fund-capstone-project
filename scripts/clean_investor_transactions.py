import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("=" * 60)
print("Cleaning Investor Transactions Dataset")
print("=" * 60)

# 1. Convert transaction_date to datetime
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# 2. Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.upper()
)

# 3. Remove duplicate rows
df = df.drop_duplicates()

# 4. Validate amount
invalid_amount = df[df["amount_inr"] <= 0]

# 5. Validate KYC status
valid_kyc = ["Verified", "Pending"]

invalid_kyc = df[~df["kyc_status"].isin(valid_kyc)]

print(f"Invalid Amount Records : {len(invalid_amount)}")
print(f"Invalid KYC Records    : {len(invalid_kyc)}")

# 6. Save cleaned dataset
output_path = "data/processed/08_investor_transactions_cleaned.csv"

df.to_csv(output_path, index=False)

print("\nCleaning Completed Successfully")
print(f"Rows    : {len(df)}")
print(f"Columns : {len(df.columns)}")
print(f"Saved to: {output_path}")