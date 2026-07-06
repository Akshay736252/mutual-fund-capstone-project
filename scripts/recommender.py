import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

performance = pd.read_sql(
    "SELECT * FROM fact_performance",
    engine
)

print("=" * 60)
print("MUTUAL FUND RECOMMENDER")
print("=" * 60)

risk = input("Enter Risk Appetite (Low/Moderate/High): ").strip().lower()

if risk == "low":
    recommendation = performance.sort_values(
        "expense_ratio_pct"
    ).head(3)

elif risk == "moderate":
    recommendation = performance.sort_values(
        "return_3yr_pct",
        ascending=False
    ).head(3)

elif risk == "high":
    recommendation = performance.sort_values(
        "return_5yr_pct",
        ascending=False
    ).head(3)

else:
    print("Invalid Input")
    exit()

print("\nTop Recommendations\n")

print(
    recommendation[
        [
            "scheme_name",
            "fund_house",
            "return_3yr_pct",
            "return_5yr_pct",
            "expense_ratio_pct"
        ]
    ]
)