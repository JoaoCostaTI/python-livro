vel = float(input('Qual foi a velocidade do carro: '))

if vel > 80:
    print('Você foi multado! ')
    multa = (vel - 80) * 5
    print(f'O valor da sua multa foi: R${multa:.2f}')
else:
    print('Você andou no limite da via, parabéns! ')