import sqlite3


def create_database():
    conn = sqlite3.connect("data/papers.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS papers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        published TEXT,
        link TEXT UNIQUE,
        summary TEXT,
        source TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS equipment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            model TEXT,
            price TEXT,
            specs TEXT,
            link TEXT UNIQUE,
            source TEXT
        )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database created successfully.")