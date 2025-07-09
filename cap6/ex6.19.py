estoque = {
    'alface': [1000, 0.45],
    'batata': [500, 1.20],
    'tomate': [2001, 2.30],
    'feijão': [100, 1.50]
}  
def estoqueProdutos():
    print('- Produto - Quantidade - Valor')
    for p, i in estoque.items():
        print(f'- {p:<9} {i[0]:<12} {i[1]}')
estoqueProdutos()

produto = str(input('Qual produto comprar: '))

if produto in estoque:
    quantidade = int(input('Quantidade: '))
    venda = [[produto, quantidade]]
    total = 0
    print('Vendas:\n')
    for op in venda:
        produto, quantidade = op
        preco = estoque[produto][1]
        custo = preco * quantidade
        print(f'{produto:12s}: {quantidade:3d} x {preco:.2f} = {custo:.2f}')
        estoque[produto][0] -= quantidade
        total += custo
        print(f'Custo total = {total:.2f}\n')
        print(f'Estoque:\n')
    estoqueProdutos()


else:
    print('Produto não encontrado! Selecione apenas os itens existentes.')
