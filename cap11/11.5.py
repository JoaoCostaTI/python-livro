import sqlite3
from contextlib import closing

nome = input('Nome a pesquisar: ')
with sqlite3.connect('agenda.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute(f'SELECT * FROM agenda where nome = ?', (nome,))
        x = 0
        while True:
            res = cursor.fetchone()
            if res is None:
                if x == 0:
                    print('Nada Encontrado.')
                break
            print(f'Nome: {res[0]}\nTelefone: {res[1]}')
            x += 1
        print(x)
