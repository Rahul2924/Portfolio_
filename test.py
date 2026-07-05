import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

# Show first 5 contact entries
cur.execute("SELECT * FROM Base_contact LIMIT 5;")
for row in cur.fetchall():
    print(row)

conn.close()
