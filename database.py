import sqlite3

def create_database():
    conn = sqlite3.connect("data/papers.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS papers (
            ...
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS equipment (
            ...
        )
    """)
    
    conn.commit()
    conn.close()

def save_paper(paper):
    conn = sqlite3.connect("data/papers.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO papers (title, published, link, summary, source)
            VALUES (?, ?, ?, ?, ?)
        """, (paper["title"], paper["published"], paper["link"], paper["summary"], paper["source"]))
        conn.commit()
    except sqlite3.IntegrityError:
        pass  # already exists, skip silently
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database created successfully.")