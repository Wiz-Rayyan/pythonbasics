import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
import mysql.connector
import io
from PIL import Image, ImageTk
import plotly.express as px
import plotly.graph_objects as go
import math

class GraphGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Generator")
        self.root.geometry("1200x700")

        self.data = None
        self.columns = []

        # User inputs
        self.graph_type = tk.StringVar()
        self.x_column = tk.StringVar()
        self.y_column = tk.StringVar()
        self.z_column = tk.StringVar()
        self.graph_title = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=10)

        tk.Button(top_frame, text="Upload CSV/Excel", command=self.upload_data).pack(side="left", padx=10)

        tk.Label(top_frame, text="Graph Type:").pack(side="left")
        graph_menu = ttk.Combobox(top_frame, textvariable=self.graph_type, values=[
            "Line Chart", "Bar Chart", "Pie Chart", "Histogram", "Box Plot",
            "Scatter Plot", "Area Chart", "Heatmap", "Violin Plot", "Radar Chart",
            "3D Surface", "3D Scatter", "Treemap", "Sunburst Chart", "Funnel Chart", "Waterfall Chart"
        ], state="readonly")
        graph_menu.pack(side="left", padx=5)
        graph_menu.current(0)

        tk.Label(top_frame, text="X Axis:").pack(side="left")
        self.x_col_dropdown = tk.OptionMenu(top_frame, self.x_column, "")
        self.x_col_dropdown.pack(side="left", padx=5)

        tk.Label(top_frame, text="Y Axis:").pack(side="left")
        self.y_col_dropdown = tk.OptionMenu(top_frame, self.y_column, "")
        self.y_col_dropdown.pack(side="left", padx=5)

        tk.Label(top_frame, text="Z Axis (for 3D/Tree/Sunburst):").pack(side="left")
        self.z_col_dropdown = tk.OptionMenu(top_frame, self.z_column, "")
        self.z_col_dropdown.pack(side="left", padx=5)

        tk.Label(top_frame, text="Title:").pack(side="left")
        tk.Entry(top_frame, textvariable=self.graph_title, width=20).pack(side="left", padx=5)

        tk.Button(top_frame, text="Generate Chart", command=self.generate_plot).pack(side="left", padx=10)

        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack(fill="both", expand=True)

        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(pady=10)

        tk.Button(bottom_frame, text="Upload Chart to MySQL", command=self.save_and_upload).pack(side="left", padx=10)
        tk.Button(bottom_frame, text="View Stored Charts", command=self.view_images).pack(side="left", padx=10)
        tk.Button(bottom_frame, text="Delete Stored Charts", command=self.delete_image).pack(side="left", padx=10)

    def upload_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
        if not file_path:
            return
        try:
            if file_path.endswith('.csv'):
                self.data = pd.read_csv(file_path)
            else:
                self.data = pd.read_excel(file_path)
            self.columns = self.data.columns.tolist()
            self.update_dropdowns()
            messagebox.showinfo("Success", "Data loaded successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data:\n{e}")

    def update_dropdowns(self):
        menu_x = self.x_col_dropdown["menu"]
        menu_y = self.y_col_dropdown["menu"]
        menu_z = self.z_col_dropdown["menu"]

        menu_x.delete(0, "end")
        menu_y.delete(0, "end")
        menu_z.delete(0, "end")

        for col in self.columns:
            menu_x.add_command(label=col, command=tk._setit(self.x_column, col))
            menu_y.add_command(label=col, command=tk._setit(self.y_column, col))
            menu_z.add_command(label=col, command=tk._setit(self.z_column, col))

    def generate_plot(self):
        if self.data is None:
            messagebox.showerror("Error", "Please upload a dataset first.")
            return

        graph = self.graph_type.get()
        x = self.x_column.get()
        y = self.y_column.get()
        z = self.z_column.get()
        title = self.graph_title.get()

        fig = None
        try:
            if graph in ["Line Chart", "Bar Chart", "Pie Chart", "Histogram", "Box Plot",
                         "Scatter Plot", "Area Chart", "Heatmap", "Violin Plot", "Radar Chart",
                         "3D Surface", "3D Scatter"]:
                fig = plt.figure(figsize=(8, 5))
                ax = fig.add_subplot(111, projection='3d' if '3D' in graph else None)

                if graph == "Line Chart":
                    ax.plot(self.data[x], self.data[y])
                elif graph == "Bar Chart":
                    ax.bar(self.data[x], self.data[y])
                elif graph == "Pie Chart":
                    plt.pie(self.data[y], labels=self.data[x], autopct='%1.1f%%')
                elif graph == "Histogram":
                    ax.hist(self.data[y], bins=10)
                elif graph == "Box Plot":
                    sns.boxplot(data=self.data, x=x, y=y, ax=ax)
                elif graph == "Scatter Plot":
                    ax.scatter(self.data[x], self.data[y])
                elif graph == "Area Chart":
                    ax.stackplot(self.data[x], self.data[y])
                elif graph == "Heatmap":
                    sns.heatmap(self.data.corr(), annot=True, ax=ax)
                elif graph == "Violin Plot":
                    sns.violinplot(data=self.data, x=x, y=y, ax=ax)
                elif graph == "Radar Chart":
                    labels = self.data[x].tolist()
                    values = self.data[y].tolist()
                    angles = [n / float(len(labels)) * 2 * math.pi for n in range(len(labels))]
                    values += values[:1]
                    angles += angles[:1]
                    ax = plt.subplot(111, polar=True)
                    ax.plot(angles, values)
                    ax.fill(angles, values, alpha=0.25)
                    ax.set_xticks(angles[:-1])
                    ax.set_xticklabels(labels)
                elif graph == "3D Surface":
                    ax.plot_surface(self.data[x], self.data[y], self.data[z], cmap='viridis')
                elif graph == "3D Scatter":
                    ax.scatter(self.data[x], self.data[y], self.data[z])

                ax.set_title(title)
            else:
                if graph == "Funnel Chart":
                    fig = px.funnel(self.data, x=self.data[x], y=self.data[y])
                elif graph == "Sunburst Chart":
                    fig = px.sunburst(self.data, path=[x, y], values=z)
                elif graph == "Treemap":
                    fig = px.treemap(self.data, path=[x, y], values=z)
                elif graph == "Waterfall Chart":
                    fig = go.Figure(go.Waterfall(x=self.data[x], y=self.data[y], measure=["relative"] * len(self.data)))

                fig.show()
                return

        except Exception as e:
            messagebox.showerror("Error", f"Plot generation failed:\n{e}")
            return

        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def save_and_upload(self):
        if self.canvas_frame.winfo_children():
            widget = self.canvas_frame.winfo_children()[0]
            postscript = widget.postscript(colormode='color')
            img = Image.open(io.BytesIO(postscript.encode('utf-8')))
            buffer = io.BytesIO()
            img.save(buffer, format='PNG')
            img_bytes = buffer.getvalue()

            conn = mysql.connector.connect(host="localhost", user="root", password="", database="graph_db")
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS charts (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), image LONGBLOB)")
            cursor.execute("INSERT INTO charts (title, image) VALUES (%s, %s)", (self.graph_title.get(), img_bytes))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Chart uploaded to MySQL successfully!")

    def view_images(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="", database="graph_db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, image FROM charts")
        records = cursor.fetchall()
        conn.close()

        view_win = tk.Toplevel(self.root)
        view_win.title("Stored Charts")

        for idx, (id, title, image) in enumerate(records):
            img = Image.open(io.BytesIO(image))
            img.thumbnail((400, 300))
            photo = ImageTk.PhotoImage(img)
            label = tk.Label(view_win, text=title, image=photo, compound='top')
            label.image = photo
            label.grid(row=idx//2, column=idx%2, padx=10, pady=10)

    def delete_image(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="writeurownpasswrd", database="graph_db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, title FROM charts")
        records = cursor.fetchall()

        delete_win = tk.Toplevel(self.root)
        delete_win.title("Delete Chart")

        def delete_selected(id):
            cursor.execute("DELETE FROM charts WHERE id = %s", (id,))
            conn.commit()
            delete_win.destroy()
            messagebox.showinfo("Deleted", "Chart deleted successfully.")

        for id, title in records:
            btn = tk.Button(delete_win, text=f"Delete '{title}'", command=lambda i=id: delete_selected(i))
            btn.pack(pady=5)

        conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphGeneratorApp(root)
    root.mainloop()
