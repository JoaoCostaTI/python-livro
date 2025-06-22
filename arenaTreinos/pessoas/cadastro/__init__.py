pessoas = {}
listaPessoas = list()

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
