import subprocess
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def redirect_to_home(script_path):
    subprocess.run(['python', script_path])

# Main window
root = tk.Tk()
root.title("Login Page")
root.configure(bg="pink")

# Message to user
msg = '''Login to enter
        Shivaguru Students DBMS'''
msg_label = tk.Label(root, text=msg, font=("Helvetica",20),bg="pink")
msg_label.pack(pady=10)

# To display logo
logo_image = Image.open(r"C:\Users\ELCOT\OneDrive\Desktop\Akash python\students dbms\logo.jpeg")  # Replace "shivu.jpg" with the path to your logo image

# Resize the image to a smaller size
width, height = logo_image.size
new_width = int(width * 0.3)  # You can adjust the scaling factor as needed
new_height = int(height * 0.3)
logo_image.thumbnail((new_width, new_height))
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_photo)
logo_label.pack(pady=10)

# User ID and password
user_id_original = "Admin"
password_original = "sgstudbms"

# Function to execute after clicking submit button
def submit_button_click():
    user_id_input = user_id_entry.get()
    password_input = password_entry.get()

    if user_id_input == user_id_original and password_input == password_original:
        redirect_to_home("home_page.py")
    else:
        messagebox.showerror("Invalid", '''Check your password
and user id''')

# labels and entry fields to input login details
user_id_label = tk.Label(root, text="Enter User ID:",bg='pink')
user_id_label.pack(side=tk.LEFT, padx=10, pady=50)
user_id_entry = tk.Entry(root)
user_id_entry.pack(side=tk.LEFT, padx=10, pady=5)

password_label = tk.Label(root, text="Enter Password:",bg='pink')
password_label.pack(side=tk.LEFT, padx=10, pady=50)
password_entry = tk.Entry(root)
password_entry.pack(side=tk.LEFT, padx=10, pady=50)

# Submit button creation
submit_button = tk.Button(root, text="Submit",command=submit_button_click, bg="blue", fg="white")
submit_button.pack(pady=55)


# Main loop
root.mainloop()

