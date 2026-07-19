'''
NumPy is the core Python library for scientific computing, providing powerful N‑dimensional arrays, mathematical functions, random number generation, 
and linear algebra routines. It’s widely used in data science, machine learning, and engineering because it combines Python’s ease of use with 
the speed of optimized C code. 

ndarray object: Efficient, fixed-size, homogeneous data arrays.
Vectorization: Perform operations on entire arrays without explicit loops.
Broadcasting: Apply operations across arrays of different shapes.
Mathematical tools: Linear algebra, Fourier transforms, statistics, random sampling.
Interoperability: Works seamlessly with libraries like Pandas, SciPy, scikit-learn, TensorFlow, and PyTorch.
Performance: Core routines are written in optimized C, making NumPy much faster than pure Python loops.

Quick Comparison: Python Lists vs NumPy Arrays

Feature	                    Python List	                            NumPy Array
Size flexibility	        Dynamic	                                Fixed at creation
Data types	                Mixed	                                Homogeneous
Performance	                Slower	                                Faster
Memory Usage	            More	                                Less
Mathematical Operations	    Not supported	                        Supported
Indexing	                Standard	                            Advanced    

'''

### 1. Creating Arrays
import numpy as np

# 1D array
arr = np.array([1, 2, 3, 4])
print("1D Array:", arr)
# 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:\n", matrix)

### 2. Array Operations
# Element-wise operations
sum_arr = arr + 5
print("Array after adding 5:", sum_arr)
prod_arr = arr * 2
print("Array after multiplying by 2:", prod_arr)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)   # [5 7 9]
print(a * b)   # [4 10 18]


### 3. Indexing and Slicing
print("First element of 1D array:", arr[0])
print("First row of 2D array:\n", matrix[0])
print("Subarray:\n", matrix[0:2, 0:3])

### 3. Broadcasting
# Broadcasting allows operations between arrays of different shapes
c = np.array([[1], [2], [3]])
d = np.array([4, 5, 6])
print("Broadcasting result:\n", c + d)
a = np.array([1, 2, 3])
print(a + 10)   # [11 12 13]


### 4. Reshaping and Transposing
reshaped = matrix.reshape(1, 9)
print("Reshaped array:\n", reshaped)
transposed = matrix.T
print("Transposed array:\n", transposed)

### 5. Mathematical Functions
# Basic mathematical functions
print("Sum of elements in array:", np.sum(arr))
print("Mean of elements in array:", np.mean(arr))
print("Standard deviation of elements in array:", np.std(arr))

arr = np.arange(9).reshape(3,3)
print(arr)

### 6. Data Preparation
# Sample dataset: features and labels
print("Data Preparation")
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([0, 1, 0, 1])

# Normalize features
X_norm = (X - X.mean(axis=0)) / X.std(axis=0)
print(X_norm)

print("Linear Algebra in ML")
# Weight vector
w = np.array([0.5, -0.2])
# Predictions using dot product
preds = X_norm.dot(w)
print(preds)

