import tkinter as tk
from tkinter import *

r = tk.Tk()
r.geometry("350x400+400+300")
r.title("Word Jumble")
r.configure(background="#000000")

lb1 = Label(
  r,
  text = "U r here?",
  font = ("Verdana", 18),
  bg = "#000000",
  fg = "#ffffff",
)
lb1.pack()

e1 = Entry(
  r,
  font = ("Verdana", 16)

)
e1.pack()

btncheck = Button(
  r,
  text = "Check",
  font = ("Comic sans ms", 16),
  width = 16,
  bg = "#4C4B4B",
  fg = "#6ab04c",
  relief = GROOVE,
)
btncheck.pack()

r.mainloop()