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
def check_password(event=None):  # Added `event=None` to handle key binding
    password = entry_password.get()
    if not password:
        messagebox.showwarning("Warning", "Please enter a password")
        return
    
    entropy = calculate_entropy(password)
    strength = "Weak"
    color = "red"
    progress = 33  # Default progress for weak passwords
    
    if entropy > 60:
        strength = "Strong"
        color = "green"
        progress = 100
    elif entropy > 40:
        strength = "Medium"
        color = "orange"
        progress = 66
    
    label_result.config(text=f"Strength: {strength} (Entropy: {entropy:.2f})", foreground=color)
    progress_bar["value"] = progress

# Function to suggest a stronger password
def suggest_password():
    strong_pass = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, strong_pass)

# Function to toggle password visibility
def toggle_password():
    if entry_password.cget("show") == "":
        entry_password.config(show="*")
        btn_toggle_password.config(text="Show Password")
    else:
        entry_password.config(show="")
        btn_toggle_password.config(text="Hide Password")

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.configure(bg="#2C2F33")  # Set background color

# Apply styles
style = ttk.Style()
style.configure("TButton", font=("Arial", 12))  # Adjust font size for buttons
style.configure("TLabel", font=("Arial", 12), background="#2C2F33", foreground="white")  # Adjust font size for labels
style.configure("TProgressbar", thickness=20)  # Adjust progress bar thickness

# Create a frame for the widgets
frame = ttk.Frame(root, padding=20)
frame.place(relx=0.5, rely=0.5, anchor="center")  # Center the frame

label_title = ttk.Label(frame, text="Enter Password:")
label_title.pack()

entry_password = ttk.Entry(frame, width=30, show="*")  # Password is hidden by default
entry_password.pack(pady=5)

btn_toggle_password = ttk.Button(frame, text="Show Password", command=toggle_password)
btn_toggle_password.pack(pady=5)

btn_check = ttk.Button(frame, text="Check Strength", command=check_password)
btn_check.pack(pady=5)

label_result = ttk.Label(frame, text="", font=("Arial", 12, "bold"))  # Adjust font size for result
label_result.pack(pady=5)

progress_bar = ttk.Progressbar(frame, orient="horizontal", length=200, mode="determinate")
progress_bar.pack(pady=5)

btn_suggest = ttk.Button(frame, text="Suggest Strong Password", command=suggest_password)
btn_suggest.pack(pady=5)

# Bind the Enter key to the check_password function
root.bind("<Return>", check_password)

root.mainloop()
