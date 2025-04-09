import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import mysql.connector
from PIL import Image, ImageTk
import io
import os

# MySQL connection details
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '0nbh6mysql',
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

# Fetch image list from DB
def get_image_list():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM images")
    result = cursor.fetchall()
    conn.close()
    return result

# Fetch image by ID
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

        self.graph_type = tk.StringVar()
        self.title = tk.StringVar()
        self.xlabel = tk.StringVar()
        self.ylabel = tk.StringVar()
        self.xdata = tk.StringVar()
        self.ydata = tk.StringVar()

        self.setup_ui()

    def setup_ui(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", padding=6, relief="flat", background="#4caf50", foreground="white")

        tk.Label(self.root, text="Graph Type:", bg="#2e3f4f", fg="white").pack()
        ttk.Combobox(self.root, textvariable=self.graph_type,
                     values=["Line", "Bar", "Pie", "Histogram", "3D"], width=20).pack()

        for label, var in [("Title:", self.title), 
                           ("X-Label / Labels (comma):", self.xlabel), 
                           ("Y-Label / Data (comma):", self.ylabel),
                           ("X-Data (comma):", self.xdata),
                           ("Y-Data (comma):", self.ydata)]:
            tk.Label(self.root, text=label, bg="#2e3f4f", fg="white").pack()
            tk.Entry(self.root, textvariable=var, width=40).pack()

        ttk.Button(self.root, text="Generate Graph", command=self.generate_plot).pack(pady=5)
        ttk.Button(self.root, text="Save & Upload", command=self.save_and_upload).pack(pady=5)
        ttk.Button(self.root, text="View Stored Images", command=self.view_images).pack(pady=5)
        ttk.Button(self.root, text="Delete Image", command=self.delete_image).pack(pady=5)

        self.canvas_frame = tk.Frame(self.root, bg="white")
        self.canvas_frame.pack(fill="both", expand=True)

    def generate_plot(self):
        graph = self.graph_type.get()
        fig = plt.figure()

        try:
            if graph == "3D":
                ax = fig.add_subplot(111, projection='3d')
                x = list(map(float, self.xdata.get().split(',')))
                y = list(map(float, self.ydata.get().split(',')))
                z = list(map(float, self.ylabel.get().split(',')))
                ax.plot(x, y, z)
            else:
                ax = fig.add_subplot(111)
                x = list(map(float, self.xdata.get().split(','))) if self.xdata.get() else []
                y = list(map(float, self.ydata.get().split(',')))

                if graph == "Line":
                    ax.plot(x, y)
                elif graph == "Bar":
                    ax.bar(x, y)
                elif graph == "Histogram":
                    ax.hist(y, bins=10)
                elif graph == "Pie":
                    ax.pie(y, labels=self.xlabel.get().split(','), autopct='%1.1f%%')
                    ax.axis('equal')

                ax.set_xlabel(self.xlabel.get())
                ax.set_ylabel(self.ylabel.get())
                ax.set_title(self.title.get())
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
        self.current_fig = fig

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
