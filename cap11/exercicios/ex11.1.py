import sqlite3

conexao = sqlite3.connect('precos.db')

cursor = conexao.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS precos(nome text, preco)')

valores = [('Banana', 8.99), ('Abacate', 3.99), ('Melancia', 1.99)]

cursor.executemany('INSERT INTO precos values(?, ?)', valores)

conexao.commit()

cursor.close()
conexao.close()
