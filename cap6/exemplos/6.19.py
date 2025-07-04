compras = []

while True:
    produto = input('Produto: ')
    if produto == 'fim':
        break
    qtd = int(input('Quantidade: '))
    preco = float(input('Preço: '))
    compras.append([produto,qtd,preco])
soma = 0.0
for p in compras:
    print(f'{p[0]:20s} x {p[1]:5d} {p[2]:5.2f} {p[1] * p[2]:6.2f}')
    soma += p[1] * p[2]
print(f'Total: R${soma:7.2f}')