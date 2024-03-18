import sqlite3

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

