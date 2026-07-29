
import pandas as pd

'''
The [] operator is the basic and frequently used method for indexing in Pandas. 
It allows us to select columns and filter rows based on conditions. 
This method can be used to select individual columns or multiple columns.
'''
print("1. Selecting a Single Column")
# To select a single column, we simply refer the column name inside square brackets.
data = pd.read_csv("./nba.csv", index_col="Name")
print(data.head(5))

first = data["Age"]
print(first.head(5))

# 2. Selecting Multiple Columns
# To select multiple columns, pass a list of column names inside the [] operator:
first = data[["Age", "College", "Salary"]]
print("\nMultiple Columns selected from Dataset")
print(first.head(5))


data = pd.read_csv("./nba.csv", index_col="Name")
print("=========\n",data)
row = data.loc["Avery Bradley"]
print(row)

# 2. Selecting Multiple Rows by Label
rows = data.loc[["Avery Bradley", "R.J. Hunter"]]
print(rows)

# 3. Selecting Specific Rows and Columns
selection = data.loc[["Avery Bradley", "R.J. Hunter"], ["Team", "Number", "Position"]]
print(selection)

# 4. Selecting All Rows and Specific Columns
# We can select all rows and specific columns by using a colon [:] to indicate all rows followed by the list of column names
all_rows_specific_columns = data.loc[:, ["Team", "Position", "Salary"]]
print(all_rows_specific_columns)

# 1. Selecting a Single Row by Position
data = pd.read_csv("./nba.csv", index_col="Name")
print("============\n",data)
row = data.iloc[3]
print(row)

# 2. Selecting Multiple Rows by Position
rows = data.iloc[[3, 5, 7]]
print(rows)


# 1. .head(): Returns the first n rows of a DataFrame
print(data.head(5))

# 2. .tail(): Returns the last n rows of a DataFrame
print(data.tail(5))

# 3. .at[]: Access a single value for a row/column label pair
value = data.at["Avery Bradley", "Age"]
print(value)

# 4. .query(): Query the DataFrame using a boolean expression
result = data.query("Age > 25 and College == 'Duke'")
print(result)





