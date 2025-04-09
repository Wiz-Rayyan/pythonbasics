from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Hotel Management System")
root.geometry("800x600")
root.configure(bg="lightblue")

# Data storage
booking_details = {}
room_rent = 0
restaurant_bill = 0

def view_available_rooms():
    messagebox.showinfo("Available Rooms", "Rooms Available:\n1. Deluxe Room - ₹2000/night\n2. Executive Room - ₹3000/night\n3. Suite - ₹5000/night")

def enter_booking_details():
    def save_details():
        booking_details['name'] = name_entry.get()
        booking_details['phone'] = phone_entry.get()
        booking_details['room_type'] = room_type_var.get()
        booking_details['nights'] = int(nights_entry.get())
        details_window.destroy()
        messagebox.showinfo("Saved", "Booking details saved successfully!")

    details_window = Toplevel(root)
    details_window.title("Booking Details")
    details_window.geometry("400x300")

    Label(details_window, text="Name:").pack()
    name_entry = Entry(details_window)
    name_entry.pack()

    Label(details_window, text="Phone:").pack()
    phone_entry = Entry(details_window)
    phone_entry.pack()

    Label(details_window, text="Room Type:").pack()
    room_type_var = StringVar(details_window)
    room_type_var.set("Deluxe")
    OptionMenu(details_window, room_type_var, "Deluxe", "Executive", "Suite").pack()

    Label(details_window, text="Number of Nights:").pack()
    nights_entry = Entry(details_window)
    nights_entry.pack()

    Button(details_window, text="Save", command=save_details).pack(pady=10)

def calculate_room_rent():
    global room_rent
    if not booking_details:
        messagebox.showwarning("Missing Info", "Please enter booking details first.")
        return

    rate = {"Deluxe": 2000, "Executive": 3000, "Suite": 5000}
    room_type = booking_details['room_type']
    nights = booking_details['nights']
    room_rent = rate[room_type] * nights
    messagebox.showinfo("Room Rent", f"Room Rent for {nights} nights in {room_type}: ₹{room_rent}")

def calculate_restaurant_bill():
    def save_bill():
        global restaurant_bill
        total = 0
        total += int(breakfast_entry.get()) * 150
        total += int(lunch_entry.get()) * 300
        total += int(dinner_entry.get()) * 250
        restaurant_bill = total
        food_window.destroy()
        messagebox.showinfo("Restaurant Bill", f"Total Restaurant Bill: ₹{restaurant_bill}")

    food_window = Toplevel(root)
    food_window.title("Restaurant Bill")
    food_window.geometry("300x250")

    Label(food_window, text="Breakfast (₹150):").pack()
    breakfast_entry = Entry(food_window)
    breakfast_entry.pack()

    Label(food_window, text="Lunch (₹300):").pack()
    lunch_entry = Entry(food_window)
    lunch_entry.pack()

    Label(food_window, text="Dinner (₹250):").pack()
    dinner_entry = Entry(food_window)
    dinner_entry.pack()

    Button(food_window, text="Calculate", command=save_bill).pack(pady=10)

def display_guest_details():
    if not booking_details:
        messagebox.showwarning("Missing Info", "No booking details available.")
    else:
        details = f"Name: {booking_details['name']}\nPhone: {booking_details['phone']}\nRoom: {booking_details['room_type']}\nNights: {booking_details['nights']}"
        messagebox.showinfo("Guest Details", details)

def generate_total_bill():
    if not booking_details:
        messagebox.showwarning("Missing Info", "No booking details available.")
        return
    total = room_rent + restaurant_bill
    messagebox.showinfo("Total Bill", f"Room Rent: ₹{room_rent}\nRestaurant: ₹{restaurant_bill}\nTotal: ₹{total}")

def finish_and_exit():
    confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if confirm:
        root.destroy()

# Title
Label(root, text="Hotel Management System", font=("Arial", 24, "bold"), bg="lightblue", fg="navy").pack(pady=20)

# Options Frame
options_frame = Frame(root, bg="lightblue")
options_frame.pack(pady=10)

options = [
    ("1 | View Available Rooms", view_available_rooms),
    ("2 | Enter Booking Details", enter_booking_details),
    ("3 | Calculate Room Rent", calculate_room_rent),
    ("4 | Calculate Restaurant Bill", calculate_restaurant_bill),
    ("5 | Display Guest Details", display_guest_details),
    ("6 | Generate Total Bill Amount", generate_total_bill),
    ("7 | Finish Up and Exit", finish_and_exit)
]

for text, func in options:
    Button(options_frame, text=text, font=("Arial", 14), width=40, pady=10, command=func).pack(pady=5)

root.mainloop()
