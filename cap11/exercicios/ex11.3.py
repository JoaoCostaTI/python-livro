import sqlite3
from contextlib import closing

produto = input('Qual produto pesquisar? ')
with sqlite3.connect('precos.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('SELECT * from precos where nome = ?' ,(produto,))
        res = cursor.fetchone()
        while True:
            if res is None:
                print('Não encontrado! ')
                break
            print(f'Produto: {res[0]}\nPreço: R${res[1]:.2f}')
            break