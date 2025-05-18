import re
import tkinter as tk
from tkinter import ttk, messagebox

def check_password_strength(password):
    strength = 0
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[0-9]", password): 
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): 
        strength += 1
    if len(password) >= 10:
        strength += 1
    return strength

def check_strength():
    password = password_entry.get()
    strength = check_password_strength(password)
    percentage = (strength / 5) * 100

    progress_bar['value'] = percentage
    percent_label.config(text=f"{percentage:.0f}%")

    lowercase_label.config(fg=success_color if re.search(r"[a-z]", password) else error_color)
    uppercase_label.config(fg=success_color if re.search(r"[A-Z]", password) else error_color)
    number_label.config(fg=success_color if re.search(r"[0-9]", password) else error_color)
    symbol_label.config(fg=success_color if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) else error_color)
    length_label.config(fg=success_color if len(password) >= 10 else error_color)

    if strength == 5:
        result_label.config(text="Very Strong Password", fg=success_color)
    elif strength == 4:
        result_label.config(text="Strong Password", fg=success_color)
    elif strength == 3:
        result_label.config(text="Moderate Password", fg="orange")
    elif strength == 2:
        result_label.config(text="Weak Password", fg=error_color)
        messagebox.showwarning("Weak Password", "Your password is weak! Try adding uppercase letters, numbers, or special characters.")
    else:
        result_label.config(text="Very Weak Password", fg=error_color)
        messagebox.showwarning("Very Weak Password", "Your password is very weak! Make it much stronger.")

def toggle_password_visibility():
    global show_password
    if show_password:
        password_entry.config(show="*")
        toggle_button.config(text="Show Password")
        show_password = False
    else:
        password_entry.config(show="")
        toggle_button.config(text="Hide Password")
        show_password = True

def clear_fields():
    password_entry.delete(0, tk.END)
    progress_bar['value'] = 0
    percent_label.config(text="0%")
    result_label.config(text="Password strength will appear here.", fg=text_color)
    lowercase_label.config(fg=text_color)
    uppercase_label.config(fg=text_color)
    number_label.config(fg=text_color)
    symbol_label.config(fg=text_color)
    length_label.config(fg=text_color)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("600x750")
root.resizable(False, False)
root.configure(bg="linen")  

show_password = False

bg_color = "linen"           
button_color = "bisque"       
hover_color = "wheat"        
text_color = "saddlebrown"    
success_color = "green"       
error_color = "red"           


title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 20, "bold"), bg=bg_color, fg=text_color)
title_label.pack(pady=20)


password_entry = tk.Entry(root, show="*", font=("Arial", 14), width=30, bg="white", fg=text_color, insertbackground=text_color, relief="flat")
password_entry.pack(pady=10)

toggle_button = tk.Button(root, text="Show Password", command=toggle_password_visibility, bg=button_color, fg=text_color, relief="flat")
toggle_button.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=check_strength, bg=button_color, fg=text_color, relief="flat")
check_button.pack(pady=20)

clear_button = tk.Button(root, text="Clear", command=clear_fields, bg=button_color, fg=text_color, relief="flat")
clear_button.pack(pady=5)

result_label = tk.Label(root, text="Password strength will appear here.", font=("Arial", 14), bg=bg_color, fg=text_color)
result_label.pack(pady=10)

style = ttk.Style()
style.theme_use('clam')
style.configure("TProgressbar", thickness=20, troughcolor=button_color, background=success_color, bordercolor=button_color)
progress_bar = ttk.Progressbar(root, length=300, mode='determinate', style="TProgressbar")
progress_bar.pack(pady=10)

percent_label = tk.Label(root, text="0%", font=("Arial", 12), bg=bg_color, fg=text_color)
percent_label.pack()

conditions_label = tk.Label(root, text="Password must include:", font=("Arial", 12, "underline"), bg=bg_color, fg=text_color)
conditions_label.pack(pady=10)

lowercase_label = tk.Label(root, text="• At least one lowercase letter", font=("Arial", 11), bg=bg_color, fg=text_color)
lowercase_label.pack()

uppercase_label = tk.Label(root, text="• At least one uppercase letter", font=("Arial", 11), bg=bg_color, fg=text_color)
uppercase_label.pack()

number_label = tk.Label(root, text="• At least one number", font=("Arial", 11), bg=bg_color, fg=text_color)
number_label.pack()

symbol_label = tk.Label(root, text="• At least one special character", font=("Arial", 11), bg=bg_color, fg=text_color)
symbol_label.pack()

length_label = tk.Label(root, text="• At least 10 characters", font=("Arial", 11), bg=bg_color, fg=text_color)
length_label.pack()

root.mainloop()

