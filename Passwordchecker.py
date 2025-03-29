import tkinter as tk
from tkinter import ttk, messagebox
import hashlib
import math
import random
import string

# Function to calculate entropy
def calculate_entropy(password):
    char_sets = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        string.punctuation
    ]
    
    pool_size = sum(any(c in charset for c in password) for charset in char_sets) * 26
    entropy = len(password) * math.log2(pool_size) if pool_size else 0
    return entropy

# Function to check password strength
def check_password():
    password = entry_password.get()
    if not password:
        messagebox.showwarning("Warning", "Please enter a password")
        return
    
    entropy = calculate_entropy(password)
    strength = "Weak"
    color = "red"
    
    if entropy > 60:
        strength = "Strong"
        color = "green"
    elif entropy > 40:
        strength = "Medium"
        color = "orange"
    
    label_result.config(text=f"Strength: {strength} (Entropy: {entropy:.2f})", foreground=color)

# Function to suggest a stronger password
def suggest_password():
    strong_pass = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, strong_pass)

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")
root.configure(bg="#2C2F33")

style = ttk.Style()
style.configure("TButton", font=("Arial", 12))
style.configure("TLabel", font=("Arial", 12), background="#2C2F33", foreground="white")

frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

label_title = ttk.Label(frame, text="Enter Password:")
label_title.pack()

entry_password = ttk.Entry(frame, width=30, show="*")
entry_password.pack(pady=5)

btn_check = ttk.Button(frame, text="Check Strength", command=check_password)
btn_check.pack(pady=5)

label_result = ttk.Label(frame, text="", font=("Arial", 12, "bold"))
label_result.pack(pady=5)

btn_suggest = ttk.Button(frame, text="Suggest Strong Password", command=suggest_password)
btn_suggest.pack(pady=5)

root.mainloop()
