import sqlite3

conn = sqlite3.connect("data/papers.db")
cursor = conn.cursor()

cursor.execute("SELECT title, published, source FROM papers")
rows = cursor.fetchall()

print(f"Total papers in database: {len(rows)}")
print("-" * 40)
for row in rows:
    print(row)

conn.close()    