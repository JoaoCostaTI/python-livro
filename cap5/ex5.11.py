depositoInicial = float(input('Deposito Inicial: R$'))
taxaDeJuros = float(input('Taxa de Juros: '))

mes = 1
rendimento = depositoInicial

while mes <= 24:
    rendimento += (rendimento * taxaDeJuros) / 100
    print(f'No {mes}º mes renderá = R${rendimento:8.2f}')

    mes += 1
print(f'O ganho obtido em juros foi: R${rendimento-depositoInicial:.2f}')

