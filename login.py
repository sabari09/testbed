import tkinter as tk
from tkinter import messagebox

# Predefined credentials
ROLLNO = "165120"
USERNAME = "admin"
PASSWORD = "Bubble@09"

# Toggle password visibility
def toggle_password():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# Login validation function
def login():
    entered_rollno = Rollno_entry.get()
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    
    if entered_rollno == ROLLNO and entered_username == USERNAME and entered_password == PASSWORD:
        messagebox.showinfo("Login Successful", "Welcome!")
    else:
        messagebox.showerror("Login Failed")
