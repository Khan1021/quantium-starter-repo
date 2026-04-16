import pandas as pd
import glob

# Load all 3 CSV files and combine them
files = glob.glob("data/daily_sales_data_*.csv")
df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

# Filter to pink morsel only
df = df[df["product"] == "pink morsel"]

# Remove $ from price and convert to float, then calculate sales
df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)
df["sales"] = df["price"] * df["quantity"]

# Keep only the required columns
df = df[["sales", "date", "region"]]

# Save to output file
df.to_csv("data/output.csv", index=False)

print("Done! output.csv created with", len(df), "rows.")