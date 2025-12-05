import sqlite3

with sqlite3.connect('estados.db') as conexao:
    for r in conexao.execute("""
    select regiao, count(*), min(populacao), max(populacao), avg(populacao), sum(populacao) from estados group by regiao order by sum(populacao) desc"""):
        print(f"{r[0]:<15}{r[1]:<7}{r[2]:<18}{r[3]:<10}{r[4]:<10,.0f}{r[5]:<13,}")
    print(f'\nBrasil:')