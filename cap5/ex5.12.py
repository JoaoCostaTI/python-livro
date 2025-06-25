depositoInicial = float(input('Deposito Inicial: R$'))
taxaDeJuros = float(input('Taxa de Juros: '))

mes = 1
rendimento = depositoInicial
depositoMes = 0
depositoMesAcumulado = 0

while mes <= 5:
    rendimento = rendimento + (rendimento * taxaDeJuros) / 100
    print(f'No {mes}º mes renderá = R${rendimento:8.2f}')
    mes += 1

    depositoMes = float(input('Deseja depositar algo? R$'))
    rendimento += depositoMes
    depositoMesAcumulado += depositoMes

print(f'O ganho obtido em juros foi: R${rendimento-depositoInicial-depositoMesAcumulado:.2f}')
