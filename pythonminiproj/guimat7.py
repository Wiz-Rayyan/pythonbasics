import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import plotly.express as px
import mysql.connector
import os
from PIL import Image
import io
import uuid
import plotly.io as pio

# Main App Class
class GraphGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV/Excel Graph Generator")
        self.root.geometry("1200x700")

        self.data = None
        self.figure = plt.Figure(figsize=(8, 5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        ttk.Button(frame, text="Upload CSV/Excel", command=self.upload_file).pack(pady=10)

        self.column_label = tk.Label(frame, text="Select X Column")
        self.column_label.pack()
        self.x_column_combo = ttk.Combobox(frame)
        self.x_column_combo.pack()

        self.y_column_label = tk.Label(frame, text="Select Y Column")
        self.y_column_label.pack()
        self.y_column_combo = ttk.Combobox(frame)
        self.y_column_combo.pack()

        self.z_column_label = tk.Label(frame, text="Select Z Column (for 3D/Tree) ")
        self.z_column_label.pack()
        self.z_column_combo = ttk.Combobox(frame)
        self.z_column_combo.pack()

        tk.Label(frame, text="Graph Type").pack()
        self.graph_type = ttk.Combobox(frame, values=[
            "Line", "Bar", "Scatter", "Histogram", "Pie", "Boxplot", "Heatmap",
            "3D Scatter", "3D Surface", "Treemap", "Sunburst Chart", "Radar Chart"
        ])
        self.graph_type.pack()

        tk.Label(frame, text="Title").pack()
        self.title_entry = tk.Entry(frame)
        self.title_entry.pack()

        ttk.Button(frame, text="Generate Graph", command=self.generate_graph).pack(pady=10)
        ttk.Button(frame, text="Upload to MySQL", command=self.save_and_upload).pack(pady=10)
        ttk.Button(frame, text="View Saved Charts", command=self.view_charts).pack(pady=10)
        ttk.Button(frame, text="Delete Chart", command=self.delete_image).pack(pady=10)

        self.image_id_entry = tk.Entry(frame)
        self.image_id_entry.pack()
        self.image_id_entry.insert(0, "Enter Unique ID to Delete")

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx")])
        if file_path:
            if file_path.endswith(".csv"):
                self.data = pd.read_csv(file_path)
            else:
                self.data = pd.read_excel(file_path)

            columns = list(self.data.columns)
            self.x_column_combo['values'] = columns
            self.y_column_combo['values'] = columns
            self.z_column_combo['values'] = columns

    def generate_graph(self):
        graph = self.graph_type.get()
        x = self.x_column_combo.get()
        y = self.y_column_combo.get()
        z = self.z_column_combo.get()
        title = self.title_entry.get()

        if not graph or not x or not y:
            messagebox.showerror("Error", "Please select required columns and graph type")
            return

        self.figure.clf()

        try:
            if graph == "Line":
                ax = self.figure.add_subplot(111)
                ax.plot(self.data[x], self.data[y])
                ax.set_title(title)

            elif graph == "Bar":
                ax = self.figure.add_subplot(111)
                ax.bar(self.data[x], self.data[y])
                ax.set_title(title)

            elif graph == "Scatter":
                ax = self.figure.add_subplot(111)
                ax.scatter(self.data[x], self.data[y])
                ax.set_title(title)

            elif graph == "Histogram":
                ax = self.figure.add_subplot(111)
                ax.hist(self.data[y], bins=10)
                ax.set_title(title)

            elif graph == "Pie":
                self.figure.clf()
                plt.pie(self.data[y], labels=self.data[x], autopct='%1.1f%%')
                plt.title(title)

            elif graph == "Boxplot":
                ax = self.figure.add_subplot(111)
                sns.boxplot(x=self.data[x], y=self.data[y], ax=ax)
                ax.set_title(title)

            elif graph == "Heatmap":
                ax = self.figure.add_subplot(111)
                sns.heatmap(self.data.corr(), annot=True, cmap="coolwarm", ax=ax)
                ax.set_title(title)

            elif graph == "3D Scatter":
                fig = px.scatter_3d(self.data, x=x, y=y, z=z, title=title)
                fig.show()
                return

            elif graph == "3D Surface":
                fig = px.surface(self.data, x=x, y=y, z=z, title=title)
                fig.show()
                return

            elif graph == "Treemap":
                fig = px.treemap(self.data, path=[x, y], values=z, title=title)
                fig.show()
                return

            elif graph == "Sunburst Chart":
                fig = px.sunburst(self.data, path=[x, y], values=z, title=title)
                fig.show()
                return

            elif graph == "Radar Chart":
                categories = self.data[x].tolist()
                values = self.data[y].tolist()
                self.figure.clf()
                ax = self.figure.add_subplot(111, polar=True)
                values += values[:1]
                categories += categories[:1]
                angles = [n / float(len(categories)) * 2 * 3.14159 for n in range(len(categories))]
                ax.plot(angles, values, linewidth=2, linestyle='solid')
                ax.fill(angles, values, 'skyblue', alpha=0.4)
                ax.set_title(title)

            self.canvas.draw()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_and_upload(self):
        unique_id = str(uuid.uuid4())
        file_path = f"{unique_id}.png"
        try:
            self.figure.savefig(file_path)

            with open(file_path, 'rb') as f:
                image_data = f.read()

            os.remove(file_path)

            conn = mysql.connector.connect(host="localhost", user="root", password="writeurownpasswrd", database="graph_db")
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS graphs (
                    id VARCHAR(255) PRIMARY KEY,
                    title TEXT,
                    image LONGBLOB
                )
            """)
            cursor.execute("INSERT INTO graphs (id, title, image) VALUES (%s, %s, %s)", (unique_id, self.title_entry.get(), image_data))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", f"Graph uploaded with ID: {unique_id}")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def view_charts(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="writeurownpasswrd", database="graph_db")
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, image FROM graphs")
            records = cursor.fetchall()
            conn.close()

            view_window = tk.Toplevel(self.root)
            view_window.title("Saved Charts")

            for idx, (img_id, title, image_data) in enumerate(records):
                image = Image.open(io.BytesIO(image_data))
                image = image.resize((400, 300))
                photo = tk.PhotoImage(image)
                label = tk.Label(view_window, image=photo)
                label.image = photo
                label.grid(row=idx, column=0)
                tk.Label(view_window, text=f"ID: {img_id}\nTitle: {title}").grid(row=idx, column=1)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_image(self):
        unique_id = self.image_id_entry.get()
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="writeurownpasswrd", database="graph_db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM graphs WHERE id=%s", (unique_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Deleted", f"Chart with ID {unique_id} deleted.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = GraphGeneratorApp(root)
    root.mainloop()
