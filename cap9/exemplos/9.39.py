AGENDA = []

import json

def pedeNome():
    return input("Nome: ")
def pedeTelefone():
    return input("Telefone: ")
def mostraDados (nome, telefone):
    print(f"Nome: {nome}\nTelefone: {telefone}")
def pedeNomeArquivo():
    return input("Nome do arquivo: ")
def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(AGENDA):
        if e[0].lower() == mnome:
            return p
    return None

def novo():
    nome = pedeNome()
    telefone = pedeTelefone()
    AGENDA.append([nome, telefone])

def apaga():
    nome = pedeNome()
    p = pesquisa(nome)
    if p is not None:
        del AGENDA[p]
    else:
        print("Nome não encontrado.")
    
def altera():
    p = pesquisa(pedeNome())
    if p is not None:
        nome = AGENDA[p][0]
        telefone = AGENDA[p][1]

        print("Encontrado:")
        mostraDados(nome, telefone)
        nome = pedeNome()
        telefone = pedeTelefone()
        AGENDA[p] = [nome, telefone]
    else:
        print("Nome não encontrado.")

def lista():
    print("\nAgenda\n\n------")
    for e in AGENDA:
        mostraDados(e[0], e[1])
    print("------\n")

def le():
    global AGENDA
    nomeArquivo = pedeNomeArquivo()
    with open(nomeArquivo, 'r', encoding="utf-8") as arquivo:
        AGENDA = json.load(arquivo)

def grava():
    nomeArquivo = pedeNomeArquivo()
    with open(nomeArquivo, 'w', encoding="utf-8") as arquivo:
        json.dump(AGENDA, arquivo, indent=2, ensure_ascii=False)

def validaFaixaInteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor or inicio <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")
        
def menu():
    print("1 - Novo\n2 - Altera\n3 - Apaga\n4 - Lista\n5 - Grava\n6 - Lê\n0 - Sai")
    return validaFaixaInteiro("Escolha uma opção: ", 0, 6)

while opcao := menu():
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        grava()
    elif opcao == 6:
        le()