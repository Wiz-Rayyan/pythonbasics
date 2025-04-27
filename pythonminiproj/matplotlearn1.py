import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_name):
    if file_name.endswith(".csv"):
        return pd.read_csv(file_name)
    elif file_name.endswith(".xlsx"):
        return pd.read_excel(file_name)
    else:
        raise ValueError("Only CSV and Excel files are supported.")

def plot_numeric_columns(df):
    numeric_cols = df.select_dtypes(include='number').columns.tolist()

    if len(numeric_cols) < 2:
        print("Need at least 2 numeric columns to plot.")
        return

    print(f"Numeric columns: {numeric_cols}")

    x_col = input(f"Choose X-axis column from above: ")
    y_col = input(f"Choose Y-axis column from above: ")

    if x_col not in numeric_cols or y_col not in numeric_cols:
        print("❌ Invalid column names.")
        return

    plt.figure(figsize=(8, 5))
    plt.plot(df[x_col], df[y_col], marker='o', color='teal')
    plt.title(f"{y_col} vs {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    file_name = input("Enter filename (CSV or XLSX): ")

    try:
        df = load_data(file_name)
        print("📊 Data Loaded:")
        print(df.head())
        plot_numeric_columns(df)
    except Exception as e:
        print("❌ Error:", e)
