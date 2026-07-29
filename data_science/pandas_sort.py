import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [40, 30, 10, 55],
        'Score': [85, 90, 95, 80]}
df = pd.DataFrame(data)

sorted_df = df.sort_values(by='Age')
print(sorted_df)

sorted_df = df.sort_values(by='Age',ascending=False)
print(sorted_df)

# Sorting a DataFrame by Multiple Columns
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Score': [85, 90, 95, 80]}
df = pd.DataFrame(data)

sorted_df = df.sort_values(by=['Age', 'Score'])
print(sorted_df)
# This will sort first by Age and if multiple rows have the same Age, it will then sort those rows by Salary.
