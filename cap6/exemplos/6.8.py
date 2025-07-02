#LIFO

"""
pratos = [1,2,3,4]

# ultimo elemento a entrar, é o primeiro a sair
print(pratos[-1])

#Adicionando um elemento na ultima posição
pratos.append(5)
print(pratos[-1])

#removendo um elemento da ultima posição
pratoRemovido = pratos.pop(-1)
print(pratoRemovido)
"""

prato = 5
pilha = list(range(1, prato + 1))

while True:

    print(f'Lista de Pratos: {pilha}')

    print('A - Adicionar Prato\nR - Remover Prato\nS - Sair do programa')

    op = str(input('Sua opção: '))

    if op == 'A':
        prato += 1
        pilha.append(prato + 1)
        
        
    elif op == 'R':
        removido = pilha.pop(-1)
        print(f'Prato {removido} removido da pilha')
    elif op == 'S':
        print('Saindo do Programa...')
        break
    else:
        print('Escolher apenas as opções acima! ')