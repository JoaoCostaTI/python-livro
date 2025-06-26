listaCompleta = []

for c in range(1,11):
    n = int(input('Digite um numero: '))
    listaCompleta.append(n)

semRepetidos = list(set(listaCompleta))

for c in semRepetidos:
    print(f'{c} aparece {listaCompleta.count(c)}x')
