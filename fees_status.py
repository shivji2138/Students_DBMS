import tkinter as tk
import mysql.connector
from tkinter import messagebox

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "shivusql",
    database = "students_details"
)

cursor = conn.cursor()

def see_fees_status():
    stu_id = id_entry.get()
    cursor.execute("SELECT * FROM fees_details WHERE stu_id=%s",(stu_id,))
    status = cursor.fetchone()
    if status:
        result_label.configure(text=f"{status}")
    else:
        messagebox.showerror("Not found" , "Check The Student ID")

#tkinter window
root = tk.Tk()
root.title("Fee Status")
root.geometry("250x250")
root.configure(bg='skyblue')

#gui components
label_id = tk.Label(root, text="Enter ID:",bg='skyblue')
label_id.pack()

id_entry = tk.Entry(root)
id_entry.pack(pady=10)

see_fee_status = tk.Button(root, text="See Status", bg="purple",fg="white",command = see_fees_status)
see_fee_status.pack(pady=10)

result_label = tk.Label(root,text="",bg='skyblue')
result_label.pack(pady=10)

#mainloop
root.mainloop()

#close db connection
conn.close()
    
    
