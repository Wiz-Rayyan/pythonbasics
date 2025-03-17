import tkinter as tk
from tkinter import *

r = tk.Tk()
r.geometry("400x505")

b4 = Button(r, text="b4", width=15, height=2) 
b4.pack(expand= True, fill=BOTH)

b5 = Button(r, text="b5", width=15, height=2) 
b5.pack(side = LEFT)

r.mainloop()

#grid vs place vs pack. gid and pack cant b used together