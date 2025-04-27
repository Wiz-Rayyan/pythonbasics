import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mysql.connector
from PIL import Image, ImageTk
import io
import os
import pandas as pd  # for reading from table in csv

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

# Fetch image list from DB. Returns a list of all stored images as (id, name) tuples.
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
        self.uploaded_df = None  # to hold CSV/Excel data

        self.setup_ui()

    def setup_ui(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", padding=6, relief="flat", background="#4caf50", foreground="white")

        tk.Label(self.root, text="Graph Type:", bg="#2e3f4f", fg="white").pack()
        ttk.Combobox(self.root, textvariable=self.graph_type,
                     values=["Line", "Bar", "Pie", "Histogram", "3D", "Scatter", "3D Scatter", "Boxplot", "Bubble Chart"], width=20).pack()

        for label, var in [("Title:", self.title), 
                           ("X-Label (Bar/Line):", self.xlabel), 
                           ("Y-Label (Bar/Line) / Z-axis in 3D:", self.ylabel),
                           ("X-Data (comma):", self.xdata),
                           ("Y-Data (comma):", self.ydata)]:
            tk.Label(self.root, text=label, bg="#2e3f4f", fg="white").pack()
            tk.Entry(self.root, textvariable=var, width=40).pack()

        ttk.Button(self.root, text="Upload CSV/Excel & Generate Graph", command=self.upload_data_and_generate_plot).pack(pady=5)
        ttk.Button(self.root, text="Generate Graph", command=self.generate_plot).pack(pady=5)

        ttk.Button(self.root, text="Save & Upload", command=self.save_and_upload).pack(pady=5)
        ttk.Button(self.root, text="View Stored Images", command=self.view_images).pack(pady=5)
        ttk.Button(self.root, text="Delete Image", command=self.delete_image).pack(pady=5)

        self.canvas_frame = tk.Frame(self.root, bg="white")
        self.canvas_frame.pack(fill="both", expand=True)

    def upload_data_and_generate_plot(self):
        # Open file dialog for CSV/Excel file
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx *.xls")])
        if not file_path:
            return

        try:
            if file_path.endswith(('.xlsx', '.xls')):
                df = pd.read_excel(file_path)
            elif file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            else:
                messagebox.showerror("Error", "Unsupported file type!")
                return

            # Store DataFrame
            self.uploaded_df = df
            self.generate_plot()
        except Exception as e:
            messagebox.showerror("Error", f"Error while reading the file: {str(e)}")

    def generate_plot(self):
        # Check if we have uploaded data, otherwise use manual input data
        if self.uploaded_df is None:
            # Use manual input data
            try:
                xdata = list(map(float, self.xdata.get().split(',')))
                ydata = list(map(float, self.ydata.get().split(',')))
            except ValueError:
                messagebox.showerror("Error", "Invalid data entered. Please enter comma-separated numeric values.")
                return
            if len(xdata) != len(ydata):
                messagebox.showerror("Error", "X and Y data must have the same length.")
                return
            df = pd.DataFrame({'X': xdata, 'Y': ydata})
        else:
            # Use uploaded CSV/Excel data
            df = self.uploaded_df

        graph = self.graph_type.get()
        fig = plt.figure()
        ax = fig.add_subplot(111)

        if graph == "Line":
            df.plot(x='X', y='Y', ax=ax)
        elif graph == "Bar":
            df.plot(kind='bar', x='X', y='Y', ax=ax)
        elif graph == "Pie":
            df.plot.pie(y='Y', ax=ax)
        elif graph == "3D Scatter":
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(df['X'], df['Y'], df['Y'])  # Dummy 3D plot using Y values again as Z for simplicity
        else:
            messagebox.showerror("Error", f"Graph type {graph} not supported yet.")

        ax.set_title(self.title.get())
        ax.set_xlabel(self.xlabel.get())
        ax.set_ylabel(self.ylabel.get())

        # Display plot on Tkinter canvas
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()
        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    def save_and_upload(self):
        # Save the plot as an image and upload it to MySQL
        img_path = "graph_image.png"
        plt.savefig(img_path)
        upload_image(img_path, "graph_image")
        messagebox.showinfo("Success", "Image saved and uploaded to MySQL!")

    def view_images(self):
        images = get_image_list()
        if not images:
            messagebox.showinfo("No Images", "No images found in the database.")
            return

        for img in images:
            img_data = fetch_image_by_id(img[0])
            if img_data:
                image = Image.open(io.BytesIO(img_data))
                image.show()

    def delete_image(self):
        images = get_image_list()
        if not images:
            messagebox.showinfo("No Images", "No images found in the database.")
            return

        img_ids = [img[0] for img in images]
        selected_img_id = simpledialog.askinteger("Select Image", "Enter the image ID to delete:", minvalue=1, maxvalue=len(images))
        if selected_img_id in img_ids:
            delete_image_by_id(selected_img_id)
            messagebox.showinfo("Success", "Image deleted from database.")
        else:
            messagebox.showerror("Error", "Invalid image ID.")

if __name__ == "__main__":
    create_table()
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
