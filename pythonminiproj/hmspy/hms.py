import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Globals
mycon = None
cursor = None
userName = ""
password = ""
cid = ""

def connect_to_mysql():
    global mycon, cursor, userName, password

    userName = username_entry.get()
    password = password_entry.get()
    try:
        mycon = mysql.connector.connect(
            host="localhost", user=userName, passwd=password, auth_plugin='mysql_native_password'
        )
        cursor = mycon.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS HMS")
        cursor.execute("COMMIT")
        messagebox.showinfo("Success", "MySQL connection established!")
        show_main_menu()
    except Exception as e:
        messagebox.showerror("Connection Error", str(e))

def connect_to_db():
    global mycon, cursor
    try:
        mycon = mysql.connector.connect(
            host="localhost", user=userName, passwd=password, database="HMS", auth_plugin='mysql_native_password'
        )
        cursor = mycon.cursor()
    except:
        messagebox.showerror("Error", "Couldn't connect to HMS database!")

def guest_details_gui():
    connect_to_db()

    def save_guest():
        global cid
        cid = cid_entry.get()
        name = name_entry.get()
        address = address_entry.get()
        age = age_entry.get()
        nationality = country_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()

        create_table = """CREATE TABLE IF NOT EXISTS C_DETAILS(
            CID VARCHAR(20), C_NAME VARCHAR(30), C_ADDRESS VARCHAR(30),
            C_AGE VARCHAR(30), C_COUNTRY VARCHAR(30), P_NO VARCHAR(30),
            C_EMAIL VARCHAR(30))"""
        cursor.execute(create_table)
        sql = "INSERT INTO C_DETAILS VALUES(%s,%s,%s,%s,%s,%s,%s)"
        values = (cid, name, address, age, nationality, phone, email)
        cursor.execute(sql, values)
        cursor.execute("COMMIT")
        messagebox.showinfo("Saved", "Guest registered successfully!")
        guest_window.destroy()

    guest_window = tk.Toplevel(root)
    guest_window.title("Guest Details")

    labels = ["Guest ID", "Name", "Address", "Age", "Country", "Phone", "Email"]
    entries = []

    for i, label in enumerate(labels):
        tk.Label(guest_window, text=label).grid(row=i, column=0, padx=10, pady=5)
    cid_entry = tk.Entry(guest_window)
    name_entry = tk.Entry(guest_window)
    address_entry = tk.Entry(guest_window)
    age_entry = tk.Entry(guest_window)
    country_entry = tk.Entry(guest_window)
    phone_entry = tk.Entry(guest_window)
    email_entry = tk.Entry(guest_window)

    cid_entry.grid(row=0, column=1)
    name_entry.grid(row=1, column=1)
    address_entry.grid(row=2, column=1)
    age_entry.grid(row=3, column=1)
    country_entry.grid(row=4, column=1)
    phone_entry.grid(row=5, column=1)
    email_entry.grid(row=6, column=1)

    tk.Button(guest_window, text="Submit", command=save_guest).grid(row=7, column=0, columnspan=2, pady=10)

def show_main_menu():
    login_frame.pack_forget()
    main_menu_frame.pack(padx=20, pady=20)

# --- GUI Start ---
root = tk.Tk()
root.title("Hotel Management System")

# Login Frame
login_frame = tk.Frame(root)
login_frame.pack(padx=20, pady=20)

tk.Label(login_frame, text="Enter MySQL Username:").grid(row=0, column=0, pady=5)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1, pady=5)

tk.Label(login_frame, text="Enter MySQL Password:").grid(row=1, column=0, pady=5)
password_entry = tk.Entry(login_frame, show='*')
password_entry.grid(row=1, column=1, pady=5)

tk.Button(login_frame, text="Connect to MySQL", command=connect_to_mysql).grid(row=2, column=0, columnspan=2, pady=10)

# Main Menu Frame
main_menu_frame = tk.Frame(root)

tk.Label(main_menu_frame, text="Main Menu", font=("Arial", 16)).pack(pady=10)

tk.Button(main_menu_frame, text="1. Enter Guest Details", command=guest_details_gui, width=30).pack(pady=5)
tk.Button(main_menu_frame, text="Exit", command=root.destroy, width=30).pack(pady=5)

root.mainloop()
