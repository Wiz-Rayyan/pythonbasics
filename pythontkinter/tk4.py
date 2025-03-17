import tkinter as tk
from tkinter import *
from tkinter import messagebox

r = tk.Tk()
r.geometry("400x500")

def button_clicking():
  messagebox.showerror("no    Error", "button has been clicked")

Button(
  r,
  text="Click",
  bg="#000000",
  fg="#ffffff",
  width=20,
  height= 2,
  command = button_clicking,
).pack()

e1 =Entry(
  r,
  font = ("Verdana", 16),
).pack(padx=50, ipadx=10, ipady=10)

r.mainloop()