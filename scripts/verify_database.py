import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

print("=" * 60)
print("DATABASE TABLES")
print("=" * 60)

print(tables)

print("\n")

for table in tables["name"]:
    rows = pd.read_sql(f"SELECT COUNT(*) AS Total_Rows FROM {table}", conn)
    print(f"{table:<25} {rows.iloc[0,0]}")

conn.close()