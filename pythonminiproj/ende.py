import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import base64  
import mysql.connector



# RAIL FENCE CIPHER
def rail_fence_encrypt(text, key):
    key = int(key)
    rail = ['' for _ in range(key)]
    direction = False
    row = 0
    for char in text:
        rail[row] += char
        if row == 0 or row == key - 1:
            direction = not direction
        row += 1 if direction else -1
    return ''.join(rail)

def rail_fence_decrypt(text, key):
    key = int(key)
    pattern = [0] * len(text)
    direction = False
    row = 0
    for i in range(len(text)):
        pattern[i] = row
        if row == 0 or row == key - 1:
            direction = not direction
        row += 1 if direction else -1

    rail = ['' for _ in range(key)]
    pos = [0] * key
    for i in range(key):
        pos[i] = pattern.count(i)

    idx = 0
    for r in range(key):
        for i in range(len(pattern)):
            if pattern[i] == r and pos[r] > 0:
                rail[r] += text[idx]
                idx += 1
                pos[r] -= 1

    result = ''
    count = [0] * key
    for i in pattern:
        result += rail[i][count[i]]
        count[i] += 1
    return result


# SIMPLE XOR CIPHER
def xor_encrypt(text, key):
    key = int(key)
    return ''.join(chr(ord(c) ^ key) for c in text)

def xor_decrypt(text, key):
    return xor_encrypt(text, key)  # symmetric


# COLUMNAR TRANSPOSITION CIPHER
def columnar_encrypt(text, key):
    key = key.upper()
    columns = ['' for _ in key]
    for i, char in enumerate(text):
        columns[i % len(key)] += char
    sorted_key = sorted(list(key))
    result = ''
    for char in sorted_key:
        idx = key.index(char)
        result += columns[idx]
    return result

def columnar_decrypt(cipher, key):
    key = key.upper()
    n = len(cipher)
    cols = len(key)
    rows = n // cols + (n % cols > 0)
    total_slots = rows * cols
    padding = total_slots - n

    sorted_key = sorted([(char, i) for i, char in enumerate(key)])
    col_lengths = [rows] * cols
    for i in range(padding):
        col_lengths[sorted_key[-(i+1)][1]] -= 1

    idx = 0
    columns = [''] * cols
    for char, i in sorted_key:
        l = col_lengths[i]
        columns[i] = cipher[idx:idx+l]
        idx += l

    result = ''
    for r in range(rows):
        for c in range(cols):
            if r < len(columns[c]):
                result += columns[c][r]
    return result

# AFFINE CIPHER
def affine_encrypt(text, key):
    a, b = map(int, key.split(','))
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr(((a * (ord(char) - base) + b) % 26) + base)
        else:
            result += char
    return result

def affine_decrypt(text, key):
    a, b = map(int, key.split(','))
    result = ''
    m = 26
    # Modular inverse of a
    for i in range(1, m):
        if (a * i) % m == 1:
            a_inv = i
            break
    else:
        raise ValueError("No modular inverse for a.")
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr(((a_inv * ((ord(char) - base - b)) % 26) + base))
        else:
            result += char
    return result

def atbash_cipher(text):
    result = ''
    for char in text:
        if char.isupper():
            result += chr(90 - (ord(char) - 65))
        elif char.islower():
            result += chr(122 - (ord(char) - 97))
        else:
            result += char
    return result  # same for encrypt/decrypt

def rot13_cipher(text):
    result = ''
    for char in text:
        if char.isalpha():
            shift = 13
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result  # same for encrypt/decrypt

def base64_encrypt(text, key=None):  # key not needed
    return base64.b64encode(text.encode()).decode()

def base64_decrypt(text, key=None):
    return base64.b64decode(text.encode()).decode()

def binary_encrypt(text, key=None):
    return ' '.join(format(ord(c), '08b') for c in text)

def binary_decrypt(text, key=None):
    return ''.join(chr(int(b, 2)) for b in text.split())

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/'
}
REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def morse_encrypt(text, key=None):
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)

def morse_decrypt(text, key=None):
    return ''.join(REVERSE_MORSE_CODE_DICT.get(code, '') for code in text.split())


def caesar_encrypt(text, key):
    result = ""
    key = int(key) % 26
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -int(key))

def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            k = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(char) - shift + k) % 26 + shift)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            k = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(char) - shift - k) % 26 + shift)
            key_index += 1
        else:
            result += char
    return result

def store_to_mysql(original, encrypted, cipher, key):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",         # ⚠️ 
            password="writeurownpasswrd",         # ⚠️ 
            database="encrypter_app"
        )
        cursor = connection.cursor()
        query = "INSERT INTO encrypted_data (original_text, encrypted_text, cipher_type, key_used) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (original, encrypted, cipher, key))
        connection.commit()
        connection.close()
        messagebox.showinfo("Success", "Encrypted data stored in MySQL!")
    except Exception as e:
        messagebox.showerror("Error", f"MySQL Error:\n{e}")

def retrieve_and_decrypt():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",         # ⚠️ use your MySQL credentials
            password="writeurownpasswrd",
            database="encrypter_app"
        )
        cursor = connection.cursor()
        cursor.execute("SELECT id, encrypted_text, cipher_type, key_used FROM encrypted_data")
        records = cursor.fetchall()
        connection.close()

        if not records:
            messagebox.showinfo("Empty", "No records found in database.")
            return

        # Show options to user
        select_window = tk.Toplevel(root)
        select_window.title("Select Encrypted Data")

        listbox = tk.Listbox(select_window, width=80)
        for rec in records:
            listbox.insert(tk.END, f"ID {rec[0]} | Cipher: {rec[2]} | Key: {rec[3]} | Encrypted: {rec[1]}")
        listbox.pack()

        def on_select():
            index = listbox.curselection()
            if not index:
                return
            rec = records[index[0]]
            cipher = rec[2]
            enc_text = rec[1]
            key = rec[3]

            # Set dropdown & key in UI
            cipher_dropdown.set(cipher)
            key_entry.delete(0, tk.END)
            key_entry.insert(0, key)
            text_input.delete("1.0", tk.END)

            text_input.insert("1.0", enc_text)

            select_window.destroy()

        tk.Button(select_window, text="Load", command=on_select).pack(pady=5)

    except Exception as e:
        messagebox.showerror("Error", f"MySQL Fetch Error:\n{e}")


# Encryption button logic
def encrypt():
    text = text_input.get("1.0", tk.END).strip()
    cipher = cipher_dropdown.get()
    key = key_entry.get().strip()
    
    try:
        if cipher == "Caesar Cipher":
            if not key.isdigit():
                messagebox.showerror("Error", "Key must be a number for Caesar Cipher.")
                return
            result = caesar_encrypt(text, key)

        elif cipher == "Vigenère Cipher":
            if not key.isalpha():
                messagebox.showerror("Error", "Key must be a word for Vigenère Cipher.")
                return
            result = vigenere_encrypt(text, key)
        elif cipher == "Atbash Cipher":
            result = atbash_cipher(text)
        elif cipher == "ROT13":
            result = rot13_cipher(text)
        elif cipher == "Base64":
            result = base64_encrypt(text)
        elif cipher == "Binary":
            result = binary_encrypt(text)
        elif cipher == "Morse Code":
            result = morse_encrypt(text)
        elif cipher == "Rail Fence":
            result = rail_fence_encrypt(text, key)
        elif cipher == "XOR Cipher":
            result = xor_encrypt(text, key)
        elif cipher == "Columnar Transposition":
            result = columnar_encrypt(text, key)
        elif cipher == "Affine Cipher":
            result = affine_encrypt(text, key)


        else:
            result = f"Encryption for '{cipher}' not added yet."

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)

    except Exception as e:
        messagebox.showerror("Encryption Error", str(e))


# Decryption button logic
def decrypt():
    text = text_input.get("1.0", tk.END).strip()
    cipher = cipher_dropdown.get()
    key = key_entry.get().strip()

    try:
        if cipher == "Caesar Cipher":
            if not key.isdigit():
                messagebox.showerror("Error", "Key must be a number for Caesar Cipher.")
                return
            result = caesar_decrypt(text, key)

        elif cipher == "Vigenère Cipher":
            if not key.isalpha():
                messagebox.showerror("Error", "Key must be a word for Vigenère Cipher.")
                return
            result = vigenere_decrypt(text, key)
        elif cipher == "Atbash Cipher":
            result = atbash_cipher(text)
        elif cipher == "ROT13":
            result = rot13_cipher(text)
        elif cipher == "Base64":
            result = base64_decrypt(text)
        elif cipher == "Binary":
            result = binary_decrypt(text)
        elif cipher == "Morse Code":
            result = morse_decrypt(text)
        elif cipher == "Rail Fence":
            result = rail_fence_decrypt(text, key)
        elif cipher == "XOR Cipher":
            result = xor_decrypt(text, key)
        elif cipher == "Columnar Transposition":
            result = columnar_decrypt(text, key)
        elif cipher == "Affine Cipher":
            result = affine_decrypt(text, key)

        else:
            result = f"Decryption for '{cipher}' not added yet."

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)

    except Exception as e:
        messagebox.showerror("Decryption Error", str(e))




# Create main app window
root = tk.Tk()
root.title("Encryption-Decryption App")
root.geometry("700x500")
root.configure(bg="#1e1e2e")

store_btn = tk.Button(
    root,
    text="Store to MySQL",
    command=lambda: store_to_mysql(
        text_input.get("1.0", tk.END).strip(),
        output_box.get("1.0", tk.END).strip(),  # ✅ Fixed here
        cipher_dropdown.get(),
        key_entry.get()
    )
)

store_btn.pack(pady=5)
retrieve_btn = tk.Button(root, text="Retrieve from MySQL", command=retrieve_and_decrypt)
retrieve_btn.pack(pady=5)

# Title
title = tk.Label(root, text="🔐 Cipher Vault", font=("Helvetica", 20, "bold"), bg="#1e1e2e", fg="#f8f8f2")
title.pack(pady=10)

# Input Frame
frame = tk.Frame(root, bg="#1e1e2e")
frame.pack(pady=10)

# Input text
tk.Label(frame, text="Enter Text:", font=("Helvetica", 12), bg="#1e1e2e", fg="#f8f8f2").grid(row=0, column=0, sticky="w")
text_input = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=60, height=4, font=("Courier", 10))
text_input.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

# Cipher Type
tk.Label(frame, text="Cipher Type:", font=("Helvetica", 12), bg="#1e1e2e", fg="#f8f8f2").grid(row=2, column=0, sticky="w")
cipher_options = [
    "Caesar Cipher", "Vigenère Cipher", "Atbash Cipher", "ROT13",
    "Affine Cipher", "Rail Fence Cipher", "Columnar Transposition", "Playfair Cipher", "XOR Cipher","Hill Cipher",
    "Base64", "Morse Code", "Binary", "RSA (demo)", "AES (demo)"
]      
    
    
  
    
cipher_dropdown = ttk.Combobox(frame, values=cipher_options, state="readonly", width=25)
cipher_dropdown.set("Caesar Cipher")
cipher_dropdown.grid(row=2, column=1, padx=5, pady=5)

# Key
tk.Label(frame, text="Key:", font=("Helvetica", 12), bg="#1e1e2e", fg="#f8f8f2").grid(row=3, column=0, sticky="w")
key_entry = tk.Entry(frame, font=("Courier", 12), width=30)
key_entry.grid(row=3, column=1, padx=5, pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#1e1e2e")
btn_frame.pack(pady=10)

encrypt_btn = tk.Button(btn_frame, text="Encrypt", width=15, bg="#50fa7b", fg="black")
encrypt_btn.config(command=encrypt)
encrypt_btn.grid(row=0, column=0, padx=10)

decrypt_btn = tk.Button(btn_frame, text="Decrypt", width=15, bg="#ffb86c", fg="black")
decrypt_btn.config(command=decrypt)
decrypt_btn.grid(row=0, column=1, padx=10)





save_btn = tk.Button(btn_frame, text="Save to MySQL", width=15, bg="#8be9fd", fg="black")
save_btn.grid(row=1, column=0, padx=10, pady=5)

retrieve_btn = tk.Button(btn_frame, text="Retrieve from MySQL", width=20, bg="#bd93f9", fg="black")
retrieve_btn.grid(row=1, column=1, padx=10, pady=5)

# Output Box
tk.Label(root, text="Output:", font=("Helvetica", 12), bg="#1e1e2e", fg="#f8f8f2").pack()
output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=6, font=("Courier", 10))
output_box.pack(pady=10)



root.mainloop()
