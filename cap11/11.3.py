import sqlite3
from contextlib import closing

with sqlite3.connect('agenda.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('SELECT * FROM agenda')
        while True:
            res = cursor.fetchone()
            if res is None:
                break
            print(f'Nome: {res[0]}\nTel: {res[1]}')
         