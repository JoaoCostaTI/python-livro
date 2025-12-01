import sqlite3
from contextlib import closing

with sqlite3.connect('agenda.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('DELETE FROM agenda where nome = "Joao"')
        print('Registros afetados: ', cursor.rowcount)
        if cursor.rowcount >=1:
            conexao.commit()
            print('Alterações gravadas...')
        else:
            conexao.rollback()
            print('Alterações abortadas.')