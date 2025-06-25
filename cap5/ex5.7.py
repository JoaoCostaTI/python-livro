n = int(input('Tabuada de: '))

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))

while inicio <= fim:
    print(f'{n} x {inicio} = {inicio*n}')
    inicio += 1