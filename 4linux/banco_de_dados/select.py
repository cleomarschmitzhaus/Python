#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('cafe.db') # try
cursor =  conn.cursor()

SQL = "SELECT * FROM ingrediente"

for registro in cursor.execute(SQL):
    print(registro)

conn.commit()
conn.close()

exit()

### AULA 7 de 12 - Banco de dados