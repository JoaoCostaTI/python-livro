estoque = {
    'alface': [1000, 0.45],
    'batata': [500, 1.20],
    'tomate': [2001, 2.30],
    'feijão': [100, 1.50]
}  
venda = [["tomate",5],["batata",10],["alface",500]]
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
for chave, dados in estoque.items():
    print(f'Descrição: {chave}')
    print(f'Quantidade: {dados[0]}')
    print(f'Preço: {dados[1]:.2f}')
