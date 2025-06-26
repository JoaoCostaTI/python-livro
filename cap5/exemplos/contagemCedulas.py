valor = int(input('Digite o valor a pagar: '))
cedulas = 0
atual = 50
aPagar = valor

while True:
    if atual <= aPagar:
        aPagar -= atual
        cedulas += 1
    else:
        print(f'{cedulas} cédula(s) de R${atual}')
        if aPagar == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0
