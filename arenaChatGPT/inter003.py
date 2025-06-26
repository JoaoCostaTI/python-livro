nPares = []
nImpares = []

while True:
    n = int(input('Numero: '))

    if n == 0:
        print('Saindo do programa...')
        break

    elif n % 2 == 0:
        nPares.append(n)
    else:
        nImpares.append(n)

print(f'Soma: {sum(nPares)} números Pares\nLista completa com eles: {nPares}\nSoma: {sum(nImpares)} números Impares\nLista completa com eles: {nImpares}')