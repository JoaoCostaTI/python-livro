import sqlite3

print('Região Estados Populacao  Mínima  Máxima  Média  Total(Soma)')
with sqlite3.connect('estados.db') as conexao:
    for r in conexao.execute('''
    select regiao, count(*), min(populacao), max(populacao), avg(populacao), sum(populacao) as tpop
    from estados
    group by regiao
    having count(*) > 5
    order by tpop desc                               
'''):
        print(f"{r[0]:<10}{r[1]:<10}{r[2]:<18}{r[3]:<18}{r[4]:<20}{r[5]:<13}")