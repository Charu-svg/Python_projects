import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # for heatmap

# -----------------------------
# Step 1: Create a sample dataset
# -----------------------------
data = {
    "HouseID": [1, 2, 3, 4, 5],
    "Rooms": [3, 4, 2, 5, 3],
    "Size_sqft": [1200, 1500, 800, 2000, 1300],
    "Price": [200000, 250000, 120000, 400000, 220000]
}

df = pd.DataFrame(data)

print("---- Dataset ----")
print(df)

# -----------------------------
# Step 2: Basic Analysis
# -----------------------------
avg_price = df["Price"].mean()
print("\nAverage House Price:", avg_price)

avg_rooms = df["Rooms"].mean()
print("Average Number of Rooms:", avg_rooms)

# -----------------------------
# Step 3: Visualization
# -----------------------------

# Bar chart: Rooms vs Price
plt.figure(figsize=(6, 4))
plt.bar(df["Rooms"], df["Price"], color="skyblue")
plt.xlabel("Number of Rooms")
plt.ylabel("House Price")
plt.title("Rooms vs Price (Bar Chart)")
plt.show()

# Scatter plot: Size vs Price
plt.figure(figsize=(6, 4))
plt.scatter(df["Size_sqft"], df["Price"], color="green")
plt.xlabel("Size (sqft)")
plt.ylabel("House Price")
plt.title("Size vs Price (Scatter Plot)")
plt.show()

# Heatmap: Correlation
plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
