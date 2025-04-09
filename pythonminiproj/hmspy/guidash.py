import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_chart():
    try:
        chart_type = chart_type_var.get()
        x_values = list(map(str.strip, entry_x.get().split(',')))
        y_values = list(map(float, entry_y.get().split(',')))
        
        # Handle non-numeric x values for Pie chart
        if chart_type == "Pie Chart":
            labels = x_values
            sizes = y_values
        else:
            x_values = list(map(float, x_values))

        title = entry_title.get()
        xlabel = entry_xlabel.get()
        ylabel = entry_ylabel.get()
        color = entry_color.get()

        # Clear previous figure if any
        for widget in frame_chart.winfo_children():
            widget.destroy()

        # Create a new figure
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)

        if chart_type == "Line Chart":
            ax.plot(x_values, y_values, color=color)
        elif chart_type == "Bar Chart":
            ax.bar(x_values, y_values, color=color)
        elif chart_type == "Pie Chart":
            ax.pie(sizes, labels=labels, colors=[color]*len(labels), autopct='%1.1f%%')
        elif chart_type == "Scatter Plot":
            ax.scatter(x_values, y_values, color=color)

        if chart_type != "Pie Chart":
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
        ax.set_title(title)

        # Embed chart in GUI
        canvas = FigureCanvasTkAgg(fig, master=frame_chart)
        canvas.draw()
        canvas.get_tk_widget().pack()
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# ---------- GUI START ----------
root = tk.Tk()
root.title("ChartMate - Create Charts Easily")
root.geometry("600x750")

# Chart Type
tk.Label(root, text="Select Chart Type:", font=("Arial", 12)).pack(pady=5)
chart_types = ["Line Chart", "Bar Chart", "Pie Chart", "Scatter Plot"]
chart_type_var = tk.StringVar()
chart_dropdown = ttk.Combobox(root, textvariable=chart_type_var, values=chart_types, state="readonly")
chart_dropdown.pack()
chart_dropdown.current(0)

# Data Inputs
def labeled_entry(label_text):
    tk.Label(root, text=label_text, font=("Arial", 11)).pack(pady=5)
    entry = tk.Entry(root, width=50)
    entry.pack()
    return entry

entry_x = labeled_entry("Enter X values (comma separated):")
entry_y = labeled_entry("Enter Y values (comma separated):")
entry_title = labeled_entry("Chart Title:")
entry_xlabel = labeled_entry("X-axis Label:")
entry_ylabel = labeled_entry("Y-axis Label:")
entry_color = labeled_entry("Color (e.g. red, blue, green):")

# Plot Button
btn_plot = tk.Button(root, text="Plot Chart", font=("Arial", 11), command=plot_chart)
btn_plot.pack(pady=15)

# Chart Display Frame
frame_chart = tk.Frame(root)
frame_chart.pack()

# Run the App
root.mainloop()
