import sqlite3

def search_papers(keyword, cursor):
    cursor.execute("""
        SELECT title, published, link, source
        FROM papers
        WHERE title LIKE ? OR summary LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%"))
    return cursor.fetchall()

def search_equipment(keyword, cursor):
    cursor.execute("""
        SELECT name, model, price, specs, link, source
        FROM equipment
        WHERE name LIKE ? OR specs LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%"))
    return cursor.fetchall()

def search_all(keyword):
    conn = sqlite3.connect("data/papers.db")
    cursor = conn.cursor()

    papers = search_papers(keyword, cursor)
    equipment = search_equipment(keyword, cursor)

    conn.close()
    return papers, equipment

if __name__ == "__main__":
    keyword = input("What are you searching for? ")
    papers, equipment = search_all(keyword)

    print(f"\n=== PAPERS ({len(papers)} found) ===")
    print("-" * 40)
    for title, published, link, source in papers:
        print(f"Title: {title}")
        print(f"Published: {published}")
        print(f"Link: {link}")
        print(f"Source: {source}")
        print("-" * 40)

    print(f"\n=== EQUIPMENT ({len(equipment)} found) ===")
    print("-" * 40)
    for name, model, price, specs, link, source in equipment:
        print(f"Name: {name}")
        print(f"Model: {model}")
        print(f"Price: {price}")
        print(f"Specs: {specs}")
        print(f"Link: {link}")
        print(f"Source: {source}")
        print("-" * 40)