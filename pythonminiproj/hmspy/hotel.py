from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win

class HMS:
    def __init__(self, root):
        self.root=root
        self.root.title("HMS")
        self.root.geometry("1550x800+0+0")
    # header
        img1=Image.open(r"C:\Users\Rayyan\OneDrive\เอกสาร\pythonbasics\pythonminiproj\hmspy\image\img1.png") 
        img1 = img1.resize((1500,340))
        self.photoimg1=ImageTk.PhotoImage(img1)

        lbimg=Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lbimg.place(x=0, y=0, width=1550, height=240)
    # logo
        img2=Image.open(r"C:\Users\Rayyan\OneDrive\เอกสาร\pythonbasics\pythonminiproj\hmspy\image\img2.png") 
        img2 = img2.resize((230, 340), Image.LANCZOS)  # Resize it correctly

        self.photoimg2=ImageTk.PhotoImage(img2)

        lbimg=Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbimg.place(x=0, y=0, width=230, height=240)

        # title
        lbl_title = Label(self.root, text="Hotel Management System", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=240,width=1550,height=50)

        main_frame=Frame(self.root,  bd=4, relief=RIDGE)
        main_frame.place(x=0,y=290,width=1550,height=620)
        
        #menu
        lbl_title = Label(main_frame, text="Menu", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=0, width=230, height=50)

        
        btn_frame=Frame(main_frame,  bd=4, relief=RIDGE)
        btn_frame.place(x=0,y=52, width=228,height=190)

        cust_btn=Button(btn_frame, text="CUSTOMER",command=self.cust_details,width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)

            
        # ROOM Button
        room_btn = Button(btn_frame, text="ROOM", width=22, font=("times new roman", 14, "bold"),
                        bg="black", fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        # DETAILS Button
        details_btn = Button(btn_frame, text="DETAILS", width=22, font=("times new roman", 14, "bold"),
                            bg="black", fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        # REPORT Button
        report_btn = Button(btn_frame, text="REPORT", width=22, font=("times new roman", 14, "bold"),
                            bg="black", fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        # LOGOUT Button
        logout_btn = Button(btn_frame, text="LOGOUT", width=22, font=("times new roman", 14, "bold"),
                            bg="black", fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=1)
    # hotelimage
        img3=Image.open(r"C:\Users\Rayyan\OneDrive\เอกสาร\pythonbasics\pythonminiproj\hmspy\image\img3.png") 
        img3 = img3.resize((1310,590))
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbimg=Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lbimg.place(x=225, y=0, width=1310, height=490)


        img4=Image.open(r"C:\Users\Rayyan\OneDrive\เอกสาร\pythonbasics\pythonminiproj\hmspy\image\img4.png") 
        img4 = img4.resize((230,190))
        self.photoimg4=ImageTk.PhotoImage(img4)

        lbimg1=Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lbimg1.place(x=0, y=250, width=230, height=230)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

        


    

if __name__ == "__main__":
  root = Tk()
  obj = HMS(root)
  root.mainloop()