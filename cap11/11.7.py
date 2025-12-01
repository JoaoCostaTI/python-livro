import sqlite3

with sqlite3.connect('agenda.db') as conexao:
    for r in conexao.execute('select * from agenda'):
        print(f'Nome: {r[0]} - Telefone: {r[1]}')