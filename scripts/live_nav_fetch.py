import requests
import pandas as pd

scheme_code = "125497"

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

data = response.json()

nav_df = pd.DataFrame(data["data"])

output_file = "data/raw/live_nav_125497.csv"

nav_df.to_csv(output_file, index=False)

print("Live NAV data saved successfully.")
print("Rows:", len(nav_df))
print("File:", output_file)