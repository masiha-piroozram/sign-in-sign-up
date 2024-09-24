import hashlib
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

# Utility functions
def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def save_user(username, password_hash, phone_number):
    """Saves the username, hashed password, and phone number to a file."""
    with open('users.txt', 'a') as file:
        file.write(f"{username},{password_hash},{phone_number}\n")

def user_exists(username):
    """Checks if a username already exists in the file."""
    if not os.path.exists('users.txt'):
        return False
    with open('users.txt', 'r') as file:
        for line in file:
            stored_username, _, _ = line.strip().split(',')
            if stored_username == username:
                return True
    return False

def validate_user(username, password):
    """Validates a user's credentials."""
    if not os.path.exists('users.txt'):
        return False
    password_hash = hash_password(password)
    with open('users.txt', 'r') as file:
        for line in file:
            stored_username, stored_password_hash, _ = line.strip().split(',')
            if stored_username == username and stored_password_hash == password_hash:
                return True
    return False

def get_phone_number(username):
    """Retrieves the phone number for a given username."""
    if not os.path.exists('users.txt'):
        return None
    with open('users.txt', 'r') as file:
        for line in file:
            stored_username, _, phone_number = line.strip().split(',')
            if stored_username == username:
                return phone_number
    return None

def reset_password(username, phone_number, new_password):
    """Resets the user's password if the phone number matches."""
    if not os.path.exists('users.txt'):
        return "User not found."
    new_password_hash = hash_password(new_password)
    lines = []
    with open('users.txt', 'r') as file:
        for line in file:
            stored_username, stored_password_hash, stored_phone_number = line.strip().split(',')
            if stored_username == username and stored_phone_number == phone_number:
                lines.append(f"{username},{new_password_hash},{phone_number}\n")
            else:
                lines.append(line)
    with open('users.txt', 'w') as file:
        file.writelines(lines)
    return "Password reset successfully."

def sign_up(username, password, phone_number):
    """Handles user sign-up."""
    if user_exists(username):
        return "Username already exists. Please choose a different username."
    if len(password) < 6:
        return "Password must be at least 6 characters long."
    if not phone_number.startswith("09") or len(phone_number) != 11:
        return "Phone number must start with '09' and be 11 characters long."
    password_hash = hash_password(password)
    save_user(username, password_hash, phone_number)
    return "User signed up successfully."

def sign_in(username, password):
    """Handles user sign-in."""
    if not user_exists(username):
        return "You don't have an account. Please sign up first."
    if validate_user(username, password):
        return "Sign-in successful."
    return "Invalid username or password."

# GUI functions
def sign_up_gui():
    def validate_sign_up():
        username = username_entry.get()
        password = password_entry.get()
        phone_number = phone_number_entry.get()
        valid = True

        if user_exists(username):
            username_error.config(text="Username already exists.")
            valid = False
        else:
            username_error.config(text="")

        if len(password) < 6:
            password_error.config(text="Password must be at least 6 characters long.")
            valid = False
        else:
            password_error.config(text="")

        if not phone_number.startswith("09") or len(phone_number) != 11:
            phone_number_error.config(text="Phone number must start with '09' and be 11 characters long.")
            valid = False
        else:
            phone_number_error.config(text="")

        if valid:
            message = sign_up(username, password, phone_number)
            messagebox.showinfo("Sign Up", message)
            sign_up_window.destroy()

    sign_up_window = tk.Toplevel(root)
    sign_up_window.title("Sign Up")

    tk.Label(sign_up_window, text="Username:").grid(row=0, column=0, padx=10, pady=5)
    username_entry = tk.Entry(sign_up_window)
    username_entry.grid(row=0, column=1, padx=10, pady=5)
    username_error = tk.Label(sign_up_window, text="", fg="red")
    username_error.grid(row=0, column=2, padx=10, pady=5)

    tk.Label(sign_up_window, text="Password:").grid(row=1, column=0, padx=10, pady=5)
    password_entry = tk.Entry(sign_up_window, show='*')
    password_entry.grid(row=1, column=1, padx=10, pady=5)
    password_error = tk.Label(sign_up_window, text="", fg="red")
    password_error.grid(row=1, column=2, padx=10, pady=5)

    tk.Label(sign_up_window, text="Phone Number:").grid(row=2, column=0, padx=10, pady=5)
    phone_number_entry = tk.Entry(sign_up_window)
    phone_number_entry.grid(row=2, column=1, padx=10, pady=5)
    phone_number_error = tk.Label(sign_up_window, text="", fg="red")
    phone_number_error.grid(row=2, column=2, padx=10, pady=5)

    tk.Button(sign_up_window, text="Sign Up", command=validate_sign_up).grid(row=3, column=1, pady=10)

def sign_in_gui():
    def validate_sign_in():
        username = username_entry.get()
        password = password_entry.get()
        attempts = 0

        if not user_exists(username):
            messagebox.showerror("Sign In", "You don't have an account. Please sign up first.")
            sign_in_window.destroy()
            return

        while attempts < 3:
            message = sign_in(username, password)
            if message == "Sign-in successful.":
                messagebox.showinfo("Sign In", message)
                sign_in_window.destroy()
                return
            else:
                attempts += 1
                password = simpledialog.askstring("Sign In", f"Invalid password. Attempt {attempts}/3. Enter password again:", show='*')

        phone_number = simpledialog.askstring("Reset Password", "Enter phone number to reset password:")
        stored_phone_number = get_phone_number(username)
        if phone_number == stored_phone_number:
            new_password = simpledialog.askstring("Reset Password", "Enter new password:", show='*')
            message = reset_password(username, phone_number, new_password)
            messagebox.showinfo("Reset Password", message)
        else:
            messagebox.showerror("Reset Password", "Phone number does not match.")

    sign_in_window = tk.Toplevel(root)
    sign_in_window.title("Sign In")

    tk.Label(sign_in_window, text="Username:").grid(row=0, column=0, padx=10, pady=5)
    username_entry = tk.Entry(sign_in_window)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(sign_in_window, text="Password:").grid(row=1, column=0, padx=10, pady=5)
    password_entry = tk.Entry(sign_in_window, show='*')
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Button(sign_in_window, text="Sign In", command=validate_sign_in).grid(row=2, column=1, pady=10)

# Main GUI
root = tk.Tk()
root.title("Sign In/Sign Up System")

sign_up_button = tk.Button(root, text="Sign Up", command=sign_up_gui)
sign_up_button.pack(pady=10)

sign_in_button = tk.Button(root, text="Sign In", command=sign_in_gui)
sign_in_button.pack(pady=10)

root.mainloop()
