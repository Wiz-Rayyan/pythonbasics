import tkinter as tk  
def on_button_click():  
    label.config(text="Hello")

root = tk.Tk()
root.title("Tkinter Example")  
label = tk.Label(root, text="Click the button")  
label.pack(pady=40)  
button = tk.Button(root, text="Click Me", command=on_button_click()) 
button.pack(pady=40)  
root.mainloop() 