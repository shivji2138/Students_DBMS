import mysql.connector
import tkinter as tk
from tkinter import messagebox

#connect db
conn= mysql.connector.connect(
    host="localhost",
    user="root",
    password="shivusql",
    database="students_details"
)
cursor=conn.cursor()

def submit_button_clicked():
    try:
        stu_id = int(stuid_entry.get())
        stu_name = stuname_entry.get()
        clasS = int(std_entry.get())
        bookfees = int(bookfees_entry.get())
        tuitionfees = int(tuitionfees_entry.get())
        totalfees = bookfees+tuitionfees
        paidfees = int(paidfees_entry.get())
        balancefees = totalfees-paidfees
        cursor = conn.cursor()
        sql = "INSERT INTO fees_details(stu_id, stu_name, class, book_fees, tuition_fees, total_fees, paid_fees, balance_fees) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (stu_id, stu_name, clasS, bookfees, tuitionfees, totalfees, paidfees, balancefees)
        cursor.execute(sql, val)
        conn.commit()
        messagebox.showinfo("Success", "Data inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        messagebox.showerror("Error", f"Error: {err}")
        
#tkinter window
root = tk.Tk()
root.title("Update Fees")
root.configure(bg="skyblue")
root.geometry("300x300")

#create button and label
stuid_label= tk.Label(root,text="Enter student ID:",bg="skyblue")
stuid_label.grid(row=0,column=0,padx=10,pady=10)

stuid_entry = tk.Entry(root)
stuid_entry.grid(padx=10,row=0,pady=10,column=1)

stuname_label = tk.Label(root,text="Enter Student Name:",bg='skyblue')
stuname_label.grid(row=1,padx=10,column=0,pady=10)

stuname_entry = tk.Entry(root)
stuname_entry.grid(row=1,padx=10,pady=10,column=1)

std_label = tk.Label(root,text="Enter Class:", bg='skyblue')
std_label.grid(row=2,padx=10,pady=10,column=0)

std_entry = tk.Entry(root)
std_entry.grid(row=2,column=1,padx=10,pady=10)

bookfees_label = tk.Label(root, text="Enter Book Fees:",bg="skyblue")
bookfees_label.grid(row=3,column=0,padx=10,pady=10)

bookfees_entry = tk.Entry(root)
bookfees_entry.grid(row=3,column=1,padx=10,pady=10)

tuitionfees_label = tk.Label(root,text="Enter Tuition Fees:",bg="skyblue")
tuitionfees_label.grid(row=4,column=0,padx=10,pady=10)

tuitionfees_entry = tk.Entry(root)
tuitionfees_entry.grid(row=4,column=1,padx=10,pady=10)

#totalfees=

paidfees_label = tk.Label(root,text="Enter Paid Fees:",bg="skyblue")
paidfees_label.grid(row=5,column=0,padx=10,pady=10)

paidfees_entry = tk.Entry(root)
paidfees_entry.grid(row=5,column=1,padx=10,pady=10)

#balancefees

submit_button= tk.Button(root,text='Submit',command=submit_button_clicked,bg='green',fg='white')
submit_button.grid(row=6,column=1,padx=10,pady=10)

#mainwindow
root.mainloop()

#close db connection
conn.close()


