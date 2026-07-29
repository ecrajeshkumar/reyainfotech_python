import pandas as pd

'''
The index in a Pandas DataFrame represents the labels assigned to each row.
'''

print("Accessing and Modifying the index")

data = {'Name' : ['Rajesh', 'Reya', 'kooku'],
        'Age'  : [40, 7, 25],
        'Gender':['Male', 'Female', 'Trans']
        }
df = pd.DataFrame(data)
print(df.index)
print(df)

print("Setting a custom index")
# The set_index() method is used to change the index of a DataFrame by setting one or more columns as the new index.
res = df.set_index('Name')
print(res)

print("Resetting the index")
res = df.reset_index(drop=True)
print(res)

data = {'age': [25, 30], 'city': ['NY', 'LA']}
df = pd.DataFrame(data, index=['Alice', 'Bob'])
print(df)
row = df.loc['Alice']
print(row)


data = { 'Name': ['Jake', 'Mike', 'Sam'],
         'Age': [25, 30, 22],
         'Salary': [50000, 55000, 40000] }
df = pd.DataFrame(data)
res = df.set_index('Age')
print(res)
