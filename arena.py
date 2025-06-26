nInicial = int(input('Numero inicial: '))
nFinal = int(input('Numero Final: '))

nPares = []



for c in range(nInicial, nFinal+1):
    if c % 2 == 0:
        nPares.append(c)
print(nPares) 