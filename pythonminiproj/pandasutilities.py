import pandas as pd

# ----------- Load from CSV or Excel -----------
file_path = input("Enter file name (students.csv or students.xlsx): ")

if file_path.endswith(".csv"):
    df = pd.read_csv(file_path)
elif file_path.endswith(".xlsx"):
    df = pd.read_excel(file_path)
else:
    print("❌ Unsupported file format.")
    exit()

print("\n📊 Loaded Data:\n", df)

# ----------- Sort by Math marks -----------
print("\n🏅 Top Math Students:")
print(df.sort_values(by="Math", ascending=False).head(3))

# ----------- Drop rows with any missing values -----------
print("\n🧹 Dropping rows with missing values:")
cleaned_df = df.dropna()
print(cleaned_df)

# ----------- Fill missing values with column mean -----------
print("\n📥 Filling missing values with column means:")
filled_df = df.fillna(df.mean(numeric_only=True))
print(filled_df)

# ----------- Average per subject -----------
print("\n📚 Average Marks per Subject:")
print(filled_df[["Math", "Science", "English"]].mean())

# ----------- Filter by age -----------
print("\n🎓 Students older than 20:")
print(filled_df[filled_df["Age"] > 20])

# ----------- Save to Excel -----------
filled_df.to_excel("cleaned_students.xlsx", index=False)
print("\n✅ Cleaned data saved to 'cleaned_students.xlsx'")
