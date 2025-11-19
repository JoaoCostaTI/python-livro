import sqlite3

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()

cursor.execute('SELECT * FROM agenda')
resultado = cursor.fetchall()
print(resultado)

for r in resultado:
    print(f'Nome: {r[0]}\nTelefone: {r[1]}')

cursor.close()
conexao.close()