import os
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------
# Example data
data = {
    "Sales": [100, 200, 300, 400, 500],
    "Profit": [20, 50, 70, 90, 120],
    "Discount": [5, 10, 15, 10, 20]
}
df = pd.DataFrame(data)

# ------------------------
# Create folder to save plots
folder = "plots"
if not os.path.exists(folder):
    os.makedirs(folder)

# ------------------------
# 1️⃣ Scatter plot: Sales vs Profit
plt.figure()
plt.scatter(df["Sales"], df["Profit"], color="teal", alpha=0.6)
plt.title("Scatter Plot: Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(folder, "scatter_sales_profit.png"))
plt.close()

# ------------------------
# 2️⃣ Bar chart: Sales vs Profit
plt.figure()
plt.bar(df["Sales"], df["Profit"], color="orange")
plt.title("Bar Chart: Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig(os.path.join(folder, "bar_chart_sales_profit.png"))
plt.close()

# ------------------------
# 3️⃣ Heatmap: Correlation matrix
corr = df[["Sales","Profit","Discount"]].corr()
plt.figure()
plt.imshow(corr, cmap="coolwarm", interpolation="nearest")
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.index)), corr.index)

# Annotate values
for i in range(len(corr.index)):
    for j in range(len(corr.columns)):
        plt.text(j, i, f"{corr.iloc[i,j]:.2f}", ha="center", va="center", color="black", fontsize=9)

plt.title("Heatmap: Correlation Matrix")
plt.tight_layout()
plt.savefig(os.path.join(folder, "heatmap_sales_profit_discount.png"))
plt.close()

# ------------------------
# 4️⃣ Line chart: Sales vs Profit
plt.figure()
plt.plot(df["Sales"], df["Profit"], marker='o', color="green", linestyle='-')
plt.title("Line Chart: Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(folder, "line_chart_sales_profit.png"))
plt.close()

# ------------------------
print(f"All plots saved successfully in folder: {folder}")
# analysis.py
# Line-by-line Pandas + Matplotlib example with comments for every step.

# 1) load libraries
import pandas as pd                # pandas: for data loading and analysis
import numpy as np                 # numpy: numeric operations (optional)
import matplotlib.pyplot as plt    # matplotlib: for plotting

# 2) read CSV into a DataFrame
# Replace 'data.csv' with your CSV filename if different
df = pd.read_csv("data.csv")       # Read the CSV file into a pandas DataFrame

# 3) inspect the data
print("First 5 rows:")
print(df.head())                   # Show first 5 rows so you know what's inside
print("\nData types & non-null counts:")
print(df.info())                   # Show column types and missing values
print("\nSummary statistics (numeric columns):")
print(df.describe())               # Summary stats like mean, std, min, max

# 4) handle missing values (simple approach)
# If you have missing values, you can drop them or fill them.
# Here we drop rows that have any missing value. Use carefully.
df = df.dropna()                   # Remove rows with missing values

# 5) calculate the average (mean) of a selected column, e.g. "Sales"
average_sales = df["Sales"].mean() # Compute mean of Sales column
print(f"\nAverage Sales: {average_sales:.2f}")

# 6) grouped average: average Sales by Category
avg_by_category = df.groupby("Category")["Sales"].mean().reset_index()
print("\nAverage Sales by Category:")
print(avg_by_category)

# 7) create a bar chart (one figure)
plt.figure(figsize=(8,5))                                    # create a new figure
plt.bar(avg_by_category["Category"], avg_by_category["Sales"])# draw bars
plt.title("Average Sales by Category")                        # title
plt.xlabel("Category")                                        # x-axis label
plt.ylabel("Average Sales")                                   # y-axis label
plt.xticks(rotation=45)                                       # rotate labels so they fit
plt.tight_layout()                                            # adjust layout
plt.savefig("bar_chart.png")                                  # save to file
plt.show()                                                    # display it

# 8) scatter plot: Sales vs Profit
plt.figure(figsize=(7,5))
plt.scatter(df["Sales"], df["Profit"], alpha=0.6)             # scatter
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True)
plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.show()

# 9) heatmap (correlation matrix) using matplotlib (no seaborn)
corr = df[["Sales", "Profit", "Discount"]].corr()             # compute correlation matrix
plt.figure(figsize=(6,5))
plt.imshow(corr, interpolation='nearest')                     # show matrix as heatmap
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.index)), corr.index)
# write numbers on the heatmap
for i in range(len(corr.index)):
    for j in range(len(corr.columns)):
        plt.text(j, i, f"{corr.iloc[i,j]:.2f}", ha='center', va='center', fontsize=9)
plt.title("Correlation matrix")
plt.tight_layout()
plt.savefig("heatmap.png")
plt.show()

# 10) simple insights (text output)
top_category = avg_by_category.loc[avg_by_category["Sales"].idxmax(), "Category"]
print(f"\nCategory with highest average Sales: {top_category}")
print("\nCorrelation matrix:")
print(corr)
