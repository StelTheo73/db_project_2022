import sqlite3
DB_PATH = './src/data/database.db'

db = sqlite3.connect(DB_PATH)

query = db.execute("SELECT name FROM clubs")

l = [q[0] for q in query]

print(l)
