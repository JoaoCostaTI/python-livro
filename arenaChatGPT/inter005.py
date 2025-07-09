produtos = {}
listaProdutos = []

for p in range(5):
    produtos['nome'] = str(input('Nome do produto: '))
    produtos['preco'] = float(input(f'Preço de {produtos['nome']} R$'))

    listaProdutos.append(produtos.copy())

print('---Produtos cadastrados---')
for c in listaProdutos:
    print(f'Nome: {c['nome']} - R${c['preco']:.2f}')

print('Produtos que custam mais de R$50,00')
for c in listaProdutos:
    if c['preco'] > 50:
        print(f'Nome: {c['nome']} - R${c['preco']:.2f}')