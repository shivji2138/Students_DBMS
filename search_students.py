import tkinter as tk
import mysql.connector

def search_student():
    stu_id = id_entry.get()
    cursor.execute("SELECT * FROM biodata WHERE stu_id=%s", (stu_id,))
    student = cursor.fetchone()
    if student:
        result_label.config(text=f'''Student found
                                NAME: {student[1]}
                                DOB: {student[2]}
                                AGE: {student[3]}
                                STD: {student[4]}
                                BLOOD GROUP: {student[5]}
                                AADHAAR NUM: {student[6]}
                                FATHER'S NAME: {student[7]}
                                MOTHER'S NAME: {student[8]}
                                FATHER'S OCCUPATION: {student[9]}
                                MOTHER'S OCCUPATION: {student[10]}
                                ANNUAL INCOME: {student[11]}
                                RESIDENTIAL ADDRESS: {student[12]}
                                MOBILE NUMBER: {student[13]}
                                PARENT EMAIL: {student[14]}
                                STUDENT'S EMAIL: {student[15]}''')
    else:
        result_label.config(text="Student not found.")

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="shivusql",
    database="students_details"
)
cursor = conn.cursor()

# Create Tkinter window
root = tk.Tk()
root.title("Student Search")
root.configure(bg='pink')
root.geometry('600x450')

# Create GUI components
label_name = tk.Label(root, text="Enter ID to search:", bg='pink')
label_name.pack()

id_entry = tk.Entry(root)
id_entry.pack()

search_button = tk.Button(root, text="Search", command=search_student,bg="blue",fg="white")
search_button.pack(pady=10)

result_label = tk.Label(root, text="", bg='pink')
result_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

# Close the database connection
conn.close()
