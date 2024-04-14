import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import mysql.connector

def redirect_to_script(script_path):
    subprocess.run(['python',script_path])

# Create the main window
root = tk.Tk()
root.title("Home Page")
root.configure(bg='pink')
root.geometry('500x690')

# Function to handle button click
def button_clicked(script_path):
    redirect_to_script(script_path)

# Welcome message
welcome_message = "Welcome to Shivaguru Students DBMS Portal"
welcome_label = tk.Label(root, text=welcome_message, bg='pink', font=("Helvetica", 16))
welcome_label.pack(pady=20)

# To display logo
logo_image = Image.open(r"C:\Users\ELCOT\OneDrive\Desktop\Akash python\students dbms\logo.jpeg")  # path to logo image

# Resize the image to a smaller size
width, height = logo_image.size
new_width = int(width * 0.3)  # we can adjust the scaling factor as needed
new_height = int(height * 0.3)
logo_image.thumbnail((new_width, new_height))
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(root, image=logo_photo)
logo_label.pack(pady=10)

# Creating buttons to redirect to Scripts
button1 = tk.Button(root, text="Add Students", command=lambda: button_clicked("add_students.py"),bg="blue",fg="white")
button1.pack(pady=10)

button2 = tk.Button(root, text="Search Students", command=lambda: button_clicked("search_students.py"),bg="purple",fg="white")
button2.pack(padx=5,pady=0)

button3 = tk.Button(root, text="Remove Students", command=lambda: button_clicked("remove_stu.py"),bg="red",fg="white")
button3.pack(pady=10)

button4 = tk.Button(root, text="View Table",command=lambda: button_clicked("view_table.py"),bg="yellow",fg="blue")
button4.pack(pady=10)

button5 = tk.Button(root, text="Add Bio Data",command=lambda: button_clicked("biodata.py"),bg="violet",fg="black")
button5.pack(pady=10)

button6 = tk.Button(root, text="Fee Status", command=lambda: button_clicked("fees_status.py"),bg="black", fg="white")
button6.pack(pady=10)

button7 = tk.Button(root,text="Pay Fees", command= lambda: button_clicked("pay_fees.py"),bg="orange",fg="white")
button7.pack(pady=10)

button8 = tk.Button(root,text="Update Fees", command= lambda: button_clicked('update_fees.py'), bg="skyblue", fg="black")
button8.pack(pady=10)

# Run the main event loop
root.mainloop()
