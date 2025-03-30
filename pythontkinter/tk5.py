# initial proj: word anagram. more similar word games be added: guess the jumbled word, guess the missing letter, tell opposite, then mcq quiz to tell nonsynonyms, 


import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

words = [
    "listen",
    "earth",
    "save",
    "angel",
    "debit",
    "stressed",
    "cider",
    "lapse",
    "dusty",
    "fried",
    "silent",
    "enlist",
    "stone",
    "night",
    "spare",
    "meat",
    "act",
    "loop",
    "slate",
    "flow",
]

answers = [
    "silent",
    "heart",
    "vase",
    "glean",
    "bited",
    "desserts",
    "cried",
    "peals",
    "study",
    "fired",
    "listen",
    "tinsel",
    "tones",
    "thing",
    "pears",
    "team",
    "cat",
    "polo",
    "stale",
    "wolf",
]


num = random.randrange(0, 20, 1)

def res():
  global words,answers, num
  num = random.randrange(0, 20, 1)
  lb1.config(text=words[num])
  e1.delete(0, END)


def default():
  global words,answers, num
  lb1.config(text=words[num])

def checkanswer():
  global words, answers, num
  var = e1.get()
  if var == answers[num]:
    messagebox.showinfo("Correct", "this is anagram for it")
    res()
  else:
    messagebox.showerror("error", "not n anagram")
    e1.delete(0, END)

r = tk.Tk()
r.geometry("350x400+400+300")
r.title("Word Anagram")
r.configure(background="#000000")

lb1 = Label(
  r,
  text = "U r here?",
  font = ("Verdana", 18),
  bg = "#000000",
  fg = "#ffffff",
)
lb1.pack(pady=30, ipady=10, ipadx=10)


ans = StringVar()


e1 = Entry(
  r,
  font = ("Verdana", 16),
  textvariable = ans, 

)
e1.pack(ipadx=5,ipady=5)

btncheck = Button(
  r,
  text = "Check",
  font = ("Comic sans ms", 16),
  width = 16,
  bg = "#4C4B4B",
  fg = "#6ab04c",
  relief = GROOVE,
  command = checkanswer, 
)
btncheck.pack(pady=40)

btnreset = Button(
  r,
  text = "Reset",
  font = ("Comic sans ms", 16),
  width = 16,
  bg = "#4C4B4B",
  fg = "#EA425C",
  command = res,
)
btnreset.pack(pady=50)

default()

r.mainloop()