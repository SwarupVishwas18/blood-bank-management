import sqlite3 as sql

conn = sql.connect('trans.db')

c = conn.cursor()

c.execute("""
    CREATE TABLE trans (
        name text,
        email text,
        bloodType text,
        packets INTEGER,
        transtype text
            )
""")

conn.commit()
