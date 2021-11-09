#!/usr/bin/python3

import sqlite3

# 1 conectar com o arquivo de banco de dados
conn = sqlite3.connect('cafe.db')

# 2 criar um cursor para executar instruções

cursor = conn.cursor()

# 3 criar instruções SQL
SQL = """
    CREATE TABLE ingrediente(
    id integer primary key autoincrement,
    nome text,
    descricao text,
    tipo text,
    unidade_medida text);
"""
# função que executa instrução SQL
cursor.execute(SQL)

exit()