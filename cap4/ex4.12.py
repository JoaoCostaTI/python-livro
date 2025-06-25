qtdKWh = int(input('Quantidade gasta de kWh: '))
tipoInstalacao = str(input('Qual tipo de instalação: '))
preco = 0

if tipoInstalacao == 'R':
    if qtdKWh <= 500:
        preco = qtdKWh * 0.40
    else:
        preco = qtdKWh * 0.65
elif tipoInstalacao == 'C':
    if qtdKWh <= 1000:
        preco = qtdKWh * 0.55
    else:
        preco = qtdKWh * 0.60
else:
    if qtdKWh <= 5000:
        preco = qtdKWh * 0.55
    else:
        preco = qtdKWh * 0.60

print(f'Tipo de instalação: {tipoInstalacao}\nGasto de {qtdKWh}kWh\nValor total: R${preco:.2f}')
