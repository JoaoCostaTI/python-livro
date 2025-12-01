import sqlite3
from contextlib import closing

with sqlite3.connect('precos.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('SELECT * FROM precos')
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print('-' *5)
            print(f'Produto: {resultado[0]}\nPreço: R${resultado[1]:.2f}')
        print('-' * 5)
 