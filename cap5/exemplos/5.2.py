tabuada = 1

while tabuada <= 10:
    numero = 1
    while numero <= 10:
        print(f'{numero} x {tabuada} = {numero * tabuada}')
        numero += 1
    tabuada += 1
    print('-' * 10)