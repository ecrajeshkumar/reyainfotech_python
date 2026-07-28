import numpy as np

print("1. Accessing Elements in 1D Arrays")
arr = np.array([10, 20, 30, 40, 50])
print(arr[0])

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)
print(matrix[1, 2])

print("Slicing Arrays")
arr = np.array([0, 1, 2, 3, 4, 5])
print(arr[1:4])

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[0:2, 1:3])

arr = np.array([10, 15, 20, 25, 30])
print(arr[arr > 20])

print("Broadcasting in Conditional Operations")
a = np.array([12, 24, 35, 15, 60, 72])
b = np.array(["Adult", "Minor"])
res = np.where(a > 18, b[0], b[1])
print(res)


img = np.array([ [100, 120, 130],
                 [90, 110, 140],
                 [80, 100, 120] ])

m = img.mean(axis=0)
s = img.std(axis=0)
res = (img - m) / s
print(res)