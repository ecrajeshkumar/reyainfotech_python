import pandas as pd

# 1. Concatenating DataFrame using .concat()
data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
         'Age': [27, 24, 22, 32],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

data2 = {'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
         'Age': [17, 14, 12, 52],
         'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
         'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}

df1 = pd.DataFrame(data1, index = [0,1,2,3])
df2 = pd.DataFrame(data2, index = [4,5,6,7])
frames = [df1, df2]
res = pd.concat(frames)
print(res)

res = pd.concat(frames, keys=['x', 'y'])
print(res)