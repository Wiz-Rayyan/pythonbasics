import pandas as pd

def load_file(file_name):
    if file_name.endswith(".csv"):
        return pd.read_csv(file_name)
    elif file_name.endswith(".xlsx"):
        return pd.read_excel(file_name)
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx")

def show_summary(df):
    print("\n📊 Data Preview:")
    print(df.head())

    print("\n🔢 Numeric Columns:", df.select_dtypes(include='number').columns.tolist())

    print("\n📉 Description of Numeric Columns:")
    print(df.describe())

    print("\n❓ Missing Values per Column:")
    print(df.isnull().sum())

def show_top_3_averaged(df):
    numeric_df = df.select_dtypes(include='number')
    if numeric_df.empty:
        print("\n❌ No numeric columns to compute average.")
        return
    df['Average'] = numeric_df.mean(axis=1)
    print("\n🏆 Top 3 Rows with Highest Averages:")
    print(df.sort_values(by='Average', ascending=False).head(3))
    df.drop(columns="Average", inplace=True)  # optional cleanup

if __name__ == "__main__":
    file_name = input("Enter file name (with .csv or .xlsx): ")
    
    try:
        df = load_file(file_name)
        show_summary(df)
        show_top_3_averaged(df)
    except Exception as e:
        print("❌ Error:", e)
