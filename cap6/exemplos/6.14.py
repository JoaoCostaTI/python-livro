compras = []

while True:
    produto = input('Produto: ')
    if produto == 'fim':
        break
    compras.append(produto)
for p in compras:
    print(p)