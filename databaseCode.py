import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
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

def load_data():
    conn = sqlite3.connect("packing.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_status(id, new_status):
    conn = sqlite3.connect("packing.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE items SET status = ? WHERE ID = ?", (new_status, id))
    conn.commit()
    conn.close()

def delete_item(id):
    conn = sqlite3.connect("packing.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = ?", (id))
    conn.commit()
    conn.close()

def query_items(search_query):
    conn = sqlite3.connect("packing.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE name LIKE ?  OR category LIKE ? OR status LIKE ?", 
    ('%'+search_query+'%', '%'+search_query+'%', '%'+search_query+'%'))
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

def change_status():
    selected_item = tree.selection()
    if selected_item:
        item_id = tree.item(selected_item, 'values')[0]
        new_status = simpledialog.askstring("Update Status", "Enter new status:")
        if new_status:  # Making sure that the user didn't cancel the dialog
            update_status(item_id, new_status)
            refresh_view()
    else:
        messagebox.showinfo("Update Error", "No item selected. Please select an item to update.")


def delete_selected_item():
    selected_item = tree.selection()
    if selected_item:
        item_id = tree.item(selected_item, 'values')[0]
        # Use the messagebox to confirm deletion
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this item?"):
            delete_item(item_id)
            tree.delete(selected_item)
            print("Item deleted successfully.")
    else:
        messagebox.showwarning("Delete Error", "No item selected. Please select an item to delete.")


def perform_query():
    search_query = simpledialog.askstring("Query Items", "Enter search term:")
    if search_query:
        rows = query_items(search_query)
        for row in tree.get_children():
            tree.delete(row)
        for row in rows:
            tree.insert("", tk.END, values=row)

app = tk.Tk()
app.title("Packing List")

tree = ttk.Treeview(app, columns=("ID", "Name", "Category", "Status"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Category", text="Category")
tree.heading("Status", text="Status")
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

###############
##  BUTTONS  ##
###############

refresh_button = tk.Button(app, text="Refresh", command=refresh_view)
update_button = tk.Button(app, text="Update Status", command=change_status)
delete_button = tk.Button(app, text="Delete Item", command=delete_selected_item)
query_button = tk.Button(app, text="Query", command=perform_query)


refresh_button.pack(side=tk.RIGHT, padx=10, pady=10)
update_button.pack(side=tk.RIGHT, padx=10, pady=10)
delete_button.pack(side=tk.RIGHT, padx=10, pady=10)
query_button.pack(side=tk.RIGHT, padx=10, pady=10)

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
