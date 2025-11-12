import sqlite3

def init_db():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                      id INTEGER PRIMARY KEY,
                      date TEXT,
                      category TEXT,
                      description TEXT,
                      amount REAL,
                      type TEXT)''')
    conn.commit()
    conn.close()

def add_transaction(date, category, description, amount, ttype):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO transactions (date, category, description, amount, type) VALUES (?, ?, ?, ?, ?)',
                   (date, category, description, amount, ttype))
    conn.commit()
    conn.close()

def fetch_transactions():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions ORDER BY date DESC')
    rows = cursor.fetchall()
    conn.close()
    return rows
