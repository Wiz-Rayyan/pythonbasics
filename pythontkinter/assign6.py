import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load the CSV data and create a pandas DataFrame
df = pd.read_csv("diabetes.csv")  # Ensure the CSV file is in the same directory

# Step 3: Data Analysis - Mean, Median, Standard Deviation of "Pregnancies"
mean_preg = df["Pregnancies"].mean()
median_preg = df["Pregnancies"].median()
std_preg = df["Pregnancies"].std()

print("Statistics for 'Pregnancies':")
print(f"Mean: {mean_preg}")
print(f"Median: {median_preg}")
print(f"Standard Deviation: {std_preg}")

# Step 4: Filter rows where Pregnancies > 2
filtered_df = df.loc[df["Pregnancies"] > 2]
print("\nFiltered Data (Pregnancies > 2):")
print(filtered_df.head())  # Display first few rows

# Step 5a: Scatter Plot for Glucose Levels
plt.figure(figsize=(7, 5))
plt.scatter(df.index, df["Glucose"], color='blue', alpha=0.5)
plt.xlabel("Index")
plt.ylabel("Glucose Level")
plt.title("Scatter Plot of Glucose Levels")
plt.grid(True)
plt.show()

# Step 5b: Histogram for Insulin Levels
plt.figure(figsize=(7, 5))
plt.hist(df["Insulin"], bins=20, color='purple', alpha=0.7, edgecolor='black')
plt.xlabel("Insulin Level")
plt.ylabel("Frequency")
plt.title("Histogram of Insulin Levels")
plt.grid(True)
plt.show()
