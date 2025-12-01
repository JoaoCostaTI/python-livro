import sqlite3
from contextlib import closing

with sqlite3.connect('agenda.db') as conexao:
    conexao.row_factory = sqlite3.Row
    with closing(conexao.cursor()) as cursor:
        for r in cursor.execute('SELECT * FROM agenda'):
            print(f'Nome: {r["nome"]}\nTelefone: {r["telefone"]}')