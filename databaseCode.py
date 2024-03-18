import tkinter as tk
from tkinter import ttk
import sqlite3
import threading

# Database Operations
def create_db():
    conn = sqlite3.connect('packing.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS items
                    (id INTEGER PRIMARY KEY, name TEXT, category TEXT, status TEXT)''')
    conn.commit()
    conn.close()

def insert_item(name, category, status='Not Packed'):
    conn = sqlite3.connect('packing.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name, category, status) VALUES (?, ?, ?)", (name, category, status))
    conn.commit()
    conn.close()

def load_data():
    conn = sqlite3.connect('packing.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()
    conn.close()
    return rows


# GUI
def view_data():
    for row in tree.get_children():
        tree.delete(row)
    rows = load_data()
    for row in rows:
        tree.insert("", tk.END, values=row)

def refresh_view():
    view_data()

app = tk.Tk()
app.title("Packing List")

tree = ttk.Treeview(app, columns=("ID", "Name", "Category", "Status"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Category", text="Category")
tree.heading("Status", text="Status")
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

refresh_button = tk.Button(app, text="Refresh", command=refresh_view)
refresh_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Terminal Input Function
def terminal_input():
    while True:
        print("Enter item details (name, category, status) or 'quit' to exit:")
        details = input("> ")
        if details.lower() == 'quit':
            break
        try:
            name, category, status = details.split(", ")
            insert_item(name, category, status)
            print("Slayyyyyyyy - item added successfully.")
        except ValueError:
            print("lmao, wrong format, dummy. try again: name, category, status")

# make a thread for running terminal input
#have tkinter gui running in thread 2
input_thread = threading.Thread(target=terminal_input, daemon=True)
input_thread.start()

# Initially create the database and table
create_db()

view_data()

app.mainloop()
