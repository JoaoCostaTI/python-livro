lugaresVagos = [10,2,0,3,0]
ingressosVendidos = [0,0,0,0,0]

print(f'Salas disponiveis: {len(lugaresVagos)}')

while True:
    #Controle das salas e vagas disponiveis
    print('-' * 20)
    for sala, vagas in enumerate(lugaresVagos):
        if vagas > 0:
            print(f'Sala {sala + 1} - Vagas: {vagas}')
    print('-' * 20)

    #Selecionando a sala especifica
    sala = int(input('Sala (0 sai): '))

    #Saindo do programa 
    if sala == 0:
        print('FIM...')
        break   

    #tratamento de erro caso seja selecionado uma sala que não existe
    if sala > len(lugaresVagos) or sala < 1:
        print('Sala inválida! ')

    #tratamento de erro caso a sala não tenha o numero de vaga desejado
    elif lugaresVagos[sala -1] == 0:
        print('Desculpe, sala lotada!')
    
    else:
        lugares = int(input(f'Quantos lugares você deseja ({lugaresVagos[sala - 1]} vagos): '))

        if lugares > lugaresVagos[sala - 1]:
            print('Esse numero de lugares  não está disponivel.')
        elif lugares < 0:
            print('Numero inválido!')
        else:
            #calculando ingressos vendidos por sala
            ingressosVendidos[sala - 1] += lugares

            lugaresVagos[sala - 1] -= lugares
            print(f'{lugares} lugares vendidos')

print('Utilização das salas')
for sala, vagos in enumerate(lugaresVagos):
    print(f'Sala {sala + 1} - [{vagos}] lugar(es) vazio(s)')

print('Controle de ingressos Vendidos por sala')
totalIngressos = 0
for sala, ingressos in enumerate(ingressosVendidos):
    print(f'Sala {sala + 1} - [{ingressos}] ingressos vendidos.')
    totalIngressos += ingressos
print(f'Total de ingressos vendidos: {totalIngressos}')