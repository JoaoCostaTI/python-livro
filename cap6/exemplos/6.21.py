tabela = {
    'alface': 0.45,
    'Batata': 1.20,
    'tomate': 2.30,
    'feijão': 1.50
}

while True:
    produto = input('Digite o nome do produto, fim para terminar: ')
    if produto == 'fim':
        break
    if produto in tabela:
        print(f'Preço {tabela[produto]:.2f}')
    else:
        print('Produto não encontrado! ')