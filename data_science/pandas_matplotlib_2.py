import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("data2.csv")

# Group by city and calculate average age
avg_age = df.groupby("City")["Age"].mean()

# Create subplots: 1 row, 2 columns
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Bar chart
avg_age.plot(kind="bar", ax=axes[0], color="skyblue", edgecolor="black")
axes[0].set_title("Average Age per City - Bar Chart")
axes[0].set_xlabel("City")
axes[0].set_ylabel("Average Age")

# Pie chart
avg_age.plot(kind="pie", ax=axes[1], autopct="%1.1f%%", startangle=90, colors=["lightgreen","lightcoral","lightblue"])
axes[1].set_title("Average Age per City - Pie Chart")
axes[1].set_ylabel("")  # Hide y-label for pie chart

plt.tight_layout()
plt.show()
