import sqlite3

print('Região Número de Estados')
print('====== =================')
with sqlite3.connect('estados.db') as conexao:
    for r in conexao.execute("""
    select regiao, count(*)
    from estados
    group by regiao
    """):
        print(f'{r[0]:<15} {r[1]:<17}')