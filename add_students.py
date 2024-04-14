import mysql.connector
import tkinter as tk
from tkinter import messagebox

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="shivusql",
            database="students_details"
        )
        return conn
    except mysql.connector.Error as err:
        return None

def insert_data(conn, stu_id, stu_name, gender, percentage, clasS, section, age):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO stu_general_details(stu_id, stu_name, gender, percentage, class, section, age) VALUES (%s, %s,%s,%s,%s,%s,%s)"
        val = (stu_id, stu_name, gender, percentage, clasS, section, age)
        cursor.execute(sql, val)
        conn.commit()
        messagebox.showinfo("Success", "Data inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        messagebox.showerror("Error", f"Error: {err}")

def submit_button_clicked():
    stu_id = int(student_id_entry.get())
    stu_name = name_entry.get()
    gender = gender_entry.get()
    percentage = int(percentage_entry.get())
    clasS = int(class_entry.get())
    section = section_entry.get()
    age = int(age_entry.get())
    
    conn = connect_to_database()
    if conn:
        insert_data(conn, stu_id, stu_name, gender, percentage, clasS, section, age)
        conn.close()

# Create the main window
root = tk.Tk()
root.title("Student Details Entry Form")
root.configure(bg="pink")

# Create labels and entry fields
tk.Label(root, text="Student ID:", bg="pink").grid(row=0, column=0, padx=10, pady=5)
student_id_entry = tk.Entry(root)
student_id_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Name:",bg="pink").grid(row=1, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Gender:",bg="pink").grid(row=2, column=0, padx=10, pady=5)
gender_entry = tk.Entry(root)
gender_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Percentage:",bg="pink").grid(row=3, column=0, padx=10, pady=5)
percentage_entry = tk.Entry(root)
percentage_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Class:",bg="pink").grid(row=4, column=0, padx=10, pady=5)
class_entry = tk.Entry(root)
class_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Section:", bg="pink").grid(row=5, column=0, padx=10, pady=5)
section_entry = tk.Entry(root)
section_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="Age:",bg="pink").grid(row=6, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=6, column=1, padx=10, pady=5)

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit_button_clicked, bg="green", fg="white")
submit_button.grid(row=7, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
