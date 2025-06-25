plano = input('Qual é o plano de celular? ')
if plano == 'falopouco':
    minutosDoPlano = 100
    extra = 0.20
    preco = 50
if plano == 'falomuito':
    minutosDoPlano = 500
    extra = 0.15
    preco = 99
if plano != 'falopouco' and plano != 'falomuito':
    print('Não conheço esse plano')
if plano == 'falopouco' or plano == 'falomuito':
    minutosConsumidos = int(input('Quantos minutos vc consumiu? '))
    print('Você vai pagar: ')
    print(f'Preço do plano: R${preco:10.2f}')
    suplemento = 0
    if minutosConsumidos > minutosDoPlano:
        suplemento = extra * (minutosConsumidos - minutosDoPlano)
    print(f'Suplemento R${suplemento:10.2f}')
    print(f'TOTAL: R${preco + suplemento:10.2f}')