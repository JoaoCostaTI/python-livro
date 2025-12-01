import sqlite3
from contextlib import closing

estados = [
    ["Acre", 954991],
    ["Alagoas", 3351543],
    ["Amapá", 845731],
    ["Amazonas", 4411153],
    ["Bahia", 15203913],
    ["Ceará", 9187103],
    ["Distrito Federal", 3266429],
    ["Espírito Santo", 4181249],
    ["Goiás", 7513933],
    ["Maranhão", 7153262],
    ["Mato Grosso", 3726256],
    ["Mato Grosso do Sul", 2809394],
    ["Minas Gerais", 21411923],
    ["Pará", 8690745],
    ["Paraíba", 4237364],
    ["Paraná", 11641516],
    ["Pernambuco", 9593765],
    ["Piauí", 3550381],
    ["Rio de Janeiro", 17463349],
    ["Rio Grande do Norte", 3616918],
    ["Rio Grande do Sul", 11329605],
    ["Rondônia", 1828689],
    ["Roraima", 652713],
    ["Santa Catarina", 7656920],
    ["São Paulo", 46387458],
    ["Sergipe", 2278308],
    ["Tocantins", 1647565]
]


with sqlite3.connect('estados.db') as conexao:
    conexao.row_factory = sqlite3.Row
    with closing(conexao.cursor()) as cursor:
        cursor.execute('CREATE TABLE estados (id integer primary key autoincrement, nome text, populacao integer)')
        cursor.executemany('INSERT INTO estados (nome, populacao) values (?, ?)', estados)
    conexao.commit()

