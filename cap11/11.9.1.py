import sqlite3
from contextlib import closing

with sqlite3.connect('estados.db') as conexao:

    with closing(conexao.cursor()) as cursor:
        conexao.row_factory = sqlite3.Row
        
        print(f'{"ID":<3}{"ESTADO":<20s}{"POPULAÇÃO":<12}')
        print('=' * 37)
        for r in conexao.execute('SELECT * from estados order by populacao desc'):
            print(f'{r["id"]:<3}{r["nome"]:<20}{r["populacao"]:<12}')