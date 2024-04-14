import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shivusql",
    database="students_details"
)

cursor = conn.cursor()

def see_stu_fee_detail():
    stu_id = id_entry.get()
    amount_paid = float(money_entry.get())
    cursor.execute("SELECT balance_fees, paid_fees FROM fees_details WHERE stu_id=%s", (stu_id,))
    row = cursor.fetchone()
    if row:
        balance = row[0] - amount_paid
        total_paid_fee = row[1] + amount_paid
        result_label.config(text=f"Balance: {balance}")
        # Update the balance and total paid fees in the fees_details table
        sql = "UPDATE fees_details SET balance_fees = %s, paid_fees = %s WHERE stu_id = %s"
        val = (balance, total_paid_fee, stu_id)
        cursor.execute(sql, val)
        conn.commit()
    else:
        messagebox.showerror("Error", "Student ID not found")

#create tkinter window
root = tk.Tk()
root.title("Pay Fees")
root.geometry("250x250")
root.configure(bg='skyblue')

#create gui components
id_label =tk.Label(root, text="Enter Student ID",bg='skyblue')
id_label.pack(pady=10)

id_entry = tk.Entry(root)
id_entry.pack(pady=10)

money_label = tk.Label(root, text="Enter the Amount:",bg='skyblue')
money_label.pack(pady=10)

money_entry = tk.Entry(root)
money_entry.pack(pady=10)

pay_button = tk.Button(root, text="Pay Now",command=see_stu_fee_detail,bg='purple',fg='white')
pay_button.pack(pady=10)

result_label = tk.Label(root, text="",bg='skyblue')
result_label.pack(pady=10)

#mainloop
root.mainloop()

#close the db connection
conn.close()
