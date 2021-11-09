#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('cafe.db')

cursor = conn.cursor()

SQL = """
    UPDATE ingrediente
    SET unidade_medida= 'l'
    WHERE id=1

"""

cursor.execute(SQL)
conn.commit()
conn.close()

exit()