#FIFO
#Comando A = Adicionar pessoa FILA 1
#Comando F = Atender pessoa FILA 1

#Comando B = Adicionar FILA 2
#Comando G = Atender pessoa FILA 2


pessoas1 = 10
pessoas2 = 5
fila1 = list(range(1, pessoas1 + 1))
fila2 = list(range(1, pessoas2 + 1))

while True:

    print('A - FILA 1\nB - FILA 2\nC - Sair do programa')

    op = input('Qual fila de atendimento?')

    if op == 'A':
        fila = fila1

        while True:
            print(f'Fila atual {fila}')
            print('1 - Adicionar pessoa ao fim da fila\n2 - Realizar um atendimento\n3 - Voltar menu Filas')

            op = int(input('Digite sua opção: '))

            op1 = str(op)

            if len(op1) == 1:
                if op == 1:
                    pessoas1 += 1
                    fila.append(pessoas1)
                    print(f'Pessoa {pessoas1} adicionado a fila...')
                elif op == 2:
                    if len(fila) > 0:
                        primeiro = fila.pop(0)
                        print(f'Pessoa {primeiro} removido da fila...')
                    else:
                        print('A fila está vazia! ')

                elif op == 3:
                    print('Voltando menu Filas...')
                    break

                else:
                    print('ERRO! Digite apenas as opções disponiveis! ')
            else:
                qtd1 = str(op).count('1')
                qtd2 = str(op).count('2')

                for c in range(qtd1):
                    pessoas1 += 1
                    fila.append(pessoas1)
                    print(f'Pessoa {pessoas1} adicionado a fila...')   
                for c in range(qtd2):
                    if len(fila) > 0:
                        primeiro = fila.pop(0)
                        print(f'Pessoa {primeiro} removido da fila...')
                    else:
                        print('A fila está vazia! ')
                if '3' in str(op):
                    print('Voltando menu Filas...')
                    break 
                else:
                    print('ERRO! Digite apenas as opções disponiveis! ')
    elif op == 'B':
        fila = fila2
        while True:
            print(f'Fila atual {fila}')
            print('1 - Adicionar pessoa ao fim da fila\n2 - Realizar um atendimento\n3 - Voltar menu Filas')

            op = int(input('Digite sua opção: '))

            op1 = str(op)

            if len(op1) == 1:
                if op == 1:
                    pessoas2 += 1
                    fila.append(pessoas2)
                    print(f'Pessoa {pessoas2} adicionado a fila...')
                elif op == 2:
                    if len(fila) > 0:
                        primeiro = fila.pop(0)
                        print(f'Pessoa {primeiro} removido da fila...')
                    else:
                        print('A fila está vazia! ')

                elif op == 3:
                    print('Voltando menu Filas...')
                    break

                else:
                    print('ERRO! Digite apenas as opções disponiveis! ')
            else:
                qtd1 = str(op).count('1')
                qtd2 = str(op).count('2')

                for c in range(qtd1):
                    pessoas2 += 1
                    fila.append(pessoas2)
                    print(f'Pessoa {pessoas2} adicionado a fila...')   
                for c in range(qtd2):
                    if len(fila) > 0:
                        primeiro = fila.pop(0)
                        print(f'Pessoa {primeiro} removido da fila...')
                    else:
                        print('A fila está vazia! ')
                if '3' in str(op):
                    print('Voltando menu Filas...')
                    break 
                else:
                    print('ERRO! Digite apenas as opções disponiveis! ')
    elif op == 'C':
        print('Saindo do programa...')
        break
    else:
        print('ERRO! Selecione apenas as opções disponiveis.  ')
