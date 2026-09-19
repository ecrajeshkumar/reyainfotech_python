
import numpy as np

# 1D array creation:
one_dimensional_list = [1,2,4]
one_dimensional_arr = np.array(one_dimensional_list)
print("1D array is : \n",one_dimensional_arr) 

#2D array creation:
two_dimensional_list=[[1,2,3],[4,5,6]]
two_dimensional_arr = np.array(two_dimensional_list)
print("2D array is : \n",two_dimensional_arr)

# 3D array creation:
three_dimensional_list=[[[1,2,3],[4,5,6],[7,8,9]]]
three_dimensional_arr = np.array(three_dimensional_list)
print("3D array is : \n",three_dimensional_arr)

# 6D array creation:
ndArray = np.array([1, 2, 3, 4], ndmin=6)
print("ndArray: \n", ndArray)
print('\nDimensions of array:', ndArray.ndim)

'''
You are given a numpy array and a new column as inputs. How will you delete the second column and replace the column with a new column value?

Given array:

[[35 53 63]
[72 12 22]
[43 84 56]]

New Column values:

[  
   20 
   30 
   40
]
'''
import numpy as np
#inputs
inputArray = np.array([[35,53,63],[72,12,22],[43,84,56]])
new_col = np.array([[20,30,40]])
# delete 2nd column
arr = np.delete(inputArray , 1, axis = 1)
#insert new_col to array
arr = np.insert(arr , 1, new_col, axis = 1)
print (arr)

#  How will you find the nearest value in a given numpy array?
def find_nearest_value(arr, value):
   arr = np.asarray(arr)
   idx = (np.abs(arr - value)).argmin()
   return arr[idx]
#Driver code
arr = np.array([ 0.21169,  0.61391, 0.6341, 0.0131, 0.16541,  0.5645,  0.5742])
value = 0.52
print(find_nearest_value(arr, value)) # Prints 0.5645

# How will you reverse the numpy array using one line of code?
reversed_array = arr[::-1]
