import sqlite3

conexao = sqlite3.connect('hahaha.db')
cursor = conexao.cursor()

cursor.execute('SELECT * FROM hahaha')

dados = cursor.fetchall()
print(dados)

cursor.close()
conexao.close()


