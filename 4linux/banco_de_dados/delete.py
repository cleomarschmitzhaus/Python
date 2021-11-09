#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('cafe.db')

cursor =  conn.cursor()

SQL = """
    DELETE FROM ingrediente
    WHERE id = 1

"""

cursor.execute(SQL)

conn.commit()

exit()