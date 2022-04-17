"""
    RUN THIS CODE ONLY ONCE
    IT CREATES DATABASE AND TABLE
"""

import sqlite3 as sql

conn = sql.connect('blood.db')

c = conn.cursor()

# c.execute("""
#     CREATE TABLE blood (
#         bloodType text,
#         availablePackets INTEGER
#     )
# """)

c.execute("INSERT INTO blood VALUES ('A+', '0')")
c.execute("INSERT INTO blood VALUES ('B+', '0')")
c.execute("INSERT INTO blood VALUES ('AB+', '0')")
c.execute("INSERT INTO blood VALUES ('O+', '0')")

c.execute("INSERT INTO blood VALUES ('A-', '0')")
c.execute("INSERT INTO blood VALUES ('B-', '0')")
c.execute("INSERT INTO blood VALUES ('AB-', '0')")
c.execute("INSERT INTO blood VALUES ('O-', '0')")


conn.commit()
