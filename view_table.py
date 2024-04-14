import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def view_table():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="shivusql",
        database="students_details"
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM stu_general_details")
    table = cursor.fetchall()

    cursor.close()
    conn.close()

    if table:
        

        # Display table headers with separate sizes for different columns
        headers = [('ID', 8), ('Name', 30), ('Gender', 12), ("%", 8), ("STD", 8), ("Section", 8), ("Age", 8)]  # (Column name, Column width)
        for i, (header, width) in enumerate(headers):
            header_label = tk.Label(table_frame, text=header, borderwidth=1, relief="solid", width=width, bg="LightGray", font=("Arial", 10, "bold"))
            header_label.grid(row=0, column=i, sticky="nsew")

        # Display table data
        for row_index, row_data in enumerate(table, start=1):
            for col_index, col_data in enumerate(row_data):
                width = headers[col_index][1]  # Get width for this column
                data_label = tk.Label(table_frame, text=col_data, borderwidth=1, relief="solid", width=width, bg="White", font=("Arial", 10))
                data_label.grid(row=row_index, column=col_index, sticky="nsew")

        # Update canvas and scrolling region
        root.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

def search_table():
    stuid = search_entry.get()
    if stuid:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="shivusql",
            database="students_details"
        )
        cursor = conn.cursor()

        query = "SELECT * FROM stu_general_details WHERE stu_id = %s"
        cursor.execute(query, (stuid,))
        result = cursor.fetchall()

        cursor.close()
        conn.close()

        if result:
            # Clear existing table
            for widget in table_frame.winfo_children():
                widget.destroy()

            # Display table headers with separate sizes for different columns
            headers = [('ID', 8), ('Name', 30), ('Gender', 12), ("%", 8), ("STD", 8), ("Section", 8), ("Age", 8)]  # (Column name, Column width)
            for i, (header, width) in enumerate(headers):
                header_label = tk.Label(table_frame, text=header, borderwidth=1, relief="solid", width=width, bg="LightGray", font=("Arial", 10, "bold"))
                header_label.grid(row=0, column=i, sticky="nsew")

            # Display table data
            for row_index, row_data in enumerate(result, start=1):
                for col_index, col_data in enumerate(row_data):
                    width = headers[col_index][1]  # Get width for this column
                    data_label = tk.Label(table_frame, text=col_data, borderwidth=1, relief="solid", width=width, bg="White", font=("Arial", 10))
                    data_label.grid(row=row_index, column=col_index, sticky="nsew")

            # Update canvas and scrolling region
            root.update_idletasks()
            canvas.config(scrollregion=canvas.bbox("all"))
        else:
            tk.messagebox.showinfo("Search", "No matching record found.")

root = tk.Tk()
root.title("View tables")
root.configure(bg="WhiteSmoke")

canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

table_frame = tk.Frame(canvas, bg="White")
canvas.create_window((0, 0), window=table_frame, anchor='nw')

search_frame = tk.Frame(root, bg="WhiteSmoke")
search_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)

search_label = tk.Label(search_frame, text="Search ID:", bg="WhiteSmoke", font=("Arial", 10))
search_label.grid(row=0, column=0, padx=(0, 5))

search_entry = tk.Entry(search_frame, bg="White", font=("Arial", 10))
search_entry.grid(row=0, column=1, padx=(0, 5))

search_button = tk.Button(search_frame, text="Search", command=search_table, bg="DodgerBlue", fg="White", font=("Arial", 10, "bold"), padx=10, pady=5, bd=0)
search_button.grid(row=0, column=2, padx=(0, 5))

view_button = tk.Button(root, text="View Students", command=view_table, bg="DodgerBlue", fg="White", font=("Arial", 10, "bold"), padx=10, pady=5, bd=0)
view_button.pack(pady=10)

root.mainloop()
