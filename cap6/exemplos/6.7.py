ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f'\nExistem {len(fila)} clientes na fila...')
    print(f'Fila atual: {fila}')
    print('Digite F para adicionar um cliente ao fim da fila,')
    print('ou A para realizar o atendimento. S para sair.')
    op = input('Operação (F, A ou S): ')

    if op == 'A':
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f'Cliente{atendido} atendido')
        else:
            print('Fila vazia! Ninguém para atender.')
    elif op == 'F':
        ultimo += 1
        fila.append(ultimo)
    elif op == 'S':
        break
    else:
        print('Operação inválida! Digite APENAS (F, A ou S) !!!')