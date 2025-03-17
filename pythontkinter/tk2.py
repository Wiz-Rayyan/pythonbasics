import tkinter as tk
from tkinter import *
from tkinter import messagebox

r = tk.Tk()
r.geometry("400x600")


def bton_cluticking():
  messagebox.showinfo("no info", "button has been clicked")

def war():
  messagebox.showwarning("no warning", "u clicked b2")

b1 = Button(r, text="b1", width=15, height=2, command= bton_cluticking,)
b1.grid()

b2 = Button(r, text="b2", width=15, height=2, command= war,)
b2.grid(row=0,column=1)

b3 = Button(r, text="b3", width=15, height=2)
b3.grid()

# b4 = Button(r, text="b4", width=15, height=2)
# b4.place(x=50, y=70) # x, y is of pixel position



r.mainloop()