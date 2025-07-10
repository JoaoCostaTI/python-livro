import json

livros = []

# Carregar livros do arquivo JSON ou criar lista vazia
try:
    with open('livros.json', 'r', encoding='utf-8') as arquivo:
        livros = json.load(arquivo)
except FileNotFoundError:
    livros = []

#reajustes formatacao
def formatacao(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'{msg}'.center(tam))
    print('~' * tam)

#Menu
def menu():
    print('-' * 25)
    print('1 - Cadastrar Livro\n2 - Listar Livro\n3 - Sair do programa: ')
    print('-' * 25)

while True:
    menu()
    op = int(input('Sua opção: '))

    if op == 1:
        #cadastrar os livros:
        dados = {}

        dados['nome'] = input('Nome do livro: ')
        dados['autor'] = input('Nome Autor(a): ')
        dados['situacao'] = input('---Situação---\n[Quero Ler]\n[Lendo]\n[Lido]')
        livros.append(dados)
        with open('livros.json', 'w', encoding='utf-8') as arquivo:
            json.dump(livros, arquivo, ensure_ascii=False, indent=4)

    elif op == 2:
        if len(livros) == 0:
            formatacao('Nenhum livro cadastrado! Cadastre ao menos 1 livro! ')   
        else:
            print('~' * 50)
            #listar os livros
            print(f'{"Nº":<5}{"Nome":<20}{"Autor(a)":<20}{"Situação":<15}')
            print('-' * 65)
            for k, livro in enumerate(livros):
                print(f'{k:<5}{livro["nome"]:<20}{livro["autor"]:<20}{livro["situacao"]:<15}')
            print('~' * 50)
    elif op == 3:
        formatacao('Saindo do programa...')
        break
    else:
        formatacao('Opção inválida! Selecione uma opção do menu! ')
        

