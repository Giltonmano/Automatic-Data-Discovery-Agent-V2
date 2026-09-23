import sqlite3

conn = sqlite3.connect("data/papers.db")
cursor = conn.cursor()

equipment_data = [
    ("Elmi CM-6M Swing-Out Centrifuge, 3500 rpm, 100-240V", "CM-6M", "$1,544.00",
     "Digital display, Max Speed 3500 rpm, Max RCF 2300 x g",
     "https://www.coleparmer.com/i/elmi-cm-6m-swing-out-centrifuge-3500-rpm-100-240v/8523009", "coleparmer"),
    ("Elmi CM-7S Touchscreen Swing-Out Centrifuge, 3500 rpm, 100-240V", "CM-7S", "$1,860.00",
     "Touchscreen, Max Speed 3500 rpm, Max RCF 2300 x g",
     "https://www.coleparmer.com/i/elmi-cm-7s-touchscreen-swing-out-centrifuge-3500-rpm-100-240v/8523020", "coleparmer"),
    ("Elmi CM-8S Touchscreen Swing-Out Centrifuge, 4500 rpm, 100-240V", "CM-8S", "$2,125.00",
     "Touchscreen, Max Speed 4500 rpm, Max RCF 3400 x g",
     "https://www.coleparmer.com/i/elmi-cm-8s-touchscreen-swing-out-centrifuge-4500-rpm-100-240v/8523021", "coleparmer"),
]

for name, model, price, specs, link, source in equipment_data:
    try:
        cursor.execute("""
            INSERT INTO equipment (name, model, price, specs, link, source)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, model, price, specs, link, source))
        print("Saved:", name)
    except sqlite3.IntegrityError:
        print("Already exists, skipped:", name)

conn.commit()
conn.close()