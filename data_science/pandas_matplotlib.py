import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("data2.csv")

# Preview first 5 rows
print(df.head())

# Group by city and calculate average age
avg_age = df.groupby("City")["Age"].mean()

print(avg_age)

# Plot bar chart
avg_age.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Average Age per City")
plt.xlabel("City")
plt.ylabel("Average Age")
plt.show()
