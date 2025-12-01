import sqlite3
from contextlib import closing

with sqlite3.connect('agenda.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute("""
    UPDATE AGENDA set telefone = "34190900"
""")
        print(f"Registros alterados: ", cursor.rowcount)
        
    if cursor.rowcount == 1:
        conexao.commit()
        print('Alterações realizadas com sucesso! ')
    else:
        conexao.rollback()
        print('Alterações abortadas! Algo deu errado. ')