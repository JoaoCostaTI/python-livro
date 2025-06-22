import cabecalho
from time import sleep
from pessoas import cadastro

pessoas = {}
listaPessoas = list()

def menuInicial():
    while True:
        sleep(1)
        cabecalho.cabecalhoMenu()
        print('------------------------')
        print(f'1 - Listar Pessoas \n2 - Cadastrar Pessoas \n3 - Sair do Programa')
        print('------------------------')
        sleep(1)
        op = int(input('Digite sua opção: '))
    
        if op == 1:
            cabecalho.cabecalho()
            for k , item in enumerate(pessoas):
                print(f'{k:<3}{item["nome"]:<10} {item["idade"]:>7}')

        if op == 2:
            sleep(1)
            pessoas = cadastroPessoas() 

        if op == 3:
            sleep(1)
            print('Saindo do programa...')
            sleep(1)
            break

def cadastroPessoas():
    flag = True
    cont = 0
    while flag:
        pessoas['nome'] = str(input('Nome: '))
        pessoas['idade'] = int(input('Idade: '))

        listaPessoas.append(pessoas.copy())
        pessoas.clear()

        cont += 1
        if cont == 3:
            flag = False

    return listaPessoas
