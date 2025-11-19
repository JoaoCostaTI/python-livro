import sqlite3

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('SELECT * FROM agenda')

while True:
    res = cursor.fetchone()
    if res is None:
        break
    print(f'Nome: {res[0]}\nTelefone: {res[1]}')

cursor.close()
conexao.close()