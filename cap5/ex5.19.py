valor = float(input('Digite o valor a pagar: '))
dinheiro = 0
atual = 100
aPagar = valor

while True:
    if valor < 0.01:
        print('Erro, valor abaixo de 1 centavo não é aceito! ')
        break
    else:
        if atual <= aPagar:
            aPagar -= atual
            dinheiro += 1
            aPagar = round(aPagar, 2)
        else:
            print(f'{dinheiro} cédula(s) de R${atual}')
            if aPagar == 0:
                break
            if atual == 100:
                atual = 50
            elif atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            elif atual == 1:
                atual = 0.50
            elif atual == 0.50:
                atual = 0.10
            elif atual == 0.10:
                atual = 0.05
            elif atual == 0.05:
                atual = 0.02
            elif atual == 0.02:
                atual = 0.01
            dinheiro = 0