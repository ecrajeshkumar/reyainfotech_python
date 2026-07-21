'''
Pandas is built on top of NumPy and provides high-level data structures:
    Series → 1D labeled array (like a column in Excel).
    DataFrame → 2D labeled table (like a spreadsheet or SQL table).
It’s designed for cleaning, transforming, analyzing, and visualizing data.

Quick Comparison: NumPy vs Pandas

Feature	        NumPy Arrays	        Pandas DataFrame
Labels	        None	                Row & column labels
Data types	    Homogeneous	            Heterogeneous
Operations	    Fast math	            Rich data manipulation
Use case	    Numerical computing	    Data analysis & wrangling
'''

import pandas as pd

print("1. Creating a Series...")
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)

print("2. Creating a DataFrame...")
data = {
    "Name": ["Rajesh", "Punam", "Prince"],
    "Age": [35, 32, 5],
    "City": ["Pune", "Pune", "Pune"]
}
df = pd.DataFrame(data)
print(df)

print("3. Selecting Data...")
print(df["Name"]) # Select column
print(df.loc[0])  # Select row by label
print(df.iloc[1])  # Select row by index

print("4. Filtering...")
print(df[df["Age"] > 30])

print("5. Grouping and Aggregation...")
print(df.groupby("City")["Age"].mean())

