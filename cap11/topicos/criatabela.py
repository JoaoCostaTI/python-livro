import sqlite3

dados = [
    ('Joao', '31992206233'),
    ('Pedro', '9876543213'),
    ('Ana', '987654651')
]

conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE if not EXISTS agenda (nome, telefone)')

cursor.executemany("""
    INSERT INTO agenda(nome, telefone)
    VALUES(?,?)
""", dados)

conexao.commit()
cursor.close()
conexao.close()


conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()

cursor.execute('SELECT * FROM agenda')
resultado = cursor.fetchall()

print(resultado)