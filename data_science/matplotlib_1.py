'''
A plotting library for Python.

Provides functions to create line plots, bar charts, scatter plots, histograms, pie charts, and more.

Highly customizable: colors, labels, legends, styles.

Often used with NumPy arrays or Pandas DataFrames.

'''
import numpy as np
import matplotlib.pyplot as plt

print("1. Line Plot...")
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, label="Line")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.legend()
plt.show()

print("2. Scatter Plot")
x = [5, 7, 8, 7, 6, 9, 5, 6]
y = [99, 86, 87, 88, 100, 86, 103, 87]

plt.scatter(x, y, color="red")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Plot Example")
plt.show()

print("3. Bar Chart")
categories = ["A", "B", "C", "D"]
values = [3, 7, 5, 6]

plt.bar(categories, values, color="green")
plt.title("Bar Chart Example")
plt.show()

print("4. Histogram")
data = np.random.randn(1000)  # 1000 random values
plt.hist(data, bins=30, color="blue", alpha=0.7)
plt.title("Histogram Example")
plt.show()

