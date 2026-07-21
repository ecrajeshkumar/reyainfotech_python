'''
let’s walk through how to filter rows and select specific columns right after loading a CSV with Pandas. 
This is the bread‑and‑butter of real‑world data analysis.
'''
import pandas as pd

print("Load CSV file...")
df = pd.read_csv("data.csv")

print("Preview the first 5 rows...")
print(df.head())
# print(df.info())
# print(df.describe())

print("Select specific columns...")
print(df[["year", "industry_name_ANZSIC"]])

print("Filter rows where year > 2020...")
filtered = df[df["year"] > 2020]
print(filtered)

print("Combine filtering and column selection...")
print(df.loc[df["year"] > 2020, ["industry_name_ANZSIC", "value"]])



