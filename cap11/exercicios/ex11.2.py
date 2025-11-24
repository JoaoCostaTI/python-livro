import sqlite3

conexao = sqlite3.connect('precos.db')
cursor = conexao.cursor()

cursor.execute('SELECT * FROM precos')
precos = cursor.fetchall()

for p in precos:
    print(f'Produto: {p[0]}\nValor: R${p[1]:.2f}')