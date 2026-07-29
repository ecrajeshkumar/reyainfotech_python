'''
Pandas is built on top of NumPy and provides high-level data structures:
    Series → 1D labeled array (like a column in Excel).
    DataFrame → 2D labeled table (like a spreadsheet or SQL table).
It is designed for cleaning, transforming, analyzing, and visualizing data.

Quick Comparison: NumPy vs Pandas

Feature	        NumPy Arrays	        Pandas DataFrame
Labels	        None	                Row & column labels
Data types	    Homogeneous	            Heterogeneous
Operations	    Fast math	            Rich data manipulation
Use case	    Numerical computing	    Data analysis & wrangling
'''

import pandas as pd

# pandas.DataFrame(data, index, columns)


print("1. Creating a Series...")
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)

print("2. Creating a DataFrame...")

df = pd.DataFrame()
print(df)

print("Creating DataFrame from dict of Numpy Array")
# The dictionary contains three keys: 'Name', 'Age' and City.
# Each key has different set of list.
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

print("Creating a DataFrame from a List of Dictionaries")
data = [
    {'name': 'Mike', 'degree': 'MBA', 'score': 90},
    {'name': 'Dan', 'degree': 'BCA', 'score': 40},
    {'name': 'Emilia', 'degree': 'M.Tech', 'score': 80},
]
df = pd.DataFrame(data)
print(df)

print("Creating a DataFrame from Lists or Arrays")
# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)

print("To create a Pandas DataFrame by passing lists of dictionaries and row indexes.")
# Initialize data of lists
data = [{'b': 2, 'c': 3}, {'a': 10, 'b': 20, 'c': 30}]
# Creates pandas DataFrame by passing
# Lists of dictionaries and row index.
df = pd.DataFrame(data, index=['first', 'second'])
print(df)

print("Creating a DataFrame from Another DataFrame")
original_df = pd.DataFrame({
    'Name': ['Tom', 'Nick', 'Krish', 'Jack'],
    'Age': [20, 21, 19, 18]
})
print(original_df)
new_df = original_df[['Name']] 
print(new_df)

print("Create DataFrame from a Dictionary of Series")
# Initialize data to Dicts of series.
d = {'one': pd.Series([10, 20, 30, 40],
                      index=['a', 'b', 'c', 'd']),
     'two': pd.Series([10, 20, 30, 40],
                      index=['a', 'b', 'c', 'd'])}

# creates Dataframe.
df = pd.DataFrame(d)
print(df)

print("Create DataFrame using the zip() function")
# List1
Name = ['tom', 'krish', 'nick', 'juli']
# List2
Age = [25, 30, 26, 22]
# get the list of tuples from two lists.
# and merge them by using zip().
list_of_tuples = list(zip(Name, Age))
print(list_of_tuples)

df = pd.DataFrame(list_of_tuples,
                  columns=['Name', 'Age'])
print(df)


print("Create a DataFrame by Proving the Index Label Explicitly")
# initialize data of lists.
data = {'Name': ['Tom', 'Jack', 'nick', 'juli'],
        'marks': [99, 98, 95, 90]}

# Creates pandas DataFrame.
df = pd.DataFrame(data, index=['rank1',
                               'rank2',
                               'rank3',
                               'rank4'])

# print the data
print(df)


print("pd.DataFrame.from_dict()")
data = [{'name': 'Jake', 'age': 25},
        {'name': 'Martin', 'age': 30}]
df = pd.DataFrame.from_dict(data)
print(df)

print("pd.DataFrame.from_records()")
data = [{'name': 'Jake', 'age': 25},
        {'name': 'Martin', 'age': 30}]
df = pd.DataFrame.from_records(data)
print(df)

print("pd.json_normalize")
data = [{'name': 'Jake', 'age': 25},
        {'name': 'Martin', 'age': 30}]
df = pd.json_normalize(data)
print(df)

