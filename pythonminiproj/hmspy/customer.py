from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector 
import random
from tkinter import messagebox

class Cust_Win:
  def __init__(self, root):
    self.root=root
    self.root.title("HMS")
    self.root.geometry("1295x550+230+220")


    # variable
    self.var_ref=StringVar()
    x=random.randint(1000,9999)
    self.var_ref.set(x)

    self.var_cust_name=StringVar()
    self.var_address=StringVar()
    
    self.var_gender=StringVar()
    self.var_post=StringVar()
    
    self.var_mobile=StringVar()
    self.var_email=StringVar()
    
    self.var_nationality=StringVar()
    self.var_alt_address=StringVar()
    
    self.var_id_proof=StringVar()
    self.var_id_number=StringVar()

    # title
    lbl_title = Label(self.root, text="Add Customer Details", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
    lbl_title.place(x=0,y=0,width=1550,height=50)
#logo
    img2=Image.open(r"C:\Users\Rayyan\OneDrive\เอกสาร\pythonbasics\pythonminiproj\hmspy\image\img2.png") 
    img2 = img2.resize((100, 40), Image.LANCZOS)  # Resize it correctly

    self.photoimg2=ImageTk.PhotoImage(img2)

    lbimg=Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
    lbimg.place(x=0, y=0, width=100, height=40)

    #label
    labelframeleft=LabelFrame(self.root, bd=4, relief=RIDGE, text="Customer Details", font=("times new roman", 12, "bold"),padx=2 )
    labelframeleft.place(x=5,y=50, width=425, height=490)

    #lbls  and entries

      # cust_ref
    lbl_cust_ref=Label(labelframeleft,  text="Customer Reference, ",  font=("times new roman", 12, "bold"),padx=2, pady=6)
    lbl_cust_ref.grid(row=0,column=0, sticky=W)

    entry_ref=ttk.Entry(labelframeleft, textvariable=self.var_ref, width=22, font=("times new roman", 12, "bold"))
    entry_ref.grid(row=0,column=1)

    
      # cust_name
    cname=Label(labelframeleft, text="Customer Name ",  font=("times new roman", 12, "bold"),padx=2, pady=6)
    cname.grid(row=1,column=0, sticky=W)

    txtcname=ttk.Entry(labelframeleft, textvariable=self.var_cust_name, width=22, font=("arial", 12, "bold"))
    txtcname.grid(row=1,column=1)

    
      # cust_address
    lblmname=Label(labelframeleft, text="Address ",  font=("arial", 12, "bold"),padx=2, pady=6)
    lblmname.grid(row=2,column=0, sticky=W)

    txtmname=ttk.Entry(labelframeleft,textvariable=self.var_address, width=22, font=("arial", 12, "bold"))
    txtmname.grid(row=2,column=1)

    
      # gender combobox
    label_gender=Label(labelframeleft, text="Gender ",  font=("arial", 12, "bold"),padx=2, pady=6)
    label_gender.grid(row=3,column=0, sticky=W)
    combo_gender=ttk.Combobox(labelframeleft, textvariable=self.var_gender, font=("arial", 12, "bold"), width=20, state="readonly")
    combo_gender["value"]=("male", "female", "lgbtq")
    combo_gender.grid(row=3, column=1)

      # postcode
    lblPostCode=Label(labelframeleft, text="Post Code ",  font=("arial", 12, "bold"),padx=2, pady=6)
    lblPostCode.grid(row=4,column=0, sticky=W)
    txtPostCode=ttk.Entry(labelframeleft, textvariable=self.var_mobile, width=22, font=("times new roman", 12, "bold"))
    txtPostCode.grid(row=4,column=1)

      # mobilenumber
    lblMobile=Label(labelframeleft, text="Mobile ",  font=("arial", 12, "bold"),padx=2, pady=6)
    lblMobile.grid(row=5,column=0, sticky=W)

    txtMobile=ttk.Entry(labelframeleft, textvariable=self.var_post, width=22, font=("times new roman", 12, "bold"))
    txtMobile.grid(row=5,column=1)

      # email
    lblEmail=Label(labelframeleft, text="email",  font=("arial", 12, "bold"),padx=2, pady=6)
    lblEmail.grid(row=6,column=0, sticky=W)

    txtEmail=ttk.Entry(labelframeleft, width=22, textvariable=self.var_email, font=("times new roman", 12, "bold"))
    txtEmail.grid(row=6,column=1)

      # nationality combobox
    lblNationality=Label(labelframeleft, text="Nationality ",  font=("arial", 12, "bold"),padx=2, pady=6)
    lblNationality.grid(row=7,column=0, sticky=W)
    combo_nationality=ttk.Combobox(labelframeleft, textvariable=self.var_nationality, font=("arial", 12, "bold"), width=20, state="readonly")
    combo_nationality["value"]=("India", "Pakistan", "China", "SriLanka", "Burma", "Combodia", "Laos")
    combo_nationality.grid(row=7, column=1)

  

      # idproof combobox
    lblPostCode=Label(labelframeleft, text="ID Proof ",  font=("arial", 12, "bold"),padx=2, pady=6)
    lblPostCode.grid(row=8,column=0, sticky=W)
    combo_id=ttk.Combobox(labelframeleft, textvariable=self.var_id_proof, font=("arial", 12, "bold"), width=20, state="readonly")
    combo_id["value"]=("Driving Licence", "AAdhar CArd", "Passport")
    combo_id.grid(row=8, column=1)
      #id number
    lblIdProof=Label(labelframeleft, text="ID Number ",  font=("arial", 12, "bold"),padx=2, pady=6)
    lblIdProof.grid(row=9,column=0, sticky=W)
    txtIdNumber=ttk.Entry(labelframeleft, textvariable=self.var_id_number, width=22, font=("times new roman", 12, "bold"))
    txtIdNumber.grid(row=9,column=1)

      #alt address
    lblAddress=Label(labelframeleft, text="Alternate Address ",  font=("arial", 12, "bold"),padx=2, pady=6)
    lblAddress.grid(row=10,column=0, sticky=W)
    txtAddress=ttk.Entry(labelframeleft, width=22, textvariable=self.var_alt_address, font=("times new roman", 12, "bold"))
    txtAddress.grid(row=10,column=1)

    #btns
    btn_frame=Frame(labelframeleft, bd=2, relief=RIDGE)
    btn_frame.place(x=0,y=400,width=412,height=40)
    btnAdd = Button(btn_frame, text="ADD", command=self.add_data, font=("times new roman", 12, "bold"), bg="black", fg="gold" , width=8)
    btnAdd.grid(row=0,column=0, padx=1)
    btnUpdate = Button(btn_frame, text="Update", command=self.update_data, font=("times new roman", 12, "bold"), bg="black", fg="gold" , width=8)
    btnUpdate.grid(row=0,column=1, padx=1)
    btnDelete = Button(btn_frame, text="delete", command=self.delete_data, font=("times new roman", 12, "bold"), bg="black", fg="gold" , width=8)
    btnDelete.grid(row=0,column=2, padx=1)
    btnReset = Button(btn_frame, text="reset", font=("times new roman", 12, "bold"), bg="black", fg="gold" , width=8)
    btnReset.grid(row=0,column=3, padx=1)
    btnset = Button(btn_frame, text="set", font=("times new roman", 12, "bold"), bg="black", fg="gold" , width=8)
    btnset.grid(row=0,column=4, padx=1)
    

    # table frame
    Table_Frame=LabelFrame(self.root, bd=2, relief=RIDGE,text="View Details and search system", font=("arial", 12, "bold"))
    Table_Frame.place(x=435,y=50, width=860, height=490)

    lblSearchBy=Label(Table_Frame, font=("times new roman", 12, "bold"), text="Search by", bg="red", fg="white")
    lblSearchBy.grid(row=0,column=0,sticky=W)
    combo_search=ttk.Combobox(Table_Frame, font=("arial", 12, "bold"), width=15, state="readonly")
    combo_search["value"]=("Mobile", "Ref")
    combo_search.current(0)
    combo_search.grid(row=0, column=1)
    txtsearch=ttk.Entry(Table_Frame, width=22, font=("times new roman", 12, "bold"))
    txtsearch.grid(row=0,column=2, padx=2)
    btnsearch = Button(Table_Frame, text="Search", font=("times new roman", 12, "bold"), bg="black", fg="gold" , width=8)
    btnsearch.grid(row=0,column=3, padx=1)
    btnshowall = Button(Table_Frame, text="Showall", font=("times new roman", 12, "bold"), bg="black", fg="gold" , width=8)
    btnshowall.grid(row=0,column=4, padx=1)

    #show date table
    details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
    details_table.place(x=0,y=50,width=860,height=350)

    scroll_x=ttk.Scrollbar(details_table, orient=HORIZONTAL)
    scroll_y=Scrollbar(details_table,orient=VERTICAL)
    self.Cust_Details_Table=ttk.Treeview(details_table, column=("ref", "name", "address", "gender", "post", "mobile", "email", "nationality", "idproof", "idnumber", "altaddress"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=self.Cust_Details_Table.xview)
    scroll_y.config(command=self.Cust_Details_Table.yview)

    self.Cust_Details_Table.heading("ref", text="Refer No")
    self.Cust_Details_Table.heading("name", text="Name")
    self.Cust_Details_Table.heading("address", text="Adress")
    self.Cust_Details_Table.heading("gender", text="Gender")
    self.Cust_Details_Table.heading("post", text="PostCode")
    self.Cust_Details_Table.heading("mobile", text="Mobile")
    self.Cust_Details_Table.heading("email", text="Email")
    self.Cust_Details_Table.heading("nationality", text="Nationality")
    self.Cust_Details_Table.heading("idproof", text="Id Proof")
    self.Cust_Details_Table.heading("idnumber", text="Id NUmber")
    self.Cust_Details_Table.heading("altaddress", text="alternative addreess")
    self.Cust_Details_Table["show"]="headings"
    self.Cust_Details_Table.pack(fill=BOTH,expand=1)

  def add_data(self):
    if self.var_mobile.get()==""or self.var_address.get()=="":
        messagebox.showerror("error", "all fields are required", parent=self.root)
    else:
     try: 
        conn=mysql.connector.connect(host="localhost", username="root", password="writeurownpasswrd", database="hotel1")
        my_cursor=conn.cursor()
        my_cursor.execute("INSERT INTO customer (Ref, Name, Address, Gender, PostCode, Mobile, Email, Nationality, Idproof, Idnumber, Altaddress) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(
                                      self.var_ref.get(),   
                                      self.var_cust_name.get(),
                                      self.var_address.get(),
                                      
                                      self.var_gender.get(),
                                      self.var_post.get(),
                                      
                                      self.var_mobile.get(),
                                      self.var_email.get(),
                                      
                                      self.var_nationality.get(),
                                      self.var_alt_address.get(),
                                      
                                      self.var_id_proof.get(),
                                      self.var_id_number.get()

                                    ))
  
        conn.commit()
        conn.close()
        self.fetch_data()

        messagebox.showinfo("Success", "customer has been added", parent=self.root)
     except Exception as es:
       messagebox.showerror("warning", f" something went wrong:{str(es)}", parent=self.root)
  
  def update_data(self):
    if self.var_mobile.get() == "":
        messagebox.showerror("Error", "Please enter mobile number to update")
    else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="writeurownpasswrd", database="hotel1")
            my_cursor = conn.cursor()
            my_cursor.execute("""
                UPDATE customer SET 
                    Name=%s, Address=%s, Gender=%s, PostCode=%s, Email=%s, 
                    Nationality=%s, IDProof=%s, IDNumber=%s, AltAddress=%s 
                WHERE Ref=%s
            """, (
                self.var_cust_name.get(),
                self.var_address.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_alt_address.get(),
                self.var_ref.get()
            ))
            conn.commit()
            self.fetch_data()  # refresh table
            conn.close()
            self.fetch_data()

            messagebox.showinfo("Success", "Customer data has been updated successfully")
        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}")

  def delete_data(self):
      confirm = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer?")
      if confirm:
          try:
              conn = mysql.connector.connect(host="localhost", username="root", password="writeurownpasswrd", database="hotel1")
              my_cursor = conn.cursor()
              query = "DELETE FROM customer WHERE Ref=%s"
              value = (self.var_ref.get(),)
              my_cursor.execute(query, value)
              conn.commit()
              self.fetch_data()
              conn.close()
              self.fetch_data()

              messagebox.showinfo("Delete", "Customer record deleted successfully")
          except Exception as es:
              messagebox.showerror("Error", f"Error due to: {str(es)}")

  def fetch_data(self):
    conn = mysql.connector.connect(host="localhost", username="root", password="writeurownpasswrd", database="hotel1")
    my_cursor = conn.cursor()
    my_cursor.execute("SELECT * FROM customer")
    rows = my_cursor.fetchall()

    if len(rows) != 0:
        self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
        for row in rows:
            self.Cust_Details_Table.insert("", END, values=row)
        conn.commit()
    conn.close()
   






if __name__=="__main__":
  root=Tk()
  obj=Cust_Win(root)
  root.mainloop()

