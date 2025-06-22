from pessoas import cadastro
from cabecalho import *

pessoas = cadastro.cadastroPessoas()


cabecalho()
for k , item in enumerate(pessoas):
    print(f'{k:<3}{item["nome"]:<10} {item["idade"]:>7}')
