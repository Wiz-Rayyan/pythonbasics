import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mysql.connector
from PIL import Image, ImageTk
import io
import os
import pandas as pd #for reading from table in csv

# MySQL connection details
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'writeurownpasswrd',
    'database': 'my_database'
}

# Ensure MySQL table exists
def create_table():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS images (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            data LONGBLOB
        )
    ''')
    conn.commit()
    conn.close()

# Upload image to MySQL
def upload_image(image_path, name):
    with open(image_path, 'rb') as file:
        binary_data = file.read()
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO images (name, data) VALUES (%s, %s)", (name, binary_data))
    conn.commit()
    conn.close()

# Fetch image list from DB . Returns a list of all stored images as (id, name) tuples.
def get_image_list():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM images")
    result = cursor.fetchall()
    conn.close()
    return result

# Fetch image by ID. Gets the binary image data for a given image ID.
def fetch_image_by_id(img_id):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT data FROM images WHERE id = %s", (img_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Delete image by ID
def delete_image_by_id(img_id):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM images WHERE id = %s", (img_id,))
    conn.commit()
    conn.close()

# Main Application Class
class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Creator & MySQL Image Manager")
        self.root.geometry("1000x700")
        self.root.configure(bg="#2e3f4f")
# These StringVars hold user inputs for dropdowns and text fields.
        self.graph_type = tk.StringVar()
        self.title = tk.StringVar()
        self.xlabel = tk.StringVar()
        self.ylabel = tk.StringVar()
        self.xdata = tk.StringVar()
        self.ydata = tk.StringVar()
        self.uploaded_df = None  # to hold CSV data


        self.setup_ui()

    def setup_ui(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", padding=6, relief="flat", background="#4caf50", foreground="white")

        tk.Label(self.root, text="Graph Type:", bg="#2e3f4f", fg="white").pack()
        ttk.Combobox(self.root, textvariable=self.graph_type,
                     values=["Line", "Bar", "Pie", "Histogram", "3D", "Horizontal Bar",  
            "Scatter", "Boxplot", "Area", "3D Line", "3D Scatter", "3D Line Chart", "3D Bar Chart", "3D Scatter Chart",
            "Box Plot", "Area Chart", "Stacked Bar Chart", "Bubble Chart",
            "Scatter Plot", "Donut Chart", "Violin Plot", "Heatmap", 
            "Radar Chart", "Step Chart", "Polar Area Chart", 
            "Funnel Chart", "Sunburst Chart", "Treemap", 
            "Waterfall Chart", "Error Bar Chart", "Hexbin Plot"], width=20).pack()

        for label, var in [("Title:", self.title), 
                           ("X-Label (Bar/Line/piechart):", self.xlabel), 
                           ("Y-Label (Bar/Line) / z-axis in 3D:", self.ylabel),
                           ("X-Data (comma):", self.xdata),
                           ("Y-Data (comma):", self.ydata)]:
            tk.Label(self.root, text=label, bg="#2e3f4f", fg="white").pack()
            tk.Entry(self.root, textvariable=var, width=40).pack()

        ttk.Button(self.root, text="Generate Graph", command=self.generate_plot).pack(pady=5)
        ttk.Button(self.root, text="Upload CSV and Plot", command=self.fupload_csv).pack(pady=5)
        ttk.Button(self.root, text="Upload CSV", command=self.upload_data).pack(pady=5)
        ttk.Button(self.root, text="Plot CSV", command=self.plot_csv_data).pack(pady=5)
        upload_btn = tk.Button(self.root, text="Upload CSV/Excel", command=self.upload_data)
        upload_btn.pack(pady=10)

                # Chart Type Dropdown
        self.graph_var = tk.StringVar()
        self.chart_dropdown = ttk.Combobox(self.root, textvariable=self.graph_var, values=self.graph_type, state="readonly", width=40)
        self.chart_dropdown.set("Select Chart Type")
        self.chart_dropdown.pack(pady=10)

                # Generate Button
        generate_btn = tk.Button(self.root, text="Generate Chart", command=self.generate_plot)
        generate_btn.pack(pady=10)



        ttk.Button(self.root, text="Save & Upload", command=self.save_and_upload).pack(pady=5)
        ttk.Button(self.root, text="View Stored Images", command=self.view_images).pack(pady=5)
        ttk.Button(self.root, text="Delete Image", command=self.delete_image).pack(pady=5)

        self.canvas_frame = tk.Frame(self.root, bg="white")
        self.canvas_frame.pack(fill="both", expand=True)

        self.x_column = tk.StringVar()
        self.y_column = tk.StringVar()
        self.z_column = tk.StringVar()

        self.x_col_dropdown = ttk.OptionMenu(self.root, self.x_column, "")
        self.y_col_dropdown = ttk.OptionMenu(self.root, self.y_column, "")
        self.z_col_dropdown = ttk.OptionMenu(self.root, self.z_column, "")

        self.x_col_dropdown.pack(pady=5)
        self.y_col_dropdown.pack(pady=5)
        self.z_col_dropdown.pack(pady=5)

    def generate_plot(self):
        graph = self.graph_type.get()
        fig = plt.figure()
        ax = None

        try:
            if self.data is None or self.data.empty:
                messagebox.showerror("Error", "No data available to plot.")
                return

            numeric_data = self.data.select_dtypes(include=['number'])
            if numeric_data.shape[1] == 0:
                messagebox.showerror("Error", "The file does not contain numeric data.")
                return

            self.columns = self.data.columns.tolist()  # Refresh columns list

            if graph in ["3D Line", "3D Scatter", "3D Line Chart", "3D Bar Chart", "3D Scatter Chart"]:
                if numeric_data.shape[1] < 3:
                    messagebox.showerror("Error", "At least 3 numeric columns required for 3D plots.")
                    return
                x = numeric_data.iloc[:, 0]
                y = numeric_data.iloc[:, 1]
                z = numeric_data.iloc[:, 2]
                ax = fig.add_subplot(111, projection='3d')

                if graph in ["3D Line", "3D Line Chart"]:
                    ax.plot(x, y, z)
                elif graph in ["3D Scatter", "3D Scatter Chart"]:
                    ax.scatter(x, y, z)
                elif graph == "3D Bar Chart":
                    for i in range(len(x)):
                        ax.bar3d(x[i], y[i], 0, 1, 1, z[i])
                ax.set_xlabel(self.columns[0])
                ax.set_ylabel(self.columns[1])
                ax.set_zlabel(self.columns[2])

            elif graph == "Line":
                ax = fig.add_subplot(111)
                numeric_data.plot(ax=ax)
            elif graph == "Bar":
                ax = fig.add_subplot(111)
                numeric_data.plot(kind='bar', ax=ax)
            elif graph == "Stacked Bar Chart":
                ax = fig.add_subplot(111)
                numeric_data.plot(kind='bar', stacked=True, ax=ax)
            elif graph == "Horizontal Bar":
                ax = fig.add_subplot(111)
                numeric_data.plot(kind='barh', ax=ax)
            elif graph == "Scatter":
                ax = fig.add_subplot(111)
                numeric_data.plot.scatter(x=self.columns[0], y=self.columns[1], ax=ax)
            elif graph == "Bubble Chart":
                ax = fig.add_subplot(111)
                numeric_data.plot.scatter(x=self.columns[0], y=self.columns[1], s=numeric_data[self.columns[2]]*10, alpha=0.5, ax=ax)
            elif graph == "Histogram":
                ax = fig.add_subplot(111)
                numeric_data.plot(kind='hist', ax=ax)
            elif graph == "Pie":
                ax = fig.add_subplot(111)
                numeric_data.iloc[0].plot.pie(autopct='%1.1f%%', ax=ax)
                ax.axis('equal')
            elif graph == "Box Plot":
                ax = fig.add_subplot(111)
                numeric_data.plot(kind='box', ax=ax)
            elif graph == "Area Chart":
                ax = fig.add_subplot(111)
                numeric_data.plot(kind='area', stacked=False, ax=ax)
            elif graph == "Violin Plot":
                import seaborn as sns
                ax = fig.add_subplot(111)
                sns.violinplot(data=numeric_data, ax=ax)
            elif graph == "Heatmap":
                import seaborn as sns
                ax = fig.add_subplot(111)
                sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm", ax=ax)
            elif graph == "Radar Chart":
                from math import pi
                categories = self.columns
                values = numeric_data.iloc[0].tolist()
                values += values[:1]
                angles = [n / float(len(categories)) * 2 * pi for n in range(len(categories))]
                angles += angles[:1]
                ax = plt.subplot(111, polar=True)
                plt.xticks(angles[:-1], categories)
                ax.plot(angles, values)
                ax.fill(angles, values, alpha=0.25)
            elif graph == "Step Chart":
                ax = fig.add_subplot(111)
                numeric_data.plot(drawstyle='steps-post', ax=ax)
            elif graph == "Polar Area Chart":
                ax = plt.subplot(111, polar=True)
                theta = list(range(numeric_data.shape[1]))
                radii = numeric_data.iloc[0]
                bars = ax.bar(theta, radii)
            elif graph == "Hexbin Plot":
                ax = fig.add_subplot(111)
                numeric_data.plot.hexbin(x=self.columns[0], y=self.columns[1], gridsize=25, ax=ax)
            elif graph == "Donut Chart":
                ax = fig.add_subplot(111)
                numeric_data.iloc[0].plot.pie(wedgeprops=dict(width=0.5), ax=ax)
                ax.axis('equal')
            elif graph == "Error Bar Chart":
                ax = fig.add_subplot(111)
                x = numeric_data[self.columns[0]]
                y = numeric_data[self.columns[1]]
                yerr = numeric_data[self.columns[2]]
                ax.errorbar(x, y, yerr=yerr, fmt='-o')

            # Plotly charts (separate handling)
            elif graph in ["Funnel Chart", "Sunburst Chart", "Treemap", "Waterfall Chart"]:
                import plotly.express as px
                import plotly.graph_objects as go
                if graph == "Funnel Chart":
                    fig = px.funnel(self.data, x=self.columns[0], y=self.columns[1])
                elif graph == "Sunburst Chart":
                    fig = px.sunburst(self.data, path=self.columns[:2], values=self.columns[2])
                elif graph == "Treemap":
                    fig = px.treemap(self.data, path=self.columns[:2], values=self.columns[2])
                elif graph == "Waterfall Chart":
                    fig = go.Figure(go.Waterfall(x=self.data[self.columns[0]], y=self.data[self.columns[1]]))
                fig.show()
                return

            # Labeling
            if ax:
                ax.set_title(self.title.get())
                ax.set_xlabel(self.xlabel.get())
                ax.set_ylabel(self.ylabel.get())

        except Exception as e:
            messagebox.showerror("Error", f"Error while plotting: {str(e)}")
            return

        # Display plot on Tkinter canvas
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()
        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
        self.current_fig = fig

        
# now trims space. when numpy considers this as 
    def upload_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx *.xls")])
        if not file_path:
            return

        try:
            if file_path.endswith(('.xlsx', '.xls')):
                df = pd.read_excel(file_path, header=0)
            elif file_path.endswith('.csv'):
                df = pd.read_csv(file_path, header=0)
            else:
                messagebox.showerror("Error", "Unsupported file type!")
                return

            # Clean and convert to numeric
            df = df.apply(lambda col: pd.to_numeric(col, errors='coerce') if col.dtype == object else col)
            df = df.dropna(axis=1, how='all')  # Drop columns that are all NaN
            df = df.dropna(axis=0, how='all')  # Drop rows that are all NaN

            if df.select_dtypes(include='number').shape[1] < 1:
                messagebox.showerror("Error", "File uploaded but doesn't contain numeric data.")
                return

            self.data = df

            self.populate_column_dropdowns()

            messagebox.showinfo("Success", f"File uploaded with shape: {df.shape}")
            self.populate_column_dropdowns()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to upload file:\n{str(e)}")
    def populate_column_dropdowns(self):
      if hasattr(self, 'df') and not self.df.empty:
          numeric_columns = self.df.select_dtypes(include='number').columns.tolist()
          
          if not numeric_columns:
              messagebox.showerror("Error", "No numeric columns found in the file.")
              return

          # Clear existing options
          self.x_col_dropdown['menu'].delete(0, 'end')
          self.y_col_dropdown['menu'].delete(0, 'end')
          self.z_col_dropdown['menu'].delete(0, 'end')

          # Add new options
          for col in numeric_columns:
              self.x_col_dropdown['menu'].add_command(label=col, command=tk._setit(self.x_column, col))
              self.y_col_dropdown['menu'].add_command(label=col, command=tk._setit(self.y_column, col))
              self.z_col_dropdown['menu'].add_command(label=col, command=tk._setit(self.z_column, col))

          # Set default values
          if numeric_columns:
              self.x_column.set(numeric_columns[0])
              self.y_column.set(numeric_columns[1] if len(numeric_columns) > 1 else numeric_columns[0])
              self.z_column.set(numeric_columns[2] if len(numeric_columns) > 2 else numeric_columns[0])



    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV/Excel Files", "*.csv *.xlsx *.xls")])
        if file_path:
            try:
                if file_path.endswith('.csv'):
                    df = pd.read_csv(file_path, header=None)  # Assuming no header
                    df.columns = [f'Col{i+1}' for i in range(df.shape[1])]
                elif file_path.endswith(('.xls', '.xlsx')):
                    df = pd.read_excel(file_path)
                else:
                    messagebox.showerror("Unsupported File", "Only CSV and Excel files are supported.")
                    return

                df.columns = df.columns.str.strip()  # Clean header names
                self.uploaded_df = df
                self.numeric_columns = df.select_dtypes(include='number').columns.tolist()

                if not self.numeric_columns:
                    messagebox.showwarning("No Numeric Data", "File uploaded, but doesn't contain numeric data.")
                    return

                self.update_column_dropdowns()
                messagebox.showinfo("Success", "File uploaded successfully.")

            except Exception as e:
                messagebox.showerror("Error", f"Failed to read file:\n{str(e)}")



    def plot_csv_data(self):
        if self.uploaded_df is None:
            messagebox.showerror("Error", "No CSV uploaded.")
            return

        df = self.uploaded_df
        graph = self.graph_type.get().lower()
        fig = plt.figure()

        try:
            if graph in ['line', 'bar', 'histogram']:
                x = df.iloc[:, 0]
                y = df.iloc[:, 1]
                ax = fig.add_subplot(111)

                if graph == 'line':
                    ax.plot(x, y)
                elif graph == 'bar':
                    ax.bar(x, y)
                elif graph == 'histogram':
                    ax.hist(y, bins=10)

                ax.set_xlabel(df.columns[0])
                ax.set_ylabel(df.columns[1])
                ax.set_title(f"{graph.capitalize()} Chart from CSV")

            elif graph == 'pie':
                y = df.iloc[:, 1]
                labels = df.iloc[:, 0]
                ax = fig.add_subplot(111)
                ax.pie(y, labels=labels, autopct='%1.1f%%')
                ax.axis('equal')
                ax.set_title("Pie Chart from CSV")
            else:
                messagebox.showerror("Invalid Chart Type", "Only Line, Bar, Pie, and Histogram charts are supported for CSV")
                return

            for widget in self.canvas_frame.winfo_children():
                widget.destroy()

            canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)
            self.current_fig = fig

        except Exception as e:
            messagebox.showerror("Error", f"Failed to plot: {e}")

            #-----

    def fupload_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                df = pd.read_csv(file_path)
                x = df.iloc[:, 0]
                y = df.iloc[:, 1]

                fig = plt.figure()
                ax = fig.add_subplot(111)

                graph = self.graph_type.get().lower()

                if graph == "line":
                    ax.plot(x, y)
                elif graph == "bar":
                    ax.bar(x, y)
                elif graph == "histogram":
                    ax.hist(y, bins=10)
                elif graph == "pie":
                    ax.pie(y, labels=x, autopct='%1.1f%%')
                    ax.axis('equal')
                else:
                    messagebox.showerror("Invalid", "Unsupported chart type for CSV")
                    return

                ax.set_title("CSV Plot")
                ax.set_xlabel("X")
                ax.set_ylabel("Y")

                for widget in self.canvas_frame.winfo_children():
                    widget.destroy()

                canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
                canvas.draw()
                canvas.get_tk_widget().pack(fill='both', expand=True)
                self.current_fig = fig
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read or plot CSV: {e}")



    def save_and_upload(self):
        if not hasattr(self, 'current_fig'):
            messagebox.showerror("Error", "No graph to save")
            return

        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if filename:
            self.current_fig.savefig(filename)
            upload_image(filename, os.path.basename(filename))
            messagebox.showinfo("Success", "Image uploaded to MySQL")

    def view_images(self):
        image_list = get_image_list()
        if not image_list:
            messagebox.showinfo("Info", "No images in database")
            return

        top = tk.Toplevel(self.root)
        top.title("Stored Images")
        top.geometry("600x600")

        for img_id, name in image_list:
            btn = ttk.Button(top, text=f"{img_id}: {name}", command=lambda i=img_id: self.show_image(i))
            btn.pack(fill='x')

    def show_image(self, img_id):
        data = fetch_image_by_id(img_id)
        if data:
            image = Image.open(io.BytesIO(data))
            image.show()

    def delete_image(self):
        image_list = get_image_list()
        if not image_list:
            messagebox.showinfo("Info", "No images to delete")
            return

        top = tk.Toplevel(self.root)
        top.title("Delete Image")
        top.geometry("400x300")

        for img_id, name in image_list:
            btn = ttk.Button(top, text=f"Delete {img_id}: {name}",
                             command=lambda i=img_id: self.confirm_delete(i, top))
            btn.pack(fill='x')

    def confirm_delete(self, img_id, window):
        delete_image_by_id(img_id)
        messagebox.showinfo("Deleted", f"Image ID {img_id} deleted")
        window.destroy()




# Run the app
if __name__ == '__main__':
    create_table()
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
