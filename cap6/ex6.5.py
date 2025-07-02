#FIFO

pessoas = 10
fila = list(range(1, pessoas + 1))

while True:
    print(f'Fila atual {fila}')
    print('1 - Adicionar pessoa ao fim da fila\n2 - Realizar um atendimento\n3 - Sair do programa')

    op = int(input('Digite sua opção: '))

    op1 = str(op)

    if len(op1) == 1:
        if op == 1:
            pessoas += 1
            fila.append(pessoas)
            print(f'Pessoa {pessoas} adicionado a fila...')
        elif op == 2:
            if len(fila) > 0:
                primeiro = fila.pop(0)
                print(f'Pessoa {primeiro} removido da fila...')
            else:
                print('A fila está vazia! ')

        elif op == 3:
            print('Saindo do programa...')
            break

        else:
            print('ERRO! Digite apenas as opções disponiveis! ')
    else:
        qtd1 = str(op).count('1')
        qtd2 = str(op).count('2')

        for c in range(qtd1):
            pessoas += 1
            fila.append(pessoas)
            print(f'Pessoa {pessoas} adicionado a fila...')   
        for c in range(qtd2):
            if len(fila) > 0:
                primeiro = fila.pop(0)
                print(f'Pessoa {primeiro} removido da fila...')
            else:
                print('A fila está vazia! ')
        if '3' in str(op):
            print('Saindo do programa...')
            break 
        else:
            print('ERRO! Digite apenas as opções disponiveis! ')

    
