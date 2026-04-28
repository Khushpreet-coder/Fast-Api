import sqlite3

conn = sqlite3.connect("database.db", check_same_thread=False)
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        priority TEXT DEFAULT 'Medium',
        status TEXT DEFAULT 'Pending'
    )
""")
conn.commit()
