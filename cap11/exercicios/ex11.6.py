import sqlite3
from contextlib import closing

with sqlite3.connect('precos.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        produto = input('Nome do Produto: ')
        novo_preco = float(input('Novo Preço: R$'))
        cursor.execute('UPDATE precos set preco = ? where nome = ?', (novo_preco, produto))

        if cursor.rowcount == 1:
            conexao.commit()
            print(f'{produto} alterado com sucesso...')
        else:
            conexao.rollback()
            print(f'Algo deu errado... tente novamente. ')
                


