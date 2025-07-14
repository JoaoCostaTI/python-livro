import json

livros = []

# Carregar livros do arquivo JSON ou criar lista vazia
try:
    with open('livros.json', 'r', encoding='utf-8') as arquivo:
        livros = json.load(arquivo)
except FileNotFoundError:
    livros = []

###############################################################################
#reajustes formatacao
def formatacao(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'{msg}'.center(tam))
    print('~' * tam)

def limitarTextos(texto, limite):
    if len(texto) > limite:
        return texto[:limite - 3] + '...'
    return texto

def listarLivros():
        #Titulo das colunas
        print(f'{"Nº":<5}{"Nome":<30}{"Autor(a)":<20}{"Situação":<15}{"Ano":<5}{"Nº Páginas":<5}')
        print('-' * 80)
            #Listar livros com formatação limitada
        for k, livro in enumerate(livros, start=1):
            nome = limitarTextos(livro['nome'], 30)
            autor = limitarTextos(livro['autor'], 20)
            situacao = limitarTextos(livro['situacao'], 15)
            anoLeitura = livro['ano']
            nPaginas = livro["paginas"]

            print(f'{k:<5}{nome:<30}{autor:<20}{situacao:<15}{anoLeitura:<5}{nPaginas:<5}')
        print('~' * 80)
def listarLivrosLendo():
    #Titulo das colunas
        print(f'{"Nº":<5}{"Nome":<30}{"Autor(a)":<20}{"Situação":<15}{"Ano":<5}{"Nº Páginas":<5}')
        print('-' * 80)
            #Listar livros com formatação limitada
        for k, livro in enumerate(livros, start=1):
            if livro['situacao'] == 'lendo':
                nome = limitarTextos(livro['nome'], 30)
                autor = limitarTextos(livro['autor'], 20)
                situacao = limitarTextos(livro['situacao'], 15)
                anoLeitura = livro['ano']
                nPaginas = livro["paginas"]

                print(f'{k:<5}{nome:<30}{autor:<20}{situacao:<15}{anoLeitura:<5}{nPaginas:<5}')
        print('~' * 80)

###############################################################################

#Menu
def menu():
    print('-' * 25)
    print('1 - Cadastrar Livro\n2 - Listar Livro\n3 - Excluir Livro: ')
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
        dados['ano'] =  int(input('Ano de leitura: '))
        dados['paginas'] = int(input('Páginas: '))
        livros.append(dados)
        with open('livros.json', 'w', encoding='utf-8') as arquivo:
            json.dump(livros, arquivo, ensure_ascii=False, indent=4)

    elif op == 2:
        if len(livros) == 0:
            formatacao('Nenhum livro cadastrado! Cadastre ao menos 1 livro! ')   
        else:
            print('1 - Todos os Livros\n2 - Lendo\n3 - Quero Ler\n4 - Lido\n5 - Menu anterior')
            op = int(input('Sua opção: '))
            while True:
                if op == 5:
                    print('Voltando ao menu anterior...')
                    break
                elif op == 1:
                    listarLivros()
                elif op == 2:
                    listarLivrosLendo()
                else:
                    print('Opção inválida! Selecione apenas dentre as disponiveis! ')
                
    elif op == 3:
            #EXCLUSÃO DE LIVROS
            listarLivros()
            while True:
                print('Qual livro deseja excluir? (Digite o número)')
                op = int(input('Livro: '))
                if op > len(livros):
                    print('Não existe esse livro! Tente novamente')
                else:
                    print(f'*' * 65)
                    print(f'Livro [{livros[op-1]['nome']}] excluído com sucesso!')
                    del livros[op - 1] 
                    print(f'*' * 65)
                    with open('livros.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(livros, arquivo, ensure_ascii=False, indent=4)
                    break
    else:
        formatacao('Opção inválida! Selecione uma opção do menu! ')
        

