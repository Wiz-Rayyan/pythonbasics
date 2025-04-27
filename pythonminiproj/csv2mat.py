from tkinter import filedialog
import pandas as pd

def upload_csv():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        # You can auto-select which columns to plot or let user choose
        x = df.columns[0]
        y = df.columns[1]
        plot_chart(df[x], df[y], 'line')  # Example
