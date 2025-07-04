p1 = ['maçã', 10, 0.30]
p2 = ['Pera', 8, 1.30]
p3 = ['Kiwi', 15, 8.30]

compras = [p1,p2,p3]
print(compras)

for p in compras:
    print('-'*15)
    print(f'Produto: {p[0]}')
    print(f'Quantidade em estoque: {p[1]}')
    print(f'Preço: R${p[2]:.2f}')
    print('-'*15)