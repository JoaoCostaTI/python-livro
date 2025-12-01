import sqlite3
from contextlib import closing

with sqlite3.connect('precos.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        aumento = 10
        cursor.execute(f'UPDATE precos set preco = preco + ((preco * {aumento}) / 100) ')
        
        cursor.execute("""update precos set preco = preco * 1.1""")

