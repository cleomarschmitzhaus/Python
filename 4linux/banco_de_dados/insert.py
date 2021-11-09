#!/usr/bin/python3

import sqlite3

conn =  sqlite3.connect('cafe.db')

cursor = conn.cursor()

sql = """

    INSERT INTO ingrediente(nome, descricao, tipo, unidade_medida)
    VALUES('agua', 'solvente universal', 'liquido', 'ml');

"""

cursor.execute(sql)

# sempre deve ser commiotado e fgechado a conexão com o banco de dados
conn.commit()
conn.close()

exit()