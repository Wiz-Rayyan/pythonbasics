import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns

class SimpleGraphApp:
    def __init__(self, root):  # ✅ Fix: correct __init__ method
        self.root = root
        self.root.title("Graph Generator")
        self.root.geometry("1000x600")

        self.data = None
        self.figure = plt.Figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.setup_widgets()

    def setup_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        ttk.Button(frame, text="Upload CSV/Excel", command=self.load_file).pack(pady=10)

        tk.Label(frame, text="X Column").pack()
        self.x_col = ttk.Combobox(frame)
        self.x_col.pack()

        tk.Label(frame, text="Y Column").pack()
        self.y_col = ttk.Combobox(frame)
        self.y_col.pack()

        tk.Label(frame, text="Graph Type").pack()
        self.graph_type = ttk.Combobox(frame, values=[
            "Line", "Bar", "Scatter", "Histogram", "Pie", "Boxplot", "Heatmap"
        ])
        self.graph_type.pack()

        ttk.Button(frame, text="Generate Graph", command=self.generate_graph).pack(pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV/Excel", "*.csv *.xlsx")])
        if not file_path:
            return

        try:
            if file_path.endswith(".csv"):
                self.data = pd.read_csv(file_path)
            else:
                self.data = pd.read_excel(file_path)

            columns = list(self.data.columns)
            self.x_col['values'] = columns
            self.y_col['values'] = columns
            messagebox.showinfo("File Loaded", "File loaded successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file:\n{e}")

    def generate_graph(self):
        if self.data is None:
            messagebox.showerror("Error", "Please upload a file first.")
            return

        x = self.x_col.get()
        y = self.y_col.get()
        gtype = self.graph_type.get()

        if not gtype:
            messagebox.showerror("Error", "Please select a graph type.")
            return

        self.figure.clf()
        ax = self.figure.add_subplot(111)

        try:
            if gtype == "Line":
                ax.plot(self.data[x], self.data[y])
            elif gtype == "Bar":
                ax.bar(self.data[x], self.data[y])
            elif gtype == "Scatter":
                ax.scatter(self.data[x], self.data[y])
            elif gtype == "Histogram":
                ax.hist(self.data[y].dropna(), bins=10)
            elif gtype == "Pie":
                self.figure.clf()
                plt.pie(self.data[y].dropna(), labels=self.data[x], autopct="%1.1f%%")
                plt.title("Pie Chart")
            elif gtype == "Boxplot":
                sns.boxplot(x=self.data[x], y=self.data[y], ax=ax)
            elif gtype == "Heatmap":
                self.figure.clf()
                sns.heatmap(self.data.corr(), annot=True, cmap="coolwarm", ax=self.figure.add_subplot(111))
            else:
                messagebox.showerror("Error", "Unknown graph type.")
                return

            self.canvas.draw()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate graph:\n{e}")

if __name__ == "__main__": 
    root = tk.Tk()
    app = SimpleGraphApp(root)
    root.mainloop()
