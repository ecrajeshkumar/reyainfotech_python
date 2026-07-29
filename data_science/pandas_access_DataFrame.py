import pandas as pd

data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'], 
        'Age': [25, 30, 22, 35, 28], 
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'], 
        'Salary': [50000, 55000, 40000, 70000, 48000]}

df = pd.DataFrame(data)
# Display the entire DataFrame
print(df)

print("1. Accessing Columns From DataFrame")
# Access the 'Age' column
age_column = df['Age']
print(age_column)

# Access the row at index 1 (second row)
second_row = df.iloc[1]
print(second_row)

# Access the first three rows and the 'Name' and 'Age' columns
subset = df.loc[0:2, ['Name', 'Age']]
print(subset)

# Access rows where 'Age' is greater than 25
filtered_data = df[df['Age'] > 25]
print(filtered_data)

# Access the 'Salary' of the row with label 2
salary_at_index_2 = df.at[2, 'Salary']
print(salary_at_index_2)

