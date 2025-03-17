import tkinter as tk
r = tk.Tk() # variable used. object created? is it instance or something? yes. tk.Tk() is a constructor that initializes the main window. r is now a reference to this window object.

r.title("login page")
# { widgets}
# r.geometry("400x500")

ws = r.winfo_screenwidth()
hs = r.winfo_screenheight()

myw = 800
myh = 400

x = int(ws/2 - myw/2)
y = int(hs/2 - myh/2)

d1 = str(myw)+"x"+str(myh)+"+"+str(x)+"+"+str(y)
r.geometry(d1)

r.configure(background="#000000")


r.mainloop() # window appears. any other reason? and how window appears: . starts Tkinter’s event loop It listens for events (e.g., keypresses, mouse clicks, window closing). Without mainloop(), the window will open and immediately close because Python would finish execution.