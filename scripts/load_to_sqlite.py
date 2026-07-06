import os
import pandas as pd
from sqlalchemy import create_engine

# Project Root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Absolute Database Path
db_path = os.path.join(BASE_DIR, "bluestock_mf.db")

engine = create_engine(f"sqlite:///{db_path}")

datasets = {
    "dim_fund": os.path.join(BASE_DIR, "data", "processed", "01_fund_master_cleaned.csv"),
    "fact_nav": os.path.join(BASE_DIR, "data", "processed", "02_nav_history_cleaned.csv"),
    "fact_aum": os.path.join(BASE_DIR, "data", "processed", "03_aum_by_fund_house_cleaned.csv"),
    "fact_sip": os.path.join(BASE_DIR, "data", "processed", "04_monthly_sip_inflows_cleaned.csv"),
    "fact_category_inflows": os.path.join(BASE_DIR, "data", "processed", "05_category_inflows_cleaned.csv"),
    "fact_folio": os.path.join(BASE_DIR, "data", "processed", "06_industry_folio_count_cleaned.csv"),
    "fact_performance": os.path.join(BASE_DIR, "data", "processed", "07_scheme_performance_cleaned.csv"),
    "fact_transactions": os.path.join(BASE_DIR, "data", "processed", "08_investor_transactions_cleaned.csv"),
    "fact_holdings": os.path.join(BASE_DIR, "data", "processed", "09_portfolio_holdings_cleaned.csv"),
    "dim_benchmark": os.path.join(BASE_DIR, "data", "processed", "10_benchmark_indices_cleaned.csv")
}

print("=" * 60)
print("LOADING DATA INTO SQLITE DATABASE")
print("=" * 60)

for table_name, file_path in datasets.items():

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"✔ {table_name}")
    print(f"Rows Loaded : {len(df)}")
    print("-" * 60)

print("\nDatabase Created Successfully!")
print("Database Name : bluestock_mf.db")