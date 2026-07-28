'''
NumPy stands for Numerical Python and is used for handling large, multi-dimensional arrays and matrices.

'''

import numpy as np

print("Converting list into numpy array")
lst = [1,2,3,4,5]
print("list ", type(lst), lst)
arr = np.array(lst)
print("array from list", type(arr), arr)

print("\n Multi-Dimensional Array")
lst1 = [1,3,5,7,9]
lst2 = [0,2,4,6,8]
lst3 = [100,200,300,400,500]
arr2D = np.array([lst1,lst2])
print("2D array\n", arr2D)
arr2D2 = np.array([lst1,lst2,lst3])
print("2D2 array\n", arr2D2)

print("shape: indicates the number of elements along each dimension. It is returned as a tuple.")
print(arr2D.shape)
print(arr2D2.shape)

print("the rank of an array means the number of dimensions (axes) it has.")
print("Rank (ndim):", arr2D.ndim)
print("Rank (ndim):", arr2D2.ndim)
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Array:\n", arr3)
print("Rank (ndim):", arr3.ndim)   # Output: 3

print("(dtype): property specifies the type of data stored in an array, such as integers, floating-point numbers, or strings.")
arr1 = np.array([0, 4, 2])
arr2 = np.array([0.2, 0.4, 2.4])
print("Data type of array 1:", arr1.dtype)
print("Data type of array 2:", arr2.dtype)

print("Different Ways of Creating Numpy Array")

print("1. numpy.array(): creates a NumPy array from Python sequences such as lists or tuples.")
arr = np.array([1,3,5,7,9])
print(type(arr))
'''
In Numpy the 'U2' data type reprsents Unicode strings with a fixed length of 2 characters.
The 'U' indicates that the data type in Unicode, and the number '2' specifies the length of each string.
'''
print("2. numpy.fromiter(): creates a one-dimensional array from an iterable object.")
text = "ILoveMyIndia"
arr = np.fromiter(text, dtype="U2")  # numpy.fromiter(iterable, dtype, count = -1)
print(type(arr))
print(arr)

unicode = [71, 101, 101, 107]
arr = np.fromiter((chr(x) for x in unicode), dtype='U1')
print(arr)

my_iterable=[1,2,3,4,5,6]
my_array = np.fromiter(my_iterable,dtype=int)
print(my_array)

iterable = (x**3 for x in range(4))
arr = np.fromiter(iterable, int)
print (arr)

iterable = (x * x for x in range(6))
arr = np.fromiter(iterable, float)
print (arr)


print("3. numpy.arange(): returns evenly spaced values within a specified range.")
arr = np.arange(5 , 10)   # numpy.arange(start, stop, step, dtype=None)
print(arr)
arr = np.arange(1, 20, 5, dtype=np.float32)
print(arr)
sequence = np.arange(10) # By default, the sequence starts from 0 and increases by 1 until the stop value is reached (excluding it).
print("Basic Sequence:", sequence)
sequence = np.arange(0, 1, 0.2)
print("Floating-Point Sequence:", sequence)

sequence = np.arange(0, 20, 3)
print(sequence)
filtered = sequence[sequence > 10]
print("Filtered Sequence:", filtered)

print("4. numpy.linspace(): returns a specified number of evenly spaced values between two limits.")
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
arr = np.linspace(3.5, 10, 3, dtype=np.int32)
print(arr)

a = np.linspace(0, 1, num=10)
print(a)

b = np.linspace(0, 1, num=10, endpoint=False)
print(b)

array, c = np.linspace(0, 10, num=5, retstep=True)
print("Step Size:", c)

d = np.linspace(0, 1, num=16).reshape(4, 4)
print(d)

print("5. numpy.empty(): creates an array of a given shape without initializing its values.")
# numpy.empty(shape, dtype = float, order = 'C')
b = np.empty(2, dtype = int)
print("Matrix b : \n", b)

a = np.empty([2, 2], dtype = int)
print("\nMatrix a : \n", a)

c = np.empty([3, 3])
print("\nMatrix c : \n", c)

print("6. numpy.ones(): creates an array filled with ones.")
# numpy.ones() is used to create a NumPy array of a specified shape where all elements are initialized to 1.
# numpy.ones(shape, dtype=float, order='C')
arr = np.ones(5)
print(arr)

arr = np.ones((3, 4))
print(arr)

arr = np.ones((2, 3), dtype=int)
print(arr)

arr = np.ones((2, 2, 3))
print(arr)

print("7. numpy.zeros(): creates an array filled with zeros.")
# numpy.zeros(shape, dtype=float, order='C')
# numpy.zeros() is used to create a NumPy array of a specified shape where all elements are initialized to 0.
arr = np.zeros(5)
print(arr)

arr = np.zeros((3, 4))
print(arr)

arr = np.zeros((2, 3), dtype=int)
print(arr)

arr = np.zeros((2, 2, 3))
print(arr)

print("8. numpy.full() in Python")
# numpy.full(shape, fill_value, dtype = None, order = 'C')
a = np.full([2, 2], 67, dtype = int)
print("\nMatrix a : \n", a)

c = np.full([3, 3], 10.1)
print("\nMatrix c : \n", c)

print("9. numpy.random.rand()")
# numpy.random.rand(d0, d1, ..., dn)
# Parameters: d0, d1, ..., dn - Integers specifying the dimensions of the output array. If no arguments are given, a single float value is returned
x = np.random.rand()
print(x)

arr = np.random.rand(5)
print(arr)

arr = np.random.rand(3, 4)
print(arr)

arr = np.random.rand(2, 2, 2)
print(arr)

an = np.random.randn(2, 2)
ai = np.random.randint(1, 10, size=(2, 3)) 
print(an)
print(ai)
