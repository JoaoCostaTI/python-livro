
listaCompleta = []

while True:
    n = int(input('Digite um numero: '))

    if n == 0:
        print('Saindo do Programa...')
        break
    #Adicionando na lista se não estiver adicionado.
    if n not in listaCompleta:
        listaCompleta.append(n)

print(f'Lista completa Ordenada: {sorted(listaCompleta)}\nQuantidade de números válidos: {len(listaCompleta)}')