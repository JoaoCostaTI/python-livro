import sqlite3
from contextlib import closing



nome = input('Nome a selecionar: ')
with sqlite3.connect('agenda.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute(f'SELECT * from agenda where nome="{nome}"')
        while True:
            res=cursor.fetchone()
            if res is None:
                break
            print(f"Nome: {res[0]}\nTelefone: {res[1]}")